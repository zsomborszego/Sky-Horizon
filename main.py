from datetime import datetime, timedelta
from Airline import Airline
from TicketReservation import TicketReservation

def main():
    airline = Airline("Sky Horizon")

    first_plane_seed = airline.create_domestic_flight("Budapest", "Debrecen", 50, 30_000,
                                                      datetime.now() + timedelta(days=5))
    first_plane_seed.booking("Márk Géza")
    first_plane_seed.booking("Álmos Elemér")

    second_plane_seed = airline.create_domestic_flight("Győr", "Pécs", 50, 52_000, datetime.now() + timedelta(days=3))
    second_plane_seed.booking("Kiss Gábor")
    second_plane_seed.booking("Nagy Etel")

    third_plane_seed = airline.create_international_flights("Budapest", "Isztambul", 80, 140_700,
                                                            datetime.now() + timedelta(days=2))
    third_plane_seed.booking("Elek Nóra")
    third_plane_seed.booking("Kovács Viktor")

    # fixture flight numbers
    first_plane_seed_number = first_plane_seed._Flight__flight_number
    first_plane_seed._Flight__flight_number = 'SH-80879'
    airline._Airline__domestic_flights['SH-80879'] = airline._Airline__domestic_flights.pop(first_plane_seed_number)

    second_plane_seed_number = second_plane_seed._Flight__flight_number
    second_plane_seed._Flight__flight_number = 'SH-80889'
    airline._Airline__domestic_flights['SH-80889'] = airline._Airline__domestic_flights.pop(second_plane_seed_number)

    third_plane_seed_number = third_plane_seed._Flight__flight_number
    third_plane_seed._Flight__flight_number = 'SH-80909'
    airline._Airline__international_flights['SH-80909'] = airline._Airline__international_flights.pop(
        third_plane_seed_number)
    third_plane_seed._Flight__date = datetime(2024, 1, 1)

    booking_system = TicketReservation(airline)
    booking_system.start()


if __name__ == "__main__":
    main()
