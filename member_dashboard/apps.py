from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'member_dashboard'
    admin_site_name = 'member_admin'
    anonymous_listboard_url_name = 'member_dashboard:anonymous_listboard_url'
    base_template_name = 'edc_base/base.html'
    listboard_template_name = 'member_dashboard/listboard.html'
    dashboard_url_name = 'member_dashboard:listboard_url'
    listboard_url_name = 'member_dashboard:listboard_url'
    url_namespace = 'member_dashboard'
