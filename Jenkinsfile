pipeline {
          agent any
            stages {
                    stage('Test') {
                                        steps
                                            {      sh ''' pwd 
                                            whoami
                                            aws --version
                                            python --version
                                            python -m ensurepip --upgrade
                                            pip install flask
                                            python my-app.py
                                                           ''' }
                                                            }
                                                            }
                                                            }

