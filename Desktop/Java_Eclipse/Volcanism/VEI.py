import csv

with open('GVP_Volcano_List.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    with open('new_GVP.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')
        
        for line in csv_reader:
            print(line)
        
        
    
   