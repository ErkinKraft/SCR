[EN]
# SCR - Simple Call Room

SCR is designed for optimal voice communication performance, unlike giants like Discord, Skype, and TeamSpeak.

SCR currently does not offer the ability to mute your microphone, there are no friends, servers, text chats, or even an interface. But the most important thing is communication, and that's what SCR provides.

The program consists of a server-side and a client-side. If your ports are not open, you can use Radmin VPN (required on both sides) or ngrok (only on the server side).

In the future, I plan to add a separate administration section that will allow muting, adjusting the volume of users, kicking them from the call, and more.

## How to Use

1. Start the server by running SCRServer on the host machine (or another machine).
2. Enter the desired port number(0-65535) when prompted.
3. The client opens the client application by running SCRClient and enters the IP address and port number. Voilà! The server console should display a connection message.

## Advanced Information

- The server is based on the local address 127.0.0.1.
- If the host needs to be a participant in the call, use the local address (127.0.0.1) as the IP.
- When clients connect via ngrok, you unfortunately cannot track which IP address connected to you (ngrok's working principle).
- Best options for performance: open ports.
- Best option for gaming with a virtual LAN: Radmin VPN (or you can use Hamachi, but it's less stable).

Feel free to contribute to this project and make SCR even better!

[RU]
# SCR - Простая комната для звонков

SCR создана для оптимальной работы голосовой связи, в отличие от таких гигантов, как Discord, Skype и TeamSpeak.

В SCR в настоящее время нет возможности выключить микрофон, нет друзей, серверов, текстовых чатов или даже интерфейса. Но самое важное - это общение, и именно это предоставляет SCR.

Программа состоит из серверной и клиентской части. Если ваши порты закрыты, вы можете использовать Radmin VPN (необходим на обеих сторонах) или ngrok (только на стороне сервера).

В будущем я планирую добавить отдельный раздел администрирования, который позволит отключать звук у пользователей, регулировать громкость, исключать их из звонка и многое другое.

## Как использовать

1. Запустите сервер, запустив SCRServer на хост-машине (или на другой машине).
2. Введите желаемый номер порта(0-65535) при запросе.
3. Клиент открывает клиентское приложение, запустив SCRClient, и вводит IP-адрес и номер порта. Вуаля! В консоли сервера должно появиться сообщение о подключении.

## Дополнительная информация

- Сервер работает на локальном адресе 127.0.0.1.
- Если хост должен быть участником звонка, используйте локальный адрес (127.0.0.1) в качестве IP.
- Когда клиенты подключаются через ngrok, к сожалению, нельзя отследить IP-адрес, с которого они подключились (принцип работы ngrok).
- Лучший вариант для производительности: открытые порты.
- Лучший вариант для игр с виртуальной локальной сетью: Radmin VPN (или можно использовать Hamachi, но он менее стабилен).

Не стесняйтесь вносить свой вклад в этот проект и делать SCR еще лучше!
