import upcean


def create_upca(upc_number):
    barcode = upcean.oopfuncs.barcode('upca', upc_number)
    try:
        if barcode.validate_checksum() == True:
            barcode.validate_create_barcode(upc_number + '-UPCA.png', 3)
            print('[+] BARCODE GENERATED: ' + str(upc_number) + '-UPCA.png')
        else:
            print('[-] CHECKSUM FAILED FOR CODE: ' + str(upc_number))
    except:
        print('[-] CHECKSUM FAILED FOR CODE: ' + str(upc_number))


def create_upce(upc_number):
    barcode = upcean.oopfuncs.barcode('upce', upc_number)
    try:
        if barcode.validate_checksum() == True:
            barcode.validate_create_barcode(upc_number + '-UPCE.png', 3)
            print('[+] BARCODE GENERATED: ' + str(upc_number) + '-UPCEe.png')
        else:
            print('[-] CHECKSUM FAILED FOR CODE: ' + str(upc_number))
    except:
        print('[-] CHECKSUM FAILED FOR CODE: ' + str(upc_number))


# create_upca('300450296092')
# create_upce('300450296092')
# create_upce('01278907')
# create_upca('300870019448')
# create_upce('01278916')
