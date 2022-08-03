pipeline {
          agent any
            stages {
                    stage('Test') {
                                        steps
                                            {     sshPublisher(publishers: [sshPublisherDesc(configName: 'junaid-targetinstance', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand:
                                                  '''sudo python3 -m ensurepip --upgrade
                                                  sudo pip3 install flask --user
                                                  sudo python3 my-app.py''',
                                                  execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '', remoteDirectorySDF: false, removePrefix: '', sourceFiles: 'my-app.py')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])
                                      
                                                           
                                                  }
                                                    }
                                                       }
                                                           }

