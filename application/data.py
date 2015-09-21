__author__ = 'Dani'

users = [
    {
        "id": 1,
        "email": "test@safepoint.com",
        "password": "098f6bcd4621d373cade4e832627b4f6"  # test
    },
    {
        "id": 2,
        "email": "test2@safepoint.com",
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
    {"time": 1442857801737, "user_id": 1, "description": "My sister was abducted for a few hours. Do not go close to this zone.", "id": 15, "lat": 39.455418508877116, "category_id": 1, "lng": -0.4034132632250975}, {"time": 1442857801737, "user_id": 1, "description": "I found my front door broken and all my personal belongings disappeared. Jesus Christ, damn thieves!", "id": 16, "lat": 40.44074474332378, "category_id": 3, "lng": -3.637412528591834}, {"time": 1442857801737, "user_id": 1, "description": "A computer had exploded and the Computer Science School began to burn.", "id": 17, "lat": 40.3883359956592, "category_id": 5, "lng": -3.638556125519444}, {"time": 1442857801737, "user_id": 2, "description": "My laptop was violently robbed by an angry teacher in the Computer Science School. Be careful wandering this area.", "id": 18, "lat": 41.36156934405929, "category_id": 6, "lng": 2.141637178811832}, {"time": 1442857801737, "user_id": 1, "description": "I saw a street fight there. It was incredible. I advise you avoiding this zone.", "id": 19, "lat": 41.39470546094995, "category_id": 4, "lng": 2.1760545275500176}, {"time": 1442857801737, "user_id": 2, "description": "My sister was abducted for a few hours. Do not go close to this zone.", "id": 20, "lat": 41.38763312242263, "category_id": 1, "lng": 2.181444447453339}, {"time": 1442857801737, "user_id": 1, "description": "I saw a street fight there. It was incredible. I advise you avoiding this zone.", "id": 21, "lat": 40.389186219934984, "category_id": 4, "lng": -3.6518524243678248}, {"time": 1442857801737, "user_id": 2, "description": "OMG I lost my pocket. Somebody robbed me", "id": 22, "lat": 39.492810756188554, "category_id": 2, "lng": -0.41848733329823556}, {"time": 1442857801738, "user_id": 2, "description": "A computer had exploded and the Computer Science School began to burn.", "id": 23, "lat": 41.37651452213056, "category_id": 5, "lng": 2.140754137731597}, {"time": 1442857801738, "user_id": 1, "description": "A computer had exploded and the Computer Science School began to burn.", "id": 24, "lat": 41.66224046585698, "category_id": 5, "lng": -4.7182763481416}, {"time": 1442857801738, "user_id": 2, "description": "A computer had exploded and the Computer Science School began to burn.", "id": 25, "lat": 39.46799120554922, "category_id": 5, "lng": -0.3675444502530507}, {"time": 1442857801738, "user_id": 1, "description": "I saw a street fight there. It was incredible. I advise you avoiding this zone.", "id": 26, "lat": 41.38471292350884, "category_id": 4, "lng": 2.122215554498582}, {"time": 1442857801738, "user_id": 2, "description": "A computer had exploded and the Computer Science School began to burn.", "id": 27, "lat": 37.38334997888695, "category_id": 5, "lng": -6.010062049480659}, {"time": 1442857801738, "user_id": 1, "description": "OMG I lost my pocket. Somebody robbed me", "id": 28, "lat": 39.44635117551229, "category_id": 2, "lng": -0.3665430671906298}, {"time": 1442857801738, "user_id": 2, "description": "A computer had exploded and the Computer Science School began to burn.", "id": 29, "lat": 43.267276012179956, "category_id": 5, "lng": -2.922852190131345}, {"time": 1442857801738, "user_id": 1, "description": "I saw a street fight there. It was incredible. I advise you avoiding this zone.", "id": 30, "lat": 39.4825518335761, "category_id": 4, "lng": -0.4082971024088648}, {"time": 1442857801738, "user_id": 1, "description": "I found my front door broken and all my personal belongings disappeared. Jesus Christ, damn thieves!", "id": 31, "lat": 43.26138130536815, "category_id": 3, "lng": -2.923049382007524}, {"time": 1442857801738, "user_id": 2, "description": "My laptop was violently robbed by an angry teacher in the Computer Science School. Be careful wandering this area.", "id": 32, "lat": 41.378940778773696, "category_id": 6, "lng": 2.1875819981399838}, {"time": 1442857801738, "user_id": 1, "description": "A computer had exploded and the Computer Science School began to burn.", "id": 33, "lat": 41.40666771683417, "category_id": 5, "lng": 2.2194107159797984}, {"time": 1442857801738, "user_id": 1, "description": "OMG I lost my pocket. Somebody robbed me", "id": 34, "lat": 43.25682167125328, "category_id": 2, "lng": -2.918260202255363}, {"time": 1442857801738, "user_id": 1, "description": "A computer had exploded and the Computer Science School began to burn.", "id": 35, "lat": 41.64598061271746, "category_id": 5, "lng": -4.710824329064112}, {"time": 1442857801738, "user_id": 1, "description": "I saw a street fight there. It was incredible. I advise you avoiding this zone.", "id": 36, "lat": 37.37775744258911, "category_id": 4, "lng": -5.963092413125803}, {"time": 1442857801738, "user_id": 1, "description": "OMG I lost my pocket. Somebody robbed me", "id": 37, "lat": 41.38355055770754, "category_id": 2, "lng": 2.168800241153469}, {"time": 1442857801738, "user_id": 2, "description": "OMG I lost my pocket. Somebody robbed me", "id": 38, "lat": 39.46074788090551, "category_id": 2, "lng": -0.3705890350855895}, {"time": 1442857801738, "user_id": 1, "description": "I saw a street fight there. It was incredible. I advise you avoiding this zone.", "id": 39, "lat": 40.42713878710511, "category_id": 4, "lng": -3.7498102736830004}, {"time": 1442857801738, "user_id": 2, "description": "My laptop was violently robbed by an angry teacher in the Computer Science School. Be careful wandering this area.", "id": 40, "lat": 41.40933233871631, "category_id": 6, "lng": 2.205654151559162}, {"time": 1442857801738, "user_id": 1, "description": "A computer had exploded and the Computer Science School began to burn.", "id": 41, "lat": 37.36417132182082, "category_id": 5, "lng": -5.970357902714236}, {"time": 1442857801738, "user_id": 1, "description": "I found my front door broken and all my personal belongings disappeared. Jesus Christ, damn thieves!", "id": 42, "lat": 39.42853697136941, "category_id": 3, "lng": -0.4015547793659322}, {"time": 1442857801738, "user_id": 2, "description": "My laptop was violently robbed by an angry teacher in the Computer Science School. Be careful wandering this area.", "id": 43, "lat": 41.626045471455804, "category_id": 6, "lng": -4.693967172736343}, {"time": 1442857801738, "user_id": 1, "description": "My laptop was violently robbed by an angry teacher in the Computer Science School. Be careful wandering this area.", "id": 44, "lat": 39.435739226077, "category_id": 6, "lng": -0.37734798226379856}, {"time": 1442857801738, "user_id": 1, "description": "A computer had exploded and the Computer Science School began to burn.", "id": 45, "lat": 41.64691156712758, "category_id": 5, "lng": -4.750542800982957}, {"time": 1442857801738, "user_id": 1, "description": "My laptop was violently robbed by an angry teacher in the Computer Science School. Be careful wandering this area.", "id": 46, "lat": 41.61747774889298, "category_id": 6, "lng": -4.701410698204328}, {"time": 1442857801738, "user_id": 1, "description": "My laptop was violently robbed by an angry teacher in the Computer Science School. Be careful wandering this area.", "id": 47, "lat": 43.264690251652894, "category_id": 6, "lng": -2.9374680017367494}, {"time": 1442857801738, "user_id": 1, "description": "My sister was abducted for a few hours. Do not go close to this zone.", "id": 48, "lat": 37.36267263027332, "category_id": 1, "lng": -5.997388060470683}, {"time": 1442857801738, "user_id": 1, "description": "I saw a street fight there. It was incredible. I advise you avoiding this zone.", "id": 49, "lat": 43.27081094708842, "category_id": 4, "lng": -2.935931777517085}
]
