pipeline {
          agent any
            stages {
                    stage('Test') {
                                        steps
                                            {      sh ''' pwd 
                                            whoami
                                            python3 -m ensurepip --upgrade
                                            pip3 install flask
                                            sudo python3 my-app.py
                                                           ''' }
                                                            }
                                                            }
                                                            }

