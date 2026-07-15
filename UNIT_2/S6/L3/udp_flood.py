import ipaddress
import random
import socket
import time

DIMENSIONE_PACCHETTO = 1024       
MASSIMO_PACCHETTI = 99999
INTERVALLO_INVIO = 0.000000001     


def leggi_ip_target():
    
    valore = input("Inserisci l'IP della macchina target: ").strip()

    try:
        indirizzo = ipaddress.ip_address(valore)
    except ValueError as errore:
        raise ValueError("L'indirizzo IP inserito non è valido.") from errore

    if indirizzo.version != 4:
        raise ValueError("Questo programma supporta solamente indirizzi IPv4.")

    

    return str(indirizzo)


def leggi_porta_target():
    
    try:
        porta = int(input("Inserisci la porta UDP target: ").strip())
    except ValueError as errore:
        raise ValueError("La porta deve essere un numero intero.") from errore

    if not 1 <= porta <= 65535:
        raise ValueError("La porta deve essere compresa tra 1 e 65535.")

    return porta


def leggi_numero_pacchetti():
    
    try:
        numero = int(
            input(
                f"Quanti pacchetti da 1 KB vuoi inviare "
                f"(massimo {MASSIMO_PACCHETTI})? "
            ).strip()
        )
    except ValueError as errore:
        raise ValueError(
            "Il numero di pacchetti deve essere un intero."
        ) from errore

    if not 1 <= numero <= MASSIMO_PACCHETTI:
        raise ValueError(
            f"Il numero deve essere compreso tra 1 e {MASSIMO_PACCHETTI}."
        )

    return numero


def genera_pacchetto():
    
    return bytes(
        random.getrandbits(8)
        for _ in range(DIMENSIONE_PACCHETTO)
    )


def invia_pacchetti(ip_target: str, porta: int, numero: int):
   
    indirizzo_target = (ip_target, porta)
    pacchetti_inviati = 0
    byte_inviati = 0
    inizio = time.monotonic()

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        print(
            f"\nInvio controllato verso {ip_target}:{porta}..."
        )

        try:
            for indice in range(1, numero + 1):
                pacchetto = genera_pacchetto()
                byte_spediti = sock.sendto(pacchetto, indirizzo_target)

                pacchetti_inviati += 1
                byte_inviati += byte_spediti

                if indice == 1 or indice % 100 == 0 or indice == numero:
                    print(
                        f"Pacchetti inviati: {indice}/{numero}",
                        end="\r",
                        flush=True,
                    )

                time.sleep(INTERVALLO_INVIO)

        except KeyboardInterrupt:
            print("\nInvio interrotto dall'utente.")

    durata = time.monotonic() - inizio

    print("\n\nRiepilogo:")
    print(f"Target: {ip_target}:{porta}/UDP")
    print(f"Pacchetti inviati: {pacchetti_inviati}")
    print(f"Dimensione per pacchetto: {DIMENSIONE_PACCHETTO} byte")
    print(f"Totale inviato: {byte_inviati} byte")
    print(f"Durata: {durata:.2f} secondi")


def main():
    
    try:
        ip_target = leggi_ip_target()
        porta_target = leggi_porta_target()
        numero_pacchetti = leggi_numero_pacchetti()

        invia_pacchetti(
            ip_target,
            porta_target,
            numero_pacchetti,
        )

    except ValueError as errore:
        print(f"\nErrore: {errore}")
    except OSError as errore:
        print(f"\nErrore di rete: {errore}")


if __name__ == "__main__":
    main()