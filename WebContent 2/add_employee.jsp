<%-- <%@ include file="header.jsp"%> --%>

<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Admin panel</title>
<!--bootstrap cdn-->
	<link rel="stylesheet" type="text/css" href="css/style.css">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" />
    <link rel="stylesheet" href="https://cdn.datatables.net/1.10.15/css/jquery.dataTables.min.css" />
    <link rel="stylesheet" href="https://cdn.datatables.net/select/1.2.2/css/select.bootstrap.min.css" />
	
	<!--calender-->

<link href="http://fonts.googleapis.com/css?family=Economica" rel="stylesheet" type="text/css">
    <!-- Bootstrap -->
    <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.0.3/css/bootstrap.min.css">
    <!-- Respomsive slider -->
    <link href="css/responsive-calendar.css" rel="stylesheet">

<!--calender-->	
	
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script type="text/javascript" src="https://code.jquery.com/jquery-1.12.4.js"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/1.10.15/js/jquery.dataTables.min.js"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/1.10.15/js/dataTables.bootstrap.min.js"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/select/1.2.2/js/dataTables.select.min.js
"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

    <script type="text/javascript" src="js/attendence.js"></script>
		<script type="text/javascript" src="https://code.jquery.com/ui/1.12.0/jquery-ui.js"></script>
	<script src="js/jquery.btechco.excelexport.js"></script>
    <script src="js/jquery.base64.js"></script>

	<style type="text/css">
	
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
	
<!--/bootstrap cdn-->
<!--font awsome cdn-->
     <script src="https://use.fontawesome.com/23afa7f77a.js"></script>
<!--/font awsome cdn-->
</head>
<script>
$(document).ready(function() {
    $("#example").dataTable({
		"scrollX": true,
		"pagingType": "numbers",
        "processing": true,
        "serverSide": true,
        "ajax": "attendence.php"
    } );
} );

//time
var myVar = setInterval(myTimer, 1000);

function myTimer() {
    var d = new Date();
    document.getElementById("demo").innerHTML = d.toLocaleTimeString();
}
</script>

