# -*- coding: utf-8 -*-

from sopel import module

import random


@module.commands('perceval', 'pq')
def perquote(bot, trigger):
    quote = random.choice(tuple(quotes_P))
    bot.say(quote)

@module.commands('karadoc', 'kd')
def karquote(bot, trigger):
    quote = random.choice(tuple(quotes_K))
    bot.say(quote)

@module.commands('burgonde', 'bg')
def burquote(bot, trigger):
    quote = random.choice(tuple(quotes_B))
    bot.say(quote)

@module.commands('kadoc', 'kc')
def kadquote(bot, trigger):
    quote = random.choice(tuple(quotes_C))
    bot.say(quote)

@module.commands('maitredarmes', 'ma')
def marquote(bot, trigger):
    quote = random.choice(tuple(quotes_M))
    bot.say(quote)


# needed a one file solution, I'm sorry
# quotes are arranged versions of https://fr.wikiquote.org/wiki/Kaamelott/Perceval
quotes_P = {
    'Par exemple, Sire, Léodagan et moi on fait semblant de vous prendre en otage : on vous met une dague sous le cou et on traverse le camp adverse en gueulant : "Bougez pas, bougez pas ou on bute le roi!"...',
    'Putain, en plein dans sa mouille !',
    'C’est pas faux.',
    'Toi un jour je te crame ta famille, toi.',
    'Faut arrêter ces conneries de nord et de sud ! Une fois pour toutes, le nord, suivant comment on est tourné, ça change tout !',
    'Donc, pour résumer, je suis souvent victime des colibris, sous-entendu des types qu’oublient toujours tout. Euh, non… Bref, tout ça pour dire, que je voudrais bien qu’on me considère en tant que Tel.',
    'Excusez, c’est juste pour vous dire que je vais pas pouvoir rester aujourd’hui ! Faut que je retourne à la ferme de mes vieux ! Y a ma grand-mère qui a glissé sur une bouse ! C’est le vrai merdier !',
    'C’est pour ça : j’lis jamais rien. C’est un vrai piège à cons c’t’histoire-là. En plus j’sais pas lire.',
    'S’ils sont équidistants en même temps que nous, on peut repérer le dragon par rapport à une certaine distance. Si le dragon s’éloigne, on s’ra équidistant, mais ça s’ra vachement moins précis et... et pas réciproque.',
    'Sire, avec tout le respect, est-ce que la reine a les fesses blanches ?',
    'Ça sert à rien, un siège, si elle est enceinte, il faut des linges blancs et une bassine d\'eau chaude.',
    ' Une fois, à une exécution, je m\'approche d\'une fille. Pour rigoler, je lui fais : "Vous êtes de la famille du pendu ?" ... C\'était sa sœur. Bonjour l\'approche !',
    'Si Joseph d\'Arimathie a pas été trop con, vous pouvez être sûr que le Graal, c\'est un bocal à anchois.',
    'Sire, Sire ! On en a gros !',
    'Moi, j\'serais vous, je vous écouterais... Non, moi, j\'serais nous, je vous... Si moi, j\'étais vous, je vous écouterais ! Non, elle me fait chier, cette phrase !',
    'C’est marrant les petits bouts de fromage par terre. C’est ça que vous appelez une fondue ?',
    'J\'voudrais pas faire ma raclette, mais la soirée s\'annonce pas super.',
    'Quand même, ils sont onze. J\'ai calculé sur les treize dernières années, dans les deux heures qui précèdent le coucher du soleil, vous en êtes à une moyenne de 8,422.',
    'Après demain, à partir d\'aujourd\'hui ?',
    'De toutes façons, les réunions de la Table Ronde c’est deux fois par mois. Donc, si le mec il dit après-demain à partir de dans deux jours, suivant s’il le dit à la fin du mois, ça reporte.',
    'C’qui compte, c’est les valeurs !',
    'Là, vous faites sirop de vingt-et-un et vous dites : beau sirop, mi-sirop, siroté, gagne-sirop, sirop-grelot, passe-montagne, sirop au bon goût.',
    'LEODAGAN CONTRE-ATTAQUE !!!',
    'Et toc ! Remonte ton slibard, Lothard !',
    '13, 14, 15... Enfin tous les chiffres impairs jusqu\'à 22.',
    'A l\'époque quand je le disais, tout le monde oubliait de me le souhaiter. Ça me faisait pleurer. Ça m\'a gonflé, j\'ai arrêté.',
    'Dans la vie, j’avais deux ennemis : le vocabulaire et les épinards. Maintenant j’ai la botte secrète et je bouffe plus d’épinards. Merci, de rien, au revoir messieurs-dames.',
    'Salut, Sire. Je trouve qu’il fait beau, mais encore frais, mais beau !',
    'Lui c\'est Pierce, l\'autre derrière c\'est Pierce aussi, j\'ai jamais compris pourquoi, et lui euh, j\'crois qu\'il a pas d\'prénom, tout le monde l\'appelle Connard...',
    'PAYS DE GALLES INDÉPENDANT ! J\'ai un pivert dans la tête... C\'est normal ?',
    'Karadoc, c\'est le gars brillant. Le frère, à côté, c\'est sûr... C\'est vraiment un gros con.',
    'Ben j\'en ai marre. Ça revient à chaque fois sur le tapis ça.',
    'Là on est partis pour une heure avec des fédérés par-ci des fédérés par-là, j\'vais encore rien biter et ça me gonfle.',
    'Sans blague on pourrait pas fêter la mort des mecs que je connais pour une fois ?',
    'Le Graal, c’est une vraie saloperie, méfiez-vous. Un jour c’est un vase, une semaine après une pierre incandescente. [...] Incandescente, c’est : qui peut accaparer des objets sans resurgir sur autrui.',
    'Non, vous, vous vous maravez. Quand on a pas de technique, il faut y aller à la zob.',
    'SI VOUS VOULEZ QU\'ON SORTE LES PIEDS DEVANT, FAUDRA NOUS PASSER SUR L\'COOOORPS !',
    'Le code c\'est "le code" ? Ça va, ils se sont pas trop cassé le bonnet, pour l\'trouver celui-là !',
    'Y\'a du grabuge alors on appelle les 2 couillons... On met les glandus à profit !',
    'Ça prouve que j\'ai de l\'ubiquité... De l\'humilité ? C\'est pas quand il y a des infiltrations ?',
    'À ROULEEEEETTES !! HOULA... J\'l\'ai un peu trop gueulé ça, non ? À roulettes.',
    'Ah, mais c\'est de là que ça vient ! Quand on dit "ça va comme sur des roulettes". En fait ça veut dire qu\'le mec il peut balancer un morceau de rocher comme une catapulte, il continue quand même d\'avancer d\'façon mobile. ',
    'Une maquette ?! Vous avez pas dit qu\'c\'était une catapulte ?',
    'Ouh làlà! elle va pas me gonfler longtemps, la rouquine !!!',
    'Les 3 actes, c\'est les bonnes femmes qui sont mi-taupes mi-déesses, et qui ont forcé les mecs de Bethléem à construire les pyramides.',
    'Sloubi 1, sloubi 2, sloubi 3, sloubi 4, sloubi 5... ',
    'Je vous ai vu une fois dans une carriole, tirée par un cheval. Enfin, la carriole tirée par un cheval.',
    'Dans le Languedoc, ils m\'appellent Provençal. Mais c\'est moi qui m\'suis gouré en disant mon nom. Sinon, en Bretagne, c\'est le Gros Faisan au sud, et au nord, c\'est juste Ducon ..',
    'Au printemps, j’aime bien pisser du haut des remparts au lever du soleil… Y’a une belle vue !',
    'Ils ont pas de bol, quand même ! Mettre au point un truc pareil et tomber sur des cerveaux comme nous !',
    'Sur une échelle de 2 à 76, et là je préfère prendre large, de 2 à 71 on ne nous écoute pas, de 72 à 75, on nous écoute toujours pas, et seulement à 76 on nous laisse parler sans nous engueuler.',
    'Mais cherchez pas à faire des phrases pourries... On en a gros, c\'est tout !',
    'En plus je connais une technique pour tuer trois hommes en un coup rien qu’avec des feuilles mortes ! Alors là, vous êtes deux, vous avez bien de la chance.',
    'Vous vous prenez pour un enseignant ?... Non j\' s\'entais que c\'était le moment d\'faire une vanne mais y\'a rien qui est sorti.',
    'Bon ça suffit maintenant ! Vous voulez qu\'j\'me foute en rogne comme un enseignant ? ... Qu\'est ce que j\'ai avec ça moi ?',
    'Ah ça y’est, j’viens de comprendre à quoi ça sert la canne. En fait ça sert à rien… Du coup ça nous renvoie à notre propre utilité : l’Homme face à l’Absurde !',
    'C\'est pas moi qu\'explique mal, c\'est les autres qui sont cons !',
    'On va pas installer notre carré germinal à la taverne !',
    'Elle a compris la vilaine frisée ? On a dans l\'projet de fonder un clan autonome pour partir à l\'aventure et ramener du pognon pour entretenir vos grosses miches !! Alors le cageot il dit merci et il ferme sa boîte à caca !!!',
    'Vous, vous avez une idée derrière la main, j\'en mettrais ma tête au feu !',
    'Si on avait bu un coup dans des trucs qui s\'cassent, j\'en aurais pété un par terre avant d\'monter dans ma chambre, pour bien montrer comment j\'suis colère.',
    'Je vais vous poser une série de questions. Vous répondez par oui, non, ou Zbradaraldjan. Ok c\'est parti : où se trouve l\'oiseau ?... Allez c\'est facile ça. Trouve pas ? Bon tant pis. C\'était "sur la branche". Eh oui, y a des pièges.',
    'Si la mémoire est à la tête ce que le passé, peut-on y accéder à six ? Oui, non, Zbradaraldjan ?',
    'Et si je sens que y a des anguilles à la broche, dehors ! Comme César quand il a chassé les marchands du temple, et qu\'ils ont foutu le camp sur le bateau avec les bestioles et l\'pépé.',
    'Je crois que c\'est rentré par là, et c\'est ressorti par là ; et c\'est re-rentré par là, et c\'est RE-RE-SORTI PAR LA. ET NOUS ON S\'SAIGNE AUX QUATRE FROMAGES !!!',
    'Progressif... N\'oubliez pas, dans la casse, le plus important, c\'est les suites d\'épaisseurs ... Bûche de 10, Bûche de 16; Bûche de 32, Bûbûche, Bibuchette, et re-Bûche de 6 !!!',
    'On a une autorité naturelle, il faut en profiter... J\'suis sûr que même à poil on ferait toujours chef !',
    'Votre femme, si j\'avais pas la flemme de descendre de là, elle aurait pris mon pied dans son cul depuis un moment.',
    'Y bouffent que des noisettes et des escalopes de veau. Et quand ils vous donnent un coup de bec vous voyez une grande lumière et ça vous donne la diarrhée !',
    'Ouais en même temps ça vous a prouvé qu\'on avait pas froid au ventre !',
    'Nan mais je l\'ai déjà impressionné, moi ! Je lui ai expliqué une nouvelle technique de combat : on se bat à moitié à mains nues, et à moitié avec du calcium. J\'peux vous dire il faisait moins le malin !',
}

