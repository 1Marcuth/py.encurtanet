from encurtanet import EncurtaNet, NO_ADS, INTERSTITIALS_ADS

shortener = EncurtaNet("YOUR API TOKEN HERE")

url_info = shortener.shorten(
    url="https://google.com/", # URL you want to shorten
    alias="MyAlias", # URL alias
    is_text_format=False, # whether the result from the server is going to be text
    ads_type=INTERSTITIALS_ADS #ad type, you can define two types, there is no way to define banner :v and also you don't need to define if you want with ad
)

url_info.get() # result of all 
url_info.get_shortened_url() # resulting URL
url_info.get_status() # resulting status ( success | error )
url_info.get_message() # resulting message (if the api sent a message)
