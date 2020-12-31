@echo off
cd C:\Users\"Dana Scully"\.virtualenvs\hybrid_framework-3he1d7dv\Scripts
pytest -v -m "sanity" --html=C:/Users/"Dana Scully"/Selenium/hybrid_framework/reports/201230/report.html C:/Users/"Dana Scully"/Selenium/hybrid_framework/test_cases 
timeout /t 10