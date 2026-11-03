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

```bash
# 파일 복사 (cp)
root@cdcdc0e4bd3c:/# cp -r /ant/spider /ant/dog
root@cdcdc0e4bd3c:/# cd /ant
root@cdcdc0e4bd3c:/ant# ls
dog  spider
# 파일 이동 (mv)
root@cdcdc0e4bd3c:/ant# ls
dog  spider
root@cdcdc0e4bd3c:/ant# mv ./spider ./dog/
root@cdcdc0e4bd3c:/ant# ls
dog
root@cdcdc0e4bd3c:/ant# ls ./dog
spider
# 이름 변경 (mv)
root@cdcdc0e4bd3c:/ant# ls ./dog
spider
root@cdcdc0e4bd3c:/ant# mv ./dog/spider ./ladybug
root@cdcdc0e4bd3c:/ant# ls
dog  ladybug
```

### 파일 삭제 (rm)(삭제 전후 목록 기록)

```bash
# 삭제 전
root@cdcdc0e4bd3c:/ant# ls /ant /ant/dog
/ant:
dog  ladybug

/ant/dog:
cat
# 삭제 후
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

```powershell
# 로그 확인 (docker logs)
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

# 리소스 확인 (docker stats)
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker stats mybox
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
cdcdc0e4bd3c   mybox     0.00%     0B / 0B             0.00%     0B / 0B   0B / 0B     0
```

#### 컨테이너 실행, 중지, 재시작, 삭제 각 단계의 상태 변화 기록

```powershell
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker ps -a
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS                       PORTS     NAMES
cdcdc0e4bd3c   ubuntu    "/bin/bash"   53 minutes ago   Exited (137) 3 seconds ago             mybox
# 컨테이너 실행
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker start mybox
mybox
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker ps -a      
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS         PORTS     NAMES
cdcdc0e4bd3c   ubuntu    "/bin/bash"   54 minutes ago   Up 3 seconds             mybox
# 컨테이너 중지
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker stop mybox
mybox
PS C:\Users\<USER>\<FOLDER>\<PROJECT>\E1_1> docker ps -a     
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS                       PORTS     NAMES
cdcdc0e4bd3c   ubuntu    "/bin/bash"   54 minutes ago   Exited (137) 4 seconds ago             mybox
# 컨테이너 재시작
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
# 컨테이너 삭제
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

