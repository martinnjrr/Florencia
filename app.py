from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <title>Para ti 💛</title>

    <style>

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html,
        body {
            width: 100%;
            height: 100%;
        }

        body {
            background: #000;
            color: white;

            overflow: hidden;

            font-family:
                Georgia,
                "Times New Roman",
                serif;
        }


        /* =====================================
           PANTALLAS
        ===================================== */

        .pantalla {

            position: absolute;

            inset: 0;

            width: 100%;
            height: 100%;

            display: flex;

            flex-direction: column;

            align-items: center;

            justify-content: center;

            opacity: 0;

            visibility: hidden;

            transform: scale(1.03);

            transition:
                opacity 1s ease,
                transform 1s ease,
                visibility 1s;

        }


        .pantalla.activa {

            opacity: 1;

            visibility: visible;

            transform: scale(1);

        }



        /* =====================================
           PANTALLA 1 Y 2
        ===================================== */

        #pantalla1,
        #pantalla2 {

            background:
                radial-gradient(
                    circle at center,
                    #151515 0%,
                    #050505 55%,
                    #000000 100%
                );

        }



        /* =====================================
           PREGUNTA
        ===================================== */

        .pregunta {

            font-size:
                clamp(
                    2.5rem,
                    7vw,
                    5.5rem
                );

            font-weight: normal;

            margin-bottom: 45px;

            text-align: center;

            padding: 20px;

            animation:
                aparecer 1.4s ease;

        }



        /* =====================================
           BOTONES
        ===================================== */

        .botones {

            display: flex;

            gap: 25px;

        }


        button {

            min-width: 150px;

            padding:
                14px 35px;

            border:
                1px solid
                rgba(
                    255,
                    255,
                    255,
                    0.8
                );

            border-radius: 50px;

            background:
                rgba(
                    255,
                    255,
                    255,
                    0.03
                );

            color: white;

            font-size: 1.2rem;

            cursor: pointer;

            backdrop-filter:
                blur(10px);

            transition:
                background 0.35s ease,
                color 0.35s ease,
                transform 0.35s ease;

        }


        button:hover {

            background: white;

            color: black;

            transform:
                translateY(-4px);

        }


        button:active {

            transform:
                scale(0.95);

        }



        /* =====================================
           RESPUESTA NO
        ===================================== */

        #triste {

            position: absolute;

            margin-top: 270px;

            display: flex;

            align-items: center;

            justify-content: center;

            gap: 10px;

            white-space: nowrap;

            font-family:
                Arial,
                sans-serif;

            opacity: 0;

            transform:
                translateY(20px)
                scale(0.9);

            transition:
                opacity 0.6s ease,
                transform 0.6s ease;

        }


        #triste.mostrar {

            opacity: 1;

            transform:
                translateY(0)
                scale(1);

        }


        .cara-triste {

            font-size: 1.3rem;

            color: white;

        }


        #triste p {

            color: #aaaaaa;

            font-size: 1rem;

        }



        /* =====================================
           CORAZONES DE FONDO
        ===================================== */

        .corazon {

            position: absolute;

            color:
                rgba(
                    255,
                    255,
                    255,
                    0.15
                );

            font-family:
                Arial,
                sans-serif;

            animation:
                flotarCorazon
                5s
                ease-in-out
                infinite;

        }


        .c1 {

            top: 15%;
            left: 15%;

            font-size: 25px;

        }


        .c2 {

            top: 25%;
            right: 16%;

            font-size: 20px;

            animation-delay: 1s;

        }


        .c3 {

            bottom: 15%;
            left: 20%;

            font-size: 18px;

            animation-delay: 2s;

        }


        .c4 {

            bottom: 20%;
            right: 20%;

            font-size: 27px;

            animation-delay: 3s;

        }



        /* =====================================
           PANTALLA 2
        ===================================== */

        .girasol-grande {

            font-size: 7rem;

            filter:
                drop-shadow(
                    0 0 30px
                    rgba(
                        255,
                        215,
                        0,
                        0.35
                    )
                );

            animation:
                florFlotando
                2.5s
                ease-in-out
                infinite;

        }


        .texto-flor {

            margin-top: 30px;

            font-size:
                clamp(
                    2rem,
                    5vw,
                    4rem
                );

            font-weight: normal;

            text-align: center;

            padding:
                0 20px;

        }


        .corazon-amarillo {

            margin-top: 25px;

            font-size: 2rem;

            color: #ffd900;

            animation:
                latido
                1.5s
                infinite;

        }



        /* =====================================
           PANTALLA FINAL
        ===================================== */

        #pantalla3 {

            background:

                linear-gradient(
                    to bottom,

                    #42a5f5 0%,

                    #75c6ff 52%,

                    #bde7ff 68%,

                    #72b94a 69%,

                    #3c8d32 100%
                );

        }



        /* =====================================
           SOL
        ===================================== */

        .sol {

            position: absolute;

            top: 8%;

            right: 10%;

            width: 100px;

            height: 100px;

            border-radius: 50%;

            background:
                #ffe46b;

            box-shadow:

                0 0 50px
                rgba(
                    255,
                    238,
                    120,
                    0.8
                ),

                0 0 100px
                rgba(
                    255,
                    238,
                    120,
                    0.4
                );

            opacity: 0.85;

        }



        /* =====================================
           NUBES
        ===================================== */

        .nube {

            position: absolute;

            width: 160px;

            height: 50px;

            border-radius: 50px;

            background:
                rgba(
                    255,
                    255,
                    255,
                    0.7
                );

            filter:
                blur(1px);

            animation:
                moverNube
                25s
                ease-in-out
                infinite;

        }


        .nube::before,
        .nube::after {

            content: "";

            position: absolute;

            background: inherit;

            border-radius: 50%;

        }


        .nube::before {

            width: 70px;

            height: 70px;

            left: 30px;

            top: -35px;

        }


        .nube::after {

            width: 90px;

            height: 90px;

            right: 20px;

            top: -45px;

        }


        .nube1 {

            top: 15%;

            left: 8%;

        }


        .nube2 {

            top: 28%;

            left: 65%;

            transform:
                scale(0.7);

            opacity: 0.6;

            animation-delay:
                -10s;

        }



        /* =====================================
           CERROS
        ===================================== */

        .cerros {

            position: absolute;

            left: -5%;

            bottom: 28%;

            width: 110%;

            height: 180px;

            background:
                #468b55;

            clip-path:
                polygon(

                    0 100%,

                    0 75%,

                    12% 35%,

                    24% 70%,

                    38% 25%,

                    50% 68%,

                    65% 35%,

                    78% 70%,

                    91% 30%,

                    100% 60%,

                    100% 100%

                );

            opacity: 0.85;

        }



        /* =====================================
           PASTO
        ===================================== */

        .pasto {

            position: absolute;

            bottom: 0;

            left: 0;

            width: 100%;

            height: 32%;

            background:

                linear-gradient(

                    to bottom,

                    #67b845,

                    #3c8c31

                );

        }



        /* =====================================
           MENSAJE FINAL
        ===================================== */

        .mensaje-final {

            position: relative;

            z-index: 30;

            margin-top:
                -15vh;

            text-align: center;

            font-size:

                clamp(
                    3rem,
                    8vw,
                    7rem
                );

            line-height: 0.95;

            font-weight: normal;

            color: white;

            text-shadow:

                0 3px 15px
                rgba(
                    0,
                    0,
                    0,
                    0.15
                );

            opacity: 0;

            transform:
                translateY(40px);

            transition:

                opacity
                1.7s
                ease
                1s,

                transform
                1.7s
                ease
                1s;

        }


        #pantalla3.activa
        .mensaje-final {

            opacity: 1;

            transform:
                translateY(0);

        }


        .corazon-final {

            position: relative;

            z-index: 30;

            margin-top: 30px;

            font-size: 3rem;

            opacity: 0;

            transition:
                opacity
                1.5s
                ease
                2s;

        }


        #pantalla3.activa
        .corazon-final {

            opacity: 1;

        }



        /* =====================================
           JARDÍN
        ===================================== */

        #jardin {

            position: absolute;

            bottom: 0;

            left: 0;

            width: 100%;

            height: 45%;

            z-index: 20;

            pointer-events: none;

        }


        .flor {

            position: absolute;

            bottom: -300px;

            display: flex;

            flex-direction: column;

            align-items: center;

            transform-origin:
                bottom center;

            animation:

                crecer
                2.3s
                cubic-bezier(
                    0.17,
                    0.67,
                    0.32,
                    1.15
                )
                forwards;

        }


        .cabeza {

            position: relative;

            width: 80px;

            height: 80px;

            z-index: 2;

        }


        .petalo {

            position: absolute;

            width: 29px;

            height: 48px;

            left: 25px;

            top: 16px;

            background:

                linear-gradient(

                    to bottom,

                    #ffe94d,

                    #ffc400

                );

            border-radius:
                60% 60% 50% 50%;

            transform-origin:
                15px 24px;

            box-shadow:

                0 0 12px
                rgba(
                    255,
                    200,
                    0,
                    0.25
                );

        }


        .petalo:nth-child(1) {

            transform:
                rotate(0deg)
                translateY(-27px);

        }


        .petalo:nth-child(2) {

            transform:
                rotate(45deg)
                translateY(-27px);

        }


        .petalo:nth-child(3) {

            transform:
                rotate(90deg)
                translateY(-27px);

        }


        .petalo:nth-child(4) {

            transform:
                rotate(135deg)
                translateY(-27px);

        }


        .petalo:nth-child(5) {

            transform:
                rotate(180deg)
                translateY(-27px);

        }


        .petalo:nth-child(6) {

            transform:
                rotate(225deg)
                translateY(-27px);

        }


        .petalo:nth-child(7) {

            transform:
                rotate(270deg)
                translateY(-27px);

        }


        .petalo:nth-child(8) {

            transform:
                rotate(315deg)
                translateY(-27px);

        }


        .centro {

            position: absolute;

            left: 22px;

            top: 22px;

            width: 36px;

            height: 36px;

            border-radius: 50%;

            background:

                radial-gradient(

                    circle,

                    #6b4100,

                    #3d2500

                );

            z-index: 4;

        }


        .tallo {

            width: 6px;

            margin-top: -4px;

            background:

                linear-gradient(

                    to right,

                    #246b25,

                    #4a9d3d,

                    #246b25

                );

            border-radius: 5px;

        }



        /* =====================================
           ANIMACIONES
        ===================================== */

        @keyframes aparecer {

            from {

                opacity: 0;

                transform:
                    translateY(30px);

            }

            to {

                opacity: 1;

                transform:
                    translateY(0);

            }

        }


        @keyframes flotarCorazon {

            0%,
            100% {

                transform:
                    translateY(0);

            }

            50% {

                transform:
                    translateY(-15px);

            }

        }


        @keyframes florFlotando {

            0%,
            100% {

                transform:
                    translateY(0)
                    rotate(-3deg);

            }

            50% {

                transform:
                    translateY(-18px)
                    rotate(3deg);

            }

        }


        @keyframes latido {

            0%,
            100% {

                transform:
                    scale(1);

            }

            50% {

                transform:
                    scale(1.2);

            }

        }


        @keyframes moverNube {

            0% {

                transform:
                    translateX(-80px);

            }

            50% {

                transform:
                    translateX(80px);

            }

            100% {

                transform:
                    translateX(-80px);

            }

        }


        @keyframes crecer {

            from {

                bottom: -300px;

                opacity: 0;

                transform:
                    scale(0.3);

            }

            to {

                bottom: 0;

                opacity: 1;

                transform:
                    scale(1);

            }

        }



        /* =====================================
           CELULARES
        ===================================== */

        @media
        (max-width: 600px) {

            .botones {

                gap: 12px;

            }


            button {

                min-width: 110px;

                padding:
                    12px 25px;

            }


            #triste {

                margin-top:
                    240px;

                gap: 7px;

            }


            .cara-triste {

                font-size:
                    1.1rem;

            }


            #triste p {

                font-size:
                    0.9rem;

            }


            .mensaje-final {

                margin-top:
                    -20vh;

            }


            .sol {

                width: 70px;

                height: 70px;

            }

        }

    </style>
