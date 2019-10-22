from blinktrade import clients

# classe para metodos públicos, 'PROD' = produção ou 'TEST'  = testnet, 'BRL' = símbolo, BITCAMBIO = '11' ou  TESTNET = '5'.
cam = clients.OpenClient('PROD', 'BRL', '11')
print(cam.get_ticker())
print(cam.get_order_book())
print(cam.get_trade_list())

# classe para metodos privados, PROD' = produção ou 'TEST'  = testnet, 'BRL' = símbolo, BITCAMBIO = '11' ou  TESTNET = '5', Chave, Segredo.
cam = clients.AuthClient('PROD', 'BRL', '11', '<Chave>', '<Segredo>')
print(cam.get_executed_orders())
print(cam.get_pending_orders())
print(cam.get_balance())
# print(cam.buy_bitcoins_with_limited_order(price=45000, quantity=0.01))