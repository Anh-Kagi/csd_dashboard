from django.db import models


class CorvetChoices(models.Model):
    COL_CHOICES = [
        ('DON_LIN_PROD', 'donnee_ligne_de_produit'), ('DON_MAR_COMM', 'donnee_marque_commerciale'),
        ('DON_SIL', 'donnee_silhouette'), ('DON_GEN_PROD', 'donnee_genre_de_produit'),
        ('ATT_DGM', 'COMBINE (CARACTERISTIQUES)'), ('ATT_DHB', 'HAUT PARLEUR'), ('ATT_DHG', 'COMMANDE AUTO-RADIO'),
        ('ATT_DJY', 'SYSTEME NAVIGATION'), ('ATT_DLX', 'AFFICHEUR AV'), ('ATT_DUN', 'AMPLI EQUALISEUR'),
        ('ATT_DYM', 'PRISE AUXILIAIRE PACK AUDIO'), ('ATT_DYR', 'BOITIER TELEMATIQUE'), ('ATT_DAT', 'ANTENNE'),
        ('ATT_DCX', 'COTE CONDUITE/POSTE CONDUITE'), ('DON_MOT', 'MOTEUR'), ('DON_TRA', 'TRANSMISSION'),
        ('ELE_14R', 'AAS HARD - Aide Au Stationnement')
    ]

    key = models.CharField('clé', max_length=10)
    value = models.CharField('valeur', max_length=200)
    column = models.CharField('colonne', max_length=100, choices=COL_CHOICES)

    class Meta:
        verbose_name = "Convertion données CORVET"
        ordering = ['pk']
        constraints = [
            models.UniqueConstraint(fields=['key', 'column'], name='key_column_unique')
        ]

    def __str__(self):
        return f"{self.key} - {self.value} - {self.column}"


