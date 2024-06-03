import logging
import psycopg2

def db_quaery(car_plate_number: str) -> bool:
    '''Функиция запроса в БД с проверкой доступа входящего номера'''
    access_result = False
    try:
        connection = psycopg2.connect(host = 'localhost', port = 5432, user = 'postgres', password = '123456789',
                                      database = 'VehicleAccessControlComplex')
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM vacc WHERE car_plate_number = %s;', (car_plate_number,))
            if cursor.fetchall(): access_result = True
    except Exception: logging.error('Ошибка запроса в БД: {}'.format(Exception))
    finally:
        if connection:
            connection.close()
    return access_result


if __name__ == '__main__':
    print(db_quaery('X343TT161'))
    print(db_quaery('A318KM761'))
    print(db_quaery('O069AM761'))