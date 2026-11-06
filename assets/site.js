
    (function(){
      const menuBtn=document.getElementById('menuBtn');
      const mainNav=document.getElementById('mainNav');
      menuBtn.addEventListener('click',()=>{const open=mainNav.classList.toggle('open');menuBtn.setAttribute('aria-expanded',String(open));});
      mainNav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{mainNav.classList.remove('open');menuBtn.setAttribute('aria-expanded','false');}));
      const modal=document.getElementById('lightbox'),image=document.getElementById('lightboxImage'),caption=document.getElementById('lightboxCaption'),close=document.getElementById('lightboxClose');
      let previousFocus=null;
      const hide=()=>{modal.setAttribute('aria-hidden','true');image.removeAttribute('src');document.body.style.overflow='';if(previousFocus)previousFocus.focus();};
      document.querySelectorAll('[data-zoom]').forEach(btn=>btn.addEventListener('click',()=>{previousFocus=btn;const source=btn.querySelector('img');image.src=source.src;image.alt=source.alt;caption.textContent=btn.getAttribute('data-zoom');modal.setAttribute('aria-hidden','false');document.body.style.overflow='hidden';close.focus();}));
      close.addEventListener('click',hide);
      modal.addEventListener('click',e=>{if(e.target===modal)hide();});
      document.addEventListener('keydown',e=>{if(e.key==='Escape' && modal.getAttribute('aria-hidden')==='false')hide();if(e.key==='Tab' && modal.getAttribute('aria-hidden')==='false'){e.preventDefault();close.focus();}});
    })();
  