from django.contrib import admin

# Register your models here.
from .models import Blog
class BlogAdmin(admin.ModelAdmin):
	"""docstring for BlogAdmin"""
	list_display = ('title', 'content','tags_list' )
	search_fields = ('title', ) 
	list_filter = ('title',)
	date_hierarchy = 'publish_date'
	ordering = ('publish_date',) 
	list_display_links = ('title', 'content','tags_list')

	class Meta:
		verbose_name="自定义列表字段"
			
	def tags_list(self, blog):
		"""自定义列表字段"""
		#tag_names = map(lambda x: x.tag_name, blog.tags.all())
		#return ', '.join(tag_names)
		return blog.title+blog.content

admin.site.register(Blog,BlogAdmin)