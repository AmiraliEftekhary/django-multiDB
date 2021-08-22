class AuthRouter:
    route_app_labels = {
        "auth",
        "contenttypes",
        "admin",
        "sessions",
    }

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "default"
        elif model._meta.app_label == "firstApp":
            return "secondDB"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "default"
        elif model._meta.app_label == "firstApp":
            return "secondDB"
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "default"
        elif app_label == "firstApp" and db != "secondDB":
            return False
        else:
            return True
        return None
