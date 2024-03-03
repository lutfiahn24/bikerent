# bikerent
## Setup environment

1. Setup environment menggunakan Conda dengan Python versi 3.9:
    ```bash
    conda create --name main-ds python=3.9
    ```

2. Aktifkan new environment:
    ```bash
    conda activate main-ds
    ```

3. Instal paket-paket yang dibutuhkan menggunakan pip:
    ```bash
    pip install numpy pandas scipy matplotlib seaborn jupyter streamlit babel
    ```

## Menjalankan aplikasi Streamlit

Untuk menjalankan aplikasi Streamlit, gunakan perintah berikut:
```bash
streamlit run dashboard.py
