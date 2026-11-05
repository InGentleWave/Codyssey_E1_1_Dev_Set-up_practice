# Command Log

## 4. 터미널 조작

### 현재 위치 확인 (pwd)

```bash
root@cdcdc0e4bd3c:/# pwd
/
```

### 숨김 파일 포함 목록 확인 (ls -la)

```bash
root@cdcdc0e4bd3c:/# ls -la
total 60
drwxr-xr-x   1 root root 4096 Nov  3 12:19 .
drwxr-xr-x   1 root root 4096 Nov  3 12:19 ..
-rwxr-xr-x   1 root root    0 Nov  3 12:19 .dockerenv
drwxr-xr-x   2 root root 4096 Oct 25 10:26 .rock
lrwxrwxrwx   1 root root    7 Apr 20  2026 bin -> usr/bin
drwxr-xr-x   2 root root 4096 Apr 20  2026 boot
drwxr-xr-x   5 root root  360 Nov  3 12:19 dev
drwxr-xr-x   1 root root 4096 Nov  3 12:19 etc
drwxr-xr-x   3 root root 4096 Oct 25 10:26 home
lrwxrwxrwx   1 root root    7 Apr 20  2026 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Apr 20  2026 lib64 -> usr/lib64
drwxr-xr-x   2 root root 4096 Oct 25 10:25 media
drwxr-xr-x   2 root root 4096 Oct 25 10:25 mnt
drwxr-xr-x   2 root root 4096 Oct 25 10:25 opt
dr-xr-xr-x 200 root root    0 Nov  3 12:19 proc
drwx------   2 root root 4096 Oct 25 10:26 root
drwxr-xr-x   4 root root 4096 Oct 25 10:26 run
lrwxrwxrwx   1 root root    8 Apr 20  2026 sbin -> usr/sbin
drwxr-xr-x   2 root root 4096 Oct 25 10:25 srv
dr-xr-xr-x  12 root root    0 Nov  3 12:19 sys
drwxrwxrwt   2 root root 4096 Oct 25 10:25 tmp
drwxr-xr-x  12 root root 4096 Oct 25 10:24 usr
drwxr-xr-x  11 root root 4096 Oct 25 10:26 var
```

### 절대 경로 이동, 상대 경로 이동 수행

```bash
root@cdcdc0e4bd3c:/# cd /ant/spider
root@cdcdc0e4bd3c:/ant/spider# cd ../../
root@cdcdc0e4bd3c:/#
```

### 디렉터리 생성 (mkdir -p)

```bash
root@cdcdc0e4bd3c:/# mkdir -p ant 
root@cdcdc0e4bd3c:/# ls
ant  bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  temp  tmp  usr  var
```

### 파일 복사 (cp), 파일 이동 또는 이름 변경 (mv)

파일 복사 (cp)
```bash
root@cdcdc0e4bd3c:/# cp -r /ant/spider /ant/dog
root@cdcdc0e4bd3c:/# cd /ant
root@cdcdc0e4bd3c:/ant# ls
dog  spider
```
파일 이동 (mv)
```bash
root@cdcdc0e4bd3c:/ant# ls
dog  spider
root@cdcdc0e4bd3c:/ant# mv ./spider ./dog/
root@cdcdc0e4bd3c:/ant# ls
dog
root@cdcdc0e4bd3c:/ant# ls ./dog
spider
```
이름 변경 (mv)
```bash
root@cdcdc0e4bd3c:/ant# ls ./dog
spider
root@cdcdc0e4bd3c:/ant# mv ./dog/spider ./ladybug
root@cdcdc0e4bd3c:/ant# ls
dog  ladybug
```

### 파일 삭제 (rm)(삭제 전후 목록 기록)

삭제 전
```bash
root@cdcdc0e4bd3c:/ant# ls /ant /ant/dog
/ant:
dog  ladybug

/ant/dog:
cat
```
삭제 후
```bash
root@cdcdc0e4bd3c:/ant# rm ./dog
rm: cannot remove './dog': Is a directory
root@cdcdc0e4bd3c:/ant# rm -r ./dog
root@cdcdc0e4bd3c:/ant# ls
ladybug
```

### 파일 내용 확인 (cat 또는 less)

```bash
root@cdcdc0e4bd3c:/# cat /etc/os-release 
PRETTY_NAME="Ubuntu 26.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="26.04"
VERSION="26.04.1 LTS (Resolute Raccoon)"
VERSION_CODENAME=resolute
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=resolute
LOGO=ubuntu-logo
```

### 빈 파일 생성 (touch)

```bash
root@cdcdc0e4bd3c:/ant# touch file.txt
root@cdcdc0e4bd3c:/ant# ls
file.txt  ladybug
root@cdcdc0e4bd3c:/ant# cat ./file.txt
root@cdcdc0e4bd3c:/ant#
```


## 5. 권한 실습

### 파일 1개 권한 확인 (ls -l), 변경 (chmod), 변경 전후 비교
```bash
root@cdcdc0e4bd3c:/ant# ls -l file.txt
-rw-r--r-- 1 root root 0 Nov  3 12:40 file.txt
root@cdcdc0e4bd3c:/ant# chmod 600 ./file.txt
root@cdcdc0e4bd3c:/ant# ls -l file.txt
-rw------- 1 root root 0 Nov  3 12:40 file.txt
```
### 디렉터리 1개 권한 확인 (ls -ld), 변경 (chmod), 변경 전후 비교
```bash
root@cdcdc0e4bd3c:/ant# ls -ld ladybug
drwxr-xr-x 2 root root 4096 Nov  3 12:26 ladybug
root@cdcdc0e4bd3c:/ant# chmod 700 ./ladybug
root@cdcdc0e4bd3c:/ant# ls -ld ladybug
drwx------ 2 root root 4096 Nov  3 12:26 ladybug
```
## 6. Docker

### 6-1. 설치 및 점검

