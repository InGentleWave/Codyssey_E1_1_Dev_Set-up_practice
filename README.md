# Codyssey E1-1 Dev Set-up Practice

## 목차

- [1. 프로젝트 개요](#1-프로젝트-개요)
- [2. 실행 환경](#2-실행-환경)
- [3. 수행 항목 체크리스트](#3-수행-항목-체크리스트)
- [4. 터미널 조작](#4-터미널-조작)
- [5. 권한 실습](#5-권한-실습)
- [6. Docker](#6-docker)
- [7. Dockerfile 기반 웹 서버 컨테이너](#7-dockerfile-기반-웹-서버-컨테이너)
- [8. 포트 매핑 접속 증거](#8-포트-매핑-접속-증거)
- [9. 바인드 마운트 반영 + 볼륨 영속성 증거](#9-바인드-마운트-반영--볼륨-영속성-증거)
- [10. Git 설정 및 GitHub 연동](#10-git-설정-및-github-연동)
- [11. 보안 및 개인정보](#11-보안-및-개인정보)
- [12. 트러블슈팅 기록](#12-트러블슈팅-기록)
- [13. 보너스 과제](#13-보너스-과제)
- [14. 재현성 안내](#14-재현성-안내)

## 1. 프로젝트 개요

- 목표: 터미널, Docker, Git/GitHub를 직접 세팅하고, 웹 서버를 Dockerfile로 컨테이너화하여 포트 매핑, 바인드 마운트, 볼륨으로 변경 반영과 데이터 영속성을 검증한다.
- 학습 목표
  - 절대 경로와 상대 경로의 차이를 설명한다.
  - 파일 권한(r/w/x)과 755, 644 표기를 해석한다.
  - 기존 Dockerfile을 기반으로 커스텀 이미지를 만든다.
  - 포트 매핑이 필요한 이유를 설명한다.
  - Docker 볼륨의 개념을 설명한다.
  - Git과 GitHub의 역할 차이를 설명한다.
- 보너스 과제(선택): (수행 여부 기록)

## 2. 실행 환경

| 항목 | 값 |
|---|---|
| OS | Windows 11(버전 25H2 OS 빌드 26200.9818) + WSL2 Ubuntu |
| 쉘 | 5.1.26100.9818 |
| 터미널 | VSCode 1.144.1 Terminal (powershell)|
| Docker 버전 | Docker version 29.9.2, build a82e528 |
| Git 버전 | git version 2.56.0.windows.4 |
| VSCode 버전 | 1.144.1 |

## 3. 수행 항목 체크리스트

- [x] [터미널 조작](#4-터미널-조작)
- [x] [권한 실습](#5-권한-실습)
- [x] [Docker](#6-docker)
- [x] [Dockerfile 기반 웹 서버 컨테이너](#7-dockerfile-기반-웹-서버-컨테이너)
- [x] [포트 매핑 접속 증거](#8-포트-매핑-접속-증거)
- [x] [바인드 마운트 반영 + 볼륨 영속성 증거](#9-바인드-마운트-반영--볼륨-영속성-증거)
- [x] [Git 설정 및 GitHub 연동](#10-git-설정-및-github-연동)
- [x] [트러블슈팅 기록](#11-트러블슈팅-기록)
- [x] [보너스 과제](#12-보너스-과제)

## 4. 터미널 조작

-  현재 위치 확인 (pwd) [증거](./evidences/command-log.md#현재-위치-확인-pwd)
-  숨김 파일 포함 목록 확인 (ls -la) [증거](./evidences/command-log.md#숨김-파일-포함-목록-확인-ls--la)
-  절대 경로 이동, 상대 경로 이동 수행 [증거](./evidences/command-log.md#절대-경로-이동-상대-경로-이동-수행)
-  디렉터리 생성 (mkdir -p) [증거](./evidences/command-log.md#디렉터리-생성-mkdir--p)
-  파일 복사 (cp), 파일 이동 또는 이름 변경 (mv) [증거](./evidences/command-log.md#파일-복사-cp-파일-이동-또는-이름-변경-mv)
-  파일 삭제 (rm)(삭제 전후 목록 기록) [증거](./evidences/command-log.md#파일-삭제-rm삭제-전후-목록-기록)
-  파일 내용 확인 (cat 또는 less) [증거](./evidences/command-log.md#파일-내용-확인-cat-또는-less)
-  빈 파일 생성 (touch) [증거](./evidences/command-log.md#빈-파일-생성-touch)

## 5. 권한 실습

-  파일 1개 권한 확인 (ls -l), 변경 (chmod), 변경 전후 비교 [증거](./evidences/command-log.md#파일-1개-권한-확인-ls--l-변경-chmod-변경-전후-비교)
-  디렉터리 1개 권한 확인 (ls -ld), 변경 (chmod), 변경 전후 비교 [증거](./evidences/command-log.md#디렉터리-1개-권한-확인-ls--ld-변경-chmod-변경-전후-비교)

## 6. Docker

### 6-1. 설치 및 점검

-  docker --version 출력 기록 [증거](./evidences/command-log.md#docker---version-출력-기록)
-  docker info 출력 기록 (데몬 동작 확인) [증거](./evidences/command-log.md#docker-info-출력-기록-데몬-동작-확인)

### 6-2. Docker 기본 운영 명령

-  이미지: 다운로드/목록 확인(예: docker images) [증거](./evidences/command-log.md#이미지-다운로드목록-확인예-docker-images)
-  컨테이너: 실행/중지/목록 확인(예: docker ps, docker ps -a) [증거](./evidences/command-log.md#컨테이너-실행중지목록-확인예-docker-ps-docker-ps--a)
-  운영: 로그 확인(예: docker logs), 리소스 확인(예: docker stats) [증거](./evidences/command-log.md#운영-로그-확인예-docker-logs-리소스-확인예-docker-stats)
-  컨테이너 실행, 중지, 재시작, 삭제 각 단계의 상태 변화 기록 [증거](./evidences/command-log.md#컨테이너-실행-중지-재시작-삭제-각-단계의-상태-변화-기록)

### 6-3. 컨테이너 실행 실습

-  hello-world 실행 성공 기록 [증거](./evidences/command-log.md#hello-world-실행-성공-기록)
-  ubuntu 이미지 다운로드 [증거](./evidences/command-log.md#ubuntu-이미지-다운로드)
-  ubuntu 컨테이너 대화형 실행, 내부에서 ls와 echo 수행 결과 기록 [증거](./evidences/command-log.md#ubuntu-컨테이너-대화형-실행-내부에서-ls와-echo-수행-결과-기록)
-  attach와 exec의 차이 정리 [증거](./evidences/command-log.md#attach와-exec의-차이-정리)

## 7. Dockerfile 기반 웹 서버 컨테이너

-  웹 서버 소스코드 (src/) [증거](./src/index.html)
-  Dockerfile [증거](./Dockerfile)
-  방식 선택: (A) nginx 베이스 이미지 활용
-  nginx 베이스 선택 이유 : 이미 웹 서버가 설치되고 기본 설정(정적 파일 제공, CMD 포함)이 적용되어 있어 작업 시작이 수월함.
-  커스텀 포인트별 목적 : nginx 태그(stable-alpine) - 안정성과 경량성에 적합함
-  docker build 실행 명령 및 결과 로그 [로그](./evidences/command-log.md#docker-build-실행-명령-및-결과-로그)
-  포트 매핑 접속 성공 증거(브라우저 스크린샷) [스크린샷](./evidences/docker-run-localhost-8080.png)

## 8. 포트 매핑 접속 증거

-  p <host_port>:<container_port>로 실행 후, 브라우저 접속 화면(주소창 포함)
  -  1회차 포트 매핑 실행 명령 기록, 브라우저 접속 캡처 (주소창에 포트 포함) [캡처(localhost:8080)](./evidences/docker-run-localhost-8080.png)
  -  2회차 다른 호스트 포트로 실행 (컨테이너 이름은 다르게), 브라우저 접속 캡처 [캡처(localhost:8081)](./evidences/docker-run-localhost-8081.png)

## 9. 바인드 마운트 반영 + 볼륨 영속성 증거

### 9-1. 바인드 마운트 반영

-  호스트 디렉터리를 컨테이너에 연결하는 실행 명령 기록 [증거](./evidences/command-log.md#호스트-디렉터리를-컨테이너에-연결하는-실행-명령-기록)
-  호스트 파일 변경 전/후 내용 비교 [증거](./evidences/command-log.md#호스트-파일-변경-전후-내용-비교)

### 9-2. Docker 볼륨 영속성 검증

-  볼륨 생성/연결/검증 로그 [증거](./evidences/command-log.md#볼륨-생성-연결-검증-로그)
-  컨테이너 삭제 전 데이터 확인 기록 (데이터 값 또는 파일 내용 원문 포함) [증거](./evidences/command-log.md#컨테이너-삭제-전-데이터-확인-기록-데이터-값-또는-파일-내용-원문-포함)
-  컨테이너 삭제 명령과 출력 기록 [증거](./evidences/command-log.md#컨테이너-삭제-명령과-출력-기록)
-  컨테이너 삭제 직후 볼륨 목록에 해당 볼륨이 남아 있는지 확인 기록 [증거](./evidences/command-log.md#컨테이너-삭제-직후-볼륨-목록에-해당-볼륨이-남아-있는지-확인-기록)
-  삭제한 컨테이너와 같은 볼륨을 연결한 새 컨테이너 실행 [증거](./evidences/command-log.md#삭제한-컨테이너와-같은-볼륨을-연결한-새-컨테이너-실행)
-  삭제 전/후 데이터 유지 검증
  -  새 컨테이너에서 삭제 전과 동일한 데이터 확인 기록 (삭제 전 기록과 대조) [증거](./evidences/command-log.md#새-컨테이너에서-삭제-전과-동일한-데이터-확인-기록-삭제-전-기록과-대조)
  -  볼륨을 연결하지 않은 대조용 컨테이너에서 같은 경로를 확인하여 데이터가 없음을 기록 [증거](./evidences/command-log.md#볼륨을-연결하지-않은-대조용-컨테이너에서-같은-경로를-확인하여-데이터가-없음을-기록)

## 10. Git 설정 및 GitHub 연동

-  사용자 이름, 사용자 이메일(마스킹), 기본 브랜치 설정 후 git config --list 출력 기록 (민감값 마스킹) [증거](./evidences/command-log.md#12-2-문제2)
-  VSCode에서 GitHub 로그인 연동 완료 캡처 (계정 정보 가림) [증거](./evidences/vscode-github-login.png)
-  연동 완료 캡처 (토큰, 인증 코드 포함 주의) [증거](./evidences/vscode-repo-linked.png)

## 11. 트러블슈팅 기록

### 11-1. 문제 1

- 문제: Docker 커스텀 이미지 빌드 실패
- 원인 가설: 빌드 컨텍스트에 존재하지 않는 파일을 COPY 시도함 [로그](./evidences/command-log.md#11-1-1-문제-및-원인-가설)
- 확인: [로그](./evidences/command-log.md#11-1-3-확인)
- 해결 또는 대안: 빌드 컨텍스트를 상위 경로인 프로젝트 폴더로 설정하여 이미지 빌드 실행함 [증거](./evidences/command-log.md#11-1-4-해결)

### 11-2. 문제 2

- 문제: git config 설정 중 not in a git directory 오류
- 원인 가설: 현재 경로가 git directory가 아님
- 확인: [로그](./evidences/command-log.md#11-2-3-확인)
- 해결: 경로 이동 및 진행 [로그](./evidences/command-log.md#11-2-4-해결)

## 12. 보너스 과제

-  Docker Compose 기초
  -  단일 서비스용 docker-compose.yml을 작성 [증거](./compose/docker-compose.yml)
  -  Compose 실행 결과를 단일 컨테이너 실행과 비교해 기록 [증거](./evidences/command-log.md#compose-실행-결과를-단일-컨테이너-실행과-비교해-기록)
  -  실행 설정을 파일로 문서화하는 이유 : 실행에 필요한 옵션을 로그가 아닌 파일에서 쉽게 확인할 수 있어 재현 가능성을 극대화함
-  Docker Compose 멀티 컨테이너
  -  웹 서버와 보조 서비스 1개 이상을 함께 실행 [증거](./evidences/command-log.md#웹-서버와-보조-서비스-1개-이상을-함께-실행)
  -  컨테이너 간 네트워크 통신이 가능한지 확인한다. [증거](./evidences/command-log.md#컨테이너-간-네트워크-통신-확인)  
-  Compose 운영 명령어 습득
  -  up, down, ps, logs를 각각 실행하고 출력 기록 [증거](./evidences/command-log.md#up-down-ps-logs를-각각-실행하고-출력-기록)  
  -  ps, logs 중심의 상태 확인 루틴 정리 : ps와 logs docker compose 명령어를 사용하여 실행중인 컨테이너의 상태와 로그를 확인할 수 있다.
-  환경 변수 활용
  -  포트 또는 실행 모드를 환경 변수로 지정 [증거](./env-var/docker-compose.yml)
  -  값을 바꿔 실행하고 변경 전후 동작 차이 기록 [증거](./evidences/command-log.md#값을-바꿔-실행하고-변경-전후-동작-차이-기록)
  -  GitHub SSH 키 설정 [증거](./evidences/command-log.md#github-ssh-키-설정)
  -  Windows에서 SSH 키를 생성하고 공개 키를 GitHub에 등록 [키생성로그](./evidences/command-log.md#windows에서-ssh-키를-생성) [키등록캡처](./evidences/github-ssh-key-add.png)
  -  원격 주소를 SSH로 바꾸고 푸시 성공 결과 기록 [증거](./evidences/command-log.md#원격-주소를-ssh로-바꾸고-푸시-성공-결과-기록)
  
## 13. 재현성 안내

- 실행 환경 전제: 윈도우 11 vscode 내부 터미널(powershell, wsl),윈도우 11 Git Bash, docker desktop(윈도우11)