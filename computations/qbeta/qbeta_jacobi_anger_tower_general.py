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
0.0684 at BOTH anchors — the general harness and `qbeta_reeb_tower_jacobi_anger_
physical_weight.py` now compute the same object.

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

# Physical-weight reference value to reconcile against (n=3, both anchors).
# Source: qbeta_reeb_tower_jacobi_anger_physical_weight.py / PR #2453.
PHYSICAL_WEIGHT_RESIDUAL_N3 = mpf("0.0683508")

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
    """Build the CORRECT §4a object (χ_λ(𝓑_n−𝓑_p), y-frozen) and reproduce 6.8%."""
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
        match = resid is not None and abs(resid - PHYSICAL_WEIGHT_RESIDUAL_N3) < mpf("1e-4")
        reconcile_ok = reconcile_ok and match
        results[label] = {
            "q": mp.nstr(q0, 20),
            "W1": mp.nstr(W[1], 12), "W3": mp.nstr(W[3], 12), "W5": mp.nstr(W[5], 12),
            "single_x": (mp.nstr(x, 12) if x is not None else None),
            "overdet_rel_residual": (mp.nstr(resid, 6) if resid is not None else None),
            "matches_physical_weight_6_8pct": bool(match),
        }
        print(f"  {label:7s} q={mp.nstr(q0, 18)}")
        print(f"          W_1={mp.nstr(W[1], 10)}  W_3={mp.nstr(W[3], 10)}  "
              f"W_5={mp.nstr(W[5], 10)}")
        print(f"          single x*={mp.nstr(x, 10) if x else 'NO ROOT'}  "
              f"over-det residual={mp.nstr(resid, 6) if resid is not None else 'n/a'}  "
              f"[reproduces 6.8% physical-weight: {'YES' if match else 'NO'}]")

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
        "physical_weight_reference_residual_n3": mp.nstr(PHYSICAL_WEIGHT_RESIDUAL_N3, 6),
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
            "reconciles_physical_weight_6_8pct_both_anchors",
            computed=bool(reconcile_ok), expected=True, tolerance=0,
            source="single-x over-det residual vs 0.0683508 (proton + muon)",
        )
        saved = w.save()
        print(f"  Witness: {getattr(saved, 'name', saved)}")
    except Exception as e:  # pragma: no cover
        print(f"  [witness emission skipped: {type(e).__name__}: {e}]")

    return 0 if (coeffs_ok and reconcile_ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
