from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
missing=[]
for i in range(1,81):
    n=f"{i:03d}"
    for p in [ROOT/'p'/n/'index.html', ROOT/'solutions'/f'solution_{n}.svg']:
        if not p.exists(): missing.append(str(p.relative_to(ROOT)))
if missing:
    print('Missing files:')
    print('\n'.join(missing))
    raise SystemExit(1)
print('OK: 80 puzzle pages and 80 SVG solution files are present.')
