FROM node

ENV MONGO_DB_USERNAME=admin \
    MONGO_DB_PWD=qwerty

RUN mkdir -p testapp

COPY . /testapp

# RUN npm install                      // if there was not node_modules

CMD ["node","/testapp/server.js"]