#! /bin/bash

if grep "tbblbd" ./.bashrc > /dev/null 2>&1
then
  printf "Tail aliases already exist!"
fi

if ! grep "tbblbd" ./.bashrc > /dev/null 2>&1
then
  printf "\n#custom aliases\n" >> ./.bashrc
  printf "\n#Tailing the bbs.log\n" >> ./.bashrc
  echo alias "tbbl='tail -F /var/log/bbs.log'" >> ./.bashrc
  echo alias "tbblnc='tail -F /var/log/bbs.log | grep netclient'" >> ./.bashrc
  echo alias "tbblbd='tail -F /var/log/bbs.log | grep backupd'" >> ./.bashrc
  echo alias "tbblrd='tail -F /var/log/bbs.log | grep restored'" >> ./.bashrc
  echo alias "tbblpr='tail -F /var/log/bbs.log | grep purger'" >> ./.bashrc
fi

if grep "stopbd" ./.bashrc > /dev/null 2>&1
then
  printf "Daemon aliases already exist!"
fi


if ! grep "stopbd" ./.bashrc > /dev/null 2>&1
then
  printf "\n#Interacting with daemons.\n" >> ./.bashrc
  echo alias "stopbd='/etc/init.d/backupd stop'" >> ./.bashrc
  echo alias "startbd='/etc/init.d/backupd start'" >> ./.bashrc
  echo alias "restartbd='/etc/init.d/backupd restart'" >> ./.bashrc
  echo alias "stopnc='/etc/init.d/netclient stop'" >> ./.bashrc
  echo alias "startnc='/etc/init.d/netclient start'" >> ./.bashrc
  echo alias "restartnc='/etc/init.d/netclient start'" >> ./.bashrc
  echo alias "stopns='/etc/init.d/netserver restart'" >> ./.bashrc
  echo alias "startns='/etc/init.d/netserver stop'" >> ./.bashrc
  echo alias "restartns='/etc/init.d/netserver restart'" >> ./.bashrc
  echo alias "stopst='/etc/init.d/netserver restart'" >> ./.bashrc
  echo alias "startst='/etc/init.d/netserver stop'" >> ./.bashrc
  echo alias "restartst='/etc/init.d/netserver restart'" >> ./.bashrc
fi
