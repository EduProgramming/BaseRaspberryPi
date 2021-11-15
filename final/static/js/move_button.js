const SERVO_LEFT_BTN = document.getElementById('servo_left_btn')
const SERVO_RIGHT_BTN = document.getElementById('servo_right_btn')

SERVO_LEFT_BTN.addEventListener('click', () => {
	let servo_end_checkbox = document.getElementById('servo_end_checkbox')
	is_servo_end = servo_end_checkbox.checked
	SERVO_LEFT_BTN.disabled = true
	SERVO_RIGHT_BTN.disabled = true
	SERVO_LEFT_BTN.classList.remove('btn-info')
	SERVO_LEFT_BTN.classList.add('btn-secondary')
	SERVO_RIGHT_BTN.classList.remove('btn-info')
	SERVO_RIGHT_BTN.classList.add('btn-secondary')
	axios.post('/cctv_move_left', data={"state": is_servo_end})
		.then(res => {
			if (res.data.result == true) {
				SERVO_LEFT_BTN.disabled = false
				SERVO_LEFT_BTN.classList.remove('btn-secondary')
				SERVO_LEFT_BTN.classList.add('btn-info')
				SERVO_RIGHT_BTN.disabled = false
				SERVO_RIGHT_BTN.classList.remove('btn-secondary')
				SERVO_RIGHT_BTN.classList.add('btn-info')
			}
		})
		.catch(err => {
			console.error(err)
		})
})

SERVO_RIGHT_BTN.addEventListener('click', () => {
	let servo_end_checkbox = document.getElementById('servo_end_checkbox')
	is_servo_end = servo_end_checkbox.checked
	SERVO_LEFT_BTN.disabled = true
	SERVO_RIGHT_BTN.disabled = true
	SERVO_LEFT_BTN.classList.remove('btn-info')
	SERVO_LEFT_BTN.classList.add('btn-secondary')
	SERVO_RIGHT_BTN.classList.remove('btn-info')
	SERVO_RIGHT_BTN.classList.add('btn-secondary')
	axios.post('/cctv_move_right', data={"state": is_servo_end})
		.then(res => {
			if (res.data.result == true) {
				SERVO_LEFT_BTN.disabled = false
				SERVO_LEFT_BTN.classList.remove('btn-secondary')
				SERVO_LEFT_BTN.classList.add('btn-success')
				SERVO_RIGHT_BTN.disabled = false
				SERVO_RIGHT_BTN.classList.remove('btn-secondary')
				SERVO_RIGHT_BTN.classList.add('btn-success')
			}
		})
		.catch(err => {
			console.error(err)
		})
})

const FORWARD_BTN = document.getElementById('forward_btn')
const TURN_LEFT_BTN = document.getElementById('turn_left_btn')
const TURN_RIGHT_BTN = document.getElementById('turn_right_btn')
const BACKWARD_BTN = document.getElementById('backward_btn')
const STOP_BTN = document.getElementById('stop_btn')

FORWARD_BTN.addEventListener('click', () => {
	axios.get('/motor_forward')
		.then(res => {
			console.log(res)
		})
		.catch(err => {
			console.error(err)
		})
})

STOP_BTN.addEventListener('click', () => {
	axios.get('/motor_stop')
		.then(res => {
			console.log(res)
		})
		.catch(err => {
			console.error(err)
		})
})

TURN_LEFT_BTN.addEventListener('click', () => {
	axios.get('/motor_turn_left')
		.then(res => {
			console.log(res)
		})
		.catch(err => {
			console.error(err)
		})
})

TURN_RIGHT_BTN.addEventListener('click', () => {
	axios.get('/motor_turn_right')
		.then(res => {
			console.log(res)
		})
		.catch(err => {
			console.error(err)
		})
})

BACKWARD_BTN.addEventListener('click', () => {
	axios.get('/motor_backward')
		.then(res => {
			console.log(res)
		})
		.catch(err => {
			console.error(err)
		})
})

const SPEED_SETTING_BTN = document.getElementById('speed_setting_btn')
SPEED_SETTING_BTN.addEventListener('click', () => {
	let set_speed = document.getElementById('dc_speed_input').value
	set_speed = Math.max(set_speed, 0)
	set_speed = Math.min(set_speed, 100)
	axios.post('/setting_motor_speed', data={'speed': set_speed})
		.then(res => {
			console.log(res)
		})
		.catch(err => {
			console.error(err)
		})
})