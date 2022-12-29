# Install

```
pip install encurtanet
```

# Simple use example

```py
from encurtanet import EncurtaNet, NO_ADS, INTERSTITIALS_ADS

shortener = EncurtaNet("YOUR API TOKEN HERE")

url_info = shortener.shorten(
    "https://marcuth.github.io/", # Your url
    "url-alias", # Alias of the url
    True, # If response is text format
    NO_ADS # Ads type
)

shortened_url = url_info.get_shortened_url()

print(shortened_url)
```