FROM python:3.11-slim-bookworm

WORKDIR /workspace

RUN apt-get update \
    && apt-get install -y build-essential \
    git \
    vim

WORKDIR /opt

RUN git clone https://github.com/FIUBA-Posgrado-Inteligencia-Artificial/intro_ia.git

ENV PYTHONPATH="/opt/intro_ia/clase2/hanoi_tower"

WORKDIR /workspace

COPY . .

RUN pip install --no-cache-dir -r deps.txt

CMD ["bash"]
