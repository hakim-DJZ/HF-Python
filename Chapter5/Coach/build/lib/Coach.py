def get_coach_data(file):
    try:                   #turn these into a single function.
        with open(file) as fh:
            data = fh.readline()
        return(data.strip().split(','))

    except IOError as ioerr:
        print('File error' + str(ioerr))
        return(None)
