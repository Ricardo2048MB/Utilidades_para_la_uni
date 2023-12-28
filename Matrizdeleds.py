#El siguiente abecedario está codificado para una matriz de LEDs 5x7. Las letras suben (supuestamente).
"""
    Autor del módulo: Ricardo Muñoz Bolaños
    Fecha de creación: 28 de noviembre de 2023
    
    Propósito: Transformar una cadena de caracteres en una serie de bytes
    de manera sencilla para volcar el resultado en un archivo binario
    usando el software HxD.
    
    Lema: Un script tan sencillo que todo lo que usé para crearlo lo aprendí
    en mis clases de fundamentos de programación.
"""
###################NOTA: Todavía puede mejorarse.
_vaciio = "00000000000000"
_A = "0E11111F111111"
_B = "0F11110F11110F"
_C = "0E11010101110E"
_D = "0F11111111110F"
_E = "1F01010F01011F"
_F = "1F01010F010101"
_G = "0E11111D11110E"
_H = "1111F1F1111111"
_I = "1F04040404041F"
_J = "1F08080809090E"
_K = "11090503050911"
_L = "0101010101011F"
_M = "111B1511111111"
_N = "00001313151D19"
_NN = "0D001313151D19"
_O = "0E11111111110E"
_P = "0F11110F010101"
_Q = "0E111111150916"
_R = "0F11110F050911"
_S = "0E11010E10110E"
_T = "1F040404040404"
_U = "1111111111110E"
_V = "11111111110A04"
_W = "11111111151B11"
_X = "11110A040A1111"
_Y = "11111B04040404"
_Z = "1F10080402011F"
_a = "0E11101E111916"
_b = "0101010F11110F"
_c = "00000E1101110E"
_d = "1010101E11111E"
_e = "00000E110F011E"
_f = "0E110107010101"
_g = "1619111E10110E"
_h = "0101010F111111"
_i = "00040004040404"
_j = "08000808080906"
_k = "01090503050911"
_l = "04040404040404"
_m = "00011B15151111"
_n = "00000D13111111"
_nn ="0E000D13111111"
_o = "00000E1111110E"
_p = "000E11110F0101"
_q = "000E11110F0101"
_r = "00000D13010101"
_s = "000E11060C110E"
_t = "0101010701110E"
_u = "0000111111110E"
_v = "00001111110A04"
_w = "00001111151B11"
_x = "0000110A040A11"
_y = "0011111F10100E"
_z = "00001F180C031F"
_aa = "08040016191916"
_ee = "1C000E110F010E"
_ii = "08040004040404"
_oo = "0C000E1111110E"
_uu = "0804111111110E"
_guioon = "0000000E000000"
_punto = "00000000000303"
_coma = "000000000C0C06"
_dos_puntos = "000C0C000C0C00"
_punto_y_coma = "000C0C000C0E00"
_pareentesis_de_apertura = "0C10101010100C"
_pareentesis_de_cierre = "06010101010106"
_carita_feliz = "000A0000110E00"

def recorrer(cadena, tgrupo=8):####Antes era 7
    """
        Recibe una cadena y produce un efecto de transición hacia arriba en una matriz de leds.
        
        Parámetros:
        
        cadena: Es la cadena a recorrer.
        tgrupo: Es el tamaño de los grupos que se deben mostrar en cada cuadro (en bytes).
    """
####NOTA: PRÓXIMAMENTE TENGO QUE ACTUALIZAR ÉSTA FUNCIÓN
    tgrupo *= 2 ####sentencia experimental
    lista_cadenas = []
    lista_cadenasb = []
    nueva_cadena = ""
    for i in range(0, len(cadena) - tgrupo + 1):
        lista_cadenas.append(cadena[0+i:i+tgrupo])
    for i in range(0, len(lista_cadenas)):
        if i % 2 == 0:
            lista_cadenasb.append(lista_cadenas[i])
    for i in range(0, len(lista_cadenasb)):
        ##print(lista_cadenasb[i])
        nueva_cadena += lista_cadenasb[i]
    print()
    print(nueva_cadena)
    

