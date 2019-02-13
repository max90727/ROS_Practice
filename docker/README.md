
# Instructions for docker usage

Run all script when current working directory is the root of the repository

Docker image can be created and started from both windows and linux systems

## Windows
Usage

	docker\helper.bat [command]


## Linux
Usage

	docker/helper [command]

## Helper commands
	build                Creates the image from the Dockerfile instructions
	run [args]           Starts a container of the docker image (executes args if given)
	clean                Cleans all hanging images and containers (not labeled or running)
	cleanall             Clean and removes named image created by this script
	save_image           Stores the image in a compressed file

## General
### Running the docker container
When starting the container an opptional command can be used. The command will then be executed and the container will exit when finished. If the command is left out, a bash prompt will be started.

### File system interaction
The /data location inside the container is mapped to the local host filesystem (current working directory, root of repo as defined above).

In windows it is important to grant docker service access (Docker/Settings.../Shared Drives) to the location where your repository is checked out. If not granted access, the /data not be mapped and the folder will be empty.

For linux, the current user identification is transferred to the docker container to enable file access rights are maintained between host and docker container.  
