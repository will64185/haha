call cd ..

call pytest -v -n 2 --alluredir allure-results --clean-alluredir

call allure generate allure-results -c -o allure-report

call allure open allure-report