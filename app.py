from flask import Flask, jsonify, request
import whois
import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/domaininfo', methods=['GET'])
def get_domaininfo():
    url = None
    url = request.args.get('url', type=str)

    if url == None:
        return 'url parameter is required', 400
    print(url)
    domain = whois.query(url)
    data = domain.__dict__
    if data['creation_date'] != None :
        data['creation_date'] = data['creation_date'].strftime("%d-%b-%Y (%H:%M:%S.%f)")
    if data['expiration_date']!= None :
        data['expiration_date'] = data['expiration_date'].strftime("%d-%b-%Y (%H:%M:%S.%f)")
    if data['last_updated'] != None :
        data['last_updated'] = data['last_updated'].strftime("%d-%b-%Y (%H:%M:%S.%f)")
    data.pop('name_servers')
    
    return data
    #return jsonify()


@app.route('/domainname', methods=['GET'])
def get_domainname():
    url = None
    url = request.args.get('url', type=str)

    if url == None:
        return 'url parameter is required', 400
    
    domain = whois.query(url)
    data = domain.name
    
    return jsonify(data)

@app.route('/domainexpiry', methods=['GET'])
def get_domainexpiry():
    url = None
    url = request.args.get('url', type=str)

    if url == None:
        return 'url parameter is required', 400
    
    domain = whois.query(url)
    data = domain.expiration_date

    return jsonify(data)

@app.route('/domaincreation', methods=['GET'])
def get_domaincreation():
    url = None
    url = request.args.get('url', type=str)

    if url == None:
        return 'url parameter is required', 400
    
    domain = whois.query(url)
    data = domain.creation_date

    return jsonify(data)

@app.route('/domainregistrar', methods=['GET'])
def get_domainregistrar():
    url = None
    url = request.args.get('url', type=str)

    if url == None:
        return 'url parameter is required', 400
    
    domain = whois.query(url)
    data = domain.registrar

    return jsonify(data)

@app.route('/domainstatus', methods=['GET'])
def get_domainstatus():
    url = None
    url = request.args.get('url', type=str)

    if url == None:
        return 'url parameter is required', 400
    
    domain = whois.query(url)
    data = domain.status
    return jsonify(data)

if __name__ == '__main__':
    app.run(threaded=True, port=5000)