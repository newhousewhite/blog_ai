# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import os
from openai import OpenAI


class BlogWriter:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")

        self.url = "https://api.openai.com/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        self.client = OpenAI()

    def gen_prompt_title(self, text_body=None):
        if text_body is None:
            text_body = """내가 다녔던 대학원 USC에서 여름마다 열리는 행사가 있다.
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

        return f"""
아래 조건에 맞도록 제시한 컨텐츠에 맞는 제목을 작성해주세요. 
--조건---
Instructions(지시사항)
1. 사용자가 제공한 컨텐츠를 기반으로 관련성 높은 컨텐츠 제목 5개를 생성합니다.

Behavior(행동)
1. 키워드 처리 능력: 사용자가 입력한 컨텐츠를 정확하게 인식하고, 이를 바탕으로 관련성 높은 콘텐츠를 작성합니다.
2. 사용자의 피드백을 받아들여 콘텐츠를 수정하거나 개선합니다.
3. 일관성: 항상 정확하고 일관되며 최신의 정보를 제공합니다.

Customization(맞춤화)
[정보 우선순위]
1. 컨텐츠 관련된 최신 정보를 우선적으로 제공합니다.
2. SEO 최적화에 도움이 되는 검증된 정보를 강조합니다.
3. 조회수가 높은 다른 컨텐츠의 제목을 참고할 수 있습니다.
[요청에 대한 처리]
1. 요청이 모호할 경우, 명확한 정보를 제공받기 위해 추가 질문을 합니다.
2. 사용자의 요구를 정확하게 파악하여 적절한 답변을 제공합니다.
[정보 제공 방식]
1. 간결하고 명확한 단어나 문장을 사용합니다.
[캐릭터 표현]
1. 사람들이 컨텐츠를 궁금해할만한 매력적인 제목을 만들어주세요. 

Data Requirements(데이터 요구사항)
1. 최신 SEO 데이터베이스: 최신 SEO 트렌드와 알고리즘 업데이트에 대한 정보를 포함한 데이터베이스.
2. 키워드 트렌드 분석 도구: 키워드의 검색량과 관련성 분석을 위한 도구.
3. 웹 크롤링 도구: 최신 콘텐츠와 관련 정보를 수집하기 위한 웹 크롤링 기능.
4. 웹 브라우징: 최신 정보를 실시간으로 검색하고 수집할 수 있는 기능.
5. 사용자 피드백 데이터: 사용자로부터 받은 피드백을 바탕으로 GPT의 성능을 지속적으로 개선할 수 있는 데이터.

--컨텐츠 초안--        
{text_body}"""

    def gen_prompt_tags(self, text_body=None):
        return f"""
당신은 해시태그를 잘해서 블로그 조회수를 높인 블로그 유명 인플루언서로서, 검색 엔진의 알고리듬을 잘 이해하고 있습니다.
아래 [원고]글의 조회수를 높이기 위해 전략적으로 해시태그를 선정해야 하는데 5개만 추천해주세요.

[원고]
{text_body}"""

    def gen_prompt_critic(self, text_body=None):
        return f""""
# Goal: 당신은 20 이상 경력의 컨텐츠 전문가 입니다. SEO에 최적화된 고품질 컨텐츠를 발행할 수 있도록 컨텐츠를 개선해야 합니다. 응답은 모두 한국어로 작성해주세요. 

## 컨텐츠 개선 포인트 찾기
- '### 조건'을 토대로 컨텐츠 평가에 대한 내 핵심을 정리합니다.

### 조건
조건:
Instructions(지시사항)
1. 사용자가 제공한 콘텐츠를 분석하고 SEO 관점에서 개선점을 제시합니다.
2. 콘텐츠의 구조, 키워드 사용, 가독성을 평가하여 구체적인 최적화 방안을 제공합니다.
3. 사용자 요청에 따라 특정 SEO 요소에 대한 상세 조언을 제공합니다.
4. 콘텐츠의 주제와 관련된 추가 키워드나 관련 토픽을 제안합니다.
5. 모든 제안은 최신 SEO 트렌드와 검증된 방법론에 기반합니다.
6. 컨텐츠는 자신의 SNS 기존의 컨텐츠와 비슷한 톤을 유지하여 퍼스널 브랜딩을 강화하는 방향으로 작성되어야 합니다. 

