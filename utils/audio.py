def get_alert_sound_html():
    """
    Returns HTML with embedded audio that automatically plays when break is over.
    Uses a clock alarm sound that loops until stopped.
    """
    return """
    <div id="alarm-container"></div>
    <script>
        // Function to play a simple clock alarm sound
        function playAlarm() {
            console.log("Attempting to play alarm sound...");
            
            // Create container for alarm controls
            const alarmContainer = document.getElementById("alarm-container");
            if (!alarmContainer) {
                console.error("Alarm container not found");
                return;
            }
            
            // Create audio element with clock alarm sound (reliable source)
            const clockAlarmSound = "https://soundbible.com/grab.php?id=2197&type=mp3";
            const audioElement = new Audio(clockAlarmSound);
            audioElement.loop = true;  // Important: make it loop continuously
            audioElement.volume = 1.0; // Full volume to ensure it's heard
            
            // Add visible audio controls as a fallback
            const audioControls = document.createElement("audio");
            audioControls.src = clockAlarmSound;
            audioControls.controls = true;
            audioControls.autoplay = true;
            audioControls.loop = true;
            audioControls.style.display = "block";
            audioControls.style.margin = "20px auto";
            alarmContainer.appendChild(audioControls);
            
            // Try to play the sound (this may fail due to autoplay policies)
            audioElement.play()
                .then(() => {
                    console.log("Alarm playing successfully");
                })
                .catch(error => {
                    console.error("Autoplay prevented:", error);
                    // Keep the visible controls so user can manually play
                });
            
            // Create stop button
            const stopButton = document.createElement("button");
            stopButton.innerText = "Stop Alarm";
            stopButton.style.padding = "12px 24px";
            stopButton.style.backgroundColor = "#ff4b4b";
            stopButton.style.color = "white";
            stopButton.style.border = "none";
            stopButton.style.borderRadius = "4px";
            stopButton.style.cursor = "pointer";
            stopButton.style.fontSize = "18px";
            stopButton.style.fontWeight = "bold";
            stopButton.style.display = "block";
            stopButton.style.margin = "20px auto";
            stopButton.style.boxShadow = "0 4px 8px rgba(0, 0, 0, 0.2)";
            
            // Add button functionality
            stopButton.onclick = function() {
                audioElement.pause();
                audioElement.currentTime = 0;
                audioControls.pause();
                audioControls.currentTime = 0;
                this.style.display = "none";
                audioControls.style.display = "none";
                
                // Show a message confirming alarm is stopped
                const alarmStoppedMsg = document.createElement("div");
                alarmStoppedMsg.innerText = "Alarm stopped";
                alarmStoppedMsg.style.textAlign = "center";
                alarmStoppedMsg.style.color = "#555";
                alarmStoppedMsg.style.margin = "10px 0";
                alarmContainer.appendChild(alarmStoppedMsg);
            };
            
            // Add the stop button to the container
            alarmContainer.appendChild(stopButton);
            
            // Add a text instruction for browsers that block autoplay
            const playInstructions = document.createElement("p");
            playInstructions.innerText = "If you don't hear the alarm, please click play on the audio controls above.";
            playInstructions.style.textAlign = "center";
            playInstructions.style.color = "#555";
            playInstructions.style.fontSize = "14px";
            alarmContainer.appendChild(playInstructions);
        }
        
        // Execute when page loads
        document.addEventListener("DOMContentLoaded", function() {
            console.log("DOM loaded, preparing to play alarm...");
            setTimeout(playAlarm, 1000);
        });
    </script>
    """