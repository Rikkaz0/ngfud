from flask import Flask, render_template

app = Flask(__name__)

# Dữ liệu giả lập về các bài viết với ảnh nền khác nhau
posts = [
    {
        "title": "Python - Ngôn ngữ lập trình mạnh mẽ",
        "author": "Lê Nguyên Phúc",
        "content": "Python có thể đóng vài trò như là một ngôn ngữ kịch bản cho ứng dụng web, chẳng hạn như thông qua mod wsgi đối với máy chủ web Apache. Với Giao diện Cổng vào Máy chủ Web, một API chuẩn đã và đang dần phát triển để tạo điều kiện cho các ứng dụng này. Các bộ khung web như Django, Pylons, Pyramid, TurboGears, web2py, Tornado, Flask, Bottle và Zope hỗ trợ các nhà phát triển trong khâu thiết kế và bảo trì các ứng dụng phức tạp. Pyjs và IronPython có thể được dùng để phát triển phía khách của các ứng dụng dựa trên Ajax. SQLAlchemy có thể được dùng để ánh xạ dữ liệu sang một cơ sở dữ liệu quan hệ. Twisted là một bộ khung dành cho việc giao tiếp giữa các máy tính và được sử dụng bởi Dropbox chẳng hạn các thư viện như NumPy, SciPy và Matplotlib cho phép sử dụng một cách có hiệu quả Python trong tính toán khoa học, với các thư viện chuyên ngành chẳng hạn như Biopython và Astropy cung cấp các chức năng miền cụ thể. SageMath là một hệ thống đại số máy tính với một giao diện vở lập trình được trong Python: thư viện của nó trải dài trên nhiều lĩnh vực của toán học, bao gồm đại số, toán tổ hợp, giải tích số, lý thuyết số và vi tích phân. OpenCV có gán kết Python với một tập hợp các tính năng phong phú về thị giác máy tính và xử lý ảnh. Python thường được sử dụng trong các dự án trí tuệ nhân tạo và học máy với sự giúp đỡ của các thư viện như TensorFlow, Keras, Pytorch và Scikit-learn. Vì là một ngôn ngữ kịch bản với kiến trúc mô đun, cú pháp đơn giản và các công cụ xử lý văn bản phong phú, Python cũng thường được sử dụng trong xử lý ngôn ngữ tự nhiên. Python có thể được sử dụng để phát triển các giao diện người dùng đồ hoạ (GUI) bằng cách sử dụng các thư viện như Tkinter, hay để tạo ra trò chơi thông qua các thư viện chẳng hạn như Pygame, một thư viện làm trò chơi 2D.",
        "id": 1,
        "image": "https://kama-software.com/wp-content/uploads/2022/11/cac-ky-nang-cua-mot-python-developer.jpg"
    },
    {
        "title": "Flask - Microframework cho phát triển web",
        "author": "Nguyễn Phạm Nguyên Huỳnh",
        "content": "Flask là một micro framework web viết bằng ngôn ngữ lập trình Python. Nó được sử dụng để xây dựng các ứng dụng web một cách đơn giản và linh hoạt, đặc biệt thích hợp cho các dự án nhỏ và vừa. Flask thuộc loại micro framework, có nghĩa là nó cung cấp một lõi nhỏ gọn với những tính năng cơ bản cần thiết cho một ứng dụng web, nhưng không có nhiều tính năng tích hợp sẵn như các framework lớn hơn như Django.",
        "id": 2,
        "image": "https://blog.appseed.us/content/images/2023/10/cover-flask.jpg"
    },
    {
        "title": "AI - Trí tuệ nhân tạo đang thay đổi thế giới",
        "author": "Lê Tấn Duy",
        "content": "AI (Trí tuệ nhân tạo) là công nghệ giúp máy tính thực hiện các tác vụ trí tuệ mà thường cần con người, như nhận diện hình ảnh, xử lý ngôn ngữ và học từ dữ liệu. AI bao gồm **Machine Learning (Học máy)**, nơi hệ thống học từ dữ liệu để cải thiện hiệu suất, và **Natural Language Processing (Xử lý ngôn ngữ tự nhiên)**, giúp máy hiểu và sinh ngôn ngữ con người. AI hiện có nhiều ứng dụng trong các lĩnh vực như y tế, tài chính và giao thông, mang lại lợi ích lớn nhưng cũng đối mặt với thách thức về đạo đức, bảo mật và tác động xã hội.",
        "id": 3,
        "image": "https://cdn.fpt-is.com/vi/hoc-lap-trinh-tri-tue-nhan-tao-ai-1715845761.webp"
    }
]

@app.route("/")
def home():
    return render_template("index.html", posts=posts)

@app.route("/post/<int:post_id>")
def post(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)
    return render_template("post.html", post=post) if post else "Bài viết không tồn tại", 404

if __name__ == "__main__":
    app.run(debug=True)
