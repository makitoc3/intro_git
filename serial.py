import serial
ser = serial.Serial('/dev/tty.',9600,timeout=None)  # �f�o�C�X���ƃ{�[���[�g��ݒ肵�|�[�g���I�[�v�� 
ser.write("hello")      # �o��
ser.close()             # �|�[�g�̃N���[�Y
ser = serial.Serial('/dev/ttyS0', timeout=0.1)  # timeout��b�Őݒ�idefault:None)�{�[���[�g�̓f�t�H���g��9600
c = ser.read()  # 1�����ǂݍ���
str = ser.read(10)  # �w��������ǂݍ��� ������timeout���ݒ肳��Ă���k�͓ǂݎ�ꂽ������
line = ser.readline()  # �s�I�['?n'�܂Ń��[�h����
ser.close()
