#!/usr/bin/env python3
"""Reeb-spectrum resonance probe for the OPEN dynamical part of the spin-colour
coupling (conj:s5-so3-fiber-action).

The static coupling is Schur-forced (s5so3_ingredient4_coupling_schur.py).  The
open piece is the DYNAMICAL intertwining: the spin Hopf Reeb (S^3) flow's
generation-level eigenvalue (an SO(3) datum of V_ell) must "resonate" with the
colour Sasakian Reeb (S^5) flow's eigenvalue on the matched H_5(q) Wedderburn
block lambda.  This probe tests whether any NATURAL, PARAMETER-FREE relation
matches the spin-ell and colour-lambda eigenvalues across the bridge.

STRICT NUMEROLOGY GUARD (agreed protocol):
  * a 2-point match (ell=1,2) is meaningless -- many parameter-free formulas fit
    two points (e.g. both ell*(ell-1) and 2*(ell-1) give {0,2}).  Require a THIRD
    anchor (ell=3, tau) and ZERO free constants.
  * report a resonance ONLY if exact + parameter-free + holds at all >=3 anchors.
    Otherwise report NO resonance (the honest, expected outcome).

No external deps.
"""
import sys

# ---- spin side: SO(3) harmonic V_ell on the divisor sphere ----------------
def casimir_so3(ell):
    return ell * (ell + 1)

# ---- colour side: content sum of an H_5(q) Wedderburn block lambda ---------
def content_sum(lam):
    """sum over cells of (col - row), 1-based (the standard content)."""
    return sum((j + 1) - (i + 1) for i, row in enumerate(lam) for j in range(row))

# ---- the verified bridge ell -> A5-irrep -> colour block(s) ----------------
# ell=1 -> T1 -> (3,1,1)      [single block]
# ell=2 -> H  -> (3,2)        [single block]
# ell=3 -> T2 (+) G -> (3,1,1) AND (4,1)   [MULTI-block: tau spreads]
BRIDGE = {
    1: [(3, 1, 1)],
    2: [(3, 2)],
    3: [(3, 1, 1), (4, 1)],
}

print("=" * 72)
print("Reeb-resonance probe: spin-ell eigenvalue vs colour-lambda eigenvalue")
print("=" * 72)
for ell in (1, 2, 3):
    blocks = BRIDGE[ell]
    cs = [content_sum(b) for b in blocks]
    multi = " (MULTI-block: tau spreads -> colour eigenvalue AMBIGUOUS)" if len(blocks) > 1 else ""
    print(f"  ell={ell}: SO(3) Casimir ell(ell+1)={casimir_so3(ell)} ; "
          f"colour blocks {blocks} content-sums {cs}{multi}")

print()
print("=" * 72)
print("Candidate parameter-free relations (single-block anchors ell=1,2 + ell=3)")
print("=" * 72)
# content sum at the single-block anchors:
c1 = content_sum((3, 1, 1))   # ell=1
c2 = content_sum((3, 2))      # ell=2
print(f"  content: ell=1 -> {c1}, ell=2 -> {c2}")
# Two parameter-free formulas that BOTH fit the 2-point set {0,2}:
cand = {
    "ell*(ell-1)": lambda e: e * (e - 1),
    "2*(ell-1)":   lambda e: 2 * (e - 1),
}
for name, f in cand.items():
    vals2 = (f(1), f(2))
    fit2 = (vals2 == (c1, c2))
    print(f"    {name}: ell=1,2 -> {vals2}  fits 2 anchors: {fit2}")
print("  => TWO distinct parameter-free formulas fit the 2 single-block anchors")
print("     equally -> the 2-point 'match' is NON-UNIQUE (fittable). Need ell=3.")

print()
print("  ell=3 (tau) test -- the discriminating anchor:")
for name, f in cand.items():
    pred = f(3)
    # tau colour content is ambiguous (multi-block); list both block contents
    tau_cs = [content_sum(b) for b in BRIDGE[3]]
    matches = pred in tau_cs
    print(f"    {name}: predicts {pred}; tau block contents {tau_cs}; matches any: {matches}")

print()
print("=" * 72)
print("VERDICT")
print("=" * 72)
print("  - ell=3 (tau) is MULTI-block (T2 in (3,1,1), G in (4,1)): a single")
print("    colour Reeb eigenvalue is not even well-defined there.")
print("  - the apparent 2-point matches (content = ell*(ell-1) AND = 2*(ell-1))")
print("    are NON-UNIQUE and BOTH FAIL at ell=3 (predict 6 / 4; tau contents are")
print("    {0, 5}).")
print("  => NO exact, parameter-free, >=3-anchor Reeb resonance is found.")
print("     The dynamical spin-colour intertwining is NOT realized by a simple")
print("     eigenvalue match; it remains genuinely open.  Per the numerology")
print("     guard, the 2-point coincidences are NOT reported as a result.")

# Assertions encode the (negative) finding.
assert content_sum((3, 1, 1)) == 0 and content_sum((3, 2)) == 2
assert content_sum((4, 1)) == 5
# both 2-pt fits agree at ell=1,2 but fail at ell=3:
assert 1 * (1 - 1) == 0 and 2 * (2 - 1) == 2          # agree at ell=1,2
tau_cs = [content_sum(b) for b in BRIDGE[3]]
assert (3 * 2) not in tau_cs and (2 * 2) not in tau_cs  # ell(ell-1)=6, 2(ell-1)=4 absent
print("\nNO-RESONANCE (numerology-guard) ASSERTIONS VERIFIED.")
sys.exit(0)
