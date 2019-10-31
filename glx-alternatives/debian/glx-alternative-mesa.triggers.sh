#!/bin/sh
set -e

echo "interest-await register-glx-alternative-mesa"
echo

TRIPLETS="/ /i386-linux-gnu/ /x86_64-linux-gnu/ /arm-linux-gnueabihf/"
LIBS="libGL.so.1 libEGL.so.1 libGLESv1_CM.so.1 libGLESv2.so.2 libGLX_mesa.so.0"
SOLINKS="libGL.so libEGL.so libGLESv1_CM.so libGLESv2.so libGLX_indirect.so.0"

for lib in $SOLINKS $LIBS
do
	for triplet in $TRIPLETS ; do
		echo "interest-await /usr/lib${triplet}$lib"
		echo "interest-await /usr/lib/mesa-diverted${triplet}$lib"
		echo
	done
	echo
done