class Corvet(models.Model):
    vin = models.CharField('V.I.N.', max_length=17, primary_key=True)
    donnee_date_debut_garantie = models.DateTimeField('Date début garantie', null=True, blank=True)
    donnee_date_entree_montage = models.DateTimeField('Date entrée montage', null=True, blank=True)
    donnee_ligne_de_produit = models.CharField('LIGNE_DE_PRODUIT', max_length=200, blank=True)
    donnee_marque_commerciale = models.CharField('MARQUE_COMMERCIALE', max_length=200, blank=True)
    donnee_silhouette = models.CharField('SILHOUETTE', max_length=200, blank=True)
    donnee_genre_de_produit = models.CharField('GENRE_DE_PRODUIT', max_length=200, blank=True)
    attribut_ddo = models.CharField('KIT TELEPHONE MAIN LIBRE', max_length=200, blank=True)
    attribut_dgm = models.CharField('COMBINE (CARACTERISTIQUES)', max_length=200, blank=True)
    attribut_dhb = models.CharField('HAUT PARLEUR', max_length=200, blank=True)
    attribut_dhg = models.CharField('COMMANDE AUTO-RADIO', max_length=200, blank=True)
    attribut_djq = models.CharField('COMPACT DISQUE', max_length=200, blank=True)
    attribut_djy = models.CharField('SYSTEME NAVIGATION', max_length=200, blank=True)
    attribut_dkx = models.CharField('CARTOGRAPHIE POUR NAVIGATION', max_length=200, blank=True)
    attribut_dlx = models.CharField('AFFICHEUR AV', max_length=200, blank=True)
    attribut_doi = models.CharField('RECEPTION RADIO AMELIOREE', max_length=200, blank=True)
    attribut_dqm = models.CharField('TYPAGE GMP', max_length=200, blank=True)
    attribut_dqs = models.CharField('WIFI', max_length=200, blank=True)
    attribut_drc = models.CharField('RECEPTEUR RADIO', max_length=200, blank=True)
    attribut_drt = models.CharField('REGULATION CLIMAT/TEMPERATURE', max_length=200, blank=True)
    attribut_dti = models.CharField('TUNER RADIO', max_length=200, blank=True)
    attribut_dun = models.CharField('AMPLI EQUALISEUR', max_length=200, blank=True)
    attribut_dwl = models.CharField('PACK RADIO/INFO/COMMUNICATION', max_length=200, blank=True)
    attribut_dwt = models.CharField('PACK PREEQUIP. RADIO/COMMUNIC.', max_length=200, blank=True)
    attribut_dxj = models.CharField('ECRAN VIDEO AR', max_length=200, blank=True)
    attribut_dyb = models.CharField('VISION TETE HAUTE', max_length=200, blank=True)
    attribut_dym = models.CharField('PRISE AUXILIAIRE PACK AUDIO', max_length=200, blank=True)
    attribut_dyr = models.CharField('BOITIER TELEMATIQUE', max_length=200, blank=True)
    attribut_dzv = models.CharField('AIDE A LA CONDUITE', max_length=200, blank=True)
    attribut_gg8 = models.CharField('PAYS PROGRAMME (ICP)', max_length=200, blank=True)
    electronique_14f = models.CharField('RADIO HARD - Recepteur Radio', max_length=200, blank=True)
    electronique_14j = models.CharField('CLIM HARD - Climatisation', max_length=200, blank=True)
    electronique_14k = models.CharField('CMB HARD - Combine Planche de Bord', max_length=200, blank=True)
    electronique_14l = models.CharField('EMF HARD - Ecran Multifonctions', max_length=200, blank=True)
    electronique_14r = models.CharField('AAS HARD - Aide Au Stationnement', max_length=200, blank=True)
    electronique_14x = models.CharField('BTEL HARD - Boitier Telematique (radio telephone)', max_length=200, blank=True)
    electronique_19z = models.CharField('FMUX_HARD - FAÇADE MULTIPLEXÉ', max_length=200, blank=True)
    electronique_44f = models.CharField('RADIO FOURN.NO.SERIE - Recepteur Radio', max_length=200, blank=True)
    electronique_44l = models.CharField('EMF FOURN.NO.SERIE - Ecran Multifonctions', max_length=200, blank=True)
    electronique_44x = models.CharField('BTEL FOURN.NO.SERIE - Boitier Telematique (radio telephone)', max_length=200, blank=True)
    electronique_54f = models.CharField('RADIO FOURN.DATE.FAB - Recepteur Radio', max_length=200, blank=True)
    electronique_54k = models.CharField('CMB FOURN.DATE.FAB - Combine Planche de Bord', max_length=200, blank=True)
    electronique_54l = models.CharField('EMF FOURN.DATE.FAB - Ecran Multifonctions', max_length=200, blank=True)
    electronique_84f = models.CharField('RADIO DOTE - Recepteur Radio', max_length=200, blank=True)
    electronique_84l = models.CharField('EMF DOTE - Ecran Multifonctions', max_length=200, blank=True)
    electronique_84x = models.CharField('BTEL DOTE - Boitier Telematique (radio telephone)', max_length=200, blank=True)
    electronique_94f = models.CharField('RADIO SOFT - Recepteur Radio', max_length=200, blank=True)
    electronique_94l = models.CharField('EMF SOFT - Ecran Multifonctions', max_length=200, blank=True)
    electronique_94x = models.CharField('BTEL SOFT - Boitier Telematique (radio telephone)', max_length=200, blank=True)
    attribut_dat = models.CharField('ANTENNE', max_length=200, blank=True)
    attribut_dcx = models.CharField('COTE CONDUITE/POSTE CONDUITE', max_length=200, blank=True)
    electronique_19h = models.CharField('MDS HARD - Module de service telematique', max_length=200, blank=True)
    electronique_49h = models.CharField('MDS FOURN.NO.SERIE - Module de service telematique', max_length=200, blank=True)
    electronique_64f = models.CharField('RADIO FOURN.CODE - Recepteur Radio', max_length=200, blank=True)
    electronique_64x = models.CharField('BTEL FOURN.CODE - Boitier Telematique (radio telephone)', max_length=200, blank=True)
    electronique_69h = models.CharField('MDS FOURN.CODE - Module de service telematique', max_length=200, blank=True)
    electronique_89h = models.CharField('MDS DOTE - Module de service telematique', max_length=200, blank=True)
    electronique_99h = models.CharField('MDS SOFT - Module de service telematique', max_length=200, blank=True)
    electronique_14a = models.CharField('CMM HARD - Calculateur Moteur Multifonction', max_length=200, blank=True)
    electronique_34a = models.CharField('CMM SOFT LIVRE - Calculateur Moteur Multifonction', max_length=200, blank=True)
    electronique_44a = models.CharField('CMM FOURN.NO.SERIE - Calculateur Moteur Multifonction', max_length=200, blank=True)
    electronique_54a = models.CharField('CMM FOURN.DATE.FAB - Calculateur Moteur Multifonction', max_length=200, blank=True)
    electronique_64a = models.CharField('CMM FOURN.CODE - Calculateur Moteur Multifonction', max_length=200, blank=True)
    electronique_84a = models.CharField('CMM DOTE - Calculateur Moteur Multifonction', max_length=200, blank=True)
    electronique_94a = models.CharField('CMM SOFT - Calculateur Moteur Multifonction', max_length=200, blank=True)
    electronique_p4a = models.CharField('CMM EOBD - Calculateur Moteur Multifonction', max_length=200, blank=True)
    donnee_moteur = models.CharField('MOTEUR', max_length=200, blank=True)
    donnee_transmission = models.CharField('TRANSMISSION', max_length=200, blank=True)
    organes_10 = models.CharField('MOTEUR', max_length=200, blank=True)
    electronique_14b = models.CharField('BSI HARD - Boitier Servitude Intelligent', max_length=200, blank=True)
    organes_20 = models.CharField('BOITE DE VITESSES', max_length=200, blank=True)
    electronique_44b = models.CharField('BSI FOURN.NO.SERIE - Boitier Servitude Intelligent', max_length=200, blank=True)
    electronique_54b = models.CharField('BSI FOURN.DATE.FAB - Boitier Servitude Intelligent', max_length=200, blank=True)
    electronique_64b = models.CharField('BSI FOURN.CODE - Boitier Servitude Intelligent', max_length=200, blank=True)
    electronique_84b = models.CharField('BSI DOTE - Boitier Servitude Intelligent', max_length=200, blank=True)
    electronique_94b = models.CharField('BSI SOFT - Boitier Servitude Intelligent', max_length=200, blank=True)
    electronique_16p = models.CharField('HDC HARD - Haut de Colonne de Direction (COM200x)', max_length=200, blank=True)
    electronique_46p = models.CharField('HDC FOURN.NO.SERIE - Haut de Colonne de Direction (COM200x)', max_length=200, blank=True)
    electronique_56p = models.CharField('HDC FOURN.DATE.FAB - Haut de Colonne de Direction (COM200x)', max_length=200, blank=True)
    electronique_66p = models.CharField('HDC FOURN.CODE - Haut de Colonne de Direction (COM200x)', max_length=200, blank=True)
    electronique_16b = models.CharField('BSM HARD - Boitier Servitude Moteur', max_length=200, blank=True)
    electronique_46b = models.CharField('BSM FOURN.NO.SERIE - Boitier Servitude Moteur', max_length=200, blank=True)
    electronique_56b = models.CharField('BSM FOURN.DATE.FAB - Boitier Servitude Moteur', max_length=200, blank=True)
    electronique_66b = models.CharField('BSM FOURN.CODE - Boitier Servitude Moteur', max_length=200, blank=True)
    electronique_86b = models.CharField('BSM DOTE - Boitier Servitude Moteur', max_length=200, blank=True)
    electronique_96b = models.CharField('BSM SOFT - Boitier Servitude Moteur', max_length=200, blank=True)

    radio = models.ForeignKey('Multimedia', related_name='corvet_radio', on_delete=models.SET_NULL, limit_choices_to={'type': 'RAD'}, null=True, blank=True)
    btel = models.ForeignKey('Multimedia', related_name='corvet_btel', on_delete=models.SET_NULL, limit_choices_to={'type': 'NAV'}, null=True, blank=True)
    bsi = models.ForeignKey('psa.Ecu', related_name='corvet_bsi', on_delete=models.SET_NULL, limit_choices_to={'type': 'BSI'}, null=True, blank=True)
    emf = models.ForeignKey('psa.EmfModel', related_name='corvet_emf', on_delete=models.SET_NULL, null=True, blank=True)
    cmm = models.ForeignKey('psa.Ecu', related_name='corvet_cmm', on_delete=models.SET_NULL, limit_choices_to={'type': 'CMM'}, null=True, blank=True)
    bsm = models.ForeignKey('psa.Ecu', related_name='corvet_bsm', on_delete=models.SET_NULL, limit_choices_to={'type': 'BSM'}, null=True, blank=True)
    # hdc = models.ForeignKey('psa.Ecu', related_name='corvet_hdc', on_delete=models.SET_NULL, limit_choices_to={'type': 'HDC'}, null=True, blank=True)

    class Meta:
        verbose_name = "données CORVET"
        ordering = ['vin']

    def save(self, *args, **kwargs):
        if self.electronique_14x.isdigit():
            self.btel = Multimedia.objects.filter(hw_reference=self.electronique_14x).first()
        if self.electronique_14f.isdigit():
            self.radio = Multimedia.objects.filter(hw_reference=self.electronique_14f).first()
        if self.electronique_14b.isdigit():
            self.bsi = Ecu.objects.filter(comp_ref__startswith=self.electronique_14b, type='BSI').first()
        if self.electronique_14l.isdigit():
            self.emf = EmfModel.objects.filter(hw_reference__startswith=self.electronique_14l).first()
        if self.electronique_14a.isdigit():
            self.cmm = Ecu.objects.filter(comp_ref__startswith=self.electronique_14a, type='CMM').first()
        if self.electronique_16b.isdigit():
            self.bsm = Ecu.objects.filter(comp_ref__startswith=self.electronique_16b, type='BSM').first()
        # if self.electronique_16p.isdigit():
        #     self.hdc = Ecu.objects.filter(comp_ref__startswith=self.electronique_16p, type='HDC').first()
        super(Corvet, self).save(*args, **kwargs)

    def __str__(self):
        return self.vin


