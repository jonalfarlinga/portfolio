import azure.functions as func
import logging
import htmx

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.function_name(name="about")
@app.route(route="about", auth_level=func.AuthLevel.ANONYMOUS)
def get_about(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    body = htmx.about_view()
    headers = {
        "Access-Control-Allow-Origin": "https://portfolio.denny-bucklin.net"
    }
    response = func.HttpResponse(body=body, status_code=200, headers=headers)
    return response


@app.function_name(name="folio")
@app.route(route="folio", auth_level=func.AuthLevel.ANONYMOUS)
def get_folio(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return htmx.folio_view()


@app.function_name(name="resume")
@app.route(route="resume", auth_level=func.AuthLevel.ANONYMOUS)
def get_resume(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return htmx.resume_view()
