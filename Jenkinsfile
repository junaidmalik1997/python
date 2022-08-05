pipeline {
          agent {
                 label 'xyz'       }
            stages {
                    stage('Test') { 
                                        steps
                                            {    

                                                 sh '''process=$(ss -lptn 'sport = :82' | grep -oP 'pid=\\K([0-9]*)' | head -n 1)
                                                     
                                                     python3 -m ensurepip --upgrade
                                                     pip3 install flask 
                                                     pm2 stop my-app.py
                                                     pm2 start my-app.py --interpreter python3 --watch'''
                                                
                                                           
                                                  }
                                                    }
                                                       }
                                                           }