class Multimedia(models.Model):
    TYPE_CHOICES = [('RAD', 'Radio'), ('NAV', 'Navigation')]
    MEDIA_CHOICES = [
        ('N/A', 'Vide'),
        ('HDD', 'Disque Dur'), ('EMMC', 'eMMC'), ('external SD', 'Carte SD Externe'),
        ('8Go', 'Carte SD 8Go'), ('16Go', 'Carte SD 16Go'), ('8Go 16Go', 'Carte SD 8 ou 16 Go'),
    ]
    PRODUCT_CHOICES = [
        ('RD3', 'RD3'), ('RD45', 'RD45'), ('RD5', 'RD5'), ('RDE', 'RDE'),
        ('RT3', 'RT3'), ('RT4', 'RT4'), ('RT5', 'RT5'), ('RT6', 'RT6 / RNEG2'), ('RT6v2', 'RT6v2 / RNEG2'),
        ('SMEG', 'SMEG'), ('SMEGP', 'SMEG+ / SMEG+ IV1'), ('SMEGP2', 'SMEG+ IV2'),
        ('NG4', 'NG4'), ('RNEG', 'RNEG'),
        ('NAC1', 'NAC wave1'), ('NAC2', 'NAC wave2'), ('NAC3', 'NAC wave3'), ('NAC4', 'NAC wave4'),
    ]
    LVDS_CON_CHOICES = [(1, '1'), (2, '2')]
    USB_CON_CHOICES = [(1, '1'), (2, '2'), (3, '3')]
    ANT_CON_CHOICES = [(1, '1'), (2, '2'), (3, '3')]

    hw_reference = models.BigIntegerField('référence HW', primary_key=True)
    hw_type = models.CharField('type HW', max_length=10, blank=True)
    label_ref = models.CharField('réf. étiquette', max_length=10, blank=True)
    name = models.CharField('modèle', max_length=20, choices=PRODUCT_CHOICES)
    oe_reference = models.CharField('référence OEM', max_length=200, blank=True)
    supplier_oe = models.CharField("fabriquant", max_length=50, blank=True)
    pr_reference = models.CharField("référence PR", max_length=10, blank=True)
    type = models.CharField('type', max_length=3, choices=TYPE_CHOICES)
    level = models.CharField('niveau', max_length=2, blank=True)
    extra = models.CharField('supplément', max_length=100, blank=True)
    dab = models.BooleanField('DAB', default=False)
    cam = models.BooleanField('caméra de recul', default=False)
    cd_player = models.BooleanField('lecteur CD', default=False)
    jukebox = models.BooleanField('jukebox', null=True)
    carplay = models.BooleanField('CarPlay', null=True)
    media = models.CharField('type de média', max_length=20, choices=MEDIA_CHOICES, blank=True)
    lvds_con = models.IntegerField("nombre d'LVDS", choices=LVDS_CON_CHOICES, null=True, blank=True)
    ant_con = models.IntegerField("Nombre d'antenne", choices=ANT_CON_CHOICES, null=True, blank=True)
    usb_con = models.IntegerField("nombre d'USB", choices=USB_CON_CHOICES,  null=True, blank=True)
    front_pic = models.ImageField(upload_to='psa', blank=True)
    setplate_pic = models.ImageField(upload_to='psa', blank=True)
    rear_pic = models.ImageField(upload_to='psa', blank=True)
    firmware = models.ForeignKey('Firmware', on_delete=models.SET_NULL, limit_choices_to={'is_active': True}, null=True, blank=True)

    class Meta:
        verbose_name = "Données Multimédia"
        ordering = ['hw_reference']

    def save(self, *args, **kwargs):
        super(Multimedia, self).save(*args, **kwargs)
        Corvet.objects.filter(electronique_14x__exact=self.hw_reference).update(btel=self.pk)
        Corvet.objects.filter(electronique_14f__exact=self.hw_reference).update(radio=self.pk)

    def __iter__(self):
        for field in self._meta.fields:
            yield field.verbose_name.capitalize(), field.value_to_string(self)

    def __str__(self):
        return f"{self.hw_reference}_{self.name}_{self.level}_{self.type}"


