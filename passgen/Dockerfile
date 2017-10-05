FROM python:2.7
MAINTAINER chris elliott <ctelliott@gmail.com>

# install dependencies and clean up
RUN apt-get update && \
	apt-get install --no-install-recommends -q -y --force-yes \
		python-openssl && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# install dependencies
ADD ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# add passgen
ADD ./passgen.py /opt/passgen.py
RUN chmod +x /opt/passgen.py

CMD ["/opt/passgen.py"]
