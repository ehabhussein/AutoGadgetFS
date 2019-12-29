<pre>
$ sudo apt install rabbitmq-server
$ sudo rabbitmq-plugins enable rabbitmq_management
|http://localhost:15672 ; guest/guest
 ---> upload the file rabbitMQbrokerconfig/rabbitmq-Config.json and not worry about the below stuff

$ sudo rabbitmqctl add_user autogfs usb4ever
$ sudo rabbitmqctl set_user_tags autogfs administrator
$ sudo service rabbitmq-server restart



1) goto web interface http://localhost:15672 and login with user: autogfs password: usb4ever  > Admin > click on autogfs username >
    set permission to virtualhost / ,dont need to do anything except press the Set permission button

2) goto Exchange > click on Add a new exchange > set the name to agfs , set the Type to Direct , set Durability to Durable >
    click Add exchange.

3)a) goto Queues > click on Add a new queue > set the name to: todevice , set durability to Durable > click add queue.
 3)b) goto Queues > click on Add a new queue > set the name to: tohost , set durability to Durable > click add queue.

4)a) goto Exchange > click on agfs > click on Bindings > to Queue set it to todevice , routingkey set to todev > click Bind
4)b) goto Exchange > click on agfs > click on Bindings > to Queue set it to tohost , routingkey set to tohst > click Bind
4)c) goto Exchange > click on agfs > click on Bindings > to Queue set it to tonull , routingkey set to tonull > click Bind
Done
</pre>
