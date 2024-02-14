document.querySelectorAll('.dropdown-btn').forEach(item => {
  item.addEventListener('click', function() {
    var dropdownContainer = item.nextElementSibling;
    dropdownContainer.style.display = dropdownContainer.style.display === 'block' ? 'none' : 'block';
  });
});
