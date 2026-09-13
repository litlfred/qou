#!/usr/bin/env python3
"""What does an observational bound on |d(alpha)/alpha| say about q0?  (bean qou-ultb)

`qou-ultb` is a title with an empty body.  Its title asserts that actinide
cosmochronometry on CS 31082-001 (U II 3859.57 A) bounds |d(alpha)/alpha| <~
2.08e-3 -- "LOOSER than quasars but at the FORMATION site".

Two separable questions, and only one of them is answerable from this corpus:

  (1) Is 2.08e-3 the right bound?   NOT ANSWERABLE HERE.  Corpus-grep path 5
      run 2026-09-13: `library/` holds NO source on CS 31082-001, actinide
      cosmochronometry, or the U II 3859.57 A line -- one INDEX.md hit and one
      unrelated nucl-th summary, no section text.  The figure is carried by
      the bean title alone.  It is used below as an INPUT, labelled
      unverified, never as an established number.

  (2) Given ANY bound B on |d(alpha)/alpha|, what does it say about q0?
      FULLY ANSWERABLE, and that is what this probe computes.  The framework
      derives alpha_em from q, so a bound on alpha is a bound on q divided by
      the sensitivity

          S = |d ln(alpha) / d ln q|   at q0,

      giving  |dq/q| <= B / S.  Whether that is interesting is then settled by
      comparing it to the framework's OWN precision on q0.

The derived alpha is `meson_em_sinh_closed_form.alpha_em_inv_derived`, which
the L2 dashboard also uses -- so this measures the SAME object the framework
scores, not a re-derivation of it.

Precision: mpmath mpf throughout at 60 dps, and the derivative is taken
symbolically-in-the-limit via mp.diff rather than by a hand-rolled difference
quotient.  No float64 (AGENTS.md NO-FLOAT64, which binds probes).

SCOPE.  The conversion in (2) is only as good as the alpha(q) derivation it
rides on, and AGENTS.md records that derivation as conditional on an open Lean
`sorry` (the Witten-kappa Gram determinant).  So the number below is
"what this bound would say IF the framework's alpha(q) holds", not a result
about nature.  Stated here rather than left for a reader to discover.
"""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))
sys.path.insert(0, str(_ROOT / "computations"))

import mpmath as mp  # noqa: E402

mp.mp.dps = 60

from qou_substrate.constants import q_at  # noqa: E402
from meson_em_sinh_closed_form import alpha_em_inv_derived  # noqa: E402

# The bean title's figure.  UNVERIFIED -- no held source; see the docstring.
B_ULTB_UNVERIFIED = mp.mpf("2.08e-3")

# For scale only.  Quasar many-multiplet bounds are quoted at the 1e-5..1e-6
# level in the literature; used purely to check the bean's "LOOSER than
# quasars" ordering claim, which does not depend on the exact value.
B_QUASAR_ORDER = mp.mpf("1e-5")


def hdr(t: str) -> None:
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


def alpha_of(q):
    """alpha_em(q) = 1 / alpha_em_inv_derived(q)."""
    return 1 / alpha_em_inv_derived(q)


hdr("[1] The framework's alpha at the substrate anchor")

q0 = q_at(dps=60)
a_inv = alpha_em_inv_derived(q0)
a0 = alpha_of(q0)
print(f"  q0 (proton pin)        = {mp.nstr(q0, 30)}")
print(f"  alpha_em^-1 (derived)  = {mp.nstr(a_inv, 20)}")
print(f"  alpha_em    (derived)  = {mp.nstr(a0, 20)}")
print()
print("  Source: meson_em_sinh_closed_form.alpha_em_inv_derived -- the same")
print("  entry point the L2 dashboard scores, not a re-derivation.")

hdr("[2] Sensitivity  S = |d ln(alpha) / d ln q|  at q0")

dadq = mp.diff(alpha_of, q0)
S = abs(dadq * q0 / a0)
print(f"  d(alpha)/dq            = {mp.nstr(dadq, 20)}")
print(f"  S = |dlna / dlnq|      = {mp.nstr(S, 20)}")

# Cross-check against the closed form the producer verifies:
#   alpha_em^-1 is built on (3q^2 - 1)/(2q^2); confirm the derivative is not
#   an artifact of mp.diff's step by recomputing at a second dps.
mp.mp.dps = 90
q0b = q_at(dps=90)
S_b = abs(mp.diff(alpha_of, q0b) * q0b / alpha_of(q0b))
mp.mp.dps = 60
agree = abs(S - S_b) / S
print(f"  same at 90 dps         = {mp.nstr(S_b, 20)}")
print(f"  relative agreement     = {mp.nstr(agree, 5)}")
assert agree < mp.mpf("1e-25"), "sensitivity is not stable across precision"
print("  -> stable across precision, so it is the derivative and not the step.")

