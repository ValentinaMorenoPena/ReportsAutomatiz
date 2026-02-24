from config.settings import DATA_DIR

from services.contable import ContableService
from services.tesoreria import TesoreriaService
from services.valorizacion import ValorizacionService
from services.instrumentos import InstrumentosService


def main():
    print("🚀 Iniciando generación de reportes")
    print(f"📌 Origen de datos: {DATA_DIR}")

    fecha = "10/10/2025"
    print(f"📅 Fecha de proceso: {fecha}")

    base_path = DATA_DIR 

    # =========================
    # CONTABILIDAD
    # =========================
    print("\n➡️ Procesando CONTABILIDAD...")
    try:
        contable = ContableService(
            input_path=f"{base_path}/contabilidad/input/contabilidad.json",
            output_path=f"{base_path}/contabilidad/output/contabilidad.xlsx"
        )
        contable.process()

    except Exception as e:
        print(f"❌ Error procesando CONTABILIDAD: {e}")

    # =========================
    # TESORERÍA
    # =========================
    print("\n➡️ Procesando TESORERÍA...")
    try:
        tesoreria = TesoreriaService(
            input_path=f"{base_path}/tesoreria/input/tesoreria.json",
            output_path=f"{base_path}/tesoreria/output/tesoreria.xlsx"
        )
        tesoreria.process()

    except Exception as e:
        print(f"❌ Error procesando TESORERÍA: {e}")

    # =========================
    # VALORIZACIÓN
    # =========================
    print("\n➡️ Procesando VALORIZACIÓN...")
    try:
        valorizacion = ValorizacionService(
            input_path=f"{base_path}/valorizacion/input/valorizacion.json",
            output_path=f"{base_path}/valorizacion/output/valorizacion.xlsx"
        )
        valorizacion.process()

    except Exception as e:
        print(f"❌ Error procesando VALORIZACIÓN: {e}")

    # =========================
    # INSTRUMENTOS
    # =========================
    print("\n➡️ Procesando INSTRUMENTOS...")
    try:
        instrumentos = InstrumentosService(
            input_path=f"{base_path}/instrumentos/input/instrumentos.json",
            output_path=f"{base_path}/instrumentos/output/instrumentos.xlsx"
        )
        instrumentos.process()

    except Exception as e:
        print(f"❌ Error procesando INSTRUMENTOS: {e}")

    print("\n🏁 Proceso finalizado")


if __name__ == "__main__":
    main()