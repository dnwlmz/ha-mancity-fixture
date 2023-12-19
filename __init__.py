import logging
import aiohttp
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.entity import Entity

DOMAIN = "mancity_fixture"
_LOGGER = logging.getLogger(__name__)

async def async_setup(hass, config):
    session = async_get_clientsession(hass)
    fixture = ManCityFixture(hass, session)
    await fixture.async_update_data()
    hass.data[DOMAIN] = fixture
    hass.helpers.discovery.load_platform('sensor', DOMAIN, {}, config)
    return True

class ManCityFixture(Entity):
    def __init__(self, hass, session):
        self._hass = hass
        self._session = session
        self._data = None

    async def async_update_data(self):
        url = "https://api-prod.mancity.com/footballdata/fixtures/next?teamId=43"
        headers = {
            "Content-Type": "application/json",
            "Api-Version": "v1",
            "Ocp-Apim-Subscription-Key": "63ce5dd387644382ad4a677f62d16df2",
            "Authorization": "Bearer ew0KICAiYWxnIjogIlJTMjU2IiwNCiAg...",
            "Cookie": "__cf_bm=bSRqpxll34EWoNEfQGt3mjC5NS4y...",
        }
        async with self._session.get(url, headers=headers) as response:
            if response.status != 200:
                _LOGGER.error(f"Failed to fetch data: {response.status}")
                return
            self._data = await response.json()
