import os 
base_url = '/proyectoodontologia' 
for root, dirs, files in os.walk('.'): 
    for file in files: 
        if file.endswith('.html') or file.endswith('.css'): 
            path = os.path.join(root, file) 
            with open(path, 'r', encoding='utf-8', errors='ignore') as f: 
                content = f.read() 
            new_content = content.replace('src="/', 'src="' + base_url + '/').replace('href="/', 'href="' + base_url + '/') 
            with open(path, 'w', encoding='utf-8', errors='ignore') as f: 
                f.write(new_content) 
print('Listo!') 
