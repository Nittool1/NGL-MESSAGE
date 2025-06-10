import requests
import time
import random
from colorama import Fore, Style, init
from pyfiglet import Figlet

# Initialize colorama
init(autoreset=True)

# Constants
API_URL = 'https://ngl.link/api/submit'
RANDOM_WORD_API = 'https://random-word-api.herokuapp.com/word?lang=en'
REQUEST_DELAY = 0.25  # seconds between requests

# Colors
G = Fore.GREEN
R = Fore.RED
Y = Fore.YELLOW
M = Fore.MAGENTA
C = Fore.CYAN
W = Fore.WHITE
B = Fore.BLUE

# Styles
BOLD = Style.BRIGHT
RESET = Style.RESET_ALL

# Banner
def show_banner():
    f = Figlet(font='small')
    print(f"{BOLD}{M}{f.renderText('NGL MISS YOU')}{RESET}")
    print(f"{BOLD}{Y}Created by: NIT HACK YOU{RESET}")
    print(f"{BOLD}{C}Version: 1000000.0{RESET}")
    print("-" * 50 + "\n")

# Random question generator with fallback
def random_question():
    fallback_words = [
        "hello Puk ah jmr", "Anh jng Hack", "python", "Miss u bee", "SL You",
        "question", "random", "DZ", "code", "HAHAAA",
        "what", "why o ?", "how", "when", "where", "I am Hacker"
    ]
    
    try:
        response = requests.get(RANDOM_WORD_API, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data[0].capitalize() + "?"
        return random.choice(fallback_words).capitalize() + "?"
    except:
        return random.choice(fallback_words).capitalize() + "?"

# Main function
def main():
    show_banner()
    
    print(f"{BOLD}{W}Enter target username:{RESET} ", end="")
    username = input().strip()
    
    print(f"\n{BOLD}{Y}Starting NGL MISS YOU...{RESET}")
    print(f"{BOLD}{C}Press CTRL+C to stop{RESET}\n")
    
    count = 0
    success_count = 0
    start_time = time.time()
    
    try:
        while True:
            count += 1
            question = random_question()
            
            try:
                payload = {
                    'username': username,
                    'question': question,
                    'deviceId': '',
                    'gameSlug': '',
                    'referrer': ''
                }
                
                response = requests.post(API_URL, data=payload)
                
                if response.status_code == 200:
                    status = f"{G}✓ Success{RESET}"
                    success_count += 1
                else:
                    status = f"{R}✗ Failed (HTTP {response.status_code}){RESET}"
                
                # Print status with nice formatting
                print(
                    f"[{BOLD}{M}{count}{RESET}] " +
                    f"Question: {BOLD}{W}{question.ljust(15)}{RESET} | " +
                    f"Status: {status} | " +
                    f"Success Rate: {BOLD}{Y}{(success_count/count)*100:.1f}%{RESET}"
                )
                
                time.sleep(REQUEST_DELAY)
                
            except requests.exceptions.RequestException as e:
                print(f"[{BOLD}{R}ERROR{RESET}] Connection problem: {e}")
                time.sleep(1)
                continue
                
    except KeyboardInterrupt:
        end_time = time.time()
        duration = end_time - start_time
        print(f"\n{BOLD}{R}Stopped by user{RESET}")
        print(f"{BOLD}{Y}Summary:{RESET}")
        print(f"- Total attempts: {BOLD}{count}{RESET}")
        print(f"- Successful sends: {BOLD}{G}{success_count}{RESET}")
        print(f"- Success rate: {BOLD}{Y}{(success_count/count)*100:.1f}%{RESET}")
        print(f"- Duration: {BOLD}{duration:.1f} seconds{RESET}")
        print(f"- Speed: {BOLD}{count/duration:.1f} requests/second{RESET}\n")
        print(f"{BOLD}{C}Thanks for using NGL Spammer!{RESET}")

if __name__ == "__main__":
    main()