import requests
import json
import pandas as pd


# constants
TOKEN = '1974088535:AAHDri7qOv0DO8DmgK2vHXohG_Gt8ix2jfU'

# Info about the Bot
https://api.telegram.org/bot1974088535:AAHDri7qOv0DO8DmgK2vHXohG_Gt8ix2jfU/getMe

# Get updates
https://api.telegram.org/bot1974088535:AAHDri7qOv0DO8DmgK2vHXohG_Gt8ix2jfU/getUpdates

# Send message
https://api.telegram.org/bot1974088535:AAHDri7qOv0DO8DmgK2vHXohG_Gt8ix2jfU/sendMessage?chat_id=1920981910&text=Hi Victor!

def send_message(chat_id, text):
	url = 'https://api.telegram.org/bot{}/'.format(TOKEN)
	url = url + 'sendMessage?chat_id={}'.format(chat_id)
	
	r = request.post(url, json={'text': text})
	print( 'Status Code {}'.format(r.status_code))
	
	return None




def load_dataset(store_id):
	# Loading test dataset
	df10 = pd.read_csv( '/home/victor/repos/DataScience_Em_Producao/data/test.csv' )
	df_store_raw = pd.read_csv( '/home/victor/repos/DataScience_Em_Producao/data/store.csv' )

	# merge test dataset + store
	df_test = pd.merge( df10, df_store_raw, how='left', on='Store' )

	# choose store for prediction
	df_test = df_test[df_test['Store'] == store_id]



	# remove closed days
	df_test = df_test[df_test['Open'] != 0]
	df_test = df_test[~df_test['Open'].isnull()]
	df_test = df_test.drop( 'Id', axis=1 )

	# convert Dataframe to json
	data = json.dumps( df_test.to_dict( orient='records' ) )
	
	return data

def predict(data):
# API Call
	url = 'https://rossmann-model-test-victor.herokuapp.com/rossmann/predict'
	header = {'Content-type': 'application/json' } 
	data = data

	r = requests.post( url, data=data, headers=header )
	print( 'Status Code {}'.format( r.status_code ) )

	d1 = pd.DataFrame( r.json(), columns=r.json()[0].keys() )
	
	return d1
	

#d2 = d1[['store', 'prediction']].groupby( 'store' ).sum().reset_index()

#for i in range( len( d2 ) ):
#    print( 'Store Number {} will sell R${:,.2f} in the next 6 weeks'.format( 
#            d2.loc[i, 'store'], 
#            d2.loc[i, 'prediction'] ) )