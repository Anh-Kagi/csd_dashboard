from django.contrib.auth.models import User, Group
from rest_framework import serializers

from squalaetp.models import Xelon, Corvet
from raspeedi.models import Raspeedi


def products_count():
    labels = ["RT6/RNEG2", "SMEG", "RNEG", "NG4", "DISPLAY", "RTx"]
    prod_nb = []
    rtx_nb = 0
    for prod in labels:
        if prod in ["DISPLAY", "SMEG"]:
            prod_nb.append(Xelon.objects.filter(modele_produit__icontains=prod, date_retour__isnull=False).count())
        elif prod == "RTx":
            for rtx in ["RT3", "RT4", "RT5"]:
                rtx_nb += Xelon.objects.filter(modele_produit=rtx, date_retour__isnull=False).count()
        else:
            prod_nb.append(Xelon.objects.filter(modele_produit=prod, date_retour__isnull=False).count())
    prod_nb.append(rtx_nb)
    labels_nb = sum(prod_nb)
    prod_nb.append(Xelon.objects.filter(date_retour__isnull=False).count() - labels_nb)
    labels.append("AUTRES")
    return labels, prod_nb


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('url', 'name')


class RaspeediSerializer(serializers.ModelSerializer):

    class Meta:
        model = Raspeedi
        fields = ('ref_boitier', 'produit', 'facade', 'type', 'dump_peedi', 'media')


class CorvetSerializer(serializers.ModelSerializer):
    raspeedi = RaspeediSerializer(many=True)

    class Meta:
        model = Corvet
        fields = ('electronique_14l', 'electronique_94l', 'electronique_14x', 'electronique_94x', 'raspeedi')


class ProgSerializer(serializers.ModelSerializer):
    corvet = CorvetSerializer(many=True, read_only=True)

    class Meta:
        model = Xelon
        fields = ('numero_de_dossier', 'vin', 'modele_produit', 'modele_vehicule', 'corvet')