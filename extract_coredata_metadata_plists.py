from __future__ import print_function


def extract_coredata_metadata_plists(db, plist_prefix):
    zmeta = db.get_table('Z_METADATA')
    for x in zmeta.all():
        version = str(x['Z_VERSION'])
        uuid = str(x['Z_UUID'])
        plist_name = '.'.join([plist_prefix, version, uuid, 'plist'])
        print(plist_name)
        with open(plist_name, 'bw') as out:
            out.write(x['Z_PLIST'])


def main(path_to_sqlite_file):
    import os
    import dataset

    db_file_name = str(path_to_sqlite_file)
    if not os.path.isfile(db_file_name):
        raise FileNotFoundError(db_file_name)
    db = dataset.connect('sqlite:///'+db_file_name)
    extract_coredata_metadata_plists(db, db_file_name)
    return 0


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print('Usage: ' + __file__ + ' sqlitefile', file=sys.stderr)
        sys.exit(1)
    sys.exit(main(sys.argv[1]))
