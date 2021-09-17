<%-- <%@ include file="header.jsp"%> --%>

 
<style>

@media print {
 body * {
   visibility: hidden;
 }
 #section-to-print, #section-to-print * {
   visibility: visible;
 }
 #section-to-print {
   position: absolute;
   left: 0;
   top: 0;
 }
}
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

</style>

  <section class="attendence_page">
    <div class="container">
                       <div class="col-md-12">
                         <div class="inner_attendence_container">
                       <div class="col-md-10">  
                         <h4 style="color:black; font-weight:bold; width:100%;text-align: center;"><b>Pay Slip</b></h4>
                        </div>
                        <div id='loadingmessage' style='display:none;'>
                       <div class="img_div"><img src='images/loading.gif'/></div>
                    </div>
                        <div class="col-md-2">
                          <!-- <button type="button" onclick="printDiv('content_pdf')" class="btn-primary  excell_cus">Generate PDF</button>
                     -->   
                     
             <button type="button" onclick="PrintElem('content_pdf')" class="btn btn-primary  excell_cus">Generate PDF</button>
                     
                     </div>
                     </div>
                     </div><br>
                     <div class="row">
                     <div class="form-group" style="margin-bottom:100px;">
                 <div class="col-md-4">
                    <form>                  
                           <label class="control-label col-md-4" style="padding-top:7px; font-weight:100;">Select Emp</label>
				           <div class="col-md-8">
				           <select class="form-control" id="emp_name" name="employees" onchange="getPayRollMonth()"> 
				           
				           </select>                   
				           </div>       				         	      
                     </form>
                  </div>
                 <div class="col-md-4">
                  <label class="control-label col-md-4" style="padding-top:7px; font-weight:100;">Select Month</label>
             <div class="col-md-8">
              <select class="form-control" id="month" onchange="emp_record();">
                   	                  		
              </select>
            </div>  
         </div>
         </div>
         </div>
                  
    <div id="content_pdf">  
             <div>
             <img alt="" src="images/logovenkat.jpg" style="float:left;" height="150px">
            <h2 style="margin-left:15px; font-weight:bold; text-align:center;">
             <!--  MDCO Consultancy services LLP,<br>
              Mascot 90*,Vydehi Epip,WhiteField,<br> 
              Bangalore-66,Phone:8861439034,<br>
              Email-id: aamir@mdcoreone.com, Web:www.mdcoreone.com. -->
            
            </h2> 
            </div>
            <br><br>
                <!-- <h4 style="color:#337ab7; font-weight:bold; float:left; width:100%;">Pay Slip For The Month Of <span id="month_emp"></span></h4>
                 -->
                                   <table  border="" class="table" style="width:100%;">
                                  
                                    <tr>
                                       <th>Name:</th>
                                       <td id="name_emp"></td>
                                       <th>PANç</th>
                                       <td id="pan_emp"></td>
                                    </tr>
                                     <tr>
                                       <th>Employee Id:</th>                                       									 
                                       <td id="emp_id"></td>
                                       <th>Working Days</th>
                                       <td id="no_of_work_days" ></td>
                                    </tr>
                                     <tr>
                                       <th>Designation</th>
                                       <td id="designation_emp"></td>
                                       <th>Days Payable</th>
                                       <td id="no_of_work_days_pay"></td>
                                    </tr>
                                     <tr>
                                       <th>Band</th>
                                       <td id="band_no_emp"></td>
                                       <th>PF NO.</th>
                                       
                                       <td id="pf_no_emp"></td>
                                       
                                    </tr>
                                    <tr>
                                       <th>Level</th>
                                       <td id="level_emp"></td>
                                       <th>Bank Acc No</th>
                                       <td id="act_no_emp"></td>
                                    </tr>
                                    <tr>
                                       <th>Location</th>
                                       <td id="city_emp"></td>
                                       <th>Gross Salary</th>
                                       <td id="emp_grossSal"></td>
                                    </tr>
                                    <tr>
                                       <th>Bank Name</th>
                                       <td id="bank_name_emp"></td>
                                       <th>Month</th>
                                       <td id="monthname"></td>
                                    </tr>
                                 
                            
                                 </table>
                                 
                              <!--3rd table-->
                              
                              
                               <table align="left" border="1" class="table  table-bordered" style="width:100%;">
                                 
                                    <tr>
                                       <th>Earnings</th>
                                       <th>Rs</th>
                                     <!--   <td id="earnings"></td>  -->
                                       <th>Deductions</th>
                                       <th>Rs</th>
                                    </tr>
                                     <tr>
                                       <td>Basic pay</td>
                                       <td id="basic_pay_emp"></td>
                                       <td>Bus Pass Recovery</td>
                                       <td id="bus_pass_emp"></td>
                                    </tr>
                                     <tr>
                                       <td>House Rent Allowance</td>
                                       <td id="house_rent_emp"></td>
                                       <td>Provident Fund</td>
                                       <td id="pf_emp"></td>
                                    </tr>
                                     <tr>
                                       <td>Conveyance AllowanceÜ</td>
                                       <td id="conveyance_emp"></td>
                                       <td>Prof TaxÜ</td>
                                       <td id="prof_tax_emp"></td>
                                    </tr>
                                    <tr>
                                       <td>Special Allowance</td>
                                       <td id="spc_emp"></td>
                                       <td>ESI</td>
                                       <td id="esi_emp"></td>
                                    </tr>
                                    <tr>
                                       <td>Medical Allowance</td>
                                       <td id="medical_alowance_emp"></td>
                                       <td></td>
                                       <td></td>
                                    </tr>
                                    <tr>
                                       <td>Performance Incentive</td>
                                       <td id="prof_incetive"></td>
                                       <td></td>
                                       <td></td>
                                    </tr>
                                    <tr>
                                       <td>EXGRATIA/BONUS</td>
                                       <td id="bonus_emp"></td>
                                       <td></td>
                                       <td></td>
                                    </tr>
                                    <tr>
                                       <td>Longevity Bonusç</td>
                                       <td id="longvity_emp"></td>
                                       <td></td>
                                       <td></td>
                                    </tr>
                                    <tr>
                                       <th>Total Earnings</th>
                                       <td id="total_earning"></td>
                                       <th>Total DeductionsÅ</th>
                                       <td id="total_deduction"></td>
                                    </tr>
                                    <tr>
                                       <th></th>
                                       <td></td>
                                       <th>Net Salary</th>
                                       <td id="net_salary_emp"></td>
                                    </tr>
                                
                                 
                                 
                                  </table>  
                                </div><!--content pdf download--> 
                         </div><!--/attendence container-->
                         <div id="editor"></div>
                       </div><!--/col-md-12-->
  </div><!--container-->
