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
