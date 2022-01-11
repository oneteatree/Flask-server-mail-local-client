from flask import Flask, request, render_template
import socket

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()

	# Create a UDP socket at client side
	UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
	
	# Send to server using created UDP socket

	UDPClientSocket.sendto(str.encode(text), ("127.0.0.1", 20001))
	
	msgFromServer = UDPClientSocket.recvfrom(1024)

	msg = "Message from Server {}".format(msgFromServer[0])
	print(msg)

    return render_template('index.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=80)
