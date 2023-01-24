echo Install libs...
sudo apt update
sudo apt upgrade
sudo apt install python3-pip 
sudo python3 -m pip install xlrd==1.2.0
sudo python3 -m pip install requests
echo Install libs - OK

# echo Load project...(alpha)...
# wget https://github.com/Reversi-Labs/Astra_store_core/archive/refs/heads/alpha.zip
# sudo apt install unzip
# unzip Astra_store_core-alpha.zip
# echo Load project - OK

echo Enjoy work with Astra_store_installer

#echo tap ENTRY
#read -s -n 1
# SETTINGS=`stty -g`
# stty -echo
# read -n 1
# stty $SETTINGS