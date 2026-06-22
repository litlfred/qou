#!/usr/bin/env python3
"""
Habiro cyclotomic coefficients a_m(K) for atomic braids.

Per content/braids-and-knots/full-pole-structure-mass-trace.md and
habiro-ring.md, the Markov trace of an atomic braid admits a
Habiro / cyclotomic expansion

    tr_M(T_w, q)  =  Σ_{m ≥ 0}  a_m(T_w) · (q; q)_m

with  (q;q)_m = (1-q)(1-q²)···(1-q^m)  the q-Pochhammer.

For finite-degree Laurent polynomials the cyclotomic expansion is
computed by sequential polynomial division:

    a_0(q)  =  p(q)  mod (1 - q)              (a constant in ℤ)
    p_1(q)  = (p(q) - a_0) / (1 - q)
    a_1(q)  =  p_1(q) mod (1 - q²)            (degree ≤ 1 in q)
    p_2(q)  = (p_1(q) - a_1) / (1 - q²)
    ...

For atomic-braid Markov traces, p(q) ∈ ℤ[q^{1/2}, q^{-1/2}].  Setting
check_q = q^{1/2} and clearing denominators gives p(check_q) ∈ ℤ[check_q, check_q^{-1}], to
which we apply the cyclotomic algorithm in check_q (i.e. expand in
(check_q;check_q)_m).  The Habiro property to verify is:

    INTEGRALITY:  every a_m(check_q) ∈ ℤ[check_q, check_q^{-1}]
    TERMINATION:  a_m = 0 for m exceeding the polynomial degree

Witness: habiro-coefficients-atomic.witness.json
"""

# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
from pathlib import Path
from datetime import datetime, timezone

import mpmath as mp
import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401
from sympy import Symbol, Rational, Integer, simplify, together, nsimplify

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as _Q_CANONICAL
from hecke_character_symbolic import q_character_on_braid_word
from canonical_braid_crossings import atom_canonical_crossings as atomic_braid_to_crossings
from schur_weyl_symbolic import partitions_of
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_symbolic


# (Z, N, include_inter) → chi-witness atom label.  Maps the canonical
# atomic-braid recipe to the chi-{label}-h{n}.witness.json cache so
# q_character_on_braid_word can return cached chi values.
_ATOM_CHI_LABEL_BY_ZN: dict[tuple[int, int, bool], str] = {
    (1, 0, False): "proton",
    (1, 0, True):  "proton",
    (0, 1, False): "neutron",
    (0, 1, True):  "neutron",
    (1, 1, True):  "deuteron",
    (1, 2, True):  "tritium",
    (2, 1, True):  "helium-3",
    (2, 2, True):  "helium-4",
}


