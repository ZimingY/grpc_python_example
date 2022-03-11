# This is an example showing how to use docker

# The following command will take you to a docker container
docker run --rm --gpus 0 -it \
            -v $(pwd)/mount/from:/mount/to \
            -v /mount/from:/mount/to:ro \
            -e USER=$(whoami) \
            -w /the/work/directory \
            --env-file config \
            $DOCKER_IMAGE \
            bash -c "bash"


# The following command will run the script directly
docker run --rm \
    -v $(pwd)/output:/output \
    -w /work/directory \
    $DOCKER_IMAGE ./run.sh $@


