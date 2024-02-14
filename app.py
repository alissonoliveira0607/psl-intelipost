import logging
import requests
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# Configuração do arquivo de logs
logging.basicConfig(filename='./app.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

@app.route('/psl', methods=['POST'])
def receive_psl():
    try:
        data = request.json
        
        intelipost_pre_shipment_list = data.get('intelipost_pre_shipment_list')
        shipment_order_array = data.get('shipment_order_array',[])
        
        shipment_list_creation_date = datetime.now().strftime('%Y-%m-%dT%H:%M:%S-03:00')
        
        random_hash = str(uuid.uuid4())
        
        response_data = {
            'intelipost_pre_shipment_list': intelipost_pre_shipment_list,
            'logistics_provider_shipment_list': intelipost_pre_shipment_list,
            'shipment_list_creation_date': shipment_list_creation_date,
            'orders_array': [],
            "status": "OK",
            "messages": [{"type": "SUCCESS", "text": u"Operação realizada com sucesso.", "key": "success.message"}],
            "hash": random_hash
        }
        
        for order in shipment_order_array:
            order_number = order.get("order_number")
            shipment_order_volume_array = order.get("shipment_order_volume_array", [])
            order_data = {
                "order_number": order_number,
                "shipment_order_volume_array": []
            }
            for volume in shipment_order_volume_array:
                shipment_order_volume_number = volume.get("shipment_order_volume_number")
                tracking_code = volume.get("tracking_code", None) 
                volume_data = {
                    "shipment_order_volume_number": shipment_order_volume_number,
                    "tracking_code": tracking_code
                }
                order_data["shipment_order_volume_array"].append(volume_data)
            
            response_data["orders_array"].append(order_data)
        
        logging.info(f'Request: {request.json}')
        logging.info(f'Response: {response_data}')
        
        return jsonify(response_data), 200, {'Content-Type': 'application/json; charset=utf-8'}
    
    except Exception as e:
        logging.error(f'Erro durante a execução da aplicação: {e}', exc_info=True)
        return jsonify({"error": "Erro interno do servidor"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
