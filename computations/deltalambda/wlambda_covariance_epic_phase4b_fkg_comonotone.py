#!/usr/bin/env python3
r"""
wlambda_covariance_epic_phase4b_fkg_comonotone.py — Phase 4b of the covariance-kernel proof epic
(qou-x631): test the two off-the-shelf closers for the interval reduction, and CORRECT two
over-statements from the Phase-4 audit.

Phase 4 reduced the kernel (β=3) to the interval inequality
    Cov_β(C₂, ln f) ≤ 0   on β ∈ [2,3]        (C₂ = Σ_□c(□)², ln f = log dimension)
    ⇔  Cov_β(Σ_□c², Σ_□ ln h) ≥ 0  on [2,3]   (since ln f = ln k! − Σ_□ ln h).
The Phase-4 audit suggested this is a Griffiths/FKG-type inequality with C₂, Σln h monotone.
Both suggestions are WRONG; this probe records the corrections as route-eliminations.

CORRECTION 1 — C₂ and Σln h are NOT dominance-monotone.  Both are conjugation-invariant
(`C₂(λ)=C₂(λ')`, `Σln h(λ)=Σln h(λ')`) and U-shaped: large at BOTH extremes (row and column), small
in the balanced middle.  Since conjugation reverses dominance, a conjugation-symmetric function
cannot be dominance-monotone.  (E.g. k=3: (2,1)⊴(1,1,1) but C₂ rises 2→5.)

CORRECTION 2 / ROUTE (FKG on the dominance lattice) — ELIMINATED.  FKG would need `(f^λ)^β`
log-supermodular: `f^{λ∨μ}·f^{λ∧μ} ≥ f^λ·f^μ`.  This holds for k ≤ 7 but FAILS at k = 8
(first counterexample λ=(4,2,1,1), μ=(3,3,2): `f_λ f_μ = 3780 > f_∨ f_∧ = 3136`).  Plus the two
functions are not monotone (Correction 1).  So classical FKG does not apply.

ROUTE (Chebyshev / comonotonicity) — ELIMINATED.  If C₂ and Σln h were comonotone (co-ordered by a
common total order) then `Cov_μ ≥ 0` under EVERY measure μ (Chebyshev's sum inequality) — which would
contradict the Phase-1 4→5 rise anyway.  They are only ~77–80 % concordant (pairwise
`sign(ΔC₂)=sign(ΔΣln h)`); the systematic discordant family is the near-hook pair `(m,2)` vs
`(m,1,1)` (ΔC₂ = −4 while ΔΣln h > 0).  So Chebyshev does not apply.

CORRECTION 3 — the reduction does NOT "sidestep the dimension".  `Σln h = ln k! − ln f^λ`, so the
target `Cov_β(C₂, Σln h)` still contains the log-dimension `ln f`, which is NOT a polynomial function
of the diagram (∉ the Ivanov–Olshanski algebra A).  What the reduction DOES buy is a **lower power of
the dimension**: from the `(f^λ)³`-weighted sum to a `ln f`-covariance (ln f has a convergent Kerov
expansion in the `Σ_μ`; f does not).  That is a genuine simplification, but not an escape.

NET: the interval reduction (Phase 4) stands and lowers the dimension power, but BOTH off-the-shelf
correlation-inequality closers (FKG-on-dominance, Chebyshev-comonotone) are eliminated; the reduced
inequality `Cov_β(C₂, ln f) ≤ 0 on [2,3]` is still genuinely open.  scope-(a); no fit; nothing wired;
no `c_k`; L2 2/7.

# Ref: [fulman2004stein] https://doi.org/10.1090/S0002-9947-04-03499-3
"""
from __future__ import annotations

import math
import sys
from itertools import combinations_with_replacement
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))

NMAX_LSM = 9
NMAX_COMO = 14


def partitions_of(n, m=None):
    if m is None:
        m = n
    if n == 0:
        yield ()
        return
    for i in range(min(n, m), 0, -1):
        for rest in partitions_of(n - i, i):
            yield (i,) + rest


