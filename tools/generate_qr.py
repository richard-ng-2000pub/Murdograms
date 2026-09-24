import argparse
from pathlib import Path
try:
    import qrcode
except ImportError:
    raise SystemExit('Install dependency first: pip install "qrcode[pil]"')

parser=argparse.ArgumentParser(description='Generate 80 QR PNG files for puzzle pages.')
parser.add_argument('--base-url', required=True, help='Example: https://answers.example.com')
parser.add_argument('--out', default='qr', help='Output folder')
args=parser.parse_args()
base=args.base_url.rstrip('/')
out=Path(args.out); out.mkdir(parents=True, exist_ok=True)
for i in range(1,81):
    url=f'{base}/p/{i:03d}/'
    img=qrcode.make(url)
    img.save(out/f'qr_{i:03d}.png')
    print(f'{i:03d}: {url}')
print(f'Done. QR files saved to: {out.resolve()}')
