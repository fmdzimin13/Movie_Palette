/*
'Romance', key: 0 
'Family', key: 1 
'Action', key: 3 
'Horror', key: 5 
'History', key: 9 
*/
const colorMatch = [
  { idx: 0, color: "#FF8243" },
  { idx: 1, color: "#DE5D83" },
  { idx: 2, color: "#FD5E53" },
  { idx: 3, color: "#FC2847" },
  { idx: 4, color: "#FDFC74" },
  { idx: 5, color: "#8F509D" },
  { idx: 6, color: "#7851A9" },
  { idx: 7, color: "#3BB08F" },
  { idx: 8, color: "#5D76CB" },
  { idx: 9, color: "#1A4876" },
]



const recommendList = [
  { addkey: 1, recommend: [1, 2], idx: 0},
  { addkey: 3, recommend: [1, 7], idx: 1},
  { addkey: 5, recommend: [1, 8], idx: 3},
  { addkey: 9, recommend: [1, 10], idx: 6},
  { addkey: 4, recommend: [2, 7], idx: 2},
  { addkey: 6, recommend: [2, 8], idx: 4},
  { addkey: 10, recommend: [2, 10], idx: 7},
  { addkey: 8, recommend: [7, 8], idx: 5},
  { addkey: 12, recommend: [7, 10], idx: 8},
  { addkey: 14, recommend: [8, 10], idx: 9},
]


const qnaList = [
  {
    q: 'Q1 여행을 간다면 가장 가고 싶은 여행지는 어디인가요?',
    a: [
      { answer: '발리', type: ['Romance', 'History']},
      { answer: '유럽', type: ['Family']},
      { answer: '뉴질랜드', type: ['Action']},
      { answer: '멕시코', type: ['Horror']},
    ]
  },
  {
    q: 'Q2 당신이 요즘 즐겨듣는 음악은 무엇인가요?',
    a: [
      { answer: '발라드', type: ['Romance']},
      { answer: '트로트', type: ['Family']},
      { answer: '힙합 / 댄스', type: ['Action', 'History']},
      { answer: '일렉트로닉 / 메탈', type: ['Horror']},
    ]
  },
  {
    q: 'Q3 좋아하는 술 종류는?',
    a: [
      { answer: '와인', type: ['Romance']},
      { answer: '막걸리', type: ['Family', 'History']},
      { answer: '맥주', type: ['Action']},
      { answer: ' 소주', type: ['Horror']},
    ]
  },
  {
    q: 'Q4 친구들이 보는 당신의 이미지는?',
    a: [
      { answer: '자기 사람을 잘 챙긴다', type: ['Romance']},
      { answer: '스스럼 없이 편하다', type: ['Family']},
      { answer: '하이 텐션 뿜뿜뿜', type: ['Action']},
      { answer: '차가운 첫인상 그렇지만 속은 따뜻', type: ['Horror', 'History']},
    ]
  },
  {
    q: 'Q5 당신의 눈 앞에 램프 속 지니가 나타났습니다. 다음 중 원하는 능력을 준다고 할 때 고를 것은?',
    a: [
      { answer: '미모', type: ['Romance', 'History']},
      { answer: '인내심', type: ['Family']},
      { answer: '체력', type: ['Action']},
      { answer: '용기', type: ['Horror']},
    ]
  },
  {
    q: 'Q6 해리포터 시리즈의 호그와트에서 가장 들어보고 싶은 수업은?',
    a: [
      { answer: '마법의 약', type: ['Romance']},
      { answer: '마법의 역사', type: ['Family', 'History']},
      { answer: '비행', type: ['Action']},
      { answer: '어둠의 마법 방어술', type: ['Horror']},
    ]
  },
  {
    q: 'Q7 당신이 즐거보는 유튜브 컨텐츠는?',
    a: [
      { answer: '영화 / 드라마 리뷰', type: ['Romance']},
      { answer: '브이로그', type: ['Family']},
      { answer: '내셔널지오그래픽 (베어그릴스)', type: ['Action', 'History']},
      { answer: ' 미스터리나 공포 썰', type: ['Horror']},
    ]
  },
  {
    q: 'Q8 하루 중 가장 기분 좋은 시간대는?',
    a: [
      { answer: '저녁', type: ['Romance']},
      { answer: '오후', type: ['Family']},
      { answer: '오전', type: ['Action']},
      { answer: '새벽', type: ['Horror', 'History']},
    ]
  },
  {
    q: 'Q9 다음 중 무조건 하나를 선택해야 한다면 무엇을 선택하실 건가요?',
    a: [
      { answer: '하루 10시간 알고리즘 문제 풀기', type: ['Romance', 'History']},
      { answer: '시간 별로 건강 설문 작성하기', type: ['Family']},
      { answer: '2일만에 프로젝트 완성하기 (리드미 필수)', type: ['Action']},
      { answer: 'while True: 하나만 더 괜찮으신가요?', type: ['Horror']},
    ]
  },
]

