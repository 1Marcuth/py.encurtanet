from encurtanet import EncurtaNet, AdsTypes

encurtanet = EncurtaNet("YOUR API TOKEN HERE")

url_info = encurtanet.shorten(
    url = "https://marcuth.github.io/", # URL you want to shorten
    alias = "url-alias", # URL alias
    is_text_format = False, # Whether the result from the server is going to be text
    ads_type = AdsTypes.InterstitialAds # Ads type, you can define two types, there is no way to define banner and also you don't need to define if you want url with ads
)

url_info.raw_data # Result of all 
url_info.shortened_url # Resulting URL
url_info.status # Resulting status ("success" | "error")
url_info.message # Resulting message (if the api sent a message)