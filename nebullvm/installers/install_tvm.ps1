# Check if tvm directory exists
if (-not (Test-Path -Path 'tvm' -PathType Container)) { 
  git clone --recursive https://github.com/apache/tvm tvm
}

Set-Location -Path 'tvm'

if (-not (Test-Path -Path 'build' -PathType Container)) { 
  New-Item -Path 'build' -Type Directory
}

Copy-Item -Path $env:CONFIG_PATH -Destination 'build/' -Recurse -Force

Set-Location -Path 'build'

cmake ..
make -j8
pip3 install decorator attrs tornado psutil xgboost cloudpickle

Set-Location -Path '../python'
python3 setup.py install --user
Set-Location -Path '../..'
