all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def filter_colors(colors):
    return colors["sexy"] is True

sexy_list = list(filter(filter_colors, all_colors))

def generate_li(sexy_colors):
    for color in sexy_colors:
        print("<li>"+color["label"]+"</li>")

generate_li(sexy_list)