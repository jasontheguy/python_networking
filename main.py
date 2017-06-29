import sys,urllib.request
try:
    rfc_num = int(sys.argv[1])
    except(IndexError,ValueError):
        print('Must supply valid RFC number')
        sys.exit(2)
            template = 'http://www.ietf.org/rfc/rfc{}.txt'
            url = template.format(rfc_num)