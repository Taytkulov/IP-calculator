# About this project

## Prehistory

This is my first project that was implemented as a graphical application. I submitted this work as part of my university coursework. I realise that the code is far from perfect, but, as everyone knows, there is no limit to perfection and I have room to grow. Publishing this project on github is also a part of my self-education. I am ready to answer all questions for those who are interested

## Libraries

The only library that has been used in this programme is `tkinter`. All calculations were performed by means of Python language.

## Work process

The whole code is conditionally divided into two parts: Logical and GUI configuration via tkinter. The names of all variables were chosen in such a way that an IT specialist could logically guess the meaning of a variable and easily understand what it is responsible for. The programme was created as a prototype of [cisco IP calculator](https://infocisco.ru/ip_calculator.php). 

### Logic

So, the user enters the ip address, after which the programme checks the entered value. The presence of four octets, absence of extraneous characters and octet value within 0-255 is checked. If at least one of the conditions is violated - the programme requires the address to be entered again. As soon as the correct address is received, the variables are started. Variables responsible for the block with binary representation work with the help of the bin function, decimal representation is performed with the help of ordinary arithmetic. If necessary, I will supplement this file with an explanation of each function. 

### Tkinter

In the tkinter job block, everything is implemented in a simple way. Inscriptions are added to the GUI screen with `Labels`, input and output windows with `Entries`, and subnet mask selection is done with `Comboboxes`. Decimal representation is highlighted in purple colour, and binary representation in green (according to all _Matrix_ canons). In the grid menu each function is indented and the corresponding rows and columns are set. In the future it is planned to modify the ip address input window a bit.  

## Launch on Windows/MacOS

The code was compiled using the [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/) library for two operating systems (macOS and Windows). In order to run the application on Windows you need to download the `.exe` file and the `.png` icon to the same directory. In the future, I will try to find a way to run the application with the icon saved without having to download it to the device. 

For MacOS, you need to download the `.rar` archive and run directly through it. I have also attached the `.app` file for convenience. 

## P.S.

Thank you to those who took the time to read this text and test the app itself. I will be glad to receive any feedback and advice. I attach my mail for contact below. I hope this is not my last project and soon you will see updates in my profile. Good luck to everyone!

timur.aytkulov.04@mail.ru