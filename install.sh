#!/bin/bash

echo "
    **      **          **
  /**     /**         /**
  /**     /** **   ** /** *******  ******
  //**    ** /**  /** /**//**///**////**
   //**  **  /**  /** /** /**  /**   **
     //****   /**  /** /** /**  /**  **
      //**    //****** *** ***  /** ******
      //      ////// /// ///   // ////// 
"
echo "installing..."
echo "updating packages..."
apt update
apt upgrade
echo "downloading packages"
pkg install python2
echo "updating pip..."
pip2 install --upgrade pip
echo "Installing requirements..."
pip2 install -r requirements.txt


echo "Installation successful"
