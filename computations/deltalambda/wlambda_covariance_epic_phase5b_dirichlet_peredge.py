#!/usr/bin/env python3
r"""
wlambda_covariance_epic_phase5b_dirichlet_peredge.py — Phase 5b of the covariance-kernel proof epic
(qou-x631): the kernel is a Dirichlet-form sign, and the per-edge (local) sign certificate FAILS.

Phase 5 built the Plancherel-reversible down-up chain and showed
    E_P[(f(λ*)−f(λ)) · ω₃(λ)] = −(3/n) · Cov_P(f, ω₃) = −(3/n) cov(n)/n!.
Symmetrising over the exchangeable pair gives the DIRICHLET FORM identity
    E_P[(Δf)(Δω₃)] = 2·ℰ(f, ω₃),   ℰ(g,h) := ½ Σ_{λ,λ*} P(λ)K(λ,λ*)(g(λ*)−g(λ))(h(λ*)−h(λ)),
and ℰ(f,ω₃) = ⟨f,(I−K)ω₃⟩_P = τ₃⟨f,ω₃⟩_P = (3/n)·cov(n)/n!  (verified exactly, n≤9).
So the kernel is exactly the sign of a Dirichlet form:  **cov(n) ≤ 0  ⇔  ℰ(f, ω₃) ≤ 0.**

ℰ(f,ω₃) is a sum over chain EDGES with NON-NEGATIVE weights `P(λ)K(λ,λ*)`, of `(Δf)(Δω₃)` where
`Δω₃ = c_add² − c_rm²` (contents of the moved box).  If `(Δf)(Δω₃) ≤ 0` on EVERY edge, ℰ ≤ 0 would
follow immediately (a clean local proof).

RESULT — the per-edge certificate is ELIMINATED.  Bad edges (`(Δf)(Δω₃) > 0` — dimension and
content-spread move the SAME way) exist and their count grows with n (n=3..9: 0, 4, 4, 12, 16, 32,
40).  Archetype at n=4: the move `(3,1) → (2,2)` has `Δf = −1, Δω₃ = −4` — the MORE balanced square
`(2,2)` has LOWER dimension (2) than the hook-like `(3,1)` (dim 3).  So "max-dimension diagram = most
balanced" is FALSE at finite n (it holds only asymptotically, VKLS), and the sign of the kernel is a
WEIGHTED cancellation over edges, not a local per-edge fact — mirroring every earlier phase.

NET: the kernel = `ℰ(f,ω₃) ≤ 0` (a Dirichlet-form sign); the per-edge / local-certificate route is
eliminated.  The remaining Route-1 path is the JOINT Stein CLT of `(f, ω₃)` with an effective
Berry–Esseen error (Fulman gives only the marginal transposition CLT at `n^{−1/4}`) — genuine
multi-session research.  scope-(a); no fit; nothing wired; no `c_k`; L2 2/7.  In-sandbox (exact
`Fraction`).

# Ref: [fulman2004stein] https://doi.org/10.1090/S0002-9947-04-03499-3
"""
from __future__ import annotations

import math
import sys
from fractions import Fraction as Fr
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))

NMAX = 9


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


def dim(l):
    d = 1
    for h in hooks(l):
        d *= h
    return math.factorial(sum(l)) // d


def C2(l):
    return sum((j - i) ** 2 for i, row in enumerate(l) for j in range(row))


def corners_remove(l):
    l = list(l)
    out = []
    for i in range(len(l)):
        if (i == len(l) - 1 and l[i] >= 1) or (i < len(l) - 1 and l[i] > l[i + 1]):
            m = l[:]
            m[i] -= 1
            out.append(tuple(x for x in m if x > 0))
    return out


def boxes_add(m, n):
    m = list(m)
    out = []
    for i in range(len(m) + 1):
        cur = m[i] if i < len(m) else 0
        prev = m[i - 1] if i > 0 else 10 ** 9
        if cur < prev:
            a = m[:]
            if i < len(m):
                a[i] += 1
            else:
                a = a + [1]
            out.append(tuple(a))
    return out


