

document.addEventListener('click', function (e) {
  try {
    // allows for elements inside TH
    function findElementRecursive(element, tag) {
      return element.nodeName === tag ? element : findElementRecursive(element.parentNode, tag)
    }

    var descending_th_class = ' dir-d '
    var ascending_th_class = ' dir-u '
    var ascending_table_sort_class = 'asc'
    var regex_dir = / dir-(u|d) /
    var regex_table = /\bsortable\b/
    var alt_sort = e.shiftKey || e.altKey
    var element = findElementRecursive(e.target, 'TH')
    var tr = findElementRecursive(element, 'TR')
    var table = findElementRecursive(tr, 'TABLE')

    function reClassify(element, dir) {
      element.className = element.className.replace(regex_dir, '') + dir
    }

    function getValue(element) {
      // If you aren't using data-sort and want to make it just the tiniest bit smaller/faster
      // comment this line and uncomment the next one
      var value =
        (alt_sort && element.getAttribute('data-sort-alt')) || element.getAttribute('data-sort') || element.innerText
      return value
      // return element.innerText
    }
    if (regex_table.test(table.className)) {
      var column_index
      var nodes = tr.cells

      // Reset thead cells and get column index
      for (var i = 0; i < nodes.length; i++) {
        if (nodes[i] === element) {
          column_index = element.getAttribute('data-sort-col') || i
        } else {
          reClassify(nodes[i], '')
        }
      }

      var dir = descending_th_class

      // Check if we're sorting ascending or descending
      if (
        element.className.indexOf(descending_th_class) !== -1 ||
        (table.className.indexOf(ascending_table_sort_class) !== -1 &&
          element.className.indexOf(ascending_th_class) == -1)
      ) {
        dir = ascending_th_class
      }

      // Update the `th` class accordingly
      reClassify(element, dir)

      // loop through all tbodies and sort them
      for (var i = 0; i < table.tBodies.length; i++) {
        const org_tbody = table.tBodies[i]

        // Get the array rows in an array, so we can sort them...
        var rows = [].slice.call(org_tbody.rows, 0)

        var reverse = dir === ascending_th_class

        // Sort them using Array.prototype.sort()
        rows.sort(function (a, b) {
          var x = getValue((reverse ? a : b).cells[column_index])
          var y = getValue((reverse ? b : a).cells[column_index])
          var bool = x.length && y.length && !isNaN(x - y) ? x - y : x.localeCompare(y)
          return bool
        })

        // Make a clone without content
        var clone_tbody = org_tbody.cloneNode()

        // Fill it with the sorted values
        while (rows.length) {
          clone_tbody.appendChild(rows.splice(0, 1)[0])
        }

        // And finally replace the unsorted table with the sorted one
        table.replaceChild(clone_tbody, org_tbody)
      }
    }
  } catch (error) {
    // console.log(error)
  }
})