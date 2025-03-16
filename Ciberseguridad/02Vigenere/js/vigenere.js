var vigenere = vigenere || (function(){

    //Aqui tenemos que crear una funcion que se encargue de obtener el texto, desplazamiento y si va a cifrar o descifrar

    var proceso = function(txt, desp, action){
        var replace = (function(){
            //ABC
            var abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
            var longitud = abc.length;

            return function(c){
                var i = abc.indexOf(c.toLowerCase());
                if(i != -1){
                    var pos = i;
                    if(action){
                        //cifrar
                        pos += desp;
                        pos = (pos >= longitud) ? pos - longitud : pos;
                    }else{
                        //descifrar ahi lo hacen :3
                        pos -= desp;
                        pos = (pos < 0) ? pos + longitud : pos;
                    }
                    return abc[pos];
                }
                return c;
            };
        })();

        //hay que validar la cadena
        var re = (/([a-z])/ig);

        return String(txt).replace(re,function(match){
            return replace(match);
        });
    };
    return{
        //vamos a saber si queremos cifrar o descifrar
        encode : function(txt, desp){
            return proceso(txt, desp, true);
        },
        decode : function(txt, desp){
            return proceso(txt, desp, false);
        }
    };
})();

//cuando los campos esten vacios

//cuando la clave sea mas grande que el texto para cifrar

//cuando la clave sea mas grande que el texto para descifrar

//cifrar
function codificar(texto, clave){

    var resultado = "";
    var indiceclave = 0;
    var charartexto = texto.split('');

    for(var i = 0; i < charartexto.length; i++){
        var desp = obindiceClave(clave.charAt(indiceclave));
        var chartexto = charartexto[i];

        resultado += vigenere.encode(chartexto, (desp >= 26) ? desp%26 : desp);
        indiceclave++;

        if(indiceclave >= clave.length){
            indiceclave = 0;
        }

        document.getElementById("resultado").value = resultado;
    }
}

function obindiceClave(reco){
    var abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
    return abc.indexOf(reco.toLowerCase());
}

//decifrar
function decodificar(texto, clave){
    var resultado = "";
    var indiceclave = 0;
    var charartexto = texto.split('');

    for(var i = 0; i < charartexto.length; i++){
        var desp = obindiceClave(clave.charAt(indiceclave));
        var chartexto = charartexto[i];

        resultado += vigenere.decode(chartexto, (desp >= 26) ? desp % 26 : desp);
        indiceclave++;

        if(indiceclave >= clave.length){
            indiceclave = 0;
        }
    }

    document.getElementById("resultado").value = resultado;
}
//reiniciar
function reiniciar(){
    document.getElementById("texto").value = "";
    document.getElementById("clave").value = "";
    document.getElementById("resultado").value = "";
}