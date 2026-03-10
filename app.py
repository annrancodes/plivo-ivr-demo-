from flask import Flask, request, Response
import plivo

app = Flask(__name__)

@app.route("/ivr", methods=["GET", "POST"])
def ivr():
    response = plivo.voice_response.Response()

    getdigits = plivo.voice_response.GetDigits(
        action="/handle_language",
        method="POST",
        num_digits=1,
        timeout=5
    )

    getdigits.add_speak(
        "Press 1 for English. Press 2 for Spanish.",
        language="en-US"
    )

    response.add(getdigits)
    response.add_speak("No input received. Goodbye.")

    return Response(response.to_xml(), mimetype="text/xml")


@app.route("/handle_language", methods=["POST"])
def handle_language():
    digit = request.form.get("Digits")

    response = plivo.voice_response.Response()

    if digit == "1":
        language = "English"
    elif digit == "2":
        language = "Spanish"
    else:
        response.add_speak("Invalid input.")
        response.add_redirect("/ivr")
        return Response(response.to_xml(), mimetype="text/xml")

    getdigits = plivo.voice_response.GetDigits(
        action="/handle_action",
        method="POST",
        num_digits=1,
        timeout=5
    )

    getdigits.add_speak(
        f"You selected {language}. Press 1 to hear a message. Press 2 to connect to an associate."
    )

    response.add(getdigits)
    response.add_speak("No input received. Goodbye.")

    return Response(response.to_xml(), mimetype="text/xml")


@app.route("/handle_action", methods=["POST"])
def handle_action():
    digit = request.form.get("Digits")

    response = plivo.voice_response.Response()

    if digit == "1":
        response.add_play("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

    elif digit == "2":
        dial = plivo.voice_response.Dial()
        dial.add_number("14692463990")   # placeholder associate number
        response.add(dial)

    else:
        response.add_speak("Invalid input.")
        response.add_redirect("/ivr")

    return Response(response.to_xml(), mimetype="text/xml")


if __name__ == "__main__":
    app.run(port=5000)
