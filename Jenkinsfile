pipeline {
          agent any
            stages {
                    stage('Test') {
                                        steps
                                            {      sh '''  python3 -m ensurepip --upgrade
                                                           pip3 install flask
                                                           sudo chmod 777 my-app.py
                                                           python3 my-app.py
                                                           ''' }
                                                            }
                                                            }
                                                            }