#### docker --version 출력 기록
```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker --version
Docker version 29.9.2, build a82e528
```
#### docker info 출력 기록 (데몬 동작 확인)
```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker info
Client:
 Version:    29.9.2
 Context:    desktop-linux
 Debug Mode: false
 Plugins:
  agent: Docker AI Agent Runner (Docker Inc.)
    Version:  v1.152.0
    Path:     C:\Program Files\Docker\cli-plugins\docker-agent.exe
  ai: Docker AI Agent - Ask Gordon (Docker Inc.)
    Version:  v1.33.0
    Path:     C:\Program Files\Docker\cli-plugins\docker-ai.exe
  buildx: Docker Buildx (Docker Inc.)
    Version:  v0.38.1
    Path:     C:\Program Files\Docker\cli-plugins\docker-buildx.exe
  compose: Docker Compose (Docker Inc.)
    Version:  v5.6.1
    Path:     C:\Program Files\Docker\cli-plugins\docker-compose.exe
  debug: Get a shell into any image or container (Docker Inc.)
    Version:  0.49.0
    Path:     C:\Program Files\Docker\cli-plugins\docker-debug.exe
  desktop: Docker Desktop commands (Docker Inc.)
    Version:  4.97.0
    Path:     C:\Program Files\Docker\cli-plugins\docker-desktop.exe
  dhi: CLI for managing Docker Hardened Images (Docker Inc.)
    Version:  v0.0.9
    Path:     C:\Program Files\Docker\cli-plugins\docker-dhi.exe
  extension: Manages Docker extensions (Docker Inc.)
    Version:  v0.2.32
    Path:     C:\Program Files\Docker\cli-plugins\docker-extension.exe
  init: Creates Docker-related starter files for your project (Docker Inc.)
    Version:  v1.4.1
    Path:     C:\Program Files\Docker\cli-plugins\docker-init.exe
  mcp: Docker MCP Plugin (Docker Inc.)
    Version:  v0.44.2
    Path:     C:\Program Files\Docker\cli-plugins\docker-mcp.exe
  model: Docker Model Runner (Docker Inc.)
    Version:  v1.2.9
    Path:     C:\Program Files\Docker\cli-plugins\docker-model.exe
  offload: Docker Offload (Docker Inc.)
    Version:  v0.7.21
    Path:     C:\Program Files\Docker\cli-plugins\docker-offload.exe
  pass: Docker Pass Secrets Manager Plugin (beta) (Docker Inc.)
    Version:  v0.3.2
    Path:     C:\Program Files\Docker\cli-plugins\docker-pass.exe
  sandbox: "docker sandbox" is deprecated, use Docker Sandboxes instead (Docker Inc.)
    Version:  v0.13.0
    Path:     C:\Program Files\Docker\cli-plugins\docker-sandbox.exe
  scout: Docker Scout (Docker Inc.)
    Version:  v1.27.0
    Path:     C:\Program Files\Docker\cli-plugins\docker-scout.exe

Server:
 Containers: 0
  Running: 0
  Paused: 0
  Stopped: 0
 Images: 3
 Server Version: 29.9.2
 Storage Driver: overlayfs
  driver-type: io.containerd.snapshotter.v1
 Logging Driver: local
 Cgroup Driver: cgroupfs
 Cgroup Version: 2
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local splunk syslog
 CDI spec directories:
  /etc/cdi
  /var/run/cdi
 Discovered Devices:
  cdi: docker.com/gpu=webgpu
 Swarm: inactive
 Runtimes: nvidia runc io.containerd.runc.v2
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: b7a25261e029d68978bbf290df0a62fc819b3c51
 runc version: v1.5.2-0-g29dd3dc2
 init version: de40ad0
 Security Options:
  seccomp
   Profile: builtin
  cgroupns
 Kernel Version: 6.18.54.1-microsoft-standard-WSL2
 Operating System: Docker Desktop
 OSType: linux
 Architecture: x86_64
 CPUs: 12
 Total Memory: 6.448GiB
 Name: docker-desktop
 ID: 550b5363-70ee-480b-86fe-9b010fd83450
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 HTTP Proxy: http.docker.internal:3128
 HTTPS Proxy: http.docker.internal:3128
 No Proxy: hubproxy.docker.internal
 Labels:
  com.docker.desktop.address=npipe://\\.\pipe\docker_cli
 Experimental: false
 Insecure Registries:
  hubproxy.docker.internal:5555
  127.0.0.0/8
  ::1/128
 Live Restore Enabled: false
 Firewall Backend: iptables
```
### 6-2. Docker 기본 운영 명령

#### 이미지: 다운로드/목록 확인(예: docker images)

```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker images
                                                                                                     i Info →   U  In Use
IMAGE                ID             DISK USAGE   CONTENT SIZE   EXTRA
hello-world:latest   c567b231f656       25.9kB         9.49kB    U   
my-web:latest        de28cc6696af        241MB         63.9MB        
ubuntu:latest        6a06111c3b0a        163MB         45.9MB    U 
```

#### 컨테이너: 실행/중지/목록 확인(예: docker ps, docker ps -a)

```powershell
#docker ps 기본 : 실행 중인 docker 컨테이너 목록 조회
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker ps  
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS         PORTS     NAMES
cdcdc0e4bd3c   ubuntu    "/bin/bash"   51 minutes ago   Up 2 minutes             mybox
#docker ps -a : 모든 docker 컨테이너 목록 조회 (all)
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker ps -a
CONTAINER ID   IMAGE         COMMAND       CREATED             STATUS                         PORTS     NAMES
ecfae3219076   ubuntu        "/bin/bash"   4 minutes ago       Exited (137) 2 minutes ago               yourbox
034b2e6b02d0   hello-world   "/hello"      5 minutes ago       Exited (0) 5 minutes ago                 keen_perlman
cdcdc0e4bd3c   ubuntu        "/bin/bash"   51 minutes ago      Up 2 minutes                             mybox
e0d56166363f   hello-world   "/hello"      About an hour ago   Exited (0) About an hour ago             elated_shockley
#docker ps -l : 가장 마지막으로 생성된 컨테이너 목록 조회 (latest) - 실행상태 무관
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker ps -l
CONTAINER ID   IMAGE     COMMAND       CREATED         STATUS                       PORTS     NAMES
ecfae3219076   ubuntu    "/bin/bash"   4 minutes ago   Exited (137) 2 minutes ago             yourbox
```

#### 운영: 로그 확인(예: docker logs), 리소스 확인(예: docker stats)

로그 확인 (docker logs)
```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker logs elated_shockley

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

```
리소스 확인 (docker stats)
```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker stats mybox
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
cdcdc0e4bd3c   mybox     0.00%     0B / 0B             0.00%     0B / 0B   0B / 0B     0
```

