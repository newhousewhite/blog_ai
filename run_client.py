import requests
import json


# title
url_root = "https://f24f-2606-8e80-2800-8700-724d-7bff-fe2c-d463.ngrok-free.app"
query = """내가 다녔던 대학원 USC에서 여름마다 열리는 행사가 있다.
정부 펀딩으로 한국 대학생들이 이곳에 와서 2주간 데이터과학과 인공지능 교욱을 받는다.
대학교/대학원 레벨의 수업과 현직자 세미나를 듣는다.
이런 뜻깊은 행사에서 지난 몇 년간 세미나를 해왔고, 감사하게도 올 해도 초대를 받았다.
이렇게 타지에서 새로운 경험을 하는 학생들을 보면 비슷한 내 지난 추억이 떠오른다.
그때가 내 인생의 여름이었나 보다.  전국에서 모인 친구들을 사귀며 즐거운 시간을 보냈다.
내 껍질을 깨고 나오는 시간이었다.  행복한 기억들이 넘친다.
세미나를 시작하기 전 학생들 앞에서 첫인사를 할 때, 그들의 미래가 겹쳐 보이며 나도 모르게 설레었다.
            
이런 학생과의 만남은 나에게도 도움이 된다.  내 지식과 경험을 타인에게 소개하는 기회가 흔치 않기 때문이다.
회사 동료에게 하는 발표나 학회장에서의 발표와는 그 성격이 다르다.
더 쉽게 풀어내야 하고, 더 짧은 시간에 가깝게 연결될 수 있는 지점을 고민하고 찾아야 한다.
이런 만남은 일회성 이벤트가 아닌 시작이며, 그들 중 누군가와 계속 연락하며 돕고 지지하는 관계로 발전되기도 한다.
어느덧 그렇게 이어진 학생이 수백 명이나 되었다.
            
며칠 전 세미나에서는 내가 누구인지, 무슨 일을 했는지를 짧게 30분 이내로 설명했고, Q&A 시간을 오래 가졌다.
처음에는 망설였지만 점점 질문하는 손이 올라온다.  그리고 솔직한 질문도 나오기 시작한다.
조심스러울 수도 있는 질문이 과감하게 던져지는 순간, '아! 오늘 성공인가?' 하고 생각하게 된다.
궁금한 것을 있는 그대로 솔직하게 말하는 질문이 가장 좋다고 생각한다.  굳이 빙빙 돌아가거나 멋있게 포장할 필요가 없다.
진솔한 질문이 가장 좋은 질문이다.  이렇게 만나기 어렵고 처음 보는 사람에게 그런 질문을 할 수 있어야 하고,
나 스스로가 그런 질문을 해도 충분히 괜찮은 사람으로 느껴져야 한다.
어쩌면 그 30분의 발표는 Q&A 시간을 알차게 만들기 위한 발판일 수도 있다.
"""

type = "title"

url = url_root + "/" + type

headers = {
    "Content-Type": "application/json; charset=utf-8"
}

data_payload = {
    "text": query,
    "type": type
}

response = requests.post(url, json=data_payload, headers=headers)

if response.status_code == 200:
    print(json.loads(response.text)["llm_output"])