def hooks(l):
    l = list(l)
    if not l:
        return []
    conj = [sum(1 for p in l if p > j) for j in range(l[0])]
    return [(row - j) + (conj[j] - i) - 1 for i, row in enumerate(l) for j in range(row)]


def fdim(l):
    d = 1
    for h in hooks(l):
        d *= h
    return math.factorial(sum(l)) // d


def C2(l):
    return sum((j - i) ** 2 for i, row in enumerate(l) for j in range(row))


def Slnh(l):
    return sum(math.log(h) for h in hooks(l))


def psum(l, L):
    s, acc = [], 0
    for i in range(L):
        acc += l[i] if i < len(l) else 0
        s.append(acc)
    return s


def dom_le(a, b, L):
    pa, pb = psum(a, L), psum(b, L)
    return all(pa[i] <= pb[i] for i in range(L))


def log_supermodular_first_failure(kmax):
    """Return the smallest k where f is NOT log-supermodular on the dominance lattice, + witness."""
    for k in range(3, kmax + 1):
        P = list(partitions_of(k))
        L = k
        f = {p: fdim(p) for p in P}

        def meet(a, b):
            c = [q for q in P if dom_le(q, a, L) and dom_le(q, b, L)]
            for x in c:
                if all(dom_le(y, x, L) for y in c):
                    return x
            return None

        def join(a, b):
            c = [q for q in P if dom_le(a, q, L) and dom_le(b, q, L)]
            for x in c:
                if all(dom_le(x, y, L) for y in c):
                    return x
            return None

        for a, b in combinations_with_replacement(P, 2):
            m, j = meet(a, b), join(a, b)
            if m is None or j is None:
                continue
            if f[j] * f[m] < f[a] * f[b]:
                return k, (a, b, m, j, f[a] * f[b], f[j] * f[m])
    return None, None


def comonotone_fraction(kmax):
    rows = []
    for k in range(3, kmax + 1):
        P = list(partitions_of(k))
        conc = disc = 0
        for i in range(len(P)):
            for jx in range(i + 1, len(P)):
                dC = C2(P[i]) - C2(P[jx])
                dS = Slnh(P[i]) - Slnh(P[jx])
                if abs(dC) < 1e-9 or abs(dS) < 1e-12:
                    continue
                if dC * dS > 0:
                    conc += 1
                else:
                    disc += 1
        tot = conc + disc
        rows.append((k, conc, disc, conc / tot if tot else 1.0))
    return rows


