import '../app.css';
import Counter from '../components/Counter.svelte';
import Page from './routes/page.svelte';

const target = document.getElementById('app');
// target.style.width = '10rem';
// target.style.height = "1rem";

async function render() {
  // const {count} = await chrome.storage.sync.get({count: 0});

  new Page({target});
  // new Counter({target, props: {count}});
}

document.addEventListener('DOMContentLoaded', render);
