
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function testfunction(){
        console.log("access fucnction already");
        const send_data = {
            
            id:"",
        
            Volt_name:"222",
            
        
    };
    let csrftoken = getCookie('csrftoken');
    const option = {
        
        method: 'POST',
        headers: {
        "X-CSRFToken": csrftoken, 
        'Content-Type': 'application/json',
        },
        body: JSON.stringify(send_data),
    }
    
    fetch('/uploadpic/voltage/',option)
    .then((resp) => {
        
        return resp.json();
    })
    .then((pickjson) => {
        
        console.log(pickjson);
        
    
    
    })
    .catch((myerror) => {
        console.log(myerror.message);
    });
}



