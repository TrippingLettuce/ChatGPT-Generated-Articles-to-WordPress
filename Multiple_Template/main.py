import time
import beach
import citys
import hotels
import money
import places

while True:
    try:
        citys.citys_run()
        beach.beach_run()
        hotels.hotel_run()
        places.place_run()
        money.money_run()
        time.sleep(5 * 60 * 60) # sleep for 5 hours
    except Exception as e:
        logging.error(f'Error: {e}')
        time.sleep(60) # sleep for 1 minute before retrying
