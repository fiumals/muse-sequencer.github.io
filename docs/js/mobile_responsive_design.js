const SCREEN_WIDTH_FOR_MOBILE_DESIGN = 900; // less than

function refreshWidthForMobileDesign() {
	const screenWidth = window.top.innerWidth;

	const mainContainer = window.parent.document.querySelector('#main');
	const contents = window.parent.document.querySelector('#contents');

	if (screenWidth < SCREEN_WIDTH_FOR_MOBILE_DESIGN) {
		document.body.classList.add('mobile');
		mainContainer.classList.add('mobile');
		contents.classList.add('mobile');
	} else {
		document.body.classList.remove('mobile');
		mainContainer.classList.remove('mobile');
		contents.classList.remove('mobile');
		contents.classList.remove('expanded');
	}

}

function pressExpandButton() {
	const contents = window.parent.document.querySelector('#contents');
	contents.classList.toggle('expanded');
	document.body.classList.toggle('expanded');
}

document.getElementById('mobile-bar-expand-button').addEventListener('click', pressExpandButton);
document.addEventListener('DOMContentLoaded', refreshWidthForMobileDesign);
window.top.addEventListener('resize', refreshWidthForMobileDesign);


