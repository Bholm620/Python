class Song:
    def __init__(self, title, artist, album, duration_minutes, duration_seconds):
        self.title = title
        self.artist = artist
        self.album = album
        # Private attribute to store duration in seconds
        self.__duration_seconds = self._convert_to_seconds(duration_minutes, duration_seconds) 

    def _convert_to_seconds(self, minutes, seconds): 
        """
        A private method to convert minutes and seconds to total seconds.
        This method is meant for internal class use only.
        """
        return minutes * 60 + seconds

    def get_duration_formatted(self):
        """
        Public method to retrieve the duration in a human-readable format (minutes:seconds).
        """
        minutes = self.__duration_seconds // 60
        seconds = self.__duration_seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

    def get_duration_in_seconds(self):
        """
        Public method to retrieve the duration in seconds.
        """
        return self.__duration_seconds

    def set_duration(self, minutes, seconds):
        """
        Public method to update the duration. 
        It uses the private method to ensure the duration is stored correctly.
        """
        if minutes >= 0 and seconds >= 0 and seconds < 60:
            self.__duration_seconds = self._convert_to_seconds(minutes, seconds)
        else:
            print("Invalid duration provided.")

# Example usage:
my_song = Song("Bohemian Rhapsody", "Queen", "A Night at the Opera", 5, 55)

print(f"Title: {my_song.title}")  # Accessing a public attribute
print(f"Artist: {my_song.artist}")
print(f"Album: {my_song.album}")
print(f"Duration (formatted): {my_song.get_duration_formatted()}") # Accessing private attribute via getter
print(f"Duration (in seconds): {my_song.get_duration_in_seconds()}")

# Attempting to access the private attribute directly (will not work as expected due to name mangling)
# print(my_song.__duration_seconds) # This would raise an AttributeError or access the mangled name, which is not recommended

# Modifying the duration using the setter method
my_song.set_duration(6, 10)
print(f"New duration (formatted): {my_song.get_duration_formatted()}")

# Attempting to set an invalid duration
my_song.set_duration(-1, 30)
