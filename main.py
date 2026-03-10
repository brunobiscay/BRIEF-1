# import sentiment_api.py
# import sentiment_streamlit.py
# from sentiment_streamlit import run_web
# from sentiment_api import back_api_analyse_sentiment


# def main():
#    print("Hello from module-0-brief-1!")

#    back_api_analyse_sentiment()


# if __name__ == "__main__":
#    main()

# Source - https://stackoverflow.com/a/65375632
# Posted by Alcognito
# Retrieved 2026-03-10, License - CC BY-SA 4.0

import requests


def http_bin_repsonse(status_code):
    sc = status_code
    try:
        url = "http://httpbin.org/status/" + str(sc)
        response = requests.post(url)
        response.raise_for_status()

        p = response.content

    except requests.exceptions.RequestException as e:
        print("placeholder for save file / clean-up")
        raise SystemExit(e) from None

    return response, p


response, p = http_bin_repsonse(403)
print(p)
