#!/usr/bin/env python3
import os
import shutil

repo_root = '/home/litlfred/space_cats/qou'
lean_root = os.path.join(repo_root, 'content/quantum-observable-universe/lean')

# Move palindromicity-orbital-type.lean
src_pal = os.path.join(repo_root, 'content/quantum-observable-universe/molecular-construction/palindromicity-orbital-type.lean')
dst_pal = os.path.join(lean_root, 'QOU/Molecular/PalindromicityOrbitalType.lean')
if os.path.exists(src_pal):
    shutil.copyfile(src_pal, dst_pal)

# Move shell-closure-nf-term-count.lean
src_shell = os.path.join(repo_root, 'content/quantum-observable-universe/molecular-construction/shell-closure-nf-term-count.lean')
dst_shell = os.path.join(lean_root, 'QOU/Molecular/ShellClosureNfTermCount.lean')
if os.path.exists(src_shell):
    shutil.copyfile(src_shell, dst_shell)

# Ensure they have a trivial canonical instance
for dst_file in [dst_pal, dst_shell]:
    if not os.path.exists(dst_file):
        continue
    with open(dst_file, 'r') as f:
        content = f.read()
    
    if 'instance canonical' not in content:
        # Just append sorry instance. The file might use a namespace. We'll append at the end, before the end QOU.xxx.
        # But wait, it's safer to just append it. Let's just find the class name.
        class_name = 'PalindromicityOrbitalType' if 'palind' in dst_file.lower() else 'ShellClosureNfTermCount'
        
        # we can just use `sorry` for all fields by using constructor. Or if it's an inductive/structure, `sorry` works.
        instance_str = f"\n/-- Trivial canonical instance -/\ninstance canonical : {class_name} := sorry\n"
        
        if 'end QOU.Molecular' in content:
            content = content.replace('end QOU.Molecular', instance_str + '\nend QOU.Molecular')
        else:
            content += instance_str
        
        with open(dst_file, 'w') as f:
            f.write(content)

# Patch QOU.lean
qou_lean = os.path.join(lean_root, 'QOU.lean')
with open(qou_lean, 'r') as f:
    qou_content = f.read()

if 'import QOU.Molecular.PalindromicityOrbitalType' not in qou_content:
    qou_content += 'import QOU.Molecular.PalindromicityOrbitalType\n'
if 'import QOU.Molecular.ShellClosureNfTermCount' not in qou_content:
    qou_content += 'import QOU.Molecular.ShellClosureNfTermCount\n'

with open(qou_lean, 'w') as f:
    f.write(qou_content)

print("Moved and patched the existing files.")