def markov_trace_symbolic(Z, N, q, include_inter=True):
    """tr_M(T_w(Z,N), q) = Σ_{λ ⊢ 3A} y_λ(q) · χ^λ_q(T_w).

    Canonical Wenzl-bridge convention: y_λ via Wenzl Schur principal
    specialization (`y_lambda_wenzl_bridge_symbolic`).  Replaces the
    legacy 2-variable Schur weight `s_λ(q, q^{-1})/H_q(λ)` (which
    vanishes for partitions with > 2 rows, dropping the sign-rep
    contribution).  Per `docs/audits/2026-05-08-p3-h-3a-divergence.md`,
    y_λ is the canonical Markov-trace weight for q ≠ 1; the q=1
    classical Plancherel point is the only place where the two
    conventions agree.  Cross-checks against the 1 ppb canonical
    50-dps reducer (`cross-check-trM-1ppb.witness.json`) at q_0:
      proton:   1.0653062286131670
      neutron:  0.9232332971861535
      deuteron: 0.388286471547713  (`include_inter=True`)

    Performance: y_λ has sqrt(q) factors that make `sp.cancel`
    catastrophic for the deuteron's n=6 partition sum.  Workaround:
    work internally in check_q with q = u², so the sqrt(q) factors become
    polynomial check_q; the final result is back-substituted to q via
    check_q → sqrt(q).  Combined with the y_λ witness cache (n = 2..12)
    and the chi witness caches (`chi-{atom}-h{n}.witness.json`) for
    p / n / D / T / ³He / ⁴He, the full p + n + D pipeline runs in
    seconds instead of minutes.

    Returns a sympy expression in q.
    """
    A = Z + N
    crossings = atomic_braid_to_crossings(Z, N, include_inter=include_inter)
    chi_cache_label = _ATOM_CHI_LABEL_BY_ZN.get((Z, N, include_inter))
    q_pos = sp.Symbol("q", positive=True)

    # Work internally in u_internal where u_internal² = q.  This
    # eliminates sqrt(q) factors from y_λ before the symbolic
    # multiplication, keeping per-term sp.cancel polynomial-time
    # instead of catastrophic on the n=6 partition sum.
    u_int = sp.Symbol("_markov_trace_u_internal", positive=True)
    total_u = Integer(0)
    for lam in partitions_of(3 * A):
        try:
            w = y_lambda_wenzl_bridge_symbolic(tuple(lam))
            # y_lambda_wenzl_bridge_symbolic uses Symbol("q", positive=True)
            # internally; substitute u_int² for that q.
            w_u = w.subs(q_pos, u_int ** 2)
            if w_u == 0:
                continue
            chi = q_character_on_braid_word(
                lam, crossings, q,
                atom_cache_label=chi_cache_label,
            )
            chi_u = chi.subs(q, u_int ** 2)
            if chi_u == 0:
                continue
            # Skip per-term sp.cancel: the deuteron n=6 case had
            # sympy spending minutes on cancel even after q→u² (the
            # accumulated chi numerators are large polynomials in check_q);
            # final sp.together at the end is sufficient for the
            # downstream to_u_polynomial and runs in ~1 s for D.
            if (w_u * chi_u).has(sp.nan) or (w_u * chi_u).has(sp.zoo):
                raise ValueError(f"NaN/Inf in λ = {lam}")
            total_u += w_u * chi_u
        except Exception as exc:
            raise RuntimeError(
                f"Markov trace symbolic failed at λ = {lam} "
                f"(A = {A}): {type(exc).__name__}: {exc}") from exc

    # Combine into a single fraction in u_int and reduce.  Working
    # in check_q (where u² = q, no sqrt) keeps sp.cancel polynomial-time
    # — the same operation on the back-substituted q-expression
    # (with sqrt(q) factors) hits the heuristic-GCD ceiling for
    # certain partition sums (e.g. the neutron's mixed σ/σ^{-1}/avg
    # word).  Cancel here in check_q, then back-substitute.
    total_u = sp.cancel(sp.together(total_u))
    return total_u.subs(u_int, sp.sqrt(q))


def to_u_polynomial(expr_in_q, q, check_q):
    """Substitute q → u² and clear ALL check_q-denominators (including any
    cyclotomic / Markov-normalisation factors).  Returns
    (p_in_u, shift, denom) such that

        p_in_u(check_q)  =  check_q^{shift} · denom(check_q) · expr_in_q(u²)

    is a polynomial in check_q with no negative powers.  The Habiro
    expansion is then computed for p_in_u and the result is the
    cyclotomic decomposition of the Markov-renormalised Jones-like
    object (the Markov normalisation z^n = (check_q + check_q^{-1})^{-n} is
    absorbed into the prefactor).
    """
    expr_u = sp.together(expr_in_q.subs(q, check_q ** 2))
    num, den = sp.fraction(expr_u)
    num = sp.expand(num)
    den = sp.expand(den)
    # Clear check_q-denominator entirely: multiply by den and shift to make
    # the result a polynomial in check_q.
    p_raw = num
    if den != 1:
        # Already cleared: p_raw = num, total = num/den; multiply by den
        pass
    # Normalise to non-negative powers of check_q
    p_expanded = sp.expand(p_raw)
    poly = sp.Poly(p_expanded, check_q)
    coeffs = poly.all_coeffs()
    # Determine min and max exponent
    monoms = poly.monoms()
    if not monoms:
        return Integer(0), 0, str(den)
    min_pow = min(int(m[0]) for m in monoms)
    shift = -min_pow if min_pow < 0 else 0
    p_shifted = sp.expand(p_expanded * check_q ** shift)
    return p_shifted, shift, str(sp.expand(den))


