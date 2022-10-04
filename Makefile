VENV = env
PYTHON = python3
PIP = pip3
BIN=$(VENV)/bin

run:
	$(PYTHON) -m virtualenv env
	. $(BIN)/activate
	$(PIP) install -r requirements.txt
	$(PYTHON) run.py

clean:
	rm -rf __pycache__
	rm -rf $(VENV)

test:
	$(PYTHON) -m pytest