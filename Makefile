FILE ?= "Exercise/pytest/example1.txt"
REGEX ?= "grows"

build:
  @echo "Building container"
  @cd build && sudo docker build -t exercise .

run:
  @echo "Running tests"
  @sudo docker run --rm -v /home/ubuntu/Exercise/:/Exercise exercise python3 -m pytest /Exercise/pytest/TestSuite.py

app_runner:
  @echo "Running app"
  @sudo docker run --rm -v /home/ubuntu/Exercise/:/Exercise exercise python3 /Exercise/run_app.py -f ${FILE} -r ${REGEX}

run-interactive:
  @echo "Running interactive container"
  @sudo docker run -it -v /home/ubuntu/Exercise/:/Exercise exercise /bin/bash