import Page from './routes/page.svelte';

const target = document.getElementById('app');

async function render() {
  new Page({target});
}

document.addEventListener('DOMContentLoaded', render);
