pipeline {
          agent any
            stages {
                    stage('Test') {
                                        steps
                                            {      sh ''' pwd 
                                            whoami
                                            python3 -m ensurepip --upgrade
                                            pip install flask
                                            python my-app.py
                                                           ''' }
                                                            }
                                                            }
                                                            }

