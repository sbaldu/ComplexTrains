#

install_dir="~/.local/share/"
path_to_packer="CXXGraph/packaging/"

# Clone the repo of CXXGraph
git clone --depth 1 https://github.com/ZigRazor/CXXGraph.git $install_dir

cd $install_dir/$path_to_packer ;
# Compile 
mkdir -p build ;
cd build ;
cmake .. ; make ;

# Install CXXGraph
./tarballs ; 
sudo tar xjf CXXGraph--.tar.bz2 ;
sudo cp -r usr /

# Cleaning
rm -r $install_dir/CXXGraph
