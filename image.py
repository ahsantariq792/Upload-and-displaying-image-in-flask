import os
from flask import render_template,Flask, request, session

UPLOAD_FOLDER = "./images"
# UPLOAD_FOLDER = os.path.join('staticFiles', 'images')

app = Flask(__name__ , template_folder='template', static_folder='images')
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.secret_key = 'This is your secret key to utilize session in Flask'

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file1" not in request.files:
            return "there is no file1 in form!"
        file1 = request.files["file1"]
        path = os.path.join(app.config["UPLOAD_FOLDER"], file1.filename)
        file1.save(path)
        return render_template('/showimage.html', user_image=path)

        # session['uploaded_img_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], path)
        # return "ok"
    return """
    <h1>Upload new File</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file1">
      <input type="submit">
    </form>
    """


@app.route('/show_image')
def displayImage():
    # Retrieving uploaded file path from session
    img_file_path = session.get('uploaded_img_file_path', None)
    # Display image in Flask application web page
    return render_template('/showimage.html', user_image = path)


if __name__ == "__main__":
    app.run()
