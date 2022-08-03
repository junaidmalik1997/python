pipeline {
          agent any
            stages {
                    stage('Test') {
                                        steps
                                            {    
                                                      catchError(buildResult: 'SUCCESS', stageResult: 'SUCCESS') { 
                                                            sh "exit 0"
                                                      }          
                                                      sshPublisher(publishers: [sshPublisherDesc(configName: 'junaid-targetinstance', 
                                                  transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand:
                                                  '''process=$(sudo ss -lptn 'sport = :82' | grep -oP 'pid=\\K([0-9]*)' | head -n 1)
                                                     sudo kill $process
                                                     sudo python3 -m ensurepip --upgrade
                                                     sudo pip3 install flask --user
                                                     sudo python3 my-app.py '',execTimeout: 130000,
                                                     patternSeparator: '[, ]+', sourceFiles: 'my-app.py')], verbose: true)])
                                                
                                                           
                                                  }
                                                    }
                                                       }
                                                           }
