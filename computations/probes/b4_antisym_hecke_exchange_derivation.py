#!/usr/bin/env python3
"""Value leg — principled antisymmetric-Hecke exchange DERIVATION (both naive fail).

Scoping: docs/design/2026-07-06-gap-a4-b4-branching-projector-construction-spec.md.
The value is pinned to `B = −ln det(I + G)` with `G` a SIGN-CARRYING exchange
matrix (Perron–Frobenius excluded the positive binding factors). The [1^4] shell
is the ANTISYMMETRIC Hecke channel, eigenvalue `λ_− = −q^{-1/2} < 0` — the derived
(not fitted) sign source. This unit builds `G` from the two most natural
PRINCIPLED antisymmetric exchange factors and reads `−ln det` ONCE each — no
tuning, no search for the factor that hits 9.243.

Building blocks (q₀): `z = 1/(q^{1/2}+q^{-1/2}) = 0.4993` (symmetric, bar-even),
`λ_− = −q^{-1/2} = −0.9492` (antisym Hecke eigenvalue), `−h/2 = −0.1045` (bar-odd
part of the pn factor). Uniform 4-nucleon `G = g·(J−I)` ⇒ det(I+G) = (1+3g)(1−g)³.

RESULTS (scope-(a), one shot each — DERIVED, not fitted):
  • Candidate 1  g = λ_−·z = −0.4739 (antisym-Hecke exchange):
      det(I+G) = −1.351 < 0  ⇒  −ln det is COMPLEX — UNPHYSICAL. The naive
      antisym-Hecke exchange is too large; it over-rotates the determinant.
  • Candidate 2  g = −h/2 = −0.1045 (bar-odd pn part):
      −ln det = 0.078 (dimensionless) ≈ 0.33 MeV (×E₀) — ~28× BELOW b₄ = 9.243.

VERDICT (honest, no fit): NEITHER naive principled exchange reproduces the
target — one is unphysical (det<0), the other far too small. So the correct
exchange ENTRIES are neither `λ_−·z` nor `−h/2` uniform; they require the proper
4-nucleon [1^4] braid WRITHE structure (per-pair signs + magnitudes), which is
genuine derivation, NOT a session-tail computation. This probe records the two
principled attempts and their failure — the maximal honest narrowing. **Searching
for the `g` that yields 9.243 would be a fit (Rule-14) and is refused.**

`-- Ref:` b4_exchange_perron_frobenius_constraint.py; b4_slater_dictionary_functional_form.py.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

import mpmath as mp

# Path bridge (moved above the set_compute_dps() call — it is what
# puts computations/substrate on sys.path so `_precision` resolves).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
from substrate.witness_base import WitnessBuilder  # noqa: E402

COMP = str(_COMP)


def det_uniform(g):
    """det(I + g(J−I)) for the 4-nucleon uniform exchange."""
    return (1 + 3 * g) * (1 - g) ** 3


def main() -> int:
    q = mp.mpf("1.10997858275138080759166909561076887987449912187357763605672")
    sq = mp.sqrt(q)
    z = 1 / (sq + 1 / sq)
    h = q - 1 / q
    lam_minus = -1 / sq
    E0 = mp.mpf("0.51099895069") / (q * (q - 1))
    b4_target = mp.mpf("9.243")

    g1 = lam_minus * z
    d1 = det_uniform(g1)
    g2 = -h / 2
    d2 = det_uniform(g2)
    val2 = -mp.log(d2)
    mev2 = E0 * val2

    c1_unphysical = d1 <= 0
    c2_too_small = mev2 < b4_target / 5

    result = {
        "building_blocks": {"z_sym": mp.nstr(z, 6), "lambda_minus": mp.nstr(lam_minus, 6),
                            "minus_h_over_2": mp.nstr(-h / 2, 6)},
        "candidate_1_antisym_hecke": {
            "g": mp.nstr(g1, 6), "det_I_plus_G": mp.nstr(d1, 6),
            "status": "UNPHYSICAL (det < 0 ⇒ −ln det complex)"},
        "candidate_2_bar_odd": {
            "g": mp.nstr(g2, 6), "neg_log_det": mp.nstr(val2, 6),
            "rough_MeV": mp.nstr(mev2, 6), "status": "~28× BELOW target b₄=9.243"},
        "verdict": (
            "Both naive principled antisymmetric exchanges fail: g=λ_−·z (−0.474) gives a "
            "NEGATIVE determinant (unphysical), g=−h/2 (−0.105) gives ~0.33 MeV (~28× too "
            "small). The correct exchange entries are neither — they need the proper 4-nucleon "
            "[1^4] braid writhe structure (per-pair signs+magnitudes), genuine derivation. "
            "Searching for the g that yields 9.243 would be a fit (Rule-14) and is REFUSED. "
            "Scope-(a); this records the principled attempts and their honest failure."),
    }

    payload = {
        "computation": "b4-antisym-hecke-exchange-derivation",
        "description": ("Principled antisymmetric-Hecke exchange derivation for the [1^4] value: "
                        "g=λ_−·z gives det<0 (unphysical); g=−h/2 gives ~0.33 MeV (28× low). "
                        "Neither naive exchange reproduces b₄=9.243; the correct entries need the "
                        "4-nucleon writhe structure. No fit. audit-only."),
        "tier": "structural (one-shot −ln det for two principled exchange factors; no tuning)",
        "result": result,
        "context": {
            "axis": "GAP-A-4 class-D — [1^4] value leg, antisymmetric-Hecke exchange derivation",
            "spec": "docs/design/2026-07-06-gap-a4-b4-branching-projector-construction-spec.md",
            "status": "naive principled exchanges fail; correct entries = open derivation (writhe structure)",
        },
    }
    wb = WitnessBuilder.wrap_legacy(
        "b4-antisym-hecke-exchange-derivation", payload,
        script_path=__file__, engine="python+mpmath", output_dir=os.path.join(COMP, "probes"),
    )
    wb.add_assertion("candidate1_antisym_hecke_gives_negative_det",
                     computed=str(bool(c1_unphysical)), expected="True")
    wb.add_assertion("candidate2_bar_odd_far_below_target",
                     computed=str(bool(c2_too_small)), expected="True")
    out = wb.save(extra={"auditOnly": True})

    print("=== Antisymmetric-Hecke exchange derivation (one shot each, no tuning) ===")
    print(f"  z={float(z):.4f}  λ_−={float(lam_minus):.4f}  −h/2={float(-h/2):.4f}")
    print(f"  cand-1  g=λ_−·z={float(g1):+.4f}  det={float(d1):+.4f}  -> UNPHYSICAL (det<0)")
    print(f"  cand-2  g=−h/2={float(g2):+.4f}  -ln det={float(val2):.4f}  ~{float(mev2):.2f} MeV  -> 28× below 9.243")
    print("  VERDICT: neither naive principled exchange works; correct entries need the 4-nucleon")
    print("           [1^4] writhe structure (genuine derivation). No fit to 9.243 (refused).")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
