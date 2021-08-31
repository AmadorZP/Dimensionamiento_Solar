import os, json, requests

lon = -95.770
lat = 32.929

start_year = 2012
end_year = 2019

output = r""
base_url = r"https://power.larc.nasa.gov/api/temporal/monthly/point?parameters=T2M,ALLSKY_SFC_SW_DWN&community=RE&longitude={longitude}&latitude={latitude}&start={start}&end={end}&format=JSON"


def request_api(latitude, longitude):
    api_request_url = base_url.format(longitude=longitude, latitude=latitude, start=start_year, end=end_year)
    response = requests.get(url=api_request_url, verify=True, timeout=30.00)

    content = json.loads(response.content.decode('utf-8'))
    # guardar el archivo json
    filename = "MonthlyData_from" + str(start_year) + "to" + str(end_year)
    filepath = os.path.join(output, filename)
    with open(filepath, 'w') as file_object:
        json.dump(content, file_object)


request_api(lat, lon)
