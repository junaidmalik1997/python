pipeline {
          agent any
            stages {
                    stage('Test') {
                                        steps
                                            {      sh ''' pwd 
                                            whoami
                                            aws --version
                                            python3 --version
                                            echo "1"
                                            sudo python3 -m ensurepip --upgrade
                                            echo "2"
                                            sudo pip3 install flask --user
                                            echo "3"
                                            sudo python3 my-app.py
                                                           ''' 
                                                  }
                                                            }
                                                            }
                                                            }

