# Ohjelmistotekniikka, harjoitustyö

__Finanssit__, on _henkilökohtaisen talouden seurantasovellus_, missä voit seurata oman talouden kehitystä ja rakennetta.

### Versiot
- [Viikko 5](https://github.com/mpajuka/finanssit/releases/tag/viikko5)
- [Viikko 6](https://github.com/mpajuka/finanssit/releases/tag/viikko6)

## Dokumentaatio
- [Arkkitehtuuri](https://github.com/mpajuka/finanssit/blob/main/dokumentaatio/arkkitehtuuri.md)
- [Changelog](https://github.com/mpajuka/finanssit/blob/main/dokumentaatio/changelog.md)
- [Työaikakirjanpito](https://github.com/mpajuka/finanssit/blob/main/dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](https://github.com/mpajuka/finanssit/blob/main/dokumentaatio/vaatimusmaarittely.md)



## Ohjelman käyttö
> [!IMPORTANT]
> Ohjelman suoritus vaatii vähintään Python 3.10 tai uudemman
### Asennus
- Ympäristön riippuvuudet
```bash
poetry install
```
- Tietokannan alustaminen
```bash
poetry run invoke build
```
- Ohjelman käynnistäminen
```bash
poetry run invoke start
```

### Testien suorittaminen
```bash
poetry run invoke test
```

### Laatutarkistusten suorittaminen
```bash
poetry run invoke lint
```

### Testikattavuusraportin muodostaminen
```bash
poetry run invoke coverage-report
```

### Lähdekoodin formatointi
```bash
poetry run invoke autopep-format
```