class Firmware(models.Model):
    ECU_TYPE_CHOICES = [
        ('NAC_EUR_WAVE2', 'NAC_EUR_WAVE2'),
        ('NAC_EUR_WAVE1', 'NAC_EUR_WAVE1'),
        ('NAC_EUR_WAVE3', 'NAC_EUR_WAVE3'),
        ('NAC_EUR_WAVE4', 'NAV_EUR_WAVE4')
    ]

    update_id = models.CharField('SWL(UpdateID)', max_length=18, unique=True)
    version = models.CharField('UpdateVersion', max_length=200)
    type = models.CharField('UpdateType', max_length=100, blank=True)
    version_date = models.DateField('MediaVersionDate', null=True, blank=True)
    ecu_type = models.CharField('EcuType', max_length=50, choices=ECU_TYPE_CHOICES)
    url = models.URLField('lien de téléchargement', max_length=500, blank=True)
    is_active = models.BooleanField('actif', default=False)

    class Meta:
        verbose_name = "Firmwares Télématique"
        ordering = ['-update_id']

    def __str__(self):
        return f"{self.version}_{self.ecu_type}"


class Calibration(models.Model):
    TYPE_CHOICES = [
        ('94B', 'BSI SOFT - Boitier Servitude Intelligent'), ('94A', 'CMM SOFT - Calculateur Moteur Multifonction'),
        ('94F', 'RADIO SOFT - Recepteur Radio'), ('94L', 'EMF SOFT - Ecran Multifonctions'),
        ('94X', 'BTEL SOFT - Boitier Telematique'), ('96B', 'BSM SOFT - Boitier Servitude Moteur'),
        ('99H', 'MDS SOFT - Module de service telematique')
    ]

    factory = models.CharField('version usine', max_length=10, unique=True)
    type = models.CharField('type', max_length=3, choices=TYPE_CHOICES)
    current = models.CharField('version actuelle', max_length=10, blank=True)

    class Meta:
        verbose_name = "Calibration"
        ordering = ['-factory']

    def __str__(self):
        return self.factory


