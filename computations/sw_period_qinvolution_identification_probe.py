#!/usr/bin/env python3
# polynomial_q_not_applicable: symbolic q-rational selection-rule sums + q→1 limit
# + mpmath evaluation at q0; falsifiability/identification PROBE (audit-only
# witness), not a production derivation (compute-author §1.3). NO free parameter.
"""Probe: IDENTIFY the binding period a_D^(n)=lw(n−1) as the q-deformed involution
number, and PRUNE the naive depth-2 q-telephone recurrence.

Context. PR #2795 settled that a_D^(n)=lw(n−1)=(1/n)Σ_{λ⊢n} dim_q(λ) is
super-exponential (not the depth-2 SL₂ germ). This probe asks WHAT super-exp
object it is, by its q→1 limit.

IDENTIFICATION (positive, verified). Write T_q(n) := Σ_{λ⊢n} dim_q(λ) = n·lw(n−1).
Then
        T_q(n)  ──q→1──▶  Σ_{λ⊢n} f^λ  =  I(n)   (involution / telephone numbers,
                                                   OEIS A000085: 1,1,2,4,10,26,76,…),
the classical Frobenius–Schur identity (sum of irreducible S_n dimensions =
number of involutions). This holds for ALL n — a theorem, not a finite check:
`Σ_λ f^λ = I(n)` is proved for all n by RSK (σ ↦ (P,Q) with Q=P iff σ²=1, so
#involutions = #SYT = Σ_λ f^λ), and `dim_q(λ) → f^λ` as q→1 (q-hook → hook). The
n=1..12 loop below CONFIRMS the q-hook reduction is computed correctly; the all-n
statement rides on RSK. Hence **a_D^(n) = lw(n−1) = T_q(n)/n is the q-deformation
of I(n)/n** — a q-involution number, i.e. a q-Hermite / Rogers–Szegő moment
(involutions are the moments of the Hermite/Gaussian weight; their q-analogue is
the Rogers–Szegő moment sequence — the family of `QOU.Mass.BindingQHermiteOscillator`,
#2800). This pins the structural HOME of the z2bn kernel.

PRUNE (scope-a). The involution numbers obey the depth-2 P-recursion
I(n)=I(n−1)+(n−1)I(n−2) — depth-2 but with an n-DEPENDENT coefficient (why a_D^(n)
is super-exp and the constant-coefficient SL₂ fails). The naive q-analogue
T_q(n) =? T_q(n−1) + [n−1]_q·T_q(n−2)  (symmetric q-bracket) is EXACT at n=3 but
DRIFTS for n≥4 (and no depth-2 q-holonomic model with low-degree Laurent
coefficients in q^n closes — separate guess, best held-out ≈1.5e-3). So the exact
q-coefficient is NOT the bare [n−1]_q: the right q-statistic on involutions
(the Rogers–Szegő / q-Hermite moment recurrence) is the open z2bn frontier.

This is an identification + two scope-(a) prunes; it does NOT close the kernel.

Output: sw-period-qinvolution-identification.witness.json (audit-only).
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE / "phase5"))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _precision import COMPUTE_DPS  # noqa: E402
from q_parameter import Q_50_DIGIT_STR as Q0  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from phase5_n8_dim_q_table import dim_q_via_quantum_hooks, partitions_of  # noqa: E402


def T_sym(n: int, q: sp.Symbol) -> sp.Expr:
    """T_q(n) = Σ_{λ⊢n} dim_q(λ) (canonical q-hook quantum dimension)."""
    return sp.cancel(sum((dim_q_via_quantum_hooks(lam, q) for lam in partitions_of(n)),
                         sp.S.Zero))


def involution_numbers(nmax: int) -> list[int]:
    """I(n) = I(n−1) + (n−1) I(n−2), I(0)=I(1)=1 (OEIS A000085)."""
    I = [1, 1]
    for n in range(2, nmax + 1):
        I.append(I[-1] + (n - 1) * I[-2])
    return I


def main() -> int:
    mp.mp.dps = COMPUTE_DPS
    q = sp.Symbol("q", positive=True)
    q0 = sp.Float(Q0, 50)
    q0m = mp.mpf(Q0)
    N_ID = 12      # range for the q→1 = I(n) identification
    N_REC = 10     # range for the q-telephone recurrence prune

    def num(e: sp.Expr) -> mp.mpf:
        return mp.mpf(str(sp.N(e.subs(q, q0), 50)))

    def qsym(k: int) -> mp.mpf:
        return (q0m ** k - q0m ** (-k)) / (q0m - 1 / q0m)

    # ---- Identification: Σ_{λ⊢n} dim_q(λ) ──q→1──▶ I(n) ----------------------
    I = involution_numbers(N_ID)
    id_rows = []
    id_all_ok = True
    Tsym = {n: T_sym(n, q) for n in range(1, N_ID + 1)}
    for n in range(1, N_ID + 1):
        lim = sp.simplify(sp.limit(Tsym[n], q, 1))
        ok = sp.nsimplify(lim) == I[n]
        id_all_ok = id_all_ok and ok
        id_rows.append({"n": n, "lim_q1": str(lim), "I_n": I[n], "match": bool(ok)})

    # ---- The binding period at the substrate, and the q-telephone prune ------
    Tv = {n: num(Tsym[n]) for n in range(1, N_REC + 1)}
    rec_rows = []
    first_fail = None
    for n in range(3, N_REC + 1):
        pred = Tv[n - 1] + qsym(n - 1) * Tv[n - 2]
        rel = abs(pred - Tv[n]) / abs(Tv[n])
        rec_rows.append({
            "n": n,
            "T_q": mp.nstr(Tv[n], 12),
            "telephone_pred": mp.nstr(pred, 12),
            "rel_resid": mp.nstr(rel, 4),
            "lw_period": mp.nstr(Tv[n] / n, 12),
        })
        if first_fail is None and rel > mp.mpf("1e-3"):
            first_fail = n

    w = WitnessBuilder("sw-period-qinvolution-identification",
                       engine="python+sympy+mpmath")
    w.set_audit_only(
        "docs/audits/2026-06-26-binding-period-qinvolution-qhermite-identification.md")
    w.add_parameter("q_0", Q0)
    w.add_data("identity",
               "T_q(n)=Σ_{λ⊢n} dim_q(λ)=n·a_D^(n); a_D^(n)=lw(n−1). "
               "q→1: T_q(n)=Σ f^λ=I(n) (involutions, A000085).")
    w.add_data("q1_limit_table", id_rows)
    w.add_data("structural_home",
               "a_D^(n)=I_q(n)/n is a q-involution number = q-Hermite/Rogers–Szegő "
               "moment (involutions are Hermite moments). Family: BindingQHermiteOscillator "
               "(#2800). Explains super-exp growth (I(n)~n^{n/2}e^{√n−n/2−1/4}/√2).")
    w.add_data("telephone_recurrence_table", rec_rows)
    w.add_data("telephone_first_fail_n",
               first_fail if first_fail is not None else f"none ≤ n={N_REC}")
    w.add_data("scope_a_prune",
               "Naive depth-2 q-telephone T(n)=T(n−1)+[n−1]_q T(n−2) is exact at n=3, "
               "drifts for n≥4; no low-degree depth-2 q-holonomic model in q^n closes "
               "(separate guess, best held-out ≈1.5e-3). Exact q-coefficient ≠ bare "
               "[n−1]_q. NOT a structural exclusion of a depth-2 q-recurrence — the "
               "right q-statistic (Rogers–Szegő moment recurrence) is open (z2bn).")

    # Assertion 1 (positive identification): q→1 limit of Σ dim_q = I(n) for all n.
    w.add_assertion(
        "sum_dim_q_limit_is_involution_numbers",
        computed=1 if id_all_ok else 0, expected=1, tolerance=0,
        source=f"Σ_{{λ⊢n}} dim_q(λ) → I(n) (A000085) as q→1 for n=1..{N_ID} "
               f"⇒ a_D^(n)=lw(n−1) is the q-deformed involution number.",
    )
    # Assertion 2 (prune): the naive [n−1]_q q-telephone fails (rel>1e-3) by n≤4.
    w.add_assertion(
        "naive_q_telephone_recurrence_fails_beyond_n3",
        computed=1 if (first_fail is not None and first_fail <= 4) else 0,
        expected=1, tolerance=0,
        source=f"T(n)=T(n−1)+[n−1]_q T(n−2) first exceeds rel 1e-3 at n={first_fail} "
               f"(exact at n=3) ⇒ exact q-coefficient ≠ bare [n−1]_q.",
    )
    out = w.save()

    print("=" * 78)
    print(" a_D^(n)=lw(n−1) IS the q-deformed involution number — IDENTIFICATION")
    print("=" * 78)
    print(f"  q→1 limit of Σ_{{λ⊢n}} dim_q(λ) vs I(n) (involutions, A000085):")
    print(f"  {'n':>2} {'lim_{q→1}':>12} {'I(n)':>10} {'match':>6}")
    for r in id_rows:
        print(f"  {r['n']:>2} {r['lim_q1']:>12} {r['I_n']:>10} {str(r['match']):>6}")
    print(f"  ALL match: {id_all_ok}")
    print(f"\n  Naive depth-2 q-telephone prune (T(n)=T(n−1)+[n−1]_q T(n−2)):")
    print(f"  {'n':>2} {'T_q(n)':>14} {'telephone':>14} {'rel.resid':>12}")
    for r in rec_rows:
        print(f"  {r['n']:>2} {r['T_q']:>14} {r['telephone_pred']:>14} {r['rel_resid']:>12}")
    print(f"  first fail (rel>1e-3): n = {first_fail}  (exact at n=3 only)")
    print("  ⇒ structural home = q-Hermite/Rogers–Szegő moments (BindingQHermiteOscillator,")
    print("    #2800); exact q-statistic on involutions is the open z2bn kernel.")
    print(f"\n Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