#### 컨테이너 실행, 중지, 재시작, 삭제 각 단계의 상태 변화 기록

```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker ps -a
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS                       PORTS     NAMES
cdcdc0e4bd3c   ubuntu    "/bin/bash"   53 minutes ago   Exited (137) 3 seconds ago             mybox
```
컨테이너 실행
```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker start mybox
mybox
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker ps -a      
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS         PORTS     NAMES
cdcdc0e4bd3c   ubuntu    "/bin/bash"   54 minutes ago   Up 3 seconds             mybox
```
컨테이너 중지
```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker stop mybox
mybox
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker ps -a     
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS                       PORTS     NAMES
cdcdc0e4bd3c   ubuntu    "/bin/bash"   54 minutes ago   Exited (137) 4 seconds ago             mybox
```
컨테이너 재시작
```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker start mybox
mybox
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker ps -a      
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS         PORTS     NAMES
cdcdc0e4bd3c   ubuntu    "/bin/bash"   54 minutes ago   Up 9 seconds             mybox
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker restart mybox
mybox
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker ps -a        
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS        PORTS     NAMES
cdcdc0e4bd3c   ubuntu    "/bin/bash"   54 minutes ago   Up 1 second             mybox
```
컨테이너 삭제
```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker stop mybox
mybox
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker rm mybox
mybox
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker ps -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```


### 6-3. 컨테이너 실행 실습

#### hello-world 실행 성공 기록
```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```
#### ubuntu 이미지 다운로드
```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker pull ubuntu
Using default tag: latest
latest: Pulling from library/ubuntu
f3f25b84a7d7: Pull complete 
edafa32f5d9e: Pull complete 
21594acc2d8b: Download complete 
Digest: sha256:6a06111c3b0a8600feadb270aec771dc239bf407b25625f93f44ab00e11f4d3c
Status: Downloaded newer image for ubuntu:latest
docker.io/library/ubuntu:latest
```
#### ubuntu 컨테이너 대화형 실행, 내부에서 ls와 echo 수행 결과 기록
```console
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker run -it --name mybox ubuntu
root@cdcdc0e4bd3c:/# ls
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@cdcdc0e4bd3c:/# echo $SHELL
/bin/bash
```
#### attach와 exec의 차이 정리
docker attach 컨테이너ID : 
컨테이너의 메인 프로세스에 표준 입출력을 연결함. exit 입력 시 메인 프로세스 즉 컨테이너가 종료됨
```console
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker start mybox
mybox
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker ps -a
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS         PORTS     NAMES
f51cf60939c8   ubuntu    "/bin/bash"   55 seconds ago   Up 4 seconds             mybox
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker attach mybox
root@f51cf60939c8:/# exit
exit
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker ps -a
CONTAINER ID   IMAGE     COMMAND       CREATED              STATUS                     PORTS     NAMES
f51cf60939c8   ubuntu    "/bin/bash"   About a minute ago   Exited (0) 4 seconds ago             mybox
```

docker exec 컨테이너ID 명령어: 
컨테이너에 메인 프로세스와 무관한 새 프로세스를 실행하여 명령어에 대한 출력값을 받고 프로세스를 종료함. -it(대화형) 옵션을 사용하여 bash등과 같은 대화형 쉘을 사용할 수 있음. 이 때 exit를 입력하면 쉘이 종료되고 메인 프로세스는 계속 실행이 유지됨.

```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker ps -a
CONTAINER ID   IMAGE     COMMAND       CREATED         STATUS         PORTS     NAMES
f51cf60939c8   ubuntu    "/bin/bash"   5 minutes ago   Up 4 minutes             mybox
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker exec mybox ls
bin
boot
dev
etc
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker ps -a
CONTAINER ID   IMAGE     COMMAND       CREATED         STATUS         PORTS     NAMES
f51cf60939c8   ubuntu    "/bin/bash"   6 minutes ago   Up 4 minutes
```
docker exec -it 컨테이너ID 쉘 예시
```console
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker ps -a
CONTAINER ID   IMAGE     COMMAND       CREATED         STATUS         PORTS     NAMES
f51cf60939c8   ubuntu    "/bin/bash"   9 minutes ago   Up 8 minutes             mybox
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker exec -it mybox bash
root@f51cf60939c8:/# ls
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@f51cf60939c8:/# exit
exit

What's next:
    Try Docker Debug for seamless, persistent debugging tools in any container or image → docker debug mybox
    Learn more at https://docs.docker.com/go/debug-cli/
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker ps -a
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS          PORTS     NAMES
f51cf60939c8   ubuntu    "/bin/bash"   15 minutes ago   Up 13 minutes
```

## 7. Dockerfile 기반 웹 서버 컨테이너

### docker build 실행 명령 및 결과 로그
빌드 및 확인

