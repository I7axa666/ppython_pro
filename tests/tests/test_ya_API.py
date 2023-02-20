import unittest as ut
import requests


from settings import TOKEN_DISK
import time


class TestYaApi(ut.TestCase):
    ya_url = 'https://cloud-api.yandex.net'
    headers = {'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN_DISK}'}


    def test_auth(self):
        request = self.ya_url + '/v1/disk'
        res = requests.get(request, headers=self.headers)
        time.sleep(1)

        self.assertEqual(res.status_code, 200)

    @ut.expectedFailure
    def test_check_folder(self):
        request = self.ya_url + '/v1/disk/resources'
        params = {'path': 'folder_name'}
        res = requests.get(request, headers=self.headers, params=params)
        time.sleep(1)
        self.assertEqual(res.status_code, 200)


    def test_create_folder(self):
        request = self.ya_url + '/v1/disk/resources'
        params = {'path': 'folder_name'}
        res = requests.put(request, headers=self.headers, params=params)
        time.sleep(1)
        self.assertEqual(res.status_code, 201)


if __name__ == '__main__':
    ut.main