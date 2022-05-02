from typing import Union
import requests
from aiogram import types


def get_posts(
        vk_token: str, start_time: int
) -> Union[dict, None]:
    response = requests.get(
        "https://api.vk.com/method/newsfeed.get",
        params={
            "access_token": vk_token,
            "start_time": start_time,
            "v": 5.131,
            "filters": 'post'
        },
    )
    data = response.json()
    if "response" in data:
        return data["response"]["items"]
    return None


def get_photo_url_by_id(
        vk_token: str, owner_id, photo_id: str
) -> str:
    response = requests.get(
        "https://api.vk.com/method/photos.getById",
        params={
            "access_token": vk_token,
            "photos": str(owner_id) + '_' + str(photo_id),
            "extended": 1,
            "v": 5.131,
        },
    )
    data = response.json()
    return data["response"][0]["orig_photo"]["url"]


def get_video_url_by_id(
        vk_token: str, owner_id, video_id
) -> str:
    return "https://vk.com/video?z=" + str(owner_id) + "_" + str(video_id)


def media_attach_file(
        media: types.MediaGroup, attachment, vk_token: str, caption: str
):
    photo_type = "photo"
    video_type = "video"

    if attachment["type"] == photo_type:
        media.attach_photo(
            types.InputMediaPhoto(
                get_photo_url_by_id(
                    vk_token,
                    attachment["photo"]["owner_id"],
                    attachment["photo"]["id"]
                ),
                caption,
            )
        )
    elif attachment["type"] == video_type:
        media.attach_video(
            types.InputMediaVideo(
                get_video_url_by_id(
                    vk_token,
                    attachment["video"]["owner_id"],
                    attachment["video"]["id"]
                ),
                caption,
            )
        )
