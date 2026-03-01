"""
音乐解析 API - 获取短视频热门音乐
"""
from fastapi import FastAPI

app = FastAPI(title="音乐解析API", version="1.0.0")

@app.get("/")
def root():
    return {"message": "音乐解析API", "endpoints": ["/hot", "/search"]}

@app.get("/hot")
def hot_music():
    """热门音乐列表"""
    return {
        "success": True,
        "music": [
            {"title": "热门歌曲1", "artist": "歌手1", "url": "https://example.com/1.mp3"},
            {"title": "热门歌曲2", "artist": "歌手2", "url": "https://example.com/2.mp3"},
        ]
    }

@app.get("/search")
def search_music(q: str = ""):
    """搜索音乐"""
    return {"success": True, "results": []}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
