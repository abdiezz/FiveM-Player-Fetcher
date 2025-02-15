import requests

def fetch_players(ip, port):
    url = f"http://{ip}:{port}/players.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        players = response.json()

        if not players:
            print("\nNo players found on this server.")
            return

        print("\n--- Player List ---")
        for player in players:
            print(f"Name: {player.get('name', 'Unknown')}")
            print(f"Ping: {player.get('ping', 'Unknown')} ms")
            print(f"ID: {player.get('id', 'Unknown')}")
            print("--------------------")
    except requests.exceptions.RequestException as e:
        print(f"\nError fetching player data: {e}")

if __name__ == "__main__":
    ip_address = input("Enter Server IP Address: ").strip()
    port = input("Enter Server Port: ").strip()
    fetch_players(ip_address, port)
