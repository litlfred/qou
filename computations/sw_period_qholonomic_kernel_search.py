#!/usr/bin/env python3
# polynomial_q_not_applicable: high-precision q-holonomic recurrence search at q0;
# falsifiability PROBE (audit-only witness), not a production derivation
# (compute-author §1.3). NO fit promoted; the search RESULT is a non-closure.
"""Probe: does the binding period a_D^(n)=lw(n−1)=(1/n)·T_q(n), T_q(n)=Σ_{λ⊢n} dim_q(λ),
satisfy a bounded-depth q-difference kernel R(q,x) (prop:binding-genfun-qdifference)?

#2822 identified a_D^(n) as the q-deformed involution number (T_q(n)→I(n) at q→1,
RSK). The z2bn kernel question: is T_q(n) **q-holonomic** — i.e. does it obey a
finite-depth recurrence Σ_j a_j(q^n) T_q(n+j)=0 with a_j Laurent-polynomial in q^n
(the coefficient form of R(q,x))?

SEARCH (this probe). For depth d∈{2,3} and Laurent degree D∈{1,2,3} in x=q^n, solve
the homogeneous recurrence on the minimal exactly-determined set and **verify on
held-out n**. RESULT: no model closes. The apparent improvement at higher D is
OVERFITTING — the held-out residual shrinks only as the held-out COUNT collapses
(depth-2: L[-1,1] 0.24 @15 held → L[-2,2] 2e-3 @9 → L[-3,3] 6e-7 @3), never
reaching the precision floor (~1e-80 @ 90 dps).

DECISIVE: the depth-2 L[-2,2] held-out residual is **precision-INDEPENDENT**
(identical at 70 and 140 dps), so it is a genuine approximation error, not a
numerical artifact ⇒ **no low-order (d≤3, D≤3) q-holonomic recurrence for T_q(n)**
(scope-(a): the searched range; not a proof of non-holonomicity at all orders).

FORK (the productive redirect). There are TWO q-deformations of I(n):
  (1) T_q(n)=Σ_{λ⊢n} dim_q(λ)   — the QUANTUM-DIMENSION sum (the binding period /
      selection rule). NOT low-order q-holonomic (this search).
  (2) μ_q(n)=μ(n−1)+[n−1]_q μ(n−2) — the CROSSING-counted q-Hermite / Rogers–Szegő
      moment. Clean depth-2 q-telephone kernel (a known result).
They agree at q=1 (both = I(n)) but DIFFER at q0 (demonstrated here). The clean
R(q,x) belongs to (2); the binding selection rule is (1). z2bn must decide which is
the physical binding object — or accept that (1) needs a higher-order kernel.

Heuristic for WHY (1) breaks: dim_q=[n]_q!/∏[h]_q is a hook-QUOTIENT q-term; a
partition SUM of such quotients is generically non-holonomic. The q=1 case is
rescued by the RSK bijection (Σf^λ=I(n)) — a q=1 miracle, not q-stable.

Output: sw-period-qholonomic-kernel-search.witness.json (audit-only).
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE / "phase5"))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR as Q0  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def _make_T(dps: int):
    """Return (Tv dict, q0m) with T_q(n)=Σ_{λ⊢n} dim_q(λ) at q0, computed
    numerically via the symmetric q-hook formula at `dps` digits."""
    mp.mp.dps = dps
    q0m = mp.mpf(Q0)
    den = q0m - 1 / q0m

    def qb(k: int) -> mp.mpf:
        return (q0m ** k - q0m ** (-k)) / den

    qfac = {0: mp.mpf(1)}
    for k in range(1, 60):
        qfac[k] = qfac[k - 1] * qb(k)

    def parts(n: int, m: int | None = None):
        if m is None:
            m = n
        if n == 0:
            yield ()
            return
        for k in range(min(n, m), 0, -1):
            for r in parts(n - k, k):
                yield (k,) + r

    def hooks(lam):
        conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
        return [(lam[i] - j - 1) + (conj[j] - i - 1) + 1
                for i in range(len(lam)) for j in range(lam[i])]

    def dimq(lam):
        d = qfac[sum(lam)]
        for h in hooks(lam):
            d /= qb(h)
        return d

    NMAX = 24
    Tv = {n: mp.fsum(dimq(l) for l in parts(n)) for n in range(1, NMAX + 1)}
    return Tv, q0m, NMAX


def _search(Tv, q0m, NMAX, depth, D):
    """Solve depth-`depth`, Laurent-degree-`D` (in x=q^n) recurrence on the minimal
    set; return (held_out_max_rel, held_count)."""
    def x(n):
        return q0m ** n
    cols = [(j, e) for j in range(depth + 1) for e in range(-D, D + 1)]
    norm = (depth, 0)
    used = [c for c in cols if c != norm]
    U = len(used)
    avail = [n for n in range(2, NMAX - depth + 1)]
    if len(avail) < U + 3:
        return None
    fit, held = avail[:U], avail[U:]
    M = mp.matrix(U, U)
    rhs = mp.matrix(U, 1)
    for r, n in enumerate(fit):
        # row-slice fill (mpmath 1.3 needs a matrix value, not a bare list)
        M[r, :] = mp.matrix([[x(n) ** e * Tv[n + j] for (j, e) in used]])
        rhs[r, 0] = -Tv[n + depth]
    try:
        sol = mp.lu_solve(M, rhs)
    except Exception:
        return None
    coef = {norm: mp.mpf(1)}
    for c, (j, e) in enumerate(used):
        coef[(j, e)] = sol[c]

    def L(n):
        return mp.fsum(coef[(j, e)] * x(n) ** e * Tv[n + j] for (j, e) in cols)
    maxrel = max(abs(L(n)) / abs(Tv[n + depth]) for n in held)
    return maxrel, len(held)


def main() -> int:
    Tv, q0m, NMAX = _make_T(90)

    rows = []
    for depth in (2, 3):
        for D in (1, 2, 3):
            r = _search(Tv, q0m, NMAX, depth, D)
            if r is None:
                continue
            maxrel, held = r
            rows.append({
                "depth": depth, "laurent_deg": D,
                "params": (depth + 1) * (2 * D + 1) - 1,
                "held_out": held, "held_max_rel": mp.nstr(maxrel, 5),
            })
    none_close = all(mp.mpf(r["held_max_rel"]) > mp.mpf("1e-50") for r in rows)

    # Decisive precision-independence: depth-2 L[-2,2] at 70 vs 140 dps.
    prec = {}
    for dps in (70, 140):
        Tp, qp, Np = _make_T(dps)
        r = _search(Tp, qp, Np, 2, 2)
        prec[dps] = mp.nstr(r[0], 8) if r else "n/a"
    mp.mp.dps = 90  # restore
    precision_independent = prec.get(70) == prec.get(140)

    # FORK: crossing q-Hermite moment μ_q(n) vs T_q(n) — agree q→1, differ at q0.
    den = q0m - 1 / q0m

    def qb(k):
        return (q0m ** k - q0m ** (-k)) / den
    mu = {0: mp.mpf(1), 1: mp.mpf(1)}
    for n in range(2, 9):
        mu[n] = mu[n - 1] + qb(n - 1) * mu[n - 2]
    fork_rows = []
    for n in range(2, 9):
        rel = abs(mu[n] - Tv[n]) / abs(Tv[n])
        fork_rows.append({"n": n, "T_q (quantum-dim)": mp.nstr(Tv[n], 10),
                          "mu_q (crossing moment)": mp.nstr(mu[n], 10),
                          "rel_diff": mp.nstr(rel, 4)})
    fork_max = max(abs(mu[n] - Tv[n]) / abs(Tv[n]) for n in range(4, 9))

    w = WitnessBuilder("sw-period-qholonomic-kernel-search",
                       engine="python+mpmath")
    w.set_audit_only(
        "docs/audits/2026-06-26-binding-period-qinvolution-qhermite-identification.md")
    w.add_parameter("q_0", Q0)
    w.add_data("question",
               "Is T_q(n)=Σ_{λ⊢n} dim_q(λ) q-holonomic (a bounded-depth R(q,x))?")
    w.add_data("search_grid", rows)
    w.add_data("precision_check_depth2_L22",
               {"dps70": prec.get(70), "dps140": prec.get(140),
                "precision_independent": precision_independent})
    w.add_data("verdict_scope_a",
               "No low-order (depth≤3, Laurent-deg≤3 in q^n) q-holonomic recurrence "
               "closes for T_q(n); non-closure is precision-independent (genuine, not "
               "numerical). Higher orders unsearched — NOT a proof of non-holonomicity "
               "at all orders. The bounded-depth kernel R(q,x) of "
               "prop:binding-genfun-qdifference does not hold for the quantum-dimension "
               "period at low order.")
    w.add_data("fork_two_q_deformations_of_I_n", fork_rows)
    w.add_data("fork_note",
               "(1) T_q=Σ dim_q (quantum-dim, the binding selection rule) — no low-order "
               "kernel. (2) μ_q crossing q-Hermite moment (q-telephone [n−1]_q) — clean "
               "depth-2 kernel. Agree at q=1 (=I(n)), differ at q0. The clean R(q,x) "
               "belongs to (2); z2bn must decide which is the physical binding object.")

    w.add_assertion(
        "no_low_order_qholonomic_recurrence_for_quantum_dim_period",
        computed=1 if none_close else 0, expected=1, tolerance=0,
        source="every depth≤3, Laurent-deg≤3 recurrence has held-out residual ≫1e-50 "
               "(precision-independent at 70 vs 140 dps).")
    w.add_assertion(
        "quantum_dim_period_forks_from_crossing_qhermite_moment_at_q0",
        computed=1 if fork_max > mp.mpf("1e-3") else 0, expected=1, tolerance=0,
        source=f"max |μ_q(n)−T_q(n)|/|T_q(n)| over n=4..8 = {mp.nstr(fork_max, 5)} ≫ 0 "
               f"⇒ the two q-deformations of I(n) differ at q0 (agree at q=1).")
    out = w.save()

    print("=" * 80)
    print(" Is the binding period T_q(n)=Σ_λ dim_q q-holonomic? — KERNEL SEARCH")
    print("=" * 80)
    print(f"  {'depth':>5} {'L-deg':>5} {'params':>6} {'held':>5} {'held-out max rel':>18}")
    for r in rows:
        print(f"  {r['depth']:>5} {r['laurent_deg']:>5} {r['params']:>6} "
              f"{r['held_out']:>5} {r['held_max_rel']:>18}")
    print(f"\n  precision check depth-2 L[-2,2]: dps70={prec.get(70)}  dps140={prec.get(140)}")
    print(f"  precision-INDEPENDENT: {precision_independent}  (⇒ genuine non-closure)")
    print(f"\n  FORK — two q-deformations of I(n) (agree q→1, differ at q0):")
    print(f"  {'n':>2} {'T_q (Σdim_q)':>16} {'mu_q (crossing)':>16} {'rel_diff':>10}")
    for r in fork_rows:
        print(f"  {r['n']:>2} {r['T_q (quantum-dim)']:>16} "
              f"{r['mu_q (crossing moment)']:>16} {r['rel_diff']:>10}")
    print(f"\n  VERDICT (scope-a): no low-order q-holonomic R(q,x) for the quantum-dim")
    print(f"  binding period; the clean kernel belongs to the crossing q-Hermite moment.")
    print(f"\n Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
