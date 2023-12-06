from rest_framework import viewsets
from rest_framework.response import Response
from chatbot.models import ChatSession, Message, MessageResponse
from chatbot.serializers import MessageSerializer
from chatbot.utils import generate_chat_pairs
from nltk.chat.util import Chat, reflections  # Example, customize based on your NLTK model
from chatbot_app.decorators import authorize

class ChatSessionView(viewsets.ViewSet):
    """
    A simple ViewSet for handling chat messages.
    """

    @authorize
    def create(self, request):
        
        # Create a new chat session
        user = request.user
        session = ChatSession.objects.create(user=user)

        # Process user input
        user_input = request.data.get('message')
        bot_response = self.get_bot_response(user_input)

        # Save the message and response to the database
        Message.objects.create(session=session, text=user_input, user=user)
        Message.objects.create(session=session, text=bot_response, user=user, message_type=Message.BOT)  # Assuming bot has no user

        return Response({'response': bot_response})

    def get_bot_response(self, user_input):
        data = list(MessageResponse.objects.all().values('input_text', 'output_text'))
        train_data = [(mr['input_text'], mr['output_text']) for mr in data]
        chat = Chat(train_data, reflections)  # Replace with your trained pairs and logic
        response = chat.respond(user_input)
        if not response:
            train_data = generate_chat_pairs(1, [user_input])
            MessageResponse.objects.create(input_text=train_data[0][0], output_text=train_data[0][1])  
            return self.get_bot_response(user_input)
        else:
            return response

