from datetime import date, datetime


def get_transacciones():
    return [{"fecha": "2022-01-01", "monto": 100.00, "tarjeta": "1234-5678-9012-3456"},
            {"fecha": "2022-01-02", "monto": 50.00,
                "tarjeta": "2345-6789-0123-4567"},
            {"fecha": "2022-01-03", "monto": 75.00,
                "tarjeta": "3456-7890-1234-5678"},
            {"fecha": "2022-01-04", "monto": 200.00,
                "tarjeta": "4567-8901-2345-6789"},
            {"fecha": "2022-01-05", "monto": 150.00,
                "tarjeta": "5678-9012-3456-7890"},
            {"fecha": "2022-01-06", "monto": 125.00,
                "tarjeta": "6789-0123-4567-8901"},
            {"fecha": "2022-01-07", "monto": 75.00,
                "tarjeta": "7890-1234-5678-9012"},
            {"fecha": "2022-01-08", "monto": 50.00,
                "tarjeta": "8901-2345-6789-0123"},
            {"fecha": "2022-01-09", "monto": 225.00,
                "tarjeta": "9012-3456-7890-1234"},
            {"fecha": "2022-01-10", "monto": 175.00,
                "tarjeta": "0123-4567-8901-2345"}
            ]

def filter_by_date(transaccions, start_time: datetime, end_time: datetime) -> list[dict]:
    print(start_time, end_time)
    return [transaccion for transaccion in transaccions if start_time >= datetime.fromisoformat(transaccion["fecha"]) <= end_time]


def sum_ammount_transaccions(transaccions: list[dict]) -> float:
    sum_ammounts: float = float(sum([ammount["monto"] for ammount in transaccions]))
  
    return sum_ammounts



def main():
    transaccions = get_transacciones()

    filter_transaccions = filter_by_date(
        transaccions, datetime.fromisoformat("2022-01-03"), datetime.fromisoformat("2022-01-08"))
    
    print(filter_transaccions)

    sum_filter_ammounts = sum_ammount_transaccions(filter_transaccions)
    print(sum_filter_ammounts)


if __name__ == "__main__":
    main()
   
    
  
