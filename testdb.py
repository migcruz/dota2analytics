import os
import json
from collections import OrderedDict

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings.devl")
import django
django.setup()


from heroes.models import Hero, Ability



######## Heroes ######
# heros = Hero.objects.all()
# print type(heros)
# for hero in heros:
#     print hero

# with open('drf_heroes.json') as filepath:
#  	heroes_json = json.load(filepath, object_pairs_hook=OrderedDict)

# for key, val in heroes_json.iteritems():
#     p = Hero.objects.create(
#         hero_id = val["id"],
#         name = val["name"],
#         localized_name = val["localized_name"],
#         primary_attr = val["primary_attr"],
#         attack_type = val["attack_type"],
#         roles = val["roles"],
#         webm = val["webm"],
#         img = val["img"],
#         icon = val["icon"],
#         url = val["url"],
#         base_health = val["base_health"],
#         base_health_regen = val["base_health_regen"],
#         base_mana = val["base_mana"],
#         base_mana_regen = val["base_mana_regen"],
#         base_armor = val["base_armor"],
#         base_mr = val["base_mr"],
#         base_attack_min = val["base_attack_min"],
#         base_attack_max = val["base_attack_max"],
#         base_str = val["base_str"],
#         base_agi = val["base_agi"],
#         base_int = val["base_int"],
#         str_gain = val["str_gain"],
#         agi_gain = val["agi_gain"],
#         int_gain = val["int_gain"],
#         attack_range = val["attack_range"],
#         projectile_speed = val["projectile_speed"],
#         attack_rate = val["attack_rate"],
#         move_speed = val["move_speed"],
#         turn_rate = val["turn_rate"],
#         cm_enabled = val["cm_enabled"],
#         legs = val["legs"],
#         complexity = val["complexity"]
#     )


# heroes = Hero.objects.all().delete()
# heros = Hero.objects.all()
# print heros, len(heros)


######## Abilities ######
x = 0
with open('drf_hero_abilities.json') as filepath:
 	drf_hero_abilities = json.load(filepath, object_pairs_hook=OrderedDict)

heros = Hero.objects.all()
for hero in heros:
    for key, val in drf_hero_abilities.iteritems():
        if hero.hero_id == val["hero_id"]:
            p = Ability.objects.create(
                created_order = x,
                hero = hero,
                ability_name = val["ability_name"],
                heroid = val["hero_id"],
                ability_info = val["ability_info"]
            )
            x += 1

# abilities = Ability.objects.all()
# print abilities[0].ability_info

# abilities = Ability.objects.all().delete()





# if __name__ == '__main__':    
#     # # e.g. add a new location
#     # l = Location()
#     # l.name = 'Berlin'
#     # l.save()

#     # this is an example to access your model
#     users = EmailUser.objects.all()
#     print users

#     # # e.g. delete the location
#     # berlin = Location.objects.filter(name='Berlin')
#     # print berlin
#     # berlin.delete()