```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker build -t exam .
[+] Building 7.8s (7/7) FINISHED                                          docker:desktop-linux
 => [internal] load build definition from Dockerfile                                      0.0s
 => => transferring dockerfile: 223B                                                      0.0s
 => [internal] load metadata for docker.io/library/nginx:stable-alpine                    3.0s
 => [internal] load .dockerignore                                                         0.0s
 => => transferring context: 2B                                                           0.0s
 => [internal] load build context                                                         0.0s
 => => transferring context: 59B                                                          0.0s
 => [1/2] FROM docker.io/library/nginx:stable-alpine@sha256:0e52bd054126cdc040b1276c0af3  3.0s
 => => resolve docker.io/library/nginx:stable-alpine@sha256:0e52bd054126cdc040b1276c0af3  0.0s
 => => sha256:5b8cb54cfa408030aaa43d7bffa9141e0ae6f8a479df13c7aa152100 20.31MB / 20.31MB  2.1s
 => => sha256:bb658a2541968d2b90a8ee165ad08b7f71055c7f7832bdff98e2de2d8b 1.40kB / 1.40kB  0.5s
 => => sha256:81b64ae234ef95f3cfc19b7f6c45a511eccbefa6148889ee33ed43c6c3 1.21kB / 1.21kB  0.6s
 => => sha256:e125989d16f03d1e00b60afdd9abe46ed1437ed63b73926d036a5537f6be77 403B / 403B  0.7s
 => => sha256:885725a63a7cf1d4d5aac105944b35ece2b69a8c2cc6f7040f04727b7b8a63 964B / 964B  0.2s
 => => sha256:f19a2d3b695178ba0e57d473535f74f5d934f45e191de8334e730f83d2c627 627B / 627B  0.2s
 => => sha256:9f0afb44f10e826253b342c0265e188067c2f0a30c782a52e329928a76 1.88MB / 1.88MB  1.0s
 => => extracting sha256:9f0afb44f10e826253b342c0265e188067c2f0a30c782a52e329928a763adc6  0.2s
 => => extracting sha256:f19a2d3b695178ba0e57d473535f74f5d934f45e191de8334e730f83d2c6270  0.0s
 => => extracting sha256:885725a63a7cf1d4d5aac105944b35ece2b69a8c2cc6f7040f04727b7b8a63d  0.1s
 => => extracting sha256:e125989d16f03d1e00b60afdd9abe46ed1437ed63b73926d036a5537f6be770  0.0s
 => => extracting sha256:81b64ae234ef95f3cfc19b7f6c45a511eccbefa6148889ee33ed43c6c3f3993  0.0s
 => => extracting sha256:bb658a2541968d2b90a8ee165ad08b7f71055c7f7832bdff98e2de2d8b90cf1  0.0s
 => => extracting sha256:5b8cb54cfa408030aaa43d7bffa9141e0ae6f8a479df13c7aa152100cca358f  0.4s
 => [2/2] COPY src/index.html /usr/share/nginx/html/index.html                            0.2s
 => exporting to image                                                                    1.3s
 => => exporting layers                                                                   0.2s
 => => exporting manifest sha256:b213b9f8d2d446bb27b332c3e4861eb4da341d1d9a47f3118e06038  0.0s
 => => exporting config sha256:fb1ddaa55058bc1b22f6ae61114226f7fa77a1985d7faeaa2310c6dfa  0.0s
 => => exporting attestation manifest sha256:592e031c43577f67d5a4726911818810341c58b5517  0.0s
 => => exporting manifest list sha256:792e890320716d914ecc78a650a132aa4328defe969ee785f1  0.0s
 => => naming to docker.io/library/exam:latest                                            0.0s
 => => unpacking to docker.io/library/exam:latest

PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker images
                                                                          i Info →   U  In Use
IMAGE                ID             DISK USAGE   CONTENT SIZE   EXTRA
exam:latest          792e89032071       92.7MB         26.1MB        
hello-world:latest   c567b231f656       25.9kB         9.49kB        
my-web:latest        de28cc6696af        241MB         63.9MB        
ubuntu:latest        6a06111c3b0a        163MB         45.9MB
```

실행 및 결과

```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker run -d -p 8080:80 --name exam1 exam
23d21ba10c8b57f64a62bf1a890330687cf47009b60b3a01130a1d973b007e29

PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker ps -a
CONTAINER ID   IMAGE     COMMAND                   CREATED         STATUS                     PORTS                                     NAMES
23d21ba10c8b   exam      "/docker-entrypoint.…"   4 minutes ago   Up 4 minutes               0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   exam1
f51cf60939c8   ubuntu    "/bin/bash"               20 hours ago    Exited (255) 2 hours ago                                         mybox
```

## 9. 바인드 마운트 반영 + 볼륨 영속성 증거

### 9-1. 바인드 마운트 반영

#### 호스트 디렉터리를 컨테이너에 연결하는 실행 명령 기록

```
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker run -d --name bind-mount-p 8082:80 --mount type=bind,source="C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\src\index.html",target=/usr/share/nginx/html/index.html,readonly nginx
Unable to find image 'nginx:latest' locally
latest: Pulling from library/nginx
Digest: sha256:5ab5b0b01097420873a3f3330f44248e34a3c2a3e8d5ee30658aeae8cb7435da
Status: Downloaded newer image for nginx:latest
303efc9479f57785231cf6340644d9670df164de2b4614a841bf8849514bffe2
```

#### 호스트 파일 변경 전/후 내용 비교

호스트 파일 변경 전
![호스트 파일 변경 전](./docker-bind-mount-before-host-change.png)

호스트 파일 변경 후
![호스트 파일 변경 후](./docker-bind-mount-after-host-change.png)

### 9-2. Docker 볼륨 영속성 검증

#### 볼륨 생성/연결/검증 로그
진행 전 확인
```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker volume ls
DRIVER    VOLUME NAME
```
생성
```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker volume create mydata 
mydata
```
연결
```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker run -d --name test1 -v mydata:/data nginx 
1f1cf8ee9c066dff404401d0dc922af6bacaddbfeaf2ff8c685c495037893678
```
볼륨 내 데이터 생성
```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker exec test1 sh -c "echo 영속성 테스트 > /data/test.txt"
```

#### 컨테이너 삭제 전 데이터 확인 기록 (데이터 값 또는 파일 내용 원문 포함)

볼륨 내 데이터 확인
```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker exec test1 cat /data/test.txt
영속성 테스트
```

#### 컨테이너 삭제 명령과 출력 기록

```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker rm -f test1
test1
```

#### 컨테이너 삭제 직후 볼륨 목록에 해당 볼륨이 남아 있는지 확인 기록

```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker volume ls
DRIVER    VOLUME NAME
local     mydata
```

#### 삭제한 컨테이너와 같은 볼륨을 연결한 새 컨테이너 실행

```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker run -d --name test2 -v mydata:/data nginx
93e96c8ba0dd0a2bd75726bbdf7a741924e3a5f3c57b31e16c3bf37154ab8bcf
```

#### 새 컨테이너에서 삭제 전과 동일한 데이터 확인 기록 (삭제 전 기록과 대조)

```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker exec test2 cat /data/test.txt
영속성 테스트
```

#### 볼륨을 연결하지 않은 대조용 컨테이너에서 같은 경로를 확인하여 데이터가 없음을 기록

```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker run -d --name test3 nginx
b6051d28443c31acb02af77dc1909f28c6de46602d339f388c95349288a48893

PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker exec test3 cat /data/test.txt
cat: /data/test.txt: No such file or directory
```

