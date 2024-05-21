import os

from src.utils import get_youtube_data, create_database, save_data_to_database
from config import config

with open ('youtube_token.txt') as file:
    yt_api_key = file.read()

api_key_test = os.getenv('YT_API_KEY')


def main():
    channel_ids = [
        'UC-OVMPlMA3-YCIeg4z5z23A',  # moscowpython
        'UCwHL6WHUarjGfUM_586me8w',  # highload

    ]
    params = config()

    data = get_youtube_data(yt_api_key, channel_ids)
    create_database('youtube', params)
    save_data_to_database(data, 'youtube', params)


if __name__ == '__main__':
    main()