<body class="default">
      <!-- <header id="" class="navbar-fixed-top scroll-hide">
	        <div class="container-fluid" style="padding:0;"> 
			   <div class="logo_panel">
		            <div class="logo_box">
				     <img src="images/logo_md.jpg" alt="Logo" height="190%" width="110%">

					</div>/logo box	
					<div align="center">
						<b style="padding-right: 200px;padding-top: 20px">
							Mascot90* 1st floor, Vydehi Epip, Whitefield, Bangalore - 66,
							Phone:8861439034,
						</b>					
					</div>	
					<div align="center">							 
						<b style="padding-right: 200px">						     
							Email id: aamir@mdcoreone.com,
							Web : Www.mdcoreone.com</b>
					</div>
					<div class="right_panel">
					  <div id="demo" class="time_style"></div>
					  <div class="user_pic">
					      <img src="images/user.png" alt="user">
					  </div>/user pic
					<ul class=" nav_custom navbar-nav">
					  <li class="dropdown"><a class="dropdown-toggle a_custom" data-toggle="dropdown" href="under_construction.php" style="padding:0; margin:0; line-height:7px; text-decoration:none;">
							<br>
								<p style="font-size:14px; font-weight:600">Admin<span class="caret"></span></p></a>
                              <ul class="dropdown-menu">
                                  <li><a href="#"><i class="fa fa-user" aria-hidden="true"></i>&nbsp;&nbsp;&nbsp; Profile</a></li>
                                  <li><a href="#"><i class="fa fa-lock" aria-hidden="true"></i>&nbsp;&nbsp;&nbsp; Change Password</a></li>
								  <li><a href="#"><i class="fa fa-bed" aria-hidden="true"></i>&nbsp;&nbsp;&nbsp;  Holidays</a></li>
								  <li><a href="#"><i class="fa fa-exclamation-triangle" aria-hidden="true"></i> &nbsp;&nbsp;&nbsp; Notice Board</a></li>
								  <li><a href="#"><i class="fa fa-briefcase" aria-hidden="true"></i>&nbsp;&nbsp;&nbsp; Office Management</a></li>
								  <li><a href="#"><i class="fa fa-cog" aria-hidden="true"></i>&nbsp;&nbsp;&nbsp; Setting</a></li>
								   <li><a href="#"><i class="fa fa-sign-out" aria-hidden="true"></i>&nbsp;&nbsp;&nbsp; Logout</a></li>
                              </ul>
                            </li>
					     </ul>
					</div>
			   </div>/logo panel
	        </div>/container class
	nav bar
	       <div class="container-fluid" style="padding:0;">
			  <div class="nav_panel">
				         boostrap menu coding
					       <nav class="nav_panel_inner">
                          <ul class="nav navbar-nav">
                                  <li class="active"><a href="home.jsp">
								     <i class="fa fa-tachometer" aria-hidden="true" style="vertical-align:center; margin-left:20px;                                         font-size:28px; color:#000;">
									 </i><br>
								        <p style="font-size:14px;">Dashboard</p>
								  </a></li>
								  
								  <li class="active"><a href="add_employee.jsp">
								     <i class="fa fa-users" aria-hidden="true" style="vertical-align:center; margin-left:20px;                                         font-size:28px; color:#000;">
									 </i><br>
								        <p style="font-size:14px;">Employees</p>
								  </a></li>
								  
								  
								  <li class="active"><a href="under_construction.php">
								     <i class="fa fa-building" aria-hidden="true" style="vertical-align:center; margin-left:28px;                                         font-size:28px; color:#000;">
									 </i><br>
								        <p style="font-size:14px;">Departments</p>
								  </a></li>
								  
								  
								  <li class="active"><a href="payroll.jsp">
								     <i class="fa fa-list-alt" aria-hidden="true" style="vertical-align:center; margin-left:7px;                                         font-size:28px; color:#000;">
									 </i><br>
								        <p style="font-size:14px;">Payroll</p>
								  </a></li>
								  
								  
                             <li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="under_construction.php">
							 <i class="fa fa-calendar" aria-hidden="true" style="vertical-align:center; margin-left:63px; font-size:28px; color:#000;">
							 </i><br>
								<p style="font-size:14px;">Attendences and leaves <span class="caret"></span></p></a>
                              <ul class="dropdown-menu">
                                  <li><a href="attendence_2.php">Attendence</a></li>
                                  <li><a href="#">Leaves</a></li>
                              </ul>
                             </li>
                             <li class="active"><a href="under_construction.php">
							    <i class="fa fa-book" aria-hidden="true" style="vertical-align:center; margin-left:9px; font-size:28px; color:#000;">
								</i><br>
								    <p style="font-size:14px;">Claims</p>
							</a></li>
							
							 <li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="#">
							 <i class="fa fa-list-ol" aria-hidden="true" style="vertical-align:center; margin-left:12px; font-size:28px; color:#000;">
							 </i><br>
								<p style="font-size:14px;">Reports <span class="caret"></span></p></a>
                              <ul class="dropdown-menu">
                                  <li style="font-size:14px;"><a href="payroll_slip.jsp">Employee based payslip report</a></li>
                                  <li style="font-size:14px;"><a href="under_construction.jsp">Yearly payslip report</a></li>
                              </ul>
                             </li>
							<li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="#">
							 <i class="fa fa-sign-out" aria-hidden="true" style="vertical-align:center; margin-left:12px; font-size:28px; color:#000;">
							 </i><br>
							 	<li><a href="login.jsp"></a></li>
								<p style="font-size:14px;">Sign Out</p></a>
                              <ul class="dropdown-menu">
                                  <li style="font-size:14px;"><a href="login.jsp">Logout</a></li>
                              </ul>
                             </li>	  
								  
                         </ul>
                    </nav>
  
						 
						 /boostrap menu coding
	          </div>/nav_panel
		   </div>/container
	/nav bar
			
	  </header> -->
	  
