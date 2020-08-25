# -*- coding: utf-8 -*-

jobwords = [
        'nan',
        'temps plein', 'temps complet', 'mi temps', 'temps partiel', # Part / Full time
        'cherche', # look for
        'urgent','rapidement', 'futur', 
        'job', 'offre', # Job offer
        'trice', 'ère', 'eur', 'euse', 're', 'se', 'ème', 'trices', # Female endings
        'ères', 'eurs', 'euses', 'res', 'fe', 'fes',# Female endings
        've', 'ne', 'iere', 'rice', 'te', 'er', 'ice',
        'ves', 'nes', 'ieres', 'rices', "tes", 'ices', # Female endings
        'hf', 'fh', # Male/Female, Female/Male
        'semaine', 'semaines', 'sem', 
        'h', 'heure', 'heures', 'hebdo', 'hebdomadaire', # Time (week, hour)
        'année', 'mois', 'an', # Year
        'jour', 'jours', # Day
        'été', 'automne', 'hiver', 'printemps', # summer, winter ...
        'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche', # Week day
        'janvier', 'février', 'mars', 'avril', 'mai', 'juin', # Month
        'juillet', 'aout', 'septembre', 'octobre', 'novembre', 'décembre', 
        
        "deux", "trois", "quatre", "cinq", "six", "sept", # Number
        "huit", "neuf", "dix", "onze", # Number
        "euros", "euro", "dollars", "dollar", # Money
        
        "super", # Pour éviter "super poids lourd"
        # To clean
        'caces', 'cap', 'bts', 'dea', 'diplôme', 'bac',
        
        "taf", "ref", "poste", "pourvoir", "sein", "profil",
        "possible",
        
        'indépendant',
        'saisonnier', 'alternance', 'alternant', 'apprenti', 
        'apprentissage', 'stagiaire', 'étudiant', 'fonctionnaire', 
        'intermittent', 'élève', 'freelance', "professionnalisation",
        
        'partiel', 'cdd', 'cdi', 'contrat', 'pro',
        
        "fpe", # Fonction publique d'état
        
        
        
        'débutant', 'expérimenté', 'junior', 'senior',
        'confirmé', 'catégorie',
        
        'trilingue', 'bilingue', 
        'bi','international', 'france', 'national', 'régional',
        'européen',  'emploi', 'non',
        'exclusif', 'uniquement',

        'permis', 'ssiap', 'bnssa',
        
        ]

job_replace_infirst = {
    '3 d' : 'troisd',
    '3d':'troisd',
    '2 d': 'deuxd',
    '2d':'deuxd',
    'b to b': 'btob'
    }

job_lemmas_expr = {
    'cours particulier' : 'professeur',
    'call center' : 'centre appels',
    'vl pl vu' : 'poids lourd',
    'front end' : 'informatique',
    'back end' : 'informatique',
    'homme femme' : '',
    'femme homme' : ''
    }

