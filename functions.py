import requests


def lucky_number(dicio):
    numbers = dicio["dezenasSorteadasOrdemSorteio"]
    series = [numbers[0], numbers[1]]
    num_values = []
    lucky = ""
    for i in range(len(series)):
        num_values.append(series[i][-2])
    num_values.append("-")
    for j in range(len(numbers)):
        num_values.append(numbers[j][-1])
    for x in range(len(num_values)):
        if x == 0:
            lucky = num_values[0]
        elif x > 0:
            lucky += num_values[x]
    if int(lucky[0:2]) > 49:
        res = int(lucky[0:2]) - 50
        if res < 10:
            lucky = "0" + str(res) + lucky[-6:]
        else:
            lucky = str(res) + lucky[-6:]
    return lucky


def extract_numbers(num):
    # print("{} e {}".format(type(num), num))
    PARTE1 = "http://loterias.caixa.gov.br"
    PARTE2 = "pw/Z7_HGK818G0KG4QF0QLDEU6PK2084/res/id=buscaResultado/c=cacheLevelPage//p=concurso=%s" % num
    PARTE3 = "?timestampAjax=1635253053524"
    response = requests.get("http://loterias.caixa.gov.br/wps/portal/loterias/landing/federal")
    conteudo_site = response.headers["IBM-Web2-Location"]
    url = PARTE1 + conteudo_site + PARTE2 + PARTE3
    # print("{}".format(url))
    response = requests.get(url)
    ret = response.json()
    return ret
