<%-- <%@ include file="header.jsp"%> --%>

 
<style>
#loadingmessage{
	background-color: rgba(255,255,255,0.7);
	height:100%;
	width:100%;
	z-index: 11111;
	margin-top:-100px;
	position: fixed;	
}
.img_div{
	height: 200px;
    width: 200px;
    float: left;
    margin-top: 100px;
    margin-left: 500px;
}
.img_div img{
	height:200px;
	width:200px;
}
 
	
.model {
   display: none; /* Hidden by default */
   position: fixed; /* Stay in place */
   z-index: 1; /* Sit on top */
   padding-top: 250px; /* Location of the box */
   left: 0;
   top: 0;
   width: 100%; /* Full width */
   height: 100%; /* Full height */
   overflow: auto; /* Enable scroll if needed */
   background-color: rgb(0,0,0); /* Fallback color */
   background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
}

/* Modal Content */
.model-content {
   background-color: #fefefe;
   margin: auto;
   padding: 20px;
   border: 1px solid #888;
   width: 80%;
}

/* The Close Button */
.close {
   color: #aaaaaa;
   float: right;
   font-size: 28px;
   font-weight: bold;
}

.close:hover,
.close:focus {
   color: #000;
   text-decoration: none;
   cursor: pointer;
}

/* Style the tab */
.tab {
   overflow: hidden;
   border: 1px solid #ccc;
   background-color: #f1f1f1;
}

/* Style the buttons inside the tab */
.tab button {
   background-color: inherit;
   float: left;
   border: none;
   outline: none;
   cursor: pointer;
   padding: 14px 16px;
   transition: 0.3s;
   font-size: 17px;
}

/* Change background color of buttons on hover */
.tab button:hover {
   background-color: #ddd;
}

/* Create an active/current tablink class */
.tab button.active {
   background-color: blue;
}

/* Style the tab content */
.tabcontent {
   display: none;
   padding: 6px 12px;
   border: 1px solid #ccc;
   border-top: none;
}
.credit {
   display: none;
   padding: 6px 12px;
   border: 1px solid #ccc;
   border-top: none;
}
.cash {
   display: none;
   padding: 6px 12px;
   border: 1px solid #ccc;
   border-top: none;
}
			
	</style>