## 11. 트러블 슈팅

### 11-1. 문제1

#### 11-1-1. 문제 및 원인 가설

```powershell
# Docker 커스텀 이미지 빌드 시도
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\evidences> docker build -f ./Dockerfile -t exam .
[+] Building 2.8s (6/6) FINISHED                            docker:desktop-linux
 => [internal] load build definition from Dockerfile                        0.0s
 => => transferring dockerfile: 108B                                        0.0s
 => [internal] load metadata for docker.io/library/nginx:alpine             2.5s
 => [internal] load .dockerignore                                           0.1s
 => => transferring context: 2B                                             0.0s
 => [internal] load build context                                           0.1s
 => => transferring context: 2B                                             0.0s
 => [1/2] FROM docker.io/library/nginx:alpine@sha256:785835ea65db4bba6f021  0.1s
 => => resolve docker.io/library/nginx:alpine@sha256:785835ea65db4bba6f021  0.1s
 => ERROR [2/2] COPY src/index.html /usr/share/nginx/html/index.html        0.0s
------
 > [2/2] COPY src/index.html /usr/share/nginx/html/index.html:
------
Dockerfile:2
--------------------
   1 |     FROM nginx:alpine
   2 | >>> COPY src/index.html /usr/share/nginx/html/index.html
--------------------
# 실패 원인 : not found
ERROR: failed to build: failed to solve: failed to compute cache key: failed to calculate checksum of ref t8rlv3xuwy8z383fhde6y0ebk::hwpet34bujgaz43b9i89s8fdd: "/src/index.html": not found
```

#### 11-1-3. 확인

```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\evidences> ls


    디렉터리: C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\evidenc
    es


Mode                 LastWriteTime         Length Name                          
----                 -------------         ------ ----                          
d-----      2026-11-03   오후 7:17                local-only                    
-a----      2026-11-04   오후 5:36          24409 command-log.md                
-a----      2026-11-04   오후 4:58             71 Dockerfile                    
-a----      2026-11-02   오후 8:53          72565 vscode-github-login.png       
-a----      2026-11-02   오후 8:59          74789 vscode-repo-linked.png        


PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\evidences> ls ../


    디렉터리: C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1


Mode                 LastWriteTime         Length Name                          
----                 -------------         ------ ----                          
d-----      2026-11-04   오후 4:58                evidences                     
d-----      2026-11-02   오후 7:30                generated                     
d-----      2026-11-03   오후 1:48                guide                         
d-----      2026-11-04   오후 4:33                nginx                         
d-----      2026-11-04   오후 4:58                src                           
-a----      2026-11-04   오후 5:33          17568 README.md                     


PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\evidences> ls ../src


    디렉터리: C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\src


Mode                 LastWriteTime         Length Name                          
----                 -------------         ------ ----                          
-a----      2026-11-04   오후 4:24            302 index.html                    
```

#### 11-1-4. 해결

```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\evidences> docker build -f ./Dockerfile -t exam ../
[+] Building 2.7s (7/7) FINISHED                            docker:desktop-linux
 => [internal] load build definition from Dockerfile                        0.1s
 => => transferring dockerfile: 108B                                        0.0s
 => [internal] load metadata for docker.io/library/nginx:alpine             1.0s
 => [internal] load .dockerignore                                           0.1s
 => => transferring context: 2B                                             0.0s
 => [internal] load build context                                           0.1s
 => => transferring context: 372B                                           0.0s
 => [1/2] FROM docker.io/library/nginx:alpine@sha256:785835ea65db4bba6f021  0.1s
 => => resolve docker.io/library/nginx:alpine@sha256:785835ea65db4bba6f021  0.0s
 => CACHED [2/2] COPY src/index.html /usr/share/nginx/html/index.html       0.0s
 => exporting to image                                                      1.2s
 => => exporting layers                                                     0.0s
 => => exporting manifest sha256:ada5cdd415b90c8429adb206c8a9d346ea0317102  0.0s
 => => exporting config sha256:49f0f4dc0b23a7d586681464e795d180a3818b7b26d  0.0s
 => => exporting attestation manifest sha256:c503844f07c4599dfa1c2919982fb  0.0s
 => => exporting manifest list sha256:3c5a22df25011ba104ebd497fc7560753989  0.0s
 => => naming to docker.io/library/exam:latest                              0.0s
 => => unpacking to docker.io/library/exam:latest                           1.0s
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\evidences> docker images
                                                            i Info →   U  In Use
IMAGE                ID             DISK USAGE   CONTENT SIZE   EXTRA
exam:latest          3c5a22df2501       93.6MB         26.3MB        
hello-world:latest   c567b231f656       25.9kB         9.49kB        
my-web:latest        de28cc6696af        241MB         63.9MB        
ubuntu:latest        6a06111c3b0a        163MB         45.9MB    U   
```

### 11-2. 문제2

#### 11-2-3. 확인

```bash
$ git config user.name songdajeon
fatal: not in a git directory

$ pwd
/c/Users/<USER>
```

#### 11-2-4. 해결

```bash
$ cd ./<FOLDER>/<PROJECT>/E1_1

<USER>@<HOST> UCRT64 ~/<FOLDER>/<PROJECT>/E1_1 (main)
$ git config user.name songdajeon

$ git config user.email <EMAIL>

$ git config init.defaultBranch main

```
(초반 글로벌 설정 후 원격 연결 이후, 로컬 설정 새로 한 후의 리스트)
```bash
$ git config --list
diff.astextplain.textconv=astextplain
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
http.sslbackend=schannel
core.autocrlf=true
core.fscache=true
core.symlinks=false
pull.rebase=false
credential.helper=manager
credential.https://dev.azure.com.usehttppath=true
init.defaultbranch=master
user.name=songdajeon
user.email=<EMAIL>
init.defaultbranch=main
core.repositoryformatversion=0
core.filemode=false
core.bare=false
core.logallrefupdates=true
core.symlinks=false
core.ignorecase=true
remote.origin.url=https://github.com/InGentleWave/Codyssey_E1_1_Dev_Set-up_practice.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.main.remote=origin
branch.main.merge=refs/heads/main
```

## 12. 보너스 과제 (선택)

### Docker Compose 기초

#### Compose 실행 결과를 단일 컨테이너 실행과 비교해 기록

