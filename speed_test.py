import speedtest

def measure_bandwidth():
    """
    Mide el ancho de banda de descarga y carga de la red actual.
    """
    try:
        st = speedtest.Speedtest()
        st.get_best_server()

        print("Midiendo la velocidad de descarga...")
        download_speed = st.download() / 1_000_000  # Convertir a Mbps

        print("Midiendo la velocidad de carga...")
        upload_speed = st.upload() / 1_000_000  # Convertir a Mbps

        ping = st.results.ping

        print("\n--- Resultados del Test de Velocidad ---")
        print(f"Descarga: {download_speed:.2f} Mbps")
        print(f"Carga: {upload_speed:.2f} Mbps")
        print(f"Ping: {ping:.2f} ms")
        print("------------------------------------")

    except speedtest.ConfigRetrievalError:
        print("Error: No se pudo conectar al servidor de Speedtest. Verifica tu conexión a internet.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    measure_bandwidth()
