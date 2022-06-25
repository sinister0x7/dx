from pydoc import render_doc
from tkinter import E


if (file_name == "file1.html" or file_name == "file2.html"):
    return render_template("fi.html", page_title = page_title, page_id = page_id, file_name=file_name)
else:
    return return render_template("fi.html", page_title = page_title, page_id = page_id, file_name="")