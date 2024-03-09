# Discord_bot

Lucifer's Discord Bot
Lucifer's Discord Bot is a versatile bot developed using discord.py, designed to enhance server management and provide various fun and utility features.

Features:
Moderation Commands: Includes commands like kick and ban for effective server moderation.
Avatar Retrieval: Retrieve user avatars with a simple command.
Music Playback: Play music from YouTube directly in Discord channels.
Voice Commands: Use voice commands to interact with the bot, including playing music and more.
Chatbot Functionality: Utilizes the OpenAI API to provide advanced chatbot capabilities for natural language interaction.
Automatic Message Sniping: Retrieves and displays recently deleted messages in the server.
Installation:
Clone the repository to your local machine.
Install the required dependencies using pip install -r requirements.txt.
Obtain the necessary API keys for OpenAI and Discord.
Create a file named api.py and add your API keys:
python
Copy code
apikey = 'your_discord_api_key'
apij = 'your_openai_api_key'
Run the bot using python bot.py.
Usage:
Use &hello command to greet the bot.
Use &dp command to retrieve a user's avatar.
Use &supporter command to get information on how to become a supporter.
Use &ad command to promote your server with a predefined advertisement message.
Use &kick and &ban commands for moderation purposes.
Use &music commands to control music playback in voice channels.
Use &snipe command to retrieve the last deleted message in a channel.
Contributing:
Feel free to contribute to this project by forking the repository and submitting pull requests.
