# Aplicativo para registro de presença nos treinos - Natação UFSCar

Esse aplicativo foi criado com o intuito de registrar a presença dos atletas nos treinos da equipe de natação da UFSCar.

Atualmente, esse controle é feito de forma manual, em uma lista no Whatsapp.

Essa solução funciona, mas existem alguns desafios:
1. Dependência de uma pessoa para registrar a presença de todos os atletas diariamente. Caso a pessoa responsável esqueça, perde-se o controle de presença.
2. Risco de perda de dados se a conversa no Whatsapp for deletada acidentalmente.
3. Dificuldade em monitorar a consistência da presença de cada atleta ao longo do mês.

O aplicativo foi criado utilizando o Streamlit. Cada atleta será responsável por acessar o app, escolher a data do treino, selecionar seu nome em uma lista suspensa e inserir a senha do dia (informada durante o treino). Todos os registros serão automaticamente enviados para uma planilha no Google Drive do time.