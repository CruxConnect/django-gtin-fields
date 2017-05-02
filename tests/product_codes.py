""" Product codes for testing. """

CODES = dict(
    ISBN=dict(
        invalid=[
            '111',  # short
            '12345678901234',  # long
            '0765348275',  # checksum error
            '076534827X',  # bad character
        ],
        valid=[
            '0765348276',  # ISBN10
            '9780765348272',  # ISBN13
        ],
    ),
    UPCA=dict(
        invalid=[
            '04210000526',  # short
            '1042100005219',  # long
            '042100005265',  # checksum error
            '042100X05264',  # bad character
        ],
        valid=[
            '042100005264',
            '042100005219',
            '042100005233',
            '042100005240',
            '042200005263',
            '042500000265',
            '042520000061',
            '042526000058',
            '042526000065',
            '042526000072',
            '042526000089',
            '042526000096',
            '042100005264',
            '042100005219',
            '042100005233',
            '042100005240',
        ],
    ),
    EAN13=dict(
        invalid=[
            '780471117094',  # short
            '14006381333931',  # long
            '9780471117093',  # checksum error
            '978L471117093',  # bad character
        ],
        valid=[
            '9780471117094',
            '4006381333931',
        ],
    ),
    GTIN14=dict(
        invalid=[
            '0123456000018',  # short
            '010123456000015',  # long
            '00123456000016',  # checksum error
            '001234560Y0018',  # bad character
        ],
        valid=[
            '00123456000018',
            '10123456000015',
            '70123456000017',
            '71123456000016',
        ],
    ),
    ASIN=dict(
        invalid=[
            'B06Y125DW',  # short
            'B06Y125DWZZ',  # long
            'B06Y125-WZ',  # bad character
            'B06Y125_WZ',  # bad character
        ],
        valid=[
            'B06Y125DWZ',
            'B01G29XQ30',
            'B000N2HBSO',
            '054792822X',
            '0000000000',
            'ZZZZZZZZZZ',
        ],
    ),
    ASIN_strict=dict(
        invalid=[
            'B06Y125DW',  # short
            'B06Y125DWZZ',  # long
            'B06Y125-WZ',  # bad character
            'B06Y125_WZ',  # bad character
            'ZZZZZZZZZZ',  # doesn't start with 'B'
        ],
        valid=[
            'B06Y125DWZ',
            'B01G29XQ30',
            'B000N2HBSO',
            '054792822X',
            '0000000000',
            'B000000000',
            '000000000X',
        ],
    ),
)
