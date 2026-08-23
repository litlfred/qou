#!/usr/bin/env python3
"""Where /q^3 comes from: it is the q-Schur Plancherel weight of the trivial block.

Bean `qou-24w9`. Owner asked what the CORPUS and the LITERATURE say about the
normalisation options for `F_Bor = |tr_M(b_Bor)| . [3]_q! / q^3`.

WHAT THIS ADDS. PR #5294 closed the derivability question negatively (the factor
is unreachable by the writhe rule, double-counts the Poincare centering, and is
the sole bar-asymmetric step) and the option table found every DERIVABLE option
bar-symmetric and missing. That table was incomplete: it never considered
normalising by a single Wedderburn BLOCK weight. The corpus does exactly that,
in `phase5/phase2b_dim_v21_bridge_derivation.py:29`:

    F_Bor = |tr_M| . [3]_q! / q^3 = |tr_M| / y_(3)

with `y_lam = q^{c(lam)}/[n]_q!`, `c(lam)` the content sum. That IS an
identity -- `c((3)) = 0+1+2 = 3` -- so the exponent is not arbitrary at all: it
is the content sum of the trivial partition, and it is bar-ASYMMETRIC for a
structural reason (bar sends `lam -> lam'`, which negates `c`). This is the
first candidate that escapes the bar-symmetry wall.

THE CATCH, WHICH IS WHAT THIS PROBE MEASURES. `y_lam = q^{c(lam)}/[n]_q!` is the
q-SCHUR PLANCHEREL weight (`QOU/BraidsAndKnots/QSchurYLambdaClosedForm.lean`,
where the identification with the categorical weight is a CONJECTURE CLASS
`QSchurYLambdaClosedFormClaim`, not a theorem). The `tr_M` in `F_Bor` is the
WENZL/MARKOV trace, whose own weights are in
`y-lambda-wenzl-witness.json`. AGENTS.md states the two families are "distinct
at q != 1 -- never conflate". So the identity normalises a Markov trace by a
q-Schur weight.

Four measurements decide whether that matters, all at the proton pin:

  1. Wenzl weights + the Phase-1c character REPRODUCE the Lean-proved closed
     form for tr_M(b_Bor).  (Three independently-derived corpus objects
     agreeing -- this is the control that the Wenzl family is the right one.)
  2. q-Schur weights DO NOT.
  3. Wenzl weights are trace-normalised: sum_lam dim_lam . y_lam = 1, i.e.
     tr_M(1) = 1.  The q-Schur weights are not.
  4. 1/y^Schur_(3) IS the current factor exactly, and 1/y^Wenzl_(3) is not.

Scope-(a). This does not refute F_Bor and does not touch the Lean-proved
|tr_M(b_Bor)|. It identifies the PROVENANCE of the /q^3 and shows the
provenance is a different weight family from the trace it is applied to.

  Ref: [manuscript] prop:q-schur-y-lambda-closed-form
  Ref: [manuscript] conj:kashaev-density-equals-sdp-multiplicity
  Ref: [jones1987] Hecke algebra representations of braid groups and link
       polynomials, Ann. of Math. 126 (1987) 335-388
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "substrate"))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "qou-substrate" / "python"))

import _path_bridge  # noqa: F401, E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

import mpmath as mp  # noqa: E402
from q_parameter import Q_MP as Q0  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from qou_substrate.witness import resolve_q0_anchor  # noqa: E402

# q₀ pin, declared by the producer rather than inferred.
#
# `WitnessBuilder.build()` stamps `q0Anchor` only when `q0_anchor_is_declared()`
# is true, i.e. only when this stem is already in `q0_anchor_manifest.json`. The
# manifest is generated from the q₀ value SERIALIZED in a witness. A producer
# that reads q₀ without recording it therefore cannot bootstrap in: no stamp =>
# no manifest entry => no stamp. Declaring it here breaks that loop, and an
# explicit payload declaration wins over the resolver by design.
#
# The value comes from the SAME resolver the runtime uses, and is asserted
# against the pin this script actually computes with -- a stamp that disagrees
# with the compute is the defect `_q0_value_for_anchor`'s docstring records
# (the 2026-08-15 derive-the-muon-branch change, reverted the same day).
_Q0_ANCHOR, _Q0_VALUE = resolve_q0_anchor(__file__)
assert _Q0_VALUE is not None and str(Q0)[:14] == _Q0_VALUE[:14], (
    "q0 stamp/compute straddle: computing with "
    + str(Q0)[:16] + " but resolver says "
    + str(_Q0_ANCHOR) + " = " + _Q0_VALUE[:16]
)
_Q0_STAMP = {"q0Anchor": _Q0_ANCHOR, "q0Value": _Q0_VALUE}


VOL41 = 2 * mp.clsin(2, mp.pi / 3)

#: Partitions of 3, with their ordinary dimensions and content sums.
#: c(lam) = sum over cells (i,j) of (j - i).
PARTS = [((3,), 1, 3), ((2, 1), 2, 0), ((1, 1, 1), 1, -3)]

#: Cells of each Young diagram, 1-indexed (row, column).
CELLS = {(3,): [(1, 1), (1, 2), (1, 3)],
         (2, 1): [(1, 1), (1, 2), (2, 1)],
         (1, 1, 1): [(1, 1), (2, 1), (3, 1)]}


def _qi(n, q):
    """Balanced q-integer [n]_q = (q^n - q^-n)/(q - q^-1)."""
    return (q ** n - q ** -n) / (q - 1 / q)


def qfact3(q):
    return _qi(1, q) * _qi(2, q) * _qi(3, q)


def tr_m_lean(q):
    """The Lean-proved closed form (QOU.BraidKnot.BorromeanMarkovTrace)."""
    h = q - 1 / q
    return (4 + h ** 2 - 3 * h ** 4 - h ** 6) / (h ** 2 + 4)


def chi_21(q):
    """chi^(2,1)(beta_Bor), the Phase-1c result. chi^(3) = chi^(1,1,1) = 1."""
    return (-q ** 12 + 3 * q ** 10 - 3 * q ** 8 + 4 * q ** 6
            - 3 * q ** 4 + 3 * q ** 2 - 1) / q ** 6


def y_qschur(q):
    """q^{c(lam)} / [3]_q! -- the q-Schur Plancherel closed form."""
    f = qfact3(q)
    return {lam: q ** c / f for lam, _d, c in PARTS}


def _hook(lam, i, j):
    arm = lam[i - 1] - j
    leg = sum(1 for row in lam if row >= j) - i
    return arm + leg + 1


def _s_lambda(lam, q):
    """Fractional principal Schur specialisation, the hook-content formula.

    `s_{lam,X}(Q) = Q^{n(lam)} prod_x (1 - X Q^{c(x)}) / (1 - Q^{h(x)})`
    with `Q = q^2`, `X = q z / (1 - Q + q z)` and the convention-D Markov
    parameter `z = q^3/(q^2+1)`.  This is the formula recorded in
    `y-lambda-wenzl-witness.json`'s own `formula` field, and it is the
    literature hook-content specialisation (Stanley):
    `s_lam(1, q, ..., q^{N-1}) = q^{n(lam)} prod_x [N + c(x)] / [h(x)]`.
    """
    Q = q ** 2
    z = q ** 3 / (q ** 2 + 1)
    X = q * z / (1 - Q + q * z)
    out = Q ** sum(i * row for i, row in enumerate(lam))
    for (i, j) in CELLS[lam]:
        out *= (1 - X * Q ** (j - i)) / (1 - Q ** _hook(lam, i, j))
    return out


def y_wenzl(q):
    """The Wenzl/Markov weights, computed live at the pin passed in.

    NOT read from `y-lambda-wenzl-witness.json`: that cache was built at the
    MUON pin (2026-05-19), and reading it here while evaluating chi and tr_M at
    the proton pin is the layer straddle AGENTS.md forbids -- it showed up as a
    3.4e-12 residual in the reconstruction below, which is exactly the 11.5 ppb
    mu-p separation propagated through.  Recomputing from the witness's own
    formula reproduces it at its own pin and is exact at ours.
    """
    s_all = {lam: _s_lambda(lam, q) for lam, _d, _c in PARTS}
    total = sum(d * s_all[lam] for lam, d, _c in PARTS)
    return {lam: s_all[lam] / total for lam, _d, _c in PARTS}


def m_p_from_factor(q, N):
    """m_p = 2(m_mu . F_Bor - 6 m_e) with F_Bor = |tr_M| . N."""
    hb = (q - 1) / q
    m_mu = M_E_MEV * VOL41 / hb ** 2
    return 2 * (m_mu * tr_m_lean(q) * N - 6 * M_E_MEV)


def main() -> int:
    q = mp.mpf(Q0)
    trM = tr_m_lean(q)
    chi = {(3,): mp.mpf(1), (2, 1): chi_21(q), (1, 1, 1): mp.mpf(1)}

    yS = y_qschur(q)
    yW = y_wenzl(q)

    recon_W = sum(yW[lam] * chi[lam] for lam, _d, _c in PARTS)
    recon_S = sum(yS[lam] * chi[lam] for lam, _d, _c in PARTS)
    norm_W = sum(d * yW[lam] for lam, d, _c in PARTS)
    norm_S = sum(d * yS[lam] for lam, d, _c in PARTS)

    current = qfact3(q) / q ** 3
    inv_S3 = 1 / yS[(3,)]
    inv_W3 = 1 / yW[(3,)]
    inv_W21 = 1 / yW[(2, 1)]
    two_sq = (q + 1 / q) ** 2

    options = [
        ("writhe rule (w = 0)", mp.mpf(1), "corpus markov-axioms-primitive"),
        ("1/y^Wenzl_(3)  trivial block", inv_W3, "y-lambda-wenzl-witness"),
        ("1/y^Wenzl_(2,1) = [2]_q^2  (TL delta^(n-1))", inv_W21, "Wenzl == TL"),
        ("[3]_q!  no division", qfact3(q), "Poincare / dimension"),
        ("1/y^Schur_(3) = [3]_q!/q^3  CURRENT", inv_S3, "q-Schur Plancherel"),
    ]

    b = (
        WitnessBuilder("fbor-q3-is-qschur-plancherel-weight", engine="mpmath")
        .set_description(
            "Identifies the provenance of F_Bor's /q^3: it is 1/y_(3) for the "
            "q-SCHUR Plancherel weight y_lam = q^{c(lam)}/[n]_q!, whose "
            "exponent at lam = (3) is the content sum 0+1+2 = 3. Measures that "
            "this is a DIFFERENT weight family from the Wenzl/Markov weights "
            "that actually decompose the tr_M appearing in F_Bor: the Wenzl "
            "weights reproduce the Lean closed form and are trace-normalised, "
            "the q-Schur ones do neither."
        )
        .set_audit_only("docs/audits/2026-06-24-fbor-q3-exact-habiro-ratio-fit.md")
        .add_parameter("q_0", str(q))
        .add_parameter("q0_pin", "proton (m_p/m_e)")
        .add_parameter("markov_convention", "D  (z = q^3/(q^2+1))")
    )

    b.add_data("reconstruction", {
        "tr_M_lean_closed_form": mp.nstr(trM, 30),
        "sum_y_wenzl_chi": mp.nstr(recon_W, 30),
        "sum_y_qschur_chi": mp.nstr(recon_S, 30),
        "wenzl_abs_residual": mp.nstr(abs(recon_W - trM), 10),
        "qschur_abs_residual": mp.nstr(abs(recon_S - trM), 10),
    })
    b.add_data("trace_normalisation_sum_dim_times_y", {
        "wenzl": mp.nstr(norm_W, 30),
        "qschur": mp.nstr(norm_S, 30),
        "note": "must be 1: it is tr_M(identity), the Markov normalisation",
    })
    b.add_data("the_factor", {
        "current_[3]_q!_over_q3": mp.nstr(current, 30),
        "one_over_y_qschur_(3)": mp.nstr(inv_S3, 30),
        "one_over_y_wenzl_(3)": mp.nstr(inv_W3, 30),
        "one_over_y_wenzl_(2,1)": mp.nstr(inv_W21, 30),
        "two_bracket_squared": mp.nstr(two_sq, 30),
        "content_sum_of_(3)": 3,
    })
    b.add_data("options", [
        {"option": nm, "N": mp.nstr(N, 20), "source": src,
         "m_p_MeV": mp.nstr(m_p_from_factor(q, N), 15)}
        for nm, N, src in options
    ])

    # (1)(2) which family decomposes the trace that F_Bor actually uses
    b.add_assertion("wenzl_weights_reproduce_the_lean_trM",
                    computed=bool(abs(recon_W - trM) < mp.mpf("1e-30")),
                    expected=True)
    b.add_assertion("qschur_weights_do_not_reproduce_the_lean_trM",
                    computed=bool(abs(recon_S - trM) > mp.mpf("0.3")),
                    expected=True)
    # (3) the Markov normalisation tr_M(1) = 1
    b.add_assertion("wenzl_weights_are_trace_normalised",
                    computed=bool(abs(norm_W - 1) < mp.mpf("1e-30")),
                    expected=True)
    b.add_assertion("qschur_weights_are_not_trace_normalised",
                    computed=bool(abs(norm_S - 1) > mp.mpf("0.3")),
                    expected=True)
    # (4) the factor IS the q-Schur trivial-block weight, and is NOT the Wenzl one
    b.add_assertion("current_factor_equals_one_over_qschur_trivial_weight",
                    computed=bool(abs(current - inv_S3) < mp.mpf("1e-40")),
                    expected=True)
    b.add_assertion("current_factor_differs_from_one_over_wenzl_trivial_weight",
                    computed=bool(abs(current - inv_W3) > mp.mpf("2")),
                    expected=True)
    # the collapse: block-normalisation by the standard rep IS the TL option
    b.add_assertion("wenzl_standard_block_weight_is_inverse_two_bracket_squared",
                    computed=bool(abs(inv_W21 - two_sq) < mp.mpf("1e-40")),
                    expected=True)
    # the bar-partner of the trivial block is not available as a normaliser
    b.add_assertion("wenzl_sign_block_weight_vanishes_in_convention_D",
                    computed=bool(abs(yW[(1, 1, 1)]) < mp.mpf("1e-40")),
                    expected=True)
    b.save(_Q0_STAMP)

    print("=" * 74)
    print("F_Bor's /q^3 = 1/y_(3) -- but for WHICH weight family?")
    print("=" * 74)
    print(f"  q_0 (proton pin)                = {mp.nstr(q, 20)}")
    print()
    print("  Does sum_lam y_lam . chi^lam(beta_Bor) give the Lean tr_M?")
    print(f"    tr_M (Lean closed form)       = {mp.nstr(trM, 20)}")
    print(f"    Wenzl  weights                = {mp.nstr(recon_W, 20)}"
          f"   residual {mp.nstr(abs(recon_W - trM), 6)}")
    print(f"    q-Schur weights               = {mp.nstr(recon_S, 20)}"
          f"   residual {mp.nstr(abs(recon_S - trM), 6)}")
    print()
    print("  Trace normalisation  sum_lam dim_lam . y_lam  (must be 1):")
    print(f"    Wenzl                         = {mp.nstr(norm_W, 20)}")
    print(f"    q-Schur                       = {mp.nstr(norm_S, 20)}")
    print()
    print("  The factor:")
    print(f"    [3]_q! / q^3      (in use)    = {mp.nstr(current, 20)}")
    print(f"    1 / y^Schur_(3)               = {mp.nstr(inv_S3, 20)}   <- same")
    print(f"    1 / y^Wenzl_(3)               = {mp.nstr(inv_W3, 20)}")
    print(f"    1 / y^Wenzl_(2,1)             = {mp.nstr(inv_W21, 20)}")
    print(f"    [2]_q^2                       = {mp.nstr(two_sq, 20)}   <- same")
    print()
    print("  Options, scored on m_p:")
    for nm, N, src in options:
        v = m_p_from_factor(q, N)
        print(f"    {nm:<44} N={mp.nstr(N, 12):>16}"
              f"  m_p={mp.nstr(v, 12):>15}")
    print()
    print("  => /q^3 is the q-Schur Plancherel weight of the TRIVIAL block.")
    print("     Its exponent is the content sum c((3)) = 0+1+2 = 3, and it is")
    print("     bar-asymmetric because bar sends lam -> lam', negating c.")
    print("     But it is applied to the WENZL/Markov trace, whose own weights")
    print("     reproduce tr_M and are trace-normalised where the q-Schur ones")
    print("     are neither. The factor is a cross-family import.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
