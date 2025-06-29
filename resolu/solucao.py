# ---------------------------------------------
# XOR Reverser para recuperar a chave secreta
# ---------------------------------------------

# Valor hexadecimal recebido do servidor
hex_encoded = ""  # Coloque a sua chave

fake_flag = 'THM{thisisafakeflag}'

# Converte o hexadecimal para bytes
xored_bytes = bytes.fromhex(hex_encoded)

# Realiza XOR reverso com a flag falsa
key_stream = [chr(b ^ ord(fake_flag[i % len(fake_flag)])) for i, b in enumerate(xored_bytes)]

# Extrai os primeiros 5 caracteres (chave de fato)
recovered_key = ''.join(key_stream[:5])

# Mostra o resultado
print(f"[+] XOR Encoded (hex): {hex_encoded}")
print(f"[+] Flag falsa usada   : {fake_flag}")
print(f"[+] Chave descoberta   : {recovered_key}")
