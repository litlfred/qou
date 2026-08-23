"""General-n Jacobi–Anger tower test — RECONCILED to the §4a physical-weight object.

Path A of `docs/audits/2026-06-17-jacobi-anger-physical-weight-n3.md`: extend the
§4a single-x q-Bessel over-determination test up the brane tower, to see whether the
bar-odd tower residual → 0 as n grows.

## Tower-object reconciliation — RESOLVED (2026-06-18)

The prior WIP build of this harness used the WRONG tower object: the min-norm
autocorrelation `F(q)=Σ_w t_w·τ_M(T_w)(q)` (= `τ_M(T_β)` for `T_β∝t`, the SDP
shape-collapse fit), which gave a residual much larger than #2453's physical-weight
6.8% at n=3. That object diverges from §4a on TWO counts; both are now fixed:

1. **Wrong element.** §4a's bar-odd data is `χ_λ(𝓑_n − 𝓑_p)` — the EXPLICIT
   typed-`B₃` neutron-minus-proton braid difference (`𝓑_p` = uud, `𝓑_n` = udd;
   content block `chi-per-irrep-cyclotomic-closed-forms.md`), whose per-block closed
   forms are **Lean-proved sorry-free** (`chi-per-irrep-cyclotomic-closed-forms.lean`,
   `field_simp + ring`). It is NOT the min-norm `T_β∝t` SDP fit. (This corrects the
   prior "the tower object is fit-derived" critical-distance note, which mis-traced
   `qbeta_per_block_symbolic.py`'s min-norm `χ_λ(T_β)` — a different object — instead
   of `qbeta_per_block_paper_closed_forms.py`'s explicit `χ_λ(𝓑_n − 𝓑_p)`.)

2. **y must be FROZEN at q₀.** §4a's canonical form (audit §3 dictionary row, scope
   §9.2) is the brane-tower level sum `Σ_ℓ w_ℓ sinh(ℓη)` with CONSTANT weights
   `w_ℓ = Σ_λ y_λ(q₀)·coeff_{λ,ℓ}` — the Bessel test `w_ℓ = 2 J_ℓ(x)` requires
   η-independent `w_ℓ`, which forces the Markov weights `y_λ(q₀)` to be substrate-
   fixed. The autocorrelation re-evaluated `y_λ(e^η)` along the bar-deformation,
   producing η-dependent coefficients that cannot be read as a clean `Σ_ℓ w_ℓ sinh`.

This harness now builds the CORRECT object and reproduces 6.8% at n=3:

    χ_λ(𝓑_n − 𝓑_p)(q)        ← proved closed forms (sympy; cross-checked vs Lean)
    coeff_{λ,ℓ} := barodd_ℓ[χ_λ(e^η)]   (q-independent rationals; q=e^η)
    W_ℓ(q₀) = Σ_λ y_λ(q₀)·coeff_{λ,ℓ}   ← y FROZEN at the substrate anchor
    solve x from W_3/W_1 = J_3(x)/J_1(x); over-determine on W_5/W_1.

`reconcile_n3()` asserts the resulting residual equals the physical-weight script's
at BOTH anchors — the general harness and `qbeta_reeb_tower_jacobi_anger_
physical_weight.py` compute the same object. The reference is read from that
script LIVE, not copied: it was 0.0684 under convention C and is 0.142709 under
the convention D the registry has used since the 2026-08-09 owner ruling, and the
two harnesses agree on the new value exactly as they did on the old one. See
`reference_residual_at` for why the literal was removed.

## Tower extension (n ≥ 6) — the real, corrected blocker

The orders {7, 9, …} the q-Bessel object needs live at λ ⊢ 6, 9 (more strands). The
gate is: recompute the single-x residual with the same y-frozen rule at n = 6, 9, 12;
**shrinks → 0 monotonically** ⇒ the bar-odd tower IS the q-Bessel contraction object;
**plateaus/grows** ⇒ clean refutation.

The blocker is NOT "extend the SDP selector" (that extends a fit). It is **first-
principles**: produce `χ_λ(𝓑_n − 𝓑_p)` at λ ⊢ 6, 9 by embedding the typed-crossings
proton/neutron braids `𝓑_p`, `𝓑_n` at brane-tower levels 6, 9 (Path B-adjacent), then
`bar_odd_coeffs` + `physical_W` + `single_x_residual` below apply UNCHANGED. There is
no such braid (nor proved closed form) in the corpus today — the typed-braid character
infra is in `computations/_deprecated/`. So n=3 is the furthest the gate advances
without the first-principles higher-tower braids, and this script pins exactly what
unblocks the rest.

`validate_markov_infra()` (optional; needs `pyhecke_native`) confirms the general-n
Markov-trace machinery `τ_M(T_w)=Σ_λ y_λ χ_λ(T_w)` reproduces the hardcoded `gram.TR_M`
at n=3 — that machinery is correct and ready to consume the higher-tower braids once
they exist; it was only the autocorrelation OBJECT built on it that was wrong.

Discipline: derive-or-refute (the ratio solve is an over-determination check, not a
fit); TIERED; nothing wired; c_3/Q_β stay cal-anchored.

Ref: docs/audits/2026-06-17-jacobi-anger-physical-weight-n3.md
Ref: docs/audits/2026-06-13-reeb-phase-qbessel-identification.md §4a
Ref: content/quantum-observable-universe/mass-endomorphism/chi-per-irrep-cyclotomic-closed-forms.md
Ref: computations/qbeta/qbeta_per_block_paper_closed_forms.py
Ref: computations/qbeta/qbeta_reeb_tower_jacobi_anger_physical_weight.py
"""
from __future__ import annotations

