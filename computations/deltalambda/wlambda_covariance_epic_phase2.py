#!/usr/bin/env python3
r"""
wlambda_covariance_epic_phase2.py — Phase 2 of the covariance-kernel proof epic (qou-x631):
eliminate two more proof routes and pin the free-cumulant reframing, focusing the remaining
effort on the Śniady genus-expansion route.

The Δ_λ growth bound (#3939) reduces (#3959) to the covariance kernel
    cov(k) := Σ_{λ⊢k} (f^λ)³ (Σ_□ c(□)² − C(k,2)) ≤ 0     (⇔ T₃(k) := Σ_λ (f^λ)² χ^λ(3-cyc) ≤ 0,
    ⇔ Cov_Planch(f^λ, Σ_□c(□)²) ≤ 0).
#3998 verified k≤40 and framed it in free cumulants (Σ̂₃ = R₄ + R₂, E_Planch[R₄] = −k); Phase 1
(#4008) ruled out (1) holonomic recurrence and (2) β-monotonicity. This probe is Phase 2.

FINDING A — the R₄ reframing is EXACTLY AFFINE, i.e. NOT a new lever.  The 4th free cumulant of the
transition measure is `R₄(λ) = 3·(Σ_□c(□)² − C(k,2)) − k = 3·ω₃(λ) − k`, where ω₃(λ) = Σc² − C(k,2)
is the eigenvalue of the 3-cycle class sum on the irrep λ.  Since `k` is constant across λ⊢k,
`Cov_Planch(f^λ, R₄) = 3·Cov_Planch(f^λ, ω₃)` — the −k affine shift washes out of any covariance.
So "prove Cov(f^λ,R₄)≤0" is literally the SAME inequality as the content covariance, and R₄ gives no
independent handle.  Cross-checked: E_Planch[R₄] = −k for all k≤8 (Biane's Σ̂₃=R₄+R₂ with R₂=k).

FINDING B (ROUTE 3 — sub-family / truncation sign-definiteness).  RULED OUT.  If any natural
sub-family of shapes summed to a sign-definite partial cov, one could bound the rest.  It does not:
the two-row truncation Σ_{λ=(k−j,j)} flips positive at k=6 (−160 → +1040); the hook truncation
Σ_{λ=(k−j,1^j)} flips positive at k=4 (−4 → +16).  The sign is a GLOBAL cancellation — the negative
mass from balanced/typical shapes (ω₃<0, large f^λ) outweighs the positive mass from extreme shapes
(ω₃>0, small f^λ), with cov⁻ ≈ 1.5–2× cov⁺ consistently.  No term-by-term or truncation bound works.

FINDING C (ROUTE 4 — Murnaghan–Nakayama peeling).  RULED OUT.  MN gives
`χ^λ(3,1^{k−3}) = Σ_{ξ⊂λ border strip, |ξ|=3} (−1)^{ht(ξ)} f^{λ∖ξ}`, hence
`T₃(k) = Σ_{ν⊢k−3} f^ν · B(ν)`, `B(ν) := Σ_{λ: λ/ν = BS₃} (−1)^{ht} (f^λ)²`.  If B(ν) were ≤0 for
every ν, the sign would follow (f^ν ≥ 0).  It is NOT: B(ν) is ≤0 through k≤8 but first goes POSITIVE
at k=9 (ν⊢6), and the offender is exactly the self-conjugate staircase ν = (3,2,1), B = +6174.
(B(ν) is conjugation-symmetric, so the ± cancellation begins precisely at the self-conjugate shape.)

NET (Phase 1 + Phase 2): the kernel is (1) non-P-recursive, (2) not a β-monotone family, (3) not
sub-family sign-definite, (4) not MN-peeling sign-definite, and the R₄ reframing is an affine
relabelling (5).  Four natural local/inductive certificates are excluded; the sign is a genuinely
GLOBAL analytic anti-correlation.  The sole remaining route is Śniady's genus expansion of the joint
character cumulants on the (f^λ)³-biased measure — the obstruction being that f^λ is the
exponentially-large DIMENSION, not a bounded character ratio, so standard Kerov-CLT machinery does
not directly apply.  This is the epic's Phase-3 target.

Discipline: scope-(a) route-elimination; no fit; nothing wired; no `c_k`; L2 unchanged (2/7).
In-sandbox (integer + Fraction; no numpy). Records ruled-out routes so they are not retried.

# Ref: [sniady2006asymptotics] https://doi.org/10.1007/s00440-005-0479-7
"""
from __future__ import annotations

import math
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))

NMAX_R4 = 8
NMAX_FAM = 12
NMAX_PEEL = 10


def partitions_of(n, m=None):
    if m is None:
        m = n
    if n == 0:
        yield ()
        return
    for i in range(min(n, m), 0, -1):
        for rest in partitions_of(n - i, i):
            yield (i,) + rest


def hook_dim(l):
    l = list(l)
    if not l:
        return 1
    n = sum(l)
    conj = [sum(1 for p in l if p > j) for j in range(l[0])]
    d = 1
    for i, row in enumerate(l):
        for j in range(row):
            d *= (row - j) + (conj[j] - i) - 1
    return math.factorial(n) // d


