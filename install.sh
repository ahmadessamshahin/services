#!/bin/bash

BASE_DIR=`readlink -f $(dirname ${0})`

if [ $EUID -eq 0 ]; then
	VERSION=$(curl -Is https://github.com/getsentry/onpremise/releases/latest | grep location | head -n 1 | cut -d ":" -f 2- | rev | cut -d "/" -f1 | rev | tr -d '\r')

	cd /opt
	wget https://github.com/getsentry/onpremise/archive/${VERSION}.tar.gz
	tar -xzf ${VERSION}.tar.gz
	
	cd /opt/onpremise-${VERSION}/
	/bin/bash install.sh
	if [ $? -eq 0 ]; then
		mv /var/lib/docker/volumes/sentry-postgres{,_orig}
		cd ${BASE_DIR}
		tar -xzf sentry-postgres.tar.gz
		mv sentry-postgres /var/lib/docker/volumes/sentry-postgres
		cd /opt/onpremise-${VERSION}/
		docker-compose up -d
		export MACHINE_IP=$(ip -o route get to 8.8.8.8 | sed -n 's/.*src \([0-9.]\+\).*/\1/p')
		cd ${BASE_DIR}
		docker-compose -f docker-compose-dev.yml up -d --build
	fi

else
	echo "User is not root, exiting"
	exit 1

fi
