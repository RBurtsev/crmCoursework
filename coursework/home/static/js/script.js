function search_parts() {
    var phrase = document.getElementById('searchbar');
    var table = document.getElementById('info-parts');
    var regPhrase = new RegExp(phrase.value, 'i');
    var flag = false;
    for (var i = 1; i < table.rows.length; i++) {
        flag = false;
        for (var j = table.rows[i].cells.length - 1; j >= 0; j--) {
            flag = regPhrase.test(table.rows[i].cells[j].innerHTML);
            if (flag) break;
        }
        if (flag) {
            table.rows[i].style.display = "";
        } else {
            table.rows[i].style.display = "none";
        }

    }
}

function search_clients() {
    var phrase = document.getElementById('searchbar');
    var table = document.getElementById('info-clients');
    var regPhrase = new RegExp(phrase.value, 'i');
    var flag = false;
    for (var i = 1; i < table.rows.length; i++) {
        flag = false;
        for (var j = table.rows[i].cells.length - 1; j >= 0; j--) {
            flag = regPhrase.test(table.rows[i].cells[j].innerHTML);
            if (flag) break;
        }
        if (flag) {
            table.rows[i].style.display = "";
        } else {
            table.rows[i].style.display = "none";
        }

    }
}

function search_fixes() {
    var phrase = document.getElementById('searchbar');
    var table = document.getElementById('info-fixes');
    var regPhrase = new RegExp(phrase.value, 'i');
    var flag = false;
    for (var i = 1; i < table.rows.length; i++) {
        flag = false;
        for (var j = table.rows[i].cells.length - 1; j >= 0; j--) {
            flag = regPhrase.test(table.rows[i].cells[j].innerHTML);
            if (flag) break;
        }
        if (flag) {
            table.rows[i].style.display = "";
        } else {
            table.rows[i].style.display = "none";
        }

    }
}

function search_workers() {
    var phrase = document.getElementById('searchbar');
    var table = document.getElementById('info-workers');
    var regPhrase = new RegExp(phrase.value, 'i');
    var flag = false;
    for (var i = 1; i < table.rows.length; i++) {
        flag = false;
        for (var j = table.rows[i].cells.length - 1; j >= 0; j--) {
            flag = regPhrase.test(table.rows[i].cells[j].innerHTML);
            if (flag) break;
        }
        if (flag) {
            table.rows[i].style.display = "";
        } else {
            table.rows[i].style.display = "none";
        }

    }
}

function price_func() {
	    var result;
	    var l = 0;
	    var parts = Number(document.getElementById("parts").value);
	    var hourly_rate = Number(document.getElementById("hourly_rate").value);
	    var hours = Number(document.getElementById("hours").value);
	    var difficult = document.getElementById("difficult").value;
	    switch (difficult) {
	      case 'easy':
	        result = parts + hours * hourly_rate;
	        l = 1;
	        break;
	      case 'normal':
	        result = parts + hours * hourly_rate;
	        result = result * 1.2;
	        l = 1;
	        break;
	      case 'hard':
	        result = parts + hours * hourly_rate;
	        result = result * 1.5;
	        l = 1;
	        break;
	    }
	    if (l == 0) {
	        result = "Incorrect data for cost calculation.";
	    }

	    document.getElementById("result").innerHTML = result;
	  }


