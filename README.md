Nama : Joe Mathew Rusli
NPM : 2306152310
Kelas : PBP E

PBP E-Commerce

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) with your browser to see the result.

Open this [link](http://joe-mathew-zeroecommerce.pbp.cs.ui.ac.id/) to see the result on PWS.

## Table of Contents
- [Tugas 2](#tugas-2)
- [Tugas 3](#tugas-3)

## Tugas 2
#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat project baru dengan menggunakan command `django-admin startproject zeroecommerce`
2. Membuat aplikasi baru dengan menggunakan command `python manage.py startapp main`
3. Membuat model untuk produk dengan isi sebagai berikut:
```python
    name : CharField
    price : IntegerField
    description : TextField
    stock : IntegerField
```
4. Membuat view untuk menampilkan list produk dengan menambahkan fungsi `show_main` di `views.py` di folder main
5. Membuat routing untuk aplikasi main dengan menambahkan path ke `urls.py` di folder main
6. Membuat routing yang mengarah ke main dengan menambahkan path ke `urls.py` di folder zeroecommerce

#### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.
![alt text](image.png)

#### Jelaskan fungsi `git` dalam pengembangan perangkat lunak!
Git adalah sebuah sistem yang memungkinkan developers untuk berkolaborasi dalam pembuatan suatu program dengan cara mengelola versi dari program tersebut. Git memungkinkan developers untuk membuat branch baru, merge branch, dan melihat perubahan yang terjadi pada program. Dengan menggunakan git, developers dapat bekerja secara bersamaan tanpa mengalami konflik pada program yang sedang dikerjakan.

#### Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django dijadikan permulaan pembelajaran pengembangan perangkat lunak karena Django memiliki dokumentasi yang lengkap dan mudah dipahami. Selain itu, Django juga memiliki fitur yang lengkap dan mudah digunakan sehingga memudahkan developers dalam membuat aplikasi web. Django juga memiliki fitur yang memungkinkan developers untuk membuat aplikasi web dengan cepat dan efisien.

#### Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena model pada Django memungkinkan developers untuk berinteraksi dengan database menggunakan objek-objek Python. Dengan menggunakan model pada Django, developers dapat membuat, membaca, mengubah, dan menghapus data pada database menggunakan objek-objek Python tanpa perlu menulis query SQL secara langsung.

---
## Tugas 3
#### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery diperlukan dalam pengimplementasian sebuah platform karena data delivery memungkinkan developers untuk mengirim data dari server ke client dengan cepat dan efisien. Dengan menggunakan data delivery, developers dapat mengirim data dalam jumlah besar dengan cepat dan efisien sehingga mempercepat proses loading data pada aplikasi web. Data delivery juga memungkinkan developers untuk mengirim data dalam berbagai format seperti JSON, XML, dan HTML. Data delivert juga membuat aplikasi web menjadi lebih responsif dan interaktif, karena data dapat diambil dan ditampilkan secara real-time. 

Data delivery juga memungkinkan developers untuk mengirim data ke berbagai perangkat seperti desktop, mobile, dan tablet. Dengan menggunakan data delivery, developers dapat membuat aplikasi web yang responsif dan dapat diakses dari berbagai perangkat. Data delivery juga memungkinkan developers untuk mengirim data ke berbagai lokasi seperti server, cloud, dan CDN. Dengan menggunakan data delivery, developers dapat membuat aplikasi web yang scalable dan dapat diakses dari berbagai lokasi.

#### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya JSON lebih baik. Hal ini karena JSON lebih ringan dan lebih mudah dibaca dibandingkan XML. JSON juga lebih mudah dipahami oleh manusia dan lebih mudah diproses oleh komputer. JSON juga lebih mudah digunakan dalam pengembangan aplikasi web karena JSON dapat diakses menggunakan JavaScript. JSON juga lebih populer dibandingkan XML karena hal yang sama seperti sebelumnya, yaitu JSON lebih ringan dan lebih mudah dibaca dibandingkan XML.

Struktur JSON:
```json
{
    "name": "Joe",
    "age": 20,
    "city": "Jakarta"
}
```

Struktur XML:
```xml
<person>
    <name>Joe</name>
    <age>20</age>
    <city>Jakarta</city>
</person>
```

Jika data yang dikirim sangat banyak dan bernested-nested, jelas terlihat bahwa JSON lebih mudah dibaca jika dibandingkan dengan XML.

#### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Fungsi dari method `is_valid()` pada form Django adalah untuk memvalidasi data yang dimasukkan oleh user. Method `is_valid()` akan mengembalikan nilai `True` jika data yang dimasukkan oleh user valid dan akan mengembalikan nilai `False` jika data yang dimasukkan oleh user tidak valid. Method `is_valid()` memungkinkan developers untuk memvalidasi data yang dimasukkan oleh user sebelum data tersebut disimpan ke database. 

Dengan menggunakan method `is_valid()`, developers dapat memastikan bahwa data yang dimasukkan oleh user valid dan sesuai dengan aturan yang telah ditentukan. Method `is_valid()` juga memungkinkan developers untuk menampilkan pesan error jika data yang dimasukkan oleh user tidak valid. Dengan menggunakan method `is_valid()`,

Contoh penggunaan method `is_valid()`:
```python
if form.is_valid():
    form.save()
else:
    print(form.errors)
```

Contoh input yang tidak valid:
```python
form = ProductForm(data={'name': '1234567891011...251', 'price': 100, 'description': 'tes', 'stock': 100})
```
`'name'` harus kurang dari 250 karakter. Anggap string tersebut memiliki 251 karakter.

Contoh output:
```python
{'name': ['Ensure this value has at most 250 characters (it has 251).']}
```

#### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Kita membutuhkan `csrf_token` saat membuat form di Django untuk mencegah serangan CSRF (Cross-Site Request Forgery). CSRF adalah serangan yang memungkinkan penyerang untuk mengirimkan request palsu ke server dari situs web yang telah di-authorize oleh user. Dengan menggunakan `csrf_token`, Django akan memastikan bahwa request yang diterima oleh server berasal dari situs web yang telah diotorisasi oleh user. Jika kita tidak menambahkan `csrf_token` pada form Django, maka form tersebut rentan terhadap serangan CSRF dan penyerang dapat mengirimkan request palsu ke server dari situs web yang telah di-authorize oleh user. 

Contoh serangan CSRF:
```html
<form action="http://example.com/delete" method="POST">
    <input type="hidden" name="id" value="1">
    <input type="submit" value="Delete">
</form>
```

Hal yang terjadi jika dilakukan serangan seperti diatas adalah data yang ada pada server akan terhapus. Dengan menggunakan `csrf_token`, Django akan memastikan bahwa request yang diterima oleh server berasal dari situs web yang telah di-authorize oleh user dan mencegah serangan CSRF.

#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat `forms.py` di folder main dengan tujuan membuat form untuk `Product`
2. Membuat `views.py` di folder main dengan tujuan membuat fungsi `create_product` untuk menambahkan produk.
3. Membuat `create_product.html` di folder templates/main dengan tujuan membuat form untuk menambahkan produk.
4. Menambahkan `csrf_token` pada form di `create_product.html` untuk mencegah serangan CSRF.
5. Menambahkan fungsi `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id` di `views.py` di folder main untuk menampilkan data dalam format XML dan JSON.
6. Membuat `urls.py` di folder main dengan tujuan membuat routing untuk aplikasi main.

#### Screenshot hasil menggunakan postman.
1. Show XML
![show_xml](./public/images/tugas2/tugas2_xml.png)
2. Show JSON
![show_json](./public/images/tugas2/tugas2_json.png)
3. Show XML by ID
![show_xml_by_id](./public/images/tugas2/tugas2_xmlid.png)
4. Show JSON by ID
![show_json_by_id](./public/images/tugas2/tugas2_jsonid.png)