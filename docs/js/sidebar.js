const SIDEBAR_CACHE_ID = 'sidebar-cache';

const cachedSidebarHtml = sessionStorage.getItem(SIDEBAR_CACHE_ID);

if (cachedSidebarHtml) {
	loadSidebarHtml(cachedSidebarHtml);
}

fetch('contents.html')
	.then(r => r.text())
	.then(html => {
		sessionStorage.setItem(SIDEBAR_CACHE_ID, html);
		loadSidebarHtml(html);
	});


function loadSidebarHtml(html) {
	const contentsDiv = document.getElementById('contents');
	contentsDiv.innerHTML = html;

	afterSidebarLoaded();
}

function pressExpandButton() {
	const contents = document.querySelector('#contents');
	contents.classList.toggle('expanded');
}

function afterSidebarLoaded() {
	document.querySelector('#mobile-bar-expand-button').addEventListener('click', pressExpandButton);
}



