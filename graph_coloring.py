

#  REPRESENTASI GRAF

def buat_graf(jumlah_simpul):
    """Membuat adjacency matrix kosong berukuran n×n."""
    return [[0] * jumlah_simpul for _ in range(jumlah_simpul)]


def tambah_sisi(graf, u, v):
    """Menambahkan sisi (edge) antara simpul u dan v (tidak berarah)."""
    graf[u][v] = 1
    graf[v][u] = 1

#  FUNGSI PENGECEKAN KEAMANAN WARNA

def is_safe(graf, simpul, warna, warna_dipilih, n):
 
    for tetangga in range(n):
       
        if graf[simpul][tetangga] == 1 and warna_dipilih[tetangga] == warna:
            return False
    return True


#  FUNGSI UTAMA BACKTRACKING


def graph_coloring(graf, m, simpul, warna_dipilih, n, solusi_list, langkah):

  
    if simpul == n:
        solusi_list.append(warna_dipilih[:])
        return

    nama_warna = ["Merah", "Hijau", "Biru", "Kuning",
                  "Ungu", "Oranye", "Pink", "Coklat"]

 
    for warna in range(1, m + 1):
        langkah[0] += 1
        nama = nama_warna[warna - 1] if warna <= len(nama_warna) else f"Warna-{warna}"

        print(f"  Langkah {langkah[0]:>3} | Simpul {simpul} → Coba {nama:<8}", end=" ")

        if is_safe(graf, simpul, warna, warna_dipilih, n):
            warna_dipilih[simpul] = warna
            print(f"✔ AMAN")

      
            graph_coloring(graf, m, simpul + 1, warna_dipilih, n, solusi_list, langkah)

          
            warna_dipilih[simpul] = 0
            print(f"  {'':>31} ↩ Backtrack dari Simpul {simpul} ({nama})")
        else:
            print(f"✖ KONFLIK")



#  FUNGSI VISUALISASI


def tampilkan_graf(graf, n, nama_simpul):
    """Menampilkan struktur graf dalam bentuk adjacency matrix."""
    print("\n  Adjacency Matrix Graf:")
    print("      ", end="")
    for i in range(n):
        print(f"  {nama_simpul[i]}", end="")
    print()
    print("      " + "----" * n)
    for i in range(n):
        print(f"  {nama_simpul[i]}  |", end="")
        for j in range(n):
            print(f"  {graf[i][j]} ", end="")
        print()


def tampilkan_koneksi(graf, n, nama_simpul):
    """Menampilkan daftar sisi (edge) yang ada pada graf."""
    print("\n  Daftar Sisi (Edge):")
    ada_sisi = False
    for i in range(n):
        for j in range(i + 1, n):
            if graf[i][j] == 1:
                print(f"    {nama_simpul[i]} ── {nama_simpul[j]}")
                ada_sisi = True
    if not ada_sisi:
        print("    (Tidak ada sisi)")


def tampilkan_solusi(solusi_list, nama_simpul):
    """Menampilkan semua solusi pewarnaan yang ditemukan."""
    nama_warna = {
        1: ("Merah",   "🔴"),
        2: ("Hijau",   "🟢"),
        3: ("Biru",    "🔵"),
        4: ("Kuning",  "🟡"),
        5: ("Ungu",    "🟣"),
        6: ("Oranye",  "🟠"),
    }

    print("\n" + "="*50)
    print(f"  HASIL: {len(solusi_list)} solusi pewarnaan ditemukan")
    print("="*50)

    for idx, solusi in enumerate(solusi_list, 1):
        print(f"\n  ── Solusi #{idx} ──")
        for i, warna in enumerate(solusi):
            nama, emoji = nama_warna.get(warna, (f"Warna-{warna}", "⚫"))
            print(f"    Simpul {nama_simpul[i]:>2}  →  {emoji} {nama}")


def tampilkan_ringkasan(solusi_list, m, n, nama_simpul):
    """Menampilkan ringkasan dalam bentuk tabel."""
    nama_warna_short = {1: "Merah", 2: "Hijau", 3: "Biru",
                        4: "Kuning", 5: "Ungu", 6: "Oranye"}

    print("\n" + "="*50)
    print("  RINGKASAN SOLUSI (Tabel)")
    print("="*50)

    # Header
    header = f"  {'Solusi':^8} |"
    for nm in nama_simpul:
        header += f" {nm:^7} |"
    print(header)
    print("  " + "-"*8 + "-+" + ("-"*8 + "-+") * n)

    for idx, solusi in enumerate(solusi_list, 1):
        baris = f"  {'#'+str(idx):^8} |"
        for warna in solusi:
            nm = nama_warna_short.get(warna, f"W{warna}")
            baris += f" {nm:^7} |"
        print(baris)



#  MAIN PROGRAM

def main():
    print("║  Graph Coloring Problem — Algoritma Backtrack ║")


    # ── Konfigurasi Graf ──────────────────────────────
  
    N = 5                 
    M = 3                    
    nama_simpul = ["A", "B", "C", "D", "E"]

    # Inisialisasi graf kosong
    graf = buat_graf(N)

    # Tambahkan sisi-sisi graf
    tambah_sisi(graf, 0, 1)  # A - B
    tambah_sisi(graf, 0, 3)  # A - D
    tambah_sisi(graf, 1, 2)  # B - C
    tambah_sisi(graf, 1, 4)  # B - E
    tambah_sisi(graf, 2, 4)  # C - E
    tambah_sisi(graf, 3, 4)  # D - E

    # ── Tampilkan Info Graf 
    print(f"\n  Jumlah Simpul  : {N}")
    print(f"  Jumlah Warna   : {M} (Merah, Hijau, Biru)")
    tampilkan_koneksi(graf, N, nama_simpul)
    tampilkan_graf(graf, N, nama_simpul)

    # ── Jalankan Backtracking
    print("\n" + "="*50)
    print("  PROSES BACKTRACKING")
    print("="*50)

    warna_dipilih = [0] * N   # 0 = belum diwarnai
    solusi_list   = []
    langkah       = [0]       # Gunakan list agar bisa dimodifikasi di dalam rekursi

    graph_coloring(graf, M, 0, warna_dipilih, N, solusi_list, langkah)

    # ── Tampilkan Hasi
    if solusi_list:
        tampilkan_solusi(solusi_list, nama_simpul)
        tampilkan_ringkasan(solusi_list, M, N, nama_simpul)
    else:
        print(f"\n  ✖ Tidak ada solusi dengan {M} warna untuk graf ini.")
        print(f"    Coba tambah jumlah warna M!")

    print(f"\n  Total langkah backtracking : {langkah[0]}")
    print(f"  Total solusi ditemukan     : {len(solusi_list)}")
    print("\n  Program selesai.")


if __name__ == "__main__":
    main()