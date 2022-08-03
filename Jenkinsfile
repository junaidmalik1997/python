pipeline {
          agent any
            stages {
                    stage('Test') {
                                        steps
                                            {     sshPublisher(publishers: [sshPublisherDesc(configName: 'junaid-targetinstance', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand:
                                                  '''sudo lsof -t -i:82 | xargs -r kill

                                                  sudo python3 -m ensurepip --upgrade
                                                  sudo pip3 install flask --user
                                                  sudo python3 my-app.py''',
                                                  patternSeparator: '[, ]+', sourceFiles: 'my-app.py')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: true)])
                                                
                                                           
                                                  }
                                                    }
                                                       }
                                                           }