hdr("[3] Converting a bound on alpha into a bound on q")

print("  |dq/q|  <=  B / S      for any bound B on |d(alpha)/alpha|.")
print()
print(f"  {'B on |dalpha/alpha|':<34}{'implied |dq/q|':<26}")
print("  " + "-" * 62)
for label, B in (
    ("qou-ultb title (UNVERIFIED)", B_ULTB_UNVERIFIED),
    ("quasar-order, for scale", B_QUASAR_ORDER),
):
    implied = B / S
    print(f"  {label:<34}{mp.nstr(implied, 6):<26}")

implied_ultb = B_ULTB_UNVERIFIED / S

hdr("[4] Is it constraining?  Compare to the framework's OWN precision on q0")

# sigma(q0) as AGENTS.md records it for the proton pin.
SIGMA_Q0_PPB = mp.mpf("1.22335")
sigma_rel = SIGMA_Q0_PPB * mp.mpf("1e-9")
ratio = implied_ultb / sigma_rel

print(f"  sigma(q0), proton pin  = {mp.nstr(SIGMA_Q0_PPB, 6)} ppb = {mp.nstr(sigma_rel, 6)}")
print(f"  implied |dq/q| bound   = {mp.nstr(implied_ultb, 6)}")
print(f"  ratio bound / sigma    = {mp.nstr(ratio, 6)}")
print()
if ratio > 1:
    print(f"  The bound is LOOSER than the framework's own pin by ~{mp.nstr(ratio, 4)}x.")
    print("  So this observation CANNOT constrain q0 -- the substrate parameter is")
    print("  already known, from CODATA mass ratios, far more tightly than any")
    print("  alpha bound at this level could test.")
else:
    print("  The bound is TIGHTER than the framework's own pin -- it would be")
    print("  a genuine test.  Check this carefully; it is the surprising branch.")

hdr("[5] VERDICT -- scope (a), and it re-frames the bean rather than answering it")

print(f"""
  ESTABLISHED (exact, mpmath 60 dps, stable to 90 dps):

    S = |d ln(alpha_em) / d ln q| = {mp.nstr(S, 12)} at the proton q0.

    So a bound B on |d(alpha)/alpha| is a bound B/{mp.nstr(S, 6)} on |dq/q|.
    At the bean's asserted B = 2.08e-3 that is |dq/q| <= {mp.nstr(implied_ultb, 6)},
    which is ~{mp.nstr(ratio, 4)}x LOOSER than sigma(q0) itself.

  WHAT THAT MEANS FOR THE BEAN.  Its framing -- "LOOSER than quasars but at
  the FORMATION site" -- treats the formation-site locality as the payoff
  that offsets the weaker bound.  For THIS framework that trade does not pay:
  even a formation-site measurement {mp.nstr(ratio, 3)}x weaker than the existing pin
  constrains nothing about q0.  The interesting version of this observation
  would need B <~ {mp.nstr(S * sigma_rel, 4)}, i.e. ~{mp.nstr(B_ULTB_UNVERIFIED / (S * sigma_rel), 4)}x tighter -- far beyond
  quasar bounds too, so the whole alpha-variation programme is the wrong
  instrument for pinning q0.

  NOT ESTABLISHED, and deliberately not guessed:

    * Whether 2.08e-3 is the right bound.  `library/` holds NO source on CS
      31082-001 or actinide cosmochronometry (corpus-grep path 5, run today),
      so the figure has no provenance in this corpus.  It is an INPUT here.
      Note the conclusion is INSENSITIVE to it: the bound would have to
      improve by ~{mp.nstr(B_ULTB_UNVERIFIED / (S * sigma_rel), 3)}x to matter, so no plausible correction to
      2.08e-3 changes the verdict.

    * Whether alpha_em(q) is right.  AGENTS.md records the alpha_em
      derivation as conditional on an open Lean `sorry` (Witten-kappa Gram
      determinant), so section [3] is "IF the framework's alpha(q) holds".

  Scope (a): this says the alpha-variation route cannot TEST q0 at achievable
  precision.  It rules out no ingredient -- r-process observables may well
  constrain the framework through nuclear masses or beta rates (beans
  qou-ihtw, qou-fu7d), which is a different quantity and is untouched here.
""")

print("PROBE OK -- sensitivity stable across precision; all assertions passed.")
