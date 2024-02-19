#!/usr/bin/env sh

folder_path="./image_arch"

if [ -d $folder_path ]; then
  echo "Папка $folder_path существует"
else
  echo "Папки $folder_path не существует"
  exit 1

fi

