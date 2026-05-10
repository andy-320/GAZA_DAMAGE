import os

def save_uploaded_files(before_file, after_file, upload_folder):

    os.makedirs(upload_folder, exist_ok=True)

    before_path = os.path.join(upload_folder, before_file.filename)

    after_path = os.path.join(upload_folder, after_file.filename)

    before_file.save(before_path)

    after_file.save(after_path)

    return before_path, after_path