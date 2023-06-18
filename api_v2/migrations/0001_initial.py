# Generated by Django 3.2.19 on 2023-06-18 01:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Armor',
            fields=[
                ('name', models.CharField(help_text='Name of the item.', max_length=100)),
                ('key', models.CharField(help_text='Unique key for the Item.', max_length=100, primary_key=True, serialize=False)),
                ('grants_stealth_disadvantage', models.BooleanField(default=False, help_text='If the armor results in disadvantage on stealth checks.')),
                ('strength_score_required', models.IntegerField(help_text='Strength score required to wear the armor without penalty.', null=True)),
                ('ac_base', models.IntegerField(help_text='Integer representing the armor class without modifiers.')),
                ('ac_add_dexmod', models.BooleanField(default=False, help_text='If the final armor class includes dexterity modifier.')),
                ('ac_cap_dexmod', models.IntegerField(help_text='Integer representing the dexterity modifier cap.', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('name', models.CharField(help_text='Name of the item.', max_length=100)),
                ('desc', models.TextField(help_text='Description of the game content item. Markdown.')),
                ('key', models.CharField(help_text='Unique key for the Document.', max_length=100, primary_key=True, serialize=False)),
                ('author', models.TextField(help_text='Author or authors.')),
                ('published_at', models.DateTimeField(help_text='Date of publication, or null if unknown.')),
                ('permalink', models.URLField(help_text='Link to the document.')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('name', models.CharField(help_text='Name of the item.', max_length=100)),
                ('desc', models.TextField(help_text='Description of the game content item. Markdown.')),
                ('key', models.CharField(help_text='Unique key for the License.', max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('name', models.CharField(help_text='Name of the item.', max_length=100)),
                ('key', models.CharField(help_text='Unique key for the publishing organization.', max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ruleset',
            fields=[
                ('name', models.CharField(help_text='Name of the item.', max_length=100)),
                ('desc', models.TextField(help_text='Description of the game content item. Markdown.')),
                ('key', models.CharField(help_text='Unique key for the ruleset the document was published for.', max_length=100, primary_key=True, serialize=False)),
                ('content_prefix', models.CharField(blank=True, help_text='Short code prepended to content keys.', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('name', models.CharField(help_text='Name of the item.', max_length=100)),
                ('key', models.CharField(help_text='Unique key for the Item.', max_length=100, primary_key=True, serialize=False)),
                ('damage_type', models.CharField(choices=[('bludgeoning', 'bludgeoning'), ('piercing', 'piercing'), ('slashing', 'slashing')], help_text='The damage type dealt by attacks with the weapon.', max_length=100)),
                ('damage_dice', models.CharField(help_text='The damage dice when used making an attack.', max_length=100)),
                ('versatile_dice', models.CharField(default=0, help_text='The damage dice when attacking using versatile.\nA value of 0 means that the weapon does not have the versatile property.', max_length=100)),
                ('range_reach', models.IntegerField(default=5, help_text='The range of the weapon when making a melee attack.', validators=[django.core.validators.MinValueValidator(0)])),
                ('range_normal', models.IntegerField(default=0, help_text='The normal range of a ranged weapon attack.\nA value of 0 means that the weapon cannot be used for a ranged attack.', validators=[django.core.validators.MinValueValidator(0)])),
                ('range_long', models.IntegerField(default=0, help_text='The long range of a ranged weapon attack.\nA value of 0 means that the weapon cannot be used for a long ranged attack.', validators=[django.core.validators.MinValueValidator(0)])),
                ('is_finesse', models.BooleanField(default=False, help_text='If the weapon is finesse.')),
                ('is_thrown', models.BooleanField(default=False, help_text='If the weapon is thrown.')),
                ('is_two_handed', models.BooleanField(default=False, help_text='If the weapon is two-handed.')),
                ('requires_ammunition', models.BooleanField(default=False, help_text='If the weapon requires ammunition.')),
                ('requires_loading', models.BooleanField(default=False, help_text='If the weapon requires loading.')),
                ('is_heavy', models.BooleanField(default=False, help_text='If the weapon is heavy.')),
                ('is_light', models.BooleanField(default=False, help_text='If the weapon is light.')),
                ('is_lance', models.BooleanField(default=False, help_text='If the weapon is a lance.')),
                ('is_net', models.BooleanField(default=False, help_text='If the weapon is a net.')),
                ('is_simple', models.BooleanField(default=False, help_text='If the weapon category is simple.')),
                ('is_improvised', models.BooleanField(default=False, help_text='If the weapon is improvised.')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v2.document')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MagicItemType',
            fields=[
                ('name', models.CharField(help_text='Name of the item.', max_length=100)),
                ('key', models.CharField(help_text='Unique key for the Item.', max_length=100, primary_key=True, serialize=False)),
                ('requires_attunement', models.BooleanField(default=False, help_text='If the item requires attunement.')),
                ('rarity', models.IntegerField(choices=[(1, 'common'), (2, 'uncommon'), (3, 'rare'), (4, 'very rare'), (5, 'legendary')], help_text='Integer representing the rarity of the object.', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v2.document')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('name', models.CharField(help_text='Name of the item.', max_length=100)),
                ('desc', models.TextField(help_text='Description of the game content item. Markdown.')),
                ('size', models.IntegerField(choices=[(1, 'Tiny'), (2, 'Small'), (3, 'Medium'), (4, 'Large'), (5, 'Huge'), (6, 'Gargantuan')], default=1, help_text='Integer representing the size of the object.', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)])),
                ('weight', models.DecimalField(decimal_places=3, default=0, help_text='Number representing the weight of the object.', max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('armor_class', models.IntegerField(default=0, help_text='Integer representing the armor class of the object.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('hit_points', models.IntegerField(default=0, help_text='Integer representing the hit points of the object.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)])),
                ('key', models.CharField(help_text='Unique key for the Item.', max_length=100, primary_key=True, serialize=False)),
                ('cost', models.DecimalField(decimal_places=2, default=None, help_text='Number representing the cost of the object.', max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('armor', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='api_v2.armor')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v2.document')),
                ('magic_item_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='api_v2.magicitemtype')),
                ('weapon', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='api_v2.weapon')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='document',
            name='license',
            field=models.ForeignKey(help_text='License that the content was released under.', on_delete=django.db.models.deletion.CASCADE, to='api_v2.license'),
        ),
        migrations.AddField(
            model_name='document',
            name='publisher',
            field=models.ForeignKey(help_text='Publisher which has written the game content document.', on_delete=django.db.models.deletion.CASCADE, to='api_v2.publisher'),
        ),
        migrations.AddField(
            model_name='document',
            name='ruleset',
            field=models.ForeignKey(help_text="The document's game system that it was published for.", on_delete=django.db.models.deletion.CASCADE, to='api_v2.ruleset'),
        ),
        migrations.AddField(
            model_name='armor',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v2.document'),
        ),
    ]
