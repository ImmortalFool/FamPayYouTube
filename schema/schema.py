def individual_serializer(yt_data) -> dict:
    return{
        "_id": str(yt_data["_id"]),
        "vid": yt_data["vid"],
        "publishedAt": yt_data["publishedAt"],
        "title": yt_data["title"],
        "description": yt_data["description"],
        "thumbnails": yt_data["thumbnails"]
    }


def list_serial(yt_datas) -> list:
    return [individual_serializer(item) for item in yt_datas]
