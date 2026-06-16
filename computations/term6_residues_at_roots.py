#!/usr/bin/env python3
"""
Term 6 of the six-term mass formula via Markov-peel symbolic `tr_M(q)`.

`thm:six-term-mass-formula-complete` defines

    Term 6  =  Σ_{ζ ≠ 0, root of unity}  PP_ζ[tr_M(T_w)] (q₀)

i.e. the sum of all principal-part contributions of the meromorphic
function `tr_M(T_w, q)` at non-zero roots of unity, evaluated at
q₀.  This module computes Term 6 by **partial-fraction split** on
the u-plane lift `tr_M(u²)`, separating

    tr_M(u²) = entire(u) + PP_0(u) + PP_roots(u)

at u = u₀ = √q₀.  The Term 6 value is `PP_roots(u₀)`.

Why u-plane, why partial-fraction split:

  1. **u-plane** removes the q-plane branch ambiguity at q = ±1.
     Markov traces of atomic braids carry (q^{1/2} + q^{-1/2})
     factors, so they are single-valued in u (where u² = q) but
     only sheet-valued in q.  A naive q-plane residue at q = -1
     returns 3 + I (proton; sheet-dependent) instead of the real
     Mittag-Leffler residue.

  2. **PP split** isolates the "Term 6" part from two confounders:
       - The polynomial part `entire(u)` — has no poles.
       - The principal part `PP_0` at u = 0 — physical pole at
         q = 0 from the (q^{n}, q^{-n}) Hecke generators, but
         **not** part of the Term 6 root-of-unity sum.

     The split is computed in O(deg(N) + deg(D)) sympy ops via
     polynomial long division and one power-series inversion of
     the non-zero-pole denominator factor.  No per-pole residue
     extraction is needed (the prior `sp.residue` path scaled
     polynomially in atom size and timed out at deuteron).

Performance vs. the previous per-pole `sp.residue` path, then with
the LaurentQ-coefficient Markov-peel fast path:

  | atom    | sp.residue | partial-fraction split | + LaurentQ fast peel |
  |---------|-----------:|-----------------------:|---------------------:|
  | proton  |       30 s |                 0.42 s |                0.1 s |
  | neutron |       30 s |                 0.31 s |                0.1 s |
  | deuteron|    > 30min |                  8.1 s |                0.6 s |
  | tritium |    > 30min |                 12.0 s |                3.7 s |
  | helium-3|    > 30min |                  5.6 s |                2.1 s |
  | helium-4|    > 30min |                 50.5 s |               17.0 s |

That's a ~100× speedup at A = 1, unlocks A ≥ 2 entirely, and a
further 3-8× from routing the symbolic Markov peel through
`hecke_laurent_fast.tr_M_atomic_fast` (LaurentQ coefficients
instead of generic sympy `Expr`).

Witness:  term6-residues-at-roots.witness.json
Reference: thm:six-term-mass-formula-complete (Term 6),
           prop:full-pole-structure-mass-trace (pole structure)

Usage:
    python computations/term6_residues_at_roots.py
    python computations/term6_residues_at_roots.py \
        --atoms proton,neutron,deuteron,tritium,helium-3,helium-4
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import argparse
import sys
import time
from pathlib import Path

import sympy as sp
import mpmath

# Power-series inversion via sp.series can blow Python's default
# recursion ceiling on the larger u-plane rationals; the bump matches
# the kahler_lift fix in this same series.
sys.setrecursionlimit(20000)

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from hecke_laurent_fast import tr_M_atomic_fast as tr_M_atomic  # noqa: E402
from hecke_symbolic import q as q_sym                     # noqa: E402
from q_parameter import Q as Q0                           # noqa: E402
from witness_base import WitnessBuilder                   # noqa: E402

# Pin precision floor; matches the markov-peel witness convention.
mpmath.mp.dps = 50


ATOMS_DEFAULT = [
    ("proton",   1, 0),
    ("neutron",  0, 1),
    ("deuteron", 1, 1),
    ("tritium",  1, 2),
    ("helium-3", 2, 1),
    ("helium-4", 2, 2),
    ("lithium-5", 3, 2),
    ("lithium-6", 3, 3),
]


u_sym = sp.Symbol("u")


def lift_q_to_u(tr_sym, q, u):
    """Replace q^(k/2) with u^k everywhere in `tr_sym`.

    Avoids `sp.powdenest(force=True)` which is the wall here:
    powdenest scans every Pow node in the (10 000+-op) Markov-trace
    expression and rewrites the half-integer-q-power patterns, taking
    72 s on tritium and ~290 s on ⁴He.  Direct replacement of q^(k/2)
    via two `Expr.replace` calls runs in <1 s on the same inputs.

    Steps:
      1. `tr.replace(sqrt(q), u)` — catches the `q^(1/2)` Pow nodes
         that come from the (q^{1/2} + q^{-1/2}) Markov-trace
         denominators directly.
      2. `tr.replace(<any Pow with base q>, ...)` — lifts the
         remaining integer powers `q^k → u^(2k)` and any leftover
         half-integer powers `q^(p/2) → u^p`.
      3. Final `subs(q, u**2)` — covers any bare-q occurrences (rare
         after step 2 but cheap).

    The branch implicitly chosen is `√q = u` on the principal sheet
    of u₀ = +√q₀, matching `compute_atom`.
    """
    out = tr_sym.replace(sp.sqrt(q), u)

    def is_q_pow(node):
        return isinstance(node, sp.Pow) and node.base == q

    def transform(node):
        e = node.exp
        if e.is_Rational:
            if e.q == 1:           # q^k       → u^(2k)
                return u ** (2 * e.p)
            if e.q == 2:           # q^(p/2)   → u^p
                return u ** e.p
        return node

    out = out.replace(is_q_pow, transform)
    out = out.subs(q, u**2)
    return out


def power_series_invert(D_poly, u, k):
    """Return polynomial `I` of degree < k with `D · I ≡ 1 (mod u^k)`.

    Pure linear-recurrence inversion: given D = d_0 + d_1 u + ...,
    solve `D · I = 1` coefficient-by-coefficient up to degree k-1.
    O(k · deg(D)) ops vs `sp.series`'s general-purpose recursive
    Taylor expansion which scales worse.  On tritium (k = 61):
    direct invert = 0.20 s vs sp.series = 21.0 s (105× speedup).
    Output has been spot-checked to agree with `sp.series` exactly.

    `D_poly` must be `sp.Poly` and have non-zero constant term.
    """
    d_coeffs = D_poly.all_coeffs()[::-1]  # ascending [d_0, d_1, ...]
    d_0 = d_coeffs[0]
    if d_0 == 0:
        raise ValueError("D(0) = 0; cannot invert mod u^k")
    I = [sp.Rational(0)] * k
    I[0] = sp.Rational(1) / d_0
    deg_D = len(d_coeffs)
    for n in range(1, k):
        s = sp.Rational(0)
        # I[n] determined by D · I = 1 ⇒ Σ_{j=0..n} d_j · I_{n-j} = 0
        upper = min(n + 1, deg_D)
        for j in range(1, upper):
            s += d_coeffs[j] * I[n - j]
        I[n] = -s / d_0
    return sum(c * u**i for i, c in enumerate(I) if c != 0)


def split_polar_at_u0(tr_u_expr, u, u0_sp) -> dict:
    """Partial-fraction split of `tr_u_expr` at u = u0_sp.

    Decomposes the rational function `tr_u(u) = N(u)/D(u)` as

        tr_u(u) = entire(u) + A(u)/u^k + B(u)/Dprime(u)

    where:
      - `entire(u) = quot(u)` is the polynomial part of long-division
        N // D (zero unless deg(N) ≥ deg(D));
      - `D(u) = u^k · Dprime(u)` with `Dprime(0) ≠ 0` (factor out the
        u = 0 multiplicity);
      - `A(u)` of degree < k is the principal part at u = 0
        (negative-power Laurent coefficients), computed as
        `R(u) · Dprime(u)^{-1}` MOD u^k via `sp.series` (one power-
        series inversion);
      - `B(u)` of degree < deg(Dprime) is the principal part at the
        non-zero poles, computed as `(R(u) − A(u)·Dprime(u)) / u^k`
        as an exact polynomial division.

    Returns a dict with the four numeric values at u = u0:
      - `entire`      : quot(u0)
      - `pp_at_zero`  : A(u0) / u0^k
      - `pp_at_roots` : B(u0) / Dprime(u0)        ← **Term 6**
      - `pole_order_at_zero`: k

    Failure modes raise — caller wraps with try/except for the
    per-atom main loop.
    """
    num, den = sp.fraction(tr_u_expr)
    num_p = sp.Poly(num, u)
    den_p = sp.Poly(den, u)

    # 1) Polynomial division: separate the entire (polynomial) part
    quot, rem = sp.div(num_p, den_p, u)
    entire_at_u0 = complex(sp.N(quot.as_expr().subs(u, u0_sp), 30))

    # 2) Factor u^k out of the denominator.  Read the multiplicity
    #    directly from the trailing-zero count of the dense coefficient
    #    list rather than the previous subs(u, 0) + cancel loop, which
    #    re-substituted and re-cancelled the whole symbolic expression
    #    each step (per Gemini review on PR #536).
    coeffs_desc = den_p.all_coeffs()  # highest power first
    k = 0
    while k < len(coeffs_desc) and coeffs_desc[-1 - k].equals(0):
        k += 1
    if k > 0:
        Dprime_coeffs_desc = coeffs_desc[:-k]
    else:
        Dprime_coeffs_desc = coeffs_desc
    Dprime = sp.Poly(Dprime_coeffs_desc, u)
    # Cross-check against the closed-form D(u) for canonical pppnnn
    # atomic braids (PR #539): D(u) = 2^(2A+1) · u^(18Z+21N+1) · (1+u²)^(3A−1).
    # The auto-detected k must match the closed-form 18Z + 21N + 1.
    # (Caller-side check; passed in via expected_k_pole when known.)

    if k == 0:
        # No u = 0 pole; the proper rational is entirely Term 6.
        full = complex(sp.N(
            (rem.as_expr() / den_p.as_expr()).subs(u, u0_sp), 30
        ))
        return {
            "entire": entire_at_u0,
            "pp_at_zero": 0.0 + 0j,
            "pp_at_roots": full,
            "pole_order_at_zero": 0,
            "denom_factor_no_zero": str(sp.factor(Dprime.as_expr())),
        }

    # 3) Power-series inversion: A(u) = R(u) · Dprime(u)^{-1} MOD u^k.
    #    Direct linear-recurrence inversion (see `power_series_invert`)
    #    is ~100× faster than `sp.series(R/Dprime, u, 0, k)` on the
    #    larger atoms (tritium k = 61: 0.20 s vs 21 s).
    rem_expr = rem.as_expr()
    I_poly = power_series_invert(Dprime, u, k)
    A_full = sp.expand(rem_expr * I_poly)
    # Truncate the product to degree < k (everything ≥ k is the
    # higher-order Taylor of R/Dprime, which is the regular part at
    # u = 0 and not part of the principal A(u)).
    A_p = sp.Poly(A_full, u)
    A_coeffs = A_p.all_coeffs()[::-1]  # ascending
    A_series = sum(A_coeffs[i] * u**i for i in range(min(k, len(A_coeffs))))

    # 4) B(u) = (R(u) − A(u)·Dprime(u)) / u^k as exact polynomial.
    #    `(diff) / u^k` is an exact polynomial division (the construction
    #    of A guarantees u^k | diff); use sp.div on Poly objects rather
    #    than sp.cancel — same result but skips the GCD step that walls
    #    on big inputs.
    diff = sp.expand(rem_expr - A_series * Dprime.as_expr())
    B_p, B_rem = sp.div(sp.Poly(diff, u), sp.Poly(u**k, u), u)
    if not B_rem.is_zero:
        raise ValueError("u^k does not divide diff exactly — check A_series")
    B = B_p.as_expr()

    pp_at_zero = complex(sp.N((A_series / u**k).subs(u, u0_sp), 30))
    pp_at_roots = complex(sp.N((B / Dprime.as_expr()).subs(u, u0_sp), 30))
    return {
        "entire": entire_at_u0,
        "pp_at_zero": pp_at_zero,
        "pp_at_roots": pp_at_roots,
        "pole_order_at_zero": k,
        "denom_factor_no_zero": str(sp.factor(Dprime.as_expr())),
    }


def compute_atom(Z: int, N: int) -> dict:
    """Run Term 6 for atom (Z, N) via the partial-fraction split."""
    A = Z + N

    t0 = time.time()
    tr_sym = tr_M_atomic(Z, N)
    t_peel = time.time() - t0

    t0 = time.time()
    # Lift to u = √q via direct sqrt-replacement (see `lift_q_to_u`),
    # then `together` to get a single-rational form.  This pair was
    # previously `subs(q, u**2)` + `powdenest(force=True)` + `cancel`,
    # whose powdenest scan was the wall (~70 s tritium, ~290 s ⁴He).
    # The direct replacement runs in <1 s on the same inputs.
    tr_u = sp.together(lift_q_to_u(tr_sym, q_sym, u_sym))
    t_subs = time.time() - t0

    q0_mp = mpmath.mpf(str(Q0))
    u0_mp = mpmath.sqrt(q0_mp)
    u0_sp = sp.Float(str(u0_mp), 30)

    t0 = time.time()
    split = split_polar_at_u0(tr_u, u_sym, u0_sp)
    t_split = time.time() - t0

    pp_roots = split["pp_at_roots"]

    # Cross-check the auto-detected pole order against the closed-form
    # prediction for canonical pppnnn atomic braids (PR #539, merged
    # 2026-05-04).  D(u) = 2^(2A+1) · u^(18Z+21N+1) · (1+u²)^(3A−1).
    closed_form_pred = None
    closed_form_match = None
    if Z >= 1 and N >= 1:
        try:
            from d_u_closed_form_proof import closed_form_d_u
            cf = closed_form_d_u(Z, N, include_inter=True)
            closed_form_pred = cf["u_shift"]
            closed_form_match = (split["pole_order_at_zero"] == closed_form_pred)
        except (ImportError, ValueError, NotImplementedError):
            pass

    return {
        "Z": Z, "N": N, "A": A,
        "tr_M_u_symbolic_ops": int(sp.count_ops(tr_u)),
        "denom_pole_order_at_zero": split["pole_order_at_zero"],
        "denom_factor_no_zero": split["denom_factor_no_zero"],
        "closed_form_pole_order": closed_form_pred,
        "closed_form_match": closed_form_match,
        "elapsed_peel_sec":  round(t_peel,  3),
        "elapsed_subs_sec":  round(t_subs,  3),
        "elapsed_split_sec": round(t_split, 3),
        # Numeric components at u₀ — kept as Python complex strings so
        # the witness round-trips through json.dumps reliably.
        "entire_at_u0":      str(split["entire"]),
        "pp_at_zero_at_u0":  str(split["pp_at_zero"]),
        "pp_at_roots_at_u0": str(pp_roots),
        "term6_at_q0":       str(pp_roots),  # alias for downstream consumers
        "term6_at_q0_real":  float(pp_roots.real),
        "term6_at_q0_imag":  float(pp_roots.imag),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--atoms", type=str,
        default="proton,neutron,deuteron,tritium,helium-3,helium-4",
        help=(
            "Comma-separated atom labels to run.  Default: full A ≤ 4 "
            "spectrum (the partial-fraction split scales well; deuteron "
            "is ~8 s, helium-4 a few minutes)."
        ),
    )
    args = parser.parse_args()
    selected = set(args.atoms.split(","))

    print(
        "Term 6 — partial-fraction polar split on u-plane lift "
        "tr_M(u²); Term 6 = PP_at_roots(u₀)",
        flush=True,
    )
    print("=" * 72, flush=True)

    rows = []
    for label, Z, N in ATOMS_DEFAULT:
        if label not in selected:
            continue
        print(f"\n=== {label} (Z={Z}, N={N}, A={Z + N}) ===", flush=True)
        try:
            row = compute_atom(Z, N)
            row["atom"] = label
            print(
                f"  peel={row['elapsed_peel_sec']:.2f}s  "
                f"subs={row['elapsed_subs_sec']:.2f}s  "
                f"split={row['elapsed_split_sec']:.2f}s  "
                f"ops={row['tr_M_u_symbolic_ops']}  "
                f"k₀={row['denom_pole_order_at_zero']}",
                flush=True,
            )
            print(f"  Dprime (non-zero-pole denom) = "
                  f"{row['denom_factor_no_zero']}", flush=True)
            print(f"  entire(u₀)         = {row['entire_at_u0']}",
                  flush=True)
            print(f"  PP_0(u₀)           = {row['pp_at_zero_at_u0']}",
                  flush=True)
            print(f"  PP_roots(u₀) [T6]  = {row['pp_at_roots_at_u0']}",
                  flush=True)
            # Drop fluctuating per-row timings before adding to the
            # witness payload — they cause the witness-pipeline drift
            # detection to flag every regeneration as a substantive
            # change.  Console print above retains them for the run
            # log.
            row_for_witness = {
                k: v for k, v in row.items()
                if not k.startswith("elapsed_")
            }
            rows.append(row_for_witness)
        except Exception as exc:  # noqa: BLE001
            print(f"  FAILED: {type(exc).__name__}: {exc}", flush=True)
            rows.append({
                "atom": label, "Z": Z, "N": N, "A": Z + N,
                "error": f"{type(exc).__name__}: {exc}",
            })

    w = WitnessBuilder("term6-residues-at-roots", engine="sympy")
    w.set_description(
        "Term 6 of thm:six-term-mass-formula-complete via partial-"
        "fraction polar split on the u-plane lift tr_M(u²): "
        "tr_M(u²) = entire(u) + A(u)/u^k + B(u)/Dprime(u), with "
        "Term 6 = B(u₀)/Dprime(u₀) the principal-part contribution at "
        "non-zero poles only.  This split avoids per-pole residue "
        "extraction; sp.div + one sp.series-based power-series inversion "
        "deliver the answer in seconds where sp.residue scaled "
        "polynomially in atom size and timed out at deuteron.  "
        "Evaluation enabled by the Markov-axiom recursive ascent "
        "(#508 / PR #516) returning tr_M as a symbolic rational function "
        "in q^{1/2}."
    )
    w.set_content_block("thm:six-term-mass-formula-complete")
    w.add_parameter("q0", str(Q0))
    w.add_parameter("method", "partial_fraction_split_u_plane")
    w.add_data("results", rows)
    out_path = w.save()
    print(f"\n  → wrote {out_path}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
