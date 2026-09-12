# 赛事成绩归档

Python 后端起始工程，用于接收带签名的赛段成绩并保存可追溯记录。配置通过环境变量提供，数据文件默认位于 `data/records.db`。请保持 API、校验和存储层分离，运行与验证均在命令行完成。

## 运行

```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
