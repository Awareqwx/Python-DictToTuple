def zipTuple(d):
    arr = []
    for i in d:
        arr.append((i, d[i]))

print zipTuple({
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
})