def main() -> int:
    print("=== Covariance-kernel epic (qou-x631) — Phase 4b: FKG + Chebyshev closers eliminated ===\n")

    # Correction 1: monotonicity of C2 / Slnh under dominance (expect NOT monotone).
    k = 3
    P = list(partitions_of(k))
    c2_mono = all(C2(a) <= C2(b) for a in P for b in P if dom_le(a, b, k))
    print(f"CORRECTION 1 — C₂ dominance-monotone (k=3): {c2_mono}  (expected False; C₂ is U-shaped)")

    # Route FKG: log-supermodularity of f on dominance.
    fail_k, wit = log_supermodular_first_failure(NMAX_LSM)
    print(f"\nROUTE FKG (log-supermodular f on dominance): first failure at k={fail_k}")
    if wit:
        a, b, m, j, fab, fjm = wit
        print(f"   counterexample: λ={a}, μ={b} → f_λf_μ={fab} > f_∨f_∧={fjm}  ⇒ FKG ELIMINATED")

    # Route Chebyshev: comonotonicity fraction.
    print(f"\nROUTE Chebyshev (comonotonicity of C₂, Σln h):")
    rows = comonotone_fraction(NMAX_COMO)
    for (kk, conc, disc, frac) in [rows[0], rows[3], rows[7], rows[-1]]:
        print(f"   k={kk:2d}: concord={conc} discord={disc} frac={frac:.4f}")
    not_comonotone = any(frac < 0.999 for (_k, _c, _d, frac) in rows)
    print(f"   NOT comonotone (some discordant pairs): {not_comonotone}  ⇒ Chebyshev ELIMINATED")
    print(f"   systematic discordant family: (m,2) vs (m,1,1)  [ΔC₂=−4 while ΔΣln h>0]")

    fkg_elim = fail_k is not None
    cheby_elim = not_comonotone
    ok = (not c2_mono) and fkg_elim and cheby_elim
    print(f"\nNET: C₂/Σln h not dominance-monotone; FKG eliminated (k={fail_k}); Chebyshev eliminated "
          f"(~77–80% concordant). The interval reduction stands but lowers the dimension POWER only "
          f"(Σln h = ln k! − ln f still ∉ A); Cov_β(C₂,ln f)≤0 on [2,3] remains open.")
    print(f"\nRESULT: both off-the-shelf closers eliminated (honest correction of Phase-4 audit): {ok}")

    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("wlambda-covariance-epic-phase4b-fkg-comonotone", engine="python-exact")
        w.set_description(
            "Phase 4b of the covariance-kernel proof epic (qou-x631): test the two off-the-shelf "
            "closers for the Phase-4 interval reduction Cov_β(C₂,ln f)≤0 on [2,3], and CORRECT two "
            "Phase-4 over-statements. CORRECTION 1: C₂ and Σln h are NOT dominance-monotone — both are "
            "conjugation-invariant and U-shaped (large at row/column extremes, small in the middle). "
            "ROUTE FKG (needs (f^λ)^β log-supermodular on the dominance lattice): ELIMINATED — f is "
            "log-supermodular for k≤7 but FAILS at k=8 (λ=(4,2,1,1),μ=(3,3,2): f_λf_μ=3780>f_∨f_∧=3136). "
            "ROUTE Chebyshev (needs C₂,Σln h comonotone): ELIMINATED — only ~77–80% pairwise concordant "
            "(systematic discordant family (m,2) vs (m,1,1)). CORRECTION 3: the reduction does NOT "
            "sidestep the dimension — Σln h=ln k!−ln f still contains the log-dimension (∉ Ivanov–"
            "Olshanski algebra A); it lowers the dimension POWER (from (f)³-weighting to a ln f-"
            "covariance), a genuine simplification but not an escape. NET: the interval reduction "
            "stands; both off-the-shelf correlation-inequality closers fail; Cov_β(C₂,ln f)≤0 on [2,3] "
            "remains open. scope-(a); no fit; nothing wired; no c_k; L2 2/7.")
        w.add_data("c2_dominance_monotone", bool(c2_mono))
        w.add_data("fkg_log_supermodular_first_failure_k", fail_k)
        w.add_data("fkg_counterexample", {"lambda": list(wit[0]), "mu": list(wit[1]),
                                          "f_lam_f_mu": wit[4], "f_join_f_meet": wit[5]} if wit else None)
        w.add_data("fkg_eliminated", bool(fkg_elim))
        w.add_data("comonotone_fraction_head", [[kk, round(fr, 4)] for (kk, _c, _d, fr) in rows])
        w.add_data("chebyshev_eliminated", bool(cheby_elim))
        w.add_data("dimension_not_sidestepped_note",
                   "Sln h = ln k! - ln f; still the log-dimension, not in algebra A")
        w.add_assertion(
            "covariance_epic_phase4b_off_the_shelf_closers_eliminated",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("C₂/Σln h not dominance-monotone (U-shaped); FKG eliminated (f not log-supermodular, "
                    "fails k=8); Chebyshev eliminated (~77% concordant). Interval reduction stands but "
                    "lowers dimension power only; Cov_β(C₂,ln f)≤0 on [2,3] open. No fit; no c_k."))
        out = w.save()
        print(f"\nWitness: {out}")
    except ImportError as e:
        print(f"\n(witness skipped — witness_base unavailable: {e})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
