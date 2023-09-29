FROM python:3.11

COPY . .

RUN pip3 install -r requirements.txt

ENV PORT=8080

ENTRYPOINT python3 lbg.py --PORT ${PORT}