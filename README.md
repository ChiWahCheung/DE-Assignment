## Python Env
### Option 1: pyenv
```shell
pyenv virtualenv 3.9.13 training
pyenv activate training
```

### Option 2: conda
```shell
conda create -n training python=3.9.13
conda activate training
```

## Install Requirements
```shell
pip install -r requirements.txt
```

## Setup Database
```shell
docker-compose up
```

## Setup Airflow
```shell
bash ./scripts/airflow-bootstrap.sh
```