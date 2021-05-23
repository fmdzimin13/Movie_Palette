/*
'Romance', key: 0 
'Family', key: 1 
'Action', key: 3 
'Horror', key: 5 
'History', key: 9 
*/

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
    q: '1. 알고리즘? 뷰?',
    a: [
      { answer: 'a. 알고리즘... 퉤', type: ['Family']},
      { answer: 'b. 뷰... 퉤', type: ['Action']},
      { answer: 'c. 둘 다... 퉤', type: ['2', '3']},
      { answer: 'd. 둘 다 좋은걸요?', type: ['1', '4']},
    ]
  },
  {
    q: '2. 매일 프로젝트하기? 매일 알고리즘 풀기?',
    a: [
      { answer: 'a. 알고리즘... 퉤', type: ['Family']},
      { answer: 'b. 뷰... 퉤', type: ['Action']},
      { answer: 'c. 둘 다... 퉤', type: ['2', '3']},
      { answer: 'd. 둘 다 좋은걸요?', type: ['1', '4']},
    ]
  },
  {
    q: '3. 지금 자면 내일의 나는 .. ',
    a: [
      { answer: 'a. 알고리즘... 퉤', type: ['Family']},
      { answer: 'b. 뷰... 퉤', type: ['Action']},
      { answer: 'c. 둘 다... 퉤', type: ['2', '3']},
      { answer: 'd. 둘 다 좋은걸요?', type: ['1', '4']},
    ]
  },
  {
    q: '4. 하 왜 마지막 결과창을 못 가는거니',
    a: [
      { answer: 'a. 알고리즘... 퉤', type: ['Family']},
      { answer: 'b. 뷰... 퉤', type: ['Action']},
      { answer: 'c. 둘 다... 퉤', type: ['2', '3']},
      { answer: 'd. 둘 다 좋은걸요?', type: ['1', '4']},
    ]
  },
  {
    q: '5. 자바스크립트 퉤퉤퉤',
    a: [
      { answer: 'a. 알고리즘... 퉤', type: ['Family']},
      { answer: 'b. 뷰... 퉤', type: ['Action']},
      { answer: 'c. 둘 다... 퉤', type: ['2', '3']},
      { answer: 'd. 둘 다 좋은걸요?', type: ['1', '4']},
    ]
  },
  {
    q: '6. 자바스크립트 퉤퉤퉤',
    a: [
      { answer: 'a. 알고리즘... 퉤', type: ['Family']},
      { answer: 'b. 뷰... 퉤', type: ['Action']},
      { answer: 'c. 둘 다... 퉤', type: ['2', '3']},
      { answer: 'd. 둘 다 좋은걸요?', type: ['1', '4']},
    ]
  },
  {
    q: '7. 자바스크립트 퉤퉤퉤',
    a: [
      { answer: 'a. 알고리즘... 퉤', type: ['Family']},
      { answer: 'b. 뷰... 퉤', type: ['Action']},
      { answer: 'c. 둘 다... 퉤', type: ['2', '3']},
      { answer: 'd. 둘 다 좋은걸요?', type: ['1', '4']},
    ]
  },
  {
    q: '8. 자바스크립트 퉤퉤퉤',
    a: [
      { answer: 'a. 알고리즘... 퉤', type: ['Family']},
      { answer: 'b. 뷰... 퉤', type: ['Action']},
      { answer: 'c. 둘 다... 퉤', type: ['2', '3']},
      { answer: 'd. 둘 다 좋은걸요?', type: ['1', '4']},
    ]
  },
  {
    q: '9. 자바스크립트 퉤퉤퉤',
    a: [
      { answer: 'a. 알고리즘... 퉤', type: ['Family']},
      { answer: 'b. 뷰... 퉤', type: ['Action']},
      { answer: 'c. 둘 다... 퉤', type: ['2', '3']},
      { answer: 'd. 둘 다 좋은걸요?', type: ['1', '4']},
    ]
  },
]

const infoList = [
  {
    name: '~ 0번 색깔',
    desc: '이러이러한 당신'
  },
  {
    name: '~ 1번 색깔',
    desc: '이러이러한 당신'
  },
  {
    name: '~ 2번 색깔',
    desc: '이러이러한 당신'
  },
  {
    name: '~ 3번 색깔',
    desc: '이러이러한 당신'
  },
  {
    name: '~ 4번 색깔',
    desc: '이러이러한 당신'
  },
  {
    name: '~ 5번 색깔',
    desc: '이러이러한 당신'
  },
  {
    name: '~ 6번 색깔',
    desc: '이러이러한 당신'
  },
  {
    name: '~ 7번 색깔',
    desc: '이러이러한 당신'
  },
  {
    name: '~ 8번 색깔',
    desc: '이러이러한 당신'
  },
  {
    name: '~ 9번 색깔',
    desc: '이러이러한 당신'
  },

]