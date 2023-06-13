def TowerOfHanoi(n, source, destination, auxiliary):
    if n > 0:
        # Memindahkan n-1 cakram dari menara sumber ke menara bantu
        TowerOfHanoi(n-1, source, auxiliary, destination)
        
        # Memindahkan cakram terbesar dari menara sumber ke menara tujuan
        print(f"Pindahkan Cakram {n} dari {source} ke {destination}")
        
        # Memindahkan n-1 cakram dari menara bantu ke menara tujuan
        TowerOfHanoi(n-1, auxiliary, destination, source)

# Penggunaan:
n = 3  # Jumlah cakram
 # 'A' sebagai menara sumber, 
 # 'C' sebagai menara tujuan, 
 # 'B' sebagai menara bantu
TowerOfHanoi(n, 'A', 'C', 'B')