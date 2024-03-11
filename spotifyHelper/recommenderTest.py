import requests

# url = "https://spotify23.p.rapidapi.com/recommendations/"
#
querystring = {"limit": "1", "seed_tracks": "0c6xIDDpzE81m2q797ordA", "seed_genres": "classical,country"}
#
headers = {
    "X-RapidAPI-Key": "41db0ae0dbmshb4369a7209144dap1bf6e5jsn8938fa198638",
    "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
}
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())

d = {'tracks': [{'album': {'album_type': 'COMPILATION', 'artists': [
    {'external_urls': {'spotify': 'https://open.spotify.com/artist/3THMgU4KdL7LlO5TEREs2g'},
     'id': '3THMgU4KdL7LlO5TEREs2g', 'name': 'Joe Diffie', 'type': 'artist',
     'uri': 'spotify:artist:3THMgU4KdL7LlO5TEREs2g'}],
                           'available_markets': ['AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY',
                                                 'CZ', 'DK', 'DO', 'DE', 'EC', 'EE', 'SV', 'FI', 'FR', 'GR', 'GT', 'HN',
                                                 'HK', 'HU', 'IS', 'IE', 'IT', 'LV', 'LT', 'LU', 'MY', 'MT', 'MX', 'NL',
                                                 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE', 'PH', 'PL', 'PT', 'SG', 'SK', 'ES',
                                                 'SE', 'CH', 'TW', 'TR', 'UY', 'US', 'GB', 'AD', 'LI', 'MC', 'ID', 'JP',
                                                 'TH', 'VN', 'RO', 'IL', 'ZA', 'SA', 'AE', 'BH', 'QA', 'OM', 'KW', 'EG',
                                                 'MA', 'DZ', 'TN', 'LB', 'JO', 'PS', 'IN', 'BY', 'KZ', 'MD', 'UA', 'AL',
                                                 'BA', 'HR', 'ME', 'MK', 'RS', 'SI', 'KR', 'BD', 'PK', 'LK', 'GH', 'KE',
                                                 'NG', 'TZ', 'UG', 'AG', 'AM', 'BS', 'BB', 'BZ', 'BT', 'BW', 'BF', 'CV',
                                                 'CW', 'DM', 'FJ', 'GM', 'GE', 'GD', 'GW', 'GY', 'HT', 'JM', 'KI', 'LS',
                                                 'LR', 'MW', 'MV', 'ML', 'MH', 'FM', 'NA', 'NR', 'NE', 'PW', 'PG', 'WS',
                                                 'SM', 'ST', 'SN', 'SC', 'SL', 'SB', 'KN', 'LC', 'VC', 'SR', 'TL', 'TO',
                                                 'TT', 'TV', 'VU', 'AZ', 'BN', 'BI', 'KH', 'CM', 'TD', 'KM', 'GQ', 'SZ',
                                                 'GA', 'GN', 'KG', 'LA', 'MO', 'MR', 'MN', 'NP', 'RW', 'TG', 'UZ', 'ZW',
                                                 'BJ', 'MG', 'MU', 'MZ', 'AO', 'CI', 'DJ', 'ZM', 'CD', 'CG', 'IQ', 'LY',
                                                 'TJ', 'VE', 'ET', 'XK'],
                           'external_urls': {'spotify': 'https://open.spotify.com/album/7KOqXNB8MrQBBuIasId2Zn'},
                           'id': '7KOqXNB8MrQBBuIasId2Zn', 'images': [
        {'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b2735546f2ac6abc9cddd1c97556', 'width': 640},
        {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e025546f2ac6abc9cddd1c97556', 'width': 300},
        {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d000048515546f2ac6abc9cddd1c97556', 'width': 64}],
                           'name': 'The Essential Joe Diffie', 'release_date': '2003-03-31',
                           'release_date_precision': 'day', 'total_tracks': 14, 'type': 'album',
                           'uri': 'spotify:album:7KOqXNB8MrQBBuIasId2Zn'}, 'artists': [
    {'external_urls': {'spotify': 'https://open.spotify.com/artist/3THMgU4KdL7LlO5TEREs2g'},
     'id': '3THMgU4KdL7LlO5TEREs2g', 'name': 'Joe Diffie', 'type': 'artist',
     'uri': 'spotify:artist:3THMgU4KdL7LlO5TEREs2g'}],
                 'available_markets': ['AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ',
                                       'DK',
                                       'DO', 'DE', 'EC', 'EE', 'SV', 'FI', 'FR', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS',
                                       'IE',
                                       'IT', 'LV', 'LT', 'LU', 'MY', 'MT', 'MX', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY',
                                       'PE',
                                       'PH', 'PL', 'PT', 'SG', 'SK', 'ES', 'SE', 'CH', 'TW', 'TR', 'UY', 'US', 'GB',
                                       'AD',
                                       'LI', 'MC', 'ID', 'JP', 'TH', 'VN', 'RO', 'IL', 'ZA', 'SA', 'AE', 'BH', 'QA',
                                       'OM',
                                       'KW', 'EG', 'MA', 'DZ', 'TN', 'LB', 'JO', 'PS', 'IN', 'BY', 'KZ', 'MD', 'UA',
                                       'AL',
                                       'BA', 'HR', 'ME', 'MK', 'RS', 'SI', 'KR', 'BD', 'PK', 'LK', 'GH', 'KE', 'NG',
                                       'TZ',
                                       'UG', 'AG', 'AM', 'BS', 'BB', 'BZ', 'BT', 'BW', 'BF', 'CV', 'CW', 'DM', 'FJ',
                                       'GM',
                                       'GE', 'GD', 'GW', 'GY', 'HT', 'JM', 'KI', 'LS', 'LR', 'MW', 'MV', 'ML', 'MH',
                                       'FM',
                                       'NA', 'NR', 'NE', 'PW', 'PG', 'WS', 'SM', 'ST', 'SN', 'SC', 'SL', 'SB', 'KN',
                                       'LC',
                                       'VC', 'SR', 'TL', 'TO', 'TT', 'TV', 'VU', 'AZ', 'BN', 'BI', 'KH', 'CM', 'TD',
                                       'KM',
                                       'GQ', 'SZ', 'GA', 'GN', 'KG', 'LA', 'MO', 'MR', 'MN', 'NP', 'RW', 'TG', 'UZ',
                                       'ZW',
                                       'BJ', 'MG', 'MU', 'MZ', 'AO', 'CI', 'DJ', 'ZM', 'CD', 'CG', 'IQ', 'LY', 'TJ',
                                       'VE',
                                       'ET', 'XK'], 'disc_number': 1, 'duration_ms': 216173, 'explicit': False,
                 'external_ids': {'isrc': 'USSM19401995'},
                 'external_urls': {'spotify': 'https://open.spotify.com/track/3dSUY34vmIYWJn0M6oZ3BD'},
                 'id': '3dSUY34vmIYWJn0M6oZ3BD', 'is_local': False, 'name': 'Pickup Man', 'popularity': 47,
                 'preview_url': 'https://p.scdn.co/mp3-preview/01647d3a212d11283caf6d069bbc3c25f91ca90a?cid=d8a5ed958d274c2e8ee717e6a4b0971d',
                 'track_number': 10, 'type': 'track', 'uri': 'spotify:track:3dSUY34vmIYWJn0M6oZ3BD'}], 'seeds': [
    {'initialPoolSize': 500, 'afterFilteringSize': 417, 'afterRelinkingSize': 417, 'id': '0c6xIDDpzE81m2q797ordA',
     'type': 'TRACK'},
    {'initialPoolSize': 517, 'afterFilteringSize': 417, 'afterRelinkingSize': 417, 'id': 'classical', 'type': 'GENRE',
     'href': None},
    {'initialPoolSize': 999, 'afterFilteringSize': 417, 'afterRelinkingSize': 417, 'id': 'country', 'type': 'GENRE',
     'href': None}]}

name = d['tracks'][0]['name']
print(name)
