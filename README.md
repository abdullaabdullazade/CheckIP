1. **Kitabxanaların İdxalı:** `requests`, `colorama`, `time`, `threading` və `speedtest` kitabxanaları idxal edilir.
2. **İnternet Bağlantısı və IP Məlumatlarının Yoxlanması:** Kod `https://ipleak.net/json/` URL-dən IP məlumatlarını götürmək üçün HTTP GET sorğusu göndərir.
3. **Yükləmə və Yükləmə Sürətinin Test Edilməsi:** `speedtest` kitabxanası istifadə edilərək internet sürəti yoxlanılır.
4. **Animasiyalı Yükləmə Ekranı:** İstifadəçiyə prosesin davam etdiyini göstərmək üçün animasiyalı yükləmə ekranı əlavə edilir.
5. **Məlumatların Çap Edilməsi:** Əldə edilən məlumatlar rəngli formada ekranda göstərilir.

İndi isə buna uyğun GitHub üçün ReadMe faylı hazırlayaq:

---

# IP və İnternet Sürəti Yoxlama Skripti

Bu Python skripti sizin IP məlumatlarınızı yoxlayır və internet yükləmə/yükləmə sürətinizi test edir. Skript işləyərkən animasiyalı yükləmə ekranı göstərir.

## Tələblər

Bu skriptin işləməsi üçün aşağıdakı Python kitabxanaları quraşdırılmalıdır:
- `requests`
- `colorama`
- `speedtest-cli`

Quraşdırma üçün aşağıdakı əmr istifadə edilə bilər:
```sh
pip install requests colorama speedtest-cli
```

## İstifadə

Skripti işə salmaq üçün aşağıdakı addımları izləyin:

1. **Kodun Yüklənməsi:** Bu repozitoriyanı klonlayın və ya kodu yükləyin.
2. **Skripti İcra Edin:** Terminalda və ya komand konsolunda skripti işə salın:
    ```sh
    python script_name.py
    ```

## Skriptin Əsas Hissələri

- **IP Məlumatlarının Yoxlanması:** `requests` kitabxanası ilə IP məlumatlarını yoxlayır.
- **İnternet Sürətinin Test Edilməsi:** `speedtest` kitabxanası ilə internet sürətini test edir.
- **Yükləmə Animasiyası:** `threading` və `time` kitabxanaları ilə animasiyalı yükləmə ekranı yaradır.

## Məlumatların Nümayişi

Skript işlədikdən sonra aşağıdakı məlumatlar göstəriləcək:
- IP Ünvanı
- ISP Adı
- Ölkə
- Region
- Şəhər
- Yükləmə sürəti (Mbps)
- Yükləmə sürəti (Mbps)
- Ping (ms)

## Nümunə Çıxış

Aşağıda skriptin nümunə çıxışı göstərilmişdir:

```
       IP INFORMATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ━ Your IP:  123.45.67.89
 ━ ISP Name: MyISP
 ━ Country:  MyCountry
 ━ Region:   MyRegion
 ━ City:     MyCity

 ━ Download speed: 50.23 Mbps
 ━ Upload speed: 10.56 Mbps
 ━ Ping: 20 ms
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

