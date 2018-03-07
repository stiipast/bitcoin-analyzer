#!/usr/bin/python
import urllib, json, time, sys
import mysql.connector


def obtindre_block(block_index):

    # Guardarem els valors en llistes per despres poder utilitzar els valors per fer estadistiques (encara no els he utilitzat)
    in_tx=[]
    out_tx=[]
    fee=[]
    temps=[]
    conndb = mysql.connector.connect(user='bitcoin', database='bitcoin') #fem la connexio amb la DB
    cursor = conndb.cursor() # fem un cursor per a insertar les dades a la DB

    data = json.loads(urllib.urlopen("http://blockchain.info/rawblock/" + block_index).read())  # Descarreguem el bloc

    # Obtenim la data del block en format llegible

    block_date = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(int(data['time'])))
    block_received_time = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(int(data['received_time'])))

    for t in range(len(data["tx"])):    # recorrem el bloc, la variable t recorre cada trasaccio
        in_tx_temp = 0  # inicialitzem el sumatori del valor dels inputs de la transaccio t
        out_tx_temp = 0 # inicialitzem el sumatori del valor dels outputs de la transaccio t
        fee_temp = 0
        temps_temp = 0
        i=0 # variable per a recorrer els inputs
        j=0 # variable per a recorrer els outputs
        for i in range(len(data['tx'][t]['inputs'])):
            if(t!=0):
               in_tx_temp=in_tx_temp + data['tx'][t]['inputs'][i]['prev_out']['value'] # sumem al valor de input el nou valor per a cada input
        in_tx.append(in_tx_temp)
        for j in range(len(data['tx'][t]['out'])):
            out_tx_temp = out_tx_temp + data['tx'][t]['out'][j]['value']  # sumem els outputs
        out_tx.append(out_tx_temp)
     #   fee = (in_tx - out_tx) / 100000000.0  # fem la resta per obtindre la diferencia que son les fees i dividim per obtindre el valor en BTC
        if(t==0):
            fee_temp = out_tx_temp
        else:
            fee_temp = in_tx_temp - out_tx_temp
        fee.append(fee_temp)
        temps_temp = data['time'] - data['tx'][t]['time']
        temps.append(temps_temp) # Temps en segons que triga la transaccio en fer-se efectiva (temps de bloc - temps de tx)
     #  print "%s \t %s \t %s \t %s \t %s \t %s \t %s \t %s" %(data['block_index'], data['height'], data['hash'], t, in_tx[t], out_tx[t], fee[t], temps[t])


        tx_date = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(int(data['tx'][t]['time'])))

        # Construim les dades que introduim a la DB

        add_tx = ("INSERT INTO transaccions "
               "(block_index, block_date, altura, hash, tx_hash, tx_index, relayed_by, n_inputs, input, n_outputs, output, tx_date, fee, temps) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

        data_tx = (data['block_index'], block_date, data['height'], data['hash'], data['tx'][t]['hash'], t, data['tx'][t]['relayed_by'], len(data['tx'][t]['inputs']), in_tx[t], len(data['tx'][t]['out']), out_tx[t], tx_date, fee[t], temps[t])
        cursor.execute(add_tx, data_tx)

    # Una volta hem fet totes les tx del block enviem les dades a la DB i tamquem el cursor i la connexio

    add_block = ("INSERT INTO blocks "
            "(block_index, block_date, block_received_time, height, hash, bits, n_tx, fee, size, main_chain, relayed_by) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

    data_block = (data['block_index'], block_date, block_received_time, data['height'], data['hash'], data['bits'], data['n_tx'], data['fee'], data['size'], data['main_chain'], data['relayed_by'])
    cursor.execute(add_block, data_block)

    conndb.commit()
    cursor.close()
    conndb.close()
    return data['prev_block']  # Tornem el hash del bloc anterior al actual

# Cos principal del programa
if (len(sys.argv)) < 2:
    latest_block = json.loads(urllib.urlopen("http://blockchain.info/latestblock").read())
    block_index=str(latest_block["block_index"]) # Obtenim el index del ultim bloc generat
else:
    if (len(sys.argv[1])) != 64:
        print "El hash es incorrecte"
        exit()
    else:
        block_index = sys.argv[1]

print "Block_index \t Altura \t Hash \t Tx_Index \t input \t output \t fee \t temps"
z = 0

if
while z < 100: #obtenim els 100 primers blocks de la cadena
    block_index = obtindre_block(block_index)
    z += 1