</section><!--/attendence page-->
<script type="text/javascript" src="https://cdn.jsdelivr.net/jspdf/1.2.61/jspdf.min.js"></script>
<script>

function printDiv(content_pdf) {
     var printContents = document.getElementById("content_pdf").innerHTML;
     var originalContents = document.body.innerHTML;

     document.body.innerHTML = printContents;

     window.print();

     document.body.innerHTML = originalContents;
}


/*var doc = new jsPDF('p','pt', 'a4');
var specialElementHandlers = {
    '#editor': function (element, renderer) {
        return true;
    }
};

$('#cmd').click(function () {
    doc.fromHTML($('#content_pdf').html(), 4, 4, {
        'width': 100,
            'elementHandlers': specialElementHandlers
    });
    doc.save('<?php echo 'payslip_aug_2017'; ?>.pdf');
});*/
</script>
<?php require 'footer.php' ?>

<script>
 $(document).ready(function() {
								//alert("on document ready....")
								grabInfo();
                              })
	      
function grabInfo()
{
	 
 	 
 	$.ajax({
 		     type:'GET',
 		     url:'SelectAllEmployeeNames',
 		     data:{},
 		     dataType:'json',
 		     success: function(respo)
		 		    {
 		    	 	   //alert("hi");
 		    	 	   console.log(respo);
 		    	       var html_str ='';
 		    	        html_str='<option >'+'employee list'+'</option>';
 		    	       for(var i=0; i< respo.length; i++)
 		    	       {
 		    	    	  html_str= html_str+ '<option value="'+respo[i].emp_id+'">'+respo[i].name+'</option>';
 		    	       }//forloop
 		    	       	 
 		    	       $('#emp_name').html(html_str);           	
 		    	       	     
		 		    }//end of success
 	      })//end of ajax
}   //end of the function 