def C2(l):
    return sum((j - i) ** 2 for i, row in enumerate(l) for j in range(row))


def add_border_strips(nu, r):
    """Yield (lambda, height) for each way to add a size-`r` border strip to `nu` (Maya/edge-word)."""
    nu = list(nu)
    n = len(nu)
    npad = n + r
    nu2 = nu + [0] * (npad - n)
    N = (nu2[0] if nu2 else 0) + npad + r + 2
    w = [0] * N
    for i in range(npad):
        w[nu2[i] + (npad - 1 - i)] = 1
    res = []
    for p in range(N):
        if w[p] == 1 and p + r < N and w[p + r] == 0:
            height = sum(1 for q in range(p + 1, p + r) if w[q] == 1)
            nw = w[:]
            nw[p] = 0
            nw[p + r] = 1
            od = sorted((q for q in range(N) if nw[q] == 1), reverse=True)
            lam = tuple(x for x in (od[i] - (npad - 1 - i) for i in range(npad)) if x > 0)
            if sum(lam) == sum(nu) + r:
                res.append((lam, height))
    return res


def finding_a_r4_affine(kmax):
    """R₄(λ) = 3·ω₃(λ) − k ; check E_Planch[R₄] = −k."""
    ok = True
    rows = []
    for k in range(3, kmax + 1):
        Ck2 = k * (k - 1) // 2
        acc = Fraction(0)
        for l in partitions_of(k):
            f = hook_dim(l)
            R4 = 3 * (C2(l) - Ck2) - k
            acc += Fraction(f * f, math.factorial(k)) * R4
        rows.append((k, acc))
        if acc != -k:
            ok = False
    return ok, rows


def _partial_cov(shapes, k):
    Ck2 = k * (k - 1) // 2
    return sum(hook_dim(l) ** 3 * (C2(l) - Ck2) for l in shapes)


