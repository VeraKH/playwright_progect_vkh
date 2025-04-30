.PHONY: test test-chromium test-first test-local test-report test-ui install clean

# Установка зависимостей
install:
	pip install -r requirements.txt

# Запуск всех тестов
test:
	pytest

# Тесты в Chromium (Playwright)
test-chromium:
	pytest --browser=chromium

# Запуск тестов с маркером "first"
test-first:
	pytest -m first

# Запуск локально с переменной окружения
test-local:
	BASE_URL=http://localhost:4200 pytest

# Генерация и открытие HTML-отчета
test-report:
	pytest --html=report.html && open report.html

# UI режим для Playwright (аналог --ui)
test-ui:
	pytest --headed

# Очистка старых отчетов и кэша pytest
clean:
	rm -rf .pytest_cache report.html
