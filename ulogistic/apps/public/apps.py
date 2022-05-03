from django.apps import AppConfig

MENU_ITEMS =  [
	{
		"title": "場區狀況",
		"href": "/cntr/container_yard_status",
		"image": "/static/images/import-white.svg",
	},
	{
		"title": "進口查詢",
		"href": "/cntr/import",
		"image": "/static/images/import-white.svg",
	},
	{
		"title": "出口查詢",
		"href": "/cntr/export",
		"image": "/static/images/export-white.svg",
	},
	{
		"title": "拆櫃查詢",
		"href": "/cntr/unpack",
		"image": "/static/images/unpacking-white.svg",
	},
	# {
	# 	"title": "預約提領平台",
	# 	"href": "/user/trksrv/login",
	# 	"image": "/static/images/truck-white.svg",
	# },
]

class PublicConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'public'