const infoList = [
  {
    name: 'Mango Tango',
    desc: '주변 분위기를 탱고로 만드는 망고같은 사람',
    desc1: '상대의 마음을 편안하게 만들어 주는 데에 특별한 능력이 있는 당신. 잔잔한 일상을 소중히 여긴다. 커다란 사건이 일어나는 것을 싫어하지는 않지만, 늘 관성처럼 제자리로 돌아오는 삶을 더 좋아한다. 참으로도 망고같은 사람'
  },
  {
    name: 'Blush',
    desc: '설레임은 좋지만 잔잔한 건 싫어',
    desc1: '활발하고 도전하는 과정에서 설렘을 느끼는 당신. 어제보단 오늘이, 오늘보단 내일이 더 기대되는 당신이다. 아 추가로 당신은 얼굴이 붉어지는 로맨스를 간혹 즐기기도 한다. 영화 "미스터 앤 미세스"에서 볼 법한 사랑을 한달까',
  },
  {
    name: 'Sunset Orange',
    desc: '해가 빛나냐 아니 내가 더 빛나다!',
    desc1: '활기가 넘치는 당신. 에너지 드링크를 10병 마신 게 아닐까 착각이 될 정도로 에너지가 넘치는 당신이다. 당신의 연애 스타일은 미운 정 고운 정. 때론 넘치는 활기에 과정이 험난하기도 하지만 결말은 해피엔딩. 그러니 걱정말아라'
  },
  {
    name: 'Scarlet',
    desc: '낮과 밤이 다른 사람, 나야나',
    desc1: '핏빛인듯 마냥 빨갛진 않고 은은한 핑크빛을 함유한 스칼렛과 같은 당신. 조화로움보다는 상극을 즐기는 편이다. 달달함만 있는 건 당도 초과, 싫어한다. 스릴 있는 활동과 연애를 즐기는 당신. 언제 돌변할 지 몰라 상대방이 맘을 졸이곤 한다.'
  },
  {
    name: 'Laser Lemon',
    desc: '나는야 포춘쿠키',
    desc1: '열어보기 전까지는 속을 도통 알 수 없는 당신. 때론 한 없이 순수하고 밝은 모습이다가도, 때론 그 밝음이 무서울 때가 있다. 1주일 밤샘 프로젝트 후, 그저 웃는 당신.. 정말 밝은 걸까..? 아니면 미친 걸까..? 아무도 알 수 없다.',
  },
  {
    name: 'Vivid Violet',
    desc: '공포영화에서 가장 먼저 죽는 사람, 그건 나',
    desc1: '호기심이 많고 스릴을 즐기는 당신. 당신과 함께 공포 영화에 갇힌다면, 당신은 첫 번째로 사라질 게 분명하다. 하지만 그럼에도 후회하지 않는 당신. 하고 싶은 건 해야 직성이 풀리는 당신에게 응원의 박수를 보낸다.',
  },
  {
    name: 'Loyal Purple',
    desc: '과거는 현재를 비추는 거울이지',
    desc1: '어제가 있기에 오늘의 내가 있다고 생각하는 당신. 오래된 것의 참된 가치를 안달까. 당신의 보물단지를 보면 다른 사람들은 아마 놀랄 것이다. 연애에서도 별반 다르지 않다. 옥시토신 유효 기간 3년은 당신에겐 해당되지 않는 이야기.'
  },
  {
    name: 'Jungle Green',
    desc: '누구에겐 쉼터가, 다른 누구에겐 미로 같은 사람',
    desc1: '처음 봤을 때, 다가가기 힘든 당신. 계속 알고 지내면, 여전히 알기 힘든 당신이다. 소수의 사람들에겐 녹음이 진 쉼터 같은 당신이지만, 대부분의 사람들에게 당신은 비밀에 감싸인 어렵고도 신비로운 사람이다. 조금은 마음을 더 열어보자.',
  },
  {
    name: 'Indigo',
    desc: '벤자민 버튼의 시간은 거꾸로 간다',
    desc1: '화이팅이 넘치는 당신. 우리는 하루하루 분명 나이를 먹어가고 있는데, 당신은 어떻게 그 에너지를 유지하는가? 그저 놀라울 따름이다. 당일치기 동해바다, 아니 제주도까지도 마음만 먹으면 바로 달려갈 수 있는 사람이 바로 당신이다.',
  },
  {
    name: 'Midnight Blue',
    desc: '이 구역의 미친 부엉이는 나야',
    desc1: '새벽에 연락하면 칼답하는 당신. 당신의 24시간은 내 24시간과는 다른걸까? 새벽을 좋아하는 당신. 새벽에 걸맞는 고전 공포 영화를 즐긴다. 겁이 없다. 첫인상은 공포 영화 못지 않게 차갑지만, 알아가면 알수록... 궁금하면 오백원',
  },

]