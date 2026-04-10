#!/bin/bash

# 1. Criar diretório no HDFS (executar uma única vez)
# sudo -u hdfs hadoop fs -mkdir /user/datalake/raw

# 2. Iniciar o Agente Receptor (HDFS) em um terminal
echo "Iniciando Agente Receptor (HDFS)..."
sudo flume-ng agent -n agentehdfs -f agenteavro_hdfs.conf &

# Aguarda 5 segundos para garantir que a porta 44444 esteja aberta
sleep 5

# 3. Iniciar o Agente Coletor (AVRO) em outro terminal
echo "Iniciando Agente Coletor (Avro)..."
sudo flume-ng agent -n agenteavro -f agenteavro_hdfs.conf &

# 4. Iniciar o Gerador de Logs Python
echo "Iniciando Gerador de Logs..."
python gerador_log_web.py
