#!/usr/bin/env python3
import os
import shutil

repo_root = '/home/litlfred/space_cats/qou'
lean_root = os.path.join(repo_root, 'content/quantum-observable-universe/lean')

# 1. Move borromean-quark.lean
src_bq = os.path.join(repo_root, 'content/quantum-observable-universe/observations/borromean-quark.lean')
dst_bq = os.path.join(lean_root, 'QOU/Archimedean/BorromeanQuark.lean')
shutil.copyfile(src_bq, dst_bq)

# 2. Move and patch q-integer-mass-formula.lean
src_q = os.path.join(repo_root, 'content/quantum-observable-universe/mass-theory/q-integer-mass-formula.lean')
dst_q = os.path.join(lean_root, 'QOU/Interactions/QIntegerMassFormula.lean')

with open(src_q, 'r') as f:
    content = f.read()

# Remove 'end QOU.Interactions'
content = content.replace('end QOU.Interactions', '')

canonical_instance = """
/-- **Faithful instance.** Carries the conjecture as an explicit sorry. -/
instance canonical : QIntegerMassFormula where
  f_magic := fun _ => 0
  tolerance := 1 / 100
  tolerance_bound := ⟨by norm_num, by norm_num⟩
  fits_AME := sorry

end QOU.Interactions
"""

with open(dst_q, 'w') as f:
    f.write(content + canonical_instance)

# 3. Add to QOU.lean
qou_lean = os.path.join(lean_root, 'QOU.lean')
with open(qou_lean, 'r') as f:
    qou_content = f.read()

if 'import QOU.Archimedean.BorromeanQuark' not in qou_content:
    qou_content += '\nimport QOU.Archimedean.BorromeanQuark\n'

if 'import QOU.Interactions.QIntegerMassFormula' not in qou_content:
    qou_content += 'import QOU.Interactions.QIntegerMassFormula\n'

with open(qou_lean, 'w') as f:
    f.write(qou_content)

print("Files moved and patched successfully.")
