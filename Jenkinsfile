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
                                                     python3 -m ensurepip --upgrade
                                                     pip3 install flask --user
                                                    
                                                     pm2 start my-app.py
                                                     ''',execTimeout: 240000, patternSeparator: '[, ]+', sourceFiles: 'my-app.py'
                                                     )], verbose: true)])
                                                
                                                           
                                                  }
                                                    }
                                                       }
                                                           }
