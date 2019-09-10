FROM drwetter/testssl.sh

RUN ./testssl.sh --quiet --color 0 --jsonfile-pretty=file.json fulcrum.rocks

RUN cat file.json

ENTRYPOINT [ "cat", "file.json" ]

CMD ["cat", "file.json"]