class EmfModel(models.Model):
    hw_reference = models.CharField("référence HW", max_length=10, unique=True)
    name = models.CharField("modèle", max_length=50)
    hw = models.CharField('HW', max_length=10, blank=True)
    sw = models.CharField('SW', max_length=10, blank=True)
    supplier_oe = models.CharField("fabriquant", max_length=50, blank=True)
    pr_reference = models.CharField("référence PR", max_length=10, blank=True)

    class Meta:
        verbose_name = "Données EMF"
        ordering = ['hw_reference']

    def save(self, *args, **kwargs):
        super(EmfModel, self).save(*args, **kwargs)
        Corvet.objects.filter(electronique_14l__startswith=self.hw_reference).update(emf=self.pk)

    def __iter__(self):
        for field in self._meta.fields:
            yield field.verbose_name.capitalize(), field.value_to_string(self)

    def __str__(self):
        return f"{self.hw_reference}_{self.name}"


class Ecu(models.Model):
    TYPE_CHOICES = [
        ('BSI', 'Boitier Servitude Intelligent'), ('EMF', 'Ecran Multifonctions'),
        ('MDS', 'Module de service telematique'), ('CMM', 'Calculateur Moteur Multifonction'),
        ('BSM', 'Boitier Servitude Moteur'), ('HDC', 'Haut de Colonne de Direction (COM200x)')
    ]

    comp_ref = models.CharField("réf. comp. matériel", max_length=10, unique=True)
    mat_ref = models.CharField("réf. matériel", max_length=10, blank=True)
    name = models.CharField("nom du modèle", max_length=50)
    type = models.CharField('type', max_length=3, choices=TYPE_CHOICES)
    first_barcode = models.CharField('premier code-barres', max_length=200, blank=True)
    second_barcode = models.CharField('deuxième code-barres', max_length=200, blank=True)
    hw = models.CharField('HW', max_length=10, blank=True)
    sw = models.CharField('SW', max_length=10, blank=True)
    supplier_oe = models.CharField("fabriquant", max_length=50, blank=True)
    pr_reference = models.CharField("référence PR", max_length=10, blank=True)
    extra = models.CharField('supplément', max_length=100, blank=True)

    class Meta:
        verbose_name = "Données ECU"
        ordering = ['comp_ref']

    def save(self, *args, **kwargs):
        super(Ecu, self).save(*args, **kwargs)
        if self.type == "BSI":
            Corvet.objects.filter(electronique_14b__startswith=self.comp_ref).update(bsi=self.pk)
        # if self.type == "EMF":
        #     Corvet.objects.filter(electronique_14l__startswith=self.comp_ref).update(emf=self.pk)
        if self.type == "MDS":
            Corvet.objects.filter(electronique_19h__startswith=self.comp_ref).update(mds=self.pk)
        if self.type == "CMM":
            Corvet.objects.filter(electronique_14a__startswith=self.comp_ref).update(cmm=self.pk)
        if self.type == "BSM":
            Corvet.objects.filter(electronique_16b__startswith=self.comp_ref).update(bsm=self.pk)
        # if self.type == "HDC":
        #     Corvet.objects.filter(electronique_16p__startswith=self.comp_ref).update(hdc=self.pk)

    def __iter__(self):
        for field in self._meta.fields:
            yield field.verbose_name.capitalize(), field.value_to_string(self)

    def __str__(self):
        return f"{self.comp_ref}_{self.name}"
