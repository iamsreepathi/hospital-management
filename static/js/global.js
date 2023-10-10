console.log('global.js loaded')

function sidebarState() {
    return {
        toggle: {
            doctors: true,
            patients: false,
            nurses: false,
            appointments: false
        },
        toggleDoctors() {
            this.toggle.doctors = !this.toggle.doctors
        },
        togglePatients() {
            this.toggle.patients = !this.toggle.patients
        },
        toggleNurses() {
            this.toggle.nurses = !this.toggle.nurses
        },
        toggleAppointments() {
            this.toggle.appointments = !this.toggle.appointments
        },
    }
}