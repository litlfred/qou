with open('docs/coordination/ck-dk-canonical-registry.md', 'r') as f:
    lines = f.readlines()

out = []
in_conflict = False
for line in lines:
    if line.startswith('<<<<<<< HEAD'):
        in_conflict = True
    elif line.startswith('=======') and in_conflict:
        in_conflict = False
    elif line.startswith('>>>>>>>'):
        pass
    else:
        if not in_conflict:
            out.append(line)

with open('docs/coordination/ck-dk-canonical-registry.md', 'w') as f:
    f.writelines(out)