import sys
from fractions import Fraction as Fr
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402, F401

import sympy as sp  # noqa: E402
from mpmath import mp, mpf, besselj, findroot  # noqa: E402

from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

try:
    from qou_substrate.constants import q_at, q_muon_at
except Exception:  # pragma: no cover
    from substrate.qou_substrate.constants import q_at, q_muon_at  # type: ignore

set_compute_dps()

# Physical-weight reference to reconcile against (n=3, both anchors).
#
# COMPUTED LIVE, not frozen. This used to be `mpf("0.0683508")`, copied from
# qbeta_reeb_tower_jacobi_anger_physical_weight.py / PR #2453 — and it rotted,
# silently, for the reason a copied number always does.
#
# What happened: the owner ruling of 2026-08-09 excised convention C from the
# binding channel (`wedderburn_jones_markov.y_lambda_at` docstring; commits
# 33a6c7aa4, 36844baad). Under C, y_λ(3,q₀) = (0.4153958, 0.2809296, 0.0227449);
# under D it is (0.5054042, 0.2472979, 0) — the defining difference being the row
# cap y_λ = 0 for ℓ(λ) > 2. W_3 is unchanged at −1/4, but the weight redistributes
# between W_1 and W_5 (0.1404648 / −0.1095352 under C, 0.1236489 / −0.1263511
# under D, both still summing to 1/4), which moves x* from 4.5249 to 4.4316 and
# the over-determination residual from 0.0683508 to 0.142709.
#
# The frozen literal made that look like a broken reconciliation. It is not: the
# two harnesses still agree exactly. Re-running the reference script today under
# convention D gives 0.142709 at BOTH anchors, which is precisely what this one
# now computes. Verified by running it, not by reading it.
#
# So the check is wired to the source rather than to a copy of the source's
# output. `physical_W` / `solve_single_x` are imported from the reference script
# itself and evaluated at the SAME anchor as the value under test — strictly
# stronger than the old single shared constant, since it compares per anchor, and
# no convention change can ever make this stale again.
#
# What this assertion does and does not claim: it is an AGREEMENT check between
# two independent implementations of the same §4a object, exactly as the module
# docstring says ("the general harness and qbeta_reeb_tower_jacobi_anger_
# physical_weight.py now compute the same object"). It is NOT a claim that the
# physics succeeds. The reference script's own verdict is and remains a
# refutation: "physical weights do NOT collapse to a single-x q-Bessel at <1% —
# refutation, quantified".
from qbeta_reeb_tower_jacobi_anger_physical_weight import (  # noqa: E402
    physical_W as _reference_physical_W,
    solve_single_x as _reference_solve_single_x,
)

#: Convention-C value, retained ONLY as the historical record of what the frozen
#: literal was and when it stopped being true. Never compared against.
PHYSICAL_WEIGHT_RESIDUAL_N3_CONVENTION_C_HISTORICAL = mpf("0.0683508")


def reference_residual_at(q0):
    """The physical-weight script's own over-determination residual at `q0`.

    Calls into `qbeta_reeb_tower_jacobi_anger_physical_weight` rather than
    reproducing it: if the two ever diverge, this test is the thing that is
    supposed to notice.
    """
    _x_ref, resid_ref = _reference_solve_single_x(_reference_physical_W(q0))
    return resid_ref

