FROM node:33-alpine3.19

COPY package*.json /
RUN npm install

COPY ./entrypoint.sh /

WORKDIR /home/app/frontend
COPY . .

EXPOSE 5173
ENTRYPOINT [ "sh", "/entrypoint.sh" ]
