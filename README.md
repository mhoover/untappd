# Untappd API

## Introduction
This repo provides some wrappers on the [Untappd](http://untappd.com) API. *It is not comprehensive* and should be used as a starting point to develop more functionality. Since it does not use OAuth 2.0, this does not allow one to utilize the notification or 'actions' functionality of the Untappd API.

See [the official documentation](https://untappd.com/api/docs) for functionality and optional parameters that can be passed. See below for basic usage.

## Usage
The `Untappd()`class has four methods defined on it to use with the Untappd API, `info`, `search`, `feed`, and `specific_feed`. Parameters (from Untappd itself) for each of these are described below.

### `info`
The `info` method is useful in collection user/beer/brewery information. It requires three named arguments -- `entity`, `action`, and `identity`.

* `entity`: One of user, beer, brewery, or venue. This indicates on what the API will gather information.
* `action`: This specifies what type of information is collected on an API call. For an `entity` of 'user' then info, wishlist, friends, badges, or beers can be used. For others, only info is available.
* `identity`: This identifies which person (Untappd user id), beer (integer), brewery (integer), or venue (integer) the call is collecting information on.

### `search`
The `search` method can be used to find information on either beers or breweries. Unlike the `info` method, there is one parameter needed to specify the endpoint address (`entity`) and one required parameter in the query itself (`q`).

* `entity`: One of beer or brewery. This indicates on what the API will gather information.
* `q`: This is the term that is actually searched, i.e., the name of the beer if `entity=beer` or the brewery if otherwise.

### `feed`
The `feed` method is used to obtain information on check-ins for people, beers, venues, and breweries. It accepts two arguments for the endpoint and a variety of option parameter arguments.

* `entity`: One of user, beer, brewery, or venue. This indicates on what the API will gather information.
* `identity`: This identifies which person (Untappd user id), beer (integer), brewery (integer), or venue (integer) the call is collecting information on.

### `pub`
This method collects information on public feed information for anyone within a certain radius of a specific location. It takes two required arguments, `lat` and `lon`, which represent the latitude and longitude to search from. These are both floats.

## Optional terms
For each method, there are a variety of optional arguments that can be used for a specific call. The table below outlines what the optional parameters are, what they mean, how they should be entered and which calls they can be used with.

| Parameter | Meaning | Representation | Calls |
| --- | --- | --- | --- |
| `compact` | Show minimal information | bool | info/user (info), info/beer, info/brewery, info/venue |
| `dist_pref` | Results in miles ('m') or kilometers ('km') | str | pub |
| `limit` | Number of results to return (default=25, max=50) | int | info/user (wishlist, friends, badges, beer), search/beer, search/brewery, feed, pub |
| `max_id` | Check-in ID results should start from | int | feed |
| `min_id` | Returns check-ins newer than this value | int | feed |
| `offset` | Number of offset start results from | int | info/user (wishlist, friends, badges, beer), search/beer, search/brewery |
| `radius` | Maxium radius to search (default/max=25) | int | pub |
| `sort` | How to sort results: 'date' (default), 'checkin', 'highest_rated', 'lowest_rated', 'highest_abv', 'lowest_abv' | str | info/user (wishlist) |
| `sort` | How to sort results: 'date' (default), 'checkin', 'highest_rated', 'lowest_rated', 'highed_rated_you', 'lowest_rated_you' | str | info/user (beer) |
| `sort` | How to sort results: 'checkin' (default), 'name' | str | search/beer |

## Usage
Some basic and more advanced usage listed below:
```
# open link to API (assumes Untappd API key/secret defined as
# environmental variables)
client = Untappd(os.getenv('MYKEY'), os.getenv('MYSECRET'))

# basic call for user information
user_info = client.info('user', 'info', 'my-untappd-id')

# call for user information with optional parameters
user_info = client.info('user', 'info', 'my-untappd-id', compact=True)

# search for beer with optional parameters
stone_ipa = client.search('beer', q='Stone IPA', limit=35, sort='name')

# activity feed for beer (Stone IPA)
stone_activity = client.feed('beer', 821)
```

## Conclusion
This repo is nowhere near complete or totally functional. There is no logging (coming soon...) or error handling (also coming soon...) so use at your own risk. Have fun! Questions or concerns? Email matthew.a.hoover at gmail.com.
