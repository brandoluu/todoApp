import uvicorn 



if __name__ == "__main__":
    # run uvicorn server on port 8000
    uvicorn.run("app:api:app", host="0.0.0.0", port=8000, reload=True)
