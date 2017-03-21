/* Sehgal, Priyanka
java script for login page */

$(document).ready(function() {
	$("[name='user']").val('');
	$("[name='user']").focus();

	$('#login').on('click', function(){
	var message = "";
	var user= document.getElementById('user').value;
	var password=document.getElementById('password').value;
    $.ajax({
        type: 'POST',
        url: '/perl/jadrn045/proj1/login1.cgi',
        data: {'username': user,
                'password':password
            },
        success: function(res) {
        	if (res == 1)
            	$("#main").load("cosmetic.html");
            else
            {
            	$('#status5').text("Invalid username or password");
            	document.getElementById("user").value="";
            	document.getElementById("password").value="";
            }
        },
        error: function() {
            $('#status5').text("Some error occurred");
//         $('#delete_submit').prop('disabled',true);
        }
    });

	});
	});
