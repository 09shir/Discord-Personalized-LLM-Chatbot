# Discord Personalized LLM Chatbot

A discord bot featuring 
- an LLM chatbot fine-tuned to mimic my voice
- a fine-tuned image generator that can generate faces of mine whenever you ask for my photo

## Behind the Scene

**LLM Model**: Fine-tuned Llama2 7B Neuron using AWS SageMaker on AWS Trainium ml.g5.12xlarge instances, deployed and hosted on AWS EC2 ml.g5.2xlarge instance, and accessed through FastAPI endpoint to discord.js

**Image Generator**: Fined-tuned, deployed and hosted Flux.1 dev model using Replicate, and accessed through FastAPI endpoint to discord.js