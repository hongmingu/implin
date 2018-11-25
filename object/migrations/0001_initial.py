# Generated by Django 2.0.5 on 2018-11-01 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import object.disposers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default=None, max_length=1000, null=True)),
                ('description', models.TextField(blank=True, default=None, max_length=2000, null=True)),
                ('uuid', models.CharField(blank=True, default=None, max_length=34, null=True, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GroupMainName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('group', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Group')),
            ],
        ),
        migrations.CreateModel(
            name='GroupMainPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, default=None, max_length=34, null=True, unique=True)),
                ('description', models.TextField(blank=True, default=None, max_length=1000, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('group', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Group')),
            ],
        ),
        migrations.CreateModel(
            name='GroupName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default=None, max_length=1000, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Group')),
            ],
        ),
        migrations.CreateModel(
            name='GroupPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_50', models.ImageField(blank=True, default=None, null=True, upload_to=object.disposers.get_file_path_group_celeb_photo_50)),
                ('file_300', models.ImageField(blank=True, default=None, null=True, upload_to=object.disposers.get_file_path_group_celeb_photo_300)),
                ('uuid', models.CharField(blank=True, default=None, max_length=34, null=True, unique=True)),
                ('description', models.TextField(blank=True, default=None, max_length=1000, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, default=None, max_length=1000, null=True)),
                ('description', models.TextField(blank=True, default=None, max_length=2000, null=True)),
                ('has_another_profile', models.BooleanField(default=False)),
                ('is_open', models.BooleanField(default=True)),
                ('uuid', models.CharField(default=None, max_length=34, null=True, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post_chat_created', models.DateTimeField(default=None, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostChat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('you_say', models.BooleanField(default=True)),
                ('kind', models.PositiveSmallIntegerField(choices=[(1000, 'start'), (4000, 'text'), (5000, 'photo')], default=0)),
                ('uuid', models.CharField(default='38cfcc486afa48ed9bbc02fd743e9063', max_length=34, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('before', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.PostChat')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Post')),
            ],
        ),
        migrations.CreateModel(
            name='PostChatLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post_chat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.PostChat')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostChatLikeCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post_chat', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.PostChat')),
            ],
        ),
        migrations.CreateModel(
            name='PostChatRead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Post')),
                ('post_chat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.PostChat')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostChatRestMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=1000, null=True)),
                ('uuid', models.CharField(default='e54bb1df6883461d83b16ce119db2aaa', max_length=34, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post_chat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.PostChat')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostChatRestMessageCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post_chat', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.PostChat')),
            ],
        ),
        migrations.CreateModel(
            name='PostChatRestMessageLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post_chat_rest_message', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.PostChatRestMessage')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostChatRestMessageLikeCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post_chat_rest_message', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.PostChatRestMessage')),
            ],
        ),
        migrations.CreateModel(
            name='PostChatText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=1000, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post_chat', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.PostChat')),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=1000, null=True)),
                ('uuid', models.CharField(default='502f3362991041b693a273526b4fca0e', max_length=34, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Post')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostCommentCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Post')),
            ],
        ),
        migrations.CreateModel(
            name='PostFirstCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_checked', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Post')),
            ],
        ),
        migrations.CreateModel(
            name='PostFollow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_follow', to='object.Post')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_follow', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostFollowCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Post')),
            ],
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Post')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostLikeCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Solo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default=None, max_length=1000, null=True)),
                ('description', models.TextField(blank=True, default=None, max_length=2000, null=True)),
                ('uuid', models.CharField(blank=True, default=None, max_length=34, null=True, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SoloMainName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('solo', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Solo')),
            ],
        ),
        migrations.CreateModel(
            name='SoloMainPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, default=None, max_length=34, null=True, unique=True)),
                ('description', models.TextField(blank=True, default=None, max_length=1000, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('solo', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Solo')),
            ],
        ),
        migrations.CreateModel(
            name='SoloName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default=None, max_length=1000, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('solo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Solo')),
            ],
        ),
        migrations.CreateModel(
            name='SoloPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_50', models.ImageField(blank=True, default=None, null=True, upload_to=object.disposers.get_file_path_solo_celeb_photo_50)),
                ('file_300', models.ImageField(blank=True, default=None, null=True, upload_to=object.disposers.get_file_path_solo_celeb_photo_300)),
                ('uuid', models.CharField(blank=True, default=None, max_length=34, null=True, unique=True)),
                ('main', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, default=None, max_length=1000, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('solo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Solo')),
            ],
        ),
        migrations.AddField(
            model_name='solomainphoto',
            name='solo_photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.SoloPhoto'),
        ),
        migrations.AddField(
            model_name='solomainname',
            name='solo_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.SoloName'),
        ),
        migrations.AlterUniqueTogether(
            name='solo',
            unique_together={('name', 'description')},
        ),
        migrations.AddField(
            model_name='member',
            name='solo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Solo'),
        ),
        migrations.AddField(
            model_name='groupmainphoto',
            name='group_photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.GroupPhoto'),
        ),
        migrations.AddField(
            model_name='groupmainname',
            name='group_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.GroupName'),
        ),
        migrations.AlterUniqueTogether(
            name='group',
            unique_together={('name', 'description')},
        ),
        migrations.AlterUniqueTogether(
            name='soloname',
            unique_together={('name', 'solo')},
        ),
        migrations.AlterUniqueTogether(
            name='solomainname',
            unique_together={('solo', 'solo_name')},
        ),
        migrations.AlterUniqueTogether(
            name='postlike',
            unique_together={('user', 'post')},
        ),
        migrations.AlterUniqueTogether(
            name='postfollow',
            unique_together={('post', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='postchatrestmessagelike',
            unique_together={('user', 'post_chat_rest_message')},
        ),
        migrations.AlterUniqueTogether(
            name='postchatread',
            unique_together={('user', 'post_chat')},
        ),
        migrations.AlterUniqueTogether(
            name='postchatlike',
            unique_together={('user', 'post_chat')},
        ),
        migrations.AlterUniqueTogether(
            name='member',
            unique_together={('group', 'solo')},
        ),
        migrations.AlterUniqueTogether(
            name='groupname',
            unique_together={('name', 'group')},
        ),
        migrations.AlterUniqueTogether(
            name='groupmainname',
            unique_together={('group', 'group_name')},
        ),
    ]
