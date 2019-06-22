function sortTable(table) {
  var rows, switching, i, x, y, shouldSwitch;
  switching = true;
  /* Make a loop that will continue until
  no switching has been done: */
  while (switching) {
    // Start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    /* Loop through all table rows (except the
    first, which contains table headers): */
    for (i = 1; i < (rows.length - 1); i++) {
      // Start by saying there should be no switching:
      shouldSwitch = false;
      /* Get the two elements you want to compare,
      one from current row and one from the next: */
      x = rows[i].getElementsByTagName("TD")[2];
      y = rows[i + 1].getElementsByTagName("TD")[2];
      // Check if the two rows should switch place:
      if (parseInt(x.innerHTML) < parseInt(y.innerHTML)) {
        // If so, mark as a switch and break the loop:
        shouldSwitch = true;
        break;
      }
    }
    if (shouldSwitch) {
      /* If a switch has been marked, make the switch
      and mark that a switch has been done: */
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
    }
  }
}

function colorRows(table) {
  var rows = table.rows;
  var regions = ['Asia', 'America', 'Europe', 'Africa'];
  var regions_completed = [0, 0, 0, 0];
  for (var i = 1; i < 16; i++) {
    if (i <= 4) {
      rows[i].classList.add('top_4');  
    }
    else{
      tmp_region = rows[i].getElementsByTagName("TD")[1].innerHTML;
      tmp_index = regions.indexOf(tmp_region);
      if (regions_completed[tmp_index] == 0) {
        regions_completed[tmp_index] = 1;
        rows[i].classList.add('top_region');     
      }
    }
  }
  if(regions_completed.indexOf(0) != -1){
      var to_fill = true;
      for (var j = 6; j <= 8 && to_fill; j++) {
        if(rows[j].classList[0] === undefined){
          rows[j].classList.add('extra_region');
          to_fill = false;
        }
      }
    }
}

for (var i = 5; i >= 0; i--) {
  var table = document.getElementsByClassName("rankings")[i];
  sortTable(table);
  colorRows(table);
}

