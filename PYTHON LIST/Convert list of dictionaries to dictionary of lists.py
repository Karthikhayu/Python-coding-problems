data = [{'karthik': 'java', 'Giri': 'python'},
        {'karthik': 'php', 'Giri': 'java'},
        {'karthik': 'cloud', 'Giri': 'big-data'}]
print({key: [i[key] for i in data] for key in data[0]})