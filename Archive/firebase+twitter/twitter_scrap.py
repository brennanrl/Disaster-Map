import twitter
api = twitter.Api(consumer_key="",
                  consumer_secret="",
                  access_token_key="",
                  access_token_secret="",
                  sleep_on_rate_limit=True, tweet_mode="extended")
import json
import requests
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
import unidecode
import urllib.parse as uparse
import re

subscription_key = ""
endpoint = ""

credentials = CognitiveServicesCredentials(subscription_key)
text_analytics = TextAnalyticsClient(endpoint=endpoint, credentials=credentials)

import firebase_admin
from firebase_admin import messaging
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("./creds.json")
firebase_admin.initialize_app(cred, {
  "databaseURL": ""
})

firebase_dict = dict()

count = 0
for i, s in enumerate(api.GetStreamFilter(track=["blast", "typhoon", "flood crisis",
  "victims",
  "flood victims",
  "flood powerful",
  "powerful storms",
  "hoisted flood",
  "storms amazing",
  "explosion",
  "amazing rescue",
  "rescue women",
  "flood cost",
  "counts flood",
  "toll rises",
  "braces river",
  "river peaks",
  "crisis deepens",
  "prayers",
  "thoughts prayers",
  "affected tornado",
  "affected",
  "death toll",
  "tornado relief",
  "photos flood",
  "water rises",
  "toll",
  "flood waters",
  "flood appeal",
  "victims explosion",
  "bombing suspect",
  "massive explosion",
  "affected areas",
  "praying victims",
  "injured",
  "please join",
  "join praying",
  "prayers people",
  "redcross",
  "text redcross",
  "visiting flood",
  "lurches fire",
  "video explosion",
  "deepens death",
  "opposed flood",
  "help flood",
  "died explosions",
  "marathon explosions",
  "flood relief",
  "donate",
  "first responders",
  "flood affected",
  "donate cross",
  "braces",
  "tornado victims",
  "deadly",
  "prayers affected",
  "explosions running",
  "evacuated",
  "relief",
  "flood death",
  "deaths confirmed",
  "affected flooding",
  "people killed",
  "dozens",
  "footage",
  "survivor finds",
  "worsens eastern",
  "flood worsens",
  "flood damage",
  "people dead",
  "girl died",
  "flood",
  "donation help",
  "major flood",
  "rubble",
  "another explosion",
  "confirmed dead",
  "rescue",
  "send prayers",
  "flood warnings",
  "tornado survivor",
  "damage",
  "devastating",
  "flood toll",
  "affected hurricane",
  "prayers families",
  "releases photos",
  "hundreds injured",
  "inundated",
  "crisis",
  "text donation",
  "redcross give",
  "recede",
  "bombing",
  "massive",
  "bombing victims",
  "explosion ripped",
  "gets donated",
  "donated victims",
  "relief efforts",
  "news flood",
  "flood emergency",
  "give online",
  "fire flood",
  "huge explosion",
  "bushfire",
  "torrential rains",
  "residents",
  "breaking news",
  "redcross donate",
  "affected explosion",
  "disaster",
  "someone captured",
  "tragedy",
  "enforcement",
  "people injured",
  "twister",
  "blast",
  "crisis deepens",
  "injuries reported",
  "fatalities",
  "donated million",
  "donations assist",
  "dead explosion",
  "survivor",
  "death",
  "suspect dead",
  "peaks deaths",
  "love prayers",
  "explosion fertiliser",
  "explosion reported",
  "return home",
  "evacuees",
  "large explosion",
  "firefighters",
  "morning flood",
  "praying",
  "public safety",
  "txting redcross",
  "destroyed",
  "displaced",
  "fertilizer explosion",
  "unknown number",
  "donate tornado",
  "retweet donate",
  "flood tornado",
  "casualties",
  "climate change",
  "financial donations",
  "stay strong",
  "dead hundreds",
  "major explosion",
  "bodies recovered",
  "waters recede",
  "response disasters",
  "victims donate",
  "unaccounted",
  "fire fighters",
  "explosion victims",
  "prayers city",
  "accepting financial",
  "torrential",
  "bomber",
  "disasters txting",
  "explosion registered",
  "missing flood",
  "volunteers",
  "brought hurricane",
  "relief fund",
  "help tornado",
  "explosion fire",
  "ravaged",
  "prayers tonight",
  "tragic",
  "enforcement official",
  "saddened",
  "dealing hurricane",
  "impacted",
  "flood recovery",
  "stream",
  "dead torrential",
  "flood years",
  "nursing",
  "recover",
  "responders",
  "massive tornado",
  "buried alive",
  "alive rubble",
  "crisis rises",
  "flood peak",
  "homes inundated",
  "flood ravaged",
  "explosion video",
  "killed injured",
  "killed people",
  "people died",
  "missing explosion",
  "make donation",
  "floods kill",
  "tornado damage",
  "entire crowd",
  "cross tornado",
  "terrifying",
  "need terrifying",
  "even scary",
  "cost deaths",
  "facing flood",
  "deadly explosion",
  "dead missing",
  "floods force",
  "flood disaster",
  "tornado disaster",
  "medical examiner",
  "help victims",
  "hundreds homes",
  "severe flooding",
  "shocking video",
  "bombing witnesses",
  "magnitude",
  "firefighters police",
  "fire explosion",
  "storm",
  "flood hits",
  "floodwaters",
  "emergency",
  "flash flood",
  "flood alerts",
  "crisis unfolds",
  "daring rescue",
  "tragic events",
  "medical office",
  "deadly tornado",
  "people trapped",
  "police officer",
  "explosion voted",
  "lives hurricane",
  "bombings reports",
  "breaking suspect",
  "bombing investigation",
  "praying affected",
  "reels surging",
  "surging floods",
  "teenager floods",
  "rescue teenager",
  "appeal launched",
  "explosion injured",
  "injured explosion",
  "responders killed",
  "explosion caught",
  "city tornado",
  "help text",
  "name hurricane",
  "damaged hurricane",
  "breaking arrest",
  "suspect bombing",
  "massive manhunt",
  "releases images",
  "shot killed",
  "rains severely",
  "house flood",
  "live coverage",
  "devastating tornado",
  "lost lives",
  "reportedly dead",
  "following explosion",
  "remember lives",
  "tornado flood",
  "want help",
  "seconds bombing",
  "reported dead",
  "imminent",
  "rebuild",
  "safe hurricane",
  "surviving",
  "injuries",
  "prayers victims",
  "police suspect",
  "warning",
  "help affected",
  "kills forces",
  "dead floods",
  "flood threat",
  "military",
  "flood situation",
  "thousands homes",
  "risk running",
  "dead injured",
  "dying hurricane",
  "loss life",
  "thoughts victims",
  "bombing shot",
  "breaking enforcement",
  "police people",
  "video capturing",
  "feared dead",
  "terrible explosion",
  "prayers involved",
  "reported injured",
  "seismic",
  "victims waters",
  "flood homeowners",
  "flood claims",
  "homeowners reconnect",
  "reconnect power",
  "power supplies",
  "rescuers help",
  "free hotline",
  "hotline help",
  "please stay",
  "investigation",
  "saddened loss",
  "identified suspect",
  "bombings saddened",
  "killed police",
  "dead",
  "praying community",
  "registered magnitude",
  "leave town",
  "reported explosion",
  "heart praying",
  "life heart",
  "prepare hurricane",
  "landfall",
  "crisis worsens",
  "arrest",
  "bombing case",
  "suspect run",
  "communities damaged",
  "destruction",
  "levy",
  "tornado",
  "hurricane coming",
  "toxins flood",
  "release toxins",
  "toxins",
  "supplies waters",
  "crisis found",
  "braces major",
  "government negligent",
  "attack",
  "hurricane",
  "rebuilt communities",
  "help rebuilt",
  "rebuilt",
  "rescuers",
  "buried",
  "heart prayers",
  "flood levy",
  "watch hurricane",
  "victims lost",
  "soldier",
  "waiting hurricane",
  "run massive",
  "high river",
  "terror",
  "memorial service",
  "terror attack",
  "coast hurricane",
  "terrified hurricane",
  "aftermath",
  "suspect killed",
  "suspect pinned",
  "lost legs",
  "hurricane category",
  "names terrified",
  "authorities",
  "assist people",
  "hurricane black",
  "unknown soldier",
  "events",
  "safety",
  "troops",
  "disaster relief",
  "cleanup",
  "troops lend",
  "effected hurricane",
  "time hurricane",
  "saying hurricane",
  "praying families",
  "dramatic",
  "path hurricane"], languages=["en"])):
    tweet = twitter.Status.NewFromJsonDict(s) # json.dumps(s))
    if tweet.full_text is not None:
        text = tweet.full_text.replace("\n", " ")
        text = unidecode.unidecode(text)
        text = str(text.encode('ascii', errors='ignore'))
        # print(tweet)
        r = requests.post('http://0.0.0.0:443/calculate', json={"texts": [text]})
        ddict = r.json()['disasters']
        if ddict[0] != 'None':
            # print(text, ddict, tweet.created_at)
            documents = [
                {
                    "id": "1",
                    "language": "en",
                    "text": text
                }
            ]
            response = text_analytics.entities(documents=documents)
            locations = []
            for document in response.documents:
                # print("Document Id: ", document.id)
                # print("\tKey Entities:")
                
                for entity in document.entities:
                    if entity.type == 'Location':
                        locations.append(entity.name)
            if len(locations) > 0:
                print(text, ddict, tweet.created_at, locations)
                try:
                    response2 = text_analytics.key_phrases(documents=documents)
                    for document2 in response2.documents:
                        body = " | ".join([p for p in document2.key_phrases])
                            
                    best_loc_url = "https://maps.googleapis.com/maps/api/geocode/json?address="+uparse.quote(locations[0])+"&key="
                    loc_r = requests.get(best_loc_url)
                    loc_r_json = loc_r.json()
                    if loc_r_json['results'][0]['formatted_address'] == 'United States':
                        raise Exception
                    coords = loc_r_json['results'][0]['geometry']['location']
                    count += 1
                    fdict_key = loc_r_json['results'][0]['formatted_address']+"_nohash_"+ddict[0].lower()
                    firebase_dict[fdict_key] = firebase_dict.get(fdict_key, []) + [(coords['lat'], coords['lng'],
                                                                                    ddict[0].lower(),
                                                                                    body,
                                                                                    ddict[0]+" in "+loc_r_json['results'][0]['formatted_address'],
                                                                                    text)]
                    print(body)
