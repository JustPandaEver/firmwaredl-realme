#coding:utf-8
#author:PandaEver
#version:1.0.0
#description:realme and oplus ota firmware downloader
#usage:python dl.py <url>
#example:python dl.py https://example.com/file.zip

import urllib.request, os, sys, random, time
try:
    from tqdm import tqdm
except ImportError:
    import pip
    pip.main(['install', 'tqdm'])
    from tqdm import tqdm
os.system('cls') if os.name == 'nt' else os.system('clear')

def download_file(url, filename):
    headers = {'User-Agent': f"Dalvik/2.1.0 (Linux; U; Android {random.randint(12, 14)}; RMX3301 Build/UKQ1.{random.randint(100000, 999999)}.{random.randint(100, 999)})"}
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    total_size = int(response.getheader('Content-Length', 0))
    downloaded_size = os.path.getsize(filename) if os.path.exists(filename) else 0
    if downloaded_size > 0:
        request.add_header('Range', f'bytes={downloaded_size}-')
        response = urllib.request.urlopen(request)
    with open(filename, 'ab') as file:
        with tqdm(total=total_size, initial=downloaded_size, unit='B', unit_scale=True, desc=filename) as bar:
            while True:
                try:
                    chunk = response.read(8192)
                    if not chunk:
                        break
                    file.write(chunk)
                    bar.update(len(chunk))
                except urllib.error.URLError as e:
                    print(f"Network error: {e}. Retrying download...")
                    while True:
                        try:
                            response = urllib.request.urlopen(request)
                            break
                        except urllib.error.URLError:
                            print("Still experiencing network issues. Retrying in 5 seconds...")
                            time.sleep(5)
    print("\nDownload complete!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <url>")
        sys.exit(1)
    url = sys.argv[1]
    filename = os.path.basename(url)
    download_file(url, filename)
