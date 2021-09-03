let div_list = document.getElementsByClassName('user-list');
// console.log(div_list);
fetch('https://reqres.in/api/users?page=1')
.then((resp) => {
    // console.log(resp);
    return resp.json();
})
.then((pickjson) => {
    const users = pickjson.data;
    // console.log(users);
    users.forEach((user)=>{
    
    let div_tag = document.createElement('div');
    div_tag.classList.add('user-item');

    let tag_img = document.createElement('img');
    tag_img.classList.add('avatar');
    tag_img.src = user.avatar;

    let tag_fullname = document.createElement('h3');
    tag_fullname.classList.add('fullname');
    tag_fullname.innerHTML = user.first_name+' '+user.last_name;

    let tag_email = document.createElement('p');
    tag_email.classList.add('email');
    tag_email.innerHTML = user.email;

    div_tag.append(tag_img,tag_fullname,tag_email);
    div_list[0].append(div_tag);

    })
    
    

})
.catch((myerror) => {
    console.log(myerror.message);
});


