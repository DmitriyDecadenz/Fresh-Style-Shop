let dragItem = null;

document.addEventListener('dragstart', function(event) {
  dragItem = event.target;
  event.dataTransfer.setData('text/plain', '');
});

document.addEventListener('dragover', function(event) {
  event.preventDefault();
});

document.addEventListener('drop', function(event) {
  if (event.target.className === 'item') {
    event.target.parentNode.insertBefore(dragItem, event.target.nextSibling);
    event.preventDefault();
  }
});


