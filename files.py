slip_test = " This is a really long, string with spaces "
slip_result = slip_test.strip().split(',')
for entry in slip_result: 
    print(f' "{entry.strip()}" ')
