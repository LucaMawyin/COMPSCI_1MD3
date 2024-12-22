from typing import List


def get_bandnames(file_name: str) -> List[str]:
    '''Return a list of all of the bandnames in a band file.
    '''

    file = open(file_name,"r")

    band_rating_plays = []

    file.readline()

    for line in file:
        band_rating_plays.append(line.split(",")[0])

    file.close()


    return band_rating_plays

def average_rating(file_name: str) -> float:
    '''Return the average rating for all bands in band_file.
    '''

    file = open(file_name,"r")
    file.readline()

    avg = 0
    count = 0

    for line in file:
        avg += float(line.split(",")[1])
        count += 1

    file.close()

    return avg / count

def average_plays(file_name: str) -> float:
    ''' Return average rating for all bands in band_file.
    '''

    file = open(file_name,"r")
    file.readline()

    avg = 0
    count = 0

    for line in file:
        avg += float(line.split(",")[2])
        count += 1

    file.close()

    return avg / count

def create_playlist(file_name:str, playlist_name:str, threshold:int):
    """
    Writes a file named play_listname with bands having a rating greater
    than of equal to threshold
    """

    # Open file
    file = open(file_name,"r")

    # Just being a bit more modular
    if playlist_name[-4:] != ".txt":
        playlist_name += ".txt"

    playlist = open(playlist_name, "w")

    file.readline()


    # Getting each artist & info
    for line in file:
        current = line.split(",")
        
        # Adding artist with higher rating than threshold
        if int(current[1]) >= threshold:
            playlist.write(current[0]+","+current[1]+"\n")

    file.close()

def get_guilty_pleasures(file_name:str, playlist_name:str):
    streamThreshold = average_plays(file_name)
    rateThreshold = average_rating(file_name)

    file = open(file_name,"r")
    file.readline()

    guilty_pleasures = open(playlist_name,"w")

    for line in file:
        if int(line.split(",")[1]) < rateThreshold and int(line.split(",")[2]) > streamThreshold:
            guilty_pleasures.writelines(line)

    file.close()
    guilty_pleasures.close()

def get_poser(file_name:str,playlist_name:str):
    streamThreshold = average_plays(file_name)
    rateThreshold = average_rating(file_name)

    file = open(file_name,"r")
    file.readline()

    poser_playlist = open(playlist_name,"w")

    for line in file:
        if int(line.split(",")[1]) > rateThreshold and int(line.split(",")[2]) < streamThreshold:
            poser_playlist.writelines(line)

    file.close()
    poser_playlist.close()