from django.http.response import HttpResponse
from django.template import loader
from django.utils import timezone
from .models import Post
from .models import Media

import blog

def blog(request):
	posts = Post.objects.all().order_by('-pub_date')
	template = loader.get_template('imogap/imogap.html')
	output = template.render({'posts': posts})
	return HttpResponse(output)

