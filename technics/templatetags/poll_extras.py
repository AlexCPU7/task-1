from django import template

register = template.Library()


@register.filter(name='overload')
def overload(value, max):
    remainder = int(value) - int(max)
    if remainder > 0:
        try:
            overload = round(100 / int(max) * remainder, 2)
            return 'Перегруз составляет ' + str(overload) + '%'
        except (ValueError, TypeError):
            try:
                overload = round(100 / max * remainder, 2)
                return 'Перегруз составляет' + str(overload) + '%'
            except Exception:
                return ''
    else:
        return 'Перегруза нет'
