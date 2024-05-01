import azure.functions as func
import api.htmx as htmx
import api.table as table

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.function_name(name="about")
@app.route(route="about")
def get_about(req: func.HttpRequest) -> func.HttpResponse:
    return htmx.about_view()


@app.function_name(name="folio")
@app.route(route="folio")
def get_folio(req: func.HttpRequest) -> func.HttpResponse:
    return htmx.folio_view()


@app.function_name(name="resume")
@app.route(route="resume")
def get_resume(req: func.HttpRequest) -> func.HttpResponse:
    return htmx.resume_view()


@app.function_name(name="count")
@app.route(route="count")
def increment_counter(req: func.HttpRequest) -> func.HttpResponse:
    count = table.CounterTable().increment()
    return str(count) + " visitors to this site"


@app.function_name(name="vlog")
@app.route(route="vlog")
def get_vlog(req: func.HttpRequest) -> func.HttpResponse:
    return htmx.vlog_view()


@app.function_name(name="news")
@app.route(route="news")
def get_blog_timeline(req: func.HttpRequest) -> func.HttpResponse:
    return htmx.news_view()


@app.function_name(name="blog")
@app.route(route="blog")
def get_blog(req: func.HttpRequest) -> func.HttpResponse:
    title = req.params.get('title')
    return htmx.blog_view(title)
