from docx import Document

realistic_website_data = [
    (1, "https://www.google.com", "Search Engine", "Fast and accurate search results; clean interface", "Data privacy concerns", "Essential tool for information retrieval"),
    (2, "https://www.youtube.com", "Video Sharing Platform", "Vast content library; user-friendly; personalized recommendations", "Frequent ads; content quality varies", "Excellent for entertainment and learning"),
    (3, "https://www.facebook.com", "Social Networking", "Connects people globally; diverse features like groups and events", "Privacy issues; spread of misinformation", "Great for staying connected but requires cautious use"),
    (4, "https://www.instagram.com", "Photo and Video Sharing Platform", "Visually appealing; easy to use; engaging features like stories and reels", "Algorithm changes; impact on mental health", "Popular platform for visual content sharing"),
    (5, "https://www.twitter.com", "Microblogging and Social Networking", "Real-time updates; platform for discussions and news", "Character limit; prevalence of trolling", "Effective for quick information and trends"),
    (6, "https://www.linkedin.com", "Professional Networking", "Facilitates professional connections; job opportunities", "Premium features behind paywall", "Valuable for career development and networking"),
    (7, "https://www.wikipedia.org", "Online Encyclopedia", "Extensive information; free access; collaborative editing", "Potential inaccuracies; vandalism", "Reliable starting point for research"),
    (8, "https://www.amazon.com", "E-commerce Platform", "Wide product range; user reviews; efficient delivery", "Counterfeit products; environmental concerns", "Convenient for online shopping"),
    (9, "https://www.netflix.com", "Streaming Service", "High-quality original content; ad-free experience", "Regional restrictions; increasing subscription costs", "Leading platform for diverse entertainment"),
    (10, "https://www.reddit.com", "Community Discussion Forum", "Wide range of topics; active communities; anonymity", "Moderation issues; potential for misinformation", "Engaging platform for discussions and information"),
    (11, "https://www.pinterest.com", "Image Sharing and Social Media", "Creative inspiration; organized boards; user-friendly", "Algorithm can be repetitive; ads", "Great for discovering and saving ideas"),
    (12, "https://www.tiktok.com", "Short-form Video Sharing", "Entertaining content; algorithm learns preferences quickly", "Data privacy concerns; addictive nature", "Fun platform for short videos"),
    (13, "https://www.ebay.com", "Online Marketplace", "Auctions and fixed-price sales; diverse product listings", "Risk of fraudulent sellers; varying product quality", "Useful for buying and selling a variety of items"),
    (14, "https://www.bing.com", "Search Engine", "Rewards program; integration with Microsoft services", "Less accurate results compared to competitors", "Viable alternative search engine"),
    (15, "https://www.yahoo.com", "Web Portal and Search Engine", "Offers news, email, and finance services", "Cluttered interface; declining popularity", "Comprehensive portal but needs modernization"),
    (16, "https://www.whatsapp.com", "Messaging Application", "End-to-end encryption; user-friendly; widely used", "Limited customization; dependency on phone number", "Reliable for instant messaging"),
    (17, "https://www.twitch.tv", "Live Streaming Platform", "Interactive live content; supportive community; monetization for creators", "Inconsistent content quality; occasional toxic chat", "Leading platform for live gaming and creative content"),
    (18, "https://www.nytimes.com", "News Publication", "In-depth reporting; reputable journalism", "Paywall limits access; perceived bias", "Trusted source for news and analysis"),
    (19, "https://www.cnn.com", "News and Media Outlet", "24/7 news coverage; multimedia content", "Sensationalism; ads", "Comprehensive news source but requires critical consumption"),
    (20, "https://www.bbc.com", "News and Media Organization", "Unbiased reporting; global coverage; diverse content", "Regional restrictions; limited interactivity", "Respected source for international news"),
    (21, "https://www.quora.com", "Question-and-Answer Platform", "Diverse topics; expert answers; community-driven", "Quality of answers varies; potential for misinformation", "Informative platform for knowledge sharing"),
    (22, "https://www.medium.com", "Online Publishing Platform", "High-quality articles; clean reading experience; supports writers", "Paywalled content; varying article quality", "Great for in-depth articles and diverse perspectives"),
    (23, "https://www.spotify.com", "Music Streaming Service", "Extensive music library; personalized playlists; offline listening", "Ads in free version; limited song skips in free tier", "Excellent for music discovery and listening"),
    (24, "https://www.apple.com", "Technology Company Website", "Sleek design; comprehensive product information; seamless ecosystem", "Premium pricing; limited customization", "Informative site for Apple products and services"),
    (25, "https://www.microsoft.com", "Technology Company Website", "Wide range of products; informative; integration with Windows", "Complex navigation; frequent updates", "Resourceful for Microsoft products and services"),
    (26, "https://www.adobe.com", "Software Company Website", "Industry-standard creative tools; comprehensive tutorials", "Subscription-based pricing; steep learning curve", "Essential for creative professionals"),
    (27, "https://www.canva.com", "Graphic Design Platform", "User-friendly; vast template library; free tier available", "Limited features in free version; internet required", "Ideal for quick and easy graphic design"),
    (28, "https://www.salesforce.com", "Customer Relationship Management", "Comprehensive CRM tools; customizable; cloud-based", "Expensive for small businesses; complex setup", "Powerful solution for enterprise customer management"),
    (29, "https://www.shopify.com", "E-commerce Platform", "Easy to set up; customizable templates; supports multiple payment gateways", "Transaction fees; limited customization without coding", "Great for small to medium-sized online stores"),
    (30, "https://www.airbnb.com", "Online Lodging Marketplace", "Unique accommodations; local experiences; user reviews", "Service fees; inconsistent host quality", "Excellent for finding diverse lodging options"),
]

# Create a new document with the filled table
doc = Document()
doc.add_heading("Website Evaluation Report", level=1)

# Add table headers
headers = ["Srno", "WebSiteURL", "Purpose Of Website", "Things Liked In Website", 
           "Things Disliked In Website", "Overall Evaluation"]
table = doc.add_table(rows=1, cols=len(headers))
header_row = table.rows[0]
for idx, header in enumerate(headers):
    header_row.cells[idx].text = header

# Fill the table with the actual data
for entry in realistic_website_data:
    row = table.add_row()
    for idx, value in enumerate(entry):
        row.cells[idx].text = str(value)

# Save the file
file_path = "./Assg_1.docx"
doc.save(file_path)