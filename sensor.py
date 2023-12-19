from homeassistant.helpers.entity import Entity

def setup_platform(hass, config, add_entities, discovery_info=None):
    fixture = hass.data['mancity_fixture']
    add_entities([ManCityFixtureSensor(fixture)], True)

class ManCityFixtureSensor(Entity):
    def __init__(self, fixture):
        self._fixture = fixture

    @property
    def name(self):
        return self._fixture.name

    @property
    def state(self):
        return self._fixture.state

    @property
    def icon(self):
        return self._fixture.icon

    @property
    def device_state_attributes(self):
        return self._fixture.device_state_attributes
