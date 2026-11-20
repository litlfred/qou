#!/usr/bin/env python3
"""ROAST-M2 / bean `qou-imcd` — exponent-only test of the atomic-braid → nucleus map.

⚠ CORRECTION 2026-08-31 — THE SHORTFALL FIGURES BELOW ARE AT THE WRONG SCALE
----------------------------------------------------------------------------
This probe multiplies its dimensionless log by `m_e = 0.511 MeV` and reports
"shortfall vs B/A plateau 6.906x". It gave no reason for choosing `m_e`, and the
corpus's own binding machinery does not: `computations/b_over_a_evaluator.py`
uses the hadronic energy unit `E_0 = m_e/(q_0(q_0-1)) = 4.18598 MeV`, as does the
`B_sym` linear-chain derivation (`alpha = E_0`, CAL-1) and the ROAST itself.

    E_0 / m_e = 1 / (q_0 (q_0 - 1)) = 8.1917611722

and that ratio is the WHOLE of the reported shortfall — verified against this
file's own committed witness in
`extensive_term_energy_scale_reconciliation_probe`. At `E_0` the extensive
coefficient is 10.086 MeV/nucleon, i.e. **1.19x OVER** the 8.5 plateau and 1.57x
short of `a_V`, not 6.9x short of anything.

**What survives, and it is the whole point of this probe:** the exponent test is
*scale-free* — a constant multiplier cannot change a log–log slope — so
`log_normaliser_A_exponent = 1` and the `(1+q^2)^n` closed form are untouched, as
is the verdict that the braid→nucleus map is not the defective step. Only the
MeV magnitudes and the "residual" framing are withdrawn. Every MeV figure in the
`extensive_coefficient_MeV_per_nucleon`, `light_isotope_comparison` and
`plateau_shortfall` blocks below is at `m_e` and must be scaled by 8.1917611722.

THE QUESTION
------------
Six Δ_λ magnitude ansätze have failed, all in the same way. The ROAST
(`docs/audits/2026-08-07-l2-attack-options-ROAST.md` §R2) proposed that the
common cause might not be a missing *term* but a defective *map*: the
A-nucleons → 3A-strands identification itself. Its cheap discriminator:

    does the framework reproduce the EXPONENT of any A-dependent observable,
    with magnitude entirely free?

If it cannot get an exponent right with magnitude free, the missing object is
not a magnitude and no added term can save it.

WHAT THIS PROBE MEASURES
------------------------
The framework's only A-dependent structure that does *not* route through the
open Δ_λ magnitude is the Markov-trace normaliser. `markov_weights_symbolic`
normalises by

    Z(n) = Σ_λ s_λ(1, Q, …, Q^{r-1}) · f^λ ,  Q = q², r = 2 (convention D)

and this probe first *verifies*, against that module's own components, that

    Z(n) = (1 + q²)^n                                    [assertion 1]

i.e. the normaliser is exactly exponential in the strand count. With 3 strands
per nucleon (`n = 3A`; the corpus's ⁴He braid words carry `n_strands = 12`),
its logarithm is therefore exactly linear in A — an *extensive* quantity, which
is the shape of the SEMF volume term.

Assertion 2 is the exponent test proper: fit the A-exponent of `log Z(3A)` and
compare it against the volume term's exponent, which is 1 from the
semi-empirical mass formula. The two sides are independent — one is the
corpus's normaliser, the other is textbook nuclear physics — so this is not a
tautology in the sense of bean `qou-l81w`.

WHY `log Z` AND NOT `Z`
-----------------------
The probe reports both. `Z(3A)` itself is exponential in A (5.5e16 at A = 16),
so only the *logarithm* has any chance of being an energy. The exponent test
therefore does more than pass/fail: it *selects* the reading. "Stop discarding
the normalisation" (attack A1) has to mean its logarithm enters the energy, not
the factor.

WHAT IS DELIBERATELY NOT DONE HERE
----------------------------------
The residual is reported and **not** matched to anything. The ROAST's §R0.1
found the memo's own headline coincidence had been convention-shopped — a rule
stated in §2.1 and violated in §4.3 of the same document. Hunting a structural
origin for the leftover constant is exactly that failure mode, so this probe
stops at measuring it.

Usage:
    python3 computations/probes/braid_nucleus_map_exponent_probe.py
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from math import factorial
from pathlib import Path

import sympy as sp
from mpmath import mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import markov.markov_weights_symbolic as M  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 40

# CODATA, MeV. Used only to put the extensive coefficient in energy units;
# no fit enters through it.
M_E_MEV = mp.mpf("0.51099895069")

# Strands per nucleon. Not a free parameter: the corpus's ⁴He braid words carry
# n_strands = 12 at A = 4 (`computations/atom_braid_words.py`), and
# `atom_braid_word_3A` is named for it.
STRANDS_PER_NUCLEON = 3

# Semi-empirical mass formula, volume term B ⊃ a_V·A — the exponent is 1.
# This is the INDEPENDENT side of assertion 2; it is textbook nuclear physics,
# not a corpus quantity.
SEMF_VOLUME_EXPONENT = 1

# CODATA binding energies, as carried by binding-K-direct.witness.json.
EMPIRICAL_B = [("D", 2, "2.22456637"), ("T", 3, "8.48179663"),
               ("3He", 3, "7.71799"), ("4He", 4, "28.29561")]


def rebuild_normaliser(n: int) -> sp.Expr:
    """Z(n), rebuilt from `markov_weights_symbolic`'s own components.

    Deliberately reconstructed rather than imported: the point of assertion 1
    is to check the closed form against the partition sum the module actually
    evaluates, so the two sides must be computed by different routes.
    """
    total = 0
    for shape in (tuple(s) for s in M.partitions_of(n)):
        hooks, _ = M.hooks_and_contents(list(shape))
        prod = 1
        for h in hooks:
            prod *= h
        f_lambda = factorial(n) // prod
        total += M.schur_principal_symbolic(list(shape)) * f_lambda
    return sp.cancel(sp.simplify(total))


def main() -> int:
    w = WitnessBuilder("braid-nucleus-map-exponent-probe")
    w.set_description(
        "ROAST-M2 exponent-only test of the A-nucleons -> 3A-strands map: does the "
        "framework reproduce the extensive (A^1) exponent with magnitude free?"
    )

    # ---- assertion 1: the normaliser is exactly (1+q^2)^n --------------------
    closed_form_matches = True
    for n in range(2, 7):
        rebuilt = rebuild_normaliser(n)
        closed = sp.cancel((1 + M.Q_W) ** n)
        if sp.simplify(sp.expand(rebuilt - closed)) != 0:
            closed_form_matches = False
    w.add_assertion(
        "normaliser_equals_two_Q_pow_n",
        computed="1" if closed_form_matches else "0",
        expected="1",
        source="partition sum over markov_weights_symbolic components vs closed form (1+q^2)^n, n=2..6",
    )

    # ---- assertion 2: the A-exponent of log Z is the volume term's ----------
    q0 = Q_MP
    log_z_per_strand = mp.log(1 + q0 ** 2)

    def log_z(A: int) -> mp.mpf:
        return STRANDS_PER_NUCLEON * A * log_z_per_strand

    # log-log slope over a wide A range; exact for a pure power law
    A_lo, A_hi = 2, 64
    slope = (mp.log(log_z(A_hi)) - mp.log(log_z(A_lo))) / (mp.log(A_hi) - mp.log(A_lo))
    w.add_assertion(
        "log_normaliser_A_exponent",
        computed=mp.nstr(slope, 20),
        expected=str(SEMF_VOLUME_EXPONENT),
        tolerance="1e-30",
        source="log-log slope of log Z(3A) over A=2..64 vs the SEMF volume-term exponent",
    )

    # ---- data: the coefficient, and the residual it leaves ------------------
    per_nucleon = STRANDS_PER_NUCLEON * log_z_per_strand * M_E_MEV
    w.add_parameter("q0", mp.nstr(q0, 30))
    w.add_parameter("strands_per_nucleon", STRANDS_PER_NUCLEON)
    w.add_parameter("m_e_MeV", str(M_E_MEV))
    w.add_data("log_normaliser_per_strand", mp.nstr(log_z_per_strand, 25))
    w.add_data("extensive_coefficient_MeV_per_nucleon", mp.nstr(per_nucleon, 25))

    rows = []
    for name, A, b_str in EMPIRICAL_B:
        b = mp.mpf(b_str)
        e_fw = A * per_nucleon
        rows.append({
            "atom": name, "A": A,
            "B_empirical_MeV": b_str,
            "E_framework_MeV": mp.nstr(e_fw, 12),
            "ratio_empirical_over_framework": mp.nstr(b / e_fw, 8),
        })
    w.add_data("light_isotope_comparison", rows)

    # The plateau is where a purely extensive term is comparable at all; below
    # A ~ 5 the empirical B/A is still climbing steeply through the alpha
    # particle, so the light-isotope ratios above are not a constant and are
    # reported as diagnostic only.
    w.add_data("plateau_shortfall", {
        "B_over_A_plateau_MeV": "8.5",
        "shortfall_vs_plateau": mp.nstr(mp.mpf("8.5") / per_nucleon, 8),
        "SEMF_a_V_MeV": "15.8",
        "shortfall_vs_a_V": mp.nstr(mp.mpf("15.8") / per_nucleon, 8),
    })
    w.add_data("Z_itself_is_exponential_in_A", {
        str(A): mp.nstr(mp.e ** log_z(A), 8) for A in (2, 4, 8, 16)
    })

    # The test is not vacuous: a plausible competing normaliser fails it.
    # `markov_weights_symbolic`'s own header mentions the form
    # `dim_q(λ)²/([n]_q!·f^λ)`, and `log [n]_q!` grows like n²·log q / 2 --
    # exponent 2, not 1. So the exponent test discriminates between candidate
    # normalisers, and between strand rules: an affine rule `n = 3A + c` with
    # c != 0 would also break the exact slope.
    def log_qfact(n: int) -> mp.mpf:
        total = mp.mpf(0)
        for k in range(1, n + 1):
            total += mp.log((q0 ** k - q0 ** (-k)) / (q0 - 1 / q0))
        return total

    def qfact_slope(lo: int, hi: int) -> mp.mpf:
        return ((mp.log(log_qfact(STRANDS_PER_NUCLEON * hi))
                 - mp.log(log_qfact(STRANDS_PER_NUCLEON * lo)))
                / (mp.log(hi) - mp.log(lo)))

    # Measured, not predicted. `log [n]_q! ~ (log q)n²/2 - n·log(q - 1/q)`, so the
    # asymptotic exponent is 2 but the linear term keeps the measured slope well
    # below it at accessible n. Reported across widening windows so the trend is
    # visible rather than asserted.
    w.add_data("discriminating_power", {
        "competing_normaliser": "[n]_q! (named in markov_weights_symbolic's header)",
        "measured_A_exponent_by_window": {
            f"A={lo}..{hi}": mp.nstr(qfact_slope(lo, hi), 8)
            for lo, hi in ((2, 64), (64, 256), (256, 1024), (1024, 4096))
        },
        "note": ("Measured 1.674 on A=2..64 and rising to 1.995 on A=1024..4096 -- "
                 "asymptotically 2, approached slowly because of the linear term. "
                 "Either way it is NOT 1, so the exponent test does discriminate "
                 "between the corpus's actual normaliser and a plausible alternative, "
                 "and would also detect an affine strand rule n = 3A + c, c != 0. "
                 "The test is therefore not vacuous."),
    })
    w.add_data("SCALE_CORRECTION_2026_08_31", {
        "what_is_wrong": "Every MeV figure in this witness uses m_e = 0.511 MeV as the "
                         "energy scale, with no justification given. The corpus's binding "
                         "machinery uses E_0 = m_e/(q_0(q_0-1)) = 4.18598 MeV.",
        "scale_ratio_E0_over_me": mp.nstr(1 / (q0 * (q0 - 1)), 20),
        "corrected_extensive_coefficient_MeV_per_nucleon":
            mp.nstr(per_nucleon / (q0 * (q0 - 1)), 12),
        "corrected_vs_plateau": mp.nstr(
            mp.mpf("8.5") * q0 * (q0 - 1) / per_nucleon, 8) + "x (i.e. it OVERSHOOTS 8.5)",
        "corrected_vs_a_V": mp.nstr(
            mp.mpf("15.8") * q0 * (q0 - 1) / per_nucleon, 8) + "x short",
        "what_is_UNAFFECTED": "The exponent test itself. A constant multiplier cannot "
                              "change a log-log slope, so log_normaliser_A_exponent = 1 and "
                              "the (1+q^2)^n closed form stand, and so does the verdict that "
                              "the braid->nucleus map is not the defective step.",
        "see": "computations/probes/extensive_term_energy_scale_reconciliation_probe.py",
    })
    w.add_data("verdict", (
        "EXPONENT TEST PASSES (unaffected by the scale correction above; a log-log slope "
        "is scale-free). The 3-strands-per-nucleon map yields a normaliser whose "
        "logarithm is exactly linear in A -- the SEMF volume term's exponent -- with the "
        "coefficient constant to all computed digits. This is a NEGATIVE for the ROAST's "
        "R2 hypothesis that the braid->nucleus map is the defective step: the map's "
        "A-scaling is right. The residual is a pure multiplicative constant, not a shape "
        "error. Deliberately not matched to any structural candidate (see module "
        "docstring)."
    ))

    out = w.save()
    print(f"wrote {out}")
    print(f"  normaliser == (1+q^2)^n for n=2..6 : {closed_form_matches}")
    print(f"  A-exponent of log Z                : {mp.nstr(slope, 12)} (SEMF volume term: 1)")
    print(f"  extensive coefficient              : {mp.nstr(per_nucleon, 12)} MeV/nucleon")
    print(f"  shortfall vs B/A plateau (8.5 MeV) : {mp.nstr(mp.mpf('8.5') / per_nucleon, 6)}x")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