<section class="attendence_page">
    <div class="container">
         <div class="col-md-12">
             <div class="inner_attendence_container">
                <h4 style="color:#337ab7; font-weight:bold; width:100%; text-align: center;">Create Employee Pay Roll</h4>
                <div id='loadingmessage' style='display:none;'>
                       <div class="img_div"><img src='images/loading.gif'/></div>
                    </div> 
  
  <form id="payrolldata">                   
        <div class="col-md-6">
		 
           <div class="row">
		     <div class="form-group" style="margin-bottom:100px;">
            <label class="control-label col-md-4" style="padding-top:7px; font-weight:100;">No OF Working Days</label>
            <div class="col-md-8">
              <input class="form-control" id="no_days_working" name="no_days_working" type="number" style="margin-bottom:21px;">
            </div> 
          </div> 
          
          <div class="form-group" style="margin-bottom:100px;">
            <label class="control-label col-md-4" style="padding-top:7px; font-weight:100;">No Of Days Worked</label>
            <div class="col-md-8">
              <input class="form-control" id="no_days_worked" name="no_days_worked" type="number"  style="margin-bottom:21px;">
            </div> 
         </div> 
            </div>
             <div class="row">
          <div class="form-group" style="margin-bottom:100px;">
             
               <label class="control-label col-md-4" style="padding-top:7px; font-weight:100;">Select Emp</label>
                 <div class="col-md-8">
                   <select class="form-control" id="emp_id" name="employee" onchange="getSalDetails();" >
                   			
                   </select> 
                 </div>
              
           </div>
        </div> 
          <div class="form-group" style="margin-bottom:100px;">
            <label class="control-label col-md-4" style="padding-top:7px; font-weight:100;">Select Month</label>
            <div class="col-md-8">
              <select class="form-control" id="month" >
                   		<option>SelectMonth</option>
                   		<option value="1">january</option>
                   		<option value="2">february</option>
                   		<option value="3">march</option>
                   		<option value="4">april</option>
                   		<option value="5">may</option>
                   		<option value="6">june</option>
                   		<option value="7">july</option>
                   		<option value="8">august</option>
                   		<option value="9">september</option>
                   		<option value="10">october</option>
                   		<option value="11">november</option>
                   		<option value="12">december</option>                   		
              </select>
            </div> 
          </div>
          
              <div class="row">
                 <div class="form-group" style="margin-bottom:100px;">
            <label class="control-label col-md-4" style="padding-top:7px; font-weight:100;">Basic Pay</label>
            <div class="col-md-8">
              <input class="form-control" id="basic_sal" name="basic_sal" style="margin-bottom:21px;" type="text" value="" readonly="readonly">
            </div> 
                </div>
                
                <div class="form-group" style="margin-bottom:100px;">
            <label class="control-label col-md-4" style="padding-top:7px; font-weight:100;">House Rent Allowance</label>
            <div class="col-md-8">
              <input class="form-control" id="house_rent_allowance" name="house_rent_allowance" style="margin-bottom:21px;" type="text" value="" readonly="readonly">
            </div> 
                </div>
                </div>
                <div class="row">
                <div class="form-group" style="margin-bottom:100px;">
            <label class="control-label col-md-4" style="padding-top:7px; font-weight:100;">Conveyance Allowance</label>
            <div class="col-md-8">
              <input class="form-control" id="conveyance_allowance" name="conveyance_allowance" style="margin-bottom:21px;" type="text" value="" readonly="readonly">
            </div> 
                </div>
           
           </div>
             <br>
           
          </div><!--col md 6-->
          
          <div class="col-md-6">
          
             
          
          
                 <div class="form-group" style="margin-bottom:50px;">
            <label class="control-label col-md-4" style="padding-top:7px; font-weight:100;">ESI</label>
            <div class="col-md-8">
              <input class="form-control" id="esi" name="esi" type="text" value="" readonly="readonly">
            </div>
                </div>
           
                
         <div class="form-group" style="margin-bottom:100px;">
            <label class="control-label col-md-4" style="padding-top:7px; font-weight:100;">PF</label>
           <div class="col-md-8">
              <input class="form-control" id="pf" name="pf" type="text" value="" readonly="readonly" style="margin-bottom:21px;">
            </div>    
                </div>
               
               
                  <div class="form-group" style="margin-bottom:100px;">
            <label class="control-label col-md-4" style="padding-top:7px; font-weight:100;">Prof Tax</label>
            <div class="col-md-8">
              <input class="form-control" id="prof_tax" name="prof_tax" type="text" value="" readonly="readonly" style="margin-bottom:21px;">
            </div>
            
             
                
                <div class="form-group" style="margin-bottom:100px;">
            <label class="control-label col-md-4" style="padding-top:7px; font-weight:100;">Medical Allowance</label>
            <div class="col-md-8">
              <input class="form-control" id="medical_allowance" name="medical_allowance" style="margin-bottom:21px;" type="text" value="" readonly="readonly">
            </div> 
                </div>
                	
                <div class="form-group" style="margin-bottom:100px;">
            <label class="control-label col-md-4" style="padding-top:7px; font-weight:100;">Longevity Bonus</label>
            <div class="col-md-8">
              <input class="form-control" id="longevity_bonus" name="longevity_bonus" type="text" value="0" style="margin-bottom:21px;">
            </div>
                </div>
                
               <div class="row">
                
                <div class="form-group" style="margin-bottom:100px;">
            <label class="control-label col-md-4" style="padding-top:7px; font-weight:100;">Bus Pass Recovery</label>
            <div class="col-md-8">
              <input class="form-control" id="bus_pass_recovery" name="bus_pass_recovery" type="text" value="0" style="margin-bottom:21px;">
            </div>
                </div>
                
                <div class="form-group" style="margin-bottom:100px;">
            <label class="control-label col-md-4" style="padding-top:7px; font-weight:100;">EXGRATIA/BONUS</label>
            <div class="col-md-8">
              <input class="form-control" id="exgratia_bonus" name="exgratia_bonus" type="text" value="0" style="margin-bottom:21px;">
            </div> 
                </div>
                
                </div>
         <div class="row">
                 <div class="form-group" style="margin-bottom:100px;">
            <label class="control-label col-md-4" style="padding-top:7px; font-weight:100;">Daily Rate</label>
            <div class="col-md-8">
              <input class="form-control" id="daily_rate" name="daily_rate" style="margin-bottom:21px;" type="text" value="" readonly="readonly">
            </div> 
                </div>
           </div>
                <div class="form-group" style="margin-bottom:100px;">
            <label class="control-label col-md-4" style="padding-top:7px; font-weight:100;">Performance Incetive</label>
            <div class="col-md-8">
              <input class="form-control" id="performance_incetive" name="performance_incetive" type="text" value="0" style="margin-bottom:21px;">
            </div> 
                </div>
     </div>
     </div>
  </form>
      <div class="col-md-8" align="center">    
        <div class="col-md-4" >
            <button class="btn btn-lg btn-block btn-danger" onclick="add_sal();" style="margin-top:40px; margin-bottom:40px;">Submit</button>
        </div>
      </div>  
