function showForm(type){
    document.getElementById('registerForm').classList.add('d-none');
    document.getElementById('loginForm').classList.add('d-none');

    if(type === 'register'){
        document.getElementById('registerForm').classList.remove('d-none');
    }
    else if(type === 'login'){
        document.getElementById('loginForm').classList.remove('d-none');
    }
}

function register() {
    const fullname = document.getElementById('regFullname').value;
    const email = document.getElementById('regEmail').value;
    const password = document.getElementById('regPassword').value;

    if (!fullname){
        alert("Please Enter Your Name");
        return; 
    }
    if (!email){
        alert("Please Enter Your Email");
        return;
    }
    if (!password){
        alert("Please Enter Your Password");
        return;
    }

    const user = { fullname, email, password}
    localStorage.setItem(email,JSON.stringify(user));
    
    alert("Registration Successful!!You Can Login");

    document.getElementById('regFullnameregFullname').value ='';    
    document.getElementById('regEmail').value ='';
    document.getElementById('regPassword').value ='';

    showForm('login');
}



function login(){
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;
    
    if(!email){
        alert("Enter Your Email.....");
    }
    else if(!password){
        alert("Enter Your Password.....");
    }

    const user = localStorage.getItem(email);
    
    if (!user){
        alert("User Not Exist...");
    }
    
    const perseUser = JSON.parse(user);
    
    if(password != perseUser.password){
        alert("Wrong PassWord");
        return;
    }

    alert("Login Successful!! Welcome"+ perseUser.fullname);

    document.getElementById('loginEmail').value ='';
    document.getElementById('loginPassword').value ='';

}