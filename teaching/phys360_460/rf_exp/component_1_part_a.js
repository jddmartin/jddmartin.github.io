// machine generated; do not edit!

var images = new Array();
var descriptions = new Array();

images[0]="devices/default_thumb.jpg";
descriptions[0]="";

images[1]="devices/multimeter_thumb.jpg";
descriptions[1]="<h2>Multimeter</h2>\
<p>Hewlett-Packard 3478a</p>\
";
images[2]="devices/e3620a_thumb.jpg";
descriptions[2]="<h2>E3620a dc power supply</h2>";
images[3]="devices/vco_thumb.jpg";
descriptions[3]="\
<h2>Voltage controlled oscillator</h2>\
<p>\
Minicircuits ZX95-850-S+\
</p>\
";
images[4]="devices/isolator_thumb.jpg";
descriptions[4]="<h2> Isolator </h2>\
<p>\
Fairview Microwave, P/N SFI8090\
</p>\
";
images[5]="devices/counter_thumb.jpg";
descriptions[5]="<h2>Frequency counter</h2>\
<p> \
Racal-Dana 1999c\
</p>\
";
images[6]="devices/sma_m_m_thumb.jpg";
descriptions[6]="<h2>SMA M-M connector</h2>\
";
 

for(var i=0; i<images.length; i++) {
    preload_image[i]= new Image();
    preload_image[i].src = images[i];
}

function changeSrc(cindex)
{
    document.getElementById("thumb").src=images[cindex];
    document.getElementById("moredetailtext").innerHTML=descriptions[cindex];
}
