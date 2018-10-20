const PAGES_COUNT = 60;
const COLORS = [
  'magenta',
  'yellow',
  'cyan',
  'aquablue',
  'white',
];

let lifetime = 0;

const glitch = () => {
  if (lifetime > 70) {
    const redirect = Math.floor(Math.random() * PAGES_COUNT);
    location.href = `/2018/final/${redirect + 1}.html`;
  } else {
    for (let i = 0; i < 2; i++) {
      const tds = document.querySelectorAll('td');
      const index = Math.floor(Math.random() * tds.length);
      const td = tds[index];
      if (td) {
        // td.style.transform = `
        //   rotate(${Math.floor(Math.random() * 180)}deg)
        // `;

        td.style.backgroundColor = COLORS[
          Math.floor(Math.random() * COLORS.length)
        ];

        td.classList.add('fly');

        // td.style.marginLeft = `
        //   ${Math.floor(Math.random() * 50)}px
        // `;
      }
    }
    tick();
  }
}

const tick = () => {
  setTimeout(() => {
    lifetime++;
    requestAnimationFrame(glitch);
  }, 100);
}


setTimeout(() => {
  document.querySelector('table').style.display = 'table';
  tick();
}, 1000);
