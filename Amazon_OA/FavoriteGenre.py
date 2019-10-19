import timeit
from collections import defaultdict, Counter
userMap = {
    "David": ["song1", "song2", "song3", "song4", "song8"],
    "Emma":  ["song5", "song6", "song7"]
}
genreMap = {}
#    "Rock":    ["song1", "song3"],
#    "Dubstep": ["song7"],
#    "Techno":  ["song2", "song4"],
#    "Pop":     ["song5", "song6"],
#    "Jazz":    ["song8", "song9"]
# }

Output: {  
   "David": ["Rock", "Techno"],
   "Emma":  ["Pop"]
}

def user_to_genre(userMap,genreMap):
    song_to_genre = {}
    for k, l in genreMap.items():
        for song in l:
            song_to_genre[song] = k
    
    ans = defaultdict(list)
    
    for user, song_list in userMap.items():
        genre_list = defaultdict(int)

        for song in song_list:
            if song in genre_list:
                genre_list[song_to_genre[song]] += 1
        most_common = Counter(genre_list).most_common()
        ans[user] = [item[0] for item in most_common if item[1] == most_common[0][1]]


    return ans
print(user_to_genre(userMap, genreMap))