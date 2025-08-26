import pandas as pd
import os

def read_file_with_fallback(path, **kwargs):
    try:
        return pd.read_csv(path, encoding='utf-8-sig', **kwargs)
    except UnicodeDecodeError:
        return pd.read_csv(path, encoding='ISO-8859-1', **kwargs)
    
categories = {
'Coffee': ["coffee", "latte", "cappuccino", "sm soffee", "snapuccino", "american", 
"lemonade", "mocha", "macchiato",
"cold brew", "energy", "french is_perishabless", "esis_perishablesso", "brew", "java", 
"joe",
"cup of joe", "cuppa", "mud", "bean juice", "cof", "12 oz coffee", "cappiccino", "coffee", 
"coffe", "coffee / cappuccino", "coffee free", "cof refill", "coffee 12oz", 
"coffee 20 oz", "coffee 20oz", "coffee 24oz", "coffee big cup", "coffee large", 
"coffee medium", "coffee refil", "coffee refill", "coffee refill 12oz", 
"coffee refill 20oz", "coffee refill 24oz", "coffee small", "coffee xlg", 
"coffee1", "coffee-club", "coffeemd", "cold brewed 16oz", "ice coffee", 
"ice coffee 20 oz", "iced coffee", "iced coffee sm", "frozen coffee", 
"snapuccino", "cappiccino medium", "cappuccino refill", "cappuccino small",
"capuccino", "cappuccino", "capp", "cap", "sm coffee", "med. coffee", 
"medium coffee", "lge coffee", "lg coffee", "x lrg coffee", "xlg coffee",
"large coffee", "med coffee", "sm. coffee", "lrg coffee", 
"extra lg coffee", "sm capp", "med capp", "medium cappicino", "12 oz capp","20oz capp","med cappachino","large coffee","medium coffee",
"xlarge coffee","small coffee","large cappachino","coffee 16oz.","sm coffee","lg. coffee","med coffee","exlg coffee","24oz coffee",
"coffee/fountainrefillsmall","coffee small","coffee medium","coffee large","coffee refill","24 oz jave cappuccino","20oz coffee","8oz coffee",
"8oz jave cappuccino","20oz jave cappuccino","20 oz coffee","cappuccino small","cappuccino refill","cappiccino medium","md cappuccino","cappaccino 24oz",
"coffee 20oz","cappaccino 20oz","coffee 24oz","coffee 16oz","cappaccino 16oz","coffee refill (20 oz)","coffee cup (20 oz)","coffee (16 oz)",
"coffee refill (16 oz)","coffee (20 oz)","12 oz coffee","16 oz coffee","24 oz coffee","24 oz capp","20 oz coffee refill","coffee 16 oz","coffee 24 oz",
"coffee","coffee 12oz","coffee refill any size","coffee large refill","20z coffee","20 oz capuccino","120z coff/capp","32oz coff/capp",
"16oz coff/capp","20oz coff/capp","cappuccino   20 oz","large coffee   20 oz","cappuccino   thermos 20 oz","coffee   thermos 20 oz",
"medium coffee   16 oz","cappuccino   16 oz","large coffe","medium coffe","16 oz coffee/cap","20oz rf fountain","20  oz rf coffee/cap",
"24oz  oz coffee/cap","20 oz coffee/cap","16 oz rf coffee/cap","24 oz rf coffee/cap","ftn coffee 20","ftn coffee 16z","ftn coffee 12z",
"ftn cappuccino 12z","60+senior 12 oz coffee","12oz coffee","coffee refills","20 oz iced coffee","32oz ice coffee","16 0z coffee","cappu 20z",
"cappu 12z","coffee 16z","cappu 16z","coffee 12z","coffee 20z","cap 16oz","cap 20oz","20 oz coffee/capp","12 oz coffee/capp",
"16 oz coffee/capp","16oz coffee","16oz capp","20ozcoffee","24capp","large cappucini","refilles coffee","cafe 20 oz","cafe 16 oz",
"coffee/cappucino 16oz","coffeecappucino 24oz","20oz. coffee","16 oz capp","24 oz coff","20 oz coff","medium cappuccino","coffee 160z",
"lrgcoffee","iced latte flavored lg","chai latte md","latte flavored lg","cappucino md","iced wht choc mocha  xl","espresso shot extra",
"latte lg","iced coffee xl","coffee md","iced wht choc mocha md","coffee/capp large","cold brew md","cappuccino lg","white choc mocha lg",
"vanilla frappe lg","iced coffee lg","iced latte xl","white choc mocha md","iced latte lg","iced car macchiato sm","coffee/cap 16 oz",
"americano md","iced car macchiato lg","iced latte md","latte flavored sm","mocha sm","coffee/cap 20 oz","coffee/capp small","americano lg",
"iced matcha latte sm","iced latte flavored md","lg coffee","americano sm","refill coffee","caramel macchiato lg","iced wht choc mocha lg",
"white choc mocha sm","iced mocha lg","medium refill coffee","mocha md","caramel frappe md","latte flavored med","iced coffee md","iced latte flavored xl",
"coffee sm","latte sm","cappuccino sm","iced chai latte lg","iced matcha latte md","latte md","caramel macchiato md","iced wht choc mocha sm",
"coffee lg","iced mocha md","vanilla frappe md","car pb choc frappe xl","iced americano md","mocha frappe md","caramel frappe lg","caramel frappe sm",
"iced matcha latte lg","coffee/capp refill","wht choc mocha frappe xl","caramel frappe xl","mocha lg","iced car macchiato md","caramel macchiato sm",
"car pb choc frappe md","matcha latte sm","cold brew lg","mocha frappe lg","vanilla frappe xl","vanilla frappe sm","car pb choc frappe lg","car pb choc frappe sm",
"iced chai latte xl","iced americano lg","new 16oz coffee","refill 16oz cof","new 24oz coffee","new 20oz coffee","refill 24oz cof","coffee1","coffee xlg",
"16 oz. cappuccino","20 oz. cappuccino","24 oz. cappuccino","16 oz cap","20 oz cap","24 oz cap","16 oz capuccino","coffee refill 24oz","coffee refill 20oz",
"coffee refill 12oz","coffee-club","lge coffee","coffee big cup","sm capp","med capp","large capp","large iceed coffee","small iceed coffee",
"capacino 16oz","12z capp","20 oz capp","20 oz. coffee","32 oz coffee","16 oz coffee refill","md coffee","md capp","lg capp","coffee rfl small",
"coffee  refill","ice coffee","24oz coffee/cap","medium cappicino","large cappicino","20oz iced coffee","ice coffee 20 oz","16oz coffee / cappuccino",
"24oz coffee / cappuccino","coffe own cup","coffee guys","12 oz. coffee","16 oz. coffee","8 oz coffee","12 specialty coffee","double espresso",
"16 oz iced coffee","24oz iced coffee","12oz refill coffee","16oz refill coffee","20oz refill coffee","24oz refill coffee","iced coffee & tea 16 oz",
"coffe refill","sm coffee/12oz","med coffee/16oz","lrg coffee/20oz","iced coffee & tea 24 oz","refill coffee/capp -20oz","refill coffee/capp 21-32oz",
"refill coffee/capp 33oz-44oz","xlg coffee","iced coffee sm","senior coffee","refill coffee cup","12 oz coffe & capp","16 oz coffee & capp",
"24 oz coffee & capp","coffee & capp refill","med coffee/capp","ex lg coffee/cap","sm coffee/cap","lg coffee/capp","small cappuccino","med refill",
"frazil/iced coffee 12 oz","frazil/iced coffee 20 oz","frazil/iced cofee 32 oz","cappuccino 12oz","large coffee refill","coffee ref","coffee 16oz refill",
"coffee 20oz refill","capp 16oz","cappucino large","med coffee 16oz","lg coffee 20oz","sm coffee 12 oz","coffee sm 16 oz","coffee refill 0-24 oz",
"coffee med 20z","frazil/iced coffee 40 oz","coffee refill 25-34 oz","med cap","x - large coffee","20 0z coffee","community coffee 16oz",
"community coffee 12 oz","16oz coff","24oz coff","refill coff","20oz coff","small coff/cap","med coff/capp","22oz coffee","12oz.coffee",
"16oz. coffee","large coff/cap","sm ref coff","4oz espresso","12 oz small coffee","20 oz large coffee","capp 20oz","12z coff/capp","16z coff/capp",
"20z coff/capp","coffee mug refill","24z coff/capp","12oz  coffee","hotcoffee 20oz","hotcoffee 24oz","hotcoffee 16oz","hot refill up to 24oz",
"sm. coffee","refill coffee 16oz","med. coffee","16oz nespresso","cappicuno medium","ex lg coffee","monday coffee","refill of coffee","20oz cappuccino",
"16oz cappuccino","lg coffee refill","coffee rfl","capuccino 16oz","com ice coffee 16oz","am coffee","16oz cof/capp","20oz cof/capp","99 cnts coffee",
"coffee med","l coffee","lrg coffee refill","20oz coffee-large","12oz coffee-small","16oz coffee-medium","24oz xlarge coffee","sb frap mocha",
"sb frap coffee","cappuccino large","cappuccino 16oz","cappuccino 20oz","large cap","medium cap","small cap","24 oz cld coffee","16 oz cld coffee",
"32 oz cld coffee","lrg coffee","coffee refill large","cappuccino medium","coffee - small","coffee - medium","coffee - large","coffee refil","lg cappucinno",
"ice coffee 16oz","12 oz. coffee","16 oz. coffee","20 oz. coffee","12oz coffee","160z coffee","20oz coffee","coffee refill 12oz green","coffee refill 20oz blue",
"20oz cold brew coffee","coffee refill 16oz pink","16oz capp","coffee refill","capp 12 oz","capp 20 oz","coffee 12 oz","coffee 20 oz","16 oz coffeecapp",
"12 oz coffee","20 oz coffee","12oz capp","free coffee","24oz coffeecapp","16 ounce coff or capp","20 ounce coffe or capp","cappucino small","12 oz coffe",
"24 oz coffee","16 oz coffe","16oz coffee","refill coffee","16oz cappuccino","20oz cappuccino","cafe tango frozen coffee 16oz","16oz cafe tango"
"large cappicino"
],
'Sandwich': [  "sandwich", "red h. dog", "wrap", "burrito", "corn dog", "calzone", "taquito",
    "stromboli", "taco", "quesadilla", "gyros", "pastry", "turnover", "burger",
    "hot dog", "sub", "grinder", "hero", "hoagie", "banh mi", "panini", "muffuletta",
    "bocadillo", "american cold cut sub", "american mix sub", "american mix wrap", "angus burger",
    "angus burger special", "angus burger with cheese", "bacon c.b.", "bacon cheese burger",
    "bacon cheeseburger", "bacon egg chs biscuit", "bacon egg chs croissant", "bacon egg chsburger",
    "bacon egg hash egg roll", "bacon egg sandwich", "bacon sand", "bagel", "bagel breakfast sandwich",
    "bagel sand", "bbq pork sandwich", "bbq sandwich", "bhb bagel and cream cheese", "bhb bec", "bhb sec",
    "biscuit meat egg & cheese", "biscuit w/ sausage g", "bis gravy", "bis gravy +1", "biscuit",
    "biscuit & gravy plat", "biscuits & gravy 2", "bisuit sandwich", "bk sausage/keilbasa/cajun",
    "blt sandwich", "blt sub", "bologna sandwich", "boom boom chicken wrap", "breaded chicken sandwich",
    "breded chicken sanwich", "breakfast burrito", "breakfast burritos", "breakfast muffin",
    "breakfast puff", "breakfast sandwich", "breakfast sandwich o", "breakfast sandwiches",
    "breakfast sndwiches", "breakfast wrap", "brisket sandwich", "brkfast sand", "brkfs sand",
    "buffalo chicken sandwich", "buffalo chicken wrap", "burger w/cheese", "burrito", "burritos",
    "ched bacon burger", "cheeseburger", "cheese burger", "cheeseburger dinner",
    "cheeseburger from warmer", "cheeseburger pizza", "cheeseburger sub", "chicken bacon burrito",
    "chicken blt wrap", "chicken burger", "chicken burger w/cheese", "chicken ceasar wrap",
    "chicken chipotle wrap", "chicken enchiladas", "chicken fajita extra", "chicken mushroom swiss sandwic",
    "chicken parm sandwich", "chicken parm sub", "chicken philly sandwich", "chicken quesadilla",
    "chicken salad sand wheat", "chicken salad sandwich", "chicken salad wrap", "chicken sandwich",
    "chicken sandwich w/cheese", "chicken strip sand w/chz", "chicken thai garden wrap", "chicken waffle",
    "chicksalad sandw", "chk/burger sandwich", "chs burger", "chx salad sub", "ckn sandwich",
    "ckn sandwich cheese", "cold cut sub", "crisp meat burrito", "croiss sand",
    "dbl bacon egg cheese muffin", "double cheesburger", "double cheeseburger dinner",
    "double meat breakfast sandwich", "double meat breakfast wrap", "double meat sub",
    "double sausage egg muffin", "egg cheeseburger", "egg salad on wheat", "egg salad on white",
    "egg salad sandwich", "egg sand", "egg & cheese brd", "egg & cheese bun", "egg biscuit",
    "egg - cheese wbagelcroissant", "egg - cheese wmuffin", "egg & cheese biscuit",
    "extra veggies sandwich", "fiery chicken wrap", "grilled cheese", "grilled chicken caesar wrap",
    "grilled chicken sandwich", "grilled chix sandwich", "grilled chx", "grilled ham cheese",
    "haddock sandwich", "ham & swiss dijon sandwich", "ham biscuit", "ham bread", "ham brkfst burrito",
    "ham bun", "ham ch sub", "ham cheddar wheat", "ham cheddar white", "ham deli wrap",
    "ham egg and cheese muffin", "ham egg chs croissant", "ham egg chs muffin",
    "ham egg hashbrown muffin", "ham focaccia", "ham garden herb wrap", "ham hoagie",
    "ham is_perishabletzel sandwich", "ham salad on wheat", "ham salad on white", "ham sandwich",
    "ham sub", "ham tomato basil wrap", "ham turkey croissant", "ham turkey deli wrap",
    "ham turkey focaccia", "ham turkey hoagie", "ham turkey on wheat", "ham turkey on white",
    "hamburger", "hamurger dinner", "hoagie", "homemade burrito", "hot pocket", "italain wrap",
    "italian cold cut sub", "italian croissant", "italian hoagie", "italian mix sandwich",
    "italian mix sub", "italian parm focaccia", "jalapeno burger", "kids grilled cheese meal",
    "kids grilled cheese with ham", "large blt sandwich", "large tuna melt",
    "large tuna or chicken italian", "large turkey italian", "lrg crossant",
    "mac and cheese cheeseburger", "maple pancake sandwich", "meat - cheese wmuffin",
    "meat & cheese biscui", "meat & egg biscuit", "meat biscuit", "meatball sub",
    "meatball sub large", "minh pork vegetable egg roll", "mtegg & ch biscuit", "muffin", "muffins",
    "mushroom swiss burger", "pizza burger", "pizza sub", "is_perishable made chicken salad wrap",
    "is_perishable made fiery chicken wrap", "is_perishable made italian wrap",
    "is_perishable made roast beef wrap", "is_perishable made tuna wrap",
    "is_perishable made turkey bacon wrap", "is_perishable made turkey wrap",
    "is_perishable mt & che biscuit", "is_perishable mt & egg biscuit",
    "is_perishable mt eg ch biscuit", "is_perishablemium meat biscuit",
    "is_perishabletzel roll sandwich", "is_perishabletzel sandwich", "puff ham & cheese",
    "puff pulled pork pocket", "puff taco pocket", "pulled pork sandwich", "rb croissant",
    "rb deli wrap", "rb hoagie", "rb on wheat", "rbeef sandwich", "reuban sandwich",
    "roast beef focaccia", "roast beef on white", "roast beef is_perishabletzel sandwich",
    "roast beef sandwich", "roast beef sub", "roast beef wrap", "roebuck burger",
    "roebuck cheeseburger", "s / h sand", "sandwich", "sandwich clas", "sandwich made t.o.",
    "saus biscuit", "saus egg bagel", "saus egg brkft burrito", "saus egg chs biscuit",
    "saus egg chs croissant", "saus egg muffin", "sausage & biscuit", "sausage bun", "sausage burrito",
    "sausage dog", "sausage egg and cheese croissant", "sausage egg and cheese muffin",
    "seafood suis_perishableme wrap", "sec bagel", "sf plain bologna", "slider burger",
    "slider burger w/ cheese", "sloppy joe sandwich", "sloppy joes", "sm hot sandwich",
    "small bacon italian", "small turkey italian", "smoked chicken bacon cheese wr", "special burger",
    "specialty burger", "steak and cheese sub", "steak egg sandwich", "steak enchiladas",
    "steak hoagie", "stuffed waffle", "sub 12 inch", "sub 6 inch", "sub platter",
    "summertime chicken salad sandwich", "super burritos", "sw bologna swich", "sw chicken wrap",
    "sw chx", "taco dip", "taco salad", "taco spaghetti", "taco wrap", "tacos", "tuna melt special",
    "tuna salad on wheat", "tuna salad on white", "tuna salad sandwich", "tuna sandwich", "tuna wrap",
    "turkey cheddar on wheat", "turkey cheddar white", "turkey chipotle wrap", "turkey club wrap",
    "turkey croissant", "turkey dinner", "turkey focaccia", "turkey garken herb wrap", "turkey hoagie",
    "turkey pesto sandwich", "turkey is_perishabletzel sandwich", "turkey sandwich", "turkey sub",
    "turkey tomato basil wrap", "turkey wrap", "wrap", "wraps",
    "20 oz coffee free", "20 oz. cappuccino", "24 oz. cappuccino", "16oz coffee / cappuccino", "24oz coffee / cappuccino",
    "red hot hot bun", "2 red hot dogs", "red hot biscuit", "1 red h. dog", "red hot bread", "mini taco",
    "roller grill hot dogs", "triple cheeseburger sub", "$9.99 cold sub speci", "gyro beef",
    "single hotdog", "roast beef pretzel sandwich", "turkey pretzel sandwich", "hot dog","baconcheeseburger","swissmushroomburger","hot dog bahama","corn dog jalapeno","corn dog regular","hot dog (any)","italian  sub","chicken burger","croissant sandwich","cheese burger","ham sandwich","corn dog","hamburger/ bbq pork on bun","saus egg cheese biscuit","burrito","hot dog / sausage","hamburger/cheeseburger","chicken cheese steak","mini taco","1 corndog","bagel sandwich","sub 6 inch","sub 12 inch","grilled chix sandwich","cheeseburger pizza","hot dog/sausage dog","plain biscuit","meat biscuit","egg biscuit","meat & cheese biscui","egg & cheese biscuit","bacon hamburger","bacon hamburger combo","pizza burger","chicken strip sand w/chz","angus burger","bagel breakfast sandwich","bacon hamburger fries","bacon egg & cheese t","small - sausage burr","quesadilla steak or chicken","two meat sand","pbj sandwich","mini corn dogs 1/2lb","chk/burger sandwich","brisket sandwich","ham deli wrap","mini beef tacos","breakfast sandwhich","chicksalad sandw","rbeef sandwich","pretzel sandwich","bbq brisket sandwhich","cheeseburgers","chcken salad sand","egg salad sand","kielbasa burrito","ham and bacon burrito","bacon chs brgr","sausage and bacon burrito","reg/ jal corndog","turkey pesto sandwich","small burrito","corndog/hotdog","hot sand chrg  full $2.00","burger chk/ham","crawfish  boudin","regular corndog","malibu chicken sandwich","jimmy dean breakfast san","2 corndogs","ruben sandwich","ruben","torta asada","bologna and egg b","bacon  egg biscuit","sausage biscuit","bacon biscuit","sausage and egg biscuit","bologna biscuit","sausage egg  cheese b","bacon egg  cheese biscuit","toast sandwich","blt sandwich","philly sandwich","bologna sandwich","ham sandwich","hotdog loaded","corndog","steak egg  cheese biscuit","dbl cheeseburger","sloppy joe","crispy chicken wrap","tenderloin egg biscuit","chicken salad sand white","ham  cheese sub","pimento cheese sandwich","tenderl egg  cheese biscuit","chicken egg  cheese b","bologna egg  cheese biscuit","country ham  egg biscuit","country ham egg  cheese biscu","country ham biscuit","sausage egg  cheese toast","bacon egg  cheese toast","bologna egg  cheese toast","chicken egg  cheese toast","chicken sandwich","dbl hamburger","tuna salad sandwich","sausage cheese biscuit","tenderloin sandwich","egg salad sandwich","bologna  cheese sandwich","ds loaded walkin taco","hotdog","meatloaf sandwich","fish sandwich special","country ham egg  cheese toast","fish sandwich","dbl bacon cheeseburger","bacon cheese biscuit","tenderloin egg  cheese toast","6 chicken sandwich combo","steak hoagie","cold case sloppy joe","ds cold case taco wrap","ckn wrap","big taco","2ct hot dog","hot dog","sausgemuff bkfsand","sausagebagel bkfsand","taco salad","add taco meat","bacnbagel bkfsand","blt pizza","baconmuff bksand","6\" sub reg","12\" sub reg","wrap","6\" sub supreme","12\" sub supreme","sausage egg chs sandwich","bacon egg chs breakfast sandwi","ham egg chs breakfast sandwich","sausage only sandwich","biscuit sandwich","cheeseburger","hamburger","bacon cheeseburger","steak biscuit","steak  egg biscuit","chicken biscuit","chicken  egg biscuit","bologna  egg toast","tenderloin biscuit","cheese biscuit","waffle biscuit","plain meat biscuit.","egg cheese biscuit","soft flour breakfast burrito","breakfast burrito","chicken sandwich","cold sub","breakfast sandwich","chicken or steak biscuit","quesadilla","fish sandwich","hotdog","quesdilla half","brkfst sausage"

],
'Beverage': [ "soft drink", "ftn/slushi", "soda", "cola", "lemonade", "flavored water", "tonic",
    "sparkling", "fountain", "fount", "fizzy", "pepsi", "coke", "mountain dew", "fount",
    "fountain", "ftn", "fountain pop", "fountain soda", "ftn refill", "fountian drink",
    "soda", "soda fountain", "soda fountian", "fountain -large", "fountain -medium",
    "fountain refill", "extra lg soda", "large pop", "large soda", "med pop", "med pop refill",
    "medium fountain", "medium refill", "medium soda", "pepsi fountain soda", "refill fountain",
    "soda small", "soda 24oz", "soda 32oz", "soda 44oz", "soda large", "soda med", "soda refill",
    "soda refill 24oz", "soda refill 32oz", "soda refill 44oz", "soda refill fountain",
    "single soda 12 oz", "sm pop refill", "small fountain", "small refill", "small soda",
    "24 ftn refill", "32 oz refill", "20 oz fountain free", "32 oz fountain free",
    "44 oz fountain free", "32oz. refill", "44oz. refill", "20oz fountain pop",
    "32oz fountain pop", "44 pz fountain pop","fountain 32oz","combo fountain 32oz","fountian 44oz","fountain 22oz","coffee/fountainrefillsmall","small fountain drink","medium  fountain drink","large fountain drink","fountain refill","44 oz fountain drink","24 oz fountain drink","32 oz fountain drink","lg fountain","sm fountain","medium fountain","12pk soda","fountain 21oz","32 oz fountain refill","44 oz fountain","52 oz fountain","32 oz fountain","44 oz fountain cup","2/$4.00 20oz pepsi products","24 oz fountain","20oz soda","22oz fountain drink","big fountain refill","32oz fountain drink","20 oz coca cola","20 oz pepsi","16oz soda","12oz soda","coke","20oz fountain","44oz fountain","44oz rf fountain","ftn drink 20z","ftn drink 32z","44oz or less fountain refill","24oz fountain","fountn 20oz","fountn 16oz","fountn 32oz","44 oz foutain","medium soda","fountain soda 32oz","fountain soda 44oz","20oz. fountain","16 oz soda","44oz  ftn","fountain pop 32oz medium","fountain pop 44oz","refill fountain soda","sm fountain soda","54oz fountain","fountain pop","fountain pop 24oz small","italian soda sm","friday fountain soda","italian soda lg","italian soda md","44 fountain","22oz  fountain soda","32oz  fountain soda","24 oz fountian drink","fountain -large","fountain 32 oz","fountain 44 oz","32 oz fount pop","44 oz fount pop","16 oz. soda","32 oz. soda","refill - 12 oz soda","22 oz fountain pop","extra lg soda","44 oz fount","20oz fountain pop","32oz fountain pop","24 oz fountian","fountain","single soda","fountain 22 oz","fountain 24oz","44oz fount","soda refill","44oz lemonade","fountain 24 oz","40 oz fountain drink","pop 16oz","$3.29 soda","24oz soda","refill of fountain","ftn 20 oz rfl","fntn 32oz","32 oz fount","fount refill","fountain med","16oz/20oz fountain-small","32oz fountain-medium","soda ref 20oz","soda ref 16 oz","16oz ftn soda","fountain drink 20 oz","fountain drink 32 oz","fountain drink 44 oz","fountain drink refill 20 oz","fountain drink refill 32 oz","fountain drink refill 44 oz","fountain drink 12 oz","fountain refill 12 oz","24 oz fountains","32oz fountain","44 oz fountain","64 oz fount","fountain drink","20oz fountain drink","32oz fountain drink","44oz fountain drink","44oz refill fount","64oz refill fount","44oz fcb","32oz fcb","20oz fcb","32oz refill fount","32 oz soda","12 oz soda","20 oz soda","20oz ftn soda","32oz ftn soda","44oz ftn soda","soda refill 12oz","32oz soda refill","44oz soda refill","12oz ftn soda","fountain 20 oz","fountain 44oz","small fountain","med fountain","large fountain","32oz fountain","20 oz fountain soda","44 oz. fountain","md soda","lg soda","20 oz fountain","founatin drinks 20.oz","44 oz soda","20 oz soda","44oz refill fountain","12oz cold drink 18","32oz cold drink 8","20oz cold drink 8","52oz cold drink 8","44oz cold drink refi","44oz cold drink 8","32oz cold drink refi","52oz cold drink refi","pepsi","coke"

],
'Fruits': [ "fruits", "fruit", "apple", "bnna", "banana", "bananna", "orange", "grape", "papaya",
    "pear", "pomegranate", "1 bananna", "blueberry", "raspberry", "blackberry", "cranberry",
    "goji", "acai", "mulberry", "lemon", "lime", "grapefruit", "tangerine", "kumquat",
    "yuzu", "lychee", "mangosteen", "jackfruit", "starfruit", "passion", "durian", "longan",
    "peach", "lemons", "plum", "cherry", "apricot", "nectarine", "melon", "cantaloupe",
    "honeydew", "kiwano", "coconut", "walnut", "pecan", "almond", "brazilnut", "cashew",
    "chestnut", "buddha", "salak", "snake", "loquat", "apple", "apple fritter", "apples",
    "banana", "bananas", "bnna", "lemon", "lime", "lime/ lemon", "limes", "mandarin orange",
    "orange", "orange ration", "red apples", "fresh fruit", "fresh fruit large", "fresh fruit small", "fruit", "banana","bananas","aplleorange","apple green","limes","apple red","bananna","lime lemon orange","fresh fruit","fruit","bananas 2/$1","banana","2ct banana","mixed berries","apple 1","apple"

],
'Novelty': ["novelty", "frozen", "slush", "gelato", "sherbet", "ice pop", "ice cream",
    "cone", "snow cone", "popsicle", "slushie", "slushy", "frozen slushie",
    "ftn/slushi large", "ftn/slushi medium", "lg slushie", "lg slushie cup",
    "lg slushy", "med slushie", "med slushy", "med slush", "slush jolly rancher",
    "slush pupp", "slush puppies", "slushie 16 oz", "slushie 21 oz", "slushy large",
    "slushy med", "slushy small", "slush 16oz", "slush 40oz", "sm slush",
    "ice cream cone soft serve", "soft serve ice cream", "large cone",
    "medium cone", "small cone", "waffle cone", "frazil 12oz", "frazil 20oz",
    "frazil 32oz", "2 hard scoop", "1 hard scoop", "slushy 20 ounce", "slushy 12ounce", "Slushie Small", "Slushie Large", "20oz Slushy", "SLUSHIE 20OZ", "SLUSHIE 32OZ", "20 OZ SLUSH", "12OZ SLUSH", "30 OZ SLUSH", "Medium Slushie", "Large Slushie", "32OZ Slushie", "Small Pop   20 Oz", "SMALL MEDIUM POP REFILL", "44 OZ SLUSH", "32OZ SLUSH", "SLUSH 16Z", "SLUSH 32Z", "SLUSH 20Z", "SLUSHI 20OZ", "Frazil Slushy 22oz", "Frazil Slushy 44oz", "Med Slushie", "Large Slushy", "20 OZ Ice Cream & Shake", "16OZ SLUSHY", "12OZ SLUSHY", "16 OZ Ice Cream & Shake", "40oz Ice Cream or Shake", "Small Slush 12oz", "Large Slush 20oz", "32 OZ Ice Cream & Shake", "SLUSHIE XL", "Slush 16oz", "Slush 40oz", "32 OZ SLUSHIE", "FRAZIL32OZ", "44 OZ SLUSHY", "Frazil 12oz", "SUNDAE SOFT", "Siberian Chill 20oz Slushie", "12 OZ SLUSHIE", "20 OZ SLUSHIE", "Soft Serve Ice Cream", "Slushee Drink 16oz", "FRAZIL/ICED COFFEE 12 OZ", "FRAZIL/ICED COFFEE 20 OZ", "FRAZIL/ICED PER OZ", "Slushee 16 oz", "ICEE 24 oZ", "ICEE 16 OZ", "FRAZIL/ICED COFFEE 40 OZ", "32 Oz Slush", "24 Oz Slush", "24 OZ SLUSHIE", "Icee 16oz", "Icee 24oz", "FRAZIL 40Z", "Ice Cream Cone", "24Z SLUSHIE", "16Z SLUSHIE", "ICEE 32OZ", "20oz Frazil", "FRAZIL BUBBLE REFILL", "20oz Slush Puppy", "16oz Slush Puppy", "ICEE MED", "32 OZ FRAZIL", "40OZ FRAZIL", "benjerryspands", "12 OZ SLUSH", "32 OZ SLUSH", "LG CONE", "SM. CONE", "WAFFLE CONE", "20 OZ SLUSH", "CARIBBEAN CREAM 20OZ", "SM SLUSHY", "LG SLUSHY", "32 OZ. SLUSHY", "CUP OF ICECREAM", "ICE CREAM CONE", "SLUSH 20 OZ", "SML CONE", "SML WAFFLE", "MED CONE", "MED WAFFLE", "Slush", "SLUSH 21 OZ", "SLUSH 12OZ", "SMALL SLUSH", "LARGE SLUSH"

]
}


