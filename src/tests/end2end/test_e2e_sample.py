import pytest
import allure


class TestE2E(object):

    @allure.title("Verify E2E positive scenario for Restful Booker")
    @allure.description("Verify that Create Booking, Create Token -> Update -> Delete -> Full CRUD")
    def test_update_booking_with_id_token():
        pass

    @allure.title("Verify delete CRUD operation")
    @allure.description("Create Booking -> Delete It -> Verify")
    def test_delete_booking_id(self):
        pass
