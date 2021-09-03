function testfunction(){
    console.log("access fucnction already");
    const send_data = {

        id:"5",
    
        Volt_name:"111",
        
    
    };
    
    const option = {
        
        method: 'POST',
        headers: {
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



