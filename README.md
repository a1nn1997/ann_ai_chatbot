# ANN AI Chatbot

## Overview
This Django-based project integrates an NLTK-powered chatbot with WebSocket for real-time communication and uses PostgreSQL for data storage. Celery is used for background tasks like continuous training of the chatbot model.


## Features
- Real-time chat interface with WebSocket
- Custom AI chatbot model using ChatterBot
- PostgreSQL for session and user data storage
- Celery for asynchronous tasks like chatbot training

## Installation

### Prerequisites
- Python 3.x
- Docker
- PostgreSQL

### Setup
Clone the repository:
```bash
git clone https://github.com/a1nn1997/ann_ai_chatbot.git
cd ann_ai_chatbot
