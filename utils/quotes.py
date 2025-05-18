# utils/quotes.py - Motivational quotes utilities

import random

# Motivational quotes data
QUOTES = [
    "The secret of getting ahead is getting started. - Mark Twain",
    "It always seems impossible until it's done. - Nelson Mandela",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "The future depends on what you do today. - Mahatma Gandhi",
    "You've got this! Keep up the momentum.",
    "Small breaks lead to big productivity gains. Now back to being awesome!",
    "One step at a time. You're making progress.",
    "Focus on progress, not perfection.",
    "Every accomplishment starts with the decision to try."
]

def get_random_quote():
    """Return a random motivational quote"""
    return random.choice(QUOTES)