def invertirBytes(cadena_de_bytes):
    """
        Recibe una cadena de caracteres que representa una serie de bytes e invierte el orden de los bytes.
        Ojo: no invierte el orden del nibble.
        Devuelve una cadena de caracteres que representa los bytes dados en orden inverso.
        Por ejemplo, si el programa recibe "442345AF", devolverá "AF452344"
        Ah, por cierto, la cadena recibida debe contener un número par de caracteres.
    """
    if len(cadena_de_bytes) % 2 != 0:
        raise ValueError("La cadena debe contener un número par de caracteres.")
    cadena_invertida = ""
    for i in range(-2, -len(cadena_de_bytes)-1, -2):
        cadena_invertida += cadena_de_bytes[i+len(cadena_de_bytes):i+len(cadena_de_bytes)+2]
    return cadena_invertida


def convertirCaracter(caracter):
    """
        Esta función recibe como parámetro un caracter. Puede ser A-Z, a-z,
        vocales minúsculas con tilde, guión intermedio (signo menos), punto,
        coma, punto y coma, paréntesis de apertura y de cierre, y emoji de
        carita feliz.
        
        Lo que se obtendrá al ejecutar la función es el caracter codificado
        para aparecer correctamente en una matriz de LED's de 5 columnas
        por 7 filas.
    """
    match caracter:
        case 'A':
            return _A
        case 'B':
            return _B
        case 'C':
            return _C
        case 'D':
            return _D
        case 'E':
            return _E
        case 'F':
            return _F
        case 'G':
            return _G
        case 'H':
            return _H
        case 'I':
            return _I
        case 'J':
            return _J
        case 'K':
            return _K
        case 'L':
            return _L
        case 'M':
            return _M
        case 'N':
            return _N
        case 'Ñ':
            return _NN
        case 'O':
            return _O
        case 'P':
            return _P
        case 'Q':
            return _Q
        case 'R':
            return _R
        case 'S':
            return _S
        case 'T':
            return _T
        case 'U':
            return _U
        case 'V':
            return _V
        case 'W':
            return _W
        case 'X':
            return _X
        case 'Y':
            return _Y
        case 'Z':
            return _Z
        case 'a':
            return _a
        case 'b':
            return _b
        case 'c':
            return _c
        case 'd':
            return _d
        case 'e':
            return _e
        case 'f':
            return _f
        case 'g':
            return _g
        case 'h':
            return _h
        case 'i':
            return _i
        case 'j':
            return _j
        case 'k':
            return _k
        case 'l':
            return _l
        case 'm':
            return _m
        case 'n':
            return _n
        case 'ñ':
            return _nn
        case 'o':
            return _o
        case 'p':
            return _p
        case 'q':
            return _q
        case 'r':
            return _r
        case 's':
            return _s
        case 't':
            return _t
        case 'u':
            return _u
        case 'v':
            return _v
        case 'w':
            return _w
        case 'x':
            return _x
        case 'y':
            return _y
        case 'z':
            return _z
        case 'á':
            return _aa
        case 'é':
            return _ee
        case 'í':
            return _ii
        case 'ó':
            return _oo
        case 'ú':
            return _uu
        case '.':
            return _punto
        case ',':
            return _coma
        case '-':
            return _guioon
        case ':':
            return _dos_puntos
        case ';':
            return _punto_y_coma
        case '☺':
            return _carita_feliz
        case '(':
            return _pareentesis_de_apertura
        case ')':
            return _pareentesis_de_cierre
        case ' ':
            return _vaciio
        case _:
            print("Debes escribir un caracter válido")



def crudoACB(texto):
    """
        Convierte una cadena de texto en una cadena que representa bytes.
        Recibe una cadena de texto.
        Devuelve la cadena de texto con los bytes correspondientes a cada letra.
    """
    cadena_bytes = ""
    for i in range(len(texto)):
        cadena_bytes += convertirCaracter(texto[i])
    return cadena_bytes


def bytesConEfecto(texto):
    """
        Esta función recibe como parámetro una cadena de texto y devuelve
        la cadena transformada a una cadena que representa bytes escalonados
        para una matriz de LEDS. (Ojo: específicamente para una de 5 columnas
        por 7 filas). El hecho de estar escalonados da a la representación
        de la matriz el efecto de aparecer un caracter tras otro.
    """
    ##NOTA: Esto también puede mejorar si le pongo una triple repetición en cuanto
    ########se complete un caracter distinto de _vacio.
    recorrer(crudoACB(texto))