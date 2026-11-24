import os
from pathlib import Path
out=Path(os.environ['MAKEFUN_OUTPUT_DIR'])
out.mkdir(parents=True,exist_ok=True)
out.joinpath('entry.txt').write_text("fix: restored prod after teaching the cache to serve yesterday's 500s; root cause was my confident assumption that TTL meant 'time to live'",encoding='utf-8')