```powershell
# docker compose로 빌드 및 실행
# 사용 명령어 docker compose up -d --build
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\compose> docker compose up -d --build
[+] Building 2.8s (9/9) FINISHED                                                                                
 => [internal] load local bake definitions                                                                 0.0s
 => => reading from stdin 568B                                                                             0.0s
 => [internal] load build definition from Dockerfile                                                       0.0s
 => => transferring dockerfile: 223B                                                                       0.0s
 => [internal] load metadata for docker.io/library/nginx:stable-alpine                                     1.6s
 => [internal] load .dockerignore                                                                          0.0s
 => => transferring context: 2B                                                                            0.0s
 => [internal] load build context                                                                          0.1s
 => => transferring context: 384B                                                                          0.1s
 => CACHED [1/2] FROM docker.io/library/nginx:stable-alpine@sha256:0e52bd054126cdc040b1276c0af347aeb02a41  0.1s
 => => resolve docker.io/library/nginx:stable-alpine@sha256:0e52bd054126cdc040b1276c0af347aeb02a41b9cfe30  0.0s
 => [2/2] COPY src/index.html /usr/share/nginx/html/index.html                                             0.1s
 => exporting to image                                                                                     0.4s
 => => exporting layers                                                                                    0.2s
 => => exporting manifest sha256:c9bf45011aa2fe594a641b46afe5a2b7a72ecd46b8ef5e3b850651122d83e7a6          0.0s
 => => exporting config sha256:edb60c550f231e835702d3f7f6da6b77ccd3638705e958b11e479621b0483b8b            0.0s
 => => exporting attestation manifest sha256:422e3eaa9e87d984382823bb502cded23e419a423047be213b80211a478d  0.0s
 => => exporting manifest list sha256:759a4fdc5313519d34b07286468e9b11d5e70401ab5b93e5c016c87acaf6485e     0.0s
 => => naming to docker.io/library/my-web:1.0                                                              0.0s
 => => unpacking to docker.io/library/my-web:1.0                                                           0.1s
 => resolving provenance for metadata file                                                                 0.0s
[+] up 3/3
 ✔ Image my-web:1.0        Built                                                                            3.0s
 ✔ Network compose_default Created                                                                          0.1s
 ✔ Container compose-web-1 Started                                                                          0.6s
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\compose> docker compose ps
NAME            IMAGE        COMMAND                   SERVICE   CREATED         STATUS         PORTS
compose-web-1   my-web:1.0   "/docker-entrypoint.…"   web       7 seconds ago   Up 7 seconds   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp

# 단일 컨테이너 빌드 및 실행
# 사용 명령어 :docker build -t <이미지명> <빌드컨텍스트>,docker run -d -p 8081:80 --name <컨테이너명> <이미지명>
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\compose> docker build -t single-build ../
[+] Building 1.3s (7/7) FINISHED                                                                                  docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                              0.0s
 => => transferring dockerfile: 223B                                                                                              0.0s
 => [internal] load metadata for docker.io/library/nginx:stable-alpine                                                            0.8s
 => [internal] load .dockerignore                                                                                                 0.0s
 => => transferring context: 2B                                                                                                   0.0s
 => [internal] load build context                                                                                                 0.0s
 => => transferring context: 59B                                                                                                  0.0s
 => [1/2] FROM docker.io/library/nginx:stable-alpine@sha256:0e52bd054126cdc040b1276c0af347aeb02a41b9cfe305d6094767ac30e97949      0.1s
 => => resolve docker.io/library/nginx:stable-alpine@sha256:0e52bd054126cdc040b1276c0af347aeb02a41b9cfe305d6094767ac30e97949      0.0s
 => CACHED [2/2] COPY src/index.html /usr/share/nginx/html/index.html                                                             0.0s
 => exporting to image                                                                                                            0.2s
 => => exporting layers                                                                                                           0.0s
 => => exporting manifest sha256:1a862ffad037598012fe6ea62d7a4673340b970466b08620b46ce0c1e6192f75                                 0.0s
 => => exporting config sha256:29873a6905aef2586fb4641523132c40831c44db6dafc4996f977516cc74a388                                   0.0s
 => => exporting attestation manifest sha256:8543db95fba99d392a06ec63979ab50a2a6bc9774ed8a526418dd72d17017459                     0.0s
 => => exporting manifest list sha256:4949af2e52bbc86104f22cd91e015fc79610412aaab5d027fb3f45d4ec8cc830                            0.0s
 => => naming to docker.io/library/single-build:latest                                                                            0.0s
 => => unpacking to docker.io/library/single-build:latest                                                                         0.0s
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\compose> docker images
                                                                                                                  i Info →   U  In Use
IMAGE                 ID             DISK USAGE   CONTENT SIZE   EXTRA
exam2:latest          63c27b4f2cef        177MB         43.3MB    U   
exam:latest           792e89032071       92.7MB         26.1MB    U   
hello-world:latest    c567b231f656       25.9kB         9.49kB        
my-web:1.0            759a4fdc5313       92.7MB         26.1MB    U   
my-web:latest         de28cc6696af        241MB         63.9MB        
nginx:latest          5ab5b0b01097        243MB         66.8MB    U   
single-build:latest   4949af2e52bb       92.7MB         26.1MB        
ubuntu:latest         6a06111c3b0a        163MB         45.9MB        

PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\compose> docker run -d -p 8081:80 --name single-build-web single-build
a688c7f29e2cba8b3fdc490d242a900d639fc85b323f5f3a2315e7701b63ef34

PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\compose> docker ps
CONTAINER ID   IMAGE          COMMAND                   CREATED         STATUS         PORTS                                     NAMES
a688c7f29e2c   single-build   "/docker-entrypoint.…"   4 seconds ago   Up 3 seconds   0.0.0.0:8081->80/tcp, [::]:8081->80/tcp   single-build-web
ed5a488ad17e   my-web:1.0     "/docker-entrypoint.…"   7 minutes ago   Up 7 minutes   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   compose-web-1
```

### Docker Compose 멀티 컨테이너

#### 웹 서버와 보조 서비스 1개 이상을 함께 실행

