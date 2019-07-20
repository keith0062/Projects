
from random import choice
"""
Created on Fri Jul 19 11:18:03 2019

writer: Tom Koch
Copyright 2006 E.C. Publications Inc.

Hire Flyer Dept.
----------------
A few years out of school, most of us are amazed to discover that the
biggest clods among our former classmates have somehow latched onto the
best jobs. It's just that many under-achievers concentrate on learning
the only thing they will ever need to know, namely how to write the 
hyped up Job Application Letters that will make them seem qualified for 
cushy, high paying careers. MAD feels that its readers have the potential
to be just as boastful and dishonest in their job seeking correspondence.
So we are rushing to your aid with a pre-packaged kit that will enable
you to compose your own impressive, sure fire Application Letter. It is
easy to do. Merely give our all-purpose form the personal touch by 
filling each numbered blank with the attenbtion-getting phrase of your
choice. Then sit back and wait for lucrative offers to roll in as dazzled
employers rush to respond to your version of 
MAD'S "Do-It-Yourself" JOB APPLICATION LETTER
"""


# the groups of phrases
phrase1 = [ "it's obvious from the junk you make that you need my advice",
           "your top competitor said I was good enough to work for you",
           "I'm interested in thermal duct deployment, whatever that is",
           "I hear your building is air conditioned, and I sweat a lot" ]

phrase2 = [ "shuffling papers for eight hours a day to look busy",
           "filling an executive position as well as the next idiot",
           "going potty by myself",
           "thermal duct deployment, whatever that is" ]

phrase3 = [ "the last Venezuelan ambassador to Latvia",
           "a thermal duct deployer, whatever that is",
           "Chairman of the Board of Packard Motors",
           "presidential campaign advisor to Sergeant Shriver" 
        ]

phrase4 = [ "Oxford, just before the fire of 1969 destroyed my records",
           "the C.I.A. Academy under a secret code name",
           "many Ivy League institutions, including Dubuque Jr. High",
           "the Zsa Zsa Gabor School of Diesel Mechanics" 
        ]

phrase5 = [ "a Ph.D. in whatever your company requires",
           "top honors in Neo-Hegelian philosophy and baton twirling",
           "a bundle playing 'Go Fish' at a nickel a point",
           "66 and lost 13 for an enviable percentage of .835" 
        ]

phrase6 = [ "the upper four-fifths of my class",
           "one of the very, very hardest things they taught there",
           "front of a cheering throng of admirers",
           "a dark blue polyester suit I knitted myself" 
        ]

phrase7 = [ "advance research on social habits of Las Vegas chorus girls",
           "my impressions of Humphrey Bogart and Walter Mondale",
           "several things which I can only describe to you in person",
           "a dye job on my hair which has done worlds for my popularity" 
        ]

phrase8 = [ "difficult to explain to a layman like yourself",
           "involved with 'creative input', and other meaningless terms",
           "hard to master, especially since I broke my pencil",
           "geared to the natural talents of a water buffalo" 
        ]

phrase9 = [ "to better myself, regardless of who I had to step on",
           "a position of trust that would allow me to handle the cash",
           "a transfer to our branch office in Miami Beach",
           "permission to use the employee washroom" 
        ]

phrase10 = [ "a bottle of Listerine from the girls in the typing pool",
           "$35 from a Korean spy who knew I couldn't be bought cheap",
           "several phone calls calls from people I didn't even know",
           "a Scotch Tape dispenser of my very own" 
        ]

phrase11 = [ "a truly gifted brown nose apple polisher",
           "a constant threat to their job security",
           "a person they'd love to catch in the parking lot after dark",
           "the adult who most reminds them of Amy Carter" 
        ]

phrase12 = [ "as qualified as the clods you have working for you now",
           "less ashamed than I once did about sleeping with a Teddy Bear",
           "that I'm a credit to everything I stand for",
           "like someone who literally could tower over Nancy Walker" 
        ]

phrase13 = [ "less than you'd expect to pay each week for a microwave oven",
           "rather high because I'd like to afford a fling at bigamy",
           "naturally more than your cheapskate competitors are paying",
           "just enough to keep the loan sharks from breaking my kneecaps" 
        ]

phrase14 = [ "I am holding your mother hostage",
           "it's only a fraction of what you'd have to pay Robert Redford",
           "I have some choice pictures taken of you at a downtown motel",
           "it'd be on your conscience if I got my kneecaps broken" 
        ]

phrase15 = [ "being invited to your mansion to close the feal over drinks",
           "landing this job so I can stop sharing an apartment with your daughter",
           "next July 16, when I'll begin my first vacation at your expense",
           "getting your company back on its feet while there's still time" 
        ]


# the form letter template
letter = ("\n\n\nDear Sirs:\n\n" + 
    "    I am most anxious to present my job qualifications to your firm because " +
    choice(phrase1) + 
    ". I feel confident that I have been thoroughly trained in " + 
    choice(phrase2) + 
    " and have spent the past year gaining added experience by workng as " +
    choice(phrase3) + "." + 
    "\n\n    I received my higher education at " +
    choice(phrase4) +
    ", where I won " +
    choice(phrase5) +
    ". Following my graduation in " +
    choice(phrase6) +
    ", I went on to do " +
    choice(phrase7) + "." +
    "\n\n    Upon entering the field of business, my positions have become increasingly " +
    choice(phrase8) + 
    ". Forever seeking " + 
    choice(phrase9) + 
    ", I was ultimately honored to receive " +
    choice(phrase10) + 
    ". As a result, I am currently looked upon by my associates as " + 
    choice(phrase11) + 
    ". With this background, I naturally feel " + 
    choice(phrase12) + "." + 
    "\n\n    My starting salary requirement is " + 
    choice(phrase13) + 
    ". I sincerely believe I am well worth this amount because " + 
    choice(phrase14) + 
    ". Therefore, I look forward to " + 
    choice(phrase15) + "." +
    "\n\n\n                                       Very truly yours," +
    "\n\n\n                                       Name of Sender"
    )

print(letter)
