invoices_file = open("CupcakeInvoices.csv")

for row in invoices_file:
    print(row)

invoices_file.seek(0)

for flavor in invoices_file:
    flavor = flavor.split(',')
    print(flavor[2])

invoices_file.seek(0)

for row in invoices_file:
    values = row.split(',')
    total = int(values[3]) * float(values[4])
    print(round(total, 2))

invoices_file.seek(0)

total = 0

for total_sale in invoices_file:
    values = total_sale.split(',')
    total += int(values[3]) * float(values[4])
    # print(total)
print(round(total, 2))

invoices_file.seek(0)

total_chocolate = 0
total_vanilla = 0
total_strawberry = 0

for cupcake in invoices_file:
    flavor = cupcake.split(',')
    for item in flavor:
        if item == 'Chocolate':
            total_chocolate += 1
        if item == 'Vanilla':
            total_vanilla += 1
        if item == 'Strawberry':
            total_strawberry += 1
            
print("Chocolate:", total_chocolate)
print("Vanilla:", total_vanilla)
print("Strawberry:", total_strawberry)

invoices_file.close()