# Hardcoded n=3 bar-odd coeffs from the physical-weight script — cross-check target.
HARDCODED_BAR_ODD_N3 = {
    (3,):      {3: Fr(-1, 4), 5: Fr(-1, 4)},
    (2, 1):    {1: Fr(1, 2), 3: Fr(-1, 2)},
    (1, 1, 1): {3: Fr(-1, 4), 5: Fr(-1, 4)},
}


def chi_diff_closed_forms(q):
    """Proved per-Wedderburn-block character differences χ_λ(𝓑_n) − χ_λ(𝓑_p)(q) at H₃.

    First-principles: 𝓑_p (uud), 𝓑_n (udd) are the canonical typed-`B₃` braids of the
    content block `chi-per-irrep-cyclotomic-closed-forms.md`; these closed forms are
    Lean-proved sorry-free (`chi-per-irrep-cyclotomic-closed-forms.lean`). Single source
    of truth mirrored from `qbeta_per_block_paper_closed_forms.py`.
    """
    return {
        (3,):      -(q**2 + 1)**2 * (q**2 - 1) / (4 * q),
        (2, 1):    -(q**4 + 1) * (q**2 - 1) / (4 * q**3),
        (1, 1, 1): -(q**2 + 1)**2 * (q**2 - 1) / (4 * q**5),
    }


def bar_odd_coeffs(chi_diff, n_max_order=24):
    """Bar-odd sinh-decomposition coefficients of each closed form.

    For a Laurent polynomial f(q)=Σ_k a_k q^k with q=e^η,
        barodd[f](η) = [f(e^η) − f(e^{−η})]/2 = Σ_{ℓ>0} (a_ℓ − a_{−ℓ}) sinh(ℓη).
    Returns {λ: {ℓ: sympy.Rational}} (only nonzero orders).
    """
    q = sp.Symbol("q", positive=True)
    out = {}
    N = n_max_order  # shift to clear negative powers
    for lam, f in chi_diff.items():
        g = sp.expand(sp.together(f) * q**N)
        poly = sp.Poly(g, q)
        coeffs = {}
        for ell in range(1, N + 1):
            a_pos = poly.coeff_monomial(q**(ell + N))
            a_neg = poly.coeff_monomial(q**(N - ell)) if (N - ell) >= 0 else 0
            c = sp.nsimplify(a_pos - a_neg)
            if c != 0:
                coeffs[ell] = c
        out[lam] = coeffs
    return out


def physical_W(q0, coeffs):
    """Physical Wenzl-weighted bar-odd tower coefficients, y FROZEN at q₀.

    W_ℓ = Σ_λ y_λ(q₀) · coeff_{λ,ℓ}.  q0 is an mpf anchor (proton or muon).
    """
    y = {tuple(k): mpf(str(v)) for k, v in y_lambda_at(3, q0).items()}
    W: dict[int, "mpf"] = {}
    for lam, cks in coeffs.items():
        yl = y[lam]
        for ell, c in cks.items():
            cr = sp.Rational(c)
            W[ell] = W.get(ell, mpf(0)) + yl * (mpf(int(cr.p)) / mpf(int(cr.q)))
    return W


def single_x_residual(W):
    """Solve x from the scale-free W_3/W_1 = J_3(x)/J_1(x); over-determine on W_5/W_1.

    Returns (x, over-determination relative residual).
    """
    r31 = W[3] / W[1]

    def f(x):
        return besselj(3, x) / besselj(1, x) - r31

    x = None
    for x0 in [mpf("1"), mpf("2.5"), mpf("4.44"), mpf("6"), mpf("8")]:
        try:
            cand = findroot(f, x0)
            if abs(cand.imag) < mpf("1e-30") and cand.real > 0:
                x = cand.real
                break
        except Exception:
            continue
    if x is None or 5 not in W:
        return x, None
    pred_51 = besselj(5, x) / besselj(1, x)
    act_51 = W[5] / W[1]
    resid = abs(pred_51 - act_51) / abs(act_51)
    return x, resid


def cross_check_coeffs(derived):
    """Assert the symbolically-derived bar-odd coeffs equal the hardcoded n=3 set."""
    ok = True
    for lam, hard in HARDCODED_BAR_ODD_N3.items():
        got = derived.get(lam, {})
        hard_sp = {k: sp.Rational(v.numerator, v.denominator) for k, v in hard.items()}
        if got != hard_sp:
            ok = False
            print(f"    MISMATCH {lam}: derived={got} hardcoded={hard_sp}")
    return ok


