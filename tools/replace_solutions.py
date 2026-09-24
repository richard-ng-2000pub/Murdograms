import argparse, shutil
from pathlib import Path
parser=argparse.ArgumentParser(description='Copy 001.svg ... 080.svg into the repository solution folder.')
parser.add_argument('source', help='Folder containing 001.svg ... 080.svg')
args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
src=Path(args.source)
dst=root/'solutions'; dst.mkdir(exist_ok=True)
missing=[]
for i in range(1,81):
    n=f'{i:03d}'
    f=src/f'{n}.svg'
    if not f.exists(): missing.append(f.name); continue
    shutil.copy2(f, dst/f'solution_{n}.svg')
if missing:
    print('Missing:', ', '.join(missing))
    raise SystemExit(1)
print('Done: copied all 80 SVG files.')
