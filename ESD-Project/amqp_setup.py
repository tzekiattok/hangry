import pika

# These module-level variables are initialized whenever a new instance of python interpreter imports the module;
# In each instance of python interpreter (i.e., a program run), the same module is only imported once (guaranteed by the interpreter).
hostname = "localhost" # default hostname
port = 5672 # default port
    # connect to the broker and set up a communication channel in the connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=hostname, port=port,
        heartbeat=3600, blocked_connection_timeout=3600, # these parameters to prolong the expiration time (in seconds) of the connection
))
exchangename="order_topic"
exchangetype="topic"
    
channel = connection.channel()
queue_name = 'restaurant'
channel.queue_declare(queue=queue_name, durable=True) 
channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key='*.restaurant')
queue_name = 'customer'
channel.queue_declare(queue=queue_name, durable=True) 
channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key='*.customer')
'''
queue_name = 'EighteenChefz'
channel.queue_declare(queue=queue_name, durable=True) 
channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key=queue_name)
queue_name = 'Mala123'
channel.queue_declare(queue=queue_name, durable=True) 
channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key=queue_name)
queue_name = 'WeiZhi'
channel.queue_declare(queue=queue_name, durable=True) 
channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key=queue_name)
queue_name = 'XJWangz'
channel.queue_declare(queue=queue_name, durable=True) 
channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key=queue_name)'''
'''def createQueue(restID):
    hostname = "localhost" # default hostname
    port = 5672 # default port
    # connect to the broker and set up a communication channel in the connection
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=hostname, port=port,
            heartbeat=3600, blocked_connection_timeout=3600, # these parameters to prolong the expiration time (in seconds) of the connection
    ))
    
    channel = connection.channel()
    # Set up the exchange if the exchange doesn't exist
    # - use a 'topic' exchange to enable interaction
    exchangename="order_topic"
    exchangetype="topic"
    channel.exchange_declare(exchange=exchangename, exchange_type=exchangetype, durable=True)

    queue_name = restID
    channel.queue_declare(queue=queue_name, durable=True) 
    channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key=restID)'''
    

"""
This function in this module sets up a connection and a channel to a local AMQP broker,
and declares a 'topic' exchange to be used by the microservices in the solution.
"""
def check_setup():
    # The shared connection and channel created when the module is imported may be expired, 
    # timed out, disconnected by the broker or a client;
    # - re-establish the connection/channel is they have been closed
    global connection, channel, hostname, port, exchangename, exchangetype

    if not is_connection_open(connection):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port))
    if channel.is_closed:
        channel = connection.channel()
        channel.exchange_declare(exchange=exchangename, exchange_type=exchangetype)


def is_connection_open(connection):
    # For a BlockingConnection in AMQP clients,
    # when an exception happens when an action is performed,
    # it likely indicates a broken connection.
    # So, the code below actively calls a method in the 'connection' to check if an exception happens
    try:
        connection.process_data_events()
        return True
    except pika.exceptions.AMQPError as e:
        print("AMQP Error:", e)
        print("...creating a new connection.")
        return False
