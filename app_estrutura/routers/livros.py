from fastapi import APIRouter

router = APIRouter(
    prefix="/livros",
    tags=["livros"]
)


@router.get("/listar/")
async def listar_livros():
    return {"livros": ["livro1", "livro2", "livro3"]}