#                     data = {}
#                     data["lat"] = coords['lat']
#                     data["long"] = coords['lng']
#                     data["type"] = ddict[0].lower()
#                     data["body"] = body
#                     data["headline"] = ddict[0]+" in "+loc_r_json['results'][0]['formatted_address']
#                     data["live"] = {0: text}
                    print(count)
                    if count % 97 == 0:
                        print(firebase_dict)
                        for k, v in firebase_dict.items():
                            all_texts = []
                            if len(v) > 1:
                                print("Useful: ", k)
                                for _, _, _, _, _, text in v:
                                    all_texts.append(text)
                                data = {}
                                data["lat"] = v[0][0]
                                data["long"] = v[0][1]
                                data["type"] = v[0][2]
                                data["body"] = v[0][3]
                                data["headline"] = v[0][4]
                                data["live"] = all_texts
                                print("FIREBASE UPDATE")
                                try:
                                    db.reference().child("incidents").child(k).set(data)
                                    message = messaging.Message(
                                        notification=messaging.Notification(
                                            title='MAS',
                                            body='New disaster.',
                                        ),
                                        topic=re.sub(r'[^A-Za-z0-9]', "_", locations[0].lower()),
                                    )
                                    response = messaging.send(message)
                                    firebase_dict[k].pop(0)
                                except Exception as e:
                                    print(e)
                            # else:
                            #     del firebase_dict[k]
                    if count % 141 == 0:
                        for k, v in firebase_dict.items():
                            db.reference().child("incidents").child(k).remove()
                except Exception as e:
                    print(e)
                    pass
    # print(tweet.full_text, tweet.truncated, tweet.text.replace("\n", " "), "\n")
    # if count == 1000:
        # break