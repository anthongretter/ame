PI := python
PI_MIN_VERSION := 3.10
PI_VERSION_OK=$(shell $(PI) -c 'import sys;print(int(float("%d.%d"% sys.version_info[0:2]) >= $(PI_MIN_VERSION)))')

ifeq ($(PI_VERSION_OK),0)
	$(error "Need python $(PYTHON_VERSION) >= $(PI_MIN_VERSION)")
endif

VENV_PATH := venv

$(VENV_PATH):
	python -m venv $@

install: requirements.txt $(VENV_PATH)
	@export PI=$(word 2,$^)/bin/python
	$(PI) -m pip install -r $<

run: install
	@export PI=$(VENV_PATH)/bin/python
	@if [ -z "$(FILE)" ]; then \
		echo "Usage: make run FILE=path/to/your/file.ame"; \
	else \
		$(PI) amec.py $(FILE); \
    fi

test1: install
	$(PI) main.py 'src/test/merge.ame'

test2: install
	$(PI) main.py 'src/test/primo.ame'

test3: install
	$(PI) main.py 'src/test/adivinha.ame'

all: install
