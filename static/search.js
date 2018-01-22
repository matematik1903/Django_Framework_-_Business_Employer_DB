$(document).ready(function (){
    $("#exampleInputText3").on("input", function () {
         $(".list_VACANCY").remove();
        var data = get_vacancy_search($(this).val());
        console.log(data);
        console.log("data");

        var ul_el = $("<ul/>", {
            class: "list_VACANCY",
            id: "list"
        }).appendTo("#list");

        for (var n in data) {
            var li_el = $('<li/>', {
                class: "" + data[n].pk,
                name: data[n].fields.name,
                click: function () {
                    // start_chat($(this).attr('user_id'));
                    $(".list_VACANCY").remove();
                    console.log("good");
                    document.getElementById('exampleInputText3').value = $(this).attr("name");
                    // $.("#exampleInputText3").text(data[n].fields.name);
                    // search();
                }
                // 'data-system-id': 100,
                // 'hh_hh_hh': true
            });

            // var avatar_el = $('<img>', {
            //     class: "avatar",
            //     alt: "avatar",
            //     src: "/static/media/" + data[n].fields.dialog_logo
            // });

            var about_el = $('<div/>', {
                class: "about " + data[n].pk
            });

            var name_el = $('<div/>', {
                class: "name " + data[n].pk,
                html: data[n].fields.name
            });

            console.log(data[n].fields.name);

            // var status_el = $("<div/>", {
            //     class: "status " + data[n].pk
            // }).appendTo(".clearfix ." + data[n].pk);
            //
            // var status_text

            li_el.appendTo(ul_el);
            // avatar_el.appendTo(li_el);
            about_el.appendTo(li_el);
            name_el.appendTo(about_el);
            // status_el.appendTo(about_el);
        }
    });

    $("#exampleInputText2").on("input", function () {
         $(".list_VACANCY").remove();
        var data = get_city_search($(this).val());
        console.log(data);
        console.log("data");

        var ul_el = $("<ul/>", {
            class: "list_VACANCY",
            id: "list_city"
        }).appendTo("#list_city");

        for (var n in data) {
            var li_el = $('<li/>', {
                class: "" + data[n].pk,
                name: data[n].fields.customer_city,
                click: function () {
                    // start_chat($(this).attr('user_id'));
                    $(".list_VACANCY").remove();
                    console.log("good");
                    document.getElementById('exampleInputText2').value = $(this).attr("name");
                    // $.("#exampleInputText3").text(data[n].fields.name);
                    // search();
                }
                // 'data-system-id': 100,
                // 'hh_hh_hh': true
            });

            // var avatar_el = $('<img>', {
            //     class: "avatar",
            //     alt: "avatar",
            //     src: "/static/media/" + data[n].fields.dialog_logo
            // });

            var about_el = $('<div/>', {
                class: "about " + data[n].pk
            });

            var name_el = $('<div/>', {
                class: "name " + data[n].pk,
                html: data[n].fields.customer_city
            });

            console.log(data[n].fields.customer_city);

            // var status_el = $("<div/>", {
            //     class: "status " + data[n].pk
            // }).appendTo(".clearfix ." + data[n].pk);
            //
            // var status_text

            li_el.appendTo(ul_el);
            // avatar_el.appendTo(li_el);
            about_el.appendTo(li_el);
            name_el.appendTo(about_el);
            // status_el.appendTo(about_el);
        }
    });
});