function getPayRollMonth() {
	var empid=$('#emp_name').val();
	//alert(empid);
	$.ajax({
			 type:'GET',
		     url:'GetEmployeePayrollMonths',
		     data:{data:empid},
		     dataType:'json',
		     success: function(respo){
		    	 
		    	 						 var html_str='' 
		    	 						  html_str='<option>Select Month</option>';
		    	 						 for(i=0;i<respo.length;i++)
		    	 							 {
		    	 							   html_str= html_str+ '<option value="'+respo[i].monthID+','+respo[i].monthName+'">'+respo[i].monthName+'</option>';
		    	 							 }
		    	 						 $('#month').html(html_str);
		                              }
	      })
}


function emp_record() {
		var emp_id=$('#emp_name').val();
		var month=$('#month').val();
		 
		var month_id=month.split(",")[0];
		var monthname=month.split(",")[1];
		//alert(emp_id);
      //alert("at selecting employee");
	    
      $.ajax({
	        	 type:'GET',
			     url:'GetEmployeeById',
			     data:{data:emp_id,mid:month_id},
			     dataType:'json',
			     success: function(respo){
								    	  /*   $('#name_emp').html(respo[0].name);
								    	   $('#emp_id').html(respo[0].empId);
								    	   $('#designation_emp').html(respo[0].designation);
								    	   $('#band_no_emp').html(respo[0].band);
								    	   $('#level_emp').html(respo[0].level);
								    	   $('#pan_emp').html(respo[0].pan);
								    	   $('#pf_no_emp').html(respo[0].pfno);  */ 
								    	   
								    	   
								    	   var emp=respo[0].empDeatails;
								    	   var sal=respo[0].salDetails;
								    	   var bank=respo[0].bankDetails;
								    	   
								    	   var empArray=JSON.parse(emp); //converts string in to JSON Object
								    	   var salArray=JSON.parse(sal);
								    	   var bankArray=JSON.parse(bank);
								    	   
								    	   if(salArray[0]==null)
								    		   {
								    		   		alert("Hi! your pay slip is not generated for the selected month :(");
								    		   }
								    	   else{
								    		   
								    	   
								    		var gross_sal;		
								    		$('#monthname').html(monthname);
	                                 	    for(var i=0;i<empArray.length;i++)
	                                 	       {
								    		       $('#name_emp').html(empArray[i].name);
								    			   $('#emp_id').html(empArray[i].empId);
										    	   $('#designation_emp').html(empArray[i].designation);
										    	   $('#band_no_emp').html(empArray[i].band);
										    	   $('#level_emp').html(empArray[i].level);
										    	   $('#pan_emp').html(empArray[i].pan);
										    	   $('#pf_no_emp').html(empArray[i].pfno);
										    	   $('#emp_grossSal').html(empArray[i].grossSal);
										    	   //alert(empArray[i].grossSal);
										    	   gross_sal=empArray[i].grossSal;
								    	       }
	                                 	    
	                                 	     
	                                 	    for(var i=0;i<salArray.length;i++)
	                                 	    	{
	                                 	    	   
	                                 	    	  $('#no_of_work_days').html(salArray[i].workingDays);
	                                 	    	  $('#no_of_work_days_pay').html(salArray[i].workedDays);
	                                 	    	  $('#house_rent_emp').html(salArray[i].houseAllow);
	                                 	    	  $('#conveyance_emp').html(salArray[i].conveyAllow);
	                                 	    	  $('#bonus_emp').html(salArray[i].exgratiaBonus);
	                                 	    	  $('#esi_emp').html(salArray[i].esi);
	                                 	    	  $('#pf_emp').html(salArray[i].pf);
	                                 	    	  $('#prof_tax_emp').html(salArray[i].profTax);
	                                 	    	  $('#medical_alowance_emp').html(salArray[i].medicAllow);
	                                 	    	  $('#longvity_emp').html(salArray[i].longBonus);
	                                 	    	  $('#bus_pass_emp').html(salArray[i].busspassRecovery);
	                                 	    	  $('#prof_incetive').html(salArray[i].performanceIncentive);
	                                 	    	  $('#basic_pay_emp').html(salArray[i].basicSal);
	                                 	    	  //$('#spc_emp').html(salArray[i].specialAllow);
	                                 	    	  
	                                 	    	   
	                                 	    	 /* caliculations for getting gross sal based on esi
	                                 	    	  esi=(1.7*grosssal)/100 */
	                                 	    	  
	                                 	    	  //var gross_sal=Math.trunc((salArray[i].esi*100)/1.7);
	                                 	    	 // var special_allow=Math.trunc(gross_sal-(salArray[i].basicSal+salArray[i].houseAllow+salArray[i].conveyAllow+salArray[i].medicAllow));
	                                 	    	  
	                                 	    	 var dailyRate=Math.trunc((gross_sal/salArray[i].workingDays));
	                                 	    	 var Gross_salary=(dailyRate*salArray[i].workedDays);
	                                 	    	 
	                                 	    	// alert(Gross_salary);
	                                 	    	var special_allow=Math.trunc(Gross_salary-(salArray[i].basicSal+salArray[i].houseAllow+salArray[i].conveyAllow+salArray[i].medicAllow));
	                                 	    	 
	                                 	    	 $('#spc_emp').html(special_allow);
	                                 	    	 $('#emp_grossSal').html(gross_sal);
	                                 	    	 

	                                 	    	
	                                 	    	  
	                                 	    	 /*  var dailyRate=salArray[i].dailyPay;
	                                 	    	  var daysWorked=salArray[i].workedDays;
	                                 	    	  var basic_pay=(dailyRate*daysWorked);
	                                 	    	  $('#basic_pay_emp').html(basic_pay); */
	                                 	    	 
	                                 	    	  var TotalEarnings=(salArray[i].basicSal + salArray[i].houseAllow+salArray[i].conveyAllow +special_allow+ salArray[i].medicAllow+salArray[i].performanceIncentive+salArray[i].exgratiaBonus+salArray[i].longBonus);
	                                 	    	  
	                                 	    	  $('#total_earning').html(TotalEarnings);
	                                 	    	  
	                                 	    	  //var bussPassRecovery=1200.0;
	                                 	    	  var TotalDeductions=(salArray[i].busspassRecovery+salArray[i].pf+salArray[i].profTax+salArray[i].esi);
	                                 	    	   
	                                 	    	  $('#total_deduction').html(TotalDeductions);
	                                 	    	  
	                                 	    	  var netsalary=(TotalEarnings-TotalDeductions);
	                                 	    	  
	                                 	    	  $('#net_salary_emp').html(netsalary);
	                                 	    	 
	                                 	    	}
	                                 	    
	                                 	    
	                                 	    for(var i=0;i<bankArray.length;i++)
	                                 	    	{
		                                 	    	$('#bank_name_emp').html(bankArray[i].bankName);
		                                 	    	$('#act_no_emp').html(bankArray[i].accNo);	                                 	    	
	                                 	        }
								    	   }//end of else
			     }    
								    	  			     
            })
	
} //end of the function	   

function PrintElem(elem)
{
   var mywindow = window.open('', 'PRINT', 'height=800,width=600');

  // mywindow.document.write('<html><head><title>' + document.title  + '</title>');
   mywindow.document.write('</head><body >');
 //  mywindow.document.write('<h1>' + document.title  + '</h1>');
   mywindow.document.write(document.getElementById(elem).innerHTML);
   mywindow.document.write('</body></html>');

   mywindow.document.close(); // necessary for IE >= 10
   mywindow.focus(); // necessary for IE >= 10*/

   mywindow.print();
   mywindow.close();

   return true;
}


</script>

 

 
			
						
		
		
		

		
		
				
	

				


	
	

	
				

				
						
 

				
					
				

								

				
					
					
					
				

				
					
				

				

				
					
												

