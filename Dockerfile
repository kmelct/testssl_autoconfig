FROM drwetter/testssl.sh

COPY . .

ENTRYPOINT [ "./sslWrapper.sh" ]

CMD ["./sslWrapper.sh"]