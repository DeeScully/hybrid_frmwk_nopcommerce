@echo off
rem cd C:\Users\"Dana Scully"\.virtualenvs\hybrid_framework-3he1d7dv\Scripts
rem pytest -v -m "sanity" --html=C:/Users/"Dana Scully"/Selenium/hybrid_framework/reports/201230/report.html C:/Users/"Dana Scully"/Selenium/hybrid_framework/test_cases
rem timeout /t 10

pytest -v -m "sanity" --html=./reports/201231/report.html test_cases/