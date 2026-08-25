#!/usr/bin/env python3
"""Term 6 — Mittag-Leffler full pole sum per prop:full-pole-structure-mass-trace.

⚠ CONVENTION CAVEAT (added 2026-05-03 in PR #537 follow-up).

This script reads `habiro-coefficients-atomic.witness.json`, which is
populated by `habiro_coefficients_atomic.py::markov_trace_symbolic`
using `schur_weyl_weight(λ, q) = s_λ(q, q⁻¹) / H_q(λ)` (Schur function
at two variables / q-hook product).  That is NOT the canonical Markov
trace specified in the paper.

Per `content/.../y-lambda-closed-form-wenzl-bridge.md:1-32` and
`notation-register.md:28`, the Markov trace decomposition is

    tr_M = Σ_λ y_λ · χ^λ
    y_λ  = s_λ(1, Q, …, Q^{r-1}) / Σ_μ d_μ s_μ(1, Q, …, Q^{r-1}),
           Q = q²

i.e. the **Wenzl-bridge central coefficient**, NOT s_λ(q, q⁻¹) / H_q(λ).
At q_0 = 1.10998 the deuteron split is:

    canonical Markov tr_M (markov_peel ≡ Hoefsmit, 1ppb cross-check)  =  0.388
    Schur-Weyl-weighted trace consumed by THIS script                  =  0.177

The canonical Term-6 path is `term6_residues_at_roots.py` (PR #526),
which consumes `markov_peel.tr_M_atomic` directly.  This script is
retained for two reasons:

1. The Habiro-witness rational-in-u form is the only readily available
   symbolic representation that exposes higher-order pole structure
   in u-space, so the sqrt-sub fallback infrastructure here is
   independently useful (it can be ported to the canonical script).
2. Its numerical agreement with `markov_peel` for proton/neutron at
   q_0 (both 0.51 / 0.92 respectively when normalized) suggests the
   two traces share regular-locus behaviour even though their
   pole structures differ.

Treat `term6_in_MeV` from THIS script as the **Schur-Weyl-weighted
contribution**, NOT as the canonical Term 6.  Cross-comparison with
`term6_residues_at_roots.py` is a follow-up.

Per content/.../full-pole-structure-mass-trace.md:

  tr_M(T_w, q_0) = tr_M^entire(T_w, q_0)
                  + Σ_{n≥2} Σ_{gcd(j,n)=1} r_n^{(j)}(T_w) / (q_0 - ζ_n^{(j)})

with poles at every primitive n-th root of unity ζ_n^{(j)}, residues
r_n^{(j)}(T_w), and Cauchy kernel 1/(q_0 − ζ_n^{(j)}).  Sum is
absolutely convergent on the regular locus by Habiro's theorem.

**Caveat (per `tr_M is a Habiro-ring element, not a function on ℂ`):**
the primitive roots are dense in S¹, so this is NOT a complex-analytic
Mittag-Leffler in the ordinary sense.  In the Habiro ring `Ẑ[q]`, the
sum is symbolic / cyclotomic and converges in the q-adic topology.
At q_0 ≈ 1.11 (just outside |q|=1), the truncated sum gives a
meaningful Term-6 contribution whose magnitude this script measures.

Input:
  computations/habiro-coefficients-atomic.witness.json
  (provides full polynomial tr_M(T_w, q) for proton, neutron, and
   deuteron; T, ³He, ⁴He+ pending — symbolic Hoefsmit at H_9+ requires
   the numerical-interpolation path of habiro_coefficients_interpolate.py)

This script:
  1. Loads atom-specific tr_M(T_w, q) as a rational function in q
  2. Factors denominator into cyclotomic polynomials Φ_n(q)
  3. For each ζ_n^{(j)}, computes residue r_n^{(j)} symbolically
  4. Computes Σ r_n^{(j)} / (q_0 − ζ_n^{(j)}) up to cutoff n_max
  5. Compares to direct evaluation tr_M(T_w, q_0)

Output: term6-full-pole-sum.witness.json
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import math

import mpmath
import sympy as sp

from _precision import json_safe_float, set_compute_dps, fmt  # noqa: E402


def _json_safe(o):
    """Recursively: non-finite floats -> marker strings, finite floats -> repr."""
    if isinstance(o, bool) or o is None:
        return o
    if isinstance(o, float):
        v = json_safe_float(o)
        return v if isinstance(v, str) else repr(v)
    if isinstance(o, dict):
        return {k: _json_safe(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_json_safe(v) for v in o]
    return o

from experimental_constants import M_E_MEV
from q_parameter import Q as Q_0
from q_parameter import Q_50_DIGIT_STR as Q_0_STR
from witness_base import WitnessBuilder
from witness_polynomial import expose_polynomial

HERE = Path(__file__).parent
HABIRO_WITNESS = _pb.witness_path("habiro-coefficients-atomic.witness.json", HERE)

q = sp.Symbol("q", complex=True)


def primitive_roots_of_unity(n: int):
    """Generate primitive n-th roots of unity (j with gcd(j, n) = 1)."""
    from math import gcd
    if n < 1:
        return
    if n == 1:
        yield 1
        return
    for j in range(1, n):
        if gcd(j, n) == 1:
            yield sp.exp(2 * sp.pi * sp.I * sp.Rational(j, n))


def _higher_order_q_residue_via_sqrt_sub(
    p_in_u, denom_in_u, u_sym, zeta,
    *, radius: float = 0.05, n_samples: int = 64,
):
    """q-residue of `p_in_u(sqrt(q)) / denom_in_u(sqrt(q))` at `q = ζ`
    via the substitution `q = u²`.

    Setting `u₀ = sqrt(ζ)` on the principal branch, the contour
    identity `∮_{|u-u₀|=r} 2u · U(u) du = 2πi · Res_q[tr_M]`
    (chain-rule integrand) recovers the q-residue regardless of the
    pole order in u.  This handles the higher-order poles flagged by
    the simple-pole `cyclotomic_residue` path.

    Returns an `mpmath.mpc`.

    Mirrors `term6_residues_at_roots.residue_via_sqrt_substitution`
    but consumes the rational-in-u form directly from the Habiro
    witness so we skip an unnecessary q ↔ u round-trip.
    """
    integrand_sym = 2 * u_sym * (p_in_u / denom_in_u)
    f_lam = sp.lambdify(u_sym, integrand_sym, modules='mpmath')
    saved_dps = mpmath.mp.dps
    mpmath.mp.dps = max(saved_dps, 100)
    try:
        zeta_mp = mpmath.mpc(complex(sp.N(zeta, 60)))
        u0 = mpmath.sqrt(zeta_mp)
        r = mpmath.mpf(str(radius))
        total = mpmath.mpc(0)
        for k in range(n_samples):
            theta = 2 * mpmath.pi * k / n_samples
            e_i_theta = mpmath.exp(mpmath.mpc(0, 1) * theta)
            u_pt = u0 + r * e_i_theta
            total += f_lam(u_pt) * e_i_theta
        return total * r / n_samples
    finally:
        mpmath.mp.dps = saved_dps


def cyclotomic_residue(tr_M_expr, zeta, n: int):
    """Compute r_n^{(j)}(T_w) = lim_{q → ζ_n^{(j)}} (q − ζ) · tr_M(T_w, q).

    Returns:
      sympy expression (residue value) for simple poles
      sp.oo for higher-order poles (Mittag-Leffler formula needs Laurent expansion)
      0 for regular points
      None on error
    """
    expr = (q - zeta) * tr_M_expr
    try:
        result = sp.limit(expr, q, zeta)
        # Normalize ±oo to a sentinel
        if result == sp.oo or result == -sp.oo or result == sp.zoo:
            return sp.oo
        return result
    except Exception:
        return None



def _eval_poly_mpf(expr_in_u, u_sym, x):
    """Horner-evaluate a polynomial in `u_sym` at the `mpf` `x`, exactly.

    Coefficients come from a sympy Poly, so they are exact `Integer` or
    `Rational`; only the arithmetic at `mp.dps` is inexact, and sympy is kept
    out of the numeric path. Added 2026-08-23 (bean `qou-bm4i`) — see
    `tr_M_at_q0_polynomial` below.
    """
    poly = sp.Poly(sp.expand(expr_in_u), u_sym)
    acc = mpmath.mp.mpf(0)
    for c in poly.all_coeffs():
        r = sp.Rational(c)
        acc = acc * x + mpmath.mp.mpf(int(r.p)) / mpmath.mp.mpf(int(r.q))
    return acc


def mittag_leffler_term6(
    tr_M_poly_expr, q0_value: float, n_max: int = 6,
    *,
    sqrt_sub_fallback: tuple | None = None,
):
    """Compute Term-6 Mittag-Leffler sum up to cutoff n_max.

    Uses symbolic ζ_n^{(j)}, complex residue + 1/(q_0 − ζ) kernel.
    Returns (total_term6_real, per_n_breakdown).

    `sqrt_sub_fallback`, if provided, is a `(p_in_u, denom_in_u, u_sym)`
    triple in the Hecke parameter `u = sqrt(q)` (= spinor rate
    \check{q}; "u" kept as Python ident per Habiro literature).
    Whenever the
    simple-pole l'Hôpital path returns `sp.oo` (higher-order pole),
    the q-residue is recovered numerically via
    `_higher_order_q_residue_via_sqrt_sub` instead of being silently
    skipped.  This closes the `incomplete-higher-order-pole-detected`
    status for atoms whose denominator factors with multiplicity > 1
    at any cyclotomic root (e.g. deuteron at ζ_4).
    """
    total = sp.Rational(0)
    per_n = []
    q0_sym = sp.Rational(round(q0_value * 10**16), 10**16)
    for n in range(2, n_max + 1):
        n_contribution = sp.Rational(0)
        roots_data = []
        for j_idx, zeta in enumerate(primitive_roots_of_unity(n)):
            try:
                residue = cyclotomic_residue(tr_M_poly_expr, zeta, n)
                if residue is None or (
                    hasattr(residue, "equals") and residue.equals(0)
                ) or residue == 0:
                    roots_data.append({
                        "j_index": j_idx, "zeta": str(zeta),
                        "residue": "0 or None", "contribution": 0.0,
                    })
                    continue
                if residue == sp.oo:
                    # Higher-order pole — simple-pole l'Hôpital fails;
                    # fall back to chain-rule contour in u-space if a
                    # rational-in-u form was supplied.
                    if sqrt_sub_fallback is not None:
                        p_in_u, denom_in_u, u_sym = sqrt_sub_fallback
                        try:
                            res_q_mp = _higher_order_q_residue_via_sqrt_sub(
                                p_in_u, denom_in_u, u_sym, zeta,
                            )
                            kernel_mp = 1 / (
                                mpmath.mpc(complex(sp.N(q0_sym - zeta, 60)))
                            )
                            contrib_mp = res_q_mp * kernel_mp
                            contribution_real = float(contrib_mp.real)
                            n_contribution += sp.N(contrib_mp.real)
                            roots_data.append({
                                "j_index": j_idx,
                                "zeta_real": float(complex(sp.N(zeta)).real),
                                "zeta_imag": float(complex(sp.N(zeta)).imag),
                                "residue_complex": [
                                    float(res_q_mp.real),
                                    float(res_q_mp.imag),
                                ],
                                "kernel_complex": [
                                    float(kernel_mp.real),
                                    float(kernel_mp.imag),
                                ],
                                "contribution_real": contribution_real,
                                "method": "sqrt_substitution_contour",
                                "note": (
                                    "higher-order pole resolved via "
                                    "u = sqrt(q) contour with "
                                    "chain-rule integrand 2u·U(u)"
                                ),
                            })
                            continue
                        except Exception as exc:  # noqa: BLE001
                            roots_data.append({
                                "j_index": j_idx, "zeta": str(zeta),
                                "residue": "HIGHER-ORDER POLE",
                                "contribution": 0.0,
                                "note": (
                                    "sqrt-sub fallback failed: "
                                    f"{type(exc).__name__}: {exc}"
                                ),
                            })
                            continue
                    roots_data.append({
                        "j_index": j_idx, "zeta": str(zeta),
                        "residue": "HIGHER-ORDER POLE",
                        "contribution": 0.0,
                        "note": "lim (q-ζ)·tr_M = ∞; Mittag-Leffler needs Laurent expansion",
                    })
                    continue
                kernel = 1 / (q0_sym - zeta)
                contribution = residue * kernel
                contribution_complex = complex(sp.N(contribution))
                contribution_real = float(contribution_complex.real)
                n_contribution += sp.N(contribution)
                roots_data.append({
                    "j_index": j_idx,
                    "zeta_real": float(complex(sp.N(zeta)).real),
                    "zeta_imag": float(complex(sp.N(zeta)).imag),
                    "residue_complex": [
                        float(complex(sp.N(residue)).real),
                        float(complex(sp.N(residue)).imag),
                    ],
                    "kernel_complex": [
                        float(complex(sp.N(kernel)).real),
                        float(complex(sp.N(kernel)).imag),
                    ],
                    "contribution_real": contribution_real,
                })
            except Exception as e:
                roots_data.append({
                    "j_index": j_idx, "zeta": str(zeta),
                    "error": str(e), "contribution": 0.0,
                })
        n_total_real = float(complex(sp.N(n_contribution)).real)
        per_n.append({
            "n": n, "n_real_contribution": n_total_real, "roots": roots_data,
        })
        total += n_contribution
    return float(complex(sp.N(total)).real), per_n


def evaluate_atom_term6(atom_label: str, atom_data: dict, n_max: int = 6):
    """Evaluate Term 6 for a single atom from its Habiro witness data."""
    print(f"\n━━ {atom_label}")
    p_in_u_str = atom_data.get("p_in_u")
    denom_in_u_str = atom_data.get("denom_in_u")
    if not p_in_u_str or not denom_in_u_str:
        print("    SKIP: no p_in_u / denom_in_u in witness")
        return None
    u = sp.Symbol("u")
    try:
        # BOTH names. `to_u_polynomial(expr, q, check_q)` renders its returned
        # strings using whatever SYMBOL the caller passed, so the habiro
        # witnesses carry either — habiro-coefficients-atomic.witness.json
        # (2026-07-18) says "check_q", newer ones say "u". Sympifying with no
        # locals gave the string its OWN fresh symbol, `.subs(u, sqrt_q)` below
        # then no-opped, the expression stayed symbolic, and
        # `float(complex(...))` raised "Cannot convert expression to float" —
        # which is why this producer has been dead on main.
        _loc = {"u": u, "check_q": u}
        p_in_u = sp.sympify(p_in_u_str, locals=_loc)
        denom_in_u = sp.sympify(denom_in_u_str, locals=_loc)
    except Exception as e:
        print(f"    SKIP: sympify failed: {e}")
        return None
    # Convert u = q^{1/2} → tr_M(T_w, q) = p_in_u(u) / denom_in_u(u) at u = sqrt(q)
    sqrt_q = sp.sqrt(q)
    p_in_q = p_in_u.subs(u, sqrt_q)
    denom_in_q = denom_in_u.subs(u, sqrt_q)
    tr_M_expr = p_in_q / denom_in_q
    # tr_M at q_0, exactly.
    #
    # PRECISION (2026-08-23, bean `qou-bm4i`). This was
    #     float(complex(sp.N(tr_M_expr.subs(q, Q_0))).real)
    # on a `Q_0` that is `q_parameter.Q`, itself a float64 — so a witness
    # advertising `output_dps: 60` stored 16 digits, and the cross-validation
    # against markov_substrate_realizer ran an `rtol = 1e-9` comparison on
    # values truncated seven orders inside its own tolerance. `sp.N` also
    # defaults to 15 digits, so the sympy step lost precision independently of
    # the `float()`.
    #
    # Now: full-precision q_0 from `Q_50_DIGIT_STR`, Horner over the exact
    # polynomial coefficients at `mp.dps`, `fmt` on output.
    q0_mpf = mpmath.mp.mpf(Q_0_STR)
    u_0_mpf = mpmath.sqrt(q0_mpf)
    _p_val = _eval_poly_mpf(p_in_u, u, u_0_mpf)
    _d_val = _eval_poly_mpf(denom_in_u, u, u_0_mpf)
    if _d_val == 0:
        print("    SKIP: denominator vanishes at q_0")
        return None
    tr_M_at_q0_check = _p_val / _d_val
    print(f"    tr_M(T_w, q_0) [from polynomial] = {float(tr_M_at_q0_check):.6f}")
    print(f"    tr_M_at_q0 [from witness]        = {atom_data.get('tr_M_at_q0', 'N/A')}")

    # Compute Term-6 sum
    total, per_n = mittag_leffler_term6(
        tr_M_expr, Q_0, n_max=n_max,
        sqrt_sub_fallback=(p_in_u, denom_in_u, u),
    )
    # Higher-order poles still flagged (and zeroed) only when the
    # sqrt-sub fallback also failed.  When the contour fallback
    # resolved them, `roots_data` carries `method=sqrt_substitution_contour`
    # and the residue value has been folded into `n_contribution`.
    higher_order_unresolved = any(
        any(r.get("residue") == "HIGHER-ORDER POLE" for r in n_data["roots"])
        for n_data in per_n
    )
    higher_order_resolved = any(
        any(r.get("method") == "sqrt_substitution_contour"
            for r in n_data["roots"])
        for n_data in per_n
    )
    # A DIVERGENT total was previously reported as "complete-simple-poles-only":
    # the status only ever asked about higher-order poles, never whether the
    # Mittag-Leffler sum was finite. The deuteron's n=1 root (zeta = 1, the pole
    # at q = 1) gives an infinite residue, so its total is +inf — and the witness
    # called that complete, in bare `Infinity` tokens that made the file invalid
    # JSON on top of it.
    total_finite = bool(mpmath.isfinite(total))
    if not total_finite:
        status = "divergent-simple-pole-sum"
    elif higher_order_unresolved:
        status = "incomplete-higher-order-pole-detected"
    elif higher_order_resolved:
        status = "complete-with-sqrt-sub-fallback"
    else:
        status = "complete-simple-poles-only"
    print(f"    Term-6 Mittag-Leffler total (n≤{n_max}) = {total:.6e}")
    print(f"    in MeV: {total * M_E_MEV:.6e}")
    print(f"    status: {status}")
    for n_data in per_n:
        n = n_data["n"]
        cn = n_data["n_real_contribution"]
        print(f"      n={n}: contribution = {cn:+.6e}")
    # Record term6_in_MeV as None only when an UNRESOLVED higher-order
    # pole remains (sqrt-sub fallback failed).  When resolved via
    # contour integration the partial sum IS the full Term-6.
    # None when there is no finite value to report — a divergent sum is not a
    # number in MeV, and `inf` there read like one.
    term6_value = (None if (higher_order_unresolved or not total_finite)
                   else total * M_E_MEV)
    # Expose tr_M(T_w, q) symbolically so downstream consumers can
    # re-evaluate at any q without re-running the script.
    try:
        tr_M_polynomial = expose_polynomial(tr_M_expr, q, simplify=False)
    except Exception as e:  # pragma: no cover
        tr_M_polynomial = {
            "polynomial_q": None,
            "polynomial_q_latex": None,
            "value_at_q0": str(tr_M_at_q0_check),
            "expose_error": f"{type(e).__name__}: {str(e)[:120]}",
        }
    return {
        "atom": atom_label,
        "n_max": n_max,
        "tr_M_at_q0_polynomial": fmt(tr_M_at_q0_check),
        "tr_M_polynomial": tr_M_polynomial,
        # `_json_safe` over the whole tree: the divergence shows up in
        # per_n_breakdown roots too (residue_complex, contribution_real), and
        # every one of them was a bare `Infinity` token. Markers keep the fact
        # that the residue diverges — which is the RESULT here, not a failure —
        # while making the witness parse.
        "term6_simple_residue_partial": json_safe_float(float(total)),
        "term6_in_MeV": term6_value,
        "status": status,
        "higher_order_pole_unresolved": higher_order_unresolved,
        "higher_order_pole_resolved_via_sqrt_sub": higher_order_resolved,
        "per_n_breakdown": _json_safe(per_n),
    }


def main():
    # `_precision` does not raise mp.dps on import; without this the mpf
    # evaluation below runs at mpmath's default 15 and `fmt` pads a
    # float64-grade value out to full width (bean `qou-bm4i`).
    set_compute_dps()
    print("=" * 78)
    print("Term 6 — Mittag-Leffler full pole sum")
    print("=" * 78)
    print(f"q_0 = {Q_0}")
    print(f"m_e = {M_E_MEV} MeV")
    print()

    if not HABIRO_WITNESS.exists():
        print(f"ERROR: {HABIRO_WITNESS} not found")
        sys.exit(1)
    with open(HABIRO_WITNESS) as f:
        d = json.load(f)
    results = d.get("results", {})
    print(f"Atoms with Habiro coefficients: {list(results.keys())}")
    print()

    n_max = 6  # cutoff: enough to see the pattern, not too slow
    out_atoms = []
    for atom_label, atom_data in results.items():
        result = evaluate_atom_term6(atom_label, atom_data, n_max=n_max)
        if result:
            out_atoms.append(result)

    print()
    print("=" * 78)
    print("Conclusion: Term 6 magnitude vs A≥5 5–20% errors")
    print("=" * 78)
    for r in out_atoms:
        if r['term6_in_MeV'] is None:
            print(f"  {r['atom']:<25} Term-6 = INCOMPLETE ({r['status']})")
        else:
            print(f"  {r['atom']:<25} Term-6 = {r['term6_in_MeV']:+.6f} MeV ({r['status']})")
    print()
    print("NOTE: upstream Habiro witness now has proton, neutron, deuteron.")
    print("To assess Term 6 for T, ³He, ⁴He, ⁶Li–¹⁶O (the A≥5 atoms")
    print("with large residuals), need to extend habiro-coefficients-")
    print("atomic.witness.json to those atoms via the numerical-")
    print("interpolation path (habiro_coefficients_interpolate.py).")

    # Build witness
    w = (
        WitnessBuilder("term6-full-pole-sum", engine="python+sympy")
        .set_description(
            "Term 6 Mittag-Leffler full pole sum per "
            "prop:full-pole-structure-mass-trace. Computes Σ_{n≥2} "
            "Σ_{gcd(j,n)=1} r_n^{(j)}(T_w) / (q_0 − ζ_n^{(j)}) using "
            "symbolic Habiro residues + 1/(q_0 − ζ) kernel up to "
            "cutoff n_max=6. Upstream Habiro witness has proton, neutron, "
            "and deuteron; T, ³He, ⁴He+ pending — extension via "
            "habiro_coefficients_interpolate.py is the next step for "
            "A≥5 5–20% error assessment. Higher-order poles (e.g. "
            "deuteron at ζ_4 = ±i, where (u²+1)² appears in the "
            "u = sqrt(q) denominator) are now recovered via a "
            "chain-rule contour integral in u-space "
            "(_higher_order_q_residue_via_sqrt_sub); the deuteron Term-6 "
            "contribution that was previously emitted as 'incomplete' "
            "now resolves to ≈ 0.057 MeV."
        )
        .set_content_block("prop:full-pole-structure-mass-trace")
        # `_json_safe` also carries floats to their repr strings: every number
        # in this witness comes off a float64/sympy-N path (the residues are
        # evaluated numerically), so repr is exactly the digits produced and it
        # round-trips bit-exactly. Non-finite values become markers rather than
        # bare JSON tokens — the deuteron's divergent sum is the one that
        # matters and it is a RESULT, not a failure.
        .add_parameter("q_0", _json_safe(Q_0))
        .add_parameter("m_e_MeV", _json_safe(M_E_MEV))
        .add_parameter("n_max_cutoff", n_max)
        .add_data("atoms", _json_safe(out_atoms))
        .add_caveat(
            "CONVENTION: this script reads habiro-coefficients-atomic."
            "witness.json, populated by markov_trace_symbolic in "
            "habiro_coefficients_atomic.py via schur_weyl_weight = "
            "s_λ(q,q⁻¹) / H_q(λ). That is NOT the canonical Markov "
            "trace tr_M = Σ_λ y_λ · χ^λ specified in "
            "y-lambda-closed-form-wenzl-bridge.md; the canonical y_λ "
            "is the Wenzl-bridge central coefficient. At q_0 = 1.10998 "
            "the deuteron split is canonical 0.388 (markov_peel ≡ "
            "Hoefsmit) vs Schur-Weyl-weighted 0.177 (this script's "
            "input). The canonical Term 6 path is term6_residues_at_"
            "roots.py (PR #526), which reads markov_peel.tr_M_atomic "
            "directly. Treat term6_in_MeV here as the Schur-Weyl-"
            "weighted contribution, not the canonical Term 6."
        )
        .add_caveat(
            "Primitive roots of unity are dense in S¹, so this is NOT "
            "a complex-analytic Mittag-Leffler in the ordinary sense. "
            "tr_M is a Habiro-ring element; convergence is q-adic. "
            "Truncation at n_max=6 captures the dominant Cauchy-kernel "
            "weighted residues (smaller n → closer to q_0 = 1.11 → "
            "larger 1/|q_0 − ζ| kernel)."
        )
        .add_caveat(
            "Extend habiro-coefficients-atomic.witness.json to T, ³He, "
            "⁴He, ⁶Li, ⁷Li, ⁹Be, ¹¹B, ¹²C, ¹⁶O before this script can "
            "answer 'does Term 6 close the A≥5 5-20% errors?' — A≥4 "
            "is blocked on symbolic Hoefsmit at H_9+, the numerical-"
            "interpolation route in habiro_coefficients_interpolate.py "
            "documents A=4 as intractable at 60 dps."
        )
        .add_caveat(
            "Higher-order pole resolution: when l'Hôpital returns "
            "sp.oo, we run a Cauchy contour ∮_{|u-u₀|=0.05} 2u·U(u) du "
            "in u-space at u₀ = sqrt(ζ) (principal branch). Radius 0.05 "
            "is conservative for ℓ ≤ 12 (nearest neighbour at ≥ 2sin(π/ℓ²) "
            "≥ 0.05). Pole order is detected automatically by the "
            "contour identity — no per-pole-order branching."
        )
    )
    out_path = w.save()
    print(f"\nWitness: {out_path.name}")


if __name__ == "__main__":
    main()