def reconcile_n3():
    """Build the CORRECT §4a object (χ_λ(𝓑_n−𝓑_p), y-frozen) and reproduce the
    physical-weight script's residual — 0.142709 under convention D."""
    q = sp.Symbol("q", positive=True)
    chi = chi_diff_closed_forms(q)
    derived = bar_odd_coeffs(chi)

    print("  bar-odd coeffs (symbolic, derived from proved χ_λ(𝓑_n−𝓑_p) closed forms):")
    for lam, cks in derived.items():
        print(f"    {str(lam):10s} {dict(sorted(cks.items()))}")
    coeffs_ok = cross_check_coeffs(derived)
    print(f"  derived ≡ hardcoded physical-weight BAR_ODD_COEFFS: "
          f"{'YES ✓' if coeffs_ok else 'NO ✗'}")
    print("-" * 78)

    anchors = {"proton": q_at(), "muon": q_muon_at()}
    results = {}
    reconcile_ok = True
    for label, qf in anchors.items():
        q0 = mpf(str(qf))
        W = physical_W(q0, derived)
        x, resid = single_x_residual(W)
        resid_ref = reference_residual_at(q0)
        match = (resid is not None and resid_ref is not None
                 and abs(resid - resid_ref) < mpf("1e-4"))
        reconcile_ok = reconcile_ok and match
        results[label] = {
            "q": mp.nstr(q0, 20),
            "W1": mp.nstr(W[1], 12), "W3": mp.nstr(W[3], 12), "W5": mp.nstr(W[5], 12),
            "single_x": (mp.nstr(x, 12) if x is not None else None),
            "overdet_rel_residual": (mp.nstr(resid, 6) if resid is not None else None),
            "physical_weight_reference_residual": (
                mp.nstr(resid_ref, 6) if resid_ref is not None else None),
            "matches_physical_weight_reference": bool(match),
        }
        print(f"  {label:7s} q={mp.nstr(q0, 18)}")
        print(f"          W_1={mp.nstr(W[1], 10)}  W_3={mp.nstr(W[3], 10)}  "
              f"W_5={mp.nstr(W[5], 10)}")
        print(f"          single x*={mp.nstr(x, 10) if x else 'NO ROOT'}  "
              f"over-det residual={mp.nstr(resid, 6) if resid is not None else 'n/a'}  "
              f"[matches physical-weight reference "
              f"{mp.nstr(resid_ref, 6) if resid_ref is not None else 'n/a'}: "
              f"{'YES' if match else 'NO'}]")

    if results["proton"]["single_x"] and results["muon"]["single_x"]:
        xp = mpf(results["proton"]["single_x"])
        xm = mpf(results["muon"]["single_x"])
        swing = abs(xp - xm) / abs(xp)
        results["cross_anchor_x_swing_rel"] = mp.nstr(swing, 6)
        print(f"  cross-anchor single-x swing (rel) = {mp.nstr(swing, 6)}")

    return derived, results, coeffs_ok, reconcile_ok


def validate_markov_infra():
    """OPTIONAL: general-n Markov-trace machinery τ_M(T_w)=Σ_λ y_λ χ_λ(T_w) vs gram.TR_M.

    This is the (correct, validated) infra that will consume the higher-tower braids
    once `χ_λ(𝓑_n−𝓑_p)` exists at n=6,9. Needs `pyhecke_native`; skipped if absent.
    """
    try:
        import pyhecke_native as pyn  # noqa: F401
        from pyhecke.gram import NF_BASIS, TR_M
    except Exception as e:  # pragma: no cover
        print(f"  [skipped — pyhecke_native/pyhecke.gram unavailable: {type(e).__name__}]")
        return None

    def partitions(n):
        def rec(n, mx):
            if n == 0:
                yield ()
                return
            for k in range(min(n, mx), 0, -1):
                for rest in rec(n - k, k):
                    yield (k,) + rest
        return list(rec(n, n))

    def chi(lam, word, q_str, dps=50):
        nat = [(1, g + 1) for g in word]
        return mpf(pyn.chi_lambda_braid_mpfr(list(lam), nat, q_str, dps))

    def tau_M_word(word, n, q, parts, dps=50):
        q_str = mp.nstr(q, dps)
        y = {tuple(k): mpf(str(v)) for k, v in y_lambda_at(n, q).items()}
        return sum(y[lam] * chi(lam, word, q_str, dps) for lam in parts)

    parts = partitions(3)
    q0 = mpf(str(q_at()))
    ok = True
    for w, expected in zip(NF_BASIS, TR_M):
        got = tau_M_word(list(w), 3, q0, parts)
        d = abs(got - mpf(str(expected)))
        ok = ok and (d < mpf("1e-8"))
    print(f"  general τ_M(T_w) vs hardcoded gram.TR_M (n=3): {'PASS' if ok else 'FAIL'}")
    return ok