quotes_K = {
    'On construit un barrage, après on lance de la caillasse de l\'autre côté de la rivière pour faire croire aux autres qu\'on a traversé dans l\'autre sens. Une fois qu\'ils sont au milieu, on casse le barrage et on les noie. Ouais... le seul problème c\'est que quand on a passé quatre semaines à construire un barrage, ça fait un peu mal au cul d\'le détruire...',
    'Mais y a rien à développer ! C\'est de la merde, c\'est de la merde, c\'est tout ! Moi, on me sert ça dans une auberge, le tavernier, il s\'prend une quiche dans sa tête !',
    'Ce pain-là, il est cuit trop vite dans un four trop chaud ; la montée n\'a pas le temps de se faire et il y a trop d\'air dans la mie. […] C\'est de la merde.',
    'L\'agneau était daubé du cul !',
    'Eh oui mémé, t\'es bien mouchée!',
    'Par exemple, vous prenez aujourd’hui. Vous comptez sept jours. Ça vous emmène dans une semaine. Et bien on sera exactement le même jour qu’aujourd’hui… À une vache près, hein… C’est pas une science exacte.',
    'Des p\'tits croutons tout vieux genre pour les lapins ? Ouais j\'savais pas c\'que c\'était, dans le doute j\'les ai bouffés.',
    'La politique de l\'autruche, c\'est une politique qui court vite, une politique qui fait des gros œufs, c\'est tout.',
    'Les chicots, c\'est sacré ! Parce que si j\'les lave pas maintenant, dans dix ans, c\'est tout à la soupe. Et l\'mec qui me fera manger de la soupe il est pas né !',
    'Si ça peut m\'éviter de chlinguer du cul, je peux bien me tremper une ou deux fois par an.',
    'Qu’est-ce que c’est que ce style de bouffer des petits machins tout secs et trois gallons de flotte par jour ? […] Si la jeunesse se met à croire à ces conneries, on se dirige tout droit vers une génération de dépressifs ! Le gras, c’est la vie.',
    'Sire ! Enfin vous arrivez pour me sauver. […] De l’hypolipémie ! J’ai plus de gras dans le sang. Je vais me mettre à peler et à perdre mes cheveux…',
    'Ça y est… je vois trouble. C’est le manque de gras, je me dessèche.',
    'Vous nous utilisez bon gré malgré pour arriver sur la fin.',
    'Le Graal par ci, le Graal par là. Le Graal par ci, le Graal par là. Le Graal par ci, le Graal par là. Le Graal par ci, le Graal par là...',
    'Mon frère, il peut pas aller à l\'école. Quand on lui explique un machin technique, il s\'évanouit.',
    'C\'est normal, c\'est en se cassant la gueule qu\'on apprend à marcher. Combien de fois j\'ai failli m\'étouffer avec un os de lapin. Il faut jamais se laisser abattre par un échec, c\'est ça le secret.',
    'Oh le con! Mais il est pas fini d\'affiner!',
    'La neige qui poudroie dans la solitude de notre enfance. Qu\'est ce que vous dites de ça ?',
    'On tombe sur le fric, comme ça, du premier coup ! On s\'est même pas fait un cor au pied !',
    'Cette histoire de Graal, ça a assez traîné ! […] Si c’est pas moi qui prend les choses en main, on y est encore dans cent piges… […] Préparez la fiesta, j’suis un héros !',
    'Parce que d\'un point de vue santé publique, il vaut mieux bouffer ça une fois par mois que de la merde tous les jours. Je vais vous dire, à ce niveau là, c\'est plus de la gastronomie, c\'est de l\'érotisme.',
    'La joie de vivre et le jambon, y\'a pas trente-six recettes du bonheur !',
    'Parce que mon couteau pour le pâté, euuh, y\'a rien à faire, jm\'en tape.',
    'Lorsqu\'on le tient par la partie sporadique, ou boulière, le fenouil est un objet redondant.',
    'Tout à l’heure, on a vu que le chapelet de saucisses n’était pas un objet redondant. Et pourtant, on a pu lui trouver une utilisation périmétrique en s’en servant comme un fouet.',
    'Là, y’a les méduses, les insectes. Là, y’a les glandus, les grouillots. Là, y’a les mecs normaux. Là, y’a les chevaliers. Là, y’a les rois et les princes. Et après, bien au-dessus, y’a le Roi Arthur. Vous, vous aurez eu deux bonhommes dans votre vie, eh ben vous pourrez dire que vous avez tapé dans l’exception.',
    'Allez, faites-vous belle, que j\'me pointe avec la came présentable.',
    'Ma femme… mon ex-femme… C’était peut être un peu moins prestige parce qu’elle est pas reine… mais au moins, elle habitait pas à six heures de marche avec un autre mec.',
    'C\'est pas que c\'est difficile de la récupérer... C\'est que c\'est sa mère difficile de la récupérer, la race de sa grand-mère !',
    'Du passé faisons table en marbre.',
    'Vous dites pas : « Qu’est ce qu\'il fait chaud… », vous dites : « La chaleur est un plat qui se mange froid. »',
    'Les chiffres, c\'est pas une science exacte figurez-vous!Quand je pense à la chance que vous avez de faire partie d\'un clan dirigé par des cerveaux du combat psychologique, qui se saignent...aux quatre parfums du matin au soir !',
    'On va vous envoyer un mec que en fait on dirait qu\'il marche normalement alors qu\'il marche alternativement à cloche pied sur chaque pied alors faites gaffe !'
}

