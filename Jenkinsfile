pipeline {
          agent any
            stages {
                    stage('Test') {
                                        steps
                                            {      sh ''' pwd 
                                            whoami
                                            aws --version
                                            python3 --version
                                            sudo python3 -m ensurepip --upgrade
                                            sudo pip3 install flask --user
                                            sudo python3 my-app.py
                                                           ''' 
                                                  }
                                                    }
                                                       }
                                                           }

