var imgname=["backiee-118342.jpg","Flowers.jpg","KTM.jpg","Bike.jpg","backiee-124592.jpg"];
        var i=0;
        baseUrl="static/images/";
        function moveSlider(){
         if(i==imgname.length)
          {
          i=0;
          }
          document.getElementById("slide").src=baseUrl+imgname[i];
          i++;
          window.setTimeout("moveSlider()",2000);
        }

