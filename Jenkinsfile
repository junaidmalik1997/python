pipeline {
          agent {
                 label 'xyz'       }
            stages {
                    stage('Test') { 
                                        steps
                                            {    

                                                 sh '''
                                                     pwd
                                                     whoami
                                                     python3 -m ensurepip --upgrade
                                                     pip3 install flask 
                                                     pm2 stop my-app.py || echo "process not found"
                                                     pm2 start my-app.py --interpreter python3 --watch'''
                                                
                                                           
                                                  }
                                                    }
                                                       }
                                                           }
