# Program Web Scraping Data Covid-19
# Menampilkan data covid-19 di Indonesia yang telah diambil dan diolah
# dari server API dengan menggunakan metode web scraping

import requests
import json

# KAMUS
# Indonesia             : string
# DKI_Jakarta           : string
# Jawa_Barat            : string
# Jawa_Tengah           : string
# Jawa_Timur            : string
# Kalimantan_Timur      : string
# isRunning             : bool
# inputLokasi           : int
# inputPengguna         : int
# indeks                : int
# lanjut                : string
# inputProvinsi         : int
# namaProvinsi          : string
# tanggalAwalKasus      : string
# inputPenggunaProvinsi : int

# Fungsi data_covid
def data_covid(endpoint):
    # Mengakses data di server API

    # KAMUS LOKAL
    # response  : requests.models.Response
    # data      : dictionary

    # ALGORITMA
    response = requests.get(endpoint)
    data = json.loads(response.text)
    return data

# DATA INDONESIA
# Fungsi TotalIndo
def TotalIndo():
    # Menghasilkan data total covid-19 di Indonesia

    # KAMUS LOKAL
    # update            : dictionary
    # total, penambahan : int
    # tanggal           : string
    # total_positif     : int
    # total_meninggal   : int
    # total_sembuh      : int
    # total_dirawat     : int
    # output_total_indo : string

    # ALGORITMA
    update = data_covid(Indonesia).get("update")
    total = update.get("total")
    penambahan = update.get("penambahan")
    tanggal = penambahan.get("tanggal")
    total_positif = total.get("jumlah_positif")
    total_meninggal = total.get("jumlah_meninggal")
    total_sembuh = total.get("jumlah_sembuh")
    total_dirawat = total.get("jumlah_dirawat")
    output_total_indo = f"Data Total Covid hingga tanggal {tanggal} : \nJumlah Positif : {total_positif}\nJumlah Dirawat : {total_dirawat}\nJumlah Sembuh : {total_sembuh}\nJumlah Meninggal : {total_meninggal}\n"
    return output_total_indo

# Fungsi PertambahanHarianIndo
def PertambahanHarianIndo():
    # Menghasilkan data pertambahan harian covid-19 di Indonesia

    # KAMUS LOKAL
    # update                : dictionary
    # penambahan            : int
    # tanggal               : string
    # penambahan_positif    : int
    # penambahan_meninggal  : int
    # penambahan_sembuh     : int
    # penambahan_dirawat    : int
    # output_harian_indo    : string

    # ALGORITMA
    update = data_covid(Indonesia).get("update")
    penambahan = update.get("penambahan")
    tanggal = penambahan.get("tanggal")
    penambahan_positif = penambahan.get("jumlah_positif")
    penambahan_meninggal = penambahan.get("jumlah_meninggal")
    penambahan_sembuh = penambahan.get("jumlah_sembuh")
    penambahan_dirawat = penambahan.get("jumlah_dirawat")
    output_harian_indo = f"Data Penambahan Kasus Covid pada tanggal {tanggal} : \nPertambahan Kasus Positif : {penambahan_positif}\nPertambahan Kasus Dirawat : {penambahan_dirawat}\nPertambahan Kasus Sembuh : {penambahan_sembuh}\nPertambahan Kasus Meninggal : {penambahan_meninggal}\n"
    return output_harian_indo

# Fungsi PertambahanHariTertentuIndo
def PertambahanHariTertentuIndo(indeks):
    # Menghasilkan data pertambahan harian tertentu
    # covid-19 di Indonesia dari indeks

    # KAMUS LOKAL
    # update                    : dictionary
    # arrHarian                 : array of dictionary
    # arr_positif_harian        : array of int
    # temp                      : int
    # arr_dirawat_harian        : array of int
    # arr_sembuh_harian         : array of int
    # arr_meninggal_harian      : array of int
    # output_hari_tertentu_indo : string

    # ALGORITMA
    update = data_covid(Indonesia).get("update")
    # Memasukkan data positif harian ke array data harian positif
    arrHarian = update.get("harian")
    arr_positif_harian = [2]
    temp = 0
    for i in range(1, len(arrHarian)):
        temp = arrHarian[i].get("jumlah_positif").get("value")
        arr_positif_harian.append(temp)

    # Memasukkan data positif harian ke array data harian dirawat
    arr_dirawat_harian = [2]
    temp = 0
    for j in range(1, len(arrHarian)):
        temp = arrHarian[j].get("jumlah_dirawat").get("value")
        arr_dirawat_harian.append(temp)

    # Memasukkan data positif harian ke array data harian sembuh
    arr_sembuh_harian = [0]
    temp = 0
    for k in range(1, len(arrHarian)):
        temp = arrHarian[k].get("jumlah_sembuh").get("value")
        arr_sembuh_harian.append(temp)

    # Memasukkan data positif harian ke array data harian meninggal
    arr_meninggal_harian = [2]
    temp = 0
    for l in range(1, len(arrHarian)):
        temp = arrHarian[l].get("jumlah_meninggal").get("value")
        arr_meninggal_harian.append(temp)

    output_hari_tertentu_indo = f"Jumlah data covid hari ke {indeks} \nJumlah Positif : {arr_positif_harian[indeks - 1]} \nJumlah Dirawat : {arr_dirawat_harian[indeks - 1]} \nJumlah Sembuh : {arr_sembuh_harian[indeks - 1]} \nJumlah Meninggal : {arr_meninggal_harian[indeks - 1]} \n"
    return output_hari_tertentu_indo


