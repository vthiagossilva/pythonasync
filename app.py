import uvicorn


if __name__ == "__main__":
    uvicorn.run("infrastructure.web.server:app", host="127.0.0.1", port=3333, reload=True)
