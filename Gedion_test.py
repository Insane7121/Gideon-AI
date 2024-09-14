import datetime
import sys
import unittest
from unittest.mock import MagicMock, patch

# Assuming the original script is named gideonAI.py and we import its functions
from gideonAI import sendEmail, speak, takeCommand, wishMe  # type: ignore


class TestGideonAI(unittest.TestCase):
    
    @patch('gideonAI.engine.say')
    @patch('gideonAI.engine.runAndWait')
    def test_speak(self, mock_runAndWait, mock_say):
        """Test the speak function with valid input."""
        speak("Hello")
        mock_say.assert_called_with("Hello")
        mock_runAndWait.assert_called_once()

    @patch('gideonAI.datetime.datetime')
    @patch('gideonAI.speak')
    def test_wishMe_morning(self, mock_speak, mock_datetime):
        """Test the wishMe function during morning hours."""
        mock_datetime.now.return_value = datetime.datetime(2024, 9, 15, 9, 0, 0)  # 9:00 AM
        wishMe()
        mock_speak.assert_any_call("Good morning!")
        mock_speak.assert_any_call("I am Gideon. Sir, please tell me how may I help you")

    @patch('gideonAI.datetime.datetime')
    @patch('gideonAI.speak')
    def test_wishMe_afternoon(self, mock_speak, mock_datetime):
        """Test the wishMe function during afternoon hours."""
        mock_datetime.now.return_value = datetime.datetime(2024, 9, 15, 14, 0, 0)  # 2:00 PM
        wishMe()
        mock_speak.assert_any_call("Good afternoon!")
        mock_speak.assert_any_call("I am Gideon. Sir, please tell me how may I help you")

    @patch('gideonAI.datetime.datetime')
    @patch('gideonAI.speak')
    def test_wishMe_evening(self, mock_speak, mock_datetime):
        """Test the wishMe function during evening hours."""
        mock_datetime.now.return_value = datetime.datetime(2024, 9, 15, 19, 0, 0)  # 7:00 PM
        wishMe()
        mock_speak.assert_any_call("Good evening!")
        mock_speak.assert_any_call("I am Gideon. Sir, please tell me how may I help you")

    @patch('gideonAI.sr.Recognizer.listen')
    @patch('gideonAI.sr.Recognizer.recognize_google')
    @patch('gideonAI.sr.Microphone')
    def test_takeCommand_valid(self, mock_microphone, mock_recognize_google, mock_listen):
        """Test the takeCommand function with valid speech input."""
        mock_recognize_google.return_value = "open google"
        command = takeCommand()
        self.assertEqual(command, "open google")

    @patch('gideonAI.sr.Recognizer.listen')
    @patch('gideonAI.sr.Recognizer.recognize_google', side_effect=Exception("Error"))
    @patch('gideonAI.sr.Microphone')
    def test_takeCommand_exception(self, mock_microphone, mock_recognize_google, mock_listen):
        """Test the takeCommand function when an exception occurs."""
        command = takeCommand()
        self.assertEqual(command, "none")

    @patch('gideonAI.smtplib.SMTP')
    @patch('gideonAI.speak')
    def test_sendEmail_success(self, mock_speak, mock_smtp):
        """Test the sendEmail function for a successful email send."""
        mock_server = MagicMock()
        mock_smtp.return_value = mock_server

        sendEmail("test@example.com", "This is a test")
        mock_server.login.assert_called_with('your_email@gmail.com', 'your_password')
        mock_server.sendmail.assert_called_with('your_email@gmail.com', 'test@example.com', 'This is a test')
        mock_speak.assert_called_with("Email has been sent successfully!")

    @patch('gideonAI.smtplib.SMTP', side_effect=Exception("SMTP error"))
    @patch('gideonAI.speak')
    def test_sendEmail_failure(self, mock_speak, mock_smtp):
        """Test the sendEmail function when email sending fails."""
        sendEmail("test@example.com", "This is a test")
        mock_speak.assert_called_with("Sorry, I am unable to send the email.")


if __name__ == '__main__':
    unittest.main()
