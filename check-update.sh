#!/bin/sh
curl "https://github.com/libyal/libvmdk/releases" 2>/dev/null |grep "tag/" |sed -e 's,.*tag/,,;s,\".*,,;' |head -n1


