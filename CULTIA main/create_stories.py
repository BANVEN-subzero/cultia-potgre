
import os

stories = [
    {
        "file": "mountain_king.html",
        "id": "mountain_king",
        "title": "The Mountain King of Mount Cameroon",
        "subtitle": "A Tale of Power & Respect from the Bakweri People",
        "image": "https://i.pinimg.com/736x/fb/31/33/fb31337a2bc6979a187875f9ed899257.jpg",
        "tribe": "Bakweri",
        "sections": [
            {
                "title": "The Guardian of the Peaks",
                "content": "In the heart of what is now Southwest Cameroon, where the earth reaches toward the sky in a magnificent peak, there lived a powerful king. But this was no ordinary king in a palace. His throne was the summit of Mount Cameroon itself, and his subjects were the spirits of the mountain, the rivers that flowed from its slopes, and the forests that covered its sides."
            },
            {
                "title": "The King's Power",
                "content": "The Mountain King controlled the volcano's fiery temper. When he was pleased, the mountain slept peacefully, and the people of the Bakweri and neighboring tribes farmed the fertile volcanic soil, harvested rich crops, and lived in peace. When he was angered by disrespect or greed, he would shake the earth and send rivers of fire down the slopes."
            },
            {
                "title": "A Warning Ignored",
                "content": "There came a time when a group of hunters forgot the old rules. They took more game than they needed, they cut down sacred trees, and they mocked the mountain's spirits. The Mountain King warned them through rumblings and smoke, but they laughed and continued their ways. At last, the mountain could bear it no longer."
            },
            {
                "title": "The Mountain's Fury",
                "content": "The earth trembled. The sky turned black with ash. Rivers of lava began to flow. In terror, the people fled to the elders, who knew what must be done. They prepared offerings of palm wine, kola nuts, and the finest fabrics, and with great humility, they approached the mountain's base to beg for forgiveness."
            }
        ],
        "cultural_note": "To this day, the Bakweri people maintain a deep spiritual connection to Mount Cameroon. Before climbing the mountain, traditional offerings are made, and the mountain's power and authority are acknowledged with respect. This legend teaches that nature is not something to be conquered, but a living, sacred force to be honored and lived in harmony with."
    },
    {
        "file": "hunter_pact.html",
        "id": "hunter_pact",
        "title": "The Hunter's Pact with the Forest",
        "subtitle": "A Tale of Ambition & Consequence from the Bulu People",
        "image": "https://i.pinimg.com/736x/3d/8f/6a/3d8f6a57180c853a465d6282a9d4584c.jpg",
        "tribe": "Bulu",
        "sections": [
            {
                "title": "The Young Hunter",
                "content": "There was once a young Bulu hunter named Nkoro who was ambitious but impatient. While other hunters returned with small game, Nkoro dreamed of bringing home the largest antelopes, the fiercest boars, and the most magnificent birds. But no matter how hard he tried, his hunts never seemed to succeed as he wished."
            },
            {
                "title": "Meeting the Forest Spirit",
                "content": "One evening, deep in the forest after a particularly disappointing day, Nkoro sat weeping under a great silk-cotton tree. Suddenly, the air grew still, and a figure emerged from the shadows. It was the Forest Spirit, ancient and powerful, with eyes like pools of water and skin like bark."
            },
            {
                "title": "The Pact",
                "content": "The spirit offered Nkoro a deal: extraordinary hunting prowess, the ability to find game where no one else could, and the strength to bring down any animal. But in return, Nkoro must always leave the first and best of his kills as an offering, must never hunt on sacred days, and must never tell anyone of their agreement."
            },
            {
                "title": "Greed and Loss",
                "content": "At first, Nkoro kept his promises, and his fame grew. But as time passed, he became arrogant. He forgot the offerings, hunted on sacred days, and even boasted of his powers. The Forest Spirit withdrew its gift. Nkoro never found game again, and he learned too late that true success comes with respect and humility, not just ambition."
            }
        ],
        "cultural_note": "Bulu hunting traditions emphasize respect for the forest and its creatures. Hunters are taught to take only what they need, to honor the spirits of the animals they kill, and to recognize that the forest gives its gifts only to those who respect its rules. This story has been passed down for generations as a warning against greed and pride."
    },
    {
        "file": "golden_fish.html",
        "id": "golden_fish",
        "title": "The Golden Fish of Lake Chad",
        "subtitle": "A Tale of Wishes & Wisdom from the Kotoko People",
        "image": "https://i.pinimg.com/736x/4a/cb/38/4acb38efb39233f2d740d8c36481a6ed.jpg",
        "tribe": "Kotoko",
        "sections": [
            {
                "title": "The Fisherman and the Lake",
                "content": "Along the shores of Lake Chad, there lived a poor but honest fisherman named Abba. Every morning he would cast his nets, and every evening he would return with enough fish to feed his family, but never more. He was content with his simple life, grateful to the lake for its gifts."
            },
            {
                "title": "A Magical Catch",
                "content": "One day, Abba's net grew heavy. He pulled it in, expecting a great haul of fish, but instead found only one small fish—though it shone like pure gold. The fish spoke in a clear, gentle voice: 'Kind fisherman, please let me go. I can grant you any wish you desire.'"
            },
            {
                "title": "The Wishes Begin",
                "content": "Abba was amazed but chose a simple wish: a new hut for his family. The fish granted it, and Abba returned home to find a beautiful, sturdy hut where his old one had been. His wife was delighted, but soon she began to ask for more: fine clothes, then livestock, then land, then a palace."
            },
            {
                "title": "The Lesson of Greed",
                "content": "With each wish, Abba's wife grew more demanding. Soon, she wanted to be queen of all the land. When Abba went to the lake to make this final wish, the golden fish sighed and said, 'You have learned nothing. Go back to your old hut.' In an instant, all their riches were gone, and they were once again poor—but this time, they were grateful for what they had."
            }
        ],
        "cultural_note": "The Kotoko people of the Lake Chad region have long relied on the lake for their livelihood. This story teaches that gratitude for what we have is more valuable than endless desire. It also reminds us that great power—even the power to grant wishes—can be dangerous without wisdom and moderation."
    },
    {
        "file": "star_child.html",
        "id": "star_child",
        "title": "The Star Child of the Sky",
        "subtitle": "A Tale of Knowledge & Giving from the Mafa People",
        "image": "https://i.pinimg.com/736x/f9/69/63/f96963295e1631106a0188d57f0e48c0.jpg",
        "tribe": "Mafa",
        "sections": [
            {
                "title": "The Falling Star",
                "content": "One night, the people of a Mafa village watched in wonder as a bright star fell from the sky, landing in a nearby field. The next morning, the villagers went to investigate and found not a crater, but a beautiful child wrapped in a cloth made of stardust."
            },
            {
                "title": "The Child's Gifts",
                "content": "The villagers raised the child, whom they named Tchana, meaning 'gift from heaven'. As Tchana grew, she showed remarkable knowledge. She taught the villagers when to plant their crops by watching the stars, how to find water in dry seasons, and how to use herbs for healing."
            },
            {
                "title": "The Gift of Agriculture",
                "content": "Tchana's greatest gift was teaching the Mafa people how to build the remarkable terrace farms that still cover the Mandara Mountains today. She showed them how to channel water, enrich the soil, and grow crops that could thrive in the mountainous terrain."
            },
            {
                "title": "Return to the Stars",
                "content": "When Tchana grew old, she told the villagers that her time on Earth was done. As they watched, she rose into the sky and became a bright star, just as she had been before. To this day, the Mafa people look to that star and remember the knowledge and generosity of the Star Child."
            }
        ],
        "cultural_note": "The Mafa people are famous for their sophisticated terrace farming system that transforms steep mountainsides into productive farmland. This legend celebrates that agricultural heritage and attributes the knowledge to a divine gift, emphasizing the importance of learning, teaching, and living in harmony with the land and sky."
    },
    {
        "file": "first_cocoyam.html",
        "id": "first_cocoyam",
        "title": "The First Cocoyam",
        "subtitle": "A Tale of Hunger & Hope from the Widikum People",
        "image": "https://i.pinimg.com/736x/43/0d/dc/430ddca4751d3c956e4a5786650582db.jpg",
        "tribe": "Widikum",
        "sections": [
            {
                "title": "The Great Famine",
                "content": "Long ago, a terrible famine came to the land of the Widikum people. The rains did not fall, the crops dried up, and the rivers grew small. The people grew thin and weak, and they prayed to the spirits of the forest for help."
            },
            {
                "title": "The Forest Spirit's Visit",
                "content": "One night, an old woman appeared in the village. She looked hungry and tired, but no one had food to share—no one, that is, except an old widow named Njema. Even though she had very little left, Njema shared her last handful of corn with the stranger."
            },
            {
                "title": "A Gift from the Forest",
                "content": "The next morning, the stranger revealed herself as a Forest Spirit. She thanked Njema for her kindness and gave her a small, knobby root. 'Plant this,' the spirit said, 'and it will give you food that will sustain your people through any famine.' The root was the first cocoyam."
            },
            {
                "title": "A New Staple",
                "content": "Njema planted the root, and it grew into a strong, healthy plant with many tubers. She showed her people how to cook it, and soon, the cocoyam became a staple food. The famine ended, and the Widikum people learned that kindness and generosity are always rewarded."
            }
        ],
        "cultural_note": "Cocoyam (taro) is a staple food in Cameroon and across West and Central Africa. It is highly nutritious and can grow in conditions where other crops fail. This legend honors the importance of this vital food while teaching the values of hospitality, generosity, and care for strangers—values that are central to Widikum culture."
    },
    {
        "file": "truth_mask.html",
        "id": "truth_mask",
        "title": "The Mask of Truth",
        "subtitle": "A Tale of Justice & Leadership from the Tikar People",
        "image": "https://i.pinimg.com/736x/e0/03/3b/e0033bd341b9a400c06c67946625ee33.jpg",
        "tribe": "Tikar",
        "sections": [
            {
                "title": "The Royal Mask",
                "content": "Among the Tikar people, there was a sacred mask known as the Mask of Truth. It was kept in the royal palace and only worn by the chief during important ceremonies. The mask had the power to reveal the true character of anyone who stood before it."
            },
            {
                "title": "The Chief's Test",
                "content": "When a new chief was to be chosen, each candidate had to put on the Mask of Truth. The good and honest candidates would see the mask smile, but those with greed or cruelty in their hearts would see it frown—and the mask would not stay on their face."
            },
            {
                "title": "The Greedy Prince",
                "content": "One day, a greedy prince tried to become chief. He put on the mask, but it immediately twisted into a scowl and fell off his head. Undeterred, he tried to hide the mask so no one else could use it. But the mask was magical, and it returned to the palace on its own."
            },
            {
                "title": "The Rightful Chief",
                "content": "In the end, an honest and kind farmer was chosen as chief. When he put on the Mask of Truth, it glowed with a warm light. He ruled wisely, and under his leadership, the Tikar people prospered. The Mask of Truth continued to be used for generations, ensuring that only honest leaders would rule."
            }
        ],
        "cultural_note": "Masks hold a central place in Tikar culture, used in ceremonies, rituals, and celebrations. They are believed to connect the living with the spirit world. This legend uses the Mask of Truth to emphasize the importance of honesty, integrity, and good leadership—values that have always been essential for the well-being of Tikar communities."
    },
    {
        "file": "leopard_chief.html",
        "id": "leopard_chief",
        "title": "The Leopard and the Chief",
        "subtitle": "A Tale of Love & Respect from the Mbum People",
        "image": "https://i.pinimg.com/736x/57/01/78/5701783593e4ecf6e61261637dd13858.jpg",
        "tribe": "Mbum",
        "sections": [
            {
                "title": "The Hunter's Discovery",
                "content": "A Mbum chief was hunting in the forest when he saw a beautiful woman bathing in a stream. He approached her and asked her to marry him. She agreed, but she warned him: 'You must never look at me when I am eating.' The chief promised, and they were married."
            },
            {
                "title": "A Broken Promise",
                "content": "For years, the chief kept his promise, and they lived happily. They had children, and the chief's wife was a loving mother and partner. But one day, curiosity overcame him. When his wife thought she was alone, the chief peeked at her through a crack in the wall."
            },
            {
                "title": "The Shapeshifting Revealed",
                "content": "To the chief's shock, he saw his wife transform into a beautiful leopard as she ate. When she finished, she turned back into a woman. His wife knew he had seen her. With tears in her eyes, she said, 'You have broken your promise. I must leave you now.'"
            },
            {
                "title": "A Lasting Legacy",
                "content": "Before she left, the leopardess gave the chief a gift: the power of the leopard—strength, speed, and wisdom. She told him, 'Always remember that love requires trust and respect, even when you don't understand everything.' To this day, the Mbum people honor the leopard as a symbol of power and wisdom, and they remember the importance of keeping promises."
            }
        ],
        "cultural_note": "Leopards are respected and admired across many Cameroonian cultures for their strength, grace, and intelligence. This story uses the leopard to explore themes of trust, respect, and the idea that there is mystery and power in the world that we may not fully understand, but must still honor."
    },
    {
        "file": "spider_wisdom.html",
        "id": "spider_wisdom",
        "title": "The Wisdom of the Old Spider",
        "subtitle": "A Tale of Pride & Humility from the Efik People",
        "image": "https://i.pinimg.com/736x/27/35/e0/2735e0719029921c9b92c9030512a22d.jpg",
        "tribe": "Efik",
        "sections": [
            {
                "title": "Anansi and the Calabash",
                "content": "Anansi the spider was a clever trickster, but he was also very proud. One day, he decided that he should collect all the wisdom in the world and keep it for himself. He wove a large calabash (a gourd container) and set off to gather wisdom from every corner of the earth."
            },
            {
                "title": "Filling the Calabash",
                "content": "Anansi visited wise old men, listened to the lessons of the trees, learned from the animals, and gathered everything he could into his calabash. Soon, the calabash was full of all the wisdom in the world. Anansi proudly carried it home, thinking he was now the wisest of all."
            },
            {
                "title": "A Fall from the Tree",
                "content": "Anansi wanted to hide the calabash at the very top of a tall tree where no one else could reach it. But as he was climbing with the heavy calabash tied to his belly, he kept slipping and falling. A small child watching from below laughed and said, 'Why don't you tie the calabash to your back instead?' Anansi tried it, and it worked!"
            },
            {
                "title": "The Lesson of Humility",
                "content": "Anansi was ashamed. He thought he had all the wisdom, but a small child knew something he didn't. He realized that wisdom is not something one person can hoard—it should be shared. So he broke the calabash open, and wisdom spread across the world for everyone to learn from."
            }
        ],
        "cultural_note": "Anansi the spider is one of the most beloved characters in West and Central African folklore. He is a trickster, but his stories always teach important lessons. This story teaches that no one is too wise to learn, that we can learn from everyone—even children—and that wisdom is best when shared, not hoarded."
    },
    {
        "file": "eternal_queen.html",
        "id": "eternal_queen",
        "title": "The Queen Who Refused to Die",
        "subtitle": "A Tale of Immortality & Legacy from the Bamiléké People",
        "image": "https://i.pinimg.com/736x/83/8e/d8/838ed8605d08e09067446db67e20c610.jpg",
        "tribe": "Bamiléké",
        "sections": [
            {
                "title": "The Powerful Queen",
                "content": "There was once a powerful Bamiléké queen named Njindom. She was a wise and just ruler, and her people loved her. But as she grew old, she became afraid of death. She could not bear the thought of leaving her people and her kingdom behind."
            },
            {
                "title": "A Visit to the Witch Doctor",
                "content": "Queen Njindom called upon the most powerful witch doctor in the land. She asked him for a way to live forever. The witch doctor warned her that immortality was a great responsibility, but the queen insisted. So he gave her a special potion."
            },
            {
                "title": "The Queen's New Form",
                "content": "After drinking the potion, the queen did not die—but she did not stay as she was. She transformed into a powerful spirit who could live forever. She could no longer walk among her people as their ruler, but she could watch over them and guide them from the spirit world."
            },
            {
                "title": "A Living Legacy",
                "content": "To this day, the Bamiléké people tell stories of Queen Njindom. She is said to appear in dreams to wise leaders, to protect her kingdom from danger, and to guide her people. Even though she is not physically present, she continues to be a part of her people's lives, proving that true legacy is not about living forever, but about making a difference that lasts."
            }
        ],
        "cultural_note": "The Bamiléké people have a strong tradition of respecting their ancestors and believing in the continuing presence of spirits in the lives of the living. This legend celebrates that connection, as well as the power of good leadership that leaves a lasting impact on a community for generations."
    },
    {
        "file": "rain_bride.html",
        "id": "rain_bride",
        "title": "The Rain Bride of the Grassfields",
        "subtitle": "A Tale of Sacrifice & Love from the Kom People",
        "image": "https://i.pinimg.com/736x/18/06/f9/1806f998c473825e0778b17d7f2608a0.jpg",
        "tribe": "Kom",
        "sections": [
            {
                "title": "The Drought of Years",
                "content": "A terrible drought came to the Kom highlands. For years, the rains did not come. Rivers dried up, crops withered, and livestock died. The people prayed and performed rituals, but nothing worked. The land was dying, and the people knew they needed a miracle."
            },
            {
                "title": "The Rain Spirit's Request",
                "content": "One night, the chief had a dream. In the dream, a Rain Spirit appeared and said, 'I will bring rain back to your land, but only if you give me a bride—a young woman willing to come and live with me in the clouds.' The chief was heartbroken, but he knew what had to be done."
            },
            {
                "title": "A Brave Sacrifice",
                "content": "A young woman named Nini stepped forward. She loved her people more than she feared leaving them. So she dressed in her finest clothes, and the people of the village accompanied her to a high mountain where the clouds touched the earth. As she walked into the mist, the first drops of rain began to fall."
            },
            {
                "title": "Life Returns",
                "content": "Nini was never seen again in the village, but she was not forgotten. The rains returned, and the land became fertile once more. To this day, the Kom people tell the story of the Rain Bride and honor her sacrifice that saved their people. And sometimes, when the rain falls gently, they say it is Nini sending her love from the clouds."
            }
        ],
        "cultural_note": "Agriculture is the lifeblood of Kom society, and rain is essential for the crops that sustain the people. This legend reflects the deep connection between the Kom people and the natural world, and the value they place on sacrifice, love, and commitment to the community. It also emphasizes how women have often been central figures in Kom culture and history."
    },
    {
        "file": "healing_leaves.html",
        "id": "healing_leaves",
        "title": "The Healing Leaves of the Forest",
        "subtitle": "A Tale of Knowledge & Tradition from the Pygmy People",
        "image": "https://i.pinimg.com/736x/d9/59/79/d959794a6e735d0136d1719712991459.jpg",
        "tribe": "Pygmy (Baka)",
        "sections": [
            {
                "title": "The Sick Child",
                "content": "Deep in the rainforest, a Pygmy child fell seriously ill. The village healer tried every remedy she knew, but nothing worked. The child grew weaker, and the family feared they would lose her. In desperation, the healer decided to ask the forest spirits for help."
            },
            {
                "title": "The Spirits' Guidance",
                "content": "The healer spent the night in the forest, praying and listening. In a dream, the forest spirits appeared to her. They showed her a small plant with broad, green leaves. 'Make a tea from these leaves,' they said, 'and it will heal the child.'"
            },
            {
                "title": "The Healing Tea",
                "content": "At dawn, the healer searched the forest and found the plant exactly as it had been shown to her. She brewed a tea from the leaves and gave it to the child. Within days, the child began to recover. Soon, she was healthy and playing again with her friends."
            },
            {
                "title": "A Tradition of Healing",
                "content": "The healer carefully learned everything she could about the plant, and she taught her knowledge to the next generation. For generations, the Pygmy people have preserved this knowledge of medicinal plants, learning directly from the forest and its spirits. Even today, traditional healers continue the sacred work of caring for the health of their communities."
            }
        ],
        "cultural_note": "Indigenous forest peoples like the Baka Pygmies have an incredible knowledge of the rainforest and its plants, including which ones can be used for healing. This tradition has been passed down for thousands of years. This story honors that knowledge, the wisdom of traditional healers, and the sacred relationship between people and the forest."
    },
    {
        "file": "ancestor_wells.html",
        "id": "ancestor_wells",
        "title": "The Wells of the Ancestors",
        "subtitle": "A Tale of Memory & Community from the Mandara People",
        "image": "https://i.pinimg.com/736x/cb/0a/f7/cb0af7814d110bcb2458fb20396bdf95.jpg",
        "tribe": "Mandara",
        "sections": [
            {
                "title": "The First Ancestors",
                "content": "When the first Mandara people came to the land that would be their home, they faced a problem: there was no water. They searched everywhere, digging holes in the earth, but the soil was dry and hard. Desperately, they prayed to their ancestors for guidance."
            },
            {
                "title": "A Dream of Water",
                "content": "That night, the ancestors appeared in the dreams of the elders. 'Dig where the three baobab trees grow together,' they said, 'and you will find water that will sustain your people for all time.' The next morning, the people found the three baobabs and began to dig."
            },
            {
                "title": "The Sacred Wells",
                "content": "At the bottom of the hole, they hit water! The people dug deeper and built a well. Then, following more dreams from the ancestors, they dug other wells in sacred places around their land. These became the Wells of the Ancestors—sources of not just water, but also spiritual power."
            },
            {
                "title": "Living Memory",
                "content": "To this day, the Mandara people honor the Wells of the Ancestors. They are places of community gathering, where people come to collect water, to celebrate festivals, and to remember the ancestors who first cared for the land. The wells remind them that they are part of a long, unbroken chain of life."
            }
        ],
        "cultural_note": "Water is a vital resource, especially in the often-arid Mandara Mountains. Wells have long been central to community life. This legend connects the physical resource of water with the spiritual connection to ancestors, emphasizing the importance of memory, community, and respect for those who came before us."
    }
]

template = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - CULTIA</title>
    <link rel="icon" type="image/png" href="../img/top.png">
    
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,700;1,700&display=swap" rel="stylesheet">
    
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- AOS Animations -->
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    
    <style>
        :root {{
            --primary-green: #2d5a27;
            --accent-orange: #e67e22;
            --bg-light: #fdfaf5;
            --transition-smooth: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }}

        body {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: var(--bg-light);
            display: flex;
            min-height: 100vh;
        }}

        h1, h2, h3 {{
            font-family: 'Playfair Display', serif;
        }}

        .main-content {{
            flex: 1;
            background: #fdfaf5;
        }}

        .hero-banner {{
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('{image}');
            background-size: cover;
            background-position: center;
            height: 400px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            text-align: center;
            border-radius: 0 0 50px 50px;
            margin-bottom: -50px;
        }}

        .story-container {{
            max-width: 900px;
            margin: 0 auto;
            background: white;
            border-radius: 40px;
            padding: 80px 60px 60px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.05);
            position: relative;
            z-index: 10;
        }}

        .story-section {{
            margin-bottom: 40px;
            border-left: 4px solid var(--accent-orange);
            padding-left: 30px;
        }}

        .story-section h3 {{
            color: #333;
            font-weight: 800;
            margin-bottom: 20px;
        }}

        .story-text {{
            color: #444;
            line-height: 1.8;
            font-size: 1.1rem;
        }}

        .back-btn {{
            position: absolute;
            top: 40px;
            left: 40px;
            background: white;
            color: var(--primary-green);
            border: none;
            padding: 10px 20px;
            border-radius: 50px;
            font-weight: 700;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            transition: var(--transition-smooth);
            z-index: 100;
        }}

        .back-btn:hover {{
            transform: translateX(-5px);
            background: var(--primary-green);
            color: white;
        }}

        .cultural-note {{
            background: rgba(230, 126, 34, 0.05);
            border-radius: 30px;
            padding: 40px;
            margin-top: 60px;
            border: 1px dashed var(--accent-orange);
        }}
    </style>
