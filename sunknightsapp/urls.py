from django.conf.urls import url,include
from django.contrib.auth.views import logout_then_login


from .views import views
from .views.api import roles,servers,users,user_roles,tournaments,fights,discord_roles,points_submissions,diep_tanks,mastery
from rest_framework_bulk.routes import BulkRouter
from .views.oauth.views import OAuthCallbackDiscord,OAuthRedirectDiscord


router = BulkRouter(trailing_slash=False)
router.register(r'roles',roles.RolesViewSet)
router.register(r'badgeroles',roles.SunKnightsBadgeRoleViewSet)
router.register(r'servers',servers.ServersViewSet)
router.register(r'users',users.ClanUsersViewSet)
router.register(r'usersfast',users.ClanUsersShortSet)
router.register(r'pointsinfo',users.ClanUserPointsInfoViewSet)
router.register(r'userpointssubmission', points_submissions.BasicUserPointSubmissionViewSet)
router.register(r'oneoneonefightssubmission',points_submissions.BasicFightsSubmissionViewSet)
router.register(r'managerpointsaction', points_submissions.PointsManagerActionViewSet)
router.register(r'userroles',user_roles.UserRolesViewSet)
router.register(r'tournaments',tournaments.TournamentsViewSet)
router.register(r'tournamentsfightsconnectors',tournaments.TournamentsFightsConnectorViewSet)
router.register(r'guildfights', fights.GuildFightsViewSet)
router.register(r'discord_roles',discord_roles.DiscordRolesViewSet)
router.register(r'dieptanks',diep_tanks.DiepTanksViewSet)
router.register(r'dieptanksinheritance',diep_tanks.DiepTanksInheritanceViewSet)
router.register(r'mastery',mastery.MasteriesViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/(?P<id>[0-9]+)',views.user),
    url(r'^guilds',views.guilds,name='guilds'),
    url(r'^guilds/(?P<id>[0-9]+)',views.guild),
    url(r'^pointrole/(?P<id>[0-9]+)',views.pointrole),
    url(r'^leaderboard', views.leaderboard, name='leaderboard'),
    url(r'^aboutus', views.about_us, name='about'),
    url(r'^info/$', views.info, name='info'),
    url(r'^info/rules', views.rules, name='rules'),
    url(r'^info/newguide', views.newguide, name='newguide'),
    url(r'^info/pointguide', views.pointguide, name='pointguide'),
    url(r'^info/ranks', views.ranks, name='ranks'),
    url(r'^info/commands', views.commands, name='commands'),
    url(r'^info/faq', views.faq, name='faq'),
    url(r'^info/yt', views.yt, name='yt'),
    url(r'^info/invites', views.invites, name='invites'),
    url(r'^tankdraw', views.tankboard, name='tankboard'),
    url(r'^managesubmissions', views.manage_submissions, name='managesubmissions'),
    url(r'^api/',include(router.urls)),
    url(r'^ajaxhandler/',views.ajaxhandler, name='ajaxhandler'),
    url(r'^logout/$', views.logoutview, name='logout'),

    url(r'^accounts/login/(?P<provider>Discord)/$',
        OAuthRedirectDiscord.as_view(params={'scope': 'identify guilds'})),
    url(r'^accounts/login/(?P<provider>(\w|-)+)/$', OAuthRedirectDiscord.as_view(), name='allaccess-login'),
    url(r'^accounts/callback/(?P<provider>(\w|-)+)/$', OAuthCallbackDiscord.as_view(), name='allaccess-callback'),


]