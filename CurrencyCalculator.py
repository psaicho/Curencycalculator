# Potrzebujemy przeliczyć trochę waluty, czasy niepewne,
# warto mieć na uwadze swoją ulubioną walutę.
# Napisz klasę, która będzie zawierać dwie metody:

#       przeliczenie wybranej waluty z tabeli A na złotówki  <- dane wejściowe: kod waluty, ilość waluty
#       wskazanie aktualnego kursu z tabeli A <- dane wjećiowe: kod waluty

# Klasa w celu przeliczenia waluty powinna skorzystać z aktualnych kursów z Narodowego Banku Polskiego
# dokumentację API dla NBP znajdziesz pod adresem http://api.nbp.pl/

# Gdy skończysz prześlij mi swoje zadanie w postaci linku do swojego GitHuba, innych linków nie przyjmuję :)
# Na rozwiązanie czekam do końca dnia do niedzieli 22.01.2023


import json
import requests # need to install this package
# import of necessary libraries


class Currencycalculator():
    format = 'json'
    table = 'A'

    def exchange_currency_calculator(self, currency_code: str, amount: float) -> float:
        return round(self.current_course(currency_code) * amount, 4)

    def current_course(self, currency_code: str) -> float:
        url = 'http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/today/?format={format}' \
            .format(table=self.table, code=currency_code, format=self.format)
        return json.loads(requests.get(url).text)['rates'][0]['mid']
        # I used one line of code so as not to allocate memory for unnecessary data