#!/bin/bash

BASE_DIR=`dirname ${0}`
if [ $EUID -eq 0 ]; then
	VERSION=$(curl -Is https://github.com/getsentry/onpremise/releases/latest | grep location | head -n 1 | cut -d ":" -f 2- | rev | cut -d "/" -f1 | rev | tr -d '\r')

	cd /opt
	wget https://github.com/getsentry/onpremise/archive/${VERSION}.tar.gz
	tar -xzf ${VERSION}.tar.gz
	
	cd /opt/onpremise-${VERSION}/
	/bin/bash install.sh
	if [ $? -eq 0 ]; then
		docker-compose up -d
	fi

else
	echo "User is not root, exiting"
	exit 1

fi
