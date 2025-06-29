const new_encounter = document.getElementById("new-encounter");
const planned_encounters = document.getElementById("planned-encounters");
const new_encounter_container = document.getElementById("new-encounter-container");
const planned_encounter_container = document.getElementById("planned-encounter-container");
const new_encounter_button = document.getElementById("new-encounter-button");

const encounter_setting = document.getElementById("encounter-setting");
const encounter_area = document.getElementById("encounter-area");
const encounter_danger = document.getElementById("encounter-danger");

const encounter_title = document.getElementById("encounter-title");
const encounter_text = document.getElementById("encounter-text");



new_encounter.addEventListener("click", function () {
    console.log("New encounter button clicked");
    new_encounter_container.hidden = false;
    planned_encounter_container.hidden = true;
    
  
})

planned_encounters.addEventListener("click", function () {
    console.log("Planned encounters button clicked");
    new_encounter_container.hidden = true;
    planned_encounter_container.hidden = false;

})

new_encounter_button.addEventListener("click", function () {
    console.log("New encounter button clicked");
    let data = {
        // Add any data you want to send with the request
        // encoutnter setting, area, danger
        setting: encounter_setting.value,
        area: encounter_area.value,
        danger: encounter_danger.value
    };

    api.post('encounters', data)
        .then(response => {
            console.log("New encounter form loaded successfully");
            console.log("Response:", response);
            encounter_title.textContent = response.headline || "Default Encounter Title";
            encounter_text.textContent = response.text || "Default Encounter Text";
            
        })
        .catch(error => {
            console.error("Error loading new encounter form:", error);
            alert("Failed to load new encounter form. Please try again later.");
        })

    
}   );