<div id="myModal" class="model">

 <!-- Modal content -->
 
 <!-- ===============================================================================-->
	   <div class="model-content">
		   <span class="close" onclick="closeModel()">&times;</span>
		   <h3 ><b>Enter Percentage</b></h3><br>
		   <div>		   		 
		   		
				<div class="form-group" style="margin-bottom:30px;">
		            <label class="control-label col-md-2" style="padding-top:7px; font-weight:100;">Basic Sal</label>
		            <div class="col-md-3">
		              <input class="form-control" name="basic_Sal_Perc" type="number"  id="basic_Sal_Perc" placeholder="Enter Percentage" ><br>
		            </div>
		          <div class="form-group">
		            		<label class="control-label col-md-2" style="padding-top:7px; font-weight:100;">percent of Gross Sal</label>
		            </div> 
		             <span style="color:#d43f3a">
		                         *
		             </span>
		            <div class="col-md-3">
		              <input class="form-control" name="basic_Sal" type="number"  id="basic_Sal" placeholder="Basic Salary"  readonly="readonly"><br>
		            </div>
		                 
                </div><br>
                
                <div class="form-group" style="margin-bottom:30px;">
		            <label class="control-label col-md-2" style="padding-top:7px; font-weight:100;">Providunt Fund</label>
		            <div class="col-md-3">
		              <input class="form-control" name="providunt_fund_perc" type="number"  id="providunt_fund_perc" placeholder="Enter Percentage" ><br>
		            </div>
		          <div class="form-group">
		            		<label class="control-label col-md-2" style="padding-top:7px; font-weight:100;">percent of Basic Sal</label>
		            </div> 
		             <span style="color:#d43f3a">
		                         *
		             </span>
		           <div class="col-md-3">
		              <input class="form-control" name="providunt_fund" type="number"  id="providunt_fund" placeholder="provident Fund" readonly="readonly" ><br>
		            </div>      
		                 
                </div><br>
                
                <div class="form-group" style="margin-bottom:30px;">
		            <label class="control-label col-md-2" style="padding-top:7px; font-weight:100;">House Rent</label>
		            <div class="col-md-3">
		              <input class="form-control" name="House_rent_perc" type="number"  id="House_rent_perc" placeholder="Enter Percentage" ><br>
		            </div>
		          <div class="form-group">
		            		<label class="control-label col-md-2" style="padding-top:7px; font-weight:100;">percent of Basic Sal</label>
		            </div> 
		             <span style="color:#d43f3a">
		                         *
		             </span>		            
		            <div class="col-md-3">
		              <input class="form-control" name="House_rent" type="number"  id="House_rent" placeholder="House Rent" readonly="readonly" ><br>
		            </div>		                 
                </div><br>
                
                 <div class="form-group" style="margin-bottom:30px;">
		            <label class="control-label col-md-2" style="padding-top:7px; font-weight:100;">Employe State of Insurance(ESI)</label>
		            <div class="col-md-3">
		              <input class="form-control" name="ESI_perc" type="number"  id="ESI_perc" placeholder="Enter Percentage" ><br>
		            </div>
		          <div class="form-group">
		            		<label class="control-label col-md-2" style="padding-top:7px; font-weight:100;">percent of Gross Sal</label>
		            </div> 
		             <span style="color:#d43f3a">
		                         *
		             </span>
		             
		             <div class="col-md-3">
		              <input class="form-control" name="ESI" type="number"  id="ESI" placeholder="ESI" readonly="readonly"><br>
		             </div>
		                 
                </div><br>
                
                <div class="form-group">                		 
                				<button class="btn btn-lg btn-block btn-success" type="button" id="caliculate_sal" onclick="caliculateSalary()">Caliculate</button>                	
                </div>
                
		
		   </div>	
	   </div>
<!-- ===============================================================================-->

 </div>
	  


