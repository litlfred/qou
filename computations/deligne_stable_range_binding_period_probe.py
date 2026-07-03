"""Deligne/TL stable-range probe for the binding period T_q(n) = sum_{lam|-n} dim_q(lam).

Audit-only decisive probe (2026-07-03 audit
docs/audits/2026-07-03-parabolic-cylinder-channel-interpolation.md, sec 8/10;
owner-approved follow-up to PR #3258 "can we use this to improve mass/binding compute?").

The interpolated-category (Deligne Rep(S_t) / stable-range) reorganization writes every
lam |- n as a padded shape mu[n] = (n - |mu|, mu) with mu the shape below the first row.
Two questions, one per discipline leg:

(1) RESTRICTION PROPERTY (formal, derived then machine-verified). For FIXED mu the
    family n -> dim_q(mu[n]) has the closed form

        dim_q(mu[n]) = ( prod_{i=0}^{m+mu_1-1} [n-i]_q  /  prod_{j<=mu_1} [n-c_j]_q^{*} ) / H_q(mu)

    more precisely: hooks of rows >= 2 are exactly the hooks of mu; row-1 hooks at
    columns j > mu_1 give [n-m-mu_1]_q!; row-1 hooks at j <= mu_1 are [n - c_j]_q with
    c_j = m + j - 1 - leg_j(mu), leg_j(mu) = #{i : mu_i >= j}.  Hence

        dim_q(mu[n]) = prod_{i=0}^{m+mu_1-1} [n-i]_q / ( prod_{j=1}^{mu_1} [n-c_j]_q * H_q(mu) )

    -- a fixed rational function of (q, q^n): the per-shape family IS "polynomial in the
    level" (depth-1 q-holonomic in q^n). This is the categorical-interpolation
    restriction property at the level of q-dimensions. The probe verifies the formula
    EXACTLY (sympy, symbolic q) for all |mu| <= 4 and all valid n <= 12.

(2) FEASIBILITY (decisive measurement, no fit). If the stable range were a fast
    evaluator of T_q(n) at the substrate q_0, the truncated sums
    S_M(n) = sum_{|mu| <= M} dim_q(mu[n]) would capture T_q(n) as n grows. But at
    q_0 > 1 the sum is dominated by BALANCED shapes (max dim_q), which are maximally
    far from the stable range (long first row). The probe measures the captured
    fraction S_M(n)/T_q(n) at q_0 for M = 0..6, n <= 12.

Expected structural link: (1) + (2) explain the 2026-06-26 kernel-search negative --
each padded-shape family is depth-1 q-holonomic, but the number of families needed
grows with n, so the full sum escapes any bounded-depth kernel; and the stable
truncation captures a vanishing fraction at q_0, so interpolated-level evaluation is
NOT a high-A shortcut (scope-a if confirmed).

Discipline: no fit anywhere; (1) is an exact identity check, (2) is a measurement.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys
from datetime import datetime, timezone

import mpmath as mp
import sympy as sp

from q_parameter import Q as Q0  # noqa: E402
from phase5_n8_dim_q_table import (  # noqa: E402
    dim_q_via_quantum_hooks, hook_lengths, partitions_of,
)

DPS = 50
N_MAX = 12
MU_MAX_FORMULA = 4   # verify the restriction formula for all |mu| <= 4
M_MAX_CAPTURE = 6    # captured-fraction truncation levels


def q_int_sym(h: int, q: sp.Symbol) -> sp.Expr:
    """Symmetric [h]_q = q^(h-1) + q^(h-3) + ... + q^-(h-1) — the canonical helper's
    convention (`phase5_n8_dim_q_table.q_int_sympy`)."""
    if h == 0:
        return sp.S.Zero
    return sum(q**k for k in range(h - 1, -h, -2))


def padded(mu: tuple[int, ...], n: int) -> tuple[int, ...] | None:
    """mu[n] = (n - |mu|, mu) if it is a partition (first row long enough), else None."""
    m = sum(mu)
    first = n - m
    if first < 1 or (mu and first < mu[0]):
        return None
    return (first, *mu)


def stable_formula(mu: tuple[int, ...], n: int, q: sp.Symbol) -> sp.Expr:
    """The derived closed form for dim_q(mu[n]) as a function of (q, n) — see docstring."""
    m = sum(mu)
    mu1 = mu[0] if mu else 0
    # numerator: prod_{i=0}^{m+mu1-1} [n-i]_q  (= [n]_q!/[n-m-mu1]_q!)
    num: sp.Expr = sp.S.One
    for i in range(m + mu1):
        num *= q_int_sym(n - i, q)
    # row-1 hooks at columns j <= mu1: h = n - c_j, c_j = m + j - 1 - leg_j(mu)
    den: sp.Expr = sp.S.One
    for j in range(1, mu1 + 1):
        leg = sum(1 for part in mu if part >= j)
        den *= q_int_sym(n - (m + j - 1 - leg), q)
    # hooks of mu itself
    for h in hook_lengths(mu):
        den *= q_int_sym(h, q)
    # together() suffices — numerator/denominator are already explicit products;
    # avoid cancel()'s global GCD reduction (compute-audit P15)
    return sp.together(num / den)


def dim_q_numeric(lam: tuple[int, ...], q0: mp.mpf) -> mp.mpf:
    """Numeric q-hook quantum dimension at q0 (same convention as the canonical helper)."""
    def qi(h: int) -> mp.mpf:
        return (q0**h - q0**(-h)) / (q0 - q0**(-1))
    n = sum(lam)
    val = mp.mpf(1)
    for k in range(1, n + 1):
        val *= qi(k)
    for h in hook_lengths(lam):
        val /= qi(h)
    return val


def main() -> int:
    mp.mp.dps = DPS
    q0 = mp.mpf(str(Q0))
    q = sp.Symbol("q")

    # ---- (1) restriction property: exact symbolic verification ------------------
    print("(1) per-shape restriction formula, exact check (|mu| <= "
          f"{MU_MAX_FORMULA}, n <= {N_MAX}):")
    formula_checks = 0
    formula_failures: list[str] = []
    mus = [mu for m in range(0, MU_MAX_FORMULA + 1) for mu in partitions_of(m)]
    for mu in mus:
        for n in range(1, N_MAX + 1):
            lam = padded(mu, n)
            if lam is None:
                continue
            direct = dim_q_via_quantum_hooks(lam, q)
            derived = stable_formula(mu, n, q)
            # exact check without cancel() (compute-audit P15): cross-multiply the
            # together()-normalized fractions and compare expanded polynomials
            d_num, d_den = sp.fraction(sp.together(direct))
            f_num, f_den = sp.fraction(sp.together(derived))
            if sp.expand(d_num * f_den - f_num * d_den) != 0:
                formula_failures.append(f"mu={mu}, n={n}")
            formula_checks += 1
    print(f"    {formula_checks} (mu, n) pairs checked; "
          f"failures: {len(formula_failures)} {formula_failures[:5]}")

    # ---- (2) captured fraction at q_0 -------------------------------------------
    print(f"\n(2) stable-range captured fraction S_M(n)/T_q(n) at q_0 (dps={DPS}):")
    capture: dict[int, dict[int, str]] = {}
    frac_last: dict[int, mp.mpf] = {}
    header = "    n |  " + "  ".join(f"M={M:<2d}" for M in range(M_MAX_CAPTURE + 1))
    print(header)
    for n in range(4, N_MAX + 1):
        T = mp.fsum(dim_q_numeric(lam, q0) for lam in partitions_of(n))
        row: dict[int, str] = {}
        fr_str = []
        for M in range(M_MAX_CAPTURE + 1):
            S = mp.mpf(0)
            for m in range(0, M + 1):
                for mu in partitions_of(m):
                    lam = padded(mu, n)
                    if lam is not None:
                        S += dim_q_numeric(lam, q0)
            frac = S / T
            row[M] = mp.nstr(frac, 8)
            fr_str.append(f"{float(frac):.4f}")
            if M == M_MAX_CAPTURE:
                frac_last[n] = frac
        capture[n] = row
        print(f"   {n:2d} |  " + "  ".join(fr_str))

    # decisive verdict: does the deepest truncation hold its capture as n grows?
    decreasing = all(frac_last[n + 1] < frac_last[n]
                     for n in range(2 * M_MAX_CAPTURE, N_MAX))
    print(f"\n  capture at M={M_MAX_CAPTURE} monotonically decreasing for "
          f"n>{2 * M_MAX_CAPTURE}: {decreasing}")

    witness = {
        "description": ("Deligne/TL stable-range probe for T_q(n)=sum dim_q: (1) per-shape "
                        "padded-family closed form (rational in q, q^n — the interpolation "
                        "restriction property) verified exactly; (2) captured fraction of "
                        "the stable truncation at substrate q_0 — feasibility verdict for "
                        "interpolated-level evaluation of the binding period."),
        "audit_only": True,
        "tier": "decisive probe (formalize-first: formula derived then machine-verified; "
                "capture is a measurement, no fit)",
        "precision_dps": DPS,
        "constants": {"q_0": mp.nstr(q0, 20)},
        "restriction_property": {
            "mu_max": MU_MAX_FORMULA, "n_max": N_MAX,
            "pairs_checked": formula_checks,
            "failures": formula_failures,
            "holds": not formula_failures,
        },
        "captured_fraction": {str(n): capture[n] for n in capture},
        "verdict": {
            "per_shape_family_is_level_rational": not formula_failures,
            "stable_truncation_captures_T_at_q0": bool(
                frac_last[N_MAX] > mp.mpf("0.5")),
            "capture_decreasing_in_n": decreasing,
        },
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    from witness_base import WitnessBuilder  # noqa: E402
    out = WitnessBuilder.wrap_legacy(
        "deligne-stable-range-binding-period-probe", witness,
        script_path=__file__, engine="sympy+mpmath",
    ).save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
