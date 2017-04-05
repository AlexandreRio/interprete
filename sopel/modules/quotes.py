# -*- coding: utf-8 -*-

from sopel import module

import random


@module.commands('perceval,', 'pq')
def perquote(bot, trigger):
    quote = random.choice(tuple(quotes))
    bot.say(quote)


# needed a one file solution, I'm sorry
# quotes are arranged versions of https://fr.wikiquote.org/wiki/Kaamelott/Perceval
quotes = {
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
