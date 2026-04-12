const scriptTag = document.currentScript;

fetch('contents.html')
	.then(r => r.text())
	.then(html => {
		const div = document.createElement('div');
		div.id = 'contents-container';
		div.innerHTML = html;
		scriptTag.replaceWith(div);

		afterSidebarLoaded();
	});

function pressExpandButton() {
	const contents = document.querySelector('#contents');
	contents.classList.toggle('expanded');
}

function afterSidebarLoaded() {
	document.querySelector('#mobile-bar-expand-button').addEventListener('click', pressExpandButton);
}