<script type="text/javascript" src="js/attendence.js"></script>
 <section class="attendence_page">
    <div class="container-fluid">
    <div class="col-md-12">
      <h2>Add New Employee</h2>
    </div>
        <div class="col-md-2">
		<ul class="list-group">
		 <li class="list-group-item ">
           <a href="emp_list.jsp" style="text-decoration: none;">
           <p>
           <img src="https://shiftsystems.net/demo/assets/frontend/images/dots-beginning-text-lines-interface-button-symbol.svg" width="15">

           &nbsp;List Employees
           </p></a>
           </li>


            		<li class="list-group-item active ">
              <a href="add_employee.jsp">
                <p>
                <img src="https://shiftsystems.net/demo/assets/frontend/images/plus-sign-in-circle.svg" width="15">
                &nbsp;Add Employee
                </p>
              </a></li>
              
            </ul>
		</div>
           
     <div class="col-md-10">
         <div class="col-md-12">
          <div class="inner_attendence_container">
        
          <div class="col-md-10">
             <h4>Employee Details</h4>
          </div>
          
          <div class="col-md-2">
            <a href="add_employee_excel.jsp"><button type="button" class="btn-info excell_cus">Import from Excell</button></a>
          </div>
        <div class="col-md-6">
    
 <!-- start of "Employee Details form =============================================" -->   
        
        <form id="emp_insert">
            <div class="form-group" style="margin-bottom:30px;">
            <label class="control-label col-md-3" style="padding-top:7px; font-weight:100;">Name</label>
            <div class="col-md-7">
              <input class="form-control" name="empname" type="text" value="" id="name" placeholder="Name" required="required">
            </div>
                 <span style="color:#d43f3a">
                         *
                 </span>    
                </div>
 

      
   
   <div class="form-group" style="margin-bottom:30px;">
 <label class="control-label col-md-3" style="padding-top:7px; font-weight:100;">Date Of Birth</label>
     <div class="col-md-7">
 <div class="input-group date datepicker">
 
                <input class="form-control birth" id="dob" type="date" name="bdate" placeholder="YYYY-MM-DD" >
                <span class="input-group-addon">
                <img src="https://shiftsystems.net/demo/assets/frontend/images/date.svg" width="15">
                </span>
              </div>
              
              </div>
                   <span style="color:#d43f3a">
                        *
                      </span>              
                      </div>
                      
                      
                      
   
