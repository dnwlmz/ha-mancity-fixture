class ManCityFixtureCard extends HTMLElement {
    set hass(hass) {
        if (!this.content) {
            const card = document.createElement('ha-card');
            card.header = 'Man City Fixture';
            this.content = document.createElement('div');
            this.content.style.padding = '0 16px 16px';
            card.appendChild(this.content);
            this.appendChild(card);
        }

        const entity = hass.states['sensor.mancity_fixture'];
        const competition = entity.attributes.competition;
        const kickoff_time = entity.attributes.kickoff_time;
        const venue = entity.attributes.venue;
        const state = entity.state;

        this.content.innerHTML = `
            <style>
                .fixture-info {
                    display: flex;
                    flex-direction: column;
                }
                .fixture-info > * {
                    margin: 8px 0;
                }
            </style>
            <div class="fixture-info">
                <div>Competition: ${competition}</div>
                <div>Kickoff Time: ${kickoff_time}</div>
                <div>Venue: ${venue}</div>
                <div>State: ${state}</div>
            </div>
        `;
    }

    getCardSize() {
        return 3;
    }
}

customElements.define('mancity-fixture-card', ManCityFixtureCard);