# DATA TOP 5 BESAR PROVINSI
# Fungsi TotalProvinsi
def TotalProvinsi(namaProvinsi):
    # Menghasilkan data total covid-19 dari namaProvinsi

    # KAMUS LOKAL
    # data                  : dictionary
    # tanggal               : string
    # provinsi              : string
    # total_positif         : int
    # total_meninggal       : int
    # total_sembuh          : int
    # total_dirawat         : int
    # output_total_provinsi : string

    # ALGORITMA
    data = data_covid(namaProvinsi)
    tanggal = data.get("last_date")
    provinsi = data.get("provinsi")
    total_positif = data.get("kasus_total")
    total_meninggal = data.get("meninggal_tanpa_tgl") + data.get("meninggal_dengan_tgl")
    total_sembuh = data.get("sembuh_tanpa_tgl") + data.get("sembuh_dengan_tgl")
    total_dirawat = ((data.get("list_perkembangan"))[-1]).get("AKUMULASI_DIRAWAT_OR_ISOLASI")
    output_total_provinsi = f"Data Total Covid di {provinsi} hingga tanggal {tanggal} : \nJumlah Positif : {total_positif}\nJumlah Dirawat : {total_dirawat}\nJumlah Sembuh : {total_sembuh}\nJumlah Meninggal : {total_meninggal}\n"
    return output_total_provinsi

# Data untuk pertambahan tiap provinsi
def PertambahanHarianProvinsi(namaProvinsi):
    # Menghasilkan data pertambahan harian covid-19 dari namaProvinsi

    # KAMUS LOKAL
    # data                  : dictionary
    # tanggal               : string
    # provinsi              : string
    # penambahan_positif    : int
    # penambahan_meninggal  : int
    # penambahan_sembuh     : int
    # penambahan_dirawat    : int
    # output_harian_provinsi: string

    # ALGORITMA
    data = data_covid(namaProvinsi)
    tanggal = data.get("last_date")
    provinsi = data.get("provinsi")
    penambahan = (data.get("list_perkembangan"))[-1]
    penambahan_positif = penambahan.get("KASUS")
    penambahan_meninggal = penambahan.get("MENINGGAL")
    penambahan_sembuh = penambahan.get("SEMBUH")
    penambahan_dirawat = penambahan.get("DIRAWAT_OR_ISOLASI")
    output_harian_provinsi = f"Data Penambahan Kasus Covid di {provinsi} pada tanggal {tanggal} : \nPertambahan Kasus Positif : {penambahan_positif}\nPertambahan Kasus Dirawat : {penambahan_dirawat}\nPertambahan Kasus Sembuh : {penambahan_sembuh}\nPertambahan Kasus Meninggal : {penambahan_meninggal}\n"
    return output_harian_provinsi

# Data untuk harian tiap provinsi
def PertambahanHariTertentuProvinsi(namaProvinsi, indeks):
    # Menghasilkan data pertambahan harian tertentu
    # covid-19 dari namaProvinsi dan dari indeks

    # KAMUS LOKAL
    # data                          : dictionary
    # provinsi                      : string
    # arrHarian                     : array of dictionary
    # arr_positif_harian            : array of int
    # arr_dirawat_harian            : array of int
    # arr_sembuh_harian             : array of int
    # arr_meninggal_harian          : array of int
    # output_hari_tertentu_provinsi : string

    # ALGORITMA
    data = data_covid(namaProvinsi)
    provinsi = data.get("provinsi")
    arrHarian = data.get("list_perkembangan")
    arr_positif_harian = arrHarian[indeks-1].get("KASUS")
    arr_dirawat_harian = arrHarian[indeks-1].get("DIRAWAT_OR_ISOLASI")
    arr_sembuh_harian = arrHarian[indeks-1].get("SEMBUH")
    arr_meninggal_harian = arrHarian[indeks-1].get("MENINGGAL")
    output_hari_tertentu_provinsi = f"Jumlah data covid di {provinsi} hari ke {indeks} \nJumlah Positif : {arr_positif_harian} \nJumlah Dirawat : {arr_dirawat_harian} \nJumlah Sembuh : {arr_sembuh_harian} \nJumlah Meninggal : {arr_meninggal_harian} \n"
    return output_hari_tertentu_provinsi


# ALGORITMA PROGRAM UTAMA

# Deklarasi variabel link server API per lokasi
Indonesia = "https://data.covid19.go.id/public/api/update.json"

DKI_Jakarta = "https://data.covid19.go.id/public/api/prov_detail_DKI_JAKARTA.json"
Jawa_Barat = "https://data.covid19.go.id/public/api/prov_detail_JAWA_BARAT.json"
Jawa_Tengah = "https://data.covid19.go.id/public/api/prov_detail_JAWA_TENGAH.json"
Jawa_Timur = "https://data.covid19.go.id/public/api/prov_detail_JAWA_TIMUR.json"
Kalimatan_Timur = "https://data.covid19.go.id/public/api/prov_detail_KALIMANTAN_TIMUR.json"

