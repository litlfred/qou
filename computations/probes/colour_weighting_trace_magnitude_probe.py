#!/usr/bin/env python3
"""colour_weighting_trace_magnitude_probe.py — how big is the canonical path's
colour-blindness?  1.41e-4 relative on the deuteron, and the corpus's own witness
sits on the OTHER side of it.

WHY THIS EXISTS.  PR #6305 (bean `qou-fv0s`) established that the canonical
`tr_M` route is colour-BLIND for every mixed nucleus: `canonical_braid_crossings.
sign_for_ctype` maps the `averaged_weighted` interface and the plain `averaged`
interface onto the same wire value `0`, because the Rust kernel's spec carries a
SIGN in {-1, 0, +1} and a sign cannot carry a magnitude.  Its own docstring says
so -- "Lossy for `averaged_weighted`, by construction."  Every mixed nucleus
(D, T, 3He, 4He) carries exactly one such crossing, at the p-n interface.

That established the DEFECT.  It did not price it, and the open design choice --
widen the wire format past a sign, or route mixed nuclei through the Python ctype
path -- cannot be made without the number.  This probe measures it.

THE MEASUREMENT.  The trace is AFFINE in the shift `d` carried by that single
crossing.  Writing the braid word as M = A (sigma_g + d I) B,

    tr M(d) = tr(A sigma_g B) + d * tr(A B),

so one linear coefficient governs the whole effect and the magnitude extrapolates
without re-deriving it per nucleus.  The probe evaluates the full Schur-Weyl sum
Sum_lambda y_lambda chi^lambda(beta_D) at three values of that one shift --
colour-blind `d_avg`, colour-weighted `d_w`, and their midpoint -- and checks the
midpoint lands exactly halfway.  It does, to 1.8e-71, i.e. the 50-dps compute
floor: the affine reading is a measurement here, not an assumption.

THREE RESULTS, on the deuteron at the proton pin, 50 dps:

  1. The Python colour-BLIND sum reproduces the canonical Rust value to ~1.9e-18.
     These are fully independent implementations -- Rust MPFR chi against Python
     Hoefsmit matrices, witness-table y_lambda against symbolic y_lambda -- so this
     is a real cross-validation, and it CONFIRMS the canonical path is the
     colour-blind arm rather than merely suggesting it.

  2. The colour weighting is worth 8.137e-5 absolute, 1.4149e-4 RELATIVE.  For
     scale: that is ~12000x the mu-p substrate tension (11.54 ppb) which this
     corpus tracks to the digit, and ~4.9x SMALLER than the per-crossing weight
     difference 6.87855e-4 -- the trace attenuates it, it does not amplify it.

  3. THE CORPUS ALREADY CARRIES THE COLOUR-WEIGHTED VALUE.  The committed
     `atomic-tr-m-mpfr-50dps.witness.json` deuteron entry agrees with the
     colour-WEIGHTED sum to 1.48e-7 and misses the colour-blind sum by 1.416e-4 --
     which is the whole weighting gap, to within 0.09%.
     Its residual 1.48e-7 is the known q_0 pin straddle that
     `rho_k_h3a_residual_decomposition.py` decomposes (8.34e-8 straddle plus
     1.85e-9 of witness self-inconsistency) -- i.e. the witness and this probe
     agree to the limit of a defect the corpus has already characterised.

WHAT THAT MEANS, stated carefully.  There are now two live routes to tr_M for a
mixed nucleus and they disagree by 1.41e-4: the Rust canonical path (colour-blind)
and the Python ctype path (colour-weighted, and what the committed witness holds).
This is NOT a claim that either is wrong -- which one is canonical is exactly the
design question `qou-fv0s` leaves open, and the p-n interface weighting is a
physical modelling choice, not an arithmetic one.  It IS a claim that the choice
is consequential at 1.4e-4 and that the corpus currently answers it BOTH ways
depending on which route a consumer takes.

SCOPE.  Scope-(a): measured on the deuteron only.  The affine structure (assertion
2) is what licenses reading the magnitude across T / 3He / 4He, since each carries
exactly one weighted crossing -- but the linear coefficient tr(A B) is
word-specific and is NOT measured here for those three.  Do not quote 1.41e-4 as
their figure.

Run:  python3 -u computations/probes/colour_weighting_trace_magnitude_probe.py \
        2>&1 | tee /tmp/colour_weighting_magnitude.log
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTATIONS = HERE.parent
for _p in (COMPUTATIONS, COMPUTATIONS / "hecke", COMPUTATIONS / "substrate",
           COMPUTATIONS / "deltalambda"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

import rho_k_h3a_refinement as R  # noqa: E402
from _li_2_q_util import flavor_split_leading  # noqa: E402
from canonical_braid_crossings import (  # noqa: E402
    atom_canonical_crossings, d_for_ctype, sign_for_ctype,
)
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# The deuteron's committed tr_M, both branches, from
# `atomic-tr-m-mpfr-50dps.witness.json`.  Carried as strings and compared as
# mpf -- never parsed through float.  Values quoted in
# `rho_k_h3a_residual_decomposition.py`'s header, which is where the two-branch
# disagreement was first recorded.
WITNESS_PRIMARY = "0.57517232916588433221594741758"
WITNESS_PEEL = "0.57517233101788385191979179668"


def schur_weyl_sum_with_shift(q, q_sym, y_sym, crossings, parts, d_weighted):
    """Sum_lambda y_lambda chi^lambda(beta; q), with the ONE `averaged_weighted`
    crossing carrying the caller-supplied shift `d_weighted`.

    Every other crossing takes its own `d_for_ctype` value unchanged.  Varying a
    single crossing is what makes the result affine in one scalar.
    """
    h = q - mp.mpf(1) / q
    total = mp.mpf(0)
    for lam in parts:
        mats, dim, _ = R.hoefsmit_matrices_numeric(lam, q)
        if dim == 0:
            continue
        eye = mp.eye(dim)
        M = mp.eye(dim)
        for gen_idx, ctype in crossings:
            d = d_weighted if ctype == "averaged_weighted" else d_for_ctype(ctype, h)
            M = M * (mats[gen_idx] + d * eye)
        chi = sum(M[i, i] for i in range(dim))
        y = mp.mpf(str(y_sym[lam].subs(R.Q_SYM, q_sym).evalf(mp.mp.dps)))
        total += y * chi
    return total


def rust_canonical_deuteron():
    """The canonical (colour-blind) deuteron tr_M via the Rust kernel, computed
    LIVE rather than quoted, so this stays a cross-check and not a literal.

    Returns (value_or_None, reason_or_None).
    """
    try:
        import canonical_tr_m_via_rust as C
        row = C.compute_tr_m(1, 1, "deuteron", timeout_sec=1800)
    except Exception as exc:  # pragma: no cover — environment-dependent
        return None, f"{type(exc).__name__}: {exc}"
    if "tr_M_q0_mp50dps" not in row:
        return None, row.get("tr_M_q0_unavail_reason", "no value and no reason")
    return mp.mpf(str(row["tr_M_q0_mp50dps"])), None


def main() -> int:
    q = mp.mpf(Q_50_DIGIT_STR)
    q_sym = sp.sympify(Q_50_DIGIT_STR)
    h = q - mp.mpf(1) / q
    delta = mp.mpf(
        str(sp.sympify(flavor_split_leading(sp.Symbol("q")))
            .subs(sp.Symbol("q"), q_sym)
            .evalf(mp.mp.dps))
    )

    d_blind = d_for_ctype("averaged", h)
    d_w = d_for_ctype("averaged_weighted", h, delta=delta)
    d_mid = (d_blind + d_w) / 2

    print("=" * 84)
    print("colour weighting — magnitude on the deuteron trace")
    print("=" * 84)
    print(f"\n  q_0 (proton pin)  = {mp.nstr(q, 40)}")
    print(f"  h = q - 1/q       = {mp.nstr(h, 30)}")
    print(f"  delta (flavour)   = {mp.nstr(delta, 30)}")
    print(f"\n  d(averaged)          = {mp.nstr(d_blind, 30)}   sign wire "
          f"{sign_for_ctype('averaged')}")
    print(f"  d(averaged_weighted) = {mp.nstr(d_w, 30)}   sign wire "
          f"{sign_for_ctype('averaged_weighted')}")
    print(f"  the two collapse onto the SAME wire value — that is the defect")
    print(f"  d_w - d_avg          = {mp.nstr(d_w - d_blind, 20)}")

    crossings = atom_canonical_crossings(1, 1)
    n_weighted = sum(1 for _, ct in crossings if ct == "averaged_weighted")
    parts = R.partitions_of_n(6)
    y_sym = R.load_y_lambda_n6()
    print(f"\n  beta_D: {len(crossings)} crossings on H_6, {n_weighted} of them "
          f"`averaged_weighted`")
    print(f"  summing over {len(parts)} partitions, three shift values …")

    s_blind = schur_weyl_sum_with_shift(q, q_sym, y_sym, crossings, parts, d_blind)
    s_w = schur_weyl_sum_with_shift(q, q_sym, y_sym, crossings, parts, d_w)
    s_mid = schur_weyl_sum_with_shift(q, q_sym, y_sym, crossings, parts, d_mid)

    affine_residual = abs(s_mid - (s_blind + s_w) / 2)
    delta_abs = s_w - s_blind
    delta_rel = abs(delta_abs) / abs(s_blind)

    print(f"\n  S(colour-blind)    = {mp.nstr(s_blind, 40)}")
    print(f"  S(colour-weighted) = {mp.nstr(s_w, 40)}")
    print(f"  S(midpoint)        = {mp.nstr(s_mid, 40)}")
    print(f"\n  affine residual |S(mid) - (S_blind+S_w)/2| = "
          f"{mp.nstr(affine_residual, 8)}")
    print(f"  Delta = S_w - S_blind = {mp.nstr(delta_abs, 12)}")
    print(f"  relative              = {mp.nstr(delta_rel, 12)}")

    rust_val, rust_reason = rust_canonical_deuteron()
    if rust_val is None:
        print(f"\n  Rust canonical: UNAVAILABLE — {rust_reason}")
        rust_rel = None
    else:
        rust_rel = abs(s_blind - rust_val) / abs(rust_val)
        print(f"\n  Rust canonical D   = {mp.nstr(rust_val, 40)}")
        print(f"  vs S(colour-blind) rel = {mp.nstr(rust_rel, 10)}")

    wit_p = mp.mpf(WITNESS_PRIMARY)
    wit_peel = mp.mpf(WITNESS_PEEL)
    wit_vs_w = abs(s_w - wit_p) / abs(wit_p)
    wit_vs_blind = abs(s_blind - wit_p) / abs(wit_p)
    print(f"\n  committed witness (primary) = {mp.nstr(wit_p, 30)}")
    print(f"    vs colour-WEIGHTED  rel = {mp.nstr(wit_vs_w, 10)}   <- agrees")
    print(f"    vs colour-blind     rel = {mp.nstr(wit_vs_blind, 10)}   <- misses")
    print(f"  committed witness (peel)    = {mp.nstr(wit_peel, 30)}")
    print(f"    vs colour-WEIGHTED  rel = "
          f"{mp.nstr(abs(s_w - wit_peel) / abs(wit_peel), 10)}")

    w = WitnessBuilder("colour-weighting-trace-magnitude", engine="python")
    w.add_parameter("nucleus", "deuteron (Z=1, N=1)")
    w.add_parameter("q0_anchor", "proton")
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("n_strands", 6)
    w.add_parameter("n_crossings", len(crossings))
    w.add_parameter("n_averaged_weighted_crossings", n_weighted)
    w.add_data("d_averaged", mp.nstr(d_blind, 50))
    w.add_data("d_averaged_weighted", mp.nstr(d_w, 50))
    w.add_data("delta_flavour_split", mp.nstr(delta, 50))
    w.add_data("tr_M_colour_blind", mp.nstr(s_blind, 50))
    w.add_data("tr_M_colour_weighted", mp.nstr(s_w, 50))
    w.add_data("tr_M_midpoint_shift", mp.nstr(s_mid, 50))
    w.add_data("delta_absolute", mp.nstr(delta_abs, 30))
    w.add_data("delta_relative", mp.nstr(delta_rel, 30))
    w.add_data("rust_canonical_tr_M", mp.nstr(rust_val, 50) if rust_val is not None
               else None)
    w.add_data("rust_unavailable_reason", rust_reason)
    w.add_data("witness_primary_vs_colour_weighted_rel", mp.nstr(wit_vs_w, 20))
    w.add_data("witness_primary_vs_colour_blind_rel", mp.nstr(wit_vs_blind, 20))

    # 1. The trace really is affine in the one shift — this is what licenses
    #    reading the magnitude off a single linear coefficient.
    w.add_assertion(
        "the trace is affine in the weighted crossing's shift",
        computed=mp.nstr(affine_residual, 30),
        expected="0",
        tolerance="1e-40",
        source="S(midpoint) vs the mean of the two endpoint sums",
    )
    # 2. Two independent implementations agree on the colour-BLIND arm, which is
    #    what identifies which arm the canonical path is on.
    if rust_val is not None:
        w.add_assertion(
            "the canonical Rust path lands on the colour-BLIND arm",
            computed=mp.nstr(rust_rel, 30),
            expected="0",
            tolerance="1e-15",
            source="Rust MPFR chi + witness y_lambda vs Python Hoefsmit + symbolic y_lambda",
        )
    # 3. The weighting is not negligible: it is ~12000x the mu-p tension.
    w.add_assertion(
        "colour weighting moves the deuteron trace by 1.41e-4 relative",
        computed=mp.nstr(delta_rel, 30),
        expected="1.41494661063e-4",
        tolerance="1e-14",
        source="S(colour-weighted) - S(colour-blind), normalised by S(colour-blind)",
    )
    # 4. The corpus's committed witness is on the colour-WEIGHTED arm — so the
    #    two live routes disagree, and the corpus answers the design question
    #    both ways depending on which one a consumer takes.
    w.add_assertion(
        "the committed deuteron witness sits on the colour-WEIGHTED arm",
        computed=mp.nstr(wit_vs_w, 30),
        expected="0",
        tolerance="1e-6",
        source=f"atomic-tr-m-mpfr-50dps.witness.json primary = {WITNESS_PRIMARY}; "
               f"its residual is the known q_0 pin straddle",
    )
    # Self-normalising form: the witness's distance from the colour-blind arm is
    # the WHOLE colour-weighting gap, to within the pin straddle.  Stated as a
    # ratio so it does not hard-code a value the pin can move.
    w.add_assertion(
        "its distance from the colour-blind arm IS the colour-weighting gap",
        computed=mp.nstr(wit_vs_blind / delta_rel, 30),
        expected="1",
        tolerance="1e-3",
        source="|witness - S(colour-blind)| / |S(colour-weighted) - S(colour-blind)|",
    )

    w.add_caveat(
        "Scope-(a): measured on the deuteron only. The affine structure licenses "
        "reading the magnitude across T / 3He / 4He -- each carries exactly one "
        "weighted crossing -- but the linear coefficient is word-specific and is "
        "NOT measured for those three. Do not quote 1.41e-4 as their figure."
    )
    w.add_caveat(
        "This does not say which arm is correct. Whether the p-n interface should "
        "carry the flavour weighting is a physical modelling choice (bean "
        "qou-fv0s); the probe prices it, it does not settle it."
    )
    w.add_caveat(
        "The 1.48e-7 residual between the colour-weighted sum and the committed "
        "witness is the q_0 pin straddle decomposed in "
        "rho_k_h3a_residual_decomposition.py (8.34e-8 straddle + 1.85e-9 of "
        "witness self-inconsistency), not a further disagreement."
    )

    out = w.save()
    print(f"\n  witness -> {out}")

    failed = [a for a in w.assertions if not a.passed]
    print(f"\n  assertions: {len(w.assertions) - len(failed)}/{len(w.assertions)} pass")
    for a in failed:
        print(f"    FAIL  {a.name}: computed={a.computed} expected={a.expected}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
