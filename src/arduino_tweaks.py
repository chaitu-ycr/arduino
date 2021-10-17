
# standard Python import area
import serial
import serial.tools.list_ports as ls_ports
from time import sleep as wait
import PySimpleGUI as sg


class Uno:
    """
    control Arduino UNO R3 Relay module using 'Uno' class.
    """

    def __init__(self, com_port=None):
        """
        :param str com_port: serial com port. example 'COM4'
        """
        self.com_port = com_port
        self.serial_comm_app = serial.Serial(timeout=0.5)
        self.serial_comm_app.port = self.com_port
        self.ON = 0x01
        self.OFF = 0x00

    def open_comm_port(self):
        """
        opens arduino com port.
        """
        if not self.serial_comm_app.is_open:
            self.serial_comm_app.open()
            wait(1.5)
            self.get_relays_status()

    def close_comm_port(self):
        """
        closes arduino com port.
        """
        if self.serial_comm_app.is_open:
            self.open_comm_port()
        else:
            print(f'Port({self.com_port}) already closed...')

    def out(self, relay_number=1, on_off=0):
        """
        function used for controlling relay
        example to turn on relay 1 --> out(relay_number=0x01, on_off=0x01)

        :param int relay_number: relay number
        :param int on_off: possible values(0 / 1). 0 for Turn OFF and 1 for Turning ON relay
        """
        if not self.serial_comm_app.is_open:
            self.open_comm_port()
        self.serial_comm_app.write(f'{relay_number}{on_off}'.encode())
        wait(0.1)

    def get_relays_status(self):
        """
        returns all relays status.
        Example - [0, 1, 0, 0]
        """
        if not self.serial_comm_app.is_open:
            self.open_comm_port()
        self.serial_comm_app.write('STATUS'.encode())
        wait(0.1)
        response = self.serial_comm_app.readline().decode()
        print(f'Relays Status--> {response}')
        # 'R1=0,R2=0,R3=0,R4=0'
        return [int(status[-1]) for status in response.split(',')[:-1]]

    def turn_off_on_relay(self, relay_number=1):
        """
        Turn OFF and Turn ON relay

        :param int relay_number: relay number
        """
        if not self.serial_comm_app.is_open:
            self.open_comm_port()
        self.out(relay_number=relay_number, on_off=0x00)
        wait(2)
        self.out(relay_number=relay_number, on_off=0x01)


class UnoGui(Uno):
    def __init__(self, title='Arduino UNO GUI'):
        super().__init__()
        self.gui_theme = sg.theme('BluePurple')
        self.title = title
        self.com_ports = []
        for port, _, _ in sorted(ls_ports.comports()):
            self.com_ports.append(port)
        self.layout = [
            [sg.Combo(values=self.com_ports, key='--COM_PORTS--', enable_events=True),
             sg.Button(button_text='open com port', key='--COM_PORT_BUTTON--', metadata=0)],
            [sg.Text(text='Digital Output 1', key='--DO_TEXT1--'), sg.Button(button_text='ON  ', key='--DO_BUTTON1--', metadata=0)],
            [sg.Text(text='Digital Output 2', key='--DO_TEXT2--'), sg.Button(button_text='ON  ', key='--DO_BUTTON2--', metadata=0)],
            [sg.Text(text='Digital Output 3', key='--DO_TEXT3--'), sg.Button(button_text='ON  ', key='--DO_BUTTON3--', metadata=0)],
            [sg.Text(text='Digital Output 4', key='--DO_TEXT4--'), sg.Button(button_text='ON  ', key='--DO_BUTTON4--', metadata=0)],
        ]
        self.window = sg.Window(title=self.title, layout=self.layout)


if __name__ == '__main__':
    ug = UnoGui()
    while True:
        event, values = ug.window.read()
        if event in (None, 'Exit'):
            break
        if event == '--COM_PORTS--':
            ug.com_port = list(values.values())[0]
            print(ug.com_port)
        if event == '--COM_PORT_BUTTON--':
            ug.window[event].metadata = 1 if ug.window[event].metadata == 0 else 0
            button_text = 'close com port' if ug.window[event].metadata == 1 else 'open com port'
            ug.window[event].update(text=button_text)
        if '--DO_BUTTON' in event:
            ug.window[event].metadata = 1 if ug.window[event].metadata == 0 else 0
            button_text = 'OFF' if ug.window[event].metadata == 1 else 'ON  '
            ug.window[event].update(text=button_text)
