<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
    <link rel="stylesheet" type="text/css" href="css/style.css">
   <!-- <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"> -->
 <link rel="stylesheet" href="css/bootstrap.min.css">
    <!--  <link rel="stylesheet" href="bootstrap-3.3.7/dist/css/bootstrap.min.css">-->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
    <script type="text/javascript" src="jquery.scannerdetection.js"></script>
    <!-- <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>-->
    <script src="js/bootstrap.min.js"></script>
    <link rel="stylesheet" type="text/css" href="css/home.css">
	<link rel="stylesheet" href="css/jquerytheme.css"/>	
	<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/1.3.4/jspdf.debug.js"></script>
    <script src="https://unpkg.com/jspdf@latest/dist/jspdf.min.js"></script>
    <!--<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>-->
    <title>POSMD</title>
    <link rel="icon" href="images/logo md.JPG">
    <style>
        body {
            font-family: 'Lato', sans-serif;
        }

        .overlay {
            height: 100%;
            width: 100%;
            position: fixed;
            z-index: 1;
            top: 0;
            left: 0;
            overflow-y: hidden;
            background-color: #FFF;
            transition: 0.5s;
        }

        .overlay-content {
            position: relative;
            width: 100%;
            text-align: center;
            margin-top: -20px;
            top: 9%;
        }

        .overlay a {
            padding: 8px;
            text-decoration: none;
            color: #818181;
            display: block;
            transition: 0.3s;
        }

        .overlay a:hover,
        .overlay a:focus {
            color: #000;
        }

        .overlay .closebtn {
            position: absolute;
            top: 10px;
            right: 45px;
            font-size: 60px;
        }

        @media screen and (max-height: 450px) {
            .overlay {
                overflow-y: auto;
            }
            .overlay a {
                font-size: 20px
            }
            .overlay .closebtn {
                font-size: 40px;
                top: 15px;
                right: 35px;
            }
        }
    </style>
    
  
   
</head>

<body>
<%
	response.setHeader("Cache-Control", "no-cache, no-store, must-revalidate"); //For HTTP 1.1
	response.setHeader("Pragma", "no-cache"); //For HTTP 1.0
	response.setHeader("Expires", "0"); // For Proxies
	
	if (session.getAttribute("adminEmail") == null) {
		response.sendRedirect("login.html");
	}
