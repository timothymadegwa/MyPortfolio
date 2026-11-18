const menuButton = document.querySelector('.nav-toggle');
const navigation = document.querySelector('.nav-links');

if (menuButton && navigation) {
  menuButton.addEventListener('click', () => {
    const isOpen = menuButton.getAttribute('aria-expanded') === 'true';
    menuButton.setAttribute('aria-expanded', String(!isOpen));
    navigation.classList.toggle('is-open', !isOpen);
  });

  navigation.addEventListener('click', (event) => {
    if (event.target instanceof HTMLAnchorElement) {
      menuButton.setAttribute('aria-expanded', 'false');
      navigation.classList.remove('is-open');
    }
  });
}

const currentYear = String(new Date().getFullYear());
document.querySelectorAll('[data-current-year]').forEach((element) => {
  element.textContent = currentYear;
});

const experienceStart = new Date(2018, 3, 1);
const today = new Date();
const anniversary = new Date(today.getFullYear(), experienceStart.getMonth(), experienceStart.getDate());
const experienceYears = today.getFullYear() - experienceStart.getFullYear() - Number(today < anniversary);

document.querySelectorAll('[data-experience-years]').forEach((element) => {
  element.textContent = `${experienceYears}+ years`;
});
