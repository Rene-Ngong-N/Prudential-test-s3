// pipeline {
//     agent any

//     stages {
//         stage('Make Bucket') {
//             steps {
//               withAWS(credentials: 'aws-creds', region: 'us-east-2') {
//                 sh 'python3 createS3bucket.py'

//               }
//             }
//         }
//         stage('Upload') {
//           steps {
//             withAWS(credentials: 'aws-creds', region: 'us-east-2') {
//              s3Upload(file:'rene.txt', bucket:'good-trying3', path:'rene.txt',)
//             }
//           }
//         }
//     }
// }

pipeline {
    agent any

    stages {
        stage('Make-Bucket') {
            steps {
              withAWS(credentials: 'aws-creds', region: 'us-east-2') {
                sh 'python3 createS3bucket.py'

              }
            }
        }
        stage('upload to Bucket') {
          steps{
              withAWS(credentials: 'aws-creds', region: 'us-east-2') {
                s3Upload(file:'file.txt', bucket:'good-trying', path:'file.txt',)
              }
            }
        }
    }
}

