#!/bin/sh -e
# called by uscan with '--upstream-version' <version> <file>
DIR=emscripten-$2
TAR=../emscripten_$2.orig.tar.gz
tar zxvf $TAR
cd $DIR

rm -fr third_party/closure-compiler/compiler.jar patches

# ship sources from web-socket-js
cd third_party/websockify/include/web-socket-js/
git clone https://github.com/gimite/web-socket-js.git src
rm -rf src/.git/
cd -

cd ../

tar --exclude-vcs -c -j -f ../emscripten_$2.orig.tar.bz2 $DIR
rm -rf $DIR $TAR

