(function(){
var m=document.querySelector('.menu'),n=document.getElementById('nav');
if(m&&n){m.addEventListener('click',function(){var o=n.classList.toggle('open');m.setAttribute('aria-expanded',o)});
n.addEventListener('click',function(e){if(e.target.tagName==='A'){n.classList.remove('open');m.setAttribute('aria-expanded',false)}})}
var f=document.getElementById('inquiry');
if(f){f.addEventListener('submit',function(e){e.preventDefault();var g=function(k){return (f.elements[k]&&f.elements[k].value||'').trim()},er=f.querySelector('.err');
var name=g('name'),em=g('email'),msg=g('msg');
if(!name||!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(em)||!msg){er.textContent='Please add your name, a valid email and a few words about the project.';er.hidden=false;return}
er.hidden=true;var sv=[].slice.call(f.querySelectorAll('input[name=svc]:checked')).map(function(x){return x.value});
var body='Name: '+name+'\nEmail: '+em+'\nPhone: '+(g('phone')||'-')+'\nBusiness / website: '+(g('biz')||'-')+'\nServices: '+(sv.join(', ')||'-')+'\nTimeline: '+(g('when')||'-')+'\n\nProject:\n'+msg+'\n\n(Sent from mouthoffmedia.com)';
var subj='New project: '+(g('biz')||name);
location.href='mailto:'+f.dataset.to+'?subject='+encodeURIComponent(subj)+'&body='+encodeURIComponent(body)})}
if('serviceWorker' in navigator){addEventListener('load',function(){navigator.serviceWorker.register('/sw.js').catch(function(){})})}
})();
