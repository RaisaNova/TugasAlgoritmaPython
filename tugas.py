nilaiA = int(input("masukkan nilai A: "))
nilaiB = int(input("masukkan nilai B: "))

rataRata = (nilaiA + nilaiB) / 2

if rataRata <= 75:
    print("anda tidak lulus dengan nilai: ", rataRata)
else:
    print("anda lulus dengan nilai: ", rataRata)


print("hasil")
print("Nilai A:", nilaiA)
print("Nilai B:", nilaiB)
print("Rata-rata:", rataRata)
print("status:", "Lulus" if rataRata > 75 else "Tidak Lulus")    