```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\multi-compose> docker compose up -d --build
[+] Building 1.3s (9/9) FINISHED                                                                                                       
 => [internal] load local bake definitions                                                                                        0.0s
 => => reading from stdin 574B                                                                                                    0.0s
 => [internal] load build definition from Dockerfile                                                                              0.0s
 => => transferring dockerfile: 223B                                                                                              0.0s
 => [internal] load metadata for docker.io/library/nginx:stable-alpine                                                            0.4s
 => [internal] load .dockerignore                                                                                                 0.0s
 => => transferring context: 2B                                                                                                   0.0s
 => [internal] load build context                                                                                                 0.0s
 => => transferring context: 59B                                                                                                  0.0s
 => [1/2] FROM docker.io/library/nginx:stable-alpine@sha256:0e52bd054126cdc040b1276c0af347aeb02a41b9cfe305d6094767ac30e97949      0.1s
 => => resolve docker.io/library/nginx:stable-alpine@sha256:0e52bd054126cdc040b1276c0af347aeb02a41b9cfe305d6094767ac30e97949      0.1s
 => CACHED [2/2] COPY src/index.html /usr/share/nginx/html/index.html                                                             0.0s
 => exporting to image                                                                                                            0.3s
 => => exporting layers                                                                                                           0.0s
 => => exporting manifest sha256:15a5753609cc05ba4fe16effb102ce48d59376bf9c3b48c3970a4bfd729c254b                                 0.0s
 => => exporting config sha256:6ce490f2b2663cab0fd2405de299ef3c69ea24f8062e0ee15ac8c53acb1549ff                                   0.0s
 => => exporting attestation manifest sha256:dfd5385878c20c43dc5257dc2bc9418b16bb48cdee8910348d4d302fbc6b7604                     0.0s
 => => exporting manifest list sha256:6ef7e23123954405437414a6be4f19fa5ce3adab09f9b9752826b2f368acea38                            0.0s
 => => naming to docker.io/library/my-web:1.0                                                                                     0.0s
 => => unpacking to docker.io/library/my-web:1.0                                                                                  0.0s
 => resolving provenance for metadata file                                                                                        0.0s
[+] up 4/4
 ✔ Image my-web:1.0                Built                                                                                           1.5s
 ✔ Network multi-compose_default   Created                                                                                         0.1s
 ✔ Container multi-compose-cache-1 Started                                                                                         1.1s
 ✔ Container multi-compose-web-1   Started                                                                                         0.8s
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\multi-compose> docker compose ps
NAME                    IMAGE            COMMAND                   SERVICE   CREATED         STATUS         PORTS
multi-compose-cache-1   redis:7-alpine   "docker-entrypoint.s…"   cache     8 seconds ago   Up 6 seconds   6379/tcp
multi-compose-web-1     my-web:1.0       "/docker-entrypoint.…"   web       8 seconds ago   Up 6 seconds   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp
```

#### 컨테이너 간 네트워크 통신 확인
- getent hosts: 호스트 이름을 IP 주소로 변환합니다. 출력에 cache의 IP 주소가 나오면 서비스 디스커버리가 동작한 것입니다.

```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\multi-compose> docker compose exec web getent hosts cache
172.18.0.2        cache  cache
```

- 먼저 web 컨테이너에 어떤 도구가 있는지 확인

```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\multi-compose> docker compose exec web sh -c "which curl nc wget"
/usr/bin/curl
/usr/bin/nc
/usr/bin/wget
```

- web 컨테이너에서 cache 컨테이너의 포트가 확인 가능한지 체크합니다.
  - nc: 네트워크 연결을 확인하는 도구입니다.
  - -z: 데이터를 보내지 않고 포트 열림 여부만 확인합니다.
  - -v: 결과를 자세히 출력합니다. open 또는 succeeded 문구가 나오면 연결 성공입니다.
```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\multi-compose> docker compose exec web nc -zv cache 6379
cache (172.18.0.2:6379) open
```

- Redis 자체의 응답은 cache 컨테이너에서 확인합니다. Redis 이미지에는 redis-cli가 포함되어 있습니다.
  - redis-cli ping: Redis 서버에 연결해 응답을 요청합니다. PONG이 출력되면 서버가 정상 동작하는 것입니다.

```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\multi-compose> docker compose exec cache redis-cli ping
PONG
```

- 호스트에서 웹 서버 접속 확인
  - PowerShell의 curl은 별칭이므로 curl.exe로 실행합니다.
  - 웹 페이지가 출력되면 호스트 쪽 매핑도 정상입니다.

```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\multi-compose> curl.exe http://localhost:8080
<!-- index.html -->
<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>My First Container</title></head>
<body>
  <h1>안녕하세요, 바인드 마운트 호스트 변경 후 페이지입니다.</h1>
  <p>이 페이지는 Docker 컨테이너 안에서 실행되고 있습니다.</p>
</body>
</html>
```

### Compose 운영 명령어 습득

#### up, down, ps, logs를 각각 실행하고 출력 기록
docker compose up -d로 실행
```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\multi-compose> docker compose up -d
[+] up 3/3
 ✔ Network multi-compose_default   Created                                                                                          0.0s
 ✔ Container multi-compose-cache-1 Started                                                                                          0.4s
 ✔ Container multi-compose-web-1   Started                                                                                          0.5s
```

docker compose ps로 상태 확인
```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\multi-compose> docker compose ps
NAME                    IMAGE            COMMAND                   SERVICE   CREATED         STATUS         PORTS
multi-compose-cache-1   redis:7-alpine   "docker-entrypoint.s…"   cache     4 seconds ago   Up 3 seconds   6379/tcp
multi-compose-web-1     my-web:1.0       "/docker-entrypoint.…"   web       4 seconds ago   Up 3 seconds   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp
```