def main():
    import json
    print("=" * 78)
    print(" General-n Jacobi–Anger tower test — RECONCILED §4a object (χ_λ(𝓑_n−𝓑_p))")
    print("=" * 78)
    derived, results, coeffs_ok, reconcile_ok = reconcile_n3()
    print("-" * 78)
    print(" Optional general-n Markov-trace infra validation:")
    infra_ok = validate_markov_infra()
    print("-" * 78)
    print(" Tower extension (n≥6): needs first-principles χ_λ(𝓑_n−𝓑_p) at λ⊢6,9")
    print(" (typed proton/neutron braids embedded at brane-tower levels 6,9).")
    print(" NOT 'extend the SDP fit'. Gate: y-frozen single-x residual shrinks→0 ⇒")
    print(" q-Bessel contraction object; plateaus/grows ⇒ refutation.")
    print("-" * 78)

    out = {
        "reconciled": bool(reconcile_ok),
        "bar_odd_coeffs_match_hardcoded": bool(coeffs_ok),
        "markov_infra_n3_ok": (None if infra_ok is None else bool(infra_ok)),
        # Per-anchor now (see each row in `n3`); this key keeps the proton
        # anchor for continuity with readers of the old witness, and is the
        # LIVE reference rather than the frozen convention-C literal.
        "physical_weight_reference_residual_n3": (
            results["proton"].get("physical_weight_reference_residual")),
        "physical_weight_reference_residual_n3_convention_C_historical":
            mp.nstr(PHYSICAL_WEIGHT_RESIDUAL_N3_CONVENTION_C_HISTORICAL, 6),
        "n3": results,
    }
    print(json.dumps(out, indent=2))

    # Witness emission
    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("qbeta-jacobi-anger-tower-general", engine="sympy+mpmath")
        w.set_description(
            "General-n Jacobi–Anger tower harness, reconciled to the §4a physical-"
            "weight object. Derives the bar-odd sinh coefficients symbolically from the "
            "Lean-proved χ_λ(𝓑_n − 𝓑_p) closed forms (explicit typed-B₃ neutron-minus-"
            "proton braid difference — NOT the min-norm T_β∝t SDP fit), weights by the "
            "Markov weights y_λ FROZEN at the substrate anchor, and reproduces the "
            "physical-weight script's 6.8% single-x over-determination residual at both "
            "the proton and muon anchors. Resolves the prior tower-object reconciliation "
            "WIP. Tower extension to n≥6 requires first-principles χ_λ(𝓑_n − 𝓑_p) at "
            "λ⊢6,9 (typed braids embedded at higher brane-tower levels), not the SDP fit."
        )
        w.add_data("n3", results)
        w.add_data("bar_odd_coeffs_n3",
                   {str(lam): {int(k): str(v) for k, v in cks.items()}
                    for lam, cks in derived.items()})
        w.add_assertion(
            "bar_odd_coeffs_derived_equal_hardcoded",
            computed=bool(coeffs_ok), expected=True, tolerance=0,
            source="symbolic barodd[χ_λ(𝓑_n−𝓑_p)] vs physical-weight BAR_ODD_COEFFS",
        )
        w.add_assertion(
            # RENAMED from `reconciles_physical_weight_6_8pct_both_anchors`.
            # The old name baked a convention-C number into the identity of the
            # check, so the name itself went stale with the 2026-08-09 excision;
            # under D the same agreement holds at 0.142709. An assertion diff
            # will read this as one removed + one added — it is a rename, and
            # the predicate is unchanged apart from being computed live.
            "reconciles_physical_weight_reference_both_anchors",
            computed=bool(reconcile_ok), expected=True, tolerance=0,
            source="single-x over-det residual vs "
                   "qbeta_reeb_tower_jacobi_anger_physical_weight.solve_single_x "
                   "at the same anchor (proton + muon)",
        )
        saved = w.save()
        print(f"  Witness: {getattr(saved, 'name', saved)}")
    except Exception as e:  # pragma: no cover
        print(f"  [witness emission skipped: {type(e).__name__}: {e}]")

    return 0 if (coeffs_ok and reconcile_ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
