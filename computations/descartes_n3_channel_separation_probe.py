#!/usr/bin/env python3
"""Do the per-summand characters separate the n=3 summands where the Jones pair fails?

## Why this probe exists

PR #6547 proved `QOU.Archimedean.jones_channels_not_separating`: the two
*named Jones values* of `descartes_n3_both_detected` --

    jonesSymmetric(q) = -(q + q^-1)
    jonesMixed(q)     = -(q^-4 (1 - q^2 + q^4))

-- coincide at `q* ~ 0.7795446638`, a `q` the Descartes condition permits
(`0 < q`, `q != 1`).  So that pair cannot distinguish the spin-3/2 and
spin-1/2 summands, and "both summands are detected" does not follow from
each value being non-zero.

That is a negative about *the pair those two theorems named*.  It says
nothing about whether the framework can separate the summands at all.  The
object that should do so is the per-partition character `chi^lambda`, and
the natural next question is whether it separates at exactly the `q` where
the Jones pair fails.

## The correction this probe records

Closing #6547 the agent reported the general-`n` per-summand character
values as "the upstream gap" and "the real open item".  **That was wrong.**
The corpus-grep checklist (AGENTS.md, path 3) finds the machinery live:

  * `tools/hecke-engine/src/seminormal.rs` -- `chi_lambda_braid`,
    `chi_lambdas_braid`, Hoefsmit seminormal form, general `n`, general
    `lambda`;
  * `tools/hecke-engine/src/seminormal_mpfr.rs` -- the MPFR variants;
  * `tools/hecke-engine/src/geck_pfeiffer.rs` -- the canonical-basis
    expansion `T_beta = sum_w c_w(q) T_w`;
  * `tools/hecke-engine/src/bin/hecke_canonical_chi.rs` -- a CLI over every
    `lambda |- n`;
  * all reachable from Python today: `pyhecke_native 0.9.0` exports about
    twenty chi entry points, `chi_lambdas_braid_mpfr` among them.

"Not in this Lean file" (true) had been reported as "upstream and open"
(false).  This probe needs no new machinery, which is the point.

## What it measures

1. `chi^[3]` and `chi^[2,1]` at `q = q*` on five braid words, checking
   separation at the exact point the Jones pair coincides.
2. The closed forms, against the native seminormal path at eight sample `q`:

       chi^[3](sigma_1)   = q
       chi^[2,1](sigma_1) = q - q^-1
       difference          = q^-1        -- never zero

   So the single generator `sigma_1` separates the two summands at every
   `q` outside `{0, 1}`, which includes every Descartes `q`.
3. The `q = 1` pole: `chi_lambdas_braid_mpfr` returns the string `NaN`
   there rather than raising.  Harmless for this arc (Descartes excludes
   `q = 1`) but recorded, because a caller that does not exclude it gets a
   NaN propagated into a witness with no error.

## Precision (AGENTS.md, NO-FLOAT64 -- probes are not exempt)

`mpmath.mpf` end to end at `mp.dps = 60`; the native call is the **MPFR**
variant at 50 dps, never `chi_lambdas_braid` (f64).  `float()` appears
nowhere.  Comparisons use an explicit `mpf` tolerance rather than `==`, and
the tolerance is reported.

Reference: Hoefsmit 1974; Mathas 1999, *Iwahori-Hecke Algebras and Schur
Algebras of the Symmetric Group*.  Bean `qou-qhs3`.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from mpmath import mp, mpf, findroot

import pyhecke_native as pn

mp.dps = 60

# Tolerance for the closed-form checks.  Well above the 50-dps native
# precision floor and well below any quantity being distinguished.
TOL = mpf("1e-45")

# Partitions of 3 with at most two rows -- the SU_q(2) summands at n = 3.
# [3] is the symmetric (spin-3/2) channel, dim 1; [2,1] the mixed-symmetry
# (spin-1/2) channel, dim 2.
SHAPES = [[3], [2, 1]]

WORDS = {
    "identity": [],
    "sigma1": [(1, 1)],
    "sigma1^3 (trefoil closure)": [(1, 1), (1, 1), (1, 1)],
    "sigma1 sigma2": [(1, 1), (1, 2)],
    "sigma1 sigma2^-1": [(1, 1), (-1, 2)],
}

# Sample points for the closed forms.  Deliberately spans both sides of 1,
# includes the substrate proton pin and the coincidence root, and excludes
# q = 1 (the seminormal pole, checked separately).
SAMPLE_Q = [
    "0.779544663820934968877573423932",   # q*, the Jones-coincidence root
    "1.1099785956427390466817951293800017527",  # substrate q0 (muon pin)
    "0.5",
    "2.0",
    "0.1",
    "10.0",
    "0.999",
    "1.001",
]


def jones_symmetric(q: mpf) -> mpf:
    """`-(q + q^-1)` -- QOU.Archimedean.jonesSymmetric."""
    return -(q + 1 / q)


def jones_mixed(q: mpf) -> mpf:
    """`-(q^-4 (1 - q^2 + q^4))` -- QOU.Archimedean.jonesMixed."""
    return -(q ** -4 * (1 - q ** 2 + q ** 4))


def chi_pair(q_str: str, word: list[tuple[int, int]]) -> tuple[mpf, mpf]:
    """`(chi^[3](beta), chi^[2,1](beta))` at `q`, via the MPFR native path."""
    vals = pn.chi_lambdas_braid_mpfr(SHAPES, word, q_str, 50)
    return mpf(vals[0]), mpf(vals[1])


def main() -> int:
    # The coincidence point, re-derived here rather than quoted: the Lean
    # reduces jonesSymmetric = jonesMixed to this quintic over q > 0.
    qstar = findroot(lambda q: q ** 5 - q ** 4 + q ** 3 + q ** 2 - 1, mpf("0.78"))
    qstar_str = mp.nstr(qstar, 50)

    # Sanity: the two Jones values really do coincide there.
    jones_gap = abs(jones_symmetric(qstar) - jones_mixed(qstar))
    jones_coincide = jones_gap < TOL

    print(f"q*            = {mp.nstr(qstar, 30)}")
    print(f"jonesSymmetric(q*) = {mp.nstr(jones_symmetric(qstar), 25)}")
    print(f"jonesMixed(q*)     = {mp.nstr(jones_mixed(qstar), 25)}")
    print(f"|difference|       = {mp.nstr(jones_gap, 6)}   coincide: {jones_coincide}")

    # (1) Separation of the characters at q*.
    print(f"\nAt q = q*, do the CHARACTERS separate?\n")
    print(f"{'word':<28} {'chi^[3]':>26} {'chi^[2,1]':>26}  sep")
    rows = []
    all_sep = True
    for name, w in WORDS.items():
        a, b = chi_pair(qstar_str, w)
        sep = abs(a - b) > TOL
        all_sep &= sep
        rows.append({
            "word": name,
            "chi_sym": mp.nstr(a, 30),
            "chi_mixed": mp.nstr(b, 30),
            "abs_gap": mp.nstr(abs(a - b), 20),
            "separates": bool(sep),
        })
        print(f"{name:<28} {mp.nstr(a, 20):>26} {mp.nstr(b, 20):>26}  "
              f"{'YES' if sep else 'no'}")

    # (2) Closed forms, and hence separation at every admissible q.
    print(f"\nClosed forms on sigma_1, against the native path "
          f"(tol {mp.nstr(TOL, 3)}):\n")
    cf = []
    ok_sym = ok_mix = ok_gap = True
    for s in SAMPLE_Q:
        q = mpf(s)
        a, b = chi_pair(s, [(1, 1)])
        d_sym = abs(a - q)
        d_mix = abs(b - (q - 1 / q))
        d_gap = abs((a - b) - 1 / q)
        ok_sym &= d_sym < TOL
        ok_mix &= d_mix < TOL
        ok_gap &= d_gap < TOL
        cf.append({
            "q": s,
            "resid_chi_sym_minus_q": mp.nstr(d_sym, 6),
            "resid_chi_mixed_minus_q_minus_qinv": mp.nstr(d_mix, 6),
            "resid_gap_minus_qinv": mp.nstr(d_gap, 6),
        })
        print(f"  q = {s[:24]:<26} resid_sym {mp.nstr(d_sym, 4):>10}  "
              f"resid_mix {mp.nstr(d_mix, 4):>10}  resid_gap {mp.nstr(d_gap, 4):>10}")

    print(f"\n  chi^[3](sigma_1)   == q        at all {len(SAMPLE_Q)}: {ok_sym}")
    print(f"  chi^[2,1](sigma_1) == q - 1/q  at all {len(SAMPLE_Q)}: {ok_mix}")
    print(f"  difference         == 1/q      at all {len(SAMPLE_Q)}: {ok_gap}")

    # (3) The q = 1 pole -- a silent NaN, not a raised error.
    at_one = pn.chi_lambdas_braid_mpfr(SHAPES, [(1, 1)], "1.0", 50)
    nan_at_one = all(v.strip().lower() == "nan" for v in at_one)
    print(f"\n  at q = 1 exactly: {at_one}  (silent NaN, not an exception: "
          f"{nan_at_one})")

    verdict = (
        "characters separate the n=3 summands at q*, where the named Jones "
        "pair coincides; sigma_1 alone separates at every q outside {0, 1}"
        if (jones_coincide and all_sep and ok_sym and ok_mix and ok_gap)
        else "INCONCLUSIVE -- a check did not hold; see fields"
    )
    print(f"\nverdict: {verdict}")

    out = {
        "$schema": "witness/v1",
        "name": "descartes-n3-channel-separation",
        "description": (
            "chi^lambda separates the two n=3 SU_q(2) summands at the q where "
            "the two named Jones values of descartes_n3_both_detected coincide. "
            "Resolves the scope of QOU.Archimedean.jones_channels_not_separating "
            "(PR #6547): that negative is about the named Jones pair, not about "
            "the framework's ability to separate summands."
        ),
        "bean": "qou-qhs3",
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "every value is evaluated at q* ~ 0.7795, the root of "
            "jonesSymmetric(q) = jonesMixed(q) found by findroot, and the "
            "closed forms are checked pointwise at eight sample q (one of "
            "them a typed copy of the muon pin, used only as a sample point "
            "for an identity that holds at every q); no substrate pin is "
            "read and no result depends on which pin q0 is"),
        "precision": {"mp_dps": mp.dps, "native_dps": 50,
                      "tolerance": mp.nstr(TOL, 3),
                      "float64_used": False},
        "shapes": SHAPES,
        "q_star": mp.nstr(qstar, 50),
        "jones_at_q_star": {
            "symmetric": mp.nstr(jones_symmetric(qstar), 30),
            "mixed": mp.nstr(jones_mixed(qstar), 30),
            "abs_gap": mp.nstr(jones_gap, 20),
            "coincide": bool(jones_coincide),
        },
        "character_separation_at_q_star": rows,
        "all_words_separate": bool(all_sep),
        "closed_forms": {
            "chi_symmetric_sigma1": "q",
            "chi_mixed_sigma1": "q - q^-1",
            "difference": "q^-1",
            "residuals": cf,
            "holds_chi_symmetric": bool(ok_sym),
            "holds_chi_mixed": bool(ok_mix),
            "holds_difference": bool(ok_gap),
        },
        "q_equals_one_pole": {
            "returns": at_one,
            "silent_nan_not_exception": bool(nan_at_one),
            "note": ("the seminormal form has a pole at q = 1; Descartes "
                     "excludes it, but a caller that does not gets NaN "
                     "propagated into a witness with no error raised"),
        },
        "verdict": verdict,
        "engine": {"pyhecke_native": pn.__version__ if hasattr(pn, "__version__")
                   else "0.9.0"},
    }
    path = Path(__file__).with_name("descartes-n3-channel-separation.witness.json")
    path.write_text(json.dumps(out, indent=2) + "\n")
    print(f"wrote {path.name}")
    return 0 if "INCONCLUSIVE" not in verdict else 1


if __name__ == "__main__":
    sys.exit(main())
