# Generated by Django 3.2.10 on 2022-01-13 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ballot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cast', models.CharField(choices=[('s', 'in favour'), ('o', 'oppose'), ('a', 'abstain')], default='a', max_length=1, verbose_name='cast')),
                ('worth', models.PositiveIntegerField(default=1, verbose_name='worth')),
            ],
            options={
                'verbose_name': 'ballot',
                'verbose_name_plural': 'ballots',
            },
        ),
        migrations.CreateModel(
            name='Motion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seq', models.PositiveIntegerField(blank=True, null=True, verbose_name='sequence')),
                ('proposition', models.CharField(choices=[('l.c', 'Close the session'), ('l.t', 'Fix a time to resume the session'), ('l.a', 'Adjourn'), ('l.s', 'Recess'), ('l.P', 'Point of privilege'), ('l.A', "Appeal the chair's decision"), ('l.e', 'Amend the approved agenda'), ('l.W', 'Withdraw motion'), ('l.c', 'Enter in camera'), ('l.T', 'Impose a time limit'), ('l.r', 'Read document'), ('l.w', 'Write motion'), ('l.d', 'Divide motion'), ('l.S', 'Suspend the rules'), ('l.v', 'Conduct a secret vote'), ('l.b', 'Table discussion'), ('l.V', 'Immediately vote'), ('l.P', 'Postpone discussion definitely'), ('l.C', 'Refer to a committee'), ('l.p', 'Postpone discussion indefinitely'), ('l.m', 'Sub-amendment'), ('l.M', 'Amendment'), ('l.R', 'Main motion'), ('l.E', 'Reconsideration of a question'), ('l.n', 'Nominate a member for a committee')], max_length=3, verbose_name='proposition')),
                ('preamble', models.TextField(blank=True, verbose_name='preamble')),
                ('operative', models.TextField(verbose_name='operative clauses')),
            ],
            options={
                'verbose_name': 'motion',
                'verbose_name_plural': 'motions',
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret', models.BooleanField(default=False, verbose_name='secret')),
                ('favour', models.PositiveIntegerField(default=0, verbose_name='in favour')),
                ('oppose', models.PositiveIntegerField(default=0, verbose_name='oppose')),
                ('abstain', models.PositiveIntegerField(default=0, verbose_name='abstain')),
                ('passed', models.BooleanField(verbose_name='passed')),
                ('motion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motions.motion', verbose_name='motion')),
            ],
            options={
                'verbose_name': 'vote',
                'verbose_name_plural': 'votes',
            },
        ),
    ]
