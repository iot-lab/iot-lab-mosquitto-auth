IoT-LAB Mosquitto auth backend
------------------------------

This project implements an HTTP authentification backend for the
[Eclipse Mosquitto broker](https://github.com/eclipse/mosquitto). The backend
is designed to work with the
[mosquitto-go-auth](https://github.com/iegomez/mosquitto-go-auth) plugin.

When this auth backend is used by the auth plugin, only users registered on
IoT-LAB are allowed to connect to the broker.
For a given user, ACLs only allow access to topics starting with the pattern
`iotlab/<username>`.