def main() -> int:
    print("=== Covariance-kernel epic (qou-x631) — Phase 5b: Dirichlet form; per-edge cert fails ===\n")
    all_id = True
    bad_counts = []
    example = None
    for n in range(3, NMAX + 1):
        P = list(partitions_of(n))
        dm = {p: dim(p) for p in P}
        fact = math.factorial(n)
        dirich = Fr(0)
        edges = bad = 0
        for a in P:
            Pa = Fr(dm[a] ** 2, fact)
            Krow = {}
            for mu in corners_remove(a):
                pd = Fr(dim(mu), dm[a])
                for b in boxes_add(mu, n):
                    Krow[b] = Krow.get(b, Fr(0)) + pd * Fr(dm[b], n * dim(mu))
            for b, kab in Krow.items():
                if b == a:
                    continue
                Df = dm[b] - dm[a]
                Dom = C2(b) - C2(a)
                edges += 1
                if Df * Dom > 0:
                    bad += 1
                    if n == 4 and example is None:
                        example = (a, b, Df, Dom)
                dirich += Fr(1, 2) * Pa * kab * Fr(Df * Dom)
        kernel = sum(dm[p] ** 3 * (C2(p) - (n * (n - 1) // 2)) for p in P)
        pred = Fr(3, n) * Fr(kernel, fact)
        idok = (dirich == pred)
        all_id &= idok
        bad_counts.append(bad)
        print(f"n={n}: edges={edges} bad(ΔfΔω₃>0)={bad}  ℰ(f,ω₃)={dirich} = τ₃·cov/n!={pred} ({idok})")

    per_edge_fails = any(b > 0 for b in bad_counts)
    ok = all_id and per_edge_fails
    print(f"\nDirichlet identity ℰ(f,ω₃)=τ₃·cov/n! holds all n≤{NMAX}: {all_id}")
    print(f"per-edge sign certificate (ΔfΔω₃≤0 ∀ edges): FAILS (bad counts {bad_counts})")
    if example:
        print(f"   archetype (n=4): move {example[0]}→{example[1]}, Δf={example[2]}, Δω₃={example[3]} "
              f"— more-balanced (2,2) has LOWER dim than hook-like (3,1)")
    print(f"\nNET: kernel ⇔ ℰ(f,ω₃)≤0 (Dirichlet-form sign); per-edge/local certificate ELIMINATED "
          f"(weighted cancellation; max-dim shape ≠ most balanced at finite n). Remaining Route-1 "
          f"path = joint Stein CLT with effective Berry–Esseen error.")
    print(f"\nRESULT: Dirichlet reformulation + per-edge elimination verified: {ok}")

    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("wlambda-covariance-epic-phase5b-dirichlet-peredge", engine="python-exact")
        w.set_description(
            "Phase 5b of the covariance-kernel proof epic (qou-x631): the kernel is a Dirichlet-form "
            "sign, and the per-edge (local) certificate fails. Symmetrising the Phase-5 exchangeable "
            "pair gives E_P[(Δf)(Δω₃)]=2ℰ(f,ω₃) with ℰ(f,ω₃)=τ₃⟨f,ω₃⟩_P=(3/n)cov(n)/n! (verified "
            "exactly n≤9), so cov(n)≤0 ⇔ ℰ(f,ω₃)≤0. ℰ is a sum over chain edges with non-negative "
            "weights P(λ)K(λ,λ*) of (Δf)(Δω₃), Δω₃=c_add²−c_rm². PER-EDGE SIGN CERTIFICATE ELIMINATED: "
            "bad edges (ΔfΔω₃>0, dimension and content-spread move the same way) exist and grow with n "
            "(0,4,4,12,16,32,40 for n=3..9); archetype (3,1)→(2,2) at n=4 has Δf=−1,Δω₃=−4 (the more "
            "balanced square (2,2) has LOWER dimension than the hook-like (3,1)). So 'max-dim=most "
            "balanced' is false at finite n (VKLS only asymptotic), and the kernel sign is a weighted "
            "cancellation, not a local fact. Remaining Route-1 path = joint Stein CLT with effective "
            "Berry–Esseen error. scope-(a); no fit; nothing wired; no c_k; L2 2/7.")
        w.add_data("dirichlet_identity", "E(f,om3) = tau3 * cov(n)/n!, tau3=3/n")
        w.add_data("dirichlet_identity_verified", bool(all_id))
        w.add_data("kernel_iff", "cov(n) <= 0  <=>  Dirichlet form E(f,om3) <= 0")
        w.add_data("per_edge_bad_counts_n3to9", bad_counts)
        w.add_data("per_edge_certificate_fails", bool(per_edge_fails))
        w.add_data("archetype_bad_edge_n4", {"from": [3, 1], "to": [2, 2], "Df": -1, "Dom3": -4})
        w.add_data("remaining_route", "joint Stein CLT with effective Berry-Esseen error")
        w.add_assertion(
            "covariance_epic_phase5b_dirichlet_peredge",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("Kernel = Dirichlet-form sign ℰ(f,ω₃)≤0 (identity ℰ=τ₃·cov/n! verified n≤9); "
                    "per-edge sign certificate ELIMINATED (bad edges grow with n; max-dim shape not "
                    "most balanced at finite n). Remaining path = joint Stein CLT effective error. "
                    "No fit; no c_k."))
        out = w.save()
        print(f"\nWitness: {out}")
    except ImportError as e:
        print(f"\n(witness skipped — witness_base unavailable: {e})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