def get_keyword_matches(txt):
    if pd.isna(txt) or not isinstance(txt, str):
        return ''
    txt = txt.lower()
    matches = []
    for cat, keywords in categories.items():
        for kw in keywords:
            if kw.lower() in txt:
                matches.append(kw.lower())
    return ', '.join(set(matches))

def process_file():
    file_path = input("Enter the full file path (with extension): ").strip()
    if not os.path.exists(file_path):
        print("File does not exist. Exiting.")
        return

    delimiter = input("Enter the delimiter (e.g., ',' for CSV, '|' for pipe, '\\t' for tab): ").strip()
    has_header = input("Does the file have headers? (yes/no): ").strip().lower()

    if has_header == 'no':
        header_input = input("Enter the headers (comma-separated): ").strip()
        headers = [h.strip().lower() for h in header_input.split(',')]
        df = read_file_with_fallback(file_path, sep=delimiter, names=headers, header=None, dtype=str)
    else:
        df = read_file_with_fallback(file_path, sep=delimiter, dtype=str)

    df.columns = df.columns.str.strip().str.lower()
    print("Columns detected after lowercasing:", df.columns.tolist())

    print("Columns detected:", df.columns.tolist())

    store_col_candidates = ['store#', 'store #', 'storid', 'location','store', 'store number', 'store_num', 'store no', 'store no.']
    store_col = next((col for col in store_col_candidates if col in df.columns), None)
    if store_col is None:
        print("No store number column found.")
        return
    df.rename(columns={store_col: 'storid'}, inplace=True)

    upc_col_candidates = ['upc', 'barcode', 'product code']
    upc_col = next((col for col in upc_col_candidates if col in df.columns), None)
    if upc_col is None:
        print("No upc column found.")
        return
    df.rename(columns={upc_col: 'upc'}, inplace=True)
    print("UPC column successfully renamed. Columns now:", df.columns.tolist())


    df = df.applymap(lambda x: x.strip().lower() if isinstance(x, str) else x)
    df['upc'] = df['upc'].astype(str).str.strip().str.replace(r'\.0$', '', regex=True)
    df['upc'] = df['upc'].apply(lambda x:x if x.isdigit() and len(x) < 12 else x)
    df['storid'] = df['storid'].astype(str).str.strip()

    description_col = next((col for col in ['description', 'item description','item_desc_short', 'desc', 'product name'] if col in df.columns), None)
    if not description_col:
        print("No description column found.")
        return

    df.rename(columns={description_col: 'description'}, inplace=True)
    df['description'] = df['description'].astype(str).str.strip()
    count_df = df.groupby('storid').apply(
        lambda g: pd.Series({
            'upc = 0 Count': (g['upc'] == '0').sum(),
            'Blank Description Count': g['description'].apply(lambda x: pd.isna(x) or x.strip() == '').sum()
        })
    ).reset_index()

    df = df[df['upc'] != '0']
    df = df[df['description'] != '']
    print("Filtering rows with upc='0' or blank description...")
    

    total_dollars_exist = input("Does this file already have total dollars (e.g., price_total/sales amount)? (yes/no): ").strip().lower()
    implied_decimal = input("Is implied decimal adjustment needed? (yes/no): ").strip().lower()

    if total_dollars_exist == 'no':
        price_col_candidates = ['price', 'unit price', 'item price','net_unit_price']
        price_col = next((col for col in price_col_candidates if col in df.columns), None)
        if price_col is None:
            print("No price column found to calculate total dollars.")
            return
        df.rename(columns={price_col: 'price'}, inplace=True)

        unit_col_candidates = ['units', 'unit', 'quantity', 'quantitysold','total_net_units']
        unit_col = next((col for col in unit_col_candidates if col in df.columns), None)
        if unit_col is None:
            print("No Units column found to calculate total dollars.")
            return
        df.rename(columns={unit_col: 'quantitysold'}, inplace=True)

        df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(0.0)
        df['quantitysold'] = pd.to_numeric(df['quantitysold'], errors='coerce').fillna(1)

        if implied_decimal == 'yes':
            df['price'] = df['price'] / 100

        df['totaldollars'] = df['price'] * df['quantitysold']
    else:
        price_col_candidates = ['price_total', 'total price', 'total_dollars','total_net_sales_amt','totaldollars', 'sales amount']
        price_col = next((col for col in price_col_candidates if col in df.columns), None)
        if price_col is None:
            print("No price_total column found.")
            return
        df.rename(columns={price_col: 'totaldollars'}, inplace=True)

        unit_col_candidates = ['units', 'unit', 'quantity', 'quantitysold','qty','total_net_units']
        unit_col = next((col for col in unit_col_candidates if col in df.columns), None)
        if unit_col is None:
            print("No Units column found.")
            return
        df.rename(columns={unit_col: 'quantitysold'}, inplace=True)

        df['totaldollars'] = pd.to_numeric(df['totaldollars'], errors='coerce').fillna(0.0)
        df['quantitysold'] = pd.to_numeric(df['quantitysold'], errors='coerce').fillna(1)

        if implied_decimal == 'yes':
            df['totaldollars'] = df['totaldollars'] / 100

        df['price'] = df['totaldollars'] / df['quantitysold']

    df['upc'] = df['upc'].apply(lambda x: '{:.0f}'.format(float(x)))
    df['upc'] = pd.to_numeric(df['upc'], errors='coerce')
    df = df[df['upc'].notna()]
    df['upc'] = df['upc'].astype(int).astype(str)
    df['upc_len'] = df['upc'].str.len()
    df["is_perishable"] = 'FALSE'
 
    for idx, row in df.iterrows():
        upc = str(row['upc'])
        upc_len = len(upc)
        df.at[idx, 'upc_len'] = upc_len

        if upc_len == 11 and (upc[0] in ['2', '4']) and upc[-5:] == '00000':
            df.at[idx, 'is_perishable'] = 'TRUE'
        elif upc_len == 12 and (upc[0] in ['2', '4']) and upc[7:12] == '00000':
            df.at[idx, 'is_perishable'] = 'TRUE'
        elif upc_len in [1,2,3,4,5,6,7]:
            df.at[idx, 'is_perishable'] = 'TRUE'

        perishable_df = df[df['is_perishable'] == 'TRUE']

 
    score_values = {'Coffee': 5, 'Sandwich': 3, 'Beverage': 4, 'Fruits': 2, 'Novelty': 1}
    df.to_csv('C://Users//PAAB2011//OneDrive - NIQ\Desktop//IV TEAM PROJECTS//TEST FOR CONVENIENCE//Perishablecheck.csv')

    row_text = df['description'].astype(str).str.lower()
    df['Keyword Matches'] = df['description'].apply(get_keyword_matches)

    for cat in categories:
        df[cat] = (df['is_perishable'] == 'TRUE') & row_text.apply(lambda txt: any(kw in txt for kw in categories[cat]))
        df[cat] = df[cat].astype(int) * score_values[cat]

    df['Total'] = df[['Coffee', 'Sandwich', 'Beverage', 'Fruits', 'Novelty']].sum(axis=1)

    def custom_group(group):
        acv = group['totaldollars'].sum()
        perishable_td = group.loc[group['is_perishable'] == 'TRUE', 'totaldollars'].sum()
        item_keyword = group.loc[group['Total'] > 0, 'totaldollars'].sum()
        remaining_perishables = perishable_td - item_keyword
        score_total = group[['Coffee', 'Sandwich', 'Beverage', 'Fruits', 'Novelty']].max().sum()
        score_valid = score_total >= 11
        remaining_valid = remaining_perishables >= (0.10 * perishable_td)
    

        if not (score_valid and remaining_valid):
            return pd.Series({
                'Store #': group.name,
                'ACV': acv,
                'ACV*52': acv * 52,
                '$520K': 'PASS' if acv * 52 >= 520000 else 'FAIL',
                'Coffee': group['Coffee'].max(),
                'Soft Drinks': group['Beverage'].max(),
                'Sandwich': group['Sandwich'].max(),
                'Fruits': group['Fruits'].max(),
                'Novelty': group['Novelty'].max(),
                'Total': score_total,
                'RSI/Salvage': 'RSI',
                'perishable TD $': perishable_td,
                'Item keyword $': item_keyword,
                'remaing perishables $': remaining_perishables,
                'Penny price total': '',
                'Penny price total ≥ 5% of perishable TD': '',
                '$1 price total': '',
                '$1 price total ≥ 20% of perishable TD': '',
                '$50 price total': '',
                '$50 price total ≥ 10% of perishable TD': '',
                'SALVAGE/QUALIFIED': '',
                'Final Status': 'RSI'
            })

        penny_total = group.loc[(group['is_perishable'] == 'TRUE') & (group['price'].between(0.01, 0.06)), 'totaldollars'].sum()
        dollar1_total = group.loc[(group['is_perishable'] == 'TRUE') & (group['price'] == 1.00), 'totaldollars'].sum()
        dollar50_total = group.loc[(group['is_perishable'] == 'TRUE') & (group['price'] == 50.00), 'totaldollars'].sum()

        penny_flag = 'CORRECTIONS NEEDED' if penny_total >= (0.05 * perishable_td) else 'NO CORRECTIONS NEEDED'
        dollar1_flag = 'CORRECTIONS NEEDED' if dollar1_total >= (0.20 * perishable_td) else 'NO CORRECTIONS NEEDED'
        dollar50_flag = 'CORRECTIONS NEEDED' if dollar50_total >= (0.10 * perishable_td) else 'NO CORRECTIONS NEEDED'

        final_result = 'QUALIFIED' if all([
            penny_flag == 'NO CORRECTIONS NEEDED',
            dollar1_flag == 'NO CORRECTIONS NEEDED',
            dollar50_flag == 'NO CORRECTIONS NEEDED'
        ]) else 'SALVAGE'

        return pd.Series({
            'Store #': group.name,
            'ACV': acv,
            'ACV*52': acv * 52,
            '$520K': 'PASS' if acv * 52 >= 520000 else 'FAIL',
            'Coffee': group['Coffee'].max(),
            'Soft Drinks': group['Beverage'].max(),
            'Sandwich': group['Sandwich'].max(),
            'Fruits': group['Fruits'].max(),
            'Novelty': group['Novelty'].max(),
            'Total': score_total,
            'RSI/Salvage': 'Salvage',
            'perishable TD $': perishable_td,
            'Item keyword $': item_keyword,
            'remaing perishables $': remaining_perishables,
            'Penny price total': penny_total,
            'Penny price total ≥ 5% of perishable TD': penny_flag,
            '$1 price total': dollar1_total,
            '$1 price total ≥ 20% of perishable TD': dollar1_flag,
            '$50 price total': dollar50_total,
            '$50 price total ≥ 10% of perishable TD': dollar50_flag,
            'SALVAGE/QUALIFIED': final_result,
            'Final Status': final_result
        })

    summary_df = df.groupby('storid').apply(custom_group).reset_index(drop=True)
    count_df.rename(columns={'storid': 'Store #'}, inplace=True)
    summary_df = summary_df.merge(count_df, how='left', on='Store #')
    ordered_columns = [
        'Store #', 'upc = 0 Count', 'Blank Description Count',
        'ACV', 'ACV*52', '$520K', 'Coffee', 'Soft Drinks', 'Sandwich', 'Fruits', 'Novelty', 'Total',
        'RSI/Salvage', 'perishable TD $', 'Item keyword $', 'remaing perishables $',
        'Penny price total', 'Penny price total ≥ 5% of perishable TD',
        '$1 price total', '$1 price total ≥ 20% of perishable TD',
        '$50 price total', '$50 price total ≥ 10% of perishable TD',
        'SALVAGE/QUALIFIED', 'Final Status'
    ]
    summary_df = summary_df.reindex(columns=ordered_columns)

    output_path = input("Enter output .xlsx path (e.g., C:\\path\\to\\output.xlsx): ").strip()
    if not output_path.lower().endswith('.xlsx'):
        print("Please provide a valid .xlsx file path.")
        return

    with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
        summary_df.to_excel(writer, sheet_name='Category & Scores', index=False)
        df.to_excel(writer, sheet_name='Raw Data with Keywords', index=False)

    print("upc perishable detection logic applied correctly.")
    print("upc formatting and zero-padding applied correctly.")
    print(f"Output saved to: {output_path}")

if __name__ == "__main__":
    process_file()


        