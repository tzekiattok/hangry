
from invokes import invoke_http

# invoke book microservice to get all books
results = invoke_http("http://localhost:5002/request_reservation/Bartok/17")
results2 = invoke_http("http://localhost:5002/reservationID/11")
print( type(results) )
print()
print( results )
print( results2 )
