import speech_recognition as sr
import pyttsx3

class AudioHandle:
    def __init__(self):
        """
        Initialize object to record voice input from a physical microphone
        """
        self.r = sr.Recognizer()
        with sr.Microphone() as source:
            self.audio = self.r.listen(source)

    def record(self):
        """
        Convert recorded input to response speech
        :return: Return response speech as a string
        """

        try:
            response = self.r.recognize_google(self.audio)
            self._engine_response('Now playing ' + response)

        except sr.UnknownValueError:
            self._engine_response('Command is not recognized')

        except sr.RequestError as e:
            print("RequestError: ".format(e))

        except ConnectionResetError as e:
            print("ConnectionResetError: ".format(e))

        return response

    @staticmethod
    def _engine_response(command):
        """
        Plays an audio response from string parameter input
        :param command: Takes in a string to complete audio response
        """
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[7].id)
        engine.say(command)
        engine.runAndWait()