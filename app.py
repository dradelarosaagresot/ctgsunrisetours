from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ✅ Ruta de la página de inicio
@app.route("/")
def inicio():
    return render_template("inicio.html")

# ✅ Ruta para la página de reservas
@app.route("/reserva", methods=["GET", "POST"])
def reserva():
    tour = request.args.get("tour", "")  # Captura el tour desde la URL
    return render_template("reserva_form.html", tour=tour)

# ✅ Ruta para procesar la reserva y enviar a WhatsApp
@app.route("/procesar_reserva", methods=["POST"])
def procesar_reserva():
    nombre = request.form["nombre"]
    celular = request.form["celular"]
    tour = request.form["tour"]
    fecha = request.form["fecha"]
    cantidad = request.form["cantidad"]

    # 📌 Número de WhatsApp Business (cambia este número al tuyo)
    numero_whatsapp = "573125680394"

    # 📌 Crear el mensaje con los datos de la reserva (evitando saltos de línea)
    mensaje = (
        f"Hola, quiero reservar un tour:%0A"
        f"📝 Nombre: {nombre}%0A"
        f"📅 Fecha: {fecha}%0A"
        f"🏝️ Tour: {tour}%0A"
        f"👥 Cantidad de personas: {cantidad}%0A"
        f"📲 Contacto: {celular}"
    )

    # 📌 Generar el enlace de WhatsApp con codificación URL correcta
    enlace_whatsapp = f"https://wa.me/{numero_whatsapp}?text={mensaje}"

    # ✅ Redirigir a WhatsApp
    return redirect(enlace_whatsapp)

# ✅ Otras rutas del menú
@app.route("/baru")
def baru():
    return render_template("baru.html")

@app.route("/islas-del-rosario")
def rosario():
    return render_template("rosario.html")

@app.route("/cenas-y-atardeceres")
def cenas():
    return render_template("cenas.html")

@app.route("/city-tour")
def city_tour():
    return render_template("city_tour.html")

@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")

@app.route("/galeria")
def galeria():
    return render_template("galeria.html")


# ✅ Ruta para la página de reserva
@app.route("/reservar")
def reservar():
    tour = request.args.get("tour", "")  # Captura el tour de la URL
    return render_template("reserva_form.html", tour=tour)  # Envíalo al formulario

if __name__ == "__main__":
    app.run(debug=True)


