import re
import requests

def get_beach_data(survey_location):
    
    if survey_location not in range(1, 6):
        raise ValueError("survey_location should be an integer 1, 2, 3, 4, or 5.")
    url = "http://narrabeen.wrl.unsw.edu.au/explore_data/time_series/"
    with requests.session() as s:
        cookies = dict(s.get(url).cookies.items())
        data = {
            "csrfmiddlewaretoken": cookies["csrftoken"],
            "profile": str(survey_location),
            "startDate": "27/04/1976",
            "endDate": "26/08/2020",
            "datatype": "WIDTH",
        }
        response = s.post(url, cookies=cookies, data=data, verify=False)
        return re.findall(r'new Date\("(.*)"\)\.getTime\(\), (\d+.\d)', response.text)