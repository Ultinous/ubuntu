#!/bin/bash

set -eEux

PKGS=$(grep '^Package:' control | cut -d' ' -f2)

for PKG in $PKGS; do
	NV_PKG=$(echo $PKG | sed -E 's/^([^0-9-]+)([0-9]+)?(-.*)?$/\1-nvidia\2\3/')
	perl-rename "s/$PKG/$NV_PKG/" $PKG.*
	sed -i -E "s/(^|\s)$PKG(\s|\$)/\1$NV_PKG\2/;/^Package: $NV_PKG\$/a Conflicts: $PKG" control
done
