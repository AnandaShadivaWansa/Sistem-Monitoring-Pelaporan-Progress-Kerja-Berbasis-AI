# Sistem Monitoring Pelaporan Progress Kerja Berbasis Natural Language Processing

**Kode Tim:** PBLIF3-MD13

Sistem web untuk mengotomatisasi pelaporan progress kerja mingguan. Personel mengisi laporan (jobdesk, progress, kendala, improvement, rencana) beserta lampiran opsional, lalu sistem menggunakan NLP melalui LLM API untuk meringkas dan mengklasifikasikan laporan ke dalam kategori **selesai, pending, kendala, improvement**. Hasilnya ditampilkan di dashboard Supervisor (SPV).

## Tech Stack
- Python, Django
- SQLite
- Tailwind CSS
- LLM API (NLP)
