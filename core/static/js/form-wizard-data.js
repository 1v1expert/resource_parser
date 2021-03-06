/*FormWizard Init*/
$(function(){
	"use strict";

	if($('#example-advanced-form').length >0){
		var form_2 = $("#example-advanced-form");
		form_2.steps({
			headerTag: "h3",
			bodyTag: "fieldset",
			transitionEffect: "fade",
			titleTemplate: '#title#',
			labels: {
				finish: "На печать ->",
				next: "Далее",
				previous: "Назад",
			},
			onStepChanging: function (event, currentIndex, newIndex)
			{
				// Allways allow previous action even if the current form is not valid!
				if (currentIndex > newIndex)
				{
					return true;
				}
				// Forbid next action on "Warning" step if the user is to young
				if (newIndex === 3 && Number($("#age-2").val()) < 18)
				{
					return false;
				}
				// Needed in some cases if the user went back (clean up)
				if (currentIndex < newIndex)
				{
					// To remove error styles
					form_2.find(".body:eq(" + newIndex + ") label.error").remove();
					form_2.find(".body:eq(" + newIndex + ") .error").removeClass("error");
				}
				form_2.validate().settings.ignore = ":disabled,:hidden";
				return form_2.valid();
			},
			onFinishing: function (event, currentIndex)
			{
				form_2.validate().settings.ignore = ":disabled";
				return form_2.valid();
			},
			onFinished: function (event, currentIndex)
			{
				alert("Submitted!");

				//axios({
  //url: '/lease/',
  //method: 'POST',
  //responseType: 'blob', // important
//}).then((response) => {
  //const url = window.URL.createObjectURL(new Blob([response.data]));
  //const link = document.createElement('a');
  //link.href = url;
  //link.setAttribute('download', 'file.pdf');
  //document.body.appendChild(link);
  //link.click();

//});

				axios({
					url: '/rental/',
					method: 'POST',
					responseType: 'blob',
					data: {
						Client: {
                            firstName: $('#firstName').val(),
                            lastName: $('#lastName').val(),
                            lastlastName: $('#lastlastName').val(),
                            pass_serial_num: $('#posportcode').val(),
                            Issued_by: $('#addressDetail').val()
                        }
  }

}).then(function(response){
	var blob = new Blob([response.data], {type: "application/pdf;charset=utf-8"});
	//downloadElement.href = URL.createObjectURL(blob);

	saveAs(blob, "contract.pdf");
  const url = window.URL.createObjectURL(new Blob([response.data]));
  //const link = document.createElement('a');
  //link.href = url;
  //link.setAttribute('download', 'file.pdf');
  //document.body.appendChild(link);
  //link.click();
					location.href(url);

});




				//$.ajaxSetup({
				//	headers:
				//		{ 'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content') }
				//});
				//var settings = {
				//	"async": true,
				//	"crossDomain": true,
				//};
				//$.post('/lease/', settings, function(data){
				//	var blob = new Blob([data]);
        //var link = document.createElement('a');
        //link.href = window.URL.createObjectURL(blob);
        //link.download = "Sample.pdf";
        //link.click();
       ///$('.tweets').html(data);
					//console.log(data);
					//var blob = new Blob([data], {type: "application/pdf;charset=utf-8"});
//saveAs(blob, "dc.pdf");
					//var newWindow = window.open("", "new window", "width=200, height=100");

       //write the data to the document of the newWindow
       //newWindow.document.write(data);
					//var blob = new Blob([data], {type: "text/plain;charset=utf-8"});
					//saveAs(blob, "config.json");
					//console.log('Succes');
		//var blob = new Blob([data], { type: 'text/plain' });
  //downloadElement.href = URL.createObjectURL(blob);
		//location.href(data);
    //});
    ///e.preventDefault();

			}
		}).validate({
			errorPlacement: function errorPlacement(error, element) { element.before(error); },
			rules: {
				confirm: {
					equalTo: "#password-2"
				}
			}
		});
	}

	$('#datable_1').DataTable({
		 "bFilter": false,
		 "bLengthChange": false,
		 "bPaginate": false,
		 "bInfo": false,
		  "footerCallback": function ( row, data, start, end, display ) {
				var api = this.api(), data;

				// Remove the formatting to get integer data for summation
				var intVal = function ( i ) {
					return typeof i === 'string' ?
						i.replace(/[\$,]/g, '')*1 :
						typeof i === 'number' ?
							i : 0;
				};

				// Total over all pages
				var total = api
					.column( 3 )
					.data()
					.reduce( function (a, b) {
						return intVal(a) + intVal(b);
					}, 0 );

				// Total over this page
				var pageTotal = api
					.column( 3, { page: 'current'} )
					.data()
					.reduce( function (a, b) {
						return intVal(a) + intVal(b);
					}, 0 );

				// Update footer
				$( api.column( 3 ).footer() ).html(
					'$'+pageTotal
				);
			}
	});

});
