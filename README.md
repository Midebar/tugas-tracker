## tugas-tracker

### Tugas 2
##### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Mengerjakan checklist sesuai urutan yang diberikan, dari membuat projek baru dengan `django-admin startproject` sampai dengan membuat logika views.py secara sederhana

##### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Client request -> urls.py memanggil views.py yang sudah diassign ke url tersebut -> views.py mereturn fungsi logik yang sudah dibuat termasuk mereturn template html yang dipanggil.

##### Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Ya dapat berjalan, hanya saja akan ada banyak dependensi/kekurangan dependensi jika tidak menggunakan virtual environment yang akan mengakibatkan bloat pada aplikasi yang ingin dijalankan, apalagi jika aplikasi tersebut di host pada cloud server

##### Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
MVC = Model View Controller
Model: Model bekerja sebagai bisnis logik dan perantara antara database dengan server/controller
View: View bekerja sebagai interface dari aplikasi yang disodorkan pada pengguna dan berinteraksi dengan controller, dan terkadang dengan model jika ada data yang diambil/disimpan
Controller: Controller bekerja dengan input dari user yang akan diproses oleh view dan di pass ke model jika diperlukan juga network layer

MVT = Model View Template
Model: Model bekerja sebagai bisnis logik dan perantara dengan database dan network
View: View bekerja sebagai logik fungsi dari aplikasi dan sebagai perantara antara model dan template
Template: Template bekerja sebagai interface dari aplikasi yang disodorkan pada pengguna dan berinteaksi dengan view

MVVM =  Model View ViewModel
Model: Model berkeja sebagai bisnis logik dan sebagai abstraksi data. Model dan ViewModel dibutuhkan jika ingin mengambil/menyimpan data
View: View bekerja sebagai pengamat ViewModel dan mengamati constraint dari user input untuk ViewModel
ViewModel: ViewModel bekerja sebagai fungsi logik yang menghandle input/output dari user dan server. Sebagai perantara antara model dan view

### Tugas3
##### Apa perbedaan antara form POST dan form GET dalam Django?
POST untuk mengirim data untuk disimpan dalam server, GET memanggil data dari server

##### Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
XML dan JSON merupakan tipe data yang biasa digunakan dalam pertukaran data antara client dan server, sedangkan HTML merupakan tipe data yang biasanya digunakan sebagai template page dari suatu halaman website. XML dan HTML memiliki kemiripan, yaitu mereka menggunakan DOM sebagai struktur dari data tersebut.

##### Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON berbentuk teks sehingga lebih ringan dan cepat untuk ditransfer dalam internet dan JSON memiliki logika yang sama dengan XML DOM

##### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Mengerjakan checklist sesuai urutan yang diberikan, dari membuat form, lalu memasukkannya ke logik views.py dan menaruh fungsi tersebut pada url baru di urls.py

### Tugas4
##### Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
UserCreationForm merupakan form untuk membuat user baru dari Django model User. 
Kelebihannya adalah kita bisa langsung memakai model User yang sudah disediakan oleh Django, kekurangannya adalah kita tidak bisa membuat custom user custom sesuai yang kita inginkan

##### Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi memverifikasi user yang login, sedangkan otorisasi memutuskan content/perintah kepada user yang telah autentikasi

##### Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies merupakan identifier dalam satu situs tertentu, sehingga tidak perlu melakukan login berulang-ulang jika pergi pada suatu subtab pada situs tersebut.
Django menghandle cookies 2 arah, yaitu menyimpannya pada client dan server dan saat user melakukan autentikasi dengan cookies yang ada, Django akan mengecek sesinya di server sesuai dengan cookies tersebut.

##### Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Cookies aman, selama tidak mengklik situs/aplikasi yang mempunyai cookies grabber pada javascript situs atau aplikasi tersebut.

##### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Membuat form dengan mengimport UserCreationForm dan serve di views.py. Buat URL routing untuk serve fungsi create user dari views.py. Mengupdate model Item dengan user, makemigrations, dan migrate.
Membuat fungsi login, logout untuk user dan menambahkan decorator views dan last login untuk landingpage dan logout di base_template.html.
Membuat dummy user dan menambahkan dummy data untuk tiap user.

### Tugas5
##### Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

##### Jelaskan HTML5 Tag yang kamu ketahui.

##### Jelaskan perbedaan antara margin dan padding.

##### Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

### Tugas 6
##### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

##### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

##### Jelaskan penerapan asynchronous programming pada AJAX.

##### Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.

##### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
