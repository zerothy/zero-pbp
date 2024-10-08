Nama : Joe Mathew Rusli
NPM : 2306152310
Kelas : PBP E

ZERO E-Commerce

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) with your browser to see the result.

Open this [link](http://joe-mathew-zero.pbp.cs.ui.ac.id/) to see the result on PWS.

## Table of Contents
- [Tugas 2](#tugas-2)
    - [Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).](#jelaskan-bagaimana-cara-kamu-mengimplementasikan-checklist-di-atas-secara-step-by-step-bukan-hanya-sekadar-mengikuti-tutorial)
    - [Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.](#buatlah-bagan-yang-berisi-request-client-ke-web-aplikasi-berbasis-django-beserta-responnya-dan-jelaskan-pada-bagan-tersebut-kaitan-antara-urlspy-viewspy-modelspy-dan-berkas-html)
    - [Jelaskan fungsi `git` dalam pengembangan perangkat lunak!](#jelaskan-fungsi-git-dalam-pengembangan-perangkat-lunak)
    - [Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?](#menurut-anda-dari-semua-framework-yang-ada-mengapa-framework-django-dijadikan-permulaan-pembelajaran-pengembangan-perangkat-lunak)
    - [Mengapa model pada Django disebut sebagai ORM?](#mengapa-model-pada-django-disebut-sebagai-orm)
- [Tugas 3](#tugas-3)
    - [Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?](#jelaskan-mengapa-kita-memerlukan-data-delivery-dalam-pengimplementasian-sebuah-platform)
    - [Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?](#menurutmu-mana-yang-lebih-baik-antara-xml-dan-json-mengapa-json-lebih-populer-dibandingkan-xml)
    - [Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?](#jelaskan-fungsi-dari-method-is_valid-pada-form-django-dan-mengapa-kita-membutuhkan-method-tersebut)
    - [Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?](#mengapa-kita-membutuhkan-csrf_token-saat-membuat-form-di-django-apa-yang-dapat-terjadi-jika-kita-tidak-menambahkan-csrf_token-pada-form-django-bagaimana-hal-tersebut-dapat-dimanfaatkan-oleh-penyerang)
    - [Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).](#jelaskan-bagaimana-cara-kamu-mengimplementasikan-checklist-di-atas-secara-step-by-step-bukan-hanya-sekadar-mengikuti-tutorial-1)
    - [Screenshot hasil menggunakan postman.](#screenshot-hasil-menggunakan-postman)
- [Tugas 4](#tugas-4)
    - [Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`](#apa-perbedaan-antara-httpresponseredirect-dan-redirect)
    - [Jelaskan cara kerja penghubungan model `Product` dengan `User`!](#jelaskan-cara-kerja-penghubungan-model-product-dengan-user)
    - [Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.](#apa-perbedaan-antara-authentication-dan-authorization-apakah-yang-dilakukan-saat-pengguna-login-jelaskan-bagaimana-django-mengimplementasikan-kedua-konsep-tersebut)
    - [Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?](#bagaimana-django-mengingat-pengguna-yang-telah-login-jelaskan-kegunaan-lain-dari-cookies-dan-apakah-semua-cookies-aman-digunakan)
    - [Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).](#jelaskan-bagaimana-cara-kamu-mengimplementasikan-checklist-di-atas-secara-step-by-step-bukan-hanya-sekadar-mengikuti-tutorial-1)
- [Tugas 5](#tugas-5)
    - [Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!](#jika-terdapat-beberapa-css-selector-untuk-suatu-elemen-html-jelaskan-urutan-prioritas-pengambilan-css-selector-tersebut)
    - [Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!](#mengapa-responsive-design-menjadi-konsep-yang-penting-dalam-pengembangan-aplikasi-web-berikan-contoh-aplikasi-yang-sudah-dan-belum-menerapkan-responsive-design)
    - [Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!](#jelaskan-perbedaan-antara-margin-border-dan-padding-serta-cara-untuk-mengimplementasikan-ketiga-hal-tersebut)
    - [Jelaskan konsep flex box dan grid layout beserta kegunaannya!](#jelaskan-konsep-flex-box-dan-grid-layout-beserta-kegunaannya)
    - [Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!](#jelaskan-bagaimana-cara-kamu-mengimplementasikan-checklist-di-atas-secara-step-by-step-bukan-hanya-sekadar-mengikuti-tutorial-1)

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
![alt text](/static/images/image.png)

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
![show_xml](/static/images/tugas3/tugas3_xml.png)
2. Show JSON
![show_json](/static/images/tugas3/tugas3_json.png)
3. Show XML by ID
![show_xml_by_id](/static/images/tugas3/tugas3_xmlid.png)
4. Show JSON by ID
![show_json_by_id](/static/images/tugas3/tugas3_jsonid.png)

---
## Tugas 4
#### Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`
`HttpResponseRedirect()` hanya dapat menerima URL lengkap sebagai argumen, sedangkan `redirect()` dapat menerima URL lengkap, nama view, dan nama URL pattern sebagai argumen. `redirect()` juga dapat menerima argumen tambahan seperti `args` dan `kwargs`. Sehingga, `redirect()` lebih fleksibel dan dapat digunakan dalam berbagai kasus.

#### Jelaskan cara kerja penghubungan model `Product` dengan `User`!
Model `Product` dan `User` dapat dihubungkan menggunakan relasi `ForeignKey`. Relasi `ForeignKey` memungkinkan satu model untuk memiliki banyak model lainnya. Dengan menggunakan relasi `ForeignKey`, model `Product` dapat memiliki relasi dengan model `User`.
```python
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```

#### Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Authentication adalah proses untuk memverifikasi identitas pengguna, sedangkan authorization adalah proses untuk memverifikasi hak akses pengguna. Saat pengguna login, Django akan melakukan proses authentication untuk memverifikasi identitas pengguna. Setelah proses authentication berhasil, Django akan melakukan proses authorization untuk memverifikasi hak akses pengguna. Django mengimplementasikan kedua konsep tersebut dengan menggunakan `User` model dan `auth` views. `User` model digunakan untuk menyimpan informasi pengguna seperti username, password, dan email. `auth` views digunakan untuk melakukan proses authentication dan authorization. Django juga menyediakan decorator `@login_required` untuk membatasi akses pengguna yang belum login. Dengan menggunakan decorator `@login_required`, Django akan memastikan bahwa pengguna yang belum login tidak dapat mengakses halaman tertentu.

#### Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login dengan menggunakan session. Session adalah cara untuk menyimpan informasi pengguna di server. Django menyimpan session pengguna di database atau cache. Django juga menggunakan cookies untuk menyimpan session ID pengguna. Cookies adalah cara untuk menyimpan informasi pengguna di browser. Cookies digunakan untuk menyimpan session ID pengguna, token CSRF, dan preferensi pengguna. Tidak semua cookies aman digunakan. Cookies yang tidak aman dapat digunakan untuk melacak pengguna, menyimpan informasi sensitif, dan menyebabkan serangan XSS (Cross-Site Scripting). Oleh karena itu, developers harus berhati-hati dalam menggunakan cookies dan memastikan bahwa cookies yang digunakan aman.

#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat fitur login dan register dengan menggunakan `auth` views di Django. Fitur logout juga diimplementasikan. Dengan menggunakan fitur-fitur yang disediakan oleh Django, saya dapat membuat aplikasi web yang memiliki fitur login, register, dan logout dengan mudah.

2. Membuat 2 akun dengan meregistrasi di bagian `/register`. Setelah itu, login dengan salah satu akun yang telah dibuat, satu per satu. Setelah login, kemudian mengakses `/create` untuk menambahkan 3 dummy data dengan model `Product`. Setelah itu, logout dan login dengan akun yang lain.

3. Menghubungkan `User` dengan `Product` dengan menambahkan field `user` pada model `Product` dengan relasi `ForeignKey`. Dengan menggunakan relasi `ForeignKey`, saya dapat menghubungkan model `Product` dengan model `User`.

4. Menampilkan `last_login` pada web dengan menambahkan field `last_login` pada model `User`. Yang dimana field tersebut menggunakan dan menerapkan `cookies` untuk menyimpan informasi pengguna di browser.

---
## Tugas 5
#### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan prioritas pengambilan CSS selector, juga dikenal sebagai specificity (spesifisitas), adalah sebagai berikut (dari yang tertinggi ke terendah):

1. **Inline Styles**: Gaya yang diterapkan langsung pada elemen HTML menggunakan atribut `style`.
2. **ID Selectors**: Selector yang menggunakan ID elemen (`#id`).
3. **Class Selectors, Attribute Selectors, dan Pseudo-Classes**: Selector yang menggunakan kelas (`.class`), atribut (`[attribute]`), dan pseudo-classes (`:pseudo-class`).
4. **Element Selectors dan Pseudo-Elements**: Selector yang menggunakan nama elemen (`element`) dan pseudo-elements (`::pseudo-element`).
5. **Universal Selector (`*`)**: Selector yang berlaku untuk semua elemen.

Jika ada konflik antara selector dengan spesifisitas yang sama, selector yang ditulis terakhir dalam file CSS akan digunakan.

### Contoh:
```html
<p id="paragraph" class="text" style="color: red;">Hello, World!</p>
```

```css
#paragraph { color: blue; }
.text { color: green; }
p { color: yellow; }
```

#### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design menjadi konsep penting dalam pengembangan aplikasi web karena:

1. Beragamnya perangkat: Pengguna mengakses web dari berbagai perangkat dengan ukuran layar yang berbeda-beda.
2. Pengalaman pengguna: Memastikan konten dapat diakses dan mudah dibaca di semua perangkat.
3. SEO: Google mempertimbangkan mobile-friendliness dalam peringkat pencarian.
4. Efisiensi: Satu desain yang responsif lebih efisien daripada membuat versi terpisah untuk desktop dan mobile.

- Contoh Aplikasi yang Menerapkan Responsive Design
    - **Amazon**: Situs e-commerce ini menyesuaikan tata letak dan ukuran elemen berdasarkan ukuran layar.
- Contoh Aplikasi yang Belum Menerapkan Responsive Design
    - Beberapa situs pemerintahan lama atau situs perusahaan kecil yang belum diperbarui sering kali tidak responsif dan sulit diakses dari perangkat mobile.


#### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
a. **Margin**:
- Ruang di luar elemen, di antara elemen tersebut dan elemen-elemen sekitarnya.
- Tidak memiliki warna atau latar belakang.
- Digunakan untuk mengatur jarak antar elemen.

b. **Border**:
- Garis yang mengelilingi elemen, terletak di antara padding dan margin.
- Dapat memiliki warna, gaya (solid, dashed, dll), dan ketebalan.
- Digunakan untuk memberi batas visual pada elemen.

c. **Padding**:
- Ruang di dalam elemen, antara konten dan border.
- Dapat memiliki warna latar belakang (mengikuti background elemen).
- Digunakan untuk memberi ruang di sekitar konten elemen.

### Visualisasi:
```
+------------------------+
|        Margin          |
|  +------------------+  |
|  |     Border       |  |
|  |  +------------+  |  |
|  |  |  Padding   |  |  |
|  |  |  +------+  |  |  |
|  |  |  |Content| |  |  |
|  |  |  +------+  |  |  |
|  |  +------------+  |  |
|  +------------------+  |
+------------------------+
```

#### Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox adalah model layout satu dimensi yang dirancang untuk menyusun elemen dalam baris atau kolom. Ini memberikan cara yang efisien untuk mendistribusikan ruang dan menyelaraskan item dalam sebuah container, bahkan ketika ukurannya tidak diketahui atau dinamis.

#### Kegunaan Flexbox:
- Membuat layout yang responsif dan fleksibel
- Menyelaraskan item secara vertikal dan horizontal dengan mudah
- Mengubah urutan tampilan elemen tanpa mengubah HTML
- Membuat navigasi bar yang responsif
- Membuat card layout yang fleksibel

#### Konsep Utama Flexbox:
- **Flex Container**: Elemen induk yang memiliki `display: flex`
- **Flex Items**: Elemen-elemen anak langsung dari flex container
- **Main Axis**: Sumbu utama flex container (horizontal untuk `row`, vertikal untuk `column`)
- **Cross Axis**: Sumbu yang tegak lurus dengan main axis

#### Properties Penting:
- `display: flex` pada container
- `flex-direction`, `justify-content`, `align-items` pada container
- `flex-grow`, `flex-shrink`, `flex-basis` pada items

### Grid Layout
Grid Layout adalah sistem layout dua dimensi yang memungkinkan Anda untuk mengatur konten dalam baris dan kolom secara bersamaan. Ini memberikan kontrol yang lebih besar atas layout halaman dibandingkan dengan Flexbox.

#### Kegunaan Grid Layout:
- Membuat layout halaman kompleks dengan mudah
- Mengatur elemen dalam grid yang presisi
- Membuat layout responsif yang dapat berubah drastis pada breakpoint berbeda
- Menangani layout dua dimensi dengan lebih efisien dibanding Flexbox

#### Konsep Utama Grid:
- **Grid Container**: Elemen induk yang memiliki `display: grid`
- **Grid Items**: Elemen-elemen anak langsung dari grid container
- **Grid Lines**: Garis pembatas yang membentuk struktur grid
- **Grid Tracks**: Baris atau kolom dalam grid
- **Grid Cells**: Perpotongan antara baris dan kolom
- **Grid Areas**: Kumpulan sel yang membentuk area tertentu

#### Properties Penting:
- `display: grid` pada container
- `grid-template-columns`, `grid-template-rows`, `grid-gap` pada container
- `grid-column`, `grid-row` pada items

#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
1. Mengimplementasi fungsi mengedit dan menghapus produk dengan menambahkan fungsi tersebut pada `views.py`.
```python
def edit_product(request, id):
    product = Product.objects.get(pk = id)

    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)
```

```python
def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()

    return HttpResponseRedirect(reverse('main:show_main'))
```

2. Mendesign halaman `login`, `register`, dan `add product` dengan menggunakan CSS Flexbox dan Grid Layout.
```html
<div class="container">
    <div class="login">
        <h2>Login</h2>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Login</button>
        </form>
    </div>
</div>
```

```css
.container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
}
```

3. Mendesign halaman daftar produk semenarik mungkin dengan menggunakan CSS, juga membuat `card_product.html` untuk menampilkan produk.
```html
<div class="bg-white rounded-lg shadow-md overflow-hidden max-w-xs w-full">
    <img src="https://images.unsplash.com/photo-1504198458649-3128b932f49e?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="{{ item.name }}" class="w-full h-48 object-cover">
    <div class="p-4">
        <h2 class="text-xl font-semibold text-gray-800 mb-2">{{ item.name }}</h2>
        <p class="text-green-600 font-bold text-lg mb-2">${{ item.price }}</p>
        <p class="text-gray-600 text-sm mb-4">{{ item.description }}</p>
        <p class="text-sm text-gray-500 mb-2">In stock: {{ item.stock }}</p>
        <div class="flex justify-between">
            <a href="{% url 'main:edit_product' item.pk %}" class="bg-background text-gray-600 px-6 flex justify-center items-center rounded hover:bg-backgroundSecondary transition duration-300 font-poppins">Edit</a>
            <a href="{% url 'main:delete_product' item.pk %}" class="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600 transition duration-300 font-poppins">Delete</a>
        </div>
    </div>
</div>
```

4. Membuat navbar yang responsif dengan menggunakan CSS Flexbox. (Kurang lebih seperti ini konsepnya)
```html
<nav class="flex items-center justify-between flex-wrap bg-background p-6">
    <div class="flex items-center flex-shrink-0 text-white mr-6">
        <span class="font-semibold text-xl tracking-tight">Zero</span>
    </div>
</nav>
```

## Tugas 6
#### Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
JavaScript adalah bahasa pemrograman yang digunakan untuk membuat aplikasi web menjadi interaktif dan dinamis. Manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web adalah sebagai berikut: 
1. **Interaktivitas**: JavaScript memungkinkan developers untuk membuat aplikasi web yang interaktif dan responsif. Dengan menggunakan JavaScript
2. **Validasi Form**: JavaScript memungkinkan developers untuk melakukan validasi form pada sisi klien. Dengan menggunakan JavaScript, developers dapat memvalidasi data yang dimasukkan oleh user sebelum data tersebut dikirim ke server.
3. **Manipulasi DOM**: JavaScript memungkinkan developers untuk memanipulasi DOM (Document Object Model) pada sisi klien. Dengan menggunakan JavaScript
4. **Ajax**: JavaScript memungkinkan developers untuk membuat aplikasi web yang asinkron. Dengan menggunakan JavaScript
5. **Animasi**: JavaScript memungkinkan developers untuk membuat animasi pada aplikasi web. Dengan menggunakan JavaScript

#### Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Fungsi dari penggunaan `await` ketika kita menggunakan `fetch` adalah untuk menunggu hingga proses fetch selesai sebelum melanjutkan eksekusi kode selanjutnya. Jika kita tidak menggunakan `await`, maka kode selanjutnya akan dieksekusi sebelum proses fetch selesai. Hal ini dapat menyebabkan data yang diambil dari server tidak tersedia saat kode selanjutnya dieksekusi. Dengan menggunakan `await`, kita dapat memastikan bahwa data yang diambil dari server tersedia sebelum kode selanjutnya dieksekusi.

#### Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Kita perlu menggunakan decorator `csrf_exempt` pada view yang akan digunakan untuk AJAX POST agar request POST yang dikirim melalui AJAX tidak memerlukan token CSRF. Jika kita tidak menggunakan decorator `csrf_exempt`, maka request POST yang dikirim melalui AJAX akan memerlukan token CSRF. Hal ini dapat menyebabkan request POST yang dikirim melalui AJAX gagal karena tidak menyertakan token CSRF.

#### Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Pembersihan data input pengguna dilakukan di belakang (backend) juga karena data input pengguna dapat dimanipulasi oleh user. Jika pembersihan data input pengguna dilakukan di frontend saja, maka user dapat memanipulasi data input pengguna sebelum data tersebut dikirim ke server. Hal ini dapat menyebabkan data input pengguna yang tidak valid atau berbahaya disimpan di database. Dengan melakukan pembersihan data input pengguna di belakang (backend), kita dapat memastikan bahwa data input pengguna yang disimpan di database valid dan aman.

#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
1. Ubah Kode Cards Data Mood untuk Mendukung AJAX GET: Mengubah kode pada `views.py` untuk mendukung AJAX GET dengan mengubah fungsi `show_json` dan `show_xml`.
```python
def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')
```
```python
def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')
```

2. Menggunakan Fetch API untuk Mengambil Data JSON dan XML: Menggunakan Fetch API pada JavaScript untuk mengambil data JSON dan XML dari server.
```javascript
fetch('/show_json')
    .then(response => response.json())
    .then(data => {
        ...
    });
```

3. Menggunakan `htmlString` dan `classNameString` untuk Menampilkan Data: Menggunakan `htmlString` dan `classNameString` pada JavaScript untuk menampilkan data JSON dan XML ke dalam elemen HTML.
```javascript
let htmlString = '';
data.forEach(item => {
    htmlString += `...`
});
document.querySelector('.cards').innerHTML = htmlString;
```

4. Membuat button untuk membuka modals yang dibuat dengan menggunakan `javascript` dan fitur POST AJAX. 
5. Membuat fungsi baru pada `views.py` untuk menambahkan produk dengan menggunakan AJAX POST.
```python
@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = bleach.clean(request.POST.get('name'), strip=True, tags=[], attributes={})
    price = bleach.clean(request.POST.get('price'), strip=True, tags=[], attributes={})
    description = bleach.clean(request.POST.get('description'), strip=True, tags=[], attributes={})
    stock = bleach.clean(request.POST.get('stock'), strip=True, tags=[], attributes={})
    user = request.user

    if not name:
        return JsonResponse({'status': 'ERROR', 'message': 'Name is required.'}, status=400)
    if not price:
        return JsonResponse({'status': 'ERROR', 'message': 'Price is required.'}, status=400)
    if not description:
        return JsonResponse({'status': 'ERROR', 'message': 'Description is required.'}, status=400)
    if not stock:
        return JsonResponse({'status': 'ERROR', 'message': 'Stock is required.'}, status=400)

    new_product = Product(
        name=name,
        price=price,
        description=description,
        stock=stock,
        user=user,
    )
    new_product.save()

    return JsonResponse({'status': 'CREATED'}, status=201)
```

6. Membuat path `/create-ajax/` di `urls.py` untuk menambahkan produk dengan menggunakan AJAX POST.
```python
path('create-ajax/', views.add_product_ajax, name='add_product_ajax'),
```

7. Menghubungkan form pada modal dengan fungsi `add_product_ajax` yang telah dibuat.

8. Merefresh halaman setelah produk berhasil ditambahkan dengan menggunakan fungsi `refreshProcts` pada JavaScript.