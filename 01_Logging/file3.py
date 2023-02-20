import logging
logging.basicConfig(filename="file31.log",level=logging.INFO, format=('%(asctime)s - %(name)s  - %(levelname)s  %(message)s'))
# logging.basicConfig(filename="file3.log",level=logging.INFO, format=('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

print("This is python using VS_CODE and learning logging")

try:
    a = int(input("Enter the value of a :"))
    b = int(input("Enter the value of b :"))

    try:
        logging.info(f"Multiplying {a} * {b}")
        c = a * b
        logging.info(c)
    except:
        logging.info('Error while multiplication')
    
    try:
        logging.info(f"Division {a} / {b}")
        d = a / b
        logging.info(d)
        
    except ZeroDivisionError as ze:
        logging.info(ze)
        
    try:
        logging.info(f"Addition {a} + {b}")
        e = a + b
        logging.info(e)
    except:
        logging.info('Error while addition')
    
except:
    logging.info("Error in your program check the input")