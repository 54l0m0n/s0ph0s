#! /usr/bin/env python 
#coding: utf-8
from scapy.all import *

ip_alvo = raw_input("Digite o IP:")

ip = IP()
ping = ICMP()
ip.dst = ip_alvo
taxa = sr1(ip/ping)#calculo para tirar o TTL

#valores do TTL varia para cada tipo de S.O
if taxa.ttl < 30:
        print("IP:%s  Sistema Operacinal =  Cyclades"%(ip_alvo))

elif taxa.ttl > 30 and taxa.ttl < 64:
        print("IP:%s  Sistema Operacinal =  Linux"%(ip_alvo))

elif taxa.ttl > 98 and taxa.ttl < 128:
        print("IP:%s  Sistema Operacinal =  Windows"%(ip_alvo))
else:
        print("IP:%s  Sistema Operacinal = CISCO"%(ip_alvo))

print taxa.show() #mostra detalhes dos pacotes enviados, porém não é necessário apenas uma Info a mais.
