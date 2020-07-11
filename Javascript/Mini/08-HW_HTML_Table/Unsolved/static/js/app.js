// Use D3 to select the table
console.log(grades)
// Use D3 to select the table body
tbody =d3.select("tbody") 
// Use D3 to set the table class to `table table-striped`

d3.select("#student-table").attr("class", "table table-striped")

// Use a forEach function to loop through the array of objects (from your data)
grades.forEach((studentgrade) => {
 
  row = tbody.append("tr")
  row.append("td").text(studentgrade.name)
  g = row.append("td").text(studentgrade.grade)
  
  if (studentgrade.grade < 70 ){
    g.attr("class", "table-warning")

  }
  if (studentgrade.grade < 60 ){
    g.attr("class", "table-danger")

  }

  // Assign values to the `student` name variable and the `grade` variable

  // Append one table row per student/grade

  // append one cell for the student and one cell for the grade

});
