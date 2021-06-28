import py_avataaars as pa


def save_avatar(avatar: pa.PyAvataaar, file_name: str):
    avatar.render_png_file(file_name)


def generate_avatar(**kwargs) -> pa.PyAvataaar:
    avatar: pa.PyAvataaar = None
    try:
        if len(kwargs) > 0:
            avatar=pa.PyAvataaar(**kwargs)
        else:
            avatar = pa.PyAvataaar()
    except:
        print("Try again")
    return avatar


if __name__ == "__main__":
    avatar = generate_avatar(style=pa.AvatarStyle.TRANSPARENT, skin_color=pa.SkinColor.BROWN, clothe_type=pa.ClotheType.BLAZER_SWEATER, hair_color=pa.HairColor.BLACK, accessories_type=pa.AccessoriesType.WAYFARERS, mouth_type=pa.MouthType.DISBELIEF)
    save_avatar(avatar, "AVATAR.png")
