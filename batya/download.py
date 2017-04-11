import urllib

def downloadAll():
    print("download Kody_ABC-3kh.csv")
    urllib.urlretrieve("https://www.rossvyaz.ru/docs/articles/Kody_ABC-3kh.csv","downloads/Kody_ABC-3kh.csv")
    print("success")

    print("download Kody_ABC-4kh.csv")
    urllib.urlretrieve("https://www.rossvyaz.ru/docs/articles/Kody_ABC-4kh.csv","downloads/Kody_ABC-4kh.csv")
    print("success")

    print("download Kody_ABC-8kh.csv")
    urllib.urlretrieve("https://www.rossvyaz.ru/docs/articles/Kody_ABC-8kh.csv","downloads/Kody_ABC-8kh.csv")
    print("success")

    print("download Kody_ABC-9kh.csv")
    urllib.urlretrieve("https://www.rossvyaz.ru/docs/articles/Kody_DEF-9kh.csv","downloads/Kody_ABC-9kh.csv")
    print("success")


if __name__ == "__main__":
    downloadAll()

