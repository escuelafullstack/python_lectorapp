from functools import reduce
ventas = [
    {"id":"001","customer_id":"001","lines":[{"product_id":"004","price":20},{"product_id":"003","price":45}]},
    {"id":"002","customer_id":"002","lines":[{"product_id":"003","price":23}]},
    {"id":"003","customer_id":"003","lines":[{"product_id":"005","price":24}]},
    {"id":"004","customer_id":"004","lines":[{"product_id":"001","price":22}]},
    {"id":"005","customer_id":"001","lines":[{"product_id":"004","price":12},{"product_id":"004","price":25}]},
    {"id":"006","customer_id":"002","lines":[{"product_id":"003","price":55}]},
    {"id":"007","customer_id":"003","lines":[{"product_id":"001","price":23}]},
    {"id":"008","customer_id":"002","lines":[{"product_id":"004","price":15}]},
    {"id":"009","customer_id":"002","lines":[{"product_id":"005","price":18}]}
]

customer_id = "001"
filtro_cliente = filter(lambda r:r["customer_id"]==customer_id,ventas)
map_cliente = map(lambda r:{"id":r["id"],
                            "customer_id":r["customer_id"],
                            "total":sum([x["price"] for x in r["lines"]])},
                            filtro_cliente)
print(list(map_cliente))
#¿Cuanto es el monto total por client?