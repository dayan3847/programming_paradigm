import time

from MediaDownloadSynchronous import MediaDownloadSynchronous
from MediaDownloadMultiprocessing import MediaDownloadMultiprocessing
from MediaDownloadThreading import MediaDownloadThreading


def my_main():
    sites = [
                "https://www.jython.org",
                "https://uady.mx/",
                "https://cujae.edu.cu/",
            ] * 2

    print('Select a option:')
    print('[1] Media Download Multiprocessing')
    print('[2] Media Download Synchronous')
    print('[3] Media Download Threading')
    print('[other] Exit')
    print('')
    option: int = int(input())

    if 1 == option:
        md = MediaDownloadMultiprocessing()
    elif 2 == option:
        md = MediaDownloadSynchronous()
    elif 3 == option:
        md = MediaDownloadThreading()
    else:
        return

    start_time = time.time()
    md.download_all_sites(sites)
    duration = time.time() - start_time

    print('End')
    print(f"Downloaded {len(sites)}")
    print(f"All threads finished successfully in {duration} seconds")


if __name__ == "__main__":
    my_main()
