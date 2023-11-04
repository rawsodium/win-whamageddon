# win-whamageddon
A Python script that removes Wham's "Last Christmas" from any of your Spotify playlists.

# Files
- auth_flow.py
    Handles the generation of a code verifier and code challenge for PKCE authorization

- script.py
    Uses the PKCE auth flow to log the user into Spotify, then scrubs "Last Christmas" from the user's playlists
