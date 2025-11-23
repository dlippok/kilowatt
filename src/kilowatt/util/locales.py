import gettext
import locale


def init_locale(application_id):
    locale_dir = "/app/share/locale"
    locale.setlocale(locale.LC_ALL, '')
    locale.bindtextdomain(application_id, locale_dir)
    gettext.bindtextdomain(application_id, locale_dir)
    gettext.textdomain(application_id)
