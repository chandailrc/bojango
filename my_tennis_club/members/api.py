from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/hello")
def hello(request, domain: str):
    return {"message": f"Hello, world from {domain}!"}
