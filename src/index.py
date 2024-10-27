from varasto import Varasto

def olut_getterit(varasto):
    print("Olut getterit:")
    print(f"saldo = {varasto.saldo}")
    print(f"tilavuus = {varasto.tilavuus}")
    print(f"paljonko_mahtuu = {varasto.paljonko_mahtuu()}")

def mehu_setterit(varasto):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    varasto.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {varasto}")
    print("Otetaan 3.14")
    varasto.ota_varastosta(3.14)
    print(f"Mehuvarasto: {varasto}")

def virheita():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

def lisaa_olutta(varasto):
    print(f"Olutvarasto: {varasto}")
    print("olutta.lisaa_varastoon(1000.0)")
    varasto.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {varasto}")

def lisaa_mehua(varasto):
    print(f"Mehuvarasto: {varasto}")
    print("mehua.lisaa_varastoon(-666.0)")
    varasto.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {varasto}")

def ota_olutta(varasto):
    print(f"Olutvarasto: {varasto}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = varasto.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {varasto}")

def ota_mehua(varasto):
    print(f"Mehuvarasto: {varasto}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = varasto.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {varasto}")

def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

    olut_getterit(olutta)

    mehu_setterit(mehua)

    virheita()

    lisaa_olutta(olutta)
    lisaa_mehua(mehua)

    ota_olutta(olutta)
    ota_mehua(mehua)


if __name__ == "__main__":
    main()
