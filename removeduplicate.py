

def removeduplicate(namesarray):
  removeduplicate = []
  for name in namesarray:
      if name not in removeduplicate:
          removeduplicate.append(name)
  return removeduplicate



names = ["Alex","John","Mary","Steve","John", "Steve"]
print(removeduplicate(names))
