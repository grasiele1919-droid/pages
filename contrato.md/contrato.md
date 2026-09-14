CONTRATO.md
1. Dados que a tela exibe
- Nome | texto | campo do formulário de agendamento.
- Telefone / WhatsApp | texto | campo do formulário de agendamento.
- Empresa / Condomínio | texto | campo do formulário de agendamento.
- Visitante | texto | cartão ilustrativo “Painel de visitas”.
- Bloco / Apt | texto | cartão ilustrativo “Painel de visitas”.
- Data e horário da visita | texto | cartão ilustrativo “Painel de visitas”.
2. Ações que o usuário dispara
- Clicar em “Benefícios” | a tela navega até a seção de benefícios.
- Clicar em “Funcionalidades” ou “Conhecer funcionalidades” | a tela navega até a seção de funcionalidades.
- Clicar em “Agendar demo” ou “Solicitar demonstração” | a tela vai até o formulário de agendamento; no botão “Solicitar demonstração”, a rolagem é suave.
- Preencher Nome, Telefone / WhatsApp e, opcionalmente, Empresa / Condomínio, e enviar “Agendar demonstração” | o formulário é limpo e a tela informa que entrará em contato em até 2 dias úteis.
- Clicar em “Falar com especialista” | a tela mostra a mensagem “Obrigado! Entraremos em contato em breve.”
3. O que o servidor precisaria fazer
- Navegar entre seções | não precisa de servidor, pois a navegação ocorre na própria página.
- Solicitar demonstração | ? receber Nome, Telefone / WhatsApp e Empresa / Condomínio; registrar a solicitação e devolver uma confirmação de recebimento.
- Falar com especialista | ? como não há campos enviados nessa ação, o servidor não tem dados para identificar ou contatar a pessoa; seria necessário definir o que deve ser enviado.
4. Dúvidas para o professor
- O projeto atual é uma landing page em HTML, CSS e JavaScript puro, não há componentes React. A referência a React corresponde a outra versão do projeto?
- Os dados do cartão “Painel de visitas” (João Silva, Apt 302 e data/hora) são apenas exemplo visual ou devem vir de dados reais?
- A tela anuncia registro de visitantes, histórico, validação de CPF e monitoramento em tempo real, mas não possui telas ou controles para essas funções. Elas fazem parte deste contrato?
- A validação de documentos mencionada na página deve incluir quais dados além do CPF?
- O prazo de “até 2 dias úteis” é apenas texto fixo ou existe uma regra real para retorno?