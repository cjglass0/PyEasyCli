import pytest
import coverage

cov = coverage.Coverage()
cov.set_option('run:omit', ['tests/*'])

cov.start()
pytest.main(args=["-rP"])

cov.stop()
cov.save()
cov.html_report(directory='covhtml')