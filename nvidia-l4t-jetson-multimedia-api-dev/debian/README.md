# Creating a nvidia-l4t-jetson-multimedia-api-dev debian package

## 0. Obtain the 'nvidia-l4t-jetson-multimedia-api' debian package from NVIDIA

    ls nvidia-l4t-jetson-multimedia-api_32.4.4-20201027211332_arm64.deb

## 1. Extract the debian package

    ar x nvidia-l4t-jetson-multimedia-api_32.4.4-20201027211332_arm64.deb

## 2. You will have the following files: control.tar.gz data.tar.bz2 debian-binary

## 3. Extract data

    tar xvf data.tar.bz2

## 4. Only the following directory will be extracted: usr

## 5. Remove unnecessary files from this directory

    rm -rf usr/src/jetson_multimedia_api/data/
    rm -rf usr/src/jetson_multimedia_api/argus/samples/
    rm -rf usr/src/jetson_multimedia_api/argus/docs/
    rm -rf usr/src/jetson_multimedia_api/argus/apps/camera/docs/

## 6. Verify that no unnecessary files remained

## 7. repack data.tar.bz2

    rm -rf data.tar.bz2
    tar cvjf data.tar.bz2 usr/

## 8. extract control.tar.gz

    tar xvf control.tar.gz

## 9. remove deleted files from md5sums

    sed -i -E '\@^[a-z0-9]+  usr/src/jetson_multimedia_api/data@d' md5sums
    sed -i -E '\@^[a-z0-9]+  usr/src/jetson_multimedia_api/argus/samples@d' md5sums
    sed -i -E '\@^[a-z0-9]+  usr/src/jetson_multimedia_api/argus/docs@d' md5sums
    sed -i -E '\@^[a-z0-9]+  usr/src/jetson_multimedia_api/argus/apps/camera/docs@d' md5sums

## 10. Update Package, Installed-Size and Depends fields inside control

    sed -i -E 's@^Package: .*$@Package: nvidia-l4t-jetson-multimedia-api-dev@' control
    sed -i -E "s@^Installed-Size: .*\$@Installed-Size: $(du -s usr/|cut -f1)@" control
    sed -i -E '/^Depends:/s@(,\s*)?tensorrt@@' control

## 11. repack control.tar.gz

    rm -rf control.tar.gz
    tar cvzf control.tar.gz control md5sums postinst

## 12. create nvidia-l4t-jetson-multimedia-api-dev package

    ar r nvidia-l4t-jetson-multimedia-api-dev_32.4.4-20201027211332_arm64.deb debian-binary control.tar.gz data.tar.bz2

## 13. ??

## 14. profit