</head>


<body>


    <!-- =====================================
         PANTALLA 1
    ====================================== -->

    <section
        id="pantalla1"
        class="pantalla activa"
    >

        <span
            class="corazon c1"
        >
            ♥
        </span>

        <span
            class="corazon c2"
        >
            ♥
        </span>

        <span
            class="corazon c3"
        >
            ♥
        </span>

        <span
            class="corazon c4"
        >
            ♥
        </span>


        <h1 class="pregunta">

            Te amo,
            <br>

            ¿me amas?

        </h1>


        <div class="botones">


            <button
                onclick="respuestaSi()"
            >

                Sí

            </button>


            <button
                onclick="respuestaNo()"
            >

                No

            </button>


        </div>


        <div id="triste">


            <span
                class="cara-triste"
            >

                :(

            </span>


            <p>

                Eso dolió un poquito...

            </p>


        </div>


    </section>



    <!-- =====================================
         PANTALLA 2
    ====================================== -->

    <section
        id="pantalla2"
        class="pantalla"
    >


        <div
            class="girasol-grande"
        >

            🌻

        </div>


        <h1
            class="texto-flor"
        >

            Ten tu flor amarilla

        </h1>


        <div
            class="corazon-amarillo"
        >

            ♥

        </div>


    </section>



    <!-- =====================================
         PANTALLA FINAL
    ====================================== -->

    <section
        id="pantalla3"
        class="pantalla"
    >


        <div class="sol"></div>


        <div
            class="nube nube1"
        ></div>


        <div
            class="nube nube2"
        ></div>


        <div
            class="cerros"
        ></div>


        <div
            class="pasto"
        ></div>


        <h1
            class="mensaje-final"
        >

            Te amo
            <br>

            tres millones

        </h1>


        <div
            class="corazon-final"
        >

            ♡

        </div>


        <div
            id="jardin"
        ></div>


    </section>



    <script>


        const pantalla1 =
            document.getElementById(
                "pantalla1"
            );


        const pantalla2 =
            document.getElementById(
                "pantalla2"
            );


        const pantalla3 =
            document.getElementById(
                "pantalla3"
            );


        const triste =
            document.getElementById(
                "triste"
            );


        const jardin =
            document.getElementById(
                "jardin"
            );



        /* =====================================
           RESPUESTA NO
        ====================================== */

        function respuestaNo() {

            triste.classList.add(
                "mostrar"
            );

        }



        /* =====================================
           RESPUESTA SÍ
        ====================================== */

        function respuestaSi() {


            triste.classList.remove(
                "mostrar"
            );


            cambiarPantalla(
                pantalla1,
                pantalla2
            );


            /*
                La flor amarilla
                permanece durante
                5 segundos.
            */

            setTimeout(
                () => {


                    crearJardin();


                    cambiarPantalla(
                        pantalla2,
                        pantalla3
                    );


                },

                5000
            );

        }



        /* =====================================
           CAMBIO DE PANTALLA
        ====================================== */

        function cambiarPantalla(
            actual,
            siguiente
        ) {


            actual.classList.remove(
                "activa"
            );


            setTimeout(
                () => {


                    siguiente
                        .classList
                        .add(
                            "activa"
                        );


                },

                650
            );

        }



        /* =====================================
           CREAR JARDÍN
        ====================================== */

        function crearJardin() {


            jardin.innerHTML = "";


            const cantidad = 18;


            for (
                let i = 0;
                i < cantidad;
                i++
            ) {


                const flor =
                    document
                        .createElement(
                            "div"
                        );


                flor.className =
                    "flor";



                /* POSICIÓN */

                const posicion =

                    (
                        i /
                        (
                            cantidad - 1
                        )
                    )

                    * 96;


                flor.style.left =

                    posicion
                    + "%";



                /* TAMAÑO */

                const escala =

                    0.45

                    +

                    Math.random()
                    * 0.75;


                flor.style.scale =
                    escala;



                /* ALTURA */

                const altura =

                    80

                    +

                    Math.random()
                    * 180;



                /* RETRASO DE APARICIÓN */

                flor.style.animationDelay =

                    (
                        Math.random()
                        * 1.2
                    )

                    + "s";



                flor.innerHTML = `


                    <div
                        class="cabeza"
                    >


                        <div
                            class="petalo"
                        ></div>


                        <div
                            class="petalo"
                        ></div>


                        <div
                            class="petalo"
                        ></div>


                        <div
                            class="petalo"
                        ></div>


                        <div
                            class="petalo"
                        ></div>


                        <div
                            class="petalo"
                        ></div>


                        <div
                            class="petalo"
                        ></div>


                        <div
                            class="petalo"
                        ></div>


                        <div
                            class="centro"
                        ></div>


                    </div>


                    <div
                        class="tallo"
                        style="
                            height:
                            ${altura}px
                        "
                    ></div>


                `;


                jardin.appendChild(
                    flor
                );


            }


        }


    </script>


</body>
</html>
"""


@app.route("/")
def inicio():
    return render_template_string(HTML)


if __name__ == "__main__":

    # Render proporciona automáticamente
    # el puerto mediante la variable PORT.
    # En localhost utilizará el puerto 5000.

    port = int(
        os.environ.get(
            "PORT",
            5000
        )
    )

    app.run(
        host="0.0.0.0",
        port=port
    )
