class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        # if path is empty string
        if not new_path:
            return

        # Absolute Path
        if new_path.startswith("/"):
            self.current_path = new_path

        # Relative Path
        else:
            components = new_path.split("/")

            # something in current diretory
            if components[0] == ".":
                components[0] = self.current_path
                self.current_path = "/".join(components)

            # going back into parent directory
            elif components[0] == "..":
                curr_dir_tree = self.current_path.split("/")
                self.current_path = "/".join(curr_dir_tree[0:-1])
                self.cd("/".join(components[1:]))

            # if the path is relative
            # simply append it to existing path
            else:
                self.current_path = self.current_path + "/" + new_path


path = Path('/a/b/c/d')
path.cd('')
print(path.current_path)
