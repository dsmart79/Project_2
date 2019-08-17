// Step 1: Read the JSON file with d3.json()
var clean_rate = d3.json('data/ufo_data.json')
  .then(function(data) {
    console.log('data:', data);

    // All code goes here


    // calculate number of records per state
    var clean_rate_tally = {};

    // Loop through each row
    data.forEach(function(row) { 
      var StateCode = row['StateCode'];

      if (!StateCode[StateCode]) {
        sightings_tally[date] = 1;
      } else {
        clean_rate_tally[StateCode] += 1;
      }
    })

    console.log('sightings_tally:', clean_rate_tally);

    clean_rate_counts = Object.values(clean_rate_tally);

    console.log('sightings_counts:', clean_rate_counts );

    // Build line chart
    var chart = c3.generate({
      bindto: '#spline-chart',
      data: {
          columns: [
              ['Sightings'].concat(clean_rate_counts)
          ],
          type: 'spline'
      }
    });

    var chart = c3.generate({
      bindto: '#chart2',
      data: {
          columns: [
              ['Sightings'].concat(clean_rate_counts)
          ],
          type: 'spline'
      }
    });

    setTimeout(function () {
      chart.transform('pie');
    }, 2000);
  })


// Step X: Create chart using the data
// var chart = c3.generate({
//   bindto: '#spline-chart',
//   data: {
//       columns: [
//           ['data1', 30, 200, 100, 400, 150, 250],
//           ['data2', 130, 100, 140, 200, 150, 50]
//       ],
//       type: 'spline'
//   }
// });