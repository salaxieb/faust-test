- **https://dzone.com/articles/running-apache-kafka-on-windows-os** - установка kafka + zookeeper или запустить docker-compose up
- **start faust -a messages_producer worker -l info --web-port 6066** запуск генератора сообщений

- **start faust -A preprocess worker -l info --web-port 6067** - запуск преобработчика сообщений

- **start faust -A reply worker -l info --web-port 6068** - запуск первого генератора ответов

- **start faust -A reply worker -l info --web-port 6069** - запуск второго генератора ответов (т.к. один процесс не справляется с потоком)
