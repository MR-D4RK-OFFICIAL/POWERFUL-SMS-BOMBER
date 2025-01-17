import requests
from bs4 import BeautifulSoup
import time

# Function: Fetch HTML Content from URL
def fetch_html(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"[!] Error Fetching URL: {e}")
        return None

# Function: Scrape Public Profile Information
def scrape_profile(url):
    html_content = fetch_html(url)
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        print(f"\n[+] Scraping Data from: {url}\n")

        # Extracting Profile Name or Title
        try:
            name = soup.find('title').text.strip()
            print(f"Name/Title: {name}")
        except AttributeError:
            print("Name not found.")

        # Extracting Meta Description
        try:
            meta_desc = soup.find('meta', attrs={'name': 'description'})['content']
            print(f"Description: {meta_desc}")
        except (AttributeError, TypeError):
            print("Description not found.")

        # Extracting Links
        try:
            links = [a['href'] for a in soup.find_all('a', href=True)]
            print(f"Total Links Found: {len(links)}")
        except Exception:
            print("No links found.")

# Function: Scrape Posts (for public post URLs)
def scrape_posts(url):
    html_content = fetch_html(url)
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        print(f"\n[+] Scraping Posts from: {url}\n")

        # Example: Extracting post content or text
        try:
            posts = soup.find_all('p')  # Adjust tag according to platform
            for idx, post in enumerate(posts[:5], 1):  # Limiting to first 5 posts
                print(f"[Post {idx}] {post.text.strip()}\n")
        except Exception:
            print("No posts found.")

# Function: Send API Requests
def api_request(api_url, payload=None):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Content-Type': 'application/json'
        }
        if payload:
            response = requests.post(api_url, json=payload, headers=headers)
        else:
            response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            print(f"\n[+] API Response: {response.json()}\n")
        else:
            print(f"[!] API Error: {response.status_code}")
    except Exception as e:
        print(f"[!] API Request Error: {e}")

# Function: Delay Between Requests
def delay(seconds):
    print(f"\n[+] Waiting for {seconds} seconds...")
    time.sleep(seconds)

# Display Logo & Developer Information
def display_logo():
    logo = """
\033[1;92m========================================
SOCIAL MEDIA SCRAPER TOOL
========================================
    """
    print(logo)

    developer_info = """
\033[1;94m[+]=====================================[+]
\033[1;32m[+] DEVELOPED BY: MR-D4RK
\033[1;32m[+] TOOL VERSION: 1.0
\033[1;32m[+] GITHUB: https://github.com/MR-D4RK-OFFICIAL
\033[1;32m[+] FACEBOOK:MD SOFIKUL ISLAM
\033[1;94m[+]=====================================[+]
    """
    print(developer_info)

# Main Program
def main():
    display_logo()

    print("""
    \033[1;92m========================================
    1. Scrape Public Profile
    2. Scrape Public Posts
    3. Send API Request
    4. Exit
    \033[1;30m""")

    while True:
        choice = input("\nEnter Your Choice (1/2/3/4): ")
        if choice == '1':
            profile_url = input("Enter Profile URL: ")
            scrape_profile(profile_url)
        elif choice == '2':
            post_url = input("Enter Post URL: ")
            scrape_posts(post_url)
        elif choice == '3':
            api_url = input("Enter API URL: ")
            payload = input("Enter Payload (JSON format, leave empty if GET): ")
            if payload.strip():
                try:
                    payload = eval(payload)  # Convert string to dictionary
                except Exception:
                    print("[!] Invalid Payload Format!")
                    continue
            else:
                payload = None
            api_request(api_url, payload)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid Choice. Try Again.")

# Run Program
if __name__ == "__main__":
    main()
