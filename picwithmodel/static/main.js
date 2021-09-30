$(document).ready(function() {
    //drag&drop img
    var dropContainer = document.getElementById('drop-container');
    dropContainer.ondragover = dropContainer.ondragend = function() {
      return false;
    };
  
    dropContainer.ondrop = function(e) {
      e.preventDefault();
      loadImage(e.dataTransfer.files[0])
    }
    //browse img
    $("#browse-button").change(function() {
      loadImage($("#browse-button").prop("files")[0]);
    });
    
    // ส่งรูปภาพไปจากClient ไป server เพื่อประมวลผลรูป
    $('.modal').modal({
      dismissible: false,
      ready: function(modal, trigger) {
        $.ajax({
          type: "POST",
          url: 'http://127.0.0.1:8000/picwithmodel/object_detection/api_request/',
          data: {
            'image64': $('#img-card-1').attr('src')
          },
          dataType: 'text',
          // ประมวลผลเสร็จ รับjson_object
          success: function(data) {
            loadStats(data)
          } 
          // ประมวลผลเสร็จปิดหน้า loading
        }).always(function() {
          modal.modal('close');
        });
      }
    });
   
    $('#go-back').click(function() {
      $('#img-card-1').removeAttr("src");
      $('#stat-table').html('');
      switchCard(0);
    });
     $('#go-start').click(function() {
      var elem = document.getElementById("result");
      elem.parentNode.removeChild(elem);
      $('#stat-table').html('');
      switchCard(0);
    });
    // คลิก show predictions แสดงรูปหลังการประมวลผล
    $('#show').click(function() {
      switchCard(3);
      var timestamp = new Date().getTime();
      var el = document.getElementById("#img-card-2");
      var queryString = "?t=" + timestamp;
      el.src = "http://127.0.0.1:8000/MEDIA/Media/test.jpeg" + queryString;
    });


    // คลิก detect object ให้open window หน้า loading
    $('#upload-button').click(function() {
      $('.modal').modal('open');
    });
  });
  //animation
  switchCard = function(cardNo) {
    var containers = [".dd-container", ".uf-container", ".dt-container", ".it-container"];
    var visibleContainer = containers[cardNo];
    for (var i = 0; i < containers.length; i++) {
      var oz = (containers[i] === visibleContainer) ? '1' : '0';
      $(containers[i]).animate({
        opacity: oz
      }, {
        duration: 200,
        queue: false,
      }).css("z-index", oz);
    }
  }
  //read img และแสดงรูป
  loadImage = function(file) {
    var reader = new FileReader();
    reader.onload = function(event) {
      $('#img-card-1').attr('src', event.target.result);
    }
    reader.readAsDataURL(file);
    switchCard(1);  
  }
  //แสดง Json หลังจากประมวลผล
  loadStats = function(jsonData) {
    switchCard(2);
    //Json(webserver)->JavascriptObj=DictObj
    var data = JSON.parse(jsonData);
    var jtext = data["objects"];
    if(data["success"] == true){
      var elem = document.createElement("div");
      elem.innerHTML = jsonData;
      elem.setAttribute('id', 'result');
      document.getElementById("result-text").appendChild(elem);
    }
  }
