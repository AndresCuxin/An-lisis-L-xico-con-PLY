import ply.lex as lex
# lista de tokens reconocidos
tokens = (
    'IF', 'ELSE', 'WHILE', 'IDENTIFICADOR', 'NUMERO', 'NUMERO_FLOAT', 'CADENA',
    'SUMA', 'RESTA', 'MULTIPLICACION', 'DIVISION', 'ASIGNACION', 'IGUALDAD',
    'PARENTESIS_IZQ', 'PARENTESIS_DER', 'CORCHETE_IZQ', 'CORCHETE_DER',
    'LLAVE_IZQ', 'LLAVE_DER', 'DOS_PUNTOS'
)
# palabras reservadas
reservadas = {'if': 'IF', 'else': 'ELSE', 'while': 'WHILE'}
# definicion de tokens para operadores y simbolos
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_ASIGNACION = r'='
t_IGUALDAD = r'=='
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_CORCHETE_IZQ = r'\['
t_CORCHETE_DER = r'\]'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_DOS_PUNTOS = r':'
# reconocer cadenas entre comillas
def t_CADENA(token):
    r'".*?"'
    token.value = token.value[1:-1]  #quitar comillas
    return token
# reconocer numeros flotantes
def t_NUMERO_FLOAT(token):
    r'\d+\.\d+'
    token.value = float(token.value)
    return token
# reconocer numeros enteros
def t_NUMERO(token):
    r'\d+'
    token.value = int(token.value)
    return token
# reconocer identificadores y palabras reservadas
def t_IDENTIFICADOR(token):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    token.type = reservadas.get(token.value, 'IDENTIFICADOR')
    return token
            # ignorar comentarios
def t_COMENTARIO(token):
    r'\#.*'
    pass  # no se almacena en los tokens

t_ignore = ' \t\n'  # ignorar espacios y tabulaciones
# manejar errores
def t_error(token):
    print(f"Error léxico: Carácter ilegal '{token.value[0]}' en línea {token.lineno}")
    token.lexer.skip(1)
# construir el analizador lexico
lexer = lex.lex()
# codigo de prueba
codigo_ejemplo = '''
if x == 10:
    y = x + 3.14 * (z - 2) / 4
    mensaje = "Hola, mundo"
    # Esto es un comentario
else:
    y = x - 2
'''
# alimentar el lexer con el codigo de prueba
lexer.input(codigo_ejemplo)

print("\nTokens generados:") # imprimir los tokens generados
print("{:<15} {:<15} {:<10}".format("Token", "Valor", "Línea"))
print("-" * 40)
for token in lexer:
    print("{:<15} {:<15} {:<10}".format(token.type, str(token.value), token.lineno))
