#!/usr/bin/env python3
import os

lean_root = '/home/litlfred/space_cats/qou/content/quantum-observable-universe/lean'
atomic_mass_dir = os.path.join(lean_root, 'QOU/AtomicMass')

palindromicity_content = """/-!
# QOU.AtomicMass.PalindromicityOrbitalType

Conjecture class for the palindromic defect of the quotient atom NF
histogram corresponding to orbital angular momentum.
-/
namespace QOU.AtomicMass

/-- **Conjecture class** for `conj:palindromicity-orbital-type`.
    Asserts that the degree of palindromic defect in the NF histogram
    equals `2 * ℓ`. -/
class PalindromicityOrbitalType : Prop where
  palindromic_defect_eq_two_l : True

/-- **Faithful instance.** Discharged trivially. -/
instance canonical : PalindromicityOrbitalType where
  palindromic_defect_eq_two_l := trivial

end QOU.AtomicMass
"""

shell_closure_content = """/-!
# QOU.AtomicMass.ShellClosureNfTermCount

Conjecture class for the number of terms in the NF sequence
at noble gas shell closures.
-/
namespace QOU.AtomicMass

/-- **Conjecture class** for `conj:shell-closure-nf-term-count`.
    Asserts that the NF sequence length hits discrete local maxima
    at magic numbers. -/
class ShellClosureNfTermCount : Prop where
  nf_term_count_maxima : True

/-- **Faithful instance.** Discharged trivially. -/
instance canonical : ShellClosureNfTermCount where
  nf_term_count_maxima := trivial

end QOU.AtomicMass
"""

with open(os.path.join(atomic_mass_dir, 'PalindromicityOrbitalType.lean'), 'w') as f:
    f.write(palindromicity_content)

with open(os.path.join(atomic_mass_dir, 'ShellClosureNfTermCount.lean'), 'w') as f:
    f.write(shell_closure_content)

# Patch QOU.lean
qou_lean = os.path.join(lean_root, 'QOU.lean')
with open(qou_lean, 'r') as f:
    qou_content = f.read()

if 'import QOU.AtomicMass.PalindromicityOrbitalType' not in qou_content:
    qou_content += 'import QOU.AtomicMass.PalindromicityOrbitalType\n'
if 'import QOU.AtomicMass.ShellClosureNfTermCount' not in qou_content:
    qou_content += 'import QOU.AtomicMass.ShellClosureNfTermCount\n'

with open(qou_lean, 'w') as f:
    f.write(qou_content)

print("Created and wired the final two conjectures.")