```console
# docker attach 컨테이너ID : 컨테이너의 메인 프로세스에 표준 입출력을 연결함. exit 입력 시 메인 프로세스 즉 컨테이너가 종료됨
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

# docker exec 컨테이너ID 명령어: 컨테이너에 메인 프로세스와 무관한 새 프로세스를 실행하여 명령어에 대한 출력값을 받고 프로세스를 종료함. -it(대화형) 옵션을 사용하여 bash등과 같은 대화형 쉘을 사용할 수 있음. 이 때 exit를 입력하면 쉘이 종료되고 메인 프로세스는 계속 실행이 유지됨.
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

# docker exec -it 컨테이너ID 쉘 예시
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

### 웹 서버 소스코드 (src/)
### Dockerfile(직접 작성, 전체 코드를 8번 섹션에 포함)
### 방식 선택: (A) nginx 베이스 이미지 활용
### 베이스 선택 이유 기록
### 커스텀 포인트별 목적 기록
### 커스텀 이미지 빌드 성공 증거

#### docker build 실행 명령 및 결과 로그
#### 빌드된 이미지 목록 확인

### 컨테이너 실행 성공 증거

#### docker run으로 컨테이너 실행 및 상태 확인

### 포트 매핑 접속 성공 증거(브라우저 스크린샷)

## 8. 포트 매핑 접속 증거

### p <host_port>:<container_port>로 실행 후, 브라우저 접속 화면(주소창 포함)

#### 1회차 포트 매핑 실행 명령 기록, 브라우저 접속 캡처 (주소창에 포트 포함)
#### 2회차 다른 호스트 포트로 실행 (컨테이너 이름은 다르게), 브라우저 접속 캡처

## 9. 바인드 마운트 반영 + 볼륨 영속성 증거

### 9-1. 바인드 마운트 반영

#### 호스트 디렉터리를 컨테이너에 연결하는 실행 명령 기록
#### 호스트 파일 변경 전/후 내용 비교
#### 변경이 컨테이너에 반영되었음을 확인

### 9-2. Docker 볼륨 영속성 검증

#### 삭제 전 데이터 준비

##### 볼륨 생성 명령과 출력 기록, 볼륨 목록 확인
##### 볼륨을 컨테이너 연결 명령 및 출력 기록
##### 볼륨을 연결한 컨테이너 실행, 내부에서 데이터 생성 기록
##### 컨테이너 상세 정보에서 볼륨 마운트 항목(볼륨 이름, 컨테이너 내부 경로)이 표시되는 출력 기록
##### 삭제 대상 컨테이너의 ID와 이름 기록
##### 컨테이너 삭제 전 데이터 확인 기록 (데이터 값 또는 파일 내용 원문 포함)

#### 컨테이너 삭제 명령과 출력 기록

#### 삭제 후 데이터 준비

##### 컨테이너 삭제 직후 볼륨 목록에 해당 볼륨이 남아 있는지 확인 기록
##### 컨테이너 삭제 후 같은 볼륨을 연결한 새 컨테이너 실행

#### 삭제 전/후 데이터 유지 검증

##### 새 컨테이너의 ID가 삭제된 컨테이너의 ID와 다름을 기록
##### 새 컨테이너에서 삭제 전과 동일한 데이터 확인 기록 (삭제 전 기록과 대조)
##### 볼륨을 연결하지 않은 대조용 컨테이너에서 같은 경로를 확인하여 데이터가 없음을 기록

#### 검증 종료 후 테스트 볼륨 정리 명령과 출력 기록

## 10. Git 설정 및 GitHub 연동

### 사용자 이름, 사용자 이메일(마스킹), 기본 브랜치 설정 후 git config --list 출력 기록 (민감값 마스킹)
### VSCode에서 GitHub 로그인 연동 완료 캡처 (계정 정보 가림)
### git bash 로컬 저장소와 원격 저장소 연결 기록
### 연동 완료 캡처 (토큰, 인증 코드 포함 주의)

## 11. 보안 및 개인정보

- 이 문서, 로그, 스크린샷에는 토큰, 비밀번호, 개인키, 인증 코드, 개인 이메일 주소를 포함하지 않습니다.
- 마스킹 형식: (기록, 예: ****-****)
- 민감정보가 노출된 경우의 처리 내역: (기록, 없으면 "해당 없음")

### README.md, command-log.md, 캡처에서 토큰, 비밀번호, 개인키, 인증 코드, 개인 이메일 검색
### 발견된 항목 마스킹 또는 제거
### 노출된 적이 있다면 제거 및 재발급 내역을 15번 섹션에 기록

## 13. 보너스 과제 (선택)

### Docker Compose 기초

#### 단일 서비스용 docker-compose.yml을 작성
#### Compose 실행 결과를 단일 컨테이너 실행과 비교해 기록
#### 실행 설정을 파일로 문서화하는 이유 정리

### Docker Compose 멀티 컨테이너

#### 웹 서버와 보조 서비스 1개 이상을 함께 실행
#### 웹 컨테이너에서 서비스 이름으로 접속되는지 확인하고 출력 기록
#### 서비스 이름 기반 컨테이너 간 통신 정리

### Compose 운영 명령어 습득

#### up, down, ps, logs를 각각 실행하고 출력 기록
#### Compose 명령 형태(docker compose 또는 docker-compose)와 버전 확인 후 기록
#### ps, logs 중심의 상태 확인 루틴 정리

### 환경 변수 활용

#### 포트 또는 실행 모드를 환경 변수로 지정
#### 값을 바꿔 실행하고 변경 전후 동작 차이 기록
#### 코드와 설정 분리의 이점 정리

### GitHub SSH 키 설정

#### Windows에서 SSH 키를 생성하고 공개 키를 GitHub에 등록
#### 원격 주소를 SSH로 바꾸고 푸시 성공 결과 기록
#### HTTPS와 SSH 키 인증의 차이 정리