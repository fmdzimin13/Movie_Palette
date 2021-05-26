
const main = document.querySelector("#main")
const qna = document.querySelector("#qna")
const result = document.querySelector('#result')
const endPoint = 9 //status바에서 사용할 변수(총 질문 수)
const select = []


function calculation () {
  const calcList = [
    { name: 'Romance', value: 0, key: 0 },
    { name: 'Family', value: 0, key: 1 },
    { name: 'Action', value: 0, key: 3 },
    { name: 'Horror', value: 0, key: 5 },
    { name: 'History', value: 0, key: 9 },
  ]
  // 돌고 돌면서 선택된 답에 대한 value 값 올려주기
  for (let i = 0; i < endPoint; i++) {
    const target = qnaList[i].a[select[i]]
    // 만약 우리가 type을 하나씩 넣는다면, 이 반복은 안해줘도
    for (let j = 0; j < target.type.length; j++) {
      for (let k = 0; k < calcList.length; k++) {
        if (target.type[j] === calcList[k].name) {
          calcList[k].value += 1
        }
      }
    } 
  }
  // console.log(calcList)
  // 높은 value 순으로 정렬된 배열 만들기
  const resultList = calcList.sort(function (a, b) {
    if (a.value > b.value) {
      return -1
    }
    if (a.value < b.value) {
      return 1
    }
    return 0
  })

  const result1 = resultList[0].key
  const result2 = resultList[1].key
  const result = result1 + result2
  
  for (let m = 0; m < recommendList.length; m++) {
    if (result === recommendList[m].addkey) {
      const idx = recommendList[m].idx
      return idx
    }
  }
}


function setResult() {

  let point = calculation()
  const resultName = document.querySelector('.resultName')
  resultName.innerHTML = infoList[point].name

  const imgDiv = document.querySelector('.colorChip')
  imgDiv.style.backgroundColor = colorMatch[point].color

  
  // const resultImg = document.createElement('img')
  // const imgDiv = document.querySelector('#resultImg')
  // const imgURL = 'img/image' + point + '.png'
  // resultImg.src = imgURL
  // resultImg.alt = point
  // imgDiv.appendChild(resultImg)
  console.log(point)
  console.log(infoList[point].desc)
  console.log(infoList[point].desc1)
  const resultDesc = document.querySelector('.resultDesc')
  resultDesc.innerHTML = infoList[point].desc
  
  const resultDesc1 = document.querySelector('.resultDesc1')
  resultDesc1.innerHTML = infoList[point].desc1
}




//결과창 띄우는 함수
function goResult () {
  
  qna.style.WebkitAnimation = "fadeOut 1s"
  qna.style.animation = "fadeOut 1s"
  setTimeout(() => {
    result.style.WebkitAnimation = "fadeIn 1.2s"
    result.style.animation = "fadeIn 1.2s"
    setTimeout(() => {
      qna.style.display = "none"
      result.style.display = "block"
    }, 450)})
    setResult()
}


//질문에 대한 대답을 가져오고,
function addAnswer(answerText, qIdx, idx) {
  const a = document.querySelector('.answerBox')
  const answer = document.createElement('button')
  answer.classList.add('answerList')
  answer.classList.add('my-3')
  answer.classList.add('py-3')
  answer.classList.add('mx-auto')
  answer.classList.add('fadeIn')
  a.appendChild(answer)
  answer.innerHTML = answerText
  // 대답 중 하나를 선택하면 다음 질문으로
  answer.addEventListener("click", function () {
    const children = document.querySelectorAll('.answerList')
    for (let i = 0; i < children.length; i++) {
      children[i].disabled = true //버튼 비활성화
      children[i].style.WebkitAnimation = "fadeOut 0.5s"
      children[i].style.animation = "fadeOut 0.5s"
    }
    setTimeout(() => {
      //qIdx번쨰 질문에서 idx번 답을 택했다는 걸 select 배열에 넣어준다
      select[qIdx] = idx
      for (let i = 0; i < children.length; i++) {
        children[i].style.display = 'none'
      }
      goNext(++qIdx)
    }, 500)
  })
}


