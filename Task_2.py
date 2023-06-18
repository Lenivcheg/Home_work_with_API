import requests

with open("token.txt", "r") as file:
    token_v1 = file.readline()


class YandexDisk:
    def __init__(self, token):
        self.token = token_v1

    def get_headers(self):
        return{
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        href = (response.json()["href"])
        response_put = requests.put(href, data=open(file_path, 'rb'))
        return response_put


Ya_upload = YandexDisk(token_v1)

Ya_upload.upload("file_for_yandeks_disc.txt")