</div>
   </div>
     </div>
       </section>
       
  <script type="text/javascript">
  	
  $(document).ready(function() {
	//alert("on ducument ready");
	grabInfo();
  })
  
   //to Create Json Object		
function createJson(formId){
  var out_params = [];
  var elements = document.getElementById(formId).elements;
  alert(elements);
  var obj ={};
  var chk = 0;
  for(var i = 0; i < elements.length ; i++){
       var item = elements.item(i);    
 
          $('input[name="'+item.name+'"]').css('borderBottom','1px solid #3aab83 ');
          obj[item.name] = item.value;
       }
         out_params.push(obj);
         return out_params;
}
  
  
  function add_sal() {
	  			  //alert("at sal");
	  			  var empid=$('#emp_id').val();	
	  			  var month_id=$('#month').val();
	  			  //alert(month_id);
	  			  var json_object=createJson('payrolldata');
	  			  var jason_string=JSON.stringify(json_object);
	  			  
	  			$.ajax({
	  				   type:'GET',
	    		       url:'InsertMonthlyPay',     //servlet
	    		       dataType: 'json',
	    		       data:{data:jason_string, eid:empid, mid:month_id},
	    		       success: function(respo){
	    		    	   
	    		    	   if(respo=='1'){
	    		    		   alert("Pay Slip Generated Succefully :)");
	    		    		   $('#payrolldata')[0].reset();
	    		    	   }
	    		    	   else{
	    		    		   alert("failed :(");
	    		    	      }
	    		       }
	  			})
}
	      
