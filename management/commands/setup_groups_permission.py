from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from users.models import EucUsers

class Command(BaseCommand):
  help = 'Setup groups and permissions'

  def handle(self, *args, **kwargs):
    admins_group, created = Group.objects.get_or_create(name='Admins')
    permissions = Permission.objects.filter(codename__in=['add_user', 'change_user', 'delete_user'])
    admins_group.permissions.add(*permissions)
    
    admin_user = EucUsers.objects.get(username='admin_username')
    admin_user.groups.add(admins_group)
    admin_user.is_staff = True
    admin_user.save()
    
    self.stdout.write(self.style.SUCCESS('Successfully set up groups and permissions'))
