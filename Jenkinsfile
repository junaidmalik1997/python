pipeline {
          agent any
            stages {
                    stage('Test') {
                                        steps
                                            {    
                                                      sshPublisher(publishers: [sshPublisherDesc(configName: 'junaid-targetinstance', 
                                                  transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand:
                                                  '''process=$(sudo ss -lptn 'sport = :82' | grep -oP 'pid=\\K([0-9]*)' | head -n 1)
                                                     sudo kill $process
                                                     sudo python3 -m ensurepip --upgrade
                                                     sudo pip3 install flask --user
                                                     sudo pm2 start my-app.py --interpreter python3''',execTimeout: 130000,
                                                     patternSeparator: '[, ]+', sourceFiles: 'my-app.py')], verbose: true)])
                                                
                                                           
                                                  }
                                                    }
                                                       }
                                                           }
