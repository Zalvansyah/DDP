ket = """Selamat datang di ZekMath
masukan pilihan :
1. Menghitung Luas Persegi
2. Menghitung Luas Lingkaran
3. Menghitung Luas Segitiga """

pilihan = input (ket)



match pilihan:
    case "1":
        print ("kamu memilih 1 untuk menghitung luas persegi")
        sisi = int(input("masukan sisi ?"))
        luasP = sisi * sisi
        print ("luas persegi yang sisinya ", sisi, "adalah ", luasP)
    case "2":
        print ("kamu memilih 2 untuk menghitung luas lingkaran")
        jari2 = float(input ("masukan jar2?"))
        luasL = 3.14 * jari2 * jari2
        print ("luas lingkaran yang jari2nya ", jari2, "jari2", jari2, "adalah", luasL)  
    case "3":
        print ("kamu memilih 3 untuk menghitung luas segitiga")
        alas = int(input("Masukkan Alas ?"))
        tinggi = int(input("Masukkan Tinggi?"))
        luasS = 0.5 * alas * tinggi
        print ("luas segitiga yang alasnya ", alas, "tinggi", "adalah", luasS)
    case _:
        print ("Maaf pilihan kamu tidak ada di dalam data kami")
        
            
        