<!--                   <div class="form-group" style="margin-bottom:30px;">
            <label class="control-label col-md-3" style="padding-top:7px; font-weight:100;">Emp Id</label>
            <div class="col-md-4">
              <input class="form-control" name="emp_id" type="text" required="required" value="" placeholder="Emp Id">
            </div>
                 <span style="color:#d43f3a">
                        *
                 </span>                                                                                                  
                </div> -->
                              
               
               <div class="form-group" style="margin-bottom:30px;">
            <label class="control-label col-md-3" style="padding-top:7px; font-weight:100;">Department</label>
            <div class="col-md-7">
              <input class="form-control" name="deptname" type="text" id="dept" value="" required="required" placeholder="Department">
            </div>
                 <span style="color:#d43f3a">
                         *
                 </span>    
                </div>
                  
                
                
   
                
                         <div class="form-group" style="margin-bottom:30px;">
            <label class="control-label col-md-3" id="test_t" style="padding-top:7px; font-weight:100;">Designation</label>
            <div class="col-md-7">
              <input class="form-control" id="designation" name="designame" type="text" value="" placeholder="Designation" >
            </div>
                 <span style="color:#d43f3a">
                     *
                 </span>    
              </div>
        
                          <div class="form-group" style="margin-bottom:30px;">
            <label class="control-label col-md-3" id="test_t" style="padding-top:7px; font-weight:100;">Band</label>
            <div class="col-md-7">
              <input class="form-control" name="e_band" type="text" value="NA" placeholder="Band">
            </div>
                 <span style="color:#fff">
                     *
                 </span>    
              </div>
              
                     <div class="form-group" style="margin-bottom:30px;">
            <label class="control-label col-md-3" id="test_t" style="padding-top:7px; font-weight:100;">Level</label>
            <div class="col-md-7">
              <input class="form-control" name="e_level" type="text" value="NA" placeholder="Level">
            </div>
                 <span style="color:#fff">
                     *
                 </span>    
              </div>
                
                 
               
          </div><!--col md 5-->
          
          <div class="col-md-6">
                       
                 <div class="form-group" style="margin-bottom:30px;">
            <label class="control-label col-md-3" style="padding-top:7px; font-weight:100;">Date Of Joining</label>
            <div class="col-md-7">
              <input class="form-control" id="doj" name="e_doj" type="date" required="required"  placeholder="YYYY-MM-DD"><br />
            </div>
            <span style="color:#d43f3a">
                         *
                 </span> 
                </div>  
          
          
         <div class="form-group" style="margin-bottom:30px;">
            <label class="control-label col-md-3" style="padding-top:7px; font-weight:100;">Email</label>
            <div class="col-md-7">
              <input class="form-control" id="email" name="e_email" type="email" value="" placeholder="Email">
            </div>
                 <span style="color:#d43f3a">
                         *
                 </span>    
                </div>
                
                
                  <div class="form-group" style="margin-bottom:30px;">
            <label class="control-label col-md-3" style="padding-top:7px; font-weight:100;">Mobile no</label>
            <div class="col-md-7">
              <input class="form-control" id="phoneno" name="phoneno" type="text" value="NA" placeholder="Mobile No" onblur="checkMobileNO();"><br />
            </div>
            <span style="color:#fff">
                        *
                </span>   
              </div>
                
  
                <div class="form-group" style="margin-bottom:30px;">
 <label class="control-label col-md-3" style="padding-top:7px; font-weight:100;">Sex</label>
     <div class="col-md-7">
              <label class="radio-inline">
              <input name="sex" type="radio" value="male">
              <span>Male</span>
              </label>
              <label class="radio-inline">
              <input name="sex" type="radio" value="female" class="female_d">
              <span>Female</span></label>
              </div>
                <span style="color:#fff">
                        *
                </span>   
                </div>
                
                
   
                
                <div class="form-group">
 <label class="control-label col-md-3" style="padding-top:7px; font-weight:100;">Martial Status</label>
     <div class="col-md-7">
              <label class="radio-inline">
              <input name="martial" type="radio" value="married">
              <span>Married</span>
              </label>
              <label class="radio-inline">
              <input name="martial" type="radio" value="single">
              <span>Single</span></label>
               <label class="radio-inline">
              <input name="martial" type="radio" value="seprated">
              <span>Separated</span></label>
              </div>
              <span style="color:#fff">
                        *
                </span>  
                 </div>
   </div>
        
                  <div class="form-group" style="margin-bottom:30px;">
            <label class="control-label col-md-3" style="padding-top:7px; font-weight:100;">PAN No</label>
            <div class="col-md-7">
              <input class="form-control" name="e_pan_no" type="text"  placeholder="PAN No"><br />
            </div>
                <span style="color:#d43f3a">
                         *
                 </span>  
              </div>
              
              
              
                  <div class="form-group" style="margin-bottom:30px;">
            <label class="control-label col-md-3" style="padding-top:7px; font-weight:100;">PF No</label>
            <div class="col-md-7">
              <input class="form-control" name="e_pf_no" type="text"  placeholder="PF No"><br />
            </div>
          <span style="color:#d43f3a">
                         *
                 </span>  
              </div>
   
   
   
          
          </div><!--col md 6-->
      
      <!-- ========================================= -->    
   
      <div class="col-md-12">          
                      <h4>Salary Details</h4>
                   </div>
                   
                   <div class="col-md-6">
                      <div class="form-group" style="margin-bottom:30px;">
            <label class="control-label col-md-3" style="padding-top:7px; font-weight:100;">Professional Tax (%)</label>
            <div class="col-md-7">
              <input class="form-control" name="e_proftax" type="number"  id="pf_perc" placeholder="Enter Percentage" ><br>
            </div>
                 <span style="color:#d43f3a">
                         *
                 </span>    
                </div>
                   
             <div class="form-group" style="margin-bottom:30px;">
            <label class="control-label col-md-3" style="padding-top:7px; font-weight:100;">Gross Salary</label>
            <div class="col-md-7">
              <input class="form-control" id="gross_sal" name="gross_sal" type="number"  placeholder="Gross Salary" >
           	   
            </div>
            
                <span style="color:#d43f3a">
                         
                 </span>     
                </div>
                
           
                <div class="form-group" style="margin-bottom:30px;">
            <label class="control-label col-md-3" style="padding-top:7px; font-weight:100;">Basic Sal(%)</label>
            <div class="col-md-7">
              <input class="form-control" name="e_msalary" type="number" id="basic_sal" value="40" placeholder="Basic Salary">
            </div>
                 <span style="color:#fff">
                         *
                 </span>    
                </div>
                   
                
                  <div class="form-group" style="margin-bottom:30px;">
            <label class="control-label col-md-3" style="padding-top:7px; font-weight:100;">PF(%)</label>
            <div class="col-md-7">
              <input class="form-control" name="e_pf" id="pf" type="number" value="12" placeholder="Provident fund" >
            </div>
                 <span style="color:#fff">
                         *
                 </span>    
                </div>
                
                <div class="form-group" style="margin-bottom:30px;">
            <label class="control-label col-md-3" style="padding-top:7px; font-weight:100;">HouseRent(%)</label>
            <div class="col-md-7">
              <input class="form-control" name="e_houserent" id="home_rent" type="number" value="40" placeholder="House Rent">
            </div>
                 <span style="color:#fff">
                         *
                 </span>    
                </div>
                
                <div class="form-group" style="margin-bottom:30px;">
            <label class="control-label col-md-3" style="padding-top:7px; font-weight:100;">Conveyance Allowance</label>
            <div class="col-md-7">
              <input class="form-control" name="e_conveyance_allowance" type="number" value="800" id="conv_allow" placeholder="Conveyance Allowance" readonly="readonly">
            </div>
                 <span style="color:#fff">
                         *
                 </span>    
                </div>
                
   
               
          </div>
          <div class="col-md-6">
           <div class="form-group" style="margin-bottom:30px;">
            <label class="control-label col-md-3" style="padding-top:7px; font-weight:100;">ESI(%)</label>
            <div class="col-md-7">
              <input class="form-control" name="e_esi" type="number" id="esi" required="required" value="1.7" placeholder="ESI" >
            </div>
                 <span style="color:#fff">
                         *
                 </span>    
                </div>
                
        
       <div class="form-group" style="margin-bottom:30px;">
            <label class="control-label col-md-3" style="padding-top:7px; font-weight:100;">Medical Allowance</label>
            <div class="col-md-7">
              <input class="form-control" name="e_medical_allowance" type="number" value="1250" id="medical_allow" placeholder="Medical Allowance" readonly="readonly"><br>
            </div>
                 <span style="color:#fff">
                         *
                 </span>    
                </div>  
                
                
          </div> 
   
                   <div class="col-md-12">          
                      <h4>Bank Details</h4>
                   </div>
                   
                   <div class="col-md-6">
            
            
            <div class="form-group" style="margin-bottom:30px;">
            <label class="control-label col-md-3" style="padding-top:7px; font-weight:100;">Bank Name</label>
            <div class="col-md-7">
              <input class="form-control" name="bank" type="text"  placeholder="Bank Name">
            </div>
                 <span style="color:#fff">
                         *
                 </span>    
                </div>
            
            
            <div class="form-group" style="margin-bottom:30px;">
            <label class="control-label col-md-3" style="padding-top:7px; font-weight:100;">Name</label>
            <div class="col-md-7">
              <input class="form-control" name="e_actname" type="text" value="" placeholder="Name On Acount" >
            </div>
                 <span style="color:#fff">
                         *
                 </span>    
                </div>
 
               
                 <div class="form-group" style="margin-bottom:30px;">
            <label class="control-label col-md-3" style="padding-top:7px; font-weight:100;">Branch</label>
            <div class="col-md-7">
              <input class="form-control" name="e_branch" type="text" id="branch" placeholder="Branch" >
            </div>
                 <span style="color:#d43f3a">
                         *
                 </span> 
                </div>
      
                  <div class="form-group" style="margin-bottom:30px;">
            <label class="control-label col-md-3" style="padding-top:7px; font-weight:100;">City</label>
            <div class="col-md-7">
              <input class="form-control" name="e_brchcity" type="text" value="" placeholder="City" >
            </div>
            <span style="color:#fff">
                         *
                 </span> 
                </div>
      
               
          </div>
          
          <div class="col-md-6">
                 <div class="form-group" style="margin-bottom:30px;">
            <label class="control-label col-md-3" style="padding-top:7px; font-weight:100;">Account no</label>
            <div class="col-md-7">
              <input class="form-control" id="ACNo" name="ACNo" type="number"  placeholder="Account No" >
            </div>
                  <span style="color:#d43f3a">
                         *
                 </span>  
                </div>
                
                 <div class="form-group" style="margin-bottom:30px;">
            <label class="control-label col-md-3" style="padding-top:7px; font-weight:100;">IFSC Code</label>
            <div class="col-md-7">
              <input class="form-control" id="e_ifsc" name="e_ifsc" type="text"   placeholder="IFSC Code" >
            </div>
                 <span style="color:#d43f3a">
                         *
                 </span>   
                </div>
               
               
                  <div class="form-group" style="margin-bottom:30px;">
            <label class="control-label col-md-3" style="padding-top:7px; font-weight:100;">Remarks</label>
            <div class="col-md-7">
              <input class="form-control" name="e_remark" type="text" value="" placeholder="Remarks" >
            </div>
                </div>
               </div>
                
          
          
          
           
         <!--=========================================================  -->          
      
      <div class="col-md-12" style="margin-bottom:20px;">
   <div class="col-md-6">
    <button class="btn btn-lg btn-block btn-success" type="button" id="save_emp" > Submit</button>
   </div>
  <div class="col-md-6">
  <button class="btn btn-lg btn-block btn-danger" type="reset"> Reset</button>
  </form>
  </div>
 </div>
      
            </div>
          
          
                  </div><!--/attendence container-->
                    </div><!--/col-md-12-->
                      </div><!--container-->
         </section><!--/attendence page-->

 
 <!-- ============================================= javaScript =======================-->
 
 <script type="text/javascript">
 	
 	$(document).ready(function() {
		
 		//alert("on MsApparels"); 		

	});
 	
		/*  $('#reg').click(function(event) */
		
		$('#save_emp').click(function(event){
			
			//alert("on saving employee");			
			var jason_object=createJson("emp_insert");    //JSON object
			//alert(jason_object);
			
			var jason_string=JSON.stringify(jason_object); // JSON object is converted in to dtring String object
			
			//the below variables are 
			/* "m_name" means the "mandatory_name", these 
			    variables are used to validate  whether the user has given data or not*/			
			var m_name        =$('#name').val();  
		    var m_dob         =$('#dob').val();  		    
		    var m_department  =$('#dept').val();	 
		    var m_designation =$('#designation').val();	 
		    var m_doj         =$('#doj').val();  
		    var m_email       =$('#email').val(); 		    
		    var m_gross_sal   =$('#gross_sal').val(); 
			var m_acno		  =$('#ACNo').val();  
			var m_ifsc		  =$('#e_ifsc').val();			 
			var m_branch	  =$('#branch').val();	
			
			/*  var num=$('#phoneno').val();
			alert("length "+num.length); */
		 
		    if(m_name==''||m_dob==''||m_department==''||m_designation=='' ||
		    	  m_doj==''||m_email=='' || m_gross_sal=='' || m_acno=='' ||
		    	  m_ifsc==''|| m_branch=='' )
		    	{
		    		alert('please fill in mandatory fields...!');
		    	}
		    else
		    	{
		    	  $.ajax({
		    		       type:'GET',
		    		       url:'EmployeRegistration',     //servlet
		    		       dataType: 'json',
		    		       data:{data:jason_string},
		    		       success: function(respo){
		    		    	   console.log(respo);
		    		    	   if(respo=='0')
		    		    		   {
		    		    		   		alert("Registration failed");
		    		    		   }
		    		    	   else{
		    		    		   alert("Registration Success");
		    		    		   $('#emp_insert')[0].reset();
		    		    	   }
		    		    	   
		    		       }// end of "Success"
		    		       
		    	        })//end of the ajax
		    	    
		    	    
		    	}
		    
		}); // end of on click function
		
	
 //to Create Json Object		