//미리 저장해둔 데이터들을 가져오는 함수(질문부터)
function goNext(qIdx){
  //마지막 질문까지 답한다면 결과로 가는 함수 실행
  if (qIdx === endPoint) {
    goResult()
    return
  } 

  let q = document.querySelector('.qBox')
  q.innerHTML = qnaList[qIdx].q
  for (let i in qnaList[qIdx].a) {
    addAnswer(qnaList[qIdx].a[i].answer, qIdx, i)
  }
  // 진행바 관련 로직
  const status = document.querySelector('.statusBar')
  status.style.width = (100/endPoint) * (qIdx+1) + '%'
}


//처음 시작하기 버튼을 누른 후에 실행되는 함수(다음 페이지로 전환)
//여기선 fadeIn과 fadeOut이 맞물려서 동작
function begin() {
  main.style.WebkitAnimation = "fadeOut 1s"
  main.style.animation = "fadeOut 1s"
  setTimeout(() => {
    qna.style.WebkitAnimation = "fadeIn 1s"
    qna.style.animation = "fadeIn 1s"
    setTimeout(() => {
      main.style.display = "none"
      qna.style.display = "block"
    }, 450)
    let qIdx = 0
    goNext(qIdx)
  }, 450)
}

const start = document.querySelector('#start')
start.addEventListener('click', function() {
  begin()
})

//get요청으로만 보내진다면 내가 맞출 수밖에... 이러면 db에 저장이 잘된다...?
// const btn = document.querySelector('#load')
// btn.addEventListener('click', function () {
//   let point = calculation()
//   const name = infoList[point].name
//   const code = colorMatch[point].color
//   axios.get('http://127.0.0.1:8000/recommend/load_color/', {
//     params: {
//       name,
//       code,
//     }
//   })
//   .then(function (res) {
//     console.log(res)
//     // console.log(res.data)
// })
// })


//성공적인 POST
const btn1 = document.querySelector('#loadpost')
console.log(btn1)
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

const data = new FormData()

  btn1.addEventListener('click', function (event) {
    console.log(event)
    let point = calculation()
    console.log(point)
    const name = infoList[point].name
    const code = colorMatch[point].color  
    data.append('personal_color', name)
    data.append('color_code', code)
    console.log(data)


    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/recommend/load/',
      headers: {
        'X-CSRFToken': csrftoken,
      },
      // data: data,
      data,
    })
    .then(function (response) {
      console.log(response.data.content)
      const p = document.querySelector('#responseMessage')
      p.innerHTML = response.data.content
    })
    .catch(function (error) {
      console.log(error)
    })
})

//문제가 되는 부분! 분명 post로 보냈는데 왜 get 요청이 보내지는거지???!
// const load = document.querySelector('#load-form')
// const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

// load.addEventListener('submit', function (event) {
//   event.preventDefault()
//   // console.log(event)
//   let point = calculation()
//   const name = infoList[point].name  
//   axios({
//     method: 'post',
//     url: 'http://127.0.0.1:8000/recommend/load/',
//     headers: {
//       'X-CSRFToken': csrftoken
//     },
//     data: { personal_color: name },
//   })
//     .then(function (response) {
//       console.log(response)
//     })
//     .catch(function (error) {
//       console.log(error)
//     })
// })

const movie = document.querySelector('#movie')
movie.addEventListener('click', function () {
  const showMovies = document.querySelector('.showMovies')
  while (showMovies.hasChildNodes()) {
    showMovies.removeChild(showMovies.firstChild)
  }

  let point = calculation()
  const target_genre1 = recommendList[point].recommend[0]
  const target_genre2 = recommendList[point].recommend[1]
  axios.get('http://127.0.0.1:8000/recommend/get_movies/', {
    params: {
      target_genre1,
      target_genre2
    }
  })
  .then(function (res) {
    // console.log(res)
    // console.log(res.data)
    for (let i = 0; i < res.data.length; i++) {
      const showMovie = document.createElement('img')
      showMovie.src = res.data[i].poster_path
      const showMovies = document.querySelector('.showMovies')
      showMovies.appendChild(showMovie)
    }

  })
})

function again() {
  result.style.WebkitAnimation = "fadeOut 1s"
  result.style.animation = "fadeOut 1s"
  setTimeout(() => {
    main.style.WebkitAnimation = "fadeIn 1s"
    main.style.animation = "fadeIn 1s"
    setTimeout(() => {
      result.style.display = "none"
      main.style.display = "block"
    }, 450)
    begin()
  }, 450)
}