# Chess Helper

Chess Helper to program do pomocy przy grze w szachy.
Dzięki niemu można sprawdzić kombinację możliwych ruchów określonej
figury na określonym polu.

## Przygotowanie do uruchomienia

Przed rozpoczęciem należy zainstalować wymagane zależności.
Wystarczy wydać w terminalu poniższe polecenie, aby zainstalować wszystkie
wymagane pakiety.

```bash
    pip3 install -r requirements.txt
```

lub

```bash
    pip install -r requirements.txt
```

## Uruchomienie
Wystarczy wydać polecenie:

```bash
    python3 app.py
```

## Jak używać?
Wystarczy wpisać odpowiedni adres internetowy do przeglądarki
lub użyć narzędzia curl, np.:

```bash
    curl http://localhost:5000/api/v1/{chess-figure}/{field}
```

Gdzie pod chess-figure podstawiamy nazwę figury, a pod field podstawiamy
pole jakie nas interesuje.