</head>

<body>
    <div id="sidebar-container"></div>

    <div class="main-content">
        <div id="header-container"></div>

        <section class="hero-banner">
            <div data-aos="zoom-out">
                <h1 class="display-2 fw-bold mb-3">{title}</h1>
                <p class="lead fs-4 opacity-75">{subtitle}</p>
            </div>
        </section>

        <div class="container py-5">
            <div class="story-container" data-aos="fade-up">
                <a href="folkloreAndMyths.html" class="back-btn">
                    <i class="fas fa-arrow-left me-2"></i> Back to Folklore
                </a>

                {sections_html}

                <div class="cultural-note">
                    <h4 class="fw-bold mb-3"><i class="fas fa-leaf me-2"></i> Cultural Significance</h4>
                    <p class="mb-0 text-muted">{cultural_note}</p>
                </div>
                
        <div id="claimSection" class="bg-light rounded-4 p-5 mb-5 text-center">
            <div class="mb-3">
                <i class="fas fa-coins text-warning" style="font-size: 3rem;"></i>
            </div>
            <h4 class="fw-bold mb-2">Ready to Claim Your Points?</h4>
            <p class="text-muted mb-4">Mark this story as completed and earn <strong class="text-success">+50</strong> points!</p>
            <button id="completeStoryBtn" class="btn btn-success btn-lg rounded-pill px-5">
                <i class="fas fa-check-circle me-2"></i> Complete Story & Claim Points
            </button>
        </div>

        <!-- Beautiful Completion Modal -->
        <div class="modal fade" id="congratsModal" tabindex="-1" aria-labelledby="congratsModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content rounded-4 border-0 shadow-lg overflow-hidden">
                    <div class="modal-header bg-gradient text-center" style="background: linear-gradient(135deg, #2d5a27 0%, #1a3a17 100%); border: none;">
                        <h5 class="modal-title text-white fw-bold" id="congratsModalLabel">🎉 Congratulations!</h5>
                        <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body p-5 text-center">
                        <div class="mb-4">
                            <div class="mx-auto bg-success bg-opacity-10 rounded-circle d-flex align-items-center justify-content-center" style="width: 100px; height: 100px;">
                                <i class="fas fa-trophy text-success" style="font-size: 3.5rem;"></i>
                            </div>
                        </div>
                        <h4 class="fw-bold mb-2">Story Completed!</h4>
                        <p class="text-muted mb-4">You've earned <strong class="text-success" style="font-size: 1.5rem;">+50 points</strong> for completing this story!</p>
                    </div>
                    <div class="modal-footer border-0 justify-content-center gap-3">
                        <button type="button" class="btn btn-secondary rounded-pill px-4" id="continueBtn">
                            Continue Exploring
                        </button>
                        <a href="folkloreAndMyths.html" class="btn btn-success rounded-pill px-4">
                            Read Another Story
                        </a>
                    </div>
                </div>
            </div>
        </div>

        <div class="text-center py-4">
            <a href="folkloreAndMyths.html" class="btn btn-outline-success rounded-pill px-5 py-3">
                <i class="fas fa-arrow-left me-2"></i> Back to Stories
            </a>
        </div>
            </div>
        </div>
    </div>

    <!-- Add Settings Manager -->
    <script src="js/settingsManager.js"></script>
    <!-- Bootstrap 5 JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <!-- AOS Animations JS -->
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <!-- Gamification System -->
    <script src="js/gamification.js"></script>

        <script>
        document.addEventListener('DOMContentLoaded', function() {{
            AOS.init({{ duration: 800, once: true }});
            
            // Load Header and Sidebar
            fetch('includes/sidebar.html').then(r => r.text()).then(data => {{
                document.getElementById('sidebar-container').innerHTML = data;
            }});
            fetch('includes/header.html').then(r => r.text()).then(data => {{
                document.getElementById('header-container').innerHTML = data.replace('{{PAGE_TITLE}}', 'Story');
                
                // Initialize Theme Toggle in Header
                if (window.settingsManager) {{
                    window.settingsManager.initHeaderThemeToggle();
                }}
            }});

            // Complete Story Button
            const completeBtn = document.getElementById('completeStoryBtn');
            const claimSection = document.getElementById('claimSection');
            let congratsModal;
            
            // First, check if story is already completed on load
            async function checkStoryCompletion() {{
                try {{
                    const progressResponse = await fetch('/api/folklore/progress', {{ credentials: 'include' }});
                    if (progressResponse.ok) {{
                        const progressData = await progressResponse.json();
                        if (progressData.success && progressData.progress && progressData.progress['{story_id}'] && progressData.progress['{story_id}'].is_completed) {{
                            // Already completed
                            if (claimSection) {{
                                claimSection.innerHTML = `
                                    <div class="p-4">
                                        <div class="d-flex align-items-center justify-content-center gap-3 mb-3">
                                            <div class="bg-success bg-opacity-10 p-3 rounded-3">
                                                <i class="fas fa-check-circle text-success" style="font-size: 2.5rem;"></i>
                                            </div>
                                            <div class="text-start">
                                                <h6 class="fw-bold mb-0" style="color: #2d5a27;">Story Completed!</h6>
                                                <p class="text-muted mb-0">+50 points earned</p>
                                            </div>
                                        </div>
                                    </div>
                                `;
                                if (completeBtn) {{
                                    completeBtn.disabled = true;
                                    completeBtn.innerHTML = '<i class="fas fa-check me-2"></i>Already Completed';
                                    completeBtn.className = 'btn btn-secondary btn-lg rounded-pill px-5';
                                }}
                            }}
                        }}
                    }}
                }} catch (err) {{
                    console.error('Error checking story completion:', err);
                }}
            }}
            
            // Initialize modal
            const modalElement = document.getElementById('congratsModal');
            if (modalElement && window.bootstrap) {{
                congratsModal = new bootstrap.Modal(modalElement);
            }}
            
            checkStoryCompletion();
            
            if (completeBtn) {{
                completeBtn.addEventListener('click', async function() {{
                    try {{
                        const response = await fetch(`/api/folklore/progress/{story_id}/complete`, {{
                            method: 'POST',
                            credentials: 'include'
                        }});
                        
                        if (response.ok) {{
                            const data = await response.json();
                            if (data.success && data.points_awarded > 0) {{
                                // Show notification via gamification system
                                if (window.gamification) {{
                                    window.gamification.points += data.points_awarded;
                                    window.gamification.updateUI();
                                    window.gamification.broadcastUpdate();
                                }}
                                
                                // Update the section
                                if (claimSection) {{
                                    claimSection.innerHTML = `
                                        <div class="p-4">
                                            <div class="d-flex align-items-center justify-content-center gap-3 mb-3">
                                                <div class="bg-success bg-opacity-10 p-3 rounded-3">
                                                    <i class="fas fa-check-circle text-success" style="font-size: 2.5rem;"></i>
                                                </div>
                                                <div class="text-start">
                                                    <h6 class="fw-bold mb-0" style="color: #2d5a27;">Story Completed!</h6>
                                                    <p class="text-muted mb-0">+50 points earned</p>
                                                </div>
                                            </div>
                                        </div>
                                    `;
                                    completeBtn.disabled = true;
                                    completeBtn.innerHTML = '<i class="fas fa-check me-2"></i>Already Completed';
                                    completeBtn.className = 'btn btn-secondary btn-lg rounded-pill px-5';
                                }}
                                
                                // Show modal if available
                                if (congratsModal) {{
                                    congratsModal.show();
                                }}
                            }} else if (!data.success) {{
                                // Handle already completed gracefully
                                if (data.message && data.message.includes('already')) {{
                                    if (claimSection) {{
                                        claimSection.innerHTML = `
                                            <div class="p-4">
                                                <div class="d-flex align-items-center justify-content-center gap-3 mb-3">
                                                    <div class="bg-success bg-opacity-10 p-3 rounded-3">
                                                        <i class="fas fa-check-circle text-success" style="font-size: 2.5rem;"></i>
                                                    </div>
                                                    <div class="text-start">
                                                        <h6 class="fw-bold mb-0" style="color: #2d5a27;">Story Completed!</h6>
                                                        <p class="text-muted mb-0">+50 points earned</p>
                                                    </div>
                                                </div>
                                            </div>
                                        `;
                                        completeBtn.disabled = true;
                                        completeBtn.innerHTML = '<i class="fas fa-check me-2"></i>Already Completed';
                                        completeBtn.className = 'btn btn-secondary btn-lg rounded-pill px-5';
                                    }}
                                }}
                            }}
                        }}
                    }} catch (error) {{
                        console.error('Error completing story:', error);
                        alert('Error completing story. Please try again.');
                    }}
                }});
            }}

            // Add continue button listener if modal exists
            const continueBtn = document.getElementById('continueBtn');
            if (continueBtn && congratsModal) {{
                continueBtn.addEventListener('click', function() {{
                    congratsModal.hide();
                }});
            }}
        }});
    </script>
</body>

</html>
"""

# Create the files in the correct directory
output_dir = "CULTIA/Robix/Robix/Frontends/bot"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for story in stories:
    # Generate the sections HTML
    sections_html = ""
    for section in story["sections"]:
        sections_html += f"""
                <div class="story-section">
                    <h3>{section['title']}</h3>
                    <p class="story-text">{section['content']}</p>
                </div>
                """
    # Format the template with the story data
    content = template.format(
        title=story["title"],
        subtitle=story["subtitle"],
        image=story["image"],
        sections_html=sections_html,
        cultural_note=story["cultural_note"],
        story_id=story["id"]
    )
    # Write the file
    file_path = os.path.join(output_dir, story["file"])
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {story['file']}")

print("\n✅ All stories created successfully!")
