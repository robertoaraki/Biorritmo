# Biorritmo

Este programa de cálculo do biorritmo foi escrito em Python 3.9, com a IDE Spyder.



Informe a *Data de nascimento* e clique no botão *Calcular Biorritmo*.

O gráfico será exibido com a data atual no centro, entre o intervalo de 15 dias antes e 15 dias depois.

Os campos *Data p/o biorritmo* e *Período* são opcionais. Se informados, será aceito apenas um campo, ou seja, se informar um, o outro será apagado.

Escolhida a *Data p/o biorritmo*, esta ficará no centro, entre o intervalo de 15 dias antes e 15 dias depois.

Escolhido o *Período* (mês e ano), nenhuma data central ficará em evidência, sendo que o primeiro dia do mês será o primeiro dia do gráfico. O período todo terá 31 dias corridos.

Os formatos aceitos para as datas são *DD/MM/AAAA* ou *MM/AAAA*.

Apesar do programa ser apresentado em janela, ele não é executável. É necessário portanto rodá-lo na linha de comando:

`python BiorritmoGUI.py`



Bibliotecas utilizadas:

- *tkinter* para a apresentação em forma de janela;
- *numpy* para a função matemática de seno;
- *matplotlib* para a criação e exibição do gráfico.

