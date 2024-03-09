from general_methods.methods import scroll_test, wait_for_element_by_locator, tap


def test_simple(start_session):
    wait_for_element_by_locator(locator='fragment_onboarding_skip_button')
    tap(locator='fragment_onboarding_skip_button')
    scroll_test(direction='вниз', duration=300)

