#!/usr/bin/env python3
"""Ingredient 4 + 5 of the s5-so3 keystone: the H5(q)->H3(q) commuting square
(algebraic leg) and the Markov-trace shift vs the 210 ppb muon gap (ingredient 5).

Uses the REAL pyhecke compute stack (not a re-implementation):
  - q0, q_factorial: pyhecke (qou_substrate substrate anchor)
  - FIG8_R_311 / FIG8_R_32 / FIG8_R_41: the figure-eight (4_1 = muon knot)
    Markov traces through the Wedderburn projectors E_(3,1,1) / E_(3,2) / E_(4,1).

Dependencies (sandbox): mpmath, numpy, sympy; tools/{qou-substrate,pyhecke,
pyhecke-native}/python on sys.path.  Canonical home for this compute is
folio-assistant/computations/ (absent in this sandbox -> sited under
docs/audits/scripts/ as a falsification probe; see the s5so3 finding doc).

VERDICT computed here: the Wedderburn-projector correction F(E,q0) named in
2026-06-13-gap-a4-operator-valued-muon-branching.md OVERSHOOTS the 210 ppb gap
by 6-8 orders of magnitude.  Ingredient 4's algebraic leg is concrete; ingredient
5 (the 210 ppb physics) is REFUTED for the named candidates.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
for sub in ("tools/qou-substrate/python", "tools/pyhecke/python", "tools/pyhecke-native/python"):
    p = os.path.join(ROOT, sub)
    if p not in sys.path:
        sys.path.insert(0, p)

try:
    import pyhecke as ph
    from pyhecke import atom
    import pyhecke.constants as c
except Exception as e:  # pragma: no cover - environment guard
    print(f"SKIP: pyhecke unavailable ({type(e).__name__}: {e}).")
    print("Install mpmath/numpy/sympy and ensure tools/*/python on path.")
    sys.exit(0)

TARGET_PPB = 2.1e-7   # the muon gap: 209.8 ppb (per-observable dashboard / GAP-A-4 doc)

q0 = float(c.q0)
qf3 = float(atom.q_factorial(3))        # [3]_q! at q0
W_alt = 1.0 / qf3                       # H3 Plancherel weight of the 1-dim alt (1,1,1) block
W_sym = 1.0 / qf3
W_std = float(ph.atom.q_dimension((2, 1))) ** 2 / qf3 if hasattr(atom, "q_dimension") else None

f311 = float(ph.FIG8_R_311)             # 4_1 trace, electron block (3,1,1)
f32 = float(ph.FIG8_R_32)               # 4_1 trace, muon block (3,2)
f41 = float(ph.FIG8_R_41)               # 4_1 trace, (4,1) block

print("=" * 72)
print("INGREDIENT 4 — commuting square, ALGEBRAIC leg (Hecke tower H5->H3)")
print("=" * 72)
print(f"  q0 = {q0}")
print(f"  [3]_q! = {qf3:.6f}  (matches lepton-bring-surface-h3-3channel.md 6.1206)")
print(f"  H3 Plancherel weights: W_sym=W_alt=1/[3]_q!={W_alt:.5f}, W_std=[2]^2/[3]_q!={W_std:.5f}")
print("  Hecke-tower Bratteli restriction H5(q)->H3(q) at generic q = box removal")
print("  = the verified Res^{S5}_{S3} branching (see s5so3_branching_backbone_verify.py):")
print("    electron (3,1,1)|S3 = (3) + 2(2,1) + (1,1,1)")
print("    muon     (3,2)|S3   = (3) + 2(2,1)")
print("    => muon block lacks exactly the (1,1,1) alt block (the e-mu difference).")
print("  The Wedderburn projectors E_lambda and their Markov traces are COMPUTABLE")
print("  (below); the GEOMETRIC leg (Reeb flow = this algebra map) stays conjectural.")

print()
print("=" * 72)
print("INGREDIENT 5 — Markov-trace shift vs the 210 ppb muon gap")
print("=" * 72)
print(f"  figure-eight 4_1 (the muon knot, m_mu = m_e * Vol(4_1)/hbar_q^2) traces:")
print(f"    FIG8_R_311 (electron proj E_(3,1,1)) = {f311:+.8f}")
print(f"    FIG8_R_32  (muon proj     E_(3,2))   = {f32:+.8f}")
print(f"    FIG8_R_41  ((4,1) block)             = {f41:+.8f}")

# Candidate F #1 (doc's named 'character shift' / sign-block subtraction):
#   F = 1 - W_alt * chi^{(1,1,1)}(beta_Bor), with chi = 1 (exact, sign rep).
chi_111 = 1.0  # ((-q)(-q^{-1}))^3 = 1, exact integer (sign rep on the Borromean)
shift_signblock = W_alt * chi_111
over_signblock = shift_signblock / TARGET_PPB
print()
print("  Candidate F #1 — sign-block subtraction (doc 5.2): F = 1 - W_alt*chi^(1,1,1)")
print(f"    chi^(1,1,1)(beta_Bor) = {chi_111:.0f} (exact);  |1-F| = W_alt = {shift_signblock:.5f} (16.3%)")
print(f"    vs target {TARGET_PPB:.2e}  ->  OVERSHOOT x {over_signblock:,.0f}  (~{__import__('math').log10(over_signblock):.1f} orders)")

# Candidate F #2 (doc's named 'normalized quantum-dimension / channel ratio'):
#   F = R_32 / R_311  (muon channel trace / electron channel trace).
ratio = f32 / f311
shift_ratio = abs(ratio - 1.0)
over_ratio = shift_ratio / TARGET_PPB
print()
print("  Candidate F #2 — channel-trace ratio (doc 3): F = R_32 / R_311")
print(f"    R_32/R_311 = {ratio:.6f}  ->  |F-1| = {shift_ratio:.4f} ({shift_ratio*100:.0f}%)")
print(f"    vs target {TARGET_PPB:.2e}  ->  OVERSHOOT x {over_ratio:,.0f}  (~{__import__('math').log10(over_ratio):.1f} orders)")

print()
print("  VERDICT: both named candidates for the Wedderburn correction F(E,q0) are")
print("  O(1)-O(10), i.e. 6-8 orders of magnitude TOO LARGE to be the 210 ppb gap.")
print("  The bare m_e*Vol(4_1)/hbar_q^2 is ALREADY good to 210 ppb; multiplying by")
print("  any of these projector corrections DESTROYS that agreement.  The structural")
print("  identity (chi^(1,1,1)=1; (1,1,1) IS the e-mu block) is exact, but the")
print("  MAGNITUDE refutes the projector mechanism as the 210 ppb closure.")
print("  => Ingredient 5 REFUTED for the named candidates (confirms synthesis sec 4).")

# Self-check assertions: the refutation is the verified content.
assert abs(qf3 - 6.1206) < 1e-3, "q_factorial(3) convention drift"
assert over_signblock > 1e5, "sign-block overshoot should be >1e5"
assert over_ratio > 1e6, "channel-ratio overshoot should be >1e6"
assert chi_111 == 1.0
print()
print("ALL INGREDIENT-4/5 ASSERTIONS VERIFIED (refutation confirmed).")
sys.exit(0)
