class DB:
    def __init__(self) -> None:
        self.contents = {}
        self.views = {}
        self.users = {}

    def add_content(self, content):
        try:
            self.contents[content.id] = content
            return True
        except Exception as e:
            print(e)
            return False

    def add_view(self, view):
        try:
            self.views[view.id] = view
            return True
        except Exception as e:
            print(e)
            return False

    def add_user(self, user):
        try:
            self.users[user.id] = user
            return True
        except Exception as e:
            print(e)
            return False

    def search_content(self, id):
        try:
            return self.contents[id]
        except Exception as e:
            print(e)
            return False

    def search_view(self, id):
        try:
            return self.views[id]
        except Exception as e:
            print(e)
            return False

    def search_user(self, id):
        try:
            return self.users[id]
        except Exception as e:
            print(e)
            return False

    def get_contents(self):
        try:
            return self.contents
        except Exception as e:
            print(e)
            return False

    def get_views(self):
        try:
            return self.views
        except Exception as e:
            print(e)
            return False

    def get_users(self):
        try:
            return self.users
        except Exception as e:
            print(e)
            return False

    def delete_content(self, id):
        try:
            del self.contents[id]
            return True
        except Exception as e:
            print(e)
            return False

    def delete_view(self, id):
        try:
            del self.views[id]
            return True
        except Exception as e:
            print(e)
            return False

    def delete_user(self, id):
        try:
            del self.users[id]
            return True
        except Exception as e:
            print(e)
            return False

    def update_content(self, content):
        try:
            self.contents[content.id] = content
            return True
        except Exception as e:
            print(e)
            return False

    def update_view(self, view):
        try:
            self.views[view.id] = view
            return True
        except Exception as e:
            print(e)
            return False

    def update_user(self, user):
        try:
            self.users[user.id] = user
            return True
        except Exception as e:
            print(e)
            return False

    def search_content_by_link(self, link):
        try:
            for content in self.contents.values():
                if content.link == link:
                    return content
            return False
        except Exception as e:
            print(e)
            return False

    def search_content_by_name(self, name):
        try:
            for content in self.contents.values():
                if content.name == name:
                    return content
            return False
        except Exception as e:
            print(e)
            return False

    def add_view_to_content(self, content_id, view):
        try:
            self.contents[content_id].views.append(view)
            return True
        except Exception as e:
            print(e)
            return False
