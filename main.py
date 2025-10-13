from ai_core import SelfImprovingAI
from data_fetcher import fetch_random_image_and_word

def run_ai_simulation(num_rounds=10):
    """
    Main function to run the AI simulation.
    It loops through a number of rounds, allowing the AI to learn.
    """
    ai = SelfImprovingAI()
    
    for i in range(num_rounds):
        print(f"\n{'='*20} Round {i+1} {'='*20}")
        
        image, correct_word = fetch_random_image_and_word()
        if not image:
            continue
            
        # AI makes a guess
        guess = ai.guess_word(image)
        print(f"AI: I guess the word is: '{guess}'.")
        
        # Self-improvement loop: Check performance and improve
        if guess == correct_word:
            print("AI: My guess was correct! I will reinforce this knowledge.")
        else:
            print(f"AI: My guess was wrong. The correct word was '{correct_word}'.")
            ai.improve(image, correct_word)

if __name__ == "__main__":
    # Ensure you have the necessary libraries installed:
    # pip install scikit-learn numpy requests pillow joblib
    
    run_ai_simulation(num_rounds=15)
