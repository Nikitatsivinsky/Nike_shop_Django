const rangeSlider = document.getElementById('range-slider');
const rangeSliderInputMin = parseInt(document.getElementById('input-0').getAttribute('min'));
const rangeSliderInputMax = parseInt(document.getElementById('input-1').getAttribute('max'));

if (rangeSlider) {
	noUiSlider.create(rangeSlider, {
    start: [rangeSliderInputMin, rangeSliderInputMax],
		connect: true,
		step: 1,
    range: {
			'min': rangeSliderInputMin,
			'max': rangeSliderInputMax
    }
	});

	const input0 = document.getElementById('input-0');
	const input1 = document.getElementById('input-1');
	const inputs = [input0, input1];

	rangeSlider.noUiSlider.on('update', function(values, handle){
		inputs[handle].value = Math.round(values[handle]);
	});

	const setRangeSlider = (i, value) => {
		let arr = [null, null];
		arr[i] = value;

		console.log(arr);

		rangeSlider.noUiSlider.set(arr);
	};

	inputs.forEach((el, index) => {
		el.addEventListener('change', (e) => {
			console.log(index);
			setRangeSlider(index, e.currentTarget.value);
		});
	});
}