docker compose logs로 로그 확인
```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\multi-compose> docker compose logs
cache-1  | 1:C 05 Nov 2026 11:26:48.734 * oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
cache-1  | 1:C 05 Nov 2026 11:26:48.734 * Redis version=7.4.12, bits=64, commit=00000000, modified=0, pid=1, just started
web-1    | /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
web-1    | /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
web-1    | /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
web-1    | 10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
web-1    | 10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
web-1    | /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
web-1    | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
web-1    | /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
web-1    | /docker-entrypoint.sh: Configuration complete; ready for start up
web-1    | 2026/11/05 11:26:48 [notice] 1#1: using the "epoll" event method
web-1    | 2026/11/05 11:26:48 [notice] 1#1: nginx/1.30.6
web-1    | 2026/11/05 11:26:48 [notice] 1#1: built by gcc 15.2.0 (Alpine 15.2.0) 
web-1    | 2026/11/05 11:26:48 [notice] 1#1: OS: Linux 6.18.54.1-microsoft-standard-WSL2
web-1    | 2026/11/05 11:26:48 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
web-1    | 2026/11/05 11:26:48 [notice] 1#1: start worker processes
web-1    | 2026/11/05 11:26:48 [notice] 1#1: start worker process 30
web-1    | 2026/11/05 11:26:48 [notice] 1#1: start worker process 31
web-1    | 2026/11/05 11:26:48 [notice] 1#1: start worker process 32
web-1    | 2026/11/05 11:26:48 [notice] 1#1: start worker process 33
web-1    | 2026/11/05 11:26:48 [notice] 1#1: start worker process 34
cache-1  | 1:C 05 Nov 2026 11:26:48.734 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
cache-1  | 1:M 05 Nov 2026 11:26:48.734 * monotonic clock: POSIX clock_gettime
cache-1  | 1:M 05 Nov 2026 11:26:48.736 * Running mode=standalone, port=6379.
cache-1  | 1:M 05 Nov 2026 11:26:48.738 * Server initialized
cache-1  | 1:M 05 Nov 2026 11:26:48.738 * Ready to accept connections tcp
web-1    | 2026/11/05 11:26:48 [notice] 1#1: start worker process 35
web-1    | 2026/11/05 11:26:48 [notice] 1#1: start worker process 36
web-1    | 2026/11/05 11:26:48 [notice] 1#1: start worker process 37
web-1    | 2026/11/05 11:26:48 [notice] 1#1: start worker process 38
web-1    | 2026/11/05 11:26:48 [notice] 1#1: start worker process 39
web-1    | 2026/11/05 11:26:48 [notice] 1#1: start worker process 40
web-1    | 2026/11/05 11:26:48 [notice] 1#1: start worker process 41
```

docker compose down로 종료
```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\multi-compose> docker compose down
[+] down 3/3
 ✔ Container multi-compose-web-1   Removed                                                                                          0.5s
 ✔ Container multi-compose-cache-1 Removed                                                                                          0.3s
 ✔ Network multi-compose_default   Removed                                                                                          0.2s
```

docker compose ps로 상태 확인
```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\multi-compose> docker compose ps
NAME      IMAGE     COMMAND   SERVICE   CREATED   STATUS    PORTS
```

### 환경 변수 활용

#### 값을 바꿔 실행하고 변경 전후 동작 차이 기록
변경 전 실행
```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\env-var> docker compose up -d
[+] up 2/2
 ✔ Container env-var-cache-1 Running                                                                                                0.0s
 ✔ Container env-var-web-1   Started                                                                                                0.7s
```
변경 전 정보
```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\env-var> docker compose config
name: env-var
services:
  cache:
    image: redis:7-alpine
    networks:
      default: null
  web:
    environment:
      APP_MODE: production
    image: my-web:1.0
    networks:
      default: null
    build:
      context: C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1
      dockerfile: Dockerfile
    depends_on:
      cache:
        condition: service_started
        required: true
    ports:
      - mode: ingress
        target: 80
        published: "8080"
        protocol: tcp
networks:
  default:
    name: env-var_default
```
환경 변수 변경 및 재실행
```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\env-var> $env:HOST_PORT = "8081"
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\env-var> docker compose up -d   
[+] up 2/2
 ✔ Container env-var-cache-1 Running                                                                                                0.0s
 ✔ Container env-var-web-1   Started
```
변경 후 정보
```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1\env-var> docker compose config  
name: env-var
services:
  cache:
    image: redis:7-alpine
    networks:
      default: null
  web:
    environment:
      APP_MODE: production
    image: my-web:1.0
    networks:
      default: null
    build:
      context: C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1
      dockerfile: Dockerfile
    depends_on:
      cache:
        condition: service_started
        required: true
    ports:
      - mode: ingress
        target: 80
        published: "8081"
        protocol: tcp
networks:
  default:
    name: env-var_default
```

### GitHub SSH 키 설정

#### Windows에서 SSH 키를 생성

```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> ssh-keygen -t ed25519 -C "<EMAIL>"
Generating public/private ed25519 key pair.
Enter file in which to save the key (C:\Users\<USER>/.ssh/id_ed25519): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in C:\Users\<USER>/.ssh/id_ed25519
Your public key has been saved in C:\Users\<USER>/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:<SHA256> <EMAIL>
The key's randomart image is:
+--[ED25519 256]--+
|<RANDOMART IMAGE>|
+----[SHA256]-----+

PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> cat ~/.ssh/id_ed25519.pub
ssh-ed25519 <SSH-ED25519>
```

#### 원격 주소를 SSH로 바꾸고 푸시 성공 결과 기록

```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> git remote -v
origin  https://github.com/InGentleWave/Codyssey_E1_1_Dev_Set-up_practice.git (fetch)
origin  https://github.com/InGentleWave/Codyssey_E1_1_Dev_Set-up_practice.git (push)

PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> git remote set-url origin git@github.com:InGentleWave/Codyssey_E1_1_Dev_Set-up_practice.git
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> git remote -v
origin  git@github.com:InGentleWave/Codyssey_E1_1_Dev_Set-up_practice.git (fetch)
origin  git@github.com:InGentleWave/Codyssey_E1_1_Dev_Set-up_practice.git (push)

PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> ssh -T git@github.com
The authenticity of host 'github.com (20.200.245.247)' can't be established.
ED25519 key fingerprint is SHA256:<SHA256>.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'github.com' (ED25519) to the list of known hosts.
Hi InGentleWave! You've successfully authenticated, but GitHub does not provide shell access.
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   evidences/command-log.md

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> git add .\evidences\command-log.md
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> git commit -m "SSH Push Test"
[main 72b0d60] SSH Push Test
 1 file changed, 5 insertions(+)
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> git push origin main
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 12 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 396 bytes | 396.00 KiB/s, done.
Total 4 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
To github.com:InGentleWave/Codyssey_E1_1_Dev_Set-up_practice.git
   8a96344..72b0d60  main -> main
```

