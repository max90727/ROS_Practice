@ECHO OFF

set DOCKER_IMAGE_NAME=aftech/robot
set WORKDIR=/data
set DOCKER_FOLDER=%~dp0

set SCRIPT=%~nx0

for /f "tokens=1-1*" %%a in ("%*") do (
   set CMD=%%a
   set args=%%b
   )

IF "%CMD%"=="build" (
    GOTO :build
)
IF "%CMD%"=="run" (
    GOTO :run
)
IF "%CMD%"=="clean" (
    GOTO :clean
)
IF "%CMD%"=="cleanall" (
    GOTO :cleanall
)

ECHO "%SCRIPT% <command> <optional command argument>
ECHO   clean          Prunes all images/containers and volumes which is not tagged
ECHO   cleanall       clean + removes named image created by this script
ECHO   build          builds the docker image (%DOCKER_IMAGE_NAME%)
ECHO   run [args]     runs image (%DOCKER_IMAGE_NAME%) and execute the optional arg, by default "bash" is called

GOTO :theend

:clean
ECHO Cleaning docker images/containers
docker images prune
docker container prune -f
docker volume prune -f
GOTO :theend

:cleanall
ECHO Cleaning and remove docker images/containers
docker rmi --force %DOCKER_IMAGE_NAME%
GOTO :theend

:build
ECHO Building docker image
docker build --no-cache -t %DOCKER_IMAGE_NAME% %DOCKER_FOLDER%
GOTO :theend

:run
IF NOT "%args%"=="" (set ARGS=%args%) ELSE (set ARGS="bash")
ECHO Running docker image (%ARGS%)
docker run -it --privileged --rm ^
    --net=host ^
    --ipc=host ^
    --volume %cd%:%WORKDIR% ^
    -w %WORKDIR% ^
    %DOCKER_IMAGE_NAME% %ARGS%
GOTO :theend


:theend