quotes_B = {
    'Ah, Biographie ! (Pet)… Biographie…',
    'Arthour !… Couhillère !',
    'Interprèèète ? Interprèèète, couhillère ?',
    'La fleur en bouquet fane, et jamais ne renaît !',
    'Arthour !… Pas changer assiette pour fromage !',
    'Couhillère, couhillère, couhillère ! Ave Cesar ! (lache une caisse)',
    'MÉTÉOOOOOOOOO !',
    'Troupa ! Troupa ! Troupatroupatroupatroupa ! TROUPA ! HAHAHAHAHAHAHA ! Troupaskaya !',
    'Arthour ! On est fort en pomme.',
    'Arthour ! Qu\'est-ce à dire que ceci ? ON EST FORTS ! En pommes…',
    'Non posso volo, no tépo mayo. Un posso volo, tandolon toulo. Tamasso (pet) tanlamalasso. Tamasso (pet) les oiseaux petits',
    'Les oiseaux sifflent, le printemps siffle !',
    'Arthour, j’apprécie les fruits au sirop !''SALSIFIS !!!!!!',
    'Jouer ! Guerre ! Salsifis !'
}

quotes_C = {
    'Pour savoir s’il va y avoir du vent, il faut mettre son doigt dans le cul du coq.',
    'Ou mettre du beurre dans le fond du plat pour pas que le gratin colle.''Y\'a des méchants ?',
    'J\'te présente vos hommages au roi Arthur.',
    'J\'ai le droit d\'être 4 jours pas chez moi, et après chez moi. Mais y a du voyage qui se prépare, et pour soigner les bêtes, y a pas que ma tante, y a moi aussi.',
    'Pourquoi je peux pas avoir un chien moi ? […] Mais c\'est juste pour mettre des coups de pied dedans ! […] Moi j\'en ai marre de toujours donner des coups de pied aux poules !',
    'À Kadoc ! À Kadoc !''Tatan, elle fait des flans.',
    'Les pattes de canaaaaaaaaaaaaaaaaaaaaaaaaaaaaard !',
    'Elle est où la poulette ?',
    'Mordu, mordu, mooooordu! Mordu mordu mordu mordu mordu mordu mordu mordu mordu mooooooooooordu !!!!',
    'Karadoc il s\'occupe, mais c\'est pas ma Tatan ! !',
    'Il ressemble à Tatan !',
    'Le caca des pigeons c\'est caca, faut pas manger.',
    'Pas du tout, les lapins, les lapins, c\'est gentil !',
    'Le poissooon ! Le petit poissooon !',
    'Des fois on n\'a pas le choix faut sacrifier des jeunes, c\'est le grand qu\'a dit.',
    'Dans trois jours, ma tata elle m’emmène à la mer pour me noyer.',
    'Y vont faire des beignets !',
    'Quand y\'a plus de roi, c\'est caca.',
    'Ça suffit ! Elle est où la poulette ? Elle est bien cachée ?',
    'Vous rendez la poulette sinon c\'est plus vous qui donnez à manger aux lapins !',
    'Ça suffit !!! Ça suffit !!! Ça suffiiiiiiiit !!!',
    'Vous rendez la poulette ou c\'est tout nus dans les orties !',
    'Le caca des canards c\'est caca.',
    'Il est où Kadoc ? Il est bien caché ?',
    'Camouflage caca...',
    'Il faut pas respirer la compote, ça fait tousser.',
    'Caca''Ça suffit, vous rendez la poulette, sinon papi va se mettre en colère.',
    'Si Kadoc il surveille bien, il aura des p\'tits cubes de fromage.',
    'Y sont où les quignons à Kadoc ? Y sont dans la poche? Y sont bien cachés ?'
}


