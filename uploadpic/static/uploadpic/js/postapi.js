let registerForm = document.getElementById('register-form');
console.log(registerForm);
let emailInput = document.getElementById('email-input');
let passwordInput = document.getElementById('password-input');

function Register(event){
    event.preventDefault();

    console.log(emailInput.value);

    const send_data = {
        email:emailInput.value,
        
        password:passwordInput.value,

        // email:eve.holt@reqres.in,

        // password:pistol,
        
     

        
    };
    const option = {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        },
        body: JSON.stringify(send_data),
    }
    fetch('https://reqres.in/api/register',option)
    .then((resp) => {
        
        return resp.json();
    })
    .then((pickjson) => {
        
        console.log(pickjson);
        alert('completed register='+pickjson.id);
    
    
    })
    .catch((myerror) => {
        console.log(myerror.message);
    });

}

registerForm.addEventListener('submit',Register);