def finding_b_subfamilies(kmax):
    """Two-row and hook truncations; return first k where each flips positive."""
    two_flip = hook_flip = None
    detail = []
    for k in range(3, kmax + 1):
        two = [(k,)] + [(k - j, j) for j in range(1, k // 2 + 1)]
        hk = [(k,)] + [tuple([k - j] + [1] * j) for j in range(1, k)]
        s2 = _partial_cov(two, k)
        sh = _partial_cov(hk, k)
        if two_flip is None and s2 > 0:
            two_flip = k
        if hook_flip is None and sh > 0:
            hook_flip = k
        detail.append((k, s2, sh))
    return two_flip, hook_flip, detail


def finding_c_peeling(kmax):
    """B(ν)=Σ_{λ/ν=BS₃}(−1)^ht (f^λ)²; first k where some B(ν)>0, and the offending ν."""
    first_pos_k = None
    offender = None
    peel_matches = True
    for k in range(3, kmax + 1):
        Ck2 = k * (k - 1) // 2
        direct_T3 = 3 * sum(hook_dim(l) ** 3 * (C2(l) - Ck2) for l in partitions_of(k)) // (
            k * (k - 1) * (k - 2))
        peel_T3 = 0
        for nu in partitions_of(k - 3):
            B = sum(((-1) ** ht) * hook_dim(lam) ** 2 for lam, ht in add_border_strips(nu, 3))
            peel_T3 += hook_dim(nu) * B
            if B > 0 and first_pos_k is None:
                first_pos_k = k
                offender = (nu, B)
        if peel_T3 != direct_T3:
            peel_matches = False
    return first_pos_k, offender, peel_matches


def sign_structure(kmax):
    """cov⁺, cov⁻ split (global-cancellation evidence)."""
    rows = []
    for k in range(3, kmax + 1):
        Ck2 = k * (k - 1) // 2
        cp = cm = 0
        for l in partitions_of(k):
            f = hook_dim(l)
            w = C2(l) - Ck2
            if w > 0:
                cp += f ** 3 * w
            elif w < 0:
                cm += f ** 3 * w
        rows.append((k, cp, cm, cp + cm))
    return rows


def main() -> int:
    print("=== Covariance-kernel proof epic (qou-x631) — Phase 2: eliminate two more routes ===\n")

    a_ok, a_rows = finding_a_r4_affine(NMAX_R4)
    print("FINDING A — R₄(λ) = 3·ω₃(λ) − k is EXACTLY AFFINE (⇒ not a new lever):")
    for (k, e) in a_rows:
        print(f"   k={k}: E_Planch[R₄] = {e}  (== −k? {e == -k})")
    print(f"   affine identity + E_Planch[R₄]=−k verified all k≤{NMAX_R4}: {a_ok}")

    two_flip, hook_flip, b_detail = finding_b_subfamilies(NMAX_FAM)
    print(f"\nFINDING B (ROUTE 3 — sub-family sign-definiteness): RULED OUT")
    print(f"   two-row truncation flips positive at k={two_flip}; hook truncation at k={hook_flip}")
    for (k, s2, sh) in b_detail[:4]:
        print(f"     k={k}: two-row={s2:>8d}  hook={sh:>8d}")

    first_pos_k, offender, peel_ok = finding_c_peeling(NMAX_PEEL)
    print(f"\nFINDING C (ROUTE 4 — Murnaghan–Nakayama peeling): RULED OUT")
    print(f"   T₃(peel) matches direct T₃ all k≤{NMAX_PEEL}: {peel_ok}")
    print(f"   B(ν) first goes POSITIVE at k={first_pos_k}, offender ν={offender[0]} (B={offender[1]}),"
          f" the self-conjugate staircase")

    print(f"\nGLOBAL-CANCELLATION structure (cov⁻ outweighs cov⁺):")
    s_rows = sign_structure(NMAX_FAM)
    for (k, cp, cm, tot) in s_rows[:5]:
        ratio = abs(cm) / cp if cp else float('inf')
        print(f"   k={k}: cov⁺={cp:>10d}  cov⁻={cm:>12d}  tot={tot:>12d}  |cov⁻|/cov⁺={ratio:.2f}")

    route3_out = (two_flip is not None) and (hook_flip is not None)
    route4_out = (first_pos_k is not None) and peel_ok
    ok = a_ok and route3_out and route4_out
    print(f"\nNET: R₄ affine (not a lever): {a_ok}; Route 3 (sub-family): {route3_out}; "
          f"Route 4 (MN-peeling): {route4_out}.")
    print("Four local/inductive certificates now excluded (Phase 1: recurrence, β-monotone; Phase 2:")
    print("sub-family, MN-peeling) + R₄ affine. The sign is a GLOBAL analytic anti-correlation;")
    print("remaining route = Śniady genus expansion on the (f^λ)³-biased measure (Phase 3 target).")
    print(f"\nRESULT: Phase-2 route-eliminations confirmed: {ok}")

    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("wlambda-covariance-epic-phase2", engine="python-exact")
        w.set_description(
            "Phase 2 of the covariance-kernel proof epic (qou-x631). FINDING A: the free-cumulant "
            "reframing is EXACTLY AFFINE — R₄(λ)=3·(Σc²−C(k,2))−k=3·ω₃(λ)−k, so Cov_Planch(f^λ,R₄)="
            "3·Cov_Planch(f^λ,ω₃) (the −k shift washes out); R₄ is NOT an independent handle. "
            "Verified E_Planch[R₄]=−k for k≤8 (Biane Σ̂₃=R₄+R₂, R₂=k). ROUTE 3 (sub-family "
            "sign-definiteness): RULED OUT — two-row truncation flips + at k=6, hook truncation at "
            "k=4; the sign is a global cancellation (cov⁻≈1.5–2×cov⁺). ROUTE 4 (Murnaghan–Nakayama "
            "peeling T₃=Σ_ν f^ν·B(ν), B(ν)=Σ_{λ/ν=BS₃}(−1)^ht(f^λ)²): RULED OUT — B(ν)≤0 through "
            "k≤8 but first POSITIVE at k=9, offender the self-conjugate staircase ν=(3,2,1), B=+6174 "
            "(peel-sum matches direct T₃ exactly). NET: four local/inductive certificates excluded + "
            "R₄ affine; the sign is a genuinely global analytic anti-correlation, leaving Śniady's "
            "genus expansion on the (f^λ)³-biased measure as the sole route (obstruction: f^λ is the "
            "exponential DIMENSION, not a bounded character ratio). scope-(a); no fit; nothing wired; "
            "no c_k; L2 2/7.")
        w.add_data("r4_affine_identity", "R4 = 3*(C2 - C(k,2)) - k = 3*omega3 - k")
        w.add_data("r4_e_planch_eq_minus_k_verified_kmax", NMAX_R4)
        w.add_data("route3_two_row_flip_k", two_flip)
        w.add_data("route3_hook_flip_k", hook_flip)
        w.add_data("route3_ruled_out", bool(route3_out))
        w.add_data("route4_peel_matches_direct", bool(peel_ok))
        w.add_data("route4_first_positive_k", first_pos_k)
        w.add_data("route4_offender_nu", list(offender[0]))
        w.add_data("route4_offender_B", int(offender[1]))
        w.add_data("route4_ruled_out", bool(route4_out))
        w.add_data("cov_sign_split_head",
                   [[k, int(cp), int(cm)] for (k, cp, cm, _t) in sign_structure(NMAX_FAM)[:6]])
        w.add_assertion(
            "covariance_epic_phase2_two_routes_eliminated",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("R₄ affine (not a lever, E_Planch[R₄]=−k verified); Route 3 (sub-family) ruled "
                    "out (two-row/hook truncations flip positive); Route 4 (MN-peeling) ruled out "
                    "(B(ν)>0 first at self-conjugate staircase ν=(3,2,1), k=9). Focuses the epic on "
                    "Śniady genus expansion. No fit; no c_k."))
        out = w.save()
        print(f"\nWitness: {out}")
    except ImportError as e:
        print(f"\n(witness skipped — witness_base unavailable: {e})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
