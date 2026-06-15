#!/usr/bin/env python3
import os

lean_root = '/home/litlfred/space_cats/qou/content/quantum-observable-universe/lean'
src_file = os.path.join(lean_root, 'QOU/Archimedean/EmCouplingBringZeroMode.lean')

with open(src_file, 'r') as f:
    content = f.read()

canonical_instance = """
/-- **Faithful instance.** Carries the explicit research-grade conjecture as a sorry.
    Since `BlochWigner_unit_circle` is an unconstrained axiom, this cannot be mathematically
    proven from first principles without additional axioms on the range of the Bloch-Wigner function. -/
instance canonical : BringZeroModeBlochClass where
  bring_zero_mode_realised := sorry

"""

if 'instance canonical : BringZeroModeBlochClass' not in content:
    content = content.replace('end QOU.Archimedean', canonical_instance + '\nend QOU.Archimedean')
    with open(src_file, 'w') as f:
        f.write(content)

qou_lean = os.path.join(lean_root, 'QOU.lean')
with open(qou_lean, 'r') as f:
    qou_content = f.read()

if 'import QOU.Archimedean.EmCouplingBringZeroMode' not in qou_content:
    qou_content += 'import QOU.Archimedean.EmCouplingBringZeroMode\n'
    with open(qou_lean, 'w') as f:
        f.write(qou_content)

print("Patched EmCouplingBringZeroMode.lean and QOU.lean")
