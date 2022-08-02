pipeline {
          agent any
            stages {
                    stage('Test') {
                                        steps
                                            {      sh ''' pwd 
                                            whoami
                                            python3 -m ensurepip --upgrade
                                            pip3 install flask
                                            python my-app.py
                                                           ''' }
                                                            }
                                                            }
                                                            }

