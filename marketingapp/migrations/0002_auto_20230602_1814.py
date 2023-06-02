# Generated by Django 3.2.19 on 2023-06-02 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketingapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name': 'About Us', 'verbose_name_plural': 'About Us'},
        ),
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name': 'Contact Us', 'verbose_name_plural': 'Contact Us'},
        ),
        migrations.AlterModelOptions(
            name='couponcode',
            options={'verbose_name': 'Coupon Code', 'verbose_name_plural': 'Coupon Codes'},
        ),
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name': 'FAQ', 'verbose_name_plural': 'FAQs'},
        ),
        migrations.AlterModelOptions(
            name='newsletter',
            options={'verbose_name': 'Newsletter', 'verbose_name_plural': 'Newsletters'},
        ),
        migrations.AlterModelOptions(
            name='privacypolicy',
            options={'verbose_name': 'Privacy Policy', 'verbose_name_plural': 'Privacy Policies'},
        ),
        migrations.AlterModelOptions(
            name='socialmedia',
            options={'verbose_name': 'Social Media', 'verbose_name_plural': 'Social Media'},
        ),
        migrations.AlterModelOptions(
            name='termsandcondition',
            options={'verbose_name': 'Terms And Condition', 'verbose_name_plural': 'Terms And Conditions'},
        ),
    ]