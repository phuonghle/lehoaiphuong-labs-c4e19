import pyexcel

a_list_of_dictionaries = [
{
    "name": "Phuong",
    "age": "25"
}
    ]

pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name="pyexcel_sample.xlsx")