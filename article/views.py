
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Article
from django.urls import reverse_lazy

class ArticleListView(ListView):
	model = Article
	template_name = 'article_list.html'


class ArticleDetailView(LoginRequiredMixin,DetailView):
	model = Article
	template_name = 'article_detail.html'
	login_url = 'login'



class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Article
	fields = ('title', 'body', 'photo')
	template_name = 'article_edit.html'
	login_url = 'login'

	def test_func(self):
		obj=self.get_object()
		return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Article
	template_name = 'article_delete.html'
	success_url = reverse_lazy('article_list')
	login_url = 'login'

	def test_func(self):
		obj=self.get_object()
		return obj.author == self.request.user  # faqatgini login qilgan user foydalanishi mumkin

class ArticleCreateView(LoginRequiredMixin,CreateView):
	model = Article
	template_name = 'article_new.html'
	fields = ('title', 'body', 'photo')
	login_url = 'login'                         # agar login qilmasdan kirmoqchi bo'lsa loginga majburan olib boradi

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)



# class ArticleCreateView(CreateView):
# 	model = Article
# 	template_name = 'article_new.html'
# 	fields = ('title', 'body', 'photo','author')


class ArticleCreateView(CreateView):
	model = Article
	template_name = 'article_new.html'
	fields = ('title', 'body', 'photo')

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)