%>
   
    <!--navebar-->
    <input type="hidden" name="rights" id="rights" value="${rights}">
    <div id="myNav" class="overlay" style="overflow:scroll;">
        <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
        <div class="overlay-content">
            <!--<div class="row">-->
                <h2 style="text-align: center;font-weight:600;font-size: 50px;color: #FF5733">POS<span style="color: #C70039">MD</span></h2>
                <hr>
            <!--</div>-->
            <form action="LogoutServlet" method="get">
             <button class="btn btn-success" type="submit">LOGOUT</button>
            </form>
            
            <div class="a_menu">
                <div class="col-md-3">
                
              <a href="sales.html" onclick="closeNav()" id="sale">
       
            <div class="col1">
              
                <div class="cus_blk"><img src="images/sales.png" /><b>Sales</b></div>
                
            </div>
        </a>
    </div>
    <div class="col-md-3">
       <!--  <a href="bank_main.html" onclick="closeNav()"> -->
       <a href="#" onclick="closeNav()" id="banks">
            <div class="col1">
                <div class="cus_blk"><img src="images/banks_1.png" /><b>Banks</b></div>
            </div>
        </a>
    </div>
    <div class="col-md-3">
        <!-- <a href="add_company.html" onclick="closeNav()"> -->
        <a href="#" onclick="closeNav()" id="company">
            <div class="col1">
                <div class="cus_blk"><img src="images/company.png" /><b>Add Company</b></div>
            </div>
        </a>
    </div>
    <div class="col-md-3">
        <!-- <a href="godown_main.html" onclick="closeNav()"> -->
        <a href="#" onclick="closeNav()" id="godown">
            <div class="col1">
                <div class="cus_blk"><img src="images/godown.png" /><b>Godown</b></div>
            </div>
        </a>
    </div>
    <div class="col-md-3">
        <!-- <a href="buisness_location_main.html" onclick="closeNav()"> -->
        <a href="#" onclick="closeNav()" id="buisness_location_main">
            <div class="col1">
                <div class="cus_blk"><img src="images/businesslocation.png" /><b>Business Location</b></div>
            </div>
        </a>
    </div>
    <div class="col-md-3">
        <!-- <a href="items.html" onclick="closeNav()"> -->
        <a href="#" onclick="closeNav()" id="items">
            <div class="col1">
                <div class="cus_blk"><img src="images/items.png" /><b>Stock</b></div>
            </div>
        </a>
    </div>
    <div class="col-md-3">
        <!-- <a href="customer_grp.html" onclick="closeNav()"> -->
        <a href="#" onclick="closeNav()" id="customer_grp">
            <div class="col1">
                <div class="cus_blk"><img src="images/customergroup.png" /><b>Customer Group</b></div>
            </div>
        </a>
    </div>
    <div class="col-md-3">
        <!-- <a href="manage_employee.html" onclick="closeNav()"> -->
        <a href="#" onclick="closeNav()" id="manage_employee">
            <div class="col1">
                <div class="cus_blk"><img src="images/employees.png" /><b>Employees</b></div>
            </div>
        </a>
    </div>
    <div class="col-md-3">
        <!-- <a href="manage_category.html" onclick="closeNav()"> -->
        <a href="#" onclick="closeNav()" id="manage_category">
            <div class="col1">
                <div class="cus_blk"><img src="images/categories.png" /><b>Manage Categories</b></div>
            </div>
        </a>
    </div>
    <div class="col-md-3">
        <!-- <a href="cash_register_main.html" onclick="closeNav()"> -->
        <a href="#" onclick="closeNav()" id="cash_register_main">
            <div class="col1">
                <div class="cus_blk"><img src="images/cash-register.png" /><b>Cash Register</b></div>
            </div>
        </a>
    </div>
    <div class="col-md-3">
        <!-- <a href="manage_supplier.html" onclick="closeNav()"> -->
        <a href="#" onclick="closeNav()" id="manage_supplier">
            <div class="col1">
                <div class="cus_blk"><img src="images/supplier.png" /><b>Supplier</b></div>
            </div>
        </a>
    </div>
    <div class="col-md-3">
        <!-- <a href="state_master.html" onclick="closeNav()"> -->
        <a href="#" onclick="closeNav()" id="state_master">
            <div class="col1">
                <div class="cus_blk"><img src="images/FinancialTransaction.png" /><b>State Master</b></div>
            </div>
        </a>
    </div>
    <div class="col-md-3">
        <!-- <a href="sale_return.html" onclick="closeNav()"> -->
        <a href="sale_return.html" onclick="closeNav()" id="sale_return">
            <div class="col1">
                <div class="cus_blk"><img src="images/return.png" /><b>Sale Return</b></div>
            </div>
        </a>
    </div>
    <div class="col-md-3">
        <!-- <a href="edit_general_po.html" onclick="closeNav()"> -->
        <a href="#" onclick="closeNav()" id="edit_general_po">
            <div class="col1">
                <div class="cus_blk"><img src="images/purchase.png" /><b>Purchase Order</b></div>
            </div>
        </a>
    </div>
    <div class="col-md-3">
        <!-- <a href="receive_items.html" onclick="closeNav()"> -->
        <a href="#" onclick="closeNav()" id="receive_items">
            <div class="col1">
                <div class="cus_blk"><img src="images/recieve_item.png" /><b>Receive Items</b></div>
            </div>
        </a>
    </div>
    <div class="col-md-3">
        <!-- <a href="manage_report.html" onclick="closeNav()"> -->
        <a href="#" onclick="closeNav()" id="manage_report">
            <div class="col1" >
                <div class="cus_blk"><img src="images/reports.png"/><b>Reports</b></div>
            </div>
        </a>
    </div>
    <div class="col-md-3">
        <!-- <a href="add_customer.html" onclick="closeNav()"> -->
        <a href="#" onclick="closeNav()" id="add_customer">
            <div class="col1">
                <div class="cus_blk"><img src="images/employees.png" /><b>Customer</b></div>
            </div>
        </a>
    </div>
      <div class="col-md-3">
        <!-- <a href="recieve_payments.html" onclick="closeNav()"> -->
        <a href="#" onclick="closeNav()" id="recieve_payments">
            <div class="col1">
                <div class="cus_blk"><img src="images/bitcoin.jpg" /><b>Receive Payments</b></div>
            </div>
        </a>
    </div>
    <div class="col-md-3">
        <!-- <a href="barcode.html" onclick="closeNav()"> -->
        <a href="#" onclick="closeNav()" id="barcode">
            <div class="col1">
                <div class="cus_blk"><img src="images/barcode.jpg" /><b>Generate Barcode</b></div>
            </div>
        </a>
    </div>
    
     <div class="col-md-3">
        <!-- <a href="createuser.html" onclick="closeNav()"> -->
        <a href="" onclick="closeNav()" id="createuser">
            <div class="col1">
                <div class="cus_blk"><img src="images/user1.jpg" /><b>Create User</b></div>
            </div>
        </a>
    </div>
    
    
    <div class="col-md-3">
        <!-- <a href="createuser.html" onclick="closeNav()"> -->
        <a href="" onclick="closeNav()" id="payroll">
            <div class="col1">
                <div class="cus_blk"><img src="images/payroll.jpg" /><b>Payroll</b></div>
            </div>
        </a>
    </div>
    
    
    <div class="col-md-3">
        <!-- <a href="createuser.html" onclick="closeNav()"> -->
        <a href="" onclick="closeNav()" id="payslip">
            <div class="col1">
                <div class="cus_blk"><img src="images/payslip1.jpg" /><b>PaySlip</b></div>
            </div>
        </a>
    </div>
    
    
    
    
    <div class="col-md-3">
        <!-- <a href="sendmail.html" onclick="closeNav()"> -->
        <a href="" onclick="closeNav()" id="sendmail">
            <div class="col1">
                <div class="cus_blk"><img src="images/mail.jpg" /><b>Send Mail</b></div>
            </div>
        </a>
    </div>
            </div>
        </div>
        
        <!--a menu-->
    </div>
   
    <!--</div>
    navebar-->
    <!--<div class="row">-->
        <header class="col-md-12" id="header">
            <strong><span style="font-size:29px;cursor:pointer; margin-top:13px; margin-left:20px; float:left;" onclick="openNav()">&#9776;</span></strong>
        </header>
    <!--</div>
    row-->
    <div id="snackbar">Warning!</div>
    <section id="get_page">
    </section>
   
    <script type="text/javascript" src="controler/menu_control.js"></script>
    <script>
    $(document).ready(function() 
    {
    	//console.log("data");
    	redirectpage();
    	//localStorage.setItem("lastname", "jagadeesh");
    	checkStatus();
    });
        function openNav() {
            document.getElementById("myNav").style.height = "100%";
        }

        function closeNav() {
            document.getElementById("myNav").style.height = "0%";
        }
        function redirectpage()
        {
        	
        	/* var right=localStorage.getItem("lastname");
        	console.log(right);
        	if(right=='jagadeesh')
        		{
        	//	alert("Please Login as Admin");
        	//	window.location.href='http://localhost:8082/POSMD/login.html';
        		var a = document.getElementById('sale'); //or grab it by tagname etc
        		a.href = "#";
        		alert("data");
        		} */
        }
        
        function checkStatus()
        {
       	// alert("data");
   //    	var path="checkForTeacher";
         
       	 $.ajax({
       	  		type: 'GET',
       	  		 url : 'LoginServlet',
       	  		//data : {path:path},
       	  		//dataType: "json",
       	  		success : function(respo) 
       	  		{	
       	  			//alert(respo);
       	  			if(respo=="1")
       	  				{
       	  				//document.getElementById("check").submit();
       	  				document.getElementById('banks').href="bank_main.html";
       	  			    document.getElementById('company').href="add_company.html";
       	  			    document.getElementById('godown').href="godown_main.html";
       	  			    document.getElementById('buisness_location_main').href="buisness_location_main.html";
       	  			    document.getElementById('items').href="items.html";
       	  		        document.getElementById('customer_grp').href="customer_grp.html";
       	  		        document.getElementById('manage_employee').href="manage_employee.html"; 
       	  		      //  document.getElementById('manage_employee').href="add_employee.jsp";  
       	  		       document.getElementById('manage_category').href="manage_category.html";
       	  		        document.getElementById('cash_register_main').href="cash_register_main.html";
	       	  		    document.getElementById('manage_supplier').href="manage_supplier.html";
	  	  		        document.getElementById('state_master').href="state_master.html";
	  	  		        document.getElementById('sale_return').href="sale_return.html"; 
	  	  		        document.getElementById('edit_general_po').href="edit_general_po.html";
	  	  		        document.getElementById('receive_items').href="receive_items.html";
		  	  		    document.getElementById('manage_report').href="manage_report.html"; 
	  	  		        document.getElementById('add_customer').href="add_customer.html";
	  	  		        document.getElementById('recieve_payments').href="recieve_payments.html";
		  	  		    document.getElementById('barcode').href="barcode.html"; 
	  	  		        document.getElementById('createuser').href="createuser.html";
	  	  		        document.getElementById('sendmail').href="sendmail.html";
	  	  		        document.getElementById('payroll').href="payroll.jsp";
	  	  		        document.getElementById('payslip').href="payroll_slip.jsp";
	  	  		        localStorage.setItem('eid',respo);
       	  				}
       	  			else
       	  			{
       	  			     localStorage.clear();
       	  				localStorage.setItem('eid',respo);
       	  				//alert(localStorage.getItem('eid')); 
       	  			}
       	  		}
       	  	}); 
        }
    </script>
</body>

</html>