job_normalize_map = [
    ("indu", "industriel"),
    ("pl","poids lourd"),
    ("spl","poids lourd"),
    ("sav","service après vente"),
    ("unix","informatique"),
    ("windows","informatique"),
    ("php","informatique"),
    ("java","informatique"),
    ("python","informatique"),
    ("jee","informatique"),
    ("sap","informatique"),
    ("abap","informatique"),
    ("ntic","informatique"),
    # ("c","informatique"),
    ("rh","ressources humaines"),
    ("vrd","voirie réseaux divers"),
    ("super poids lourd","poids lourd"),
    ("adv","administration des ventes"),
    ("cvv","chauffage climatisation"),
    ("agt","agent"),
    ("ash","agent des services hospitaliers"),
    ("ibode","infirmier de bloc opératoire"),
    ("aes","accompagnant éducatif et social"),
    ("ads","agent de sécurité"),
    ("amp","aide médico psychologique"),
    ("asvp","agent de surveillance des voies publiques"),
    ("cesf","conseiller en économie sociale et familiale"),
    ("babysitter","baby sitter"),
    ("babysitting","baby sitter"),
    ("sitting","sitter"),
    ("nounou", "nourrice"),
    ("coaching","coach"),
    ("webdesigner","web designer"),
    ("webmarketer","web marketer"),
    ("helpdesk","help desk"),
    ("prof","professeur"),
    ("maths", "mathématiques"),
    ("géo", "géographie"),
    ("philo", "philosophie"),
    ("epr","employe polyvalent de restauration"),
    ("NTIC","Informatique"),
    ("SIG","Systèmes d Information Géographique "),
    ("EPSCP","établissement public à caractère scientifique, culturel et professionnel "),
    ("NRBC","Nucléaire, Radiologique, Bactériologique, Chimique "),
    ("SAV","Service après vente"),
    ("ACIM ","Agent des Cabinets en Imagerie Médicale "),
    ("ASC","Agent des Services Commerciaux"),
    ("AEC","Agent d Escale Commerciale"),
    ("ASEM","Agent spécialisé des écoles maternelles "),
    ("TIC","Informatique"),
    ("HSE","Hygiène Sécurité Environnement "),
    ("ATER","Attaché temporaire d enseignement et de recherche "),
    ("AVS","Auxiliaire de Vie Sociale "),
    ("AIS","Auxiliaire d Intégration Scolaire"),
    ("ASV","Auxiliaire Spécialisé Vétérinaire "),
    ("AVQ","Auxiliaire Vétérinaire Qualifié"),
    ("IARD","Incendie, Accidents, Risques Divers "),
    ("NBC","Nucléaire, Bactériologique et Chimique"),
    ("PGC","Produits de Grande Consommation "),
    ("PNT","Personnel Navigant Technique "),
    ("PAO","Publication Assistée par Ordinateur"),
    ("TTA","toute arme"),
    ("VRD","Voiries et Réseaux Divers"),
    ("CMS","Composants Montés en Surface "),
    ("VSL","Véhicule Sanitaire Léger"),
    ("CIP","Conseiller d Insertion et de Probation "),
    ("CND","Contrôle Non Destructif "),
    ("MOA","Maîtrise d Ouvrage"),
    ("OPC","Ordonnancement, Pilotage et Coordination de chantier"),
    ("SPS","Sécurité, Protection de la Santé "),
    ("DAF","Directeur administratif et financier"),
    ("CHU","Centre Hospitalier Universitaire "),
    ("GSB","Grande Surface de Bricolage "),
    ("GSS","Grande Surface Spécialisée "),
    ("DOSI","Directeur de l Organisation et des Systèmes d Information "),
    ("ESAT","entreprise ou de Service d Aide par le Travail "),
    ("DRH","Directeur des Ressources Humaines "),
    ("DSI","Directeur des services informatiques "),
    ("DSPIP","Directeur des services pénitentiaires d insertion et de probation "),
    ("EPA","Etablissement Public à caractère Administratif "),
    ("EPST","Etablissement Public à caractère Scientifique et Technologique "),
    ("EPCC","Etablissement Public de Coopération Culturelle "),
    ("EPIC","Etablissement Public et Commercial "),
    ("IFSI","Institut de formation en soins infirmiers"),
    ("MAS","Machines à Sous "),
    ("SCOP","Société Coopérative Ouvrière de Production"),
    (" EVS","Employée du Service Après Vente "),
    ("EVAT","Engagée Volontaire de l Armée de Terre "),
    ("EV","Engagé Volontaire "),
    ("GIR","Groupement d Individuels Regroupés "),
    ("CN","Commande Numérique "),
    ("SICAV","Société d Investissement à Capital Variable "),
    ("OPCMV","Organisme de Placement Collectif en Valeurs Mobilières "),
    ("OPCVM","Organisme de Placement Collectif en Valeurs Mobilières "),
    ("IADE","Infirmier Anesthésiste Diplômé d Etat "),
    ("IBODE","Infirmier de bloc opératoire Diplômé d Etat "),
    ("CTC","contrôle technique de construction "),
    ("IGREF","Ingénieur du génie rural des eaux et forêts "),
    ("IAA","Inspecteur d académie adjoint"),
    ("DSDEN","directeur des services départementaux de l Education nationale "),
    ("IEN","Inspecteur de l Education Nationale "),
    ("IET","Inspecteur de l enseignement technique "),
    ("ISPV","Inspecteur de Santé Publique Vétérinaire "),
    ("IDEN","Inspecteur départemental  de l Education nationale "),
    ("IIO","Inspecteur d information et d orientation "),
    ("IGEN","Inspecteur général de l Education nationale "),
    ("IPR","Inspecteur pédagogique régional"),
    ("IPET","Inspecteur principal de l enseignement technique "),
    ("PNC","Personnel Navigant Commercial "),
    ("MPR","Magasin de Pièces de Rechange "),
    ("CME","Cellule, Moteur, Electricité "),
    ("BTP","Bâtiments et Travaux Publics "),
    ("EIR","Electricité, Instrument de bord, Radio "),
    ("MAR","Médecin Anesthésiste Réanimateur "),
    ("PMI","Protection Maternelle et Infantile "),
    ("MISP","Médecin Inspecteur de Santé Publique "),
    ("MIRTMO","Médecin Inspecteur Régional du Travail et de la Main d oeuvre "),
    ("DIM","Documentation et de l Information Médicale"),
    ("OPL","Officier pilote de ligne "),
    ("CN","commande numérique "),
    ("PPM","Patron Plaisance Moteur "),
    ("PPV","Patron Plaisance Moteur "),
    ("PhISP","Pharmacien Inspecteur de Santé Publique "),
    ("PDG","Président Directeur Général "),
    ("FLE","Français Langue Etrangère "),
    ("PLP","Professeur de lycée professionnel "),
    ("EPS","éducation physique et sportive "),
    ("PEGL","Professeur d enseignement général de lycée "),
    ("PEGC","Professeur d enseignement général des collèges "),
    ("INJS","instituts nationaux de jeunes sourds "),
    ("INJA","instituts nationaux de jeunes aveugles "),
    ("TZR","titulaire en zone de remplacement "),
    ("CFAO","Conception de Fabrication Assistée par Ordinateur "),
    ("SPIP","service pénitentiaire d insertion et de probation "),
    ("PME","Petite ou Moyenne Entreprise "),
    ("RRH","Responsable des Ressources Humaines "),
    ("QSE","Qualité Sécurité Environnement "),
    ("SASU","Secrétaire d administration scolaire et universitaire "),
    ("MAG","Metal Active Gas "),
    ("MIG","Metal Inert Gas "),
    ("TIG","Tungsten Inert Gas "),
    ("GED","Gestion électronique de documents"),
    ("CVM","Circulations Verticales Mécanisées "),
    ("TISF","Technicien Intervention Sociale et Familiale"),
    ("MAO","Musique Assistée par Ordinateur"),
    # ("Paie","paye"),
    # ("paies","paye"),
    ("ml","mission locale"),
    ("AS","aide soignant"),
    ("IDE","infirmier de soins généraux"),
    ("ERD","études recherche et développement")
    ]
