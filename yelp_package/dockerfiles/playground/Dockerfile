FROM examplecluster_itest_trusty
RUN apt-get update && apt-get install -y openssh-server docker.io curl vim
RUN mkdir -p /var/log/paasta_logs 
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN mkdir /var/run/sshd
RUN mkdir -p /nail/etc
RUN ln -s /etc/paasta/mesos-cli.json /nail/etc/mesos-cli.json
ADD ./start.sh /start.sh