# User Interface
# Deklarasi variabel isRunning
isRunning = True

# Membuat looping untuk mengulang pencarian data oleh pengguna
while (isRunning):
    # Menentukan lokasi data covid-19 yang ingin dicari
    print("=" * 50)
    print("Data apa yang mau dicari?")
    print("1. Data di Indonesia \n2. Data di provinsi besar \n3. Keluar")
    print("=" * 50)
    inputLokasi = int(input("Masukkan pilihan : "))
    print("=" * 50)
    print("")

    if (inputLokasi == 1):
        # Menentukan jenis data covid-19 yang ingin dicari
        print("1. Data Total Covid di Indonesia\n2. Data Covid Harian Terbaru di Indonesia\n3. Data Covid pada tanggal tertentu di Indonesia\n4. Keluar")
        print("=" * 50)
        inputPengguna = int(input("Masukkan pilihan : "))
        print("=" * 50)
        print("")

        if (inputPengguna == 1):
            print(TotalIndo())
            print("=" * 50)
        elif (inputPengguna == 2):
            print(PertambahanHarianIndo())
            print("=" * 50)
        elif (inputPengguna == 3):
            # Deklarasi variabel indeks sebagai input data covid-19 pada hari tertentu
            indeks = int(input("Data covid hari ke (02-03-2020 adalah hari ke 1) : "))
            print(PertambahanHariTertentuIndo(indeks))
            print("=" * 50)
        elif (inputPengguna == 4):
            # Keluar dari program
            exit()
        else:
            print("Input error!!")
            continue

        # Menentukan apakah pengguna ingin lanjut mencari data atau tidak
        lanjut = input("Ingin mencari data lain? (Y/N) : ")
        if (lanjut == "N" or lanjut == "n"):
            # Keluar dari program
            exit()
        elif (lanjut == "Y" or lanjut == "y"):
            continue
        else:
            print("Input error!!")
            continue


    elif (inputLokasi == 2):
        # Menentukan provinsi manakah yang ingin dicari datanya
        print("Data di provinsi manakah yang ingin dicari?")
        print("1. DKI Jakarta \n2. Jawa Barat \n3. Jawa Tengah \n4. Jawa Timur \n5. Kalimantan Timur \n6. Keluar")
        print("=" * 50)
        inputProvinsi = int(input("Masukkan pilihan : "))
        print("=" * 50)
        print("")

        # Deklarasi variabel namaProvinsi dan tanggalAwalKasus
        if (inputProvinsi == 1):
            namaProvinsi = DKI_Jakarta
            tanggalAwalKasus = "02-03-2020"
        elif (inputProvinsi == 2):
            namaProvinsi = Jawa_Barat
            tanggalAwalKasus = "04-03-2020"
        elif (inputProvinsi == 3):
            namaProvinsi = Jawa_Tengah
            tanggalAwalKasus = "09-03-2020"
        elif (inputProvinsi == 4):
            namaProvinsi = Jawa_Timur
            tanggalAwalKasus = "19-03-2020"
        elif (inputProvinsi == 5):
            namaProvinsi = Kalimatan_Timur
            tanggalAwalKasus = "15-03-2020"
        elif (inputProvinsi == 6):
            # Keluar dari program
            exit()
        else:
            print("Input error!!")
            continue

        # Menentukan jenis data covid-19 yang ingin dicari
        print("1. Data Total Covid\n2. Data Covid Harian Terbaru\n3. Data Covid pada tanggal tertentu\n4. Keluar")
        print("=" * 50)
        inputPenggunaProvinsi = int(input("Masukkan pilihan : "))
        print("=" * 50)
        print("")

        if (inputPenggunaProvinsi == 1):
            print(TotalProvinsi(namaProvinsi))
            print("=" * 50)
        elif (inputPenggunaProvinsi == 2):
            print(PertambahanHarianProvinsi(namaProvinsi))
            print("=" * 50)
        elif (inputPenggunaProvinsi == 3):
            # Deklarasi variabel indeks sebagai input data covid-19 pada hari tertentu
            indeks = int(input(f"Data covid hari ke ({tanggalAwalKasus} adalah hari ke 1) : "))
            print(PertambahanHariTertentuProvinsi(namaProvinsi, indeks))
            print("=" * 50)
        elif (inputPenggunaProvinsi == 4):
            # Keluar dari program
            exit()
        else:
            print("Input error!!")
            continue

        # Menentukan apakah pengguna ingin lanjut mencari data atau tidak
        lanjut = input("Ingin mencari data lain? (Y/N) : ")
        if (lanjut == "N" or lanjut == "n"):
            # Keluar dari program
            exit()
        elif (lanjut == "Y" or lanjut == "y"):
            continue
        else:
            print("Input error!!")
            continue

    elif (inputLokasi == 3):
        # Keluar dari program
        exit()
    else:
        print("Input error!!")
        continue