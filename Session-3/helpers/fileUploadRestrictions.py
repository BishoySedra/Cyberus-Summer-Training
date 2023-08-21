max_size = 1024 * 1024 * 12  # 12 MB
allowed_extensions = {"jpg", "png", "jpeg", "gif"}


def allowed_file_extension(filename):
    extension = filename.rsplit(".")[1].lower()
    return "." in filename and extension in allowed_extensions


def allowed_file_size(file):
    return len(file.read()) <= max_size