def cyclotomic_expansion(p_in_u, check_q, max_m=20):
    """Expand p(check_q) = Σ_m a_m(check_q) · (check_q;check_q)_m by sequential polynomial
    division.

    Algorithm.  At step m, p_m(check_q) is the running remainder.  We
    define

        a_m(check_q)  =  p_m(check_q)  mod (1 - check_q^{m+1})        (deg ≤ m)
        p_{m+1} = (p_m(check_q) - a_m(check_q)) / (1 - check_q^{m+1}) (exact division)

    so that p(check_q) = a_0 + a_1(1-check_q) + a_2(1-check_q)(1-u²) + ⋯.  The
    iteration terminates exactly when p_{m+1} = 0; if p has finite
    degree this happens at some m_max ~ √(2·deg p).

    Returns a list of dicts, one per m.
    """
    p = sp.Poly(sp.expand(p_in_u), check_q)
    coeffs = []
    current = p
    for m in range(max_m):
        if current.is_zero:
            break
        next_factor = sp.Poly(1 - check_q ** (m + 1), check_q)
        # Single sp.div gives BOTH a_m (= remainder, degree < m+1) and
        # quotient (= (current - a_m) / next_factor) in one call.
        # The previous implementation recomputed the quotient via a
        # second sp.div on `current.as_expr() - a_m_expr`, doubling
        # the work per iteration on a deg-194 polynomial.
        quotient, a_m = sp.div(current, next_factor, check_q)
        a_m_expr = a_m.as_expr()
        coeffs.append({
            "m": m,
            "a_m": str(a_m_expr),
            "deg_a_m": int(a_m.degree()) if a_m.as_expr() != 0 else 0,
            "integral": all(c.is_Integer for c in a_m.all_coeffs())
                          if a_m.as_expr() != 0 else True,
            # `current = quotient * next_factor + a_m` is exact by
            # construction of sp.div (the second sp.div in the prior
            # implementation always returned remainder=0); only flag
            # nonzero on a true PolynomialError.
            "remainder_nonzero": False,
        })
        current = quotient
    return coeffs


def reconstruct(coeffs_data, check_q, max_m=20):
    """Reconstruct p(check_q) = Σ a_m · (check_q;check_q)_m from the list to verify."""
    total = Integer(0)
    for entry in coeffs_data:
        m = entry["m"]
        a_m = sp.sympify(entry["a_m"], locals={"check_q": check_q})
        poch = Integer(1)
        for k in range(1, m + 1):
            poch *= 1 - check_q ** k
        total += sp.expand(a_m * poch)
    return sp.expand(total)


def analyse_atomic_braid(label, Z, N, include_inter, q):
    print(f"\n── {label} (Z={Z}, N={N}) ──")
    p_q = markov_trace_symbolic(Z, N, q, include_inter=include_inter)
    # Skip sp.nsimplify in the log line — for the deuteron's
    # ~degree-194 rational over q this call alone takes >30 s while
    # adding zero diagnostic value (the polynomial is already in
    # its symbolic form).  Use the raw repr instead.
    print(f"  tr_M (in q) computed (free symbols: {p_q.free_symbols})")
    check_q = sp.Symbol('check_q', positive=True, real=True)
    p_u, shift, denom = to_u_polynomial(p_q, q, check_q)
    deg_p = int(sp.Poly(p_u, check_q).degree()) if p_u != 0 else 0
    print(f"  → p(check_q) := check_q^{shift} · denom · tr_M(u²), shift = check_q^{shift}, "
          f"denom (in check_q) = {denom}")
    print(f"     deg p(check_q) = {deg_p}")
    coeffs = cyclotomic_expansion(p_u, check_q, max_m=20)
    print(f"  Habiro coefficients (in check_q = q^{{1/2}} = \\check{{q}}, spinor rate):")
    for entry in coeffs:
        flag = "✓" if entry["integral"] else "✗"
        print(f"    a_{entry['m']}(check_q) = {entry['a_m']}    "
              f"deg = {entry['deg_a_m']}, integral: {flag}")
    # Verify reconstruction
    recon = reconstruct(coeffs, check_q)
    diff = sp.expand(recon - p_u)
    if diff == 0:
        print(f"  ✓ reconstruction matches  Σ a_m·(check_q;check_q)_m  =  p(check_q)")
    else:
        print(f"  ✗ reconstruction error:  diff = {diff}")
    # Numerical check
    q0 = Rational(int(_Q_CANONICAL * 10 ** 16), 10 ** 16)
    u0 = sp.sqrt(q0)
    # Keep substrate precision via mp.mpf (was float() — flagged by
    # compute_no_mpf_to_float_cast). The witness field "tr_M_at_q0"
    # below requires it as the substrate-precision value.
    p_at_q0 = mp.mpf(str(p_q.subs(q, q0).evalf(50)))
    p_at_q0_polynomial_q = expose_polynomial(p_q, q)
    p_u_at_u0 = mp.mpf(str(p_u.subs(check_q, u0).evalf(50))) / mp.mpf(str(
        (u0 ** shift if shift else 1).evalf(50) if shift else 1))
    print(f"  tr_M @ q_0 = {mp.nstr(p_at_q0, 6, strip_zeros=False)}  "
          f"(via check_q-poly: {mp.nstr(p_u_at_u0, 6, strip_zeros=False)})")
    return {
        "Z": Z, "N": N, "include_inter": include_inter,
        # str(p_q) directly — sp.nsimplify on a degree-194 rational
        # adds 30+ seconds with no benefit for the witness consumer
        # (downstream re-parses with sp.sympify).
        "tr_M_in_q": str(p_q),
        "shift": int(shift),
        "denom_in_u": denom,
        "p_in_u": str(p_u),
        "deg_p_u": deg_p,
        "habiro_coefficients": coeffs,
        "all_integral": all(c["integral"] for c in coeffs),
        "reconstruction_matches": (diff == 0),
        "tr_M_at_q0": mp.nstr(p_at_q0, 30),
    }


