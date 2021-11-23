# Rossmann Store Sales Prediction

![alt text](https://github.com/VictorTerror/DataScience_Em_Producao/blob/main/img/rossmann.png?raw=True)


## **1. Business Problem**

A Rossmann é uma das maiores redes de drogarias da Europa, com cerca de 56.200 funcionários e mais de 4.000 lojas em toda o continente europeu. Em 2019, teve um faturamento de mais de € 10 bilhões. Seu CFO deseja investir parte do faturamento para reformar as lojas da rede. Para determinar o valor a ser investido em cada loja, ele solicita de uma previsão de vendas, de cada uma das unidades, para as próximas 6 semanas. Cabe ao time de Cientistas de Dados da Rossmann analisar o problema de negócio, traçar a estratégia e desenvolver a melhor solução para atender a esta requisição.



## **2. Business Assumptions**

* **Competition_distance:** É expressa em metros e no caso de seu valor ser igual a 0, assumi que não há competidores próximos e para efeitos de algorítimos de machine learning substitui esse valor por 100000 que é muito superior ao valor máximo encontrado de 75860.
* **Assortment:** Assumi que existe uma hierarquia entre os tipos de estoque. Logo lojas como o estoque C oferecem também os tipos A e B.
* **Open:** Lojas fechadas foram descartadas a principio, uma vez que suas vendas são igual a 0. Essa variável será melhor avaliada futuramente, no próximo ciclo do CRISP, para tentar melhora o desempenho do algorítimo de machine learning.


## **3. Solution Strategy**

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


## **4. Top 3 Data Insights**
* **Hipótese 01:** Lojas com compeditores mais proximos deveriam vender menos.<br/>
  **Falso** Lojas com competidores mais proximos vendem mais.<br/>
  **Insight:** Possivelmente, a proximidade com outras lojas concorrentes, crie uma região comercial mais atrativa para os clientes, o que, acaba por aumentar o faturamento. <br/>
  
* **Hipótese 02:** Lojas com promoções ativas por mais tempo deveriam vender mais.<br/>
  **Falso** lojas com promoções ativas por mais tempo vendem menos, após certo periodo de promoção.<br/>
  **Insight:** Após um periodo muito extenso de promoções, as vendas diminuem. Esse efeito é provavelmente desencadeado por uma normalização dos preços promocionais.<br/>

* **Hipótese 03:** Lojas com compedidores a mais tempo deveriam vender mais.<br/>
  **Falso** Lojas com competidores a mais tempo vendem menos.<br/>
  **Insight:** A tendência é que as vendas se dispersem entre todos os competidores, de determinada região, após grandes períodos de tempo.


## **5. Metrics**

### Modelo Base
Model Name	| MAE CV	| MAPE CV	| RMSE CV
---------- | ------ | ------- | -------
Avarege Model |	1354.800353	| 0.455051	| 1835.135542

Esperamos que os resultados dos modelos testados sejam, no mínimo, superior ao modelo de média. Caso contrário serão automaticamente descartados.
<br/>

###  Machine Learning Models - Cross Validation
Model Name	| MAE CV	| MAPE CV	| RMSE CV
---------- | ------ | ------- | -------
Linear Regression |	2081.73 +/- 295.63	| 0.3 +/- 0.02	| 2952.52 +/- 468.37
Linear Regression - Lasso	| 2116.38 +/- 341.5	 | 0.29 +/- 0.01	 | 3057.75 +/- 504.26
Random Forest Regressor |	838.18 +/- 218.74	| 0.12 +/- 0.02	| 1256.87 +/- 319.67
XGBoost Regressor	| 1048.45 +/- 172.04	| 0.14 +/- 0.02	| 1513.27 +/- 234.33

Apesar da Random Forest ter o melhor desempenho, optei pelo XGBoost Regressor por questões de performance e uma vez que utilizei a técnica de Hyperparameter Fine Tuning, essa diferença de desempenho foi significamente reduzida.


## **6. Business Results**  

Model Name	| MAE |	MAPE	| RMSE
---------- | ------ | ------- | -------
XGBoost Regressor	| 634.160515	| 0.092536	| 918.0236


![alt text](https://github.com/VictorTerror/DataScience_Em_Producao/blob/main/img/MLresultsX.png?raw=True)

Scenarios	| Values	|
---------- | ------ |
predictions |	R$ 284,390,687.45
worst_scenario |	R$ 283,679,498.75
best_scenario	| R$ 285,101,876.15



<img height="700em" src="https://github.com/VictorTerror/DataScience_Em_Producao/blob/main/img/Telegrambot.jpeg?raw=True"/>

## **7. Conclusion**


## **8. Next Steps**
Iniciar um novo ciclo do CRISP tendo como foco os dados Outliers.
Criar e analisar novos gráficos para um melhor entendimento do negócio.
Validar novas hipóteses e gerar insights.
Testar novos parametros para o XGBoost.




