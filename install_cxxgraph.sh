#

install_dir="~/.local/share/"
path_to_packer="CXXGraph/packaging/"

git clone --depth 1 https://github.com/ZigRazor/CXXGraph.git $install_dir

cd $install_dir/$path_to_packer ;
./tarballs ; 
sudo tar xjf CXXGraph--.tar.bz2 ;
sudo cp -r usr /
