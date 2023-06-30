import simpleaudio as sa
import time
import socket

host = socket.gethostname()
port = 8080
buffer_s = 100
bl = 5

opc = '00'

b1 = sa.WaveObject.from_wave_file('808 Samples/kick.WAV')
b2 = sa.WaveObject.from_wave_file('808 Samples/clap.wav')
b3 = sa.WaveObject.from_wave_file('808 Samples/snare.WAV')
b4 = sa.WaveObject.from_wave_file('808 Samples/hi hat.wav')

b5 = sa.WaveObject.from_wave_file('808 Samples/hi hat (1).WAV')
b6 = sa.WaveObject.from_wave_file('808 Samples/cymbal.wav')
b7 = sa.WaveObject.from_wave_file('808 Samples/tom.WAV')
b8 = sa.WaveObject.from_wave_file('808 Samples/bass.wav')

b9 = sa.WaveObject.from_wave_file('808 Samples/kick (1).WAV')
b10 = sa.WaveObject.from_wave_file('808 Samples/clap (1).wav')
b11 = sa.WaveObject.from_wave_file('808 Samples/snare (1).WAV')
b12 = sa.WaveObject.from_wave_file('808 Samples/hi hat (2).WAV')

b13 = sa.WaveObject.from_wave_file('808 Samples/hi hat (3).wav')
b14 = sa.WaveObject.from_wave_file('808 Samples/cymbal (1).wav')
b15 = sa.WaveObject.from_wave_file('808 Samples/tom (1).WAV')
b16 = sa.WaveObject.from_wave_file('808 Samples/bass (1).wav')


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen(bl)


    while True:
        if opc == 'ff':
            break
        conn,addr = s.accept()
        with conn:
            print('[*] Conectado a '+ str(addr[0]))
            while True:
                if opc == 'ff':
                    break
                msg = conn.recv(buffer_s)
                opc = msg.decode('utf-8')
                if not msg:
                    break
                else:
                    print('[*] {}'.format(msg.decode('utf-8')))
                    if opc == '11':
                        play_b1 = b1.play()
                    elif opc == '12':
                        play_b2 = b2.play()
                    elif opc == '13':
                        play_b3 = b3.play()
                    elif opc == '14':
                        play_b4 = b4.play()
                    elif opc == '21':
                        play_b5 = b5.play()
                    elif opc == '22':
                        play_b6 = b6.play()
                    elif opc == '23':
                        play_b7 = b7.play()
                    elif opc == '24':
                        play_b8 = b8.play()
                    elif opc == '31':
                        play_b9 = b9.play()
                    elif opc == '32':
                        play_b10 = b10.play()
                    elif opc == '33':
                        play_b11 = b11.play()
                    elif opc == '34':
                        play_b12 = b12.play()
                    elif opc == '41':
                        play_b13 = b13.play()
                    elif opc == '42':
                        play_b14 = b14.play()
                    elif opc == '43':
                        play_b15 = b15.play()
                    elif opc == '44':
                        play_b16 = b16.play()

        