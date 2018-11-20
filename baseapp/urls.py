from django.urls import path, re_path
from authapp import views as authviews
from authapp import ajax_views as auth_ajax_views
from baseapp import ajax_views as base_ajax_views
from baseapp import views

app_name = 'baseapp'

urlpatterns = [

    re_path(r'^user/accounts/$', authviews.main_create_log_in, name='main_create_log_in'),

    re_path(r'^$', views.home, name='home'),

    re_path(r'^pay/charge/$', views.pay_charge, name='pay_charge'),
    re_path(r'^pay/return/$', views.pay_return, name="pay_return"),
    re_path(r'^pay/cancel/return/$', views.pay_cancel_return, name="pay_cancel_return"),
    re_path(r'^pay/start/$', views.pay_start, name="pay_start"),

    re_path(r'^create/new/$', views.create_new, name="create_new"),
    re_path(r'^create/group/post/(?P<uuid>([0-9a-f]{32}))/$', views.create_group_post, name="create_group_post"),
    re_path(r'^create/solo/post/(?P<uuid>([0-9a-f]{32}))/$', views.create_solo_post, name="create_solo_post"),

    re_path(r'^update/group/post/(?P<uuid>([0-9a-f]{32}))/$', views.update_group_post, name="update_group_post"),
    re_path(r'^update/solo/post/(?P<uuid>([0-9a-f]{32}))/$', views.update_solo_post, name="update_solo_post"),

    re_path(r'^(?P<user_username>([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?))/$',
            views.user_profile, name='user_profile'),
    re_path(r'^solo/(?P<uuid>([0-9a-f]{32}))/$', views.solo_profile, name="solo_profile"),
    re_path(r'^group/(?P<uuid>([0-9a-f]{32}))/$', views.group_profile, name="group_profile"),

    # --------------------------------------------------------------------------------
    re_path(r'^re/create/search/$', base_ajax_views.re_create_search,
            name='re_create_search'),

    re_path(r'^re/create/check/server/time/$', base_ajax_views.re_create_check_server_time,
            name='re_create_check_server_time'),


    re_path(r'^re/create/group/post/$', base_ajax_views.re_create_group_post,
            name='re_create_group_post'),
    re_path(r'^re/create/group/post/complete/$', base_ajax_views.re_create_group_post_complete,
            name='re_create_group_post_complete'),


    re_path(r'^re/create/solo/post/$', base_ajax_views.re_create_solo_post,
            name='re_create_solo_post'),
    re_path(r'^re/create/solo/post/complete/$', base_ajax_views.re_create_solo_post_complete,
            name='re_create_solo_post_complete'),

    re_path(r'^re/update/group/post/$', base_ajax_views.re_update_group_post,
            name='re_create_group_post'),
    re_path(r'^re/update/group/post/complete/$', base_ajax_views.re_update_group_post_complete,
            name='re_create_group_post_complete'),

    re_path(r'^re/update/solo/post/$', base_ajax_views.re_update_solo_post,
            name='re_create_solo_post'),
    re_path(r'^re/update/solo/post/complete/$', base_ajax_views.re_update_solo_post_complete,
            name='re_create_solo_post_complete'),

    re_path(r'^re/profile/post/$', base_ajax_views.re_profile_post,
            name='re_profile_post'),
    re_path(r'^re/post/populate/$', base_ajax_views.re_post_populate,
            name='re_post_populate'),

    re_path(r'^re/comment/add/$', base_ajax_views.re_comment_add,
            name='re_comment_add'),
    re_path(r'^re/comment/delete/$', base_ajax_views.re_comment_delete,
            name='re_comment_delete'),
    re_path(r'^re/comment/more/load/$', base_ajax_views.re_comment_more_load,
            name='re_comment_more_load'),

    re_path(r'^re/post/like/$', base_ajax_views.re_post_like,
            name='re_post_like'),
    re_path(r'^re/post/like/list/$', base_ajax_views.re_post_like_list,
            name='re_post_like_list'),

    re_path(r'^re/follow/add/$', base_ajax_views.re_follow_add,
            name='re_follow_add'),
    re_path(r'^re/following/list/$', base_ajax_views.re_following_list,
            name='re_following_list'),
    re_path(r'^re/follower/list/$', base_ajax_views.re_follower_list,
            name='re_follower_list'),

    # --------------------------------------------------------------------------------

    re_path(r'^b/admin/$', views.b_admin, name='b_admin'),
    re_path(r'^b/admin/solo/$', views.b_admin_solo, name='b_admin_solo'),
    re_path(r'^b/admin/group/$', views.b_admin_group, name='b_admin_group'),
    re_path(r'^b/admin/member/$', views.b_admin_member, name='b_admin_member'),
    re_path(r'^b/admin/group/edit/(?P<uuid>([0-9a-f]{32}))/$', views.b_admin_group_edit, name='b_admin_group_edit'),
    re_path(r'^b/admin/solo/edit/(?P<uuid>([0-9a-f]{32}))/$', views.b_admin_solo_edit, name='b_admin_solo_edit'),
    # --------------------------------------------------------------------------------

    re_path(r'^re/group/register/$', base_ajax_views.re_group_register,
            name='re_group_register'),
    re_path(r'^re/group/list/$', base_ajax_views.re_group_list,
            name='re_group_list'),
    re_path(r'^re/solo/register/$', base_ajax_views.re_solo_register,
            name='re_group_register'),
    re_path(r'^re/solo/list/$', base_ajax_views.re_solo_list,
            name='re_group_list'),

    re_path(r'^re/member/register/$', base_ajax_views.re_member_register,
            name='re_member_register'),


    re_path(r'^re/b/admin/group/delete/$', base_ajax_views.re_b_admin_group_delete,
            name='re_admin_group_delete'),
    re_path(r'^re/b/admin/group/edit/$', base_ajax_views.re_b_admin_group_edit,
            name='re_b_admin_group_edit'),
    re_path(r'^re/b/admin/group/edit/main/name/$', base_ajax_views.re_b_admin_group_edit_main_name,
            name='re_b_admin_group_edit_main_name'),
    re_path(r'^re/b/admin/group/upload/photo/$', base_ajax_views.re_b_admin_group_upload_photo,
            name='re_b_admin_group_upload_photo'),
    re_path(r'^re/b/admin/group/edit/main/photo/register/$', base_ajax_views.re_b_admin_group_edit_main_photo_register,
            name='re_b_admin_group_edit_main_photo_register'),
    re_path(r'^re/b/admin/group/edit/photo/delete/$', base_ajax_views.re_b_admin_group_edit_photo_delete,
            name='re_b_admin_group_edit_photo_delete'),

    re_path(r'^re/b/admin/group/edit/name/delete/$', base_ajax_views.re_b_admin_group_edit_name_delete,
            name='re_b_admin_group_edit_name_delete'),

    re_path(r'^re/b/admin/group/edit/name/register/$', base_ajax_views.re_b_admin_group_edit_name_register,
            name='re_b_admin_group_edit_name_register'),

    re_path(r'^re/b/admin/group/edit/default/register/$', base_ajax_views.re_b_admin_group_edit_default_register,
            name='re_b_admin_group_edit_default_register'),

    # --------------------------------------------------------------------------------

    re_path(r'^re/b/admin/solo/delete/$', base_ajax_views.re_b_admin_solo_delete,
            name='re_admin_solo_delete'),
    re_path(r'^re/b/admin/solo/edit/$', base_ajax_views.re_b_admin_solo_edit,
            name='re_b_admin_solo_edit'),
    re_path(r'^re/b/admin/solo/edit/main/name/$', base_ajax_views.re_b_admin_solo_edit_main_name,
            name='re_b_admin_solo_edit_main_name'),
    re_path(r'^re/b/admin/solo/upload/photo/$', base_ajax_views.re_b_admin_solo_upload_photo,
            name='re_b_admin_solo_upload_photo'),
    re_path(r'^re/b/admin/solo/edit/main/photo/register/$', base_ajax_views.re_b_admin_solo_edit_main_photo_register,
            name='re_b_admin_solo_edit_main_photo_register'),
    re_path(r'^re/b/admin/solo/edit/photo/delete/$', base_ajax_views.re_b_admin_solo_edit_photo_delete,
            name='re_b_admin_solo_edit_photo_delete'),

    re_path(r'^re/b/admin/solo/edit/name/delete/$', base_ajax_views.re_b_admin_solo_edit_name_delete,
            name='re_b_admin_solo_edit_name_delete'),

    re_path(r'^re/b/admin/solo/edit/name/register/$', base_ajax_views.re_b_admin_solo_edit_name_register,
            name='re_b_admin_solo_edit_name_register'),

    re_path(r'^re/b/admin/solo/edit/default/register/$', base_ajax_views.re_b_admin_solo_edit_default_register,
            name='re_b_admin_solo_edit_default_register'),

    # --------------------------------------------------------------------------------

    re_path(r'^create/new/$', views.create_new, name='create_new'),
    re_path(r'^explore/feed/$', views.explore_feed, name='explore_feed'),
    re_path(r'^note/all/$', views.note_all, name='note_all'),

    re_path(r'^post/update/(?P<uuid>([0-9a-f]{32}))/$', views.post_update, name='post_update'),
    re_path(r'^post/(?P<uuid>([0-9a-f]{32}))/$', views.post, name='post'),
    re_path(r'^search/all/$', views.search_all, name='search_all'),
    re_path(r'^search/user/$', views.search_user, name='search_user'),
    re_path(r'^search/post/$', views.search_post, name='search_post'),

    re_path(r'^re_settings/ajax/$', auth_ajax_views.re_settings, name='re_settings'),
    re_path(r'^re_settings/ajax/upload_user_photo/$', auth_ajax_views.upload_user_photo, name='re_upload_user_photo'),
    # re_path(r'^re/create/new/$', base_ajax_views.re_create_new, name='re_create_new'),
    re_path(r'^re/post/update/$', base_ajax_views.re_post_update,
            name='re_post_update'),

    re_path(r'^re/home/feed/$', base_ajax_views.re_home_feed,
            name='re_home_feed'),

    re_path(r'^re/user/home/populate/$', base_ajax_views.re_user_home_populate,
            name='re_user_home_populate'),


    re_path(r'^re/profile/post/delete/$', base_ajax_views.re_profile_post_delete,
            name='re_profile_post_delete'),

    re_path(r'^re/profile/populate/$', base_ajax_views.re_profile_populate,
            name='re_profile_populate'),

    re_path(r'^re/explore/feed/$', base_ajax_views.re_explore_feed,
            name='re_explore_feed'),

    re_path(r'^re/note/all/$', base_ajax_views.re_note_all,
            name='re_note_all'),
    re_path(r'^re/nav/badge/populate/$', base_ajax_views.re_nav_badge_populate,
            name='re_nav_badge_populate'),

    re_path(r'^re/search/all/$', base_ajax_views.re_search_all,
            name='re_search_all'),
    re_path(r'^re/search/user/$', base_ajax_views.re_search_user,
            name='re_search_user'),
    re_path(r'^re/search/post/$', base_ajax_views.re_search_post,
            name='re_search_post'),


    # re_path(r'^email/key/send/$', views.email_key_send, name='email_key_send'),
    # re_path(r'^email/key/confirm/(?P<uid>([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?))/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        # views.email_key_confirm, name='email_key_confirm'),
    # re_path(r'^logout/$', views.log_out, name='log_out'),
    # re_path(r'^username/change/$', views.username_change, name='username_change'),
    # re_path(r'^password/change/$', views.password_change, name='password_change'),
    # re_path(r'^password/reset/$', views.password_reset, name='password_reset'),
    # re_path(r'^email/add/$', views.email_add, name='email_add'),
]
'''
    url(r'^create/$', views.main_create_log_in, name='create'),
'''