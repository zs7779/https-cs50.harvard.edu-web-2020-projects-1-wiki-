from django.shortcuts import render, redirect, reverse
from markdown2 import Markdown

from . import util, forms


markdowner = Markdown()


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wiki(request, title):
    entry = util.get_entry(title)
    article = markdowner.convert(entry) if entry else None
    md_content = "\n".join(entry.split("\n")[2:]) if entry else None
    return render(request, "encyclopedia/article.html", {
        "title": title,
        "article": article,
        "article_form": forms.ArticleForm(initial={
            "article_title": title,
            "article_content": md_content})
    })


def new(request, title=""):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html", {
            "article_form": forms.ArticleForm(initial={"article_title": title})
        })

    elif request.method == "POST":
        article_form = forms.ArticleForm(request.POST or None)
        if article_form.is_valid():
            article = {'title': article_form.cleaned_data["article_title"],
                       'content': article_form.cleaned_data["article_content"]}
            article['content'] = f"# {article['title']}\n\n{article['content']}"
            util.save_entry(article['title'],  article['content'])
            return redirect(reverse("encyclopedia:wiki", kwargs={"title": article['title']}))
        else:
            return render(request, "encyclopedia/new.html", {
                "article_form": article_form,
            })


def search(request):
    form = forms.SearchForm(request.GET or None)
    results = None
    num_results = 0
    if form.is_valid():
        query = form.cleaned_data['search_query']
        results = [entry for entry in util.list_entries() if query.lower() in entry.lower()]
        num_results = len(results)
    return render(request, "encyclopedia/search.html", {
        "query": query,
        "entries": results,
        "num_results": num_results
    })
