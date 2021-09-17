$(document).ready(function(){
 $('.a_menu a').on('click', function(e){  
    e.preventDefault( );
    var pageRef = $(this).attr('href');
  
    callpage(pageRef)

});
function callpage(pageRefInput){
$.ajax({	
	url:pageRefInput,
	type:"GET",
	dataType:"text",
	success: function(response){
		//console.log('page was loaded', response);
		$('#get_page').html(response);
	},
	error:function(error){
		//console.log('The page was not loaded', error);
	},
	complete:function(xhr, status){
		//console.log('request was completed');
	}

});
};
//button mark attendence



$('#save_data').on('click',function(){
			var vals = createJson('cust_form');
			console.log('Result:\t'+JSON.stringify(vals));
			if(vals == null){
				alert('Please fill all fields!');
			} else{
								/*$.ajax({
					type: 'POST',
					url : 'FetchDetails',
					dataType: "json",
					data : {data:vals},
					success : function(respo) {
						var drop = '';
						for(var i = 0; i< respo.length; i++){
							drop = drop+'<option value="'+respo[i].con_id+'">'+respo[i].con_name+'</option>';
						}
						$('#sub_ad_cl').html(drop);					
					}
					
				});*/
			}
		});
 function createJson(formId){
    var out_params = [];
    var elements = document.getElementById(formId).elements;
    var obj ={};
    var chk = 0;
	console.log(formId);
    for(var i = 0; i < elements.length ; i++){
        var item = elements.item(i);
        if(item.value.length <= 0){
            $('input[name="'+item.name+'"]').css('borderBottom','1px solid #FF5722 ');
            return null;            
        }
        else{
            $('input[name="'+item.name+'"]').css('borderBottom','1px solid #3aab83 ');
            obj[item.name] = item.value;
        }    
    }
    out_params.push(obj);            
    return out_params;
}

});

//


