import base64

import cv2


def img_to_base64(img_path):
    img = cv2.imread(img_path)

    _, buffer = cv2.imencode('.jpg', img)
    text = base64.b64encode(buffer).decode('ascii')
    return text


def create_html_file(text, file_name):
    html_pattern = """
    <html>
    <body>
    <img src="data:image/png;base64,{}"/>
    </body>
    </html>
    """

    html = html_pattern.format(text)
    with open(file_name, 'w') as f:
        f.write(html)


if __name__ == '__main__':
    img_path = 'data/cat.jpg'
    html_file_name = 'data/show_img.html'

    text = img_to_base64(img_path)
    create_html_file(text, html_file_name)
