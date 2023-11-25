//reset 만두틀
function resetImages() {
  for (var i = 1; i <= 9; i++) {
    var mold = document.getElementById("mold" + i);
    var storedSrc = localStorage.getItem("mandoImageSrc_mold" + i);

    if (storedSrc && !storedSrc.includes("{% static 'articles/source/img/mold.png' %}")) {
      mold.src = "{% static 'articles/source/img/mold.png' %}";
      localStorage.removeItem("mandoImageSrc_mold" + i);
    }
  }
}

document.getElementById("reset").addEventListener("click", resetImages);

//만두 리셋 경고창
const reset = document.getElementById("reset");
const resetGuide = document.getElementById("reset-guide");

reset.addEventListener("mouseover", function () {
  resetGuide.style.display = "block";
});

reset.addEventListener("mouseout", function () {
  resetGuide.style.display = "none";
});

//링크 복사
function copyLink() {
  const currentPageUrl = window.location.href; // 현재 페이지의 URL

  const tempTextArea = document.createElement("textarea");
  tempTextArea.value = currentPageUrl;
  document.body.appendChild(tempTextArea);
  tempTextArea.select();
  document.execCommand("copy");
  document.body.removeChild(tempTextArea);

}

//링크가 복사될 떄
function showLinkAlert() {
  const linkAlert = document.getElementById("link-alert");

  if (linkAlert.style.display === "none") {
    linkAlert.style.display = "block"; // 링크 알림 보이기
    // 일정 시간이 지난 후에 다시 숨김 처리
    setTimeout(function () {
      linkAlert.style.display = "none";
    }, 2000);
  } else {
    linkAlert.style.display = "none";
  }
}

var currentMoldIndex = 0; // 현재 이미지 인덱스

function changeMandoImage(id, newSrc) {
  var mold = document.getElementById(id);

  // mold.png인 경우에만 이미지 변경
  if (mold.src.includes("mold.png")) {
    mold.src = newSrc;
    localStorage.setItem("mandoImageSrc_" + id, newSrc);
  }
}

function changeSequentialMandoImage() {
  var moldCount = 9; // mold 이미지의 총 개수

  currentMoldIndex = (currentMoldIndex % moldCount) + 1; // 다음 순서의 이미지 인덱스 계산

  for (var i = 1; i <= moldCount; i++) {
    var newSrc = "mold.png";
    if (i === currentMoldIndex) {
      var randomImage = Math.random();
      // 랜덤으로 white 또는 yellow 만두 선택
      if (randomImage < 0.5) {
        newSrc = "white_mando.png";
      } else {
        newSrc = "yellow_mando.png";
      }
    }

    changeMandoImage('mold' + i, newSrc);
  }
}
