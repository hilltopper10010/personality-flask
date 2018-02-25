from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method=="POST":
        #TODO Make algorithm that determines job from survey data
        overalldescription = ""
        description = ""
        job = ""
        salary = ""
        categorydescriptions = {
            "STEM": "Your school has an excellent reputation, particularly in math and science. You enjoy science and math, and get straight As in those subjects.",
            "humanities": "You love to study how people process and document the human experience. Since humans have been able, we have used philosophy, literature, religion, art, music, history and language to understand and record our world, and you strive to broaden your understanding of those fields.",
            "arts": "You enjoy experiencing the arts and culture.  You are engaged in life and empowered to be fulfilled, responsible citizens who can make a profound positive impact on this world through your artistic contributions.",
            "badjob": "You aren't the best student, and just need to make a living.  This job, although not very lucrative, will get food on the table for you and your family.  School was never your strongsuit, and a college future is uncertain.  You do not possess many of the qualities sought after by high quality employers."
        }
        descriptions = {
            "Attorney": "A lawyer is a person who practices law, as an advocate, barrister, attorney, counselor, solicitor, not as a paralegal or charter executive secretary.[1] Working as a lawyer involves the practical application of abstract legal theories and knowledge to solve specific individualized problems, or to advance the interests of those who hire lawyers to perform legal services.",
            "Historian": "A historian is a person who studies and writes about the past, and is regarded as an authority on it. Historians are concerned with the continuous, methodical narrative and research of past events as relating to the human race; as well as the study of all history in time. If the individual is concerned with events preceding written history, the individual is an historian of prehistory.",
            "Doctor": "A physician, medical practitioner, medical doctor, or simply doctor is a professional who practises medicine, which is concerned with promoting, maintaining, or restoring health through the study, diagnosis, and treatment of disease, injury, and other physical and mental impairments. Physicians may focus their practice on certain disease categories, types of patients and methods of treatment—known as specialities—or they may assume responsibility for the provision of continuing and comprehensive medical care to individuals, families, and communities—known as general practice.",
            "Coal Miner": "Coal miners extract coal from underground mines or participate in strip mining activities. They dig tunnels, operate machinery, transport coal out of the mines, and secure the mines.",
            "Assembly Line Worker": "Assembly workers fit together the component parts of a product or segment of a product using tools, machines, and their hands.",
            "Logger": "Logging workers cut down trees, operate machinery to transport logs, cut logs into desired lengths, and maintain equipment.",
            "Farm Worker": "Farm workers cultivate and fertilize fields, plant and harvest crops, and operate farm machinery. They convey harvested crops to storage areas.",
            "Fishing Worker": "Fishing Workers prepare and maintain poles, nets, and other fishing gear. They catch, extract, and store fish.  Fishers unload their catch upon return to the docks.",
            "Taxi Driver": "Taxi drivers transport customers to airports and other destinations. They collect fares and conduct conversations with passengers.",
            "Fast Food Clerk": "Fast food and short order cooks prepare meals for patrons of fast food establishments, diners, and other non-premium eateries.",
            "Postman": "Postal workers sort and deliver the mail and assist post office patrons with their mailing needs.",
            "Bank Teller": "Bank tellers assist patrons with deposits and withdrawals, cash checks, reconcile balances, and communicate information about fees, policies and bank services.",
            "Medical Transcriptionist": "Medical transcriptionists convert recordings of patient interactions by physicians and other healthcare professionals to written documents They interpret medical terms and abbreviations.",
            "Retail Sales Associate": "Retail sales associates stock and display merchandise, advise customers, promote products, and process transactions.",
            "Newspaper Reporter": "Newspaper reporters research and write stories about local, regional, and national events.",
            "Petroleum Engineer": "Petroleum engineers work with geoscientists and other specialists to understand the geologic formation of the rock containing the reservoir. They then determine the drilling methods, design the drilling equipment, implement the drilling plan, and monitor operations.",
            "Nuclear Engineer": "Nuclear engineers research and develop the processes, instruments, and systems used to derive benefits from nuclear energy and radiation. Many of these engineers find industrial and medical uses for radioactive materials—for example, in equipment used in medical diagnosis and treatment.",
            "Marine Engineer": "Marine engineering includes the engineering of boats, ships, oil rigs and any other marine vessel or structure, as well as oceanographic engineering.",
            "Chemical Engineer": "Chemical engineering is a branch of engineering that applies physical sciences, life sciences, together with applied mathematics and economics to produce, transform, transport, and properly use chemicals, materials and energy.",
            "Research Scientist": "Computer and information research scientists invent and design new approaches to computing technology and find innovative uses for existing technology. They study and solve complex problems in computing for business, medicine, science, and other fields.",
            "Aerospace Engineer": "Aerospace engineering is the primary field of engineering concerned with the development of aircraft and spacecraft. It has two major and overlapping branches: Aeronautical engineering and Astronautical Engineering.",
            "Marine Architect": "Naval architecture, also known as naval engineering, is an engineering discipline dealing with the engineering design process, shipbuilding, maintenance, and operation of marine vessels and structures.",
            "Nuclear Medicine Technologist": "The nuclear medicine technologist is a highly specialized health care professional who looks at how the body functions in order to help in diagnosis and treatment of a range of conditions and diseases. Nuclear medicine combines imaging, patient care, chemistry, physics, mathematics, computer technology, and medicine.",
            "Business Analyst": "Business intelligence analysts use data to figure out market and business trends for companies to increase profits and efficiency. They may work directly for a company or as a consultant.",
            "Software Developer": "Software developers are the creative minds behind computer programs. Some develop the applications that allow people to do specific tasks on a computer or another device. Others develop the underlying systems that run the devices or that control networks.",
            "Teacher": "Teachers may provide instruction in literacy and numeracy, craftsmanship or vocational training, the arts, religion, civics, community roles, or life skills.  Formal teaching tasks include preparing lessons according to agreed curricula, giving lessons, and assessing pupil progress.",
            "Social Worker": "Social work is an academic discipline and profession that concerns itself with individuals, families, groups and communities in an effort to enhance social functioning and overall well-being.",
            "Writer": "A writer is a person who uses written words in various styles and techniques to communicate their ideas. Writers produce various forms of literary art and creative writing such as novels, short stories, poetry, plays, screenplays, and essays as well as various reports and news articles that may be of interest to the public.",
            "Graphic Designer": "Graphic design is the process of visual communication and problem-solving using one or more of typography, photography and illustration.",
            "Human Resources Specialist": "Human resources specialists recruit, screen, interview, and place workers. They often handle other human resources work, such as those related to employee relations, compensation and benefits, and training.",
            "Public Relations Specialist": "Public relations specialists create and maintain a favorable public image for the organization they represent. They craft media releases and develop social media programs to shape public perception of their organization and to increase awareness of its work and goals.",
            "Psychologist": "A psychologist is a mental health professional who evaluates and studies behavior and mental processes. In order to become a psychologist, a person often completes a graduate university degree in psychology, but in most jurisdictions, members of other behavioral professions (such as counselors and psychiatrists) can also evaluate, diagnose, treat, and study mental processes.",
            "Sociologist": "Sociologists study society and social behavior by examining the groups, cultures, organizations, social institutions, and processes that develop when people interact and work together.",
            "Archaeologist": "Archaeology, or archeology, is the study of human activity through the recovery and analysis of material culture. The archaeological record consists of artifacts, architecture, biofacts or ecofacts, and cultural landscapes.",
            "Economist": "Economists may analyze issues such as consumer demand and sales to help a company maximize its profits. Economists also work for research firms and think tanks, where they study and analyze a variety of economic issues.",
            "Photographer": "A photographer records events and tells stories using images. He or she takes pictures of people, places, events, and objects. Photographers often specialize in a type of photography.",
            "Art Director": "Art Director is the title for a variety of similar job functions in theater, advertising, marketing, publishing, fashion, film and television, the Internet, and video games. It is the charge of a sole art director to supervise and unify the vision.",
            "Film Director": "A film director is a person who directs the making of a film. A film director controls a film's artistic and dramatic aspects and visualizes the screenplay (or script) while guiding the technical crew and actors in the fulfillment of that vision. The director has a key role in choosing the cast members, production design, and the creative aspects of filmmaking.",
            "Art Professor": "Teaching artists, also known as artist educators or community artists, are professional artists who teach and integrate their art form, perspectives, and skills into a wide range of settings.",
            "Talent Agent": "A talent agent, or booking agent, is a person who finds jobs for actors, authors, film directors, musicians, models, film producers, professional athletes, writers, screenwriters, broadcast journalists, and other professionals in various entertainment or broadcast businesses. In addition, an agent defends, supports and promotes the interest of their clients. Talent agencies specialize, either by creating departments within the agency or developing entire agencies that primarily or wholly represent one specialty.",
            "Fashion Designer": "Fashion design is the art of application of design and aesthetics or natural beauty to clothing and accessories. Fashion design is influenced by cultural and social attitudes, and has varied over time and place.",
            "Architect": "An architect is a person who plans, designs, and reviews the construction of buildings. To practice architecture means to provide services in connection with the design of buildings and the space within the site surrounding the buildings, that have as their principal purpose human occupancy or use."
            }
        badjobs = ["Coal Miner", "Assembly Line Worker", "Logger", "Farm Worker", "Fishing Worker", "Taxi Driver", "Fast Food Clerk", "Postman", "Bank Teller", "Medical Transcriptionist", "Retail Sales Associate", "Newspaper Reporter"]
        badsalaries = ["$60K/yr", "$16/hr", "$35K/yr", "$20K/yr", "$14/hr", "$25K/yr", "$10/hr", "$45K/yr", "$13/hr", "$17/hr", "$11/hr", "$35K/yr"]
        STEMjobs = ["Software Developer", "Business Analyst", "Nuclear Medicine Technologist", "Marine Architect", "Aerospace Engineer", "Research Scientist", "Chemical Engineer", "Marine Engineer", "Nuclear Engineer", "Petroleum Engineer", "Physician"]
        STEMsalaries = ["$100K/yr", "$66K/yr", "$75K/yr", "$55K/yr", "$110K/yr", "$110K/yr", "$100K/yr", "$85K/yr", "$105K/yr", "$130K/yr", "190K/yr"]
        humanitiesjobs = ["Teacher", "Social Worker", "Writer", "Historian", "Human Resources Specialist", "Public Relations Specialist", "Psychologist", "Sociologist", "Archaeologist", "Economist", "Attorney"]
        humanitiessalaries = ["$50K/yr", "$45K/yr", "$60K/yr", "$50K/yr", "$55K/yr", "$55K/yr", "$80K/yr", "$75K/yr", "$105K/yr", "$120K/yr", "120K/yr"]
        artsjobs = ["Photographer", "Art Director", "Film Director", "Art Professor", "Talent Agent", "Fashion Designer", "Architect"]
        artssalaries = ["$30K/yr", "$90K/yr", "$70K/yr", "$70K/yr", "$85K/yr", "$60K/yr", "$75K/yr"]
        goodjobcategory = ""
        jobcategory = "goodjob"
        totalscore = 0
        name = request.form.get("name")
        characteristics = ["loyal", "problem-solver", "eager", "collaborative", "determined", "flexible", "work-ethic", "technical", "honest", "communication"]
        for characteristic in characteristics:
            temp = request.form.get(characteristic)
            if temp:
                totalscore += 7.5
        grade = request.form.get("grade")
        if grade == "A":
            totalscore += 25
        if grade == "C":
            totalscore += -25
        if grade == "D":
            totalscore += -50
        if totalscore < 65:
            jobcategory = "badjob"
        pet = request.form.get("pet")
        home = request.form.get("home")
        sport = request.form.get("sport")
        music = request.form.get("music")
        subject = request.form.get("subject")
        region = request.form.get("region")
        totalscore += int(pet) + int(home) + int(sport) + int(music) + int(region)
        if subject == "science" or subject == "math":
            goodjobcategory="STEM"
            overalldescription = categorydescriptions["STEM"]
        elif subject == "english" or subject == "history":
            goodjobcategory="humanities"
            overalldescription = categorydescriptions["humanities"]
        else:
            goodjobcategory="arts/culture"
            overalldescription = categorydescriptions["arts"]
        if jobcategory == "badjob":
            job = badjobs[round((totalscore + 100) * 11 / 250)]
            salary = badsalaries[round((totalscore + 100) * 11 / 250)]
            overalldescription = categorydescriptions["badjob"]
        elif jobcategory == "goodjob":
            if goodjobcategory == "STEM":
                job = STEMjobs[round((totalscore - 65) * 10 / 85)]
                salary = STEMsalaries[round((totalscore - 65) * 10 / 85)]
            elif goodjobcategory == "humanities":
                job = humanitiesjobs[round((totalscore - 65) * 9 / 85)]
                salary = humanitiessalaries[round((totalscore - 65) * 9 / 85)]
            else:
                job = artsjobs[round((totalscore - 65) * 6 / 85)]
                salary = artssalaries[round((totalscore - 65) * 6 / 85)]
        description = descriptions[job]
        print(totalscore)
        if jobcategory == "goodjob":
            return render_template("goodjob.html", overalldescription = overalldescription, name = name, job = job, salary = salary, description = description)
        elif jobcategory == "badjob":
            return render_template("badjob.html", overalldescription = overalldescription, name = name, job = job, salary = salary, description = description)
    else:
        return render_template("index.html")