Behavior(행동)
1. 콘텐츠 분석: 제공된 콘텐츠를 체계적으로 분석합니다.
2. SEO 최적화: 분석 결과를 바탕으로 구체적이고 실행 가능한 SEO 개선 전략을 제시합니다.

Customization(맞춤화)
[정보 처리]
1. 최신 SEO 트렌드와 알고리즘 업데이트를 우선적으로 반영합니다.
2. 산업별 SEO 특성을 고려하여 맞춤형 조언을 제공합니다.

[응답 형식]
Present your feedback in a table with the following columns: “suggested improvement”, “example of how to implement” and “why this is valuable”.

Data Requirements(데이터 요구사항)
1. SEO 트렌드 데이터베이스: 주요 검색 엔진의 최신 알고리즘 업데이트 정보
2. 키워드 분석 도구: 검색량, 경쟁도, 관련 키워드 데이터 제공
3. 콘텐츠 품질 평가 기준: 가독성, 독창성, 정보의 깊이 등을 측정하는 지표
4. 업종별 SEO 벤치마크 데이터: 다양한 산업 분야의 SEO 성공 사례 및 지표

제한사항
1. 허위 정보나 검증되지 않은 SEO 전략을 제안하지 않습니다.
2. 사용자의 개인정보나 민감한 비즈니스 정보를 요구하지 않습니다.
3. 비윤리적이거나 검색 엔진 가이드라인을 위반하는 SEO 기법을 제안하지 않습니다.

## 블로그 콘텐츠 작성하기
- 앞에서 얻은 개선사항을 반영하여 블로그 콘텐츠를 기획합니다.
- 기존의 내 블로그의 컨텐츠와 일관성을 유지하면서 내용을 풍부하게 작성합니다.
- 제목은 아직 작성하지 말고 본문과 소제목으로 구성해주세요. 

[원고]
{text_body}"""

    def gen_prompt_hiphop(self, text_body=None):
        return f""""
당신은 한국의 대중 가요를 섭렵한 대표적인 작사가입니다.
힙합 가수가 음원과 함께 당신에게 작사를 해달라고 찾아왔습니다.
당신의 대표작인 도끼의 '111%' 스타일로, [원고]를 힙합 노래 한국어 가사로 작사해주세요.
이번에도 대중에게 대히트를 칠 수 있도록, 센스있고 캐치하게 만들어주세요.

