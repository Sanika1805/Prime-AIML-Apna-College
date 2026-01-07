# key.value pairs
# unique
# unordred
# immutable

info= {
    "name":"sanika",
    "cgpa":"9.54",
    "subjects":["maths","science"],
    3.14:"pi"
}
print(info)

# to acces value
print(info[3.14])

# methods
#d.keys() returns all keys
print(info.keys())

#d.val() returns all values
dict_vals = list(info.values())
print(type (dict_vals)) #returns in form of list

#dic items  returns key value pairs
print(info.items())

#d.get(val)  returns val acc to key
print(info.get("cgpa")) #we use get to give none value in case value doen't exit

#d.update(new_item) add new oitrem to dict
info.update({
    "city":"pune"
})
print(info)