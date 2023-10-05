console.log('global.js loaded')

function sidebarState() {
    return {
        toggle: {
            doctors: false,
            patients: false,
            nurses: false
        },
        toggleDoctors() {
            console.log('toggling doctors')
            this.toggle.doctors = !this.toggle.doctors
        },
        togglePatients() {
            console.log('toggling patients')
            this.toggle.patients = !this.toggle.patients
        },
        toggleNurses() {
            console.log('toggling nurses')
            this.toggle.nurses = !this.toggle.nurses
        },
    }
}