function createJson(formId){
  var out_params = [];
  var elements = document.getElementById(formId).elements;
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
		
function solve_salary() {    
	var gross_sal = document.getElementById("gross_sal").value;
	var basic_sal = document.getElementById("basic_sal").value;    
	var home_rent = document.getElementById("home_rent").value;    
	var esi = document.getElementById("esi").value;    
	var pf = document.getElementById("pf").value;    
	var medical_allow = document.getElementById("medical_allow").value;    
	var conv_allow = document.getElementById("conv_allow").value;    
	//var spcl_allow = document.getElementById("special_allow").value;
	
	var prf_Tax_Percentage=document.getElementById("pf_perc").value;	
	
	
	
	var total_allow;
	
	//alert("prof tax "+prf_Tax_Percentage)
	 
	if(gross_sal > 15000)
						{   
		                  basic_sal= parseFloat(gross_sal / 100) * 40;  
		                  home_rent = parseFloat(basic_sal / 100) * 40;   
		                  esi= parseFloat(gross_sal / 100) * 1.7;    
		                  pf= parseFloat(basic_sal / 100) * 12;
		                  var prof_tax_amount=parseFloat(basic_sal / 100)*prf_Tax_Percentage;
		                   
		                 }   
	else    {    
		      basic_sal= parseFloat(gross_sal / 100) * 40;   
		      home_rent = parseFloat(basic_sal / 100) * 40;    
		      esi= parseFloat(gross_sal / 100) * 1.7;    
		      pf= parseFloat(0.0); 
		      var prof_tax_amount=parseFloat(basic_sal / 100)*prf_Tax_Percentage;
              alert(prof_tax_amount);
		    } 
	//total_allow = parseFloat(+medical_allow + +conv_allow+ +basic_sal + +home_rent); 
	//spcl_allow = parseFloat(gross_sal - total_allow); 
	//console.log(spcl_allow);  
	console.log(esi);  
	console.log(home_rent);  
	console.log(basic_sal);  
	console.log(pf); 
	document.getElementById("esi").value = esi; 
	document.getElementById("home_rent").value = home_rent; 
	document.getElementById("basic_sal").value = basic_sal; 
	document.getElementById("pf").value = pf; 
	//document.getElementById("special_allow").value = spcl_allow;
	document.getElementById("prof_tax_amount").value= prof_tax_amount;
	$('#prof_tax_amount').html(prof_tax_amount); //this is is in jquery

} // end of the sal function
			
//for checking whether the entered number is 10 digit or not

function checkMobileNO() {	 
	var num=$('#phoneno').val();	 
	if(num.length<10 || num.length>10)
	{
		alert("please enter 10 digit phone number")	;
	}
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
 
function openDiv(evt, cityName) 
{
    var credit=$('#prty_limit').val();
    var used=$('#usedlimit').val();
    if(parseFloat(credit)<parseFloat(used))
        {
        closeModel();
        alert("Used Limit is Exceeded the Credit Limit");
        }
    else
 {
    var netwt=$('#nt_wt').val();
    var rate=$('#wt_rate').val();
    var total=parseFloat(netwt)*parseFloat(rate);
    if(cityName=='cash')
  {
        $('#totamt').val(total);
        $('#pmode').val('Cash');
  }
    if(cityName=='credit')
    {
        $('#pmode').val('Credit');
        $('#totamt1').val(total);
    }
   var i, tabcontent, tablinks;
   tabcontent = document.getElementsByClassName("tabcontent");
   for (i = 0; i < tabcontent.length; i++) {
       tabcontent[i].style.display = "none";
   }
   tablinks = document.getElementsByClassName("tablinks");
   for (i = 0; i < tablinks.length; i++) {
       tablinks[i].className = tablinks[i].className.replace(" active", "");
   }
   document.getElementById(cityName).style.display = "block";
   evt.currentTarget.className += " active";
    }
}

//this function is to caliculate the sal based on user defined percentages
	function caliculateSalary() 
	{
		var grossSalary=$('#gross_sal').val();
		
		var basic_sal_perc=$('#basic_Sal_Perc').val();
		var home_rent_perc=$('#House_rent_perc').val();
		var esi_perc      =$('#ESI_perc').val();
		var pf_perc		  =$('#providunt_fund_perc').val();
		
		if(grossSalary > 15000)
			{
			    basic_sal= parseFloat(grossSalary / 100) * basic_sal_perc;
			    home_rent = parseFloat(basic_sal / 100) * home_rent_perc;
			    esi= parseFloat(grossSalary / 100) * esi_perc;
			    pf= parseFloat(basic_sal / 100) * pf_perc;
			    
			    alert(basic_sal);
			    alert(home_rent);
			    alert(esi);
			    alert(pf);
			    $('#basic_sal').val(basic_sal);
			    $('#pf').val(pf);
			    $('#home_rent').val(home_rent);
			    $('#esi').val(esi);
			    
			}
		 
	}


 </script>
 
 
 
 
 
 
 
 
 