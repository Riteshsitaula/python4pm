
var start=0;
function imageSlider(){
    let imageBox = document.getElementsByClassName('image_box');
    for(let i=0; i<imageBox.length ;i++){
        imageBox[i].style.display="none";
    }
    if(start>imageBox.length-1){
        start=0;
    }
    imageBox[start].style.display="block";
    setTimeout(imageSlider,1000);
    start++;
}
imageSlider();