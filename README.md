Web applikasjon for å visualisere data
==============================
*Av Isabel Burgos*

----
Sist oppdatert: 05.12.24
----

# Table of contents
1. [Hvordan bygge applikasjonen](#hvordan-bygge-applikasjonen)
2. [Hvordan kjøre applikasjonen](#hvordan-kjøre-applikasjonen)
3. [Informasjon](#informasjon)


# Hvordan bygge applikasjonen
For å løse denne oppgaven har jeg tatt i bruk rammeverket Streamlit ([docs](https://docs.streamlit.io/)), et redskap for å bygge datadrevne webapplikasjoner. Streamlit gir god støtte til frontend utviklingen, og tilbyr interaktive grensesnitt. Streamlit opererer med Pandas dataframes ([docs](https://pandas.pydata.org/docs/reference/frame.html)) for prosessering av data.

I dette tilfellet har jeg hovedsaklig tatt i bruk Streamlit's ['basic concepts'](https://docs.streamlit.io/get-started/fundamentals/main-concepts), men det er også mulig å legge til mer [avanserte prosesser](https://docs.streamlit.io/get-started/fundamentals/advanced-concepts), som caching, etc.

# Hvordan kjøre applikasjonen
For å forsikre at man har de nødvendige rammeverkene, bør man kjøre følgende kode i cmd-line:
```python
pip install -r /path/to/requirements.txt
```

For å kjøre programfil fra cmd-line og åpne webapplikasjonen:
1. Sett working directory til `.../ET_Fagoppgave/src`

2. Kjør følgene i cmd-line. Dette vil åpne webapplikasjonen i din browser.
```python
streamlit run main.py
```

Filen fortsetter å kjøre frem til man avslutter prosessen med 'Ctrl+c'. Mens programmet kjører vil endringer i koden ummiddelbart kunne lastes opp i web applikasjonen når de relevante filene er lagret. 

# Informasjon
## Antakelser
Jeg har gjort følgende antagelser under utviklingen av løsningen.
- ccnummer står for credit card number
- lat/long koordinater er hvor kortet er blitt brukt
- resterende informasjon er personlig informasjon om eieren av kortet

## Fremgangsmåte
Jeg valgte å lage to sider i applikasjonen. 

Hovedsiden viser brukeren datasettet, samt gir brukeren mulighet til å filtrere og sortere dataene. Er det ønsket kan brukeren her også søke etter konkrete verdier i datasettet. Søket kan bli gjort i hele datasettet eller i en spesifikk kolonne.

Statistikk og analyse er lagt i en egen side i applikasjonen. Her har jeg lagt fokus på informasjon jeg mener ville være mest relevant ut i fra datasettet.
1. Manglende verdier: Manglende verdier vil påvirke muligheten til å analyserer datasettet og kan også peke mot at noe er galt.
2. Delte kredittkortnumre: Skulle det være slik at flere personer er registrert på samme kredittkort kan dette gi innsikt i eventuelle familiemedlemmer, samarbeidspartnere, eller nettverk.
3. Personer med samme navn: Dette kan så klart være forskjellige personer, men det er også mulig at det er noen som forsøker å drive med svindel, el. Derfor vil det være verdt å undersøke. Man kan i tillegg sjekke om andre verdier i de relevante radene i datasettet er tilsvarende.
4. Lignende koordinater: Flere transacsjoner registrert på samme koordinater eller som viser et distinkt mønster kan være relevant å undersøke. Har man tilgang på dato og tid, vil det også være relevant å sjekke om samme kort er blitt bruk på svært forskjellige lokasjoner.
5. Alder: Lagt til for å få en oversikt over demografien i datasettet. Store transaksjoner fra yngre personer (som typisk har lav inntekt) kan for eksempel være en situasjon man gjerne vil undersøke.
6. Stat: Lagt til for å få en oversikt over demografien i datasettet.
