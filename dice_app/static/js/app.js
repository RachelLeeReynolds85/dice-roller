const diceList = ["d4", "d6", "d8", "d10", "d12", "d20",]

var diceDict = {
	d4: "blank",
	d6: "blank",
	d8: "blank",
	d10: "blank",
	d12: "blank",
	d20: "blank",
}
console.log(diceDict)

const tableColumns = ["Roll #", "Ways to roll", "Exact", "Or higher"]

function loadTable() {
	diceList.forEach(dieName => {
		var currentDie = d3.select(`#${dieName}dice`)
		var numDie = currentDie.property("value")
		console.log(numDie)
		diceDict[dieName] = parseInt(numDie)
	})

	console.log(diceDict)

	fetch(`${window.origin}/index/select-dice`, {
		method: "POST",
		credentials: "include",
		body: JSON.stringify(diceDict),
		cache: "no-cache",
		headers: new Headers({
			"content-type": "application/json"
		})
	})
	.then(function (response) {
		if (response.status !== 200) {
			console.log(`Looks like there was a problem. Status code: ${response.status}`);
			return;
		}
		response.json().then(function (tableData) {
			console.log("Table Data:")
			console.log(tableData)

			let clear_results = d3.select("#dice-table")
                if (clear_results._groups[0][0].hasChildNodes()) {
					clear_results.selectAll("table").remove()
					}

			var table = d3.select('#dice-table')
				.append('table')
				.classed("center", true)
			var thead = table.append('thead')
			var	tbody = table.append('tbody');

			// append the header row
			thead.append('tr')
			.selectAll('th')
			.data(Object.keys(tableData))
			.enter()
			.append('th')
			.text(d => d);

			for (i = 0; i < _.size(tableData["Roll Total"]); i++) {
				var row = tbody.append('tr')
				Object.keys(tableData).forEach(column => {
					row.append('td')
					.text(tableData[column][i])
				}) 				
			}

			// create a row for each object in the data
			var rows = tbody.selectAll('tr')
			.data(tableData["Roll #"])
			.enter()
			.append('tr')
			
			rows.selectAll('td')
			.data(tableData)
			.enter()
			.append('td')
			.text(d => d)

			
			
		})
	})
	.catch(function (error) {
		console.log("Fetch error: " + error)
	})


}

