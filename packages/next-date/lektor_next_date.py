from datetime import datetime
from dateutil.rrule import rrulestr
from lektor.pluginsystem import Plugin


def next_date(rule, fmt="%Y-%m-%d"):
    now = datetime.now()
    r = rrulestr("RRULE:" + rule, dtstart=now.replace(day=1))
    nxt = r.after(now, inc=True)
    return nxt.strftime(fmt) if nxt else None


class NextDatePlugin(Plugin):
    name = 'next-date'

    def on_setup_env(self, **extra):
        self.env.jinja_env.globals['next_date'] = next_date
