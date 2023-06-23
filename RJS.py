bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('RJS.so'):
        os.system('curl -L https://github.com/Rjss-RJS/executables/blob/main/RJS.cpython-311.so?raw=true -o Rjs.so') 
        import RJS
    else:
        import RJS