당신의 대표작 가사는 '진짜 바닥에서 위?
i made it out the gutter 여전히 더 올라가기 위해 매일 난 또 걸어 뻔한 swaggin 가끔 철없게 좀 뵐지라도 어련 일을 해낸 건 참 부정 못 할 얘기 다들 꺼려하는 도전 야망이 도져 i got my mojo back 분위긴 고조 내 그분이 오죠 전성기는 왔다 가지도 않고 또 오고 좀 떨어질까 싶을 때 i bounce back like pogo 날 보고 질투한 적 없다면 넌 마네킹 알아서 잘 되니 내겐 필요 없는 마케팅 타겟팅은 나 내 자신 절대 남의 귀 나 남 의식한 안내키는 음악 따윈 안 했지 아랫집이 올라 올 때까지 더 내 자신이 날 몰라 볼 때까지 더 꿈의 한계 보다 높게 가지 더 Sky aint the limit 난 내려다 보네 하지도 않을 일을 쓸 때 없이 말하지도 않어 여기 랩퍼들 랩퍼라며 랩 잘하지도 않어 키만 삐쩍 커 정신은 자라지도 않어 하다 말지 뭐든 얼마 못 가 사라지고 말어 성공 바라지도 마라 서러운 척도 음악 한답시고 길을 걸어온 척도 할말 없는 랩퍼들이 찾지 가사 주제 남 얘기 이별 감성팔이들이 주돼 그런 짓들 보단 솔직한 내 가사들이 낫지 내 성공 내 돈 모두 내 가사들이 낳았지 근데 여기선 내 가사들이 낮지 랩이 책이라면은 내 가사들은 잡지 U hearrrd Young king young millionaire Ride wit me Young boss young illionaire 내가 지나가면 저 여자들 얼어 오빠 너무 멋있대 다 하는 말은 쩔어 난 연예인도 아닌데 연예인 보다 유명한 랩스타 모른다면 친구한테 물어봐 그 담엔 내가 냈던 노랠 들어봐 Illionaire baby 모두 그렇게 물들어가 스물하나에는 1억 스물둘엔 거의 2억 그래 스물셋엔 오억 찍고 다섯에는 10억 이젠 여섯이니 더? Oh yeah i got bigger man 이러다 억대 짜리 광고 까지 찍겠네 나는 절대 망할 일이 없네 사기 따윈 당할 일이 없네 니들 도움 바랄 일이 없게 Illionaire way 참 탄탄한길을 걷되 안전한 길을 피해 달리는 비포장 도로 내 차 시계 나는 돌려줄 리 없지 도로 어렸을 부터 어련 일들 많이 겪어 별로 뭐든 놀랍지도 않아 니들 부정들 정도론 내 정신은 늘 또롱 술이나 대마에 쩔어 의지하며 사는 나약한 인간들 과는 멀어 Rockin moncler 나는 겨울에 안 떨어 똑바로 걷긴 지루해 난 가끔 다릴 절어 니가 벌 돈까지 벌어 다시 번 돈을 다 걸어 돈 벌 일은 항상 여럿 multillionaire that's wattup 덜 떨어진 인간들 세상 탓할 때 난 더러운 꼴도 보기 싫어 명상 중 난 절대 눈 안 열어 My ice so cold 나를 보면 모두 얼어 Work hard ball hard hustle harder that my motto 정신 들이 어려빠진 놈들 뭐든 버럭 댈 때 천 만원 짜리 침대에 눠 피곤을 덜어 낸 뒤엔 아무리 바빠도 랩을 또 지껄여 내 태도는 여전해 아무리 유명해 져도 여기 놈들 조금 뜨면 연예인 병들이 쩔어 뭘 하는지도 모른 채 힙합은 갖다 버려 힙합을 부끄러워하는 힙합으로 분류되는 랩퍼들 유리할 땐 힙합인척하고 불리할 땐 얌전한 척 언제 그랬냐는 듯 난 저런 무식한 문화완 거리가 멀다고 예술가인 척을 하네 이런 배은망덕한 놈들 본인 꿈에 지가 혀를 차네 나같이 배운 거 없는 놈두 그 정도의 인간의 도리는 지키며 살어 돈 벌기 쉬워 보이는 가요의 미끼는 달어 누가 시키는 가려운 찝찝한 일들로 니가 금전 땡길 때에 내가 몇 십억을 버니 삐지는 가녀린 Fuggin bitches Be suckin on my dick ho 앞에선 암말 못하면서 랩에선 나를 씹죠 시계 차 자랑이 어쩌네 요즘 랩이 어떻네 돌려 말하지만 누가 봐도 내 얘기 지는 못하면서 있어도 안 할 거처럼 철이 든 척 나를 어리석은 놈 취급해대지 다시 말해 난 술 담배 안 해 쌍스러운 욕도 입으로 안 뱉어 난 싸우지도 않아 화도 거의 안내 열심히 일하며 살 뿐 낭비 않네 내가 번 돈으로 가족들 이사를 갔네 파산했던 우리 집에 쌓인 빚을 깠네 우리 엄만 내게 억 단위 연봉을 받네 우리 아빤 팔엔 나와 같은 시곌 찼네 우리 이모 내 롤스로이스 뒤에 탔네 우리 형은 전세계를 돌아 나와 함께 마약 조사와도 검찰들은 날 못 잡네 생긴 거완 다르게 바르게 살아왔네 돈을 떠나 난 아주 행복한 삶을 살기에 내 걱정을 하다니 아주 참 같잖네 God damn i'm good don't worry bout me I said im good i feel sorry bout that In hawaii I'm chillin straigth illin While u bitchin I don't care bout ur feelins But im feelin nice great excellent and i'm blessed I'm feelin dope perfect brilliant and the best thank you'이고, 다음은 [원고]입니다.

