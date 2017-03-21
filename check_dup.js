/* Sehgal, Priyanka 
java script for checking duplicates

*/
$(document).ready(function() {

    $.get("/perl/jadrn045/proj1/fetch_category.cgi",category_a);
    $.get("/perl/jadrn045/proj1/fetch_vendor.cgi",vendor_a);




    $("#sku").on('blur',function(e) {
        var url = '/perl/jadrn045/proj1/check_dup_sku.cgi?sku=';
        url += $("#sku").val();
       $('#busy_wait').css('visibility','visible');
       $.get(url, data_handle);
        });

    $('#a_submit').on('click', function() {
        var sku = document.getElementById('sku').value;
        var category = document.getElementById('category').selectedIndex;
        var  vendor= document.getElementById('vendor').selectedIndex;
        var  vendorModel= document.getElementById('vendorModel').value;
        var  description= document.getElementById('description').value;
        var  features= document.getElementById('features').value;
        var  cost= document.getElementById('cost').value;
        var  retail= document.getElementById('retail').value;
        var  product_image= 'default.img';
        data_insert(sku,category,vendor,vendorModel,description,features,cost,retail,product_image);
    });
});

function data_insert(sku,category,vendor,vendorModel,description,features,cost,retail,product_image) {
    var message = "";
    $.ajax({
        type: 'POST',
        url: '/perl/jadrn045/proj1/insert_record.cgi',
        data: {'sku': sku,
                'category':category,
               'vendor':vendor,
               'vendorModel':vendorModel,
               'description':description,
               'features':features,
               'cost':cost,
               'retail':retail,
               'product_image':product_image
            },
        success: function(res) {
            message = res.result;
            document.getElementById('status').innerHTML = message;
            $('input[type="text"]').val('');
            document.getElementById('category').selectedIndex=0;
            document.getElementById('vendor').selectedIndex=0;
        },
        error: function() {}
    });


}

function data_handle(response){
    $('#busy_wait').css('visibility','hidden');


    if(response.startsWith("duplicate")){
        $('#status').text("This record appears to be a duplicate.");
         $('#add_submit').prop('disabled',true);
    }

    else if(response.startsWith("ok")) {

        $('#add_submit').prop('disabled',false);
    }

}

function category_a(response) {

    var toWrite = "<option value=\"-1\">Select Category</option>";
    var tmpStr = response.split("||");
    for(i=0; i<tmpStr.length; i++) {
        tmp = tmpStr[i].split("=");
        toWrite += "<option value=" + tmp[0] + ">"+tmp[1]+"</option>\n";
        }
    $('#category').append(toWrite);
    }

function vendor_a(response) {

    var toWrite = "<option value=\"-1\">Select Vendor</option>";
    var tmpStr = response.split("||");
    for(i=0; i<tmpStr.length; i++) {
        tmp = tmpStr[i].split("=");
        toWrite += "<option value=" + tmp[0] + ">"+tmp[1]+"</option>\n";
        }
    $('#vendor').append(toWrite);
    }


