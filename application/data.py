__author__ = 'Dani'

users = [
    {
        "id": 1,
        "email": "test@safepoint.com",
        "password": "098f6bcd4621d373cade4e832627b4f6"  # test
    }
]

categories = [
    {
        "id": 1,
        "name": "Abduction"
    },
    {
        "id": 2,
        "name": "Assault"
    },
    {
        "id": 3,
        "name": "Burglary"
    },
    {
        "id": 4,
        "name": "Fraud"
    },
    {
        "id": 5,
        "name": "Murder"
    },
    {
        "id": 6,
        "name": "Robbery"
    }

]

reports = [
    {
        "id": 1,
        "lat": 43.368377,
        "lng": -5.826529,
        "description": "OMG I lost my pocket. Somebody robbed me",
        "time": 1442560148835,
        "user_id": 1,
        "category_id": 3,
    },
    {
        "id": 2,
        "lat": 43.360382,
        "lng": -5.850613,
        "description": "My sister was abducted for a few hours. Do not go close to this zone.",
        "time": 1442560625966,
        "user_id": 1,
        "category_id": 1,
    },
    {
        "id": 3,
        "lat": 43.366815,
        "lng": -5.840015,
        "description": "I was late to the office because of the traffic jams. Avoid this road at morning.",
        "time": 1442560625966,
        "user_id": 1,
        "category_id": 2,
    },
    {
        "id": 4,
        "lat": 43.369748,
        "lng": -5.828599,
        "description": "I saw a street fight there. It was incredible. I advised you avoiding this zone.",
        "time": 1442560839280,
        "user_id": 1,
        "category_id": 4,
    },
    {
        "id": 5,
        "lat": 43.369748,
        "lng": -5.828599,
        "description": "A computer had exploded and the Computer Science School began to burn.",
        "time": 1442560839280,
        "user_id": 1,
        "category_id": 5,
    },
    {
        "category_id": 5,
        "description": "A car has run over a poor little girl in this street. Flood is covered on blood.",
        "id": 6,
        "lat": 43.359641,
        "lng": -5.860471999999959,
        "time": 1442840467666,
        "user_id": 2
    },
    {
        "category_id": 3,
        "description": "I found my front door broken and all my personal belongings disappeared. Jesus Christ, damn thieves!",
        "id": 7,
        "lat": 43.3694497,
        "lng": -5.85642949999999,
        "time": 1442840969866,
        "user_id": 2
    },
    {
        "category_id": 4,
        "description": "I've purchased my Real Oviedo season ticket, however the security guards don't let me go into the stadium. F*** R.O, next year I'll be supporting Real Sporting.",
        "id": 8,
        "lat": 43.3598532,
        "lng": -5.870963399999937,
        "time": 1442841280323,
        "user_id": 2
    },
    {
        "category_id": 2,
        "description": "Four-member street gang tried to steal my money. Avoid this street! Dangerous as hell.",
        "id": 9,
        "lat": 43.3715363,
        "lng": -5.834127800000033,
        "time": 1442841835482,
        "user_id": 2
    },
    {
        "category_id": 6,
        "description": "My laptop was violently robbed by an angry teacher in the Computer Science School. Be careful wandering this area.",
        "id": 10,
        "lat": 43.3547052,
        "lng": -5.852023300000042,
        "time": 1442842290343,
        "user_id": 2
    },
    {
        "category_id": 1,
        "description": "Hooded guy took 3 people as hostages in this bank. People are still terrified about this incident.",
        "id": 11,
        "lat": 43.3634273,
        "lng": -5.850202099999933,
        "time": 1442842528781,
        "user_id": 2
    },
    {
        "category_id": 6,
        "description": "Several people has lost their personal belongings in the beach.",
        "id": 12,
        "lat": 43.541322,
        "lng": -5.653305,
        "time": 1442842528781,
        "user_id": 2
    },
    {
        "category_id": 2,
        "description": "Huge fight between Real Madrid and At. de Madrid hooligans. Stay away!",
        "id": 13,
        "lat": 40.4080339,
        "lng": -3.6760974,
        "time": 1442842528781,
        "user_id": 2
    },
    {
        "category_id": 5,
        "description": "Bloody massacre of bulls in the festivity of El Toro de la Vega.",
        "id": 14,
        "lat": 41.501021,
        "lng": -4.999600,
        "time": 1442842528781,
        "user_id": 2
    },
    {"time": 1442854576564, "lat": 40.390933871813615, "lng": 40.390933871813615, "description": "My sister was abducted for a few hours. Do not go close to this zone.", "category_id": 1, "user_id": 1, "id": 48}, {"time": 1442854576564, "lat": 40.39897504134374, "lng": 40.39897504134374, "description": "My laptop was violently robbed by an angry teacher in the Computer Science School. Be careful wandering this area.", "category_id": 6, "user_id": 1, "id": 47}, {"time": 1442854576564, "lat": 40.39897504134374, "lng": 40.39897504134374, "description": "My laptop was violently robbed by an angry teacher in the Computer Science School. Be careful wandering this area.", "category_id": 6, "user_id": 1, "id": 47}, {"time": 1442854576564, "lat": 40.390933871813615, "lng": 40.390933871813615, "description": "My sister was abducted for a few hours. Do not go close to this zone.", "category_id": 1, "user_id": 1, "id": 48}, {"time": 1442854576564, "lat": 41.39929158996447, "lng": 41.39929158996447, "description": "A computer had exploded and the Computer Science School began to burn.", "category_id": 5, "user_id": 2, "id": 43}, {"time": 1442854576564, "lat": 41.39929158996447, "lng": 41.39929158996447, "description": "A computer had exploded and the Computer Science School began to burn.", "category_id": 5, "user_id": 2, "id": 43}, {"time": 1442854576564, "lat": 41.39929158996447, "lng": 41.39929158996447, "description": "A computer had exploded and the Computer Science School began to burn.", "category_id": 5, "user_id": 2, "id": 43}, {"time": 1442854576564, "lat": 41.612569908720324, "lng": 41.612569908720324, "description": "OMG I lost my pocket. Somebody robbed me", "category_id": 2, "user_id": 2, "id": 44}, {"time": 1442854576564, "lat": 40.39897504134374, "lng": 40.39897504134374, "description": "My laptop was violently robbed by an angry teacher in the Computer Science School. Be careful wandering this area.", "category_id": 6, "user_id": 1, "id": 47}, {"time": 1442854576564, "lat": 41.61241538254858, "lng": 41.61241538254858, "description": "I found my front door broken and all my personal belongings disappeared. Jesus Christ, damn thieves!", "category_id": 3, "user_id": 1, "id": 49}, {"time": 1442854576564, "lat": 41.61241538254858, "lng": 41.61241538254858, "description": "I found my front door broken and all my personal belongings disappeared. Jesus Christ, damn thieves!", "category_id": 3, "user_id": 1, "id": 49}, {"time": 1442854576564, "lat": 41.612569908720324, "lng": 41.612569908720324, "description": "OMG I lost my pocket. Somebody robbed me", "category_id": 2, "user_id": 2, "id": 44}, {"time": 1442854576564, "lat": 40.39897504134374, "lng": 40.39897504134374, "description": "My laptop was violently robbed by an angry teacher in the Computer Science School. Be careful wandering this area.", "category_id": 6, "user_id": 1, "id": 47}, {"time": 1442854576564, "lat": 40.390933871813615, "lng": 40.390933871813615, "description": "My sister was abducted for a few hours. Do not go close to this zone.", "category_id": 1, "user_id": 1, "id": 48}, {"time": 1442854576564, "lat": 40.39897504134374, "lng": 40.39897504134374, "description": "My laptop was violently robbed by an angry teacher in the Computer Science School. Be careful wandering this area.", "category_id": 6, "user_id": 1, "id": 47}, {"time": 1442854576564, "lat": 41.39929158996447, "lng": 41.39929158996447, "description": "A computer had exploded and the Computer Science School began to burn.", "category_id": 5, "user_id": 2, "id": 43}, {"time": 1442854576564, "lat": 41.39929158996447, "lng": 41.39929158996447, "description": "A computer had exploded and the Computer Science School began to burn.", "category_id": 5, "user_id": 2, "id": 43}, {"time": 1442854576564, "lat": 41.61241538254858, "lng": 41.61241538254858, "description": "I found my front door broken and all my personal belongings disappeared. Jesus Christ, damn thieves!", "category_id": 3, "user_id": 1, "id": 49}, {"time": 1442854576564, "lat": 41.39929158996447, "lng": 41.39929158996447, "description": "A computer had exploded and the Computer Science School began to burn.", "category_id": 5, "user_id": 2, "id": 43}, {"time": 1442854576564, "lat": 40.390933871813615, "lng": 40.390933871813615, "description": "My sister was abducted for a few hours. Do not go close to this zone.", "category_id": 1, "user_id": 1, "id": 48}, {"time": 1442854576564, "lat": 41.39929158996447, "lng": 41.39929158996447, "description": "A computer had exploded and the Computer Science School began to burn.", "category_id": 5, "user_id": 2, "id": 43}, {"time": 1442854576564, "lat": 41.39929158996447, "lng": 41.39929158996447, "description": "A computer had exploded and the Computer Science School began to burn.", "category_id": 5, "user_id": 2, "id": 43}, {"time": 1442854576564, "lat": 41.39929158996447, "lng": 41.39929158996447, "description": "A computer had exploded and the Computer Science School began to burn.", "category_id": 5, "user_id": 2, "id": 43}, {"time": 1442854576564, "lat": 41.612569908720324, "lng": 41.612569908720324, "description": "OMG I lost my pocket. Somebody robbed me", "category_id": 2, "user_id": 2, "id": 44}, {"time": 1442854576564, "lat": 39.492199540717, "lng": 39.492199540717, "description": "I saw a street fight there. It was incredible. I advise you avoiding this zone.", "category_id": 4, "user_id": 2, "id": 39}, {"time": 1442854576564, "lat": 40.39897504134374, "lng": 40.39897504134374, "description": "My laptop was violently robbed by an angry teacher in the Computer Science School. Be careful wandering this area.", "category_id": 6, "user_id": 1, "id": 47}, {"time": 1442854576564, "lat": 40.390933871813615, "lng": 40.390933871813615, "description": "My sister was abducted for a few hours. Do not go close to this zone.", "category_id": 1, "user_id": 1, "id": 48}, {"time": 1442854576564, "lat": 41.61241538254858, "lng": 41.61241538254858, "description": "I found my front door broken and all my personal belongings disappeared. Jesus Christ, damn thieves!", "category_id": 3, "user_id": 1, "id": 49}, {"time": 1442854576564, "lat": 41.39929158996447, "lng": 41.39929158996447, "description": "A computer had exploded and the Computer Science School began to burn.", "category_id": 5, "user_id": 2, "id": 43}, {"time": 1442854576564, "lat": 41.612569908720324, "lng": 41.612569908720324, "description": "OMG I lost my pocket. Somebody robbed me", "category_id": 2, "user_id": 2, "id": 44}, {"time": 1442854576564, "lat": 40.39897504134374, "lng": 40.39897504134374, "description": "My laptop was violently robbed by an angry teacher in the Computer Science School. Be careful wandering this area.", "category_id": 6, "user_id": 1, "id": 47}, {"time": 1442854576564, "lat": 40.39897504134374, "lng": 40.39897504134374, "description": "My laptop was violently robbed by an angry teacher in the Computer Science School. Be careful wandering this area.", "category_id": 6, "user_id": 1, "id": 47}, {"time": 1442854576564, "lat": 40.39897504134374, "lng": 40.39897504134374, "description": "My laptop was violently robbed by an angry teacher in the Computer Science School. Be careful wandering this area.", "category_id": 6, "user_id": 1, "id": 47}, {"time": 1442854576564, "lat": 40.390933871813615, "lng": 40.390933871813615, "description": "My sister was abducted for a few hours. Do not go close to this zone.", "category_id": 1, "user_id": 1, "id": 48}, {"time": 1442854576564, "lat": 41.61241538254858, "lng": 41.61241538254858, "description": "I found my front door broken and all my personal belongings disappeared. Jesus Christ, damn thieves!", "category_id": 3, "user_id": 1, "id": 49}
]
