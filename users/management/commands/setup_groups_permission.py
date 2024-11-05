# from django.core.management.base import BaseCommand
# from django.contrib.auth.models import Group, Permission
# from users.models import EucUsers

# class Command(BaseCommand):
#   help = 'Setup groups and permissions'

#   def handle(self, *args, **kwargs):
#     # Admins group and permissions
#     admins_group, created = Group.objects.get_or_create(name='Admins')
#     admin_permissions = Permission.objects.filter(codename__in=['add_user', 'change_user', 'delete_user'])
#     admins_group.permissions.add(*admin_permissions)
    
#     # Admin user
#     admin_user = EucUsers.objects.get(username='admin_username')
#     admin_user.groups.add(admins_group)
#     admin_user.is_staff = True
#     admin_user.save()

#     # Nurses group and permissions
#     nurses_group, created = Group.objects.get_or_create(name='Nurse')
#     nurse_permissions = Permission.objects.filter(
#       codename__in=[
#         'add_user', 'change_user', 'delete_user', 'view_user',
#         'add_eucstudents', 'change_eucstudents', 'delete_eucstudents', 'view_eucstudents',
#         'add_euchealthclinicinventory', 'change_euchealthclinicinventory', 'delete_euchealthclinicinventory', 'view_euchealthclinicinventory'
#       ]
#     )
#     nurses_group.permissions.add(*nurse_permissions)

#     self.stdout.write(self.style.SUCCESS('Successfully set up groups and permissions for Admins and Nurses'))


from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
  help = 'Setup groups and permissions for `Nurse`'

  def handle(self, *args, **kwargs):
    # Nurses group and permissions
    nurses_group, created = Group.objects.get_or_create(name='Nurse')
    nurse_permissions = Permission.objects.filter(
      codename__in=[
        'add_user', 'change_user', 'delete_user', 'view_user',
        'add_eucstudents', 'change_eucstudents', 'delete_eucstudents', 'view_eucstudents',
        'add_euchealthclinicinventory', 'change_euchealthclinicinventory', 'delete_euchealthclinicinventory', 'view_euchealthclinicinventory',
        'view_group'
      ] 
    )
    nurses_group.permissions.add(*nurse_permissions)

    self.stdout.write(self.style.SUCCESS('Successfully set up groups and permissions for `Nurse`'))
