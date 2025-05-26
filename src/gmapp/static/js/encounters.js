const new_encounter = document.getElementById("new-encounter");
const planned_encounters = document.getElementById("planned-encounters");
const new_encounter_container = document.getElementById("new-encounter-container");
const planned_encounter_container = document.getElementById("planned-encounter-container");

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