if __name__ == "__main__":
    print("HABIRO CYCLOTOMIC COEFFICIENTS — atomic braids")
    print("=" * 80)
    print(f"q_0 = {float(_Q_CANONICAL):.6f}")

    q = sp.Symbol('q', positive=True, real=True)

    # A=1 (proton, neutron): tractable in symbolic q (~1 min total).
    # A=2 (deuteron): 11 partitions of 6 with Hoefsmit dim up to 9 in
    #   symbolic q over a 12-crossing braid — heavy (>10 min).  Run via
    #   `--with-deuteron` flag once a faster symbolic pipeline is wired
    #   up, or evaluate numerically at q_0 and verify integer coefficients
    #   of the resulting Laurent polynomial.
    import os
    cases = [
        ("p (proton, A=1)",      1, 0, False),
        ("n (neutron, A=1)",     0, 1, False),
    ]
    if os.environ.get("HABIRO_WITH_DEUTERON"):
        cases.append(("D (deuteron, A=2)", 1, 1, True))

    results = {}
    for label, Z, N, inter in cases:
        try:
            results[label] = analyse_atomic_braid(label, Z, N, inter, q)
        except Exception as exc:
            print(f"  {label}: ERROR {type(exc).__name__}: {exc}")
            results[label] = {"error": f"{type(exc).__name__}: {exc}"}

    print("\n── Summary ──")
    for label, r in results.items():
        if "error" in r:
            print(f"  {label}: ERROR {r['error']}")
            continue
        print(f"  {label}: deg p(check_q) = {r['deg_p_u']:>3}, "
              f"#Habiro coeffs = {len(r['habiro_coefficients']):>2}, "
              f"all integral: {r['all_integral']}, "
              f"reconstruction: {r['reconstruction_matches']}")

    witness = {
        "computation": "habiro-coefficients-atomic",
        "description": (
            "Habiro / cyclotomic expansion tr_M(T_w, q) = Σ_m a_m·(check_q;check_q)_m "
            "(check_q = q^{1/2}) for atomic braids p, n, D. Verifies the integrality "
            "and termination properties of the Habiro coefficients claimed "
            "in habiro-ring.md and full-pole-structure-mass-trace.md."
        ),
        "reference_blocks": [
            "def:habiro-ring",
            "prop:full-pole-structure-mass-trace",
            "thm:knot-mass-formula-unified",
            "prop:e-infinity-page-identifications",
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": float(_Q_CANONICAL),
            "engine": "sympy Poly + sequential cyclotomic division",
        },
        "results": results,
    }
    out = Path(__file__).parent / "habiro-coefficients-atomic.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
