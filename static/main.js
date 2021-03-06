/*===== MENU SHOW Y HIDDEN =====*/ 
const navMenu = document.getElementById('nav-menu'),
toggleMenu = document.getElementById('nav-toggle'),
closeMenu = document.getElementById('nav-close')

/*SHOW*/ 
toggleMenu.addEventListener('click', ()=>{
    navMenu.classList.toggle('show')
})

/*HIDDEN*/
closeMenu.addEventListener('click', ()=>{
    navMenu.classList.remove('show')
})

/*===== ACTIVE AND REMOVE MENU =====*/
const navLink = document.querySelectorAll('.nav__link');   

function linkAction(){
  /*Active link*/
  navLink.forEach(n => n.classList.remove('active'));
  this.classList.add('active');
  
  /*Remove menu mobile*/
  navMenu.classList.remove('show')
}
navLink.forEach(n => n.addEventListener('click', linkAction));


// My code starts here.

function getToken(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getToken(
    'csrftoken'
);

var updateBtns = document.getElementsByClassName('update-likes')

for (i = 0; i < updateBtns.length; i++) {
	    updateBtns[i].addEventListener('click', function(){
		var articleId = this.dataset.id
        var action = this.dataset.action
		// console.log('articleId:', articleId, "action:", action, csrftoken)
        updateLike(articleId, action)
	})
}

function updateLike(articleId, action) {
    var url = "/update_like"
    fetch(url, {
        method : "POST",
        headers : {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrftoken
        },
        body : JSON.stringify({'articleId': articleId, 'action': action})
      }
    )
    .then((response) => {
    //     console.log(response)
        return response.json()
    })
    .then((data) => {
        // console.log('data', data)
        location.reload()
    })
}

const preloader = document.querySelector(".preloader"); 

console.log(preloader)

// const preloader = document.querySelector(".preloader");
const preloaderDuration = 1800;

const hidePreloader = () => {
    setTimeout(() => {
        preloader.classList.add("not-visible");
    }, preloaderDuration);
}

window.addEventListener("load", hidePreloader);


// for scroller 
window.onscroll = function() {myFunction()};

function myFunction() {
  var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
  var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  var scrolled = (winScroll / height) * 100;
  document.getElementById("myBar").style.width = scrolled + "%";
}

// for toggling night mode.
type="text/javascript">
document.querySelector('.checkbox').addEventListener('change',()=>{
    document.querySelectorAll('.night-mode-available').forEach(ele=>{
    ele.classList.toggle('night');
    })
});