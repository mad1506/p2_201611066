
# coding: utf-8

# In[1]:

def milkRate(coffee):
    coffeeList=coffee[1:]
    freq=0.
    for i in coffeeList:
        x=i[2].upper()
        if i[2]=="NO":
            freq=freq
        else:
            freq=freq+1
    result=(freq/len(coffeeList))*100
    return result

def sumEngMarks(marks):
    d=list()
    for i in marks:
        x=i[0].upper()
        if x=="ENGLISH":
            d.append(i[1])
    return sum(d)

def sumMatMarks(marks):
    d=list()
    for i in marks:
        x=i[0].upper()
        if x=="MATH":
            d.append(i[1])
    return sum(d)

def averEngMarks(marks):
    d=list()
    for i in marks:
        x=i[0].upper()
        if x=="ENGLISH":
            d.append(i[1])
    return float(sum(d))/len(d)

def averMatMarks(marks):
    d=list()
    for i in marks:
        x=i[0].upper()
        if x=="MATH":
            d.append(i[1])
    return float(sum(d))/len(d)

def maxWord(lyrics):
    doc=lyrics
    d=dict()
    for line in doc:
        words=line.split()
        for c in words:
            if c not in d:
                d[c]=1
            else:
                d[c]=d[c]+1
    return max(d, key=d.get)

def averWellContented(datas):
    sumlist=[]
    list=datas[1:]
    for i in list:
        sumlist.append(i[1])
    sume=sum(sumlist)
    return sume/len(sumlist)

def averContented(datas):
    sumlist=[]
    list=datas[1:]
    for i in list:
        sumlist.append(i[2])
    sume=sum(sumlist)
    return sume/len(sumlist)

def averNotContented(datas):
    sumlist=[]
    list=datas[1:]
    for i in list:
        sumlist.append(i[4])
    sume=sum(sumlist)
    return sume/len(sumlist)

def averNeverContented(datas):
    sumlist=[]
    list=datas[1:]
    for i in list:
        sumlist.append(i[5])
    sume=sum(sumlist)
    return sume/len(sumlist)

def averContenteds(datas):
    return (averWellContented(datas)+averContented(datas))/2

def averNoContenteds(datas):
    return (averNotContented(datas)+averNeverContented(datas))/2

