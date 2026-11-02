# 명령어 로그

이 문서는 README.md에서 링크로 연결합니다. 각 항목은 명령 입력과 출력 결과를 함께 기록합니다. 캡처 파일은 `images/` 폴더에 두고 해당 항목에서 링크합니다.

- 형식: 명령 입력은 `$` 뒤에 적고, 출력은 그 아래에 그대로 붙여 넣습니다.
- 민감정보: 사용자 이름, 이메일, 토큰, 비밀번호, 인증 코드는 마스킹합니다.
- 브라우저 캡처: 주소창(포트 포함)과 응답 화면이 함께 보여야 합니다.

---

## 1. 터미널 조작 로그

### 1-1. 현재 위치 확인

```text
$ (명령 입력)
(출력 결과)
```

### 1-2. 숨김 파일 포함 목록 확인

```text
$ (명령 입력)
(출력 결과)
```

### 1-3. 절대 경로 이동 / 상대 경로 이동

```text
$ (명령 입력)
(출력 결과)
```

### 1-4. 디렉터리 생성

```text
$ (명령 입력)
(출력 결과)
```

### 1-5. 빈 파일 생성 및 내용 확인

```text
$ (명령 입력)
(출력 결과)
```

### 1-6. 파일 복사, 이동 또는 이름 변경

```text
$ (명령 입력)
(출력 결과)
```

### 1-7. 파일 삭제 (삭제 전후 목록)

```text
$ (명령 입력)
(출력 결과, 삭제 전)
$ (명령 입력)
(출력 결과, 삭제 후)
```

---

## 2. 권한 실습 로그

### 2-1. 파일 권한 변경 전후

```text
$ (명령 입력)
(변경 전 출력)
$ (명령 입력)
(변경 후 출력)
```

### 2-2. 디렉터리 권한 변경 전후

```text
$ (명령 입력)
(변경 전 출력)
$ (명령 입력)
(변경 후 출력)
```

---

## 3. Docker 설치 및 점검 로그

```text
$ docker --version
(출력 결과)
$ docker info
(출력 결과)
```

---

## 4. Docker 기본 운영 명령 로그

```text
$ (hello-world 실행 명령)
(출력 결과)
$ docker images
(출력 결과)
$ docker ps
(출력 결과)
$ docker ps -a
(출력 결과)
$ docker logs (컨테이너 이름 또는 ID)
(출력 결과)
$ docker stats --no-stream
(출력 결과)
```

---

## 5. 컨테이너 실행 실습 로그

### 5-1. ubuntu 컨테이너 대화형 실행

```text
$ (명령 입력)
(내부 명령 ls, echo 출력)
$ (exit 후 docker ps -a 출력)
(출력 결과)
```

### 5-2. 백그라운드 실행 후 exec 실행

```text
$ (명령 입력)
(출력 결과)
$ (exec 명령 입력)
(출력 결과)
```

---

## 6. 커스텀 이미지 빌드 및 실행 로그

```text
$ (docker build 명령)
(마지막 출력 결과 전체)
$ docker images
(출력 결과)
$ (docker run 명령)
(출력 결과)
```

---

## 7. 포트 매핑 접속 로그

### 7-1. 1회차 (호스트 포트 8080)

```text
$ (docker run 명령)
(출력 결과)
```

- 캡처: (링크: images/port-8080.png)

### 7-2. 2회차 (호스트 포트 8081)

```text
$ (docker run 명령)
(출력 결과)
```

- 캡처: (링크: images/port-8081.png)

---

## 8. 바인드 마운트 반영 로그

```text
$ (docker run -v 명령)
(출력 결과)
(호스트 파일 수정 명령과 수정 전 내용)
(수정 후 내용)
```

- 캡처 전: (링크: images/mount-before.png)
- 캡처 후: (링크: images/mount-after.png)

---

## 9. Docker 볼륨 영속성 로그

```text
$ docker volume create mydata
(출력 결과)
$ docker volume ls
(출력 결과)
$ (볼륨 연결 실행 명령)
(출력 결과)
$ (컨테이너 내부 데이터 생성 명령과 확인 출력)
(출력 결과)
$ docker rm -f (컨테이너 이름)
(출력 결과)
$ (새 컨테이너 실행 명령)
(출력 결과)
$ (새 컨테이너에서 데이터 확인 명령)
(출력 결과)
```

---

## 10. Git 설정 로그

```text
$ git --version
git version 2.53.0
$ git config --global user.name songdajeon
$ git config --global user.email "<노리퍼 이메일 주소>"
$ git config --global init.defaultBranch main
$ git config --list
user.name=songdajeon
user.email=<노리퍼 이메일 주소>
init.defaultbranch=main
```

---

## 11. GitHub 및 VSCode 연동 증거

- GitHub 로그인 완료 캡처 (계정 정보 가림): (링크: images/github-login.png)
- 저장소 연동 완료 캡처: (링크: images/vscode-github-link.png)
- 첫 푸시 명령과 출력:

```text
$ (git push 명령)
(출력 결과)
```

---

## 12. 보너스 과제 로그 (선택)

### 12-1. Docker Compose 실행

```text
$ docker compose version
(출력 결과)
$ docker compose up -d
(출력 결과)
$ docker compose ps
(출력 결과)
$ docker compose logs
(출력 결과)
$ docker compose down
(출력 결과)
```

### 12-2. 멀티 컨테이너 통신 확인

```text
$ (통신 확인 명령)
(출력 결과)
```

### 12-3. 환경 변수 변경 전후

```text
$ (변경 전 확인 출력)
$ (변경 후 확인 출력)
```

### 12-4. SSH 키 연결 확인

```text
$ ssh -T git@github.com
(출력 결과, 사용자 이름 마스킹)
$ git push origin main
(출력 결과)
```
