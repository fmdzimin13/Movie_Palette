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
    desc: '이러이러한 당신'
  },
  {
    name: 'Blush',
    desc: '이러이러한 당신'
  },
  {
    name: 'Sunset Orange',
    desc: '이러이러한 당신'
  },
  {
    name: 'Scarlet',
    desc: '이러이러한 당신'
  },
  {
    name: 'Laser Lemon',
    desc: '이러이러한 당신'
  },
  {
    name: 'Vivid Violet',
    desc: '이러이러한 당신'
  },
  {
    name: 'Loyal Purple',
    desc: '이러이러한 당신'
  },
  {
    name: 'Jungle Green',
    desc: '이러이러한 당신'
  },
  {
    name: 'Indigo',
    desc: '이러이러한 당신'
  },
  {
    name: 'Midnight Blue',
    desc: '이러이러한 당신'
  },

]