def lab10():
    coffee=[
    ["Coffee", "Water", "Milk", "Icecream"],
    ["Espresso", "No", "No", "No"],
    ["Long Black","Yes","No","No"],
    ["Flat White","No","Yes","No"],
    ["Cappuccino","No","Yes - Frothy","No"],
    ["Affogato","No","No","Yes"],
]
    res=milkRate(coffee)
    print "Milk Rate is: ", res, "%"
    marks=[
    ["English", 100],
    ["Math", 200],
    ["English", 200],
    ["Math", 200],
    ["English", 100],
    ["Math", 300],

]
    resEngSum=sumEngMarks(marks)
    resMatSum=sumMatMarks(marks)
    resEngAver=averEngMarks(marks)
    resMatAver=averMatMarks(marks)
    print "English Marks sum: ", resEngSum
    print "Math Marks sum: ", resMatSum
    print "English Marks average: ",resEngAver
    print "Math Marks average: ", resMatAver
    lyrics=[
    "when I find myself in times of trouble",
    "mother mary comes to me",
    "speaking words of wisdom , let it be",
    "and in my hour of darkness",
    "she is standing right in front of me",
    "speaking words of wisdom , let it be",
    "let it be , let it be",
    "let it be , let it be",
    "whisper words of wisdom , let it be",
    "and when the broken-hearted people",
    "living in the world agree",
    "there will be an answer , let it be",
    "for though they may be parted",
    "there is still a chance that they will see",
    "there will be an answer , let it be",
    "let it be , let it be",
    "let it be , let it be",
    "yeah, there will be an answer , let it be",
    "let it be , let it be",
    "let it be , let it be",
    "whisper words of wisdom , let it be",
    "let it be , let it be",
    "ah, let it be, yeah , let it be",
    "whisper words of wisdom , let it be",
    "and when the night is cloudy",
    "there is still a light that shines on me",
    "shine on until tomorrow , let it be",
    "i wake up to the sound of music ,",
    "mother mary comes to me",
    "speaking words of wisdom , let it be",
    "let it be , let it be",
    "let it be , yeah , let it be",
    "oh, there will be an answer , let it be",
    "let it be , let it be",
    "let it be , yeah , let it be",
    "whisper words of wisdom,  let it be",
]
    max=maxWord(lyrics)
    print "High frequences rates word: ", max
    
    datas=[
    ["division", "well contented", "contented", "normal" "not contented" "never contented"],
    ["contents of education", 13.1, 37.1, 39.6, 8.7, 1.5],
    ["methods of education", 10.6, 34.6, 39.5, 13.4, 1.9],
    ["relations of friends", 27.1, 40.0, 28.5, 2.9, 1.5],
    ["relations of teachers", 16.2, 37.8, 38.4, 6.8, 0.8],
    ["facilities of school", 11.4, 29.8, 39.0, 14.8, 4.9],
    ["surroundings of school", 12.2, 26.5, 42.0, 14.9, 4.4],
    ["major", 13.5, 29.7, 43.4, 11.1, 2.4],
    ["wide school life", 13.7, 37.6, 43.4, 4.1, 1.2]
]
    averA=averContenteds(datas)
    averB=averNoContenteds(datas)
    print "Average of Well Contented & Contented: ", averA
    print "Average of Not Contented & Never Contented: ", averB
    
    past=[
    "MY fellow-citizens, no people on earth have more cause to be thankful than ours, and this is said reverently, in no spirit of boastfulness in our own strength, but with gratitude to the Giver of Good who has blessed us with the conditions which have enabled us to achieve so large a measure of well-being and of happiness. To us as a people it has been granted to lay the foundations of our national life in a new continent. We are the heirs of the ages, and yet we have had to pay few of the penalties which in old countries are exacted by the dead hand of a bygone civilization. We have not been obliged to fight for our existence against any alien race; and yet our life has called for the vigor and effort without which the manlier and hardier virtues wither away. Under such conditions it would be our own fault if we failed; and the success which we have had in the past, the success which we confidently believe the future will bring, should cause in us no feeling of vainglory, but rather a deep and abiding realization of all which life has offered us; a full acknowledgment of the responsibility which is ours; and a fixed determination to show that under a free government a mighty people can thrive best, alike as regards the things of the body and the things of the soul",
    "Much has been given us, and much will rightfully be expected from us. We have duties to others and duties to ourselves; and we can shirk neither. We have become a great nation, forced by the fact of its greatness into relations with the other nations of the earth, and we must behave as beseems a people with such responsibilities. Toward all other nations, large and small, our attitude must be one of cordial and sincere friendship. We must show not only in our words, but in our deeds, that we are earnestly desirous of securing their good will by acting toward them in a spirit of just and generous recognition of all their rights. But justice and generosity in a nation, as in an individual, count most when shown not by the weak but by the strong. While ever careful to refrain from wrongdoing others, we must be no less insistent that we are not wronged ourselves. We wish peace, but we wish the peace of justice, the peace of righteousness. We wish it because we think it is right and not because we are afraid. No weak nation that acts manfully and justly should ever have cause to fear us, and no strong power should ever be able to single us out as a subject for insolent aggression.",
    "Our relations with the other powers of the world are important; but still more important are our relations among ourselves. Such growth in wealth, in population, and in power as this nation has seen during the century and a quarter of its national life is inevitably accompanied by a like growth in the problems which are ever before every nation that rises to greatness. Power invariably means both responsibility and danger. Our forefathers faced certain perils which we have outgrown. We now face other perils, the very existence of which it was impossible that they should foresee. Modern life is both complex and intense, and the tremendous changes wrought by the extraordinary industrial development of the last half century are felt in every fiber of our social and political being. Never before have men tried so vast and formidable an experiment as that of administering the affairs of a continent under the forms of a Democratic republic. The conditions which have told for our marvelous material well-being, which have developed to a very high degree our energy, self-reliance, and individual initiative, have also brought the care and anxiety inseparable from the accumulation of great wealth in industrial centers. Upon the success of our experiment much depends, not only as regards our own welfare, but as regards the welfare of mankind. If we fail, the cause of free self-government throughout the world will rock to its foundations, and therefore our responsibility is heavy, to ourselves, to the world as it is to-day, and to the generations yet unborn. There is no good reason why we should fear the future, but there is every reason why we should face it seriously, neither hiding from ourselves the gravity of the problems before us nor fearing to approach these problems with the unbending, unflinching purpose to solve them aright.",
    "Yet, after all, though the problems are new, though the tasks set before us differ from the tasks set before our fathers who founded and preserved this Republic, the spirit in which these tasks must be undertaken and these problems faced, if our duty is to be well done, remains essentially unchanged. We know that self-government is difficult. We know that no people needs such high traits of character as that people which seeks to govern its affairs aright through the freely expressed will of the freemen who compose it. But we have faith that we shall not prove false to the memories of the men of the mighty past. They did their work, they left us the splendid heritage we now enjoy. We in our turn have an assured confidence that we shall be able to leave this heritage unwasted and enlarged to our children and our children's children. To do so we must show, not merely in great crises, but in the everyday affairs of life, the qualities of practical intelligence, of courage, of hardihood, and endurance, and above all the power of devotion to a lofty ideal, which made great the men who founded this Republic in the days of Washington, which made great the men who preserved this Republic in the days of Abraham Lincoln."
]
    today=[
    "Vice President Cheney, Mr. Chief Justice, President Carter, President Bush, President Clinton, reverend clergy, distinguished guests, fellow citizens:",
    "On this day, prescribed by law and marked by ceremony, we celebrate the durable wisdom of our Constitution, and recall the deep commitments that unite our country. I am grateful for the honor of this hour, mindful of the consequential times in which we live, and determined to fulfill the oath that I have sworn and you have witnessed.",
    "At this second gathering, our duties are defined not by the words I use, but by the history we have seen together. For a half century, America defended our own freedom by standing watch on distant borders. After the shipwreck of communism came years of relative quiet, years of repose, years of sabbatical —and then there came a day of fire.",
    "We have seen our vulnerability —and we have seen its deepest source. For as long as whole regions of the world simmer in resentment and tyranny —prone to ideologies that feed hatred and excuse murder — violence will gather, and multiply in destructive power, and cross the most defended borders, and raise a mortal threat. There is only one force of history that can break the reign of hatred and resentment, and expose the pretensions of tyrants, and reward the hopes of the decent and tolerant, and that is the force of human freedom.",
    "We are led, by events and common sense, to one conclusion: The survival of liberty in our land increasingly depends on the success of liberty in other lands. The best hope for peace in our world is the expansion of freedom in all the world.",
    "America's vital interests and our deepest beliefs are now one. From the day of our Founding, we have proclaimed that every man and woman on this earth has rights, and dignity, and matchless value, because they bear the image of the Maker of Heaven and earth. Across the generations we have proclaimed the imperative of self-government, because no one is fit to be a master, and no one deserves to be a slave. Advancing these ideals is the mission that created our Nation. It is the honorable achievement of our fathers. Now it is the urgent requirement of our nation's security, and the calling of our time.",
    "So it is the policy of the United States to seek and support the growth of democratic movements and institutions in every nation and culture, with the ultimate goal of ending tyranny in our world.",
    "This is not primarily the task of arms, though we will defend ourselves and our friends by force of arms when necessary. Freedom, by its nature, must be chosen, and defended by citizens, and sustained by the rule of law and the protection of minorities. And when the soul of a nation finally speaks, the institutions that arise may reflect customs and traditions very different from our own. America will not impose our own style of government on the unwilling. Our goal instead is to help others find their own voice, attain their own freedom, and make their own way.",
    "The great objective of ending tyranny is the concentrated work of generations. The difficulty of the task is no excuse for avoiding it. America's influence is not unlimited, but fortunately for the oppressed, America's influence is considerable, and we will use it confidently in freedom's cause.",
    "My most solemn duty is to protect this nation and its people against further attacks and emerging threats. Some have unwisely chosen to test America's resolve, and have found it firm.",
    "We will persistently clarify the choice before every ruler and every nation: The moral choice between oppression, which is always wrong, and freedom, which is eternally right. America will not pretend that jailed dissidents prefer their chains, or that women welcome humiliation and servitude, or that any human being aspires to live at the mercy of bullies.",
    "We will encourage reform in other governments by making clear that success in our relations will require the decent treatment of their own people. America's belief in human dignity will guide our policies, yet rights must be more than the grudging concessions of dictators; they are secured by free dissent and the participation of the governed. In the long run, there is no justice without freedom, and there can be no human rights without human liberty.",
    "Some, I know, have questioned the global appeal of liberty —though this time in history, four decades defined by the swiftest advance of freedom ever seen, is an odd time for doubt. Americans, of all people, should never be surprised by the power of our ideals. Eventually, the call of freedom comes to every mind and every soul. We do not accept the existence of permanent tyranny because we do not accept the possibility of permanent slavery. Liberty will come to those who love it.",
    "Today, America speaks anew to the peoples of the world:",
    "All who live in tyranny and hopelessness can know: the United States will not ignore your oppression, or excuse your oppressors. When you stand for your liberty, we will stand with you.",
    "Democratic reformers facing repression, prison, or exile can know: America sees you for who you are: the future leaders of your free country.",
    "The rulers of outlaw regimes can know that we still believe as Abraham Lincoln did: Those who deny freedom to others deserve it not for themselves; and, under the rule of a just God, cannot long retain it."
    "The leaders of governments with long habits of control need to know: To serve your people you must learn to trust them. Start on this journey of progress and justice, and America will walk at your side.",
    "And all the allies of the United States can know: we honor your friendship, we rely on your counsel, and we depend on your help. Division among free nations is a primary goal of freedom's enemies. The concerted effort of free nations to promote democracy is a prelude to our enemies' defeat.",
    "Today, I also speak anew to my fellow citizens:",
    "From all of you, I have asked patience in the hard task of securing America, which you have granted in good measure. Our country has accepted obligations that are difficult to fulfill, and would be dishonorable to abandon. Yet because we have acted in the great liberating tradition of this nation, tens of millions have achieved their freedom. And as hope kindles hope, millions more will find it. By our efforts, we have lit a fire as well —a fire in the minds of men. It warms those who feel its power, it burns those who fight its progress, and one day this untamed fire of freedom will reach the darkest corners of our world.",
    "A few Americans have accepted the hardest duties in this cause —in the quiet work of intelligence and diplomacy ... the idealistic work of helping raise up free governments ... the dangerous and necessary work of fighting our enemies. Some have shown their devotion to our country in deaths that honored their whole lives —and we will always honor their names and their sacrifice.",
    "All Americans have witnessed this idealism, and some for the first time. I ask our youngest citizens to believe the evidence of your eyes. You have seen duty and allegiance in the determined faces of our soldiers. You have seen that life is fragile, and evil is real, and courage triumphs. Make the choice to serve in a cause larger than your wants, larger than yourself —and in your days you will add not just to the wealth of our country, but to its character.",
    "America has need of idealism and courage, because we have essential work at home —the unfinished work of American freedom. In a world moving toward liberty, we are determined to show the meaning and promise of liberty.",
    "In America's ideal of freedom, citizens find the dignity and security of economic independence, instead of laboring on the edge of subsistence. This is the broader definition of liberty that motivated the Homestead Act, the Social Security Act, and the G.I. Bill of Rights. And now we will extend this vision by reforming great institutions to serve the needs of our time. To give every American a stake in the promise and future of our country, we will bring the highest standards to our schools, and build an ownership society. We will widen the ownership of homes and businesses, retirement savings and health insurance —preparing our people for the challenges of life in a free society. By making every citizen an agent of his or her own destiny, we will give our fellow Americans greater freedom from want and fear, and make our society more prosperous and just and equal.",
    "In America's ideal of freedom, the public interest depends on private character —on integrity, and tolerance toward others, and the rule of conscience in our own lives. Self-government relies, in the end, on the governing of the self. That edifice of character is built in families, supported by communities with standards, and sustained in our national life by the truths of Sinai, the Sermon on the Mount, the words of the Koran, and the varied faiths of our people. Americans move forward in every generation by reaffirming all that is good and true that came before —ideals of justice and conduct that are the same yesterday, today, and forever.",
    "In America's ideal of freedom, the exercise of rights is ennobled by service, and mercy, and a heart for the weak. Liberty for all does not mean independence from one another. Our nation relies on men and women who look after a neighbor and surround the lost with love. Americans, at our best, value the life we see in one another, and must always remember that even the unwanted have worth. And our country must abandon all the habits of racism, because we cannot carry the message of freedom and the baggage of bigotry at the same time.",
    "From the perspective of a single day, including this day of dedication, the issues and questions before our country are many. From the viewpoint of centuries, the questions that come to us are narrowed and few. Did our generation advance the cause of freedom? And did our character bring credit to that cause?",
    "These questions that judge us also unite us, because Americans of every party and background, Americans by choice and by birth, are bound to one another in the cause of freedom. We have known divisions, which must be healed to move forward in great purposes —and I will strive in good faith to heal them. Yet those divisions do not define America. We felt the unity and fellowship of our nation when freedom came under attack, and our response came like a single hand over a single heart. And we can feel that same unity and pride whenever America acts for good, and the victims of disaster are given hope, and the unjust encounter justice, and the captives are set free.",
    "We go forward with complete confidence in the eventual triumph of freedom. Not because history runs on the wheels of inevitability; it is human choices that move events. Not because we consider ourselves a chosen nation; God moves and chooses as He wills. We have confidence because freedom is the permanent hope of mankind, the hunger in dark places, the longing of the soul. When our Founders declared a new order of the ages; when soldiers died in wave upon wave for a union based on liberty; when citizens marched in peaceful outrage under the banner Freedom Now —they were acting on an ancient hope that is meant to be fulfilled. History has an ebb and flow of justice, but history also has a visible direction, set by liberty and the Author of Liberty.",
    "When the Declaration of Independence was first read in public and the Liberty Bell was sounded in celebration, a witness said, It rang as if it meant something. In our time it means something still. America, in this young century, proclaims liberty throughout all the world, and to all the inhabitants thereof. Renewed in our strength — tested, but not weary — we are ready for the greatest achievements in the history of freedom."
]
    pastmaxword=maxWord(past)
    todaymaxword=maxWord(today)
    print "past max word: ", pastmaxword
    print "today max word: ", todaymaxword
    
def main():
    lab10()
    
if __name__=="__main__":
    main()