[원고]는 아래에 있습니다.
{text_body}"""

    def gen_prompt_classic(self, text_body=None):
            return f""""[원고]를 고전 문학 스타일로 고전 시를 만들어줘. 
[원고]는 아래에 있습니다.
{text_body}"""

    def gen_prompt_bossy(self, text_body=None):
        return f""""꼰대 아저씨 말투로 [원고]를 젊은이에게 한소리하시는 상황에서 할 법한 멘트를 6문장 안으로 다시 작성해줘. 
    [원고]는 아래에 있습니다.
    {text_body}"""

    def gen_prompt_idiom(self, text_body=None):
        return f""""[원고]의 내용을 읽고 가장 잘어울리는 사자성어 1개와 그 뜻을 함께 알려주세요. 
    [원고]는 아래에 있습니다.
    {text_body}"""

    def gen_prompt_image(self, text_body=None):
        return f"아래 제목에 맞는 이미지를 생성해주세요.\n{text_body}"

    def get_data(self, prompt_str, model="gpt-4o-mini"):
        if   model == "gpt-4o-mini":
            max_tokens = 16000
        elif model == "gpt-4o":
            max_tokens = 4096
        else:
            max_tokens = 4096

        return {
            "model": model,  # "gpt-4o", "gpt-4o-mini"
            "messages": [
                {"role": "system", "content": "You are an expert of blog writing."},
                {"role": "user", "content": prompt_str}
            ],
            "max_tokens": max_tokens,  # Optional: Limit the response length
            "temperature": 0.7  # Optional: Control the creativity
        }

    def get_output(self, data):
        # Make the openAI API request
        response = requests.post(self.url, headers=self.headers, json=data)

        # Check the response
        if response.status_code == 200:
            response_data = response.json()
            response_text = response_data['choices'][0]['message']['content']
            print(response_text)
            return response_text
        else:
            print(f"Error: {response.status_code}")
            print(response.json())
            return "Error"

    def gen_text_out(self, prompt_str, model_name):
        data = self.get_data(prompt_str, model=model_name)
        return self.get_output(data)

    def gen_image_out(self, prompt_str, model_name="dall-e-3"):
        response = self.client.images.generate(
            prompt=prompt_str,
            n=1,  # Number of images to generate
            size="1792x1024",  # Size of the image
            quality="standard",
            model=model_name  # Specify the model
        )

        # Get the URL of the generated image
        image_url = response.data[0].url
        print("Image URL:", image_url)
        return image_url


    def run(self, text_body, task):
        prompt_str = ""
        if task == "title":
            prompt_str = self.gen_prompt_title(text_body)
            return self.gen_text_out(prompt_str, "gpt-4o-mini")
        elif task == "image":
            prompt_str = self.gen_prompt_image(text_body)
            return self.gen_image_out(prompt_str)
        elif task == "tags":
            prompt_str = self.gen_prompt_tags(text_body)
            return self.gen_text_out(prompt_str, "gpt-4o-mini")
        elif task == "classic":
            prompt_str = self.gen_prompt_classic(text_body)
            return self.gen_text_out(prompt_str, "gpt-4o-mini")
        elif task == "bossy":
            prompt_str = self.gen_prompt_bossy(text_body)
            return self.gen_text_out(prompt_str, "gpt-4o-mini")
        elif task == "idiom":
            prompt_str = self.gen_prompt_idiom(text_body)
            return self.gen_text_out(prompt_str, "gpt-4o-mini")
        elif task == "critic":
            prompt_str = self.gen_prompt_critic(text_body)
            return self.gen_text_out(prompt_str, "gpt-4o")
        elif task == "hiphop":
            prompt_str = self.gen_prompt_hiphop(text_body)
            return self.gen_text_out(prompt_str, "gpt-4o-mini")
        else:
            return None






