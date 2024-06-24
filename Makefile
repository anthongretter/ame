PI := python
PI_MIN_VERSION := 3.10
PYTHON_VERSION_OK=$(shell $(PI) -c 'import sys;print(int(float("%d.%d"% sys.version_info[0:2]) >= $(PI_MIN_VERSION)))')

ifeq ($(PYTHON_VERSION_OK),0)
	$(error "Need python $(PYTHON_VERSION) >= $(PYTHON_VERSION_MIN)")
endif

VENV_PATH:=venv

$(VENV_PATH):
	python -m venv $@

install: requirements.txt $(VENV_PATH)
	@PI=$(word 2,$^)/bin/python
	$(PI) -m pip install -r $<

all: install
