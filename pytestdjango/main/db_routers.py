
class DefaultRouter(object):

    APPS_TO_DBS = {
        'first': 'default',
        'second': 'second',
    }

    def db_for_read(self, model, **hints):
        return self.APPS_TO_DBS.get(model._meta.app_label, 'default')

    def db_for_write(self, model, **hints):
        return self.APPS_TO_DBS.get(model._meta.app_label, 'default')

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True