quotes_M = {
    'HAHA, Sire ! Je vous attends ! À moins que vous préfériez que l’on dise partout que le roi est une petite pédale qui pisse dans son froc à l’idée de se battre !',
    'Sire ! Mon père est peut-être unijambiste, mais moi, ma femme n\'a pas de moustache ! […] Alors ça vient? p\'tite bite !',
    'En garde, espèce de vieille pute dégarnie !',
    'JE NE MANGE PAS DE GRAINES !',
    'J\'estime que si on avale l\'équivalent de son poids en viande deux fois par jour, il ne faut pas s\'étonner de ne pas pouvoir mettre un pied devant l\'autre sur un champ de bataille.',
    'Moi, une fois, j\'étais soûl comme cochon, je me suis fait tatouer "J\'aime le raisin de table" sur la miche droite, et ça y est toujours !',
    'Non, je veux dire « malade mental », c\'est votre maximum, comme insulte ? Non parce qu\'il va falloir passer le cran au-dessus, mon vieux, parce que sinon, on y est encore demain !',
    'En garde, ma biquette ! Je vais vous découper le gras du cul, ça vous fera ça de moins à trimbaler !',
    'Quand on est idiot, on plante des carottes on ne s\'occupe pas de sécurité !''Du nerf, mon lapinou !… Vous allez vous faire tailler le zizi en pointe !',
    'ALLEZ, EN GARDE GROSSE CONNE ! Non, ça va pas, ça va pas !',
    'Non mais c\'est à se coincer les parties dans une porte !',
    'Vous savez quoi, Sire ? On va commencer par se faire une saucisse grillée de trois pieds de long, avec un tonnelet de pinard chacun, et derrière, peut être bien qu\'on se paiera des filles. Ah oui ! A un moment, vive la vie !',
    'Mais allez-y bon sang, magnez-vous le fion, espèce de grosse dinde !',
    'Je commence à en avoir ras le bol de votre comportement de péteux alors vous allez me faire le plaisir de me faire une bonne insulte et de vous foutre en rogne une bonne fois pour toutes!',
    'Euh, juste une chose... Manquez encore une seule fois de respect au futur roi de Bretagne, et je vous coupe les boules ! Ca vous fera une jolie petite sacoche pour ranger vos dés à coudre.',
    'Je suis, je suis, je suis une petite tapette, qui parle à tort et à travers, sans que personne ne lui demande son avis, alors elle ferme son bec la poupoule... Et elle laisse parler les grands garçons.',
    'Regardez moi la jolie petite paire de fillettes, si c\'est pas fragile!',
}

