# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"E212100","system":"readv2"},{"code":"E212200","system":"readv2"},{"code":"E213.12","system":"readv2"},{"code":"E214.11","system":"readv2"},{"code":"E216.13","system":"readv2"},{"code":"E21y600","system":"readv2"},{"code":"E21yz11","system":"readv2"},{"code":"E21z.00","system":"readv2"},{"code":"Eu60013","system":"readv2"},{"code":"Eu60200","system":"readv2"},{"code":"Eu60213","system":"readv2"},{"code":"Eu60713","system":"readv2"},{"code":"Eu60714","system":"readv2"},{"code":"Eu60800","system":"readv2"},{"code":"Eu60y12","system":"readv2"},{"code":"Eu60z11","system":"readv2"},{"code":"Eu60z12","system":"readv2"},{"code":"105029.0","system":"med"},{"code":"1293.0","system":"med"},{"code":"1364.0","system":"med"},{"code":"14747.0","system":"med"},{"code":"15098.0","system":"med"},{"code":"15960.0","system":"med"},{"code":"17420.0","system":"med"},{"code":"18565.0","system":"med"},{"code":"19931.0","system":"med"},{"code":"20033.0","system":"med"},{"code":"2076.0","system":"med"},{"code":"20839.0","system":"med"},{"code":"20881.0","system":"med"},{"code":"21077.0","system":"med"},{"code":"21338.0","system":"med"},{"code":"21665.0","system":"med"},{"code":"21671.0","system":"med"},{"code":"22259.0","system":"med"},{"code":"23597.0","system":"med"},{"code":"23977.0","system":"med"},{"code":"25146.0","system":"med"},{"code":"2729.0","system":"med"},{"code":"27481.0","system":"med"},{"code":"27803.0","system":"med"},{"code":"27945.0","system":"med"},{"code":"28227.0","system":"med"},{"code":"30395.0","system":"med"},{"code":"30603.0","system":"med"},{"code":"31632.0","system":"med"},{"code":"31789.0","system":"med"},{"code":"31819.0","system":"med"},{"code":"32869.0","system":"med"},{"code":"3369.0","system":"med"},{"code":"33741.0","system":"med"},{"code":"34456.0","system":"med"},{"code":"35642.0","system":"med"},{"code":"35763.0","system":"med"},{"code":"36043.0","system":"med"},{"code":"3709.0","system":"med"},{"code":"37289.0","system":"med"},{"code":"38031.0","system":"med"},{"code":"38100.0","system":"med"},{"code":"38371.0","system":"med"},{"code":"39011.0","system":"med"},{"code":"39535.0","system":"med"},{"code":"40057.0","system":"med"},{"code":"40104.0","system":"med"},{"code":"42496.0","system":"med"},{"code":"43690.0","system":"med"},{"code":"44242.0","system":"med"},{"code":"4515.0","system":"med"},{"code":"45188.0","system":"med"},{"code":"4759.0","system":"med"},{"code":"48687.0","system":"med"},{"code":"48796.0","system":"med"},{"code":"49600.0","system":"med"},{"code":"49721.0","system":"med"},{"code":"49779.0","system":"med"},{"code":"50188.0","system":"med"},{"code":"50348.0","system":"med"},{"code":"52465.0","system":"med"},{"code":"53335.0","system":"med"},{"code":"55969.0","system":"med"},{"code":"56502.0","system":"med"},{"code":"5652.0","system":"med"},{"code":"57567.0","system":"med"},{"code":"58693.0","system":"med"},{"code":"59008.0","system":"med"},{"code":"60522.0","system":"med"},{"code":"61969.0","system":"med"},{"code":"6339.0","system":"med"},{"code":"67130.0","system":"med"},{"code":"67590.0","system":"med"},{"code":"68042.0","system":"med"},{"code":"69000.0","system":"med"},{"code":"69185.0","system":"med"},{"code":"70899.0","system":"med"},{"code":"71431.0","system":"med"},{"code":"7745.0","system":"med"},{"code":"792.0","system":"med"},{"code":"8424.0","system":"med"},{"code":"94096.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('personality-disorders-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["personality-disorders---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["personality-disorders---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["personality-disorders---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
