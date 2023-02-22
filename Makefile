test:
	python3 -m unittest tests/test_cache.py tests/test_memory_standard.py

init:
	pip install -r requirements.txt

.PHONY: init test
