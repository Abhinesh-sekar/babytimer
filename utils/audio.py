def get_alert_sound_html():
    return """
    <div id="alarm-container" style="text-align: center; margin: 20px auto;">
        <audio autoplay loop style="display: block; margin: 0 auto;">
            <source src="https://raw.githubusercontent.com/Abhinesh-sekar/babytimer/main/resources/wake_up_call.mp3" type="audio/mp3">
            Your browser does not support the audio element.
        </audio>
    </div>
    """
