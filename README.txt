# Balloon_Project_2019

      
          ,'````',
    .`',.'        `..'``',      ____
  ,'                     `', .-'    '-.                                 
 ;                        ..' /)       '.         ,'``',  ,..,   ,..,
  ',            ,.,    .'`/  (/          \     ,.'      '`    '.'    ;
    '.,.`'.,,,.`   `''`  ;                ;  ,`                       ',
                         |                | ;                           ;
                      ___|                | `.,     ;    ,...         ,'
                   .-'   ;                ;    `.,.' `,.'    `,.     ;
                 .' /)    \              /                      `.,,'
                /  (/      '.          .' '.
               ;             '-._  _.-'     \
               |                |)(          ;
               |                (__)         |
               ;                ;/           |
                \              //            ;
                 '.          .'/            /
                   '-._  _.-' /.          .'
                       )(    /  '-._  _.-'
                      (__)  /       )(
                       |   /       (__)
                       |  /       _,'
                       | /    _,'
                       |/._,'
               --------------------------
               | Blargenoso's High      |
               | Altitude balloon code  |
               --------------------------
                              
                      ######################################################################
                      #                                                                    #
                      #           High altitude anotated camera feed (Camera.py)           #
                      #                                                                    #
                      ######################################################################

This code is for raspberry pis equiped with a sense hat and camera equiped. It also will need an i2c altimiter in future iterations. The code adds the temperature and altitude to the top of the camera feed, refreshed every second. the feed is recorded and stored every 30 minutes in the H.264 format to an external storage device. the iterative nature of the code means the video will be saved even in the event of a catastrophic faliure. The i2c altimiter code will be added as parts come in over time.


                      ######################################################################
                      #                                                                    #
                      #           Sensor Data Collection  (Temp.py)                        #
                      #                                                                    #
                      ######################################################################
                      
This code collects sensor data from the pi's sense hat such as pressure and temperature, as well as altitude data from an i2c altimiter, to compile a .csv file of the nature of the pi's surroundings. It stores thee files every 30 minutes to an external storage device, inside the balloon's black box. The code also makes use of the sense hat's led array, but this can be turned off by changing the value of the variable 'led' to 0.

                      ######################################################################
                      #                                                                    #
                      #       User manual (all of this info can be found in the wiki)      #
                      #                                                                    #
                      ######################################################################
                      
To initiate the code on startup, folllow the following commands:

~: crontab -e
@reboot python path/Temp.py
@reboot python path/Camera.py
ctrl+x
y
enter

To enable the camera on startup, follow these commands
~: sudo nano /boot/config.txt
gpu_mem=128
disable_camera_led=1
start_file=start_x.elf
fixup_file=fixup_x.dat

To enable the i2c altimiter we are using on this project, follow these commands (make sure you are connected to the internet)
On raspibian:
sudo apt-get install build-essential libi2c-dev i2c-tools python-dev libffi-dev
On arch linux:
pacman -S base-devel
pacman -S i2c-tools

once we have that installed, the rest is the same for both versions
pip install cffi
pip install smbus-cffi
pip install git+https://github.com/bivab/smbus-cffi.git
git clone https://github.com/bivab/smbus-cffi.git
