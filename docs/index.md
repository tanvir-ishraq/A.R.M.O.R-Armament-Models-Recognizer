---
title: Home
<!-- layout: page -->
---
 
<!-- Frontend prediction user interface. Data are handled by API-->
<a id="forkme_banner" href="#">A.R.M.O.R Classifier</a>
<h2 style="margin-top: 20px;"> Analyze: </h2>
<p style="font-size:18px;">  Welcome! ✨ Please wait a few moments after image upload for prediction result. Thank you for your cordial patience.</p>

<div style="display: flex; justify-content: center">
    <input id="photo" type="file" style="font-size:17.5px; height:44px">
</div>
<div id="results" style="text-align: center; margin-top: 15px;"> </div>
<br>

<!-- Description section -->
<h2 style="margin-top: 20px;"> A Comprehensive Armaments Image Recognizer </h2>
<h3 style="text-align: center"> Armament Models Recognizer for Civilian Security </h3>
<p style="font-size:17px;"> A security measure that can classify comprehensive 22 different types of most common military armaments posing threat for civilians on land. <br> 
The armament types are following: </p>
1.  2S19 Msta artillery
2.  BM-21 Grad artillery
3.  G6 Rhino artillery
4.  M109 artillery
5.  M270 MLRS artillery
6.  Smerch artillery
7.  BMP-2 vehicle
8.  BTR-80 vehicle
9.  Humvee vehicle
10. LAV-25 vehicle
11. M113 vehicle
12. MRAP vehicle
13. Leopard 2 tank
14. M1 Abrams tank
15. T-72 tank
16. Type 99 tank
17. Bayraktar TB2 UCAV drone
18. CH-5 Rainbow UCAV drone
19. Hermes 900 drone
20. Heron TP drone
21. MQ-9 Reaper UCAV drone
22. RQ-4 Global Hawk UCAV drone

<!-- ARMOR classifier API & output messaging-->
<script>
    async function loaded(reader) {   
        const response = await fetch("https://tanvir-ishraq-armor-armament-models-recognizer.hf.space/run/predict", {
                method: "POST", headers: { "Content-Type": "application/json" },
                body: JSON.stringify( {data: [reader.result]} )
            } 
        ); 
        const json = await response.json();
        const label = json['data'][0]['label'];
        let probability = json['data'][0]['confidences'][0]['confidence'] * 100;
        probability = Math.ceil(probability);
        results.innerHTML = `<p style="font-size:18px"> 
                              <strong> Result: ${label} </strong> (${probability}% pattern)  
                             </p> 
                             <img src = "${reader.result}" width="500">` ;  
    }

    function read() {
        const reader = new FileReader();
        reader.addEventListener('load', () => loaded(reader))
        reader.readAsDataURL(photo.files[0]);
    }
    
    photo.addEventListener('input', read);
</script>