function grabInfo()
{
	  
 	var tbname="emp_details";
 	$.ajax({
 		     type:'GET',
 		     url:'SelectEmployeeNames',
 		     data:{data:tbname},
 		     dataType:'json',
 		     success: function(respo)
		 		    {
 		    	 	   //alert("hi");
 		    	 	   console.log(respo);
 		    	       var html_str ='';
 		    	        html_str='<option >employee list</option>';
 		    	       for(var i=0; i< respo.length; i++)
 		    	       {
 		    	    	  html_str= html_str+ '<option value="'+respo[i].emp_id+'">'+respo[i].name+'</option>';
 		    	       }//forloop
 		    	       	 
 		    	       $('#emp_id').html(html_str);           	
 		    	       	     
		 		    }//end of success
 	      })//end of ajax
}   //end of the function 	      
 
 function getSalDetails() {
	
	var emp_id=$('#emp_id').val();
	//alert(emp_id);
	 $.ajax({
		     type:'POST',
		      url:'SelectEmpSal',
		      data:{data:emp_id},
		      dataType:'json',
		      success: function(respo) {
		    	  
		    	     var gross_sal;
		    	     var basic_salary;
		    	     var con_allow;		    	     
		    	     var esi;
		    	     var proff_tax;
		    	     var med_tax;
		    	     var house_ren;
		    	     var no_of_workingdays=$('#no_days_working').val();
		    	     var no_of_days_worked=$('#no_days_worked').val();
		    	     
		    	     //response from selectEmpSal servlet
		    	  	var sal=respo[0].salDetails;
		    	  	
		    	  	var salArray=JSON.parse(sal);
		    	  	for(var i=0;i<salArray.length;i++){
		    	  		
		    	  		//gross_sal
		    	  		 var gross_salary   =salArray[i].grossSal;
		    	  			daily_rate   =Math.trunc((gross_salary/no_of_workingdays));
		    	  			
		    	  			//alert(daily_rate);
		    	  			//gross sal based on number of days worked
		    	  			gross_sal=(daily_rate*no_of_days_worked);
		    	  			
		    	  			//alert(gross_sal);
		    	  		  
		    	  	 basic_salary_perc=salArray[i].basic_sal;
		    	  	           pf_perc=salArray[i].pf
		    	  	    house_ren_perc=salArray[i].house_ren ;
		    	  	          esi_perc=salArray[i].esi;
		    	  		  con_allow   =salArray[i].con_allow;		    	  		  
		    	  		 
		    	  		  //proff_tax   =salArray[i].prof_tax;
		    	  		  med_tax     =salArray[i].medic_allow;
		    	  		 
		  professsional_tax_percentage=salArray[i].professional_Tax_Perc; 
		    	  		 
		    	  		  //caliculationa per one working day
		    	  		  //Math.trunc function is used to convert float to int
		    	  		  
		    	  		  var dailyrate    =Math.trunc(gross_sal/no_of_workingdays);
		    	  		  
		    	  	  /*     basic_salary=Math.trunc(gross_sal*basic_salary_perc)/100;	    	  		       
		    	  		  var day_basic_sal=Math.trunc(basic_salary/no_of_workingdays); */
		    	  		  
		    	  		 // var houseRent    =(day_basic_sal*no_of_days_worked)*0.4
		    	  		 //var day_con_allow=Math.trunc(con_allow/no_of_workingdays);		    	  		  
		    	  		  //var day_esi      =Math.trunc(esi/no_of_workingdays);;
		    	  		  //var day_proff_tax=Math.trunc(proff_tax/no_of_workingdays);
		    	  		 // var day_med_tax  =Math.trunc(med_tax/no_of_workingdays);
		    	  		 // var day_house_ren=Math.trunc(house_ren/no_of_workingdays);
		    	  		  
		    	  		  //caliculations for no of days worked
		    	  		  var w_basic_sal= Math.trunc((gross_sal*basic_salary_perc)/100);
		    	  		  
		    	  		  //var w_basic_sal=  day_basic_sal*no_of_days_worked;
		    	  		  var w_professional_tax_amount=Math.trunc((w_basic_sal*professsional_tax_percentage)/100);
		    	  		 // var w_con_allow=  day_con_allow*no_of_days_worked;
		    	  		 // var w_esi      =  day_esi*no_of_days_worked;
		    	  		 // var w_proff_tax=  day_proff_tax*no_of_days_worked;
		    	  		  //var w_med_tax  =  day_med_tax*no_of_days_worked;
		    	  		  var w_house_ren=  Math.trunc((w_basic_sal*house_ren_perc)/100);
		    	  		         var w_pf=  Math.trunc((w_basic_sal*pf_perc)/100);
		    	  		              esi=  Math.trunc((gross_sal*esi_perc)/100);
		    	  		   
		    	  		
		    	  		  $('#basic_sal').val(w_basic_sal);
		    	  		  $('#daily_rate').val(dailyrate);
		    	  		  $('#house_rent_allowance').val(w_house_ren);
		    	  		  $('#conveyance_allowance').val(con_allow);
		    	  		  $('#esi').val(esi);
		    	  		  if(gross_sal>15000)
		    	  			  {
		    	  			    $('#pf').val(w_pf);
		    	  			  }
		    	  		  else{
		    	  			    $('#pf').val(0);
		    	  		      }
		    	  		  //$('#pf').val(w_pf);
		    	  		  $('#prof_tax').val(w_professional_tax_amount);
		    	  		  $('#medical_allowance').val(med_tax);
		    	  	  
		    	  	}
			}
		    	  
	 })
}
function openModel()
{
    var modal = document.getElementById('myModal');

    // Get the button that opens the modal
    //var btn = document.getElementById("myBtn");

    // Get the <span> element that closes the modal
    

    // When the user clicks the button, open the modal 
    
        modal.style.display = "block";
    

    // When the user clicks on <span> (x), close the modal
        openDiv('Cash');
}

function closeModel()
{
    var modal = document.getElementById('myModal');
     modal.style.display = "none";
}
</script>    