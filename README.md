# Rossmann Store Sales Prediction

![alt text](https://github.com/VictorTerror/DataScience_Em_Producao/blob/main/img/rossmann.png?raw=True)


## **1. Business Problem**

A Rossmann é uma das maiores redes de drogarias da Europa, com cerca de 56.200 funcionários e mais de 4.000 lojas em toda o continente europeu. Em 2019, teve um faturamento de mais de € 10 bilhões. Seu CFO deseja investir parte do faturamento para reformar as lojas da rede. Para determinar o valor a ser investido em cada loja, ele solicita de uma previsão de vendas, de cada uma das unidades, para as próximas 6 semanas. Cabe ao time de Cientistas de Dados da Rossmann analisar o problema de negócio, traçar a estratégia e desenvolver a melhor solução para atender a esta requisição.



## **2. Business Assumptions**

* **Competition_distance:** É expressa em metros e no caso de seu valor ser igual a 0, assumi que não há competidores próximos e para efeitos de algorítimos de machine learning substitui esse valor por 100000 que é muito superior ao valor máximo encontrado de 75860.

* **Assortment:** Assumi que existe uma hierarquia entre os tipos de estoque. Então lojas como o estoque C oferecem também os tipos A e B.

* **Open:** Lojas fechadas foram descartadas a principio, uma vez que suas vendas são igual a 0. Essa variável será melhor avaliada futuramente, no próximo ciclo do CRISP, para tentar melhora o desempenho do algorítimo de machine learning.


## **3. Solution Strategy**
Minha estratégia para resolver esse desafio foi:

* 1°. Data Description
* 2°. Feature Engineering
* 3°. Data Filtering
* 4°. Exploratory Data Analysis
* 5°. Data Preparation
* 6°. Feature Selection
* 7°. Machine Learning Modelling
* 8°. Hyperparameter Fine Tuning
* 9°. Business Performance
* 10°. Model deploy


## **5. Top 3 Data Insights**
* **Hipótese 01:** Lojas com compeditores mais proximos deveriam vender menos.<br/>
  **Falso** Lojas com competidores mais proximos vendem mais.<br/>
  **Insight:** Possivelmente, a proximidade com outras lojas concorrentes, crie uma região comercial mais atrativa para os clientes, o que, acaba por aumentar o faturamento. <br/>
  
* **Hipótese 02:** Imóveis construidos nos últimos anos deveriam estar em melhores condições.<br/>
  **Falso** Imóveis contruídos nos ultimos 25 anos estão em condições inferiores.<br/>
  **Insight:** Esses imóveis são promissores para serem adquiridos a preços inferiores e posteriormente reformados, melhorando sua condição e agregando o valor da reforma.<br/>

* **Hipótese 03:** O preço médio dos imóveis é maior no verão.<br/>
  **Falso** O preço médio dos imóveis é maior na primavera.<br/>
  **Insight:** Os imóveis adquiridos devem ser preferencialmente vendidos na primavera, onde o valor médio é superior à outras estações.


## **6. Conclusion**


## **7. Next Steps**


