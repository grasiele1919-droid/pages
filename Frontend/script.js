document.addEventListener('DOMContentLoaded', ()=>{
  const form = document.getElementById('demoForm');
  const demoBtn = document.getElementById('demoBtn');
  const contactSales = document.getElementById('contactSales');

  demoBtn && demoBtn.addEventListener('click', ()=>{
    document.getElementById('contact')?.scrollIntoView({behavior:'smooth'});
  });

  contactSales && contactSales.addEventListener('click', ()=>{
    alert('Obrigado! Entraremos em contato em breve.');
  });

  form && form.addEventListener('submit', (e)=>{
    e.preventDefault();
    const data = new FormData(form);
    // Simulação de envio — substituir integração real conforme necessário
    console.log('Demo request', Object.fromEntries(data.entries()));
    form.reset();
    alert('Solicitação enviada. Entraremos em contato em até 2 dias úteis.');
  });
});
