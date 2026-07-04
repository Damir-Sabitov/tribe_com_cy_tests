from pages import web_site_page
from pages.web_site_page import WebSitePage
import pytest

@pytest.mark.parametrize('language,exprected',[('English','ENG'),
                                        ('Russian','РУС'),
                                        ('Greek','ΕΛ')])
def test_change_languae(language, exprected):
    page = WebSitePage(language=language)
    page.browser_open()
    page.click_change_language_button()
    page.click_chose_language_button()
    assert page.check_language()==exprected
