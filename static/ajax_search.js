function get_vacancy_search(exampleInputText3) {
	var result = false;
	console.log(exampleInputText3);

	$.ajax({
		url: "/get_vacancy_search/",
		type: "POST",
		data: {'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(), "search_login": exampleInputText3},
		cache: false,
		dataType: "json",
        async: false,
		success: function(data){
		    result = data;
		    console.log("Ajax get info ok!")
        },
		error: function(){
    		alert("fail");
		}
	});
    console.log(result);
    return result;
}

function get_city_search(exampleInputText2) {
	var result = false;
	console.log(exampleInputText2);

	$.ajax({
		url: "/get_city_search/",
		type: "POST",
		data: {'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(), "search_login": exampleInputText2},
		cache: false,
		dataType: "json",
        async: false,
		success: function(data){
		    result = data;
		    console.log("Ajax get info ok!")
        },
		error: function(){
    		alert("fail");
		}
	});
    console.log(result);
    return result;
}