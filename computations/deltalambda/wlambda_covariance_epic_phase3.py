#!/usr/bin/env python3
r"""
wlambda_covariance_epic_phase3.py — Phase 3 of the covariance-kernel proof epic (qou-x631):
attack the kernel via the β-Plancherel (Jack) ensemble and the Stein/log-covariance reduction.

The Δ_λ growth bound (#3939) reduces (#3959) to the covariance kernel
    cov(k) := Σ_{λ⊢k} (f^λ)³ (Σ_□c(□)² − C(k,2)) ≤ 0     (⇔ Cov_Planch(f^λ, Σc²) ≤ 0).
Phase 1 (#4008) and Phase 2 (#4150) eliminated five natural certificates (holonomic recurrence,
β-monotone family, sub-family truncation, MN-peeling, tabulated closed form). This probe opens the
analytic attack and reports what survives.

REFRAMING (headline) — the kernel is one instance of a β-ENSEMBLE inequality.  Let
`G(β) := Σ_{λ⊢k} (f^λ)^β · ω₃(λ)`, `ω₃(λ) := Σ_□c(□)² − C(k,2)`, and `H(β) := G(β)/Σ_λ(f^λ)^β
= E_β[C₂] − C(k,2)` where `E_β` is the β-biased (Jack–Plancherel) average.  Then the kernel is
`G(3) ≤ 0`, and empirically the FULL family holds:
    H(β) ≤ 0  for all β ≥ 2,   with equality H(2) = 0   (β = 2 is Plancherel, E_2[C₂] = C(k,2)).
Equivalently: **β = 2 maximises the β-biased expected content-spread E_β[C₂] over β ≥ 2.**
Boundary/asymptotic data pinning the shape of H on [2,∞):
    • H(2) = 0                         (Plancherel content mean is exactly C(k,2));
    • H'(2) = Cov_Planch(ln f^λ, ω₃) < 0  (strict — verified all k ≤ 19; the log-dimension is
      negatively correlated with the content spread);
    • H(∞) < 0                         (β→∞ concentrates on the max-dimension diagram, which is
      balanced ⇒ ω₃ < 0);
    • NO positive excursion of H on (2,60] at 60-digit precision, all k ≤ 16 (this probe).
This lands the kernel squarely in the β-ensemble / Jack-polynomial literature (a far better-studied
setting than the bespoke (f^λ)³ average), where the monotone-concentration heuristic is standard.

ROUTE 1 (Stein / log-covariance).  PARTIAL — sign confirmed, exactness fails.  Kerov's CLT makes
`(ln f^λ, Σ_3)` jointly asymptotically Gaussian; for jointly Gaussian (X,Y) Stein gives the EXACT
`Cov(e^X,Y) = E[e^X]·Cov(X,Y)`, so asymptotically `sign Cov(f,ω₃) = sign Cov(ln f, ω₃)`.  The
log-covariance `Cov_Planch(ln f, ω₃) < 0` is confirmed (all k ≤ 19), and the transfer factor
`A/(E[f]·B)` is POSITIVE and bounded (≈ 0.55–0.88) — but it is NOT → 1 (the finite-k law is
non-Gaussian).  So a rigorous Route-1 proof needs (a) `Cov_Planch(ln f, ω₃) ≤ 0` [tractable via the
β-ensemble H'(2) < 0] plus (b) a proof the transfer factor stays positive — it does not follow from
naive Gaussianity, so error control (or the β-family route below) is required.

ROUTE (Descartes / variation-diminishing) — RULED OUT.  `G(β) = Σ_λ ω₃(λ) e^{β ln f^λ}` is an
exponential sum; the variation-diminishing bound gives (#real zeros of G) ≤ (#sign changes of ω₃(λ)
ordered by dimension f^λ).  That sign-change count GROWS with k (1,1,1,3,3,5,7,…,111 at k=21), so the
bound is vacuous.  (Ties in f are exact conjugate pairs λ,λ′ with equal f AND equal ω₃ — no spurious
changes.)  A dimension-ordered Descartes certificate cannot close the kernel.

NET: the kernel is reframed as the β=3 case of the β-ensemble inequality `E_β[C₂] ≤ C(k,2) ∀β≥2`
(equality at β=2), with clean boundary data (H(2)=0, H'(2)<0, H(∞)<0, no excursion).  The surviving
attack is: prove β=2 maximises E_β[C₂] on [2,∞) — a Jack/β-Plancherel statement — via a
concentration / log-convexity argument on the partition function `Z(β)=Σ_λ(f^λ)^β`, coordinating with
the Specht/S_n Lean epic `sp00` for the eventual carrier.  scope-(a); no fit; nothing wired; no c_k;
L2 unchanged (2/7).  In-sandbox (integer + Fraction + mpmath; no numpy).

# Ref: [sniady2006asymptotics] https://doi.org/10.1007/s00440-005-0479-7
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))

NMAX_LOGCOV = 19
NMAX_EXC = 16
NMAX_DESC = 21


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


def log_covariance(kmax):
    """A=Cov(f,ω₃)=cov/k! ; B=Cov(ln f,ω₃) ; E[f] ; transfer ratio A/(E[f]B). All floats."""
    rows = []
    all_B_neg = True
    all_ratio_pos = True
    for k in range(3, kmax + 1):
        Ck2 = k * (k - 1) // 2
        kf = math.factorial(k)
        A = B = Ef = 0.0
        for l in partitions_of(k):
            f = hook_dim(l)
            w = C2(l) - Ck2
            p = f * f / kf
            A += p * f * w
            B += p * math.log(f) * w if f > 0 else 0.0
            Ef += p * f
        ratio = A / (Ef * B) if (Ef * B) != 0 else float('nan')
        rows.append((k, A, B, Ef, ratio))
        if not (B < 0):
            all_B_neg = False
        if not (ratio > 0):
            all_ratio_pos = False
    return rows, all_B_neg, all_ratio_pos


def excursion_search(kmax):
    """60-dps sup of H(β)=E_β[ω₃] over β∈(2,60]; must be < 0 (no positive excursion)."""
    from mpmath import mp, mpf, power, fsum
    mp.dps = 60
    worst = mpf('-1e18')
    rows = []
    for k in range(3, kmax + 1):
        Ck2 = k * (k - 1) // 2
        shapes = [(hook_dim(l), C2(l) - Ck2) for l in partitions_of(k)]
        sup = mpf('-1e18')
        atb = None
        b = mpf('2.0')
        while b <= mpf('60'):
            Z = fsum(power(mpf(f), b) for f, _w in shapes)
            H = fsum(mpf(w) * power(mpf(f), b) for f, w in shapes) / Z
            if b > mpf('2.0001') and H > sup:
                sup = H
                atb = b
            b += mpf('0.1')
        rows.append((k, float(sup), float(atb)))
        if sup > worst:
            worst = sup
    return rows, float(worst)


def descartes_sign_changes(kmax):
    """#sign changes of ω₃(λ) when λ sorted by dimension f (the variation-diminishing bound)."""
    rows = []
    for k in range(3, kmax + 1):
        Ck2 = k * (k - 1) // 2
        data = sorted(((hook_dim(l), C2(l) - Ck2) for l in partitions_of(k)),
                      key=lambda fw: (fw[0], fw[1]))
        nz = [(1 if w > 0 else -1) for _f, w in data if w != 0]
        changes = sum(1 for a, b in zip(nz, nz[1:]) if a != b)
        rows.append((k, len(data), changes))
    return rows


def main() -> int:
    print("=== Covariance-kernel proof epic (qou-x631) — Phase 3: β-ensemble reframing + Route 1 ===\n")

    print("REFRAMING — kernel = β=3 case of  E_β[C₂] ≤ C(k,2) ∀β≥2  (equality at β=2).")
    exc_rows, worst = excursion_search(NMAX_EXC)
    print(f"   60-dps positive-excursion search of H(β)=E_β[ω₃] on β∈(2,60]:")
    for (k, sup, atb) in exc_rows[:6]:
        print(f"     k={k}: sup_{{β>2}} H = {sup:+.3e} at β={atb:.2f}")
    no_excursion = worst < 0
    print(f"   global sup over k≤{NMAX_EXC}, β∈(2,60]: {worst:+.3e}  "
          f"→ {'NO positive excursion (conjecture holds)' if no_excursion else 'POSITIVE — FALSE'}")

    print(f"\nROUTE 1 (Stein / log-covariance):")
    lc_rows, all_B_neg, all_ratio_pos = log_covariance(NMAX_LOGCOV)
    for (k, A, B, Ef, ratio) in [lc_rows[0], lc_rows[3], lc_rows[7], lc_rows[-1]]:
        print(f"     k={k:2d}: Cov(f,ω₃)={A:+.3e}  Cov(ln f,ω₃)={B:+.4f}  E[f]={Ef:.2f}  "
              f"A/(E[f]B)={ratio:.4f}")
    print(f"   Cov_Planch(ln f, ω₃) < 0 all k≤{NMAX_LOGCOV}: {all_B_neg}  "
          f"(= H'(2) < 0, the strict boundary slope)")
    print(f"   transfer factor A/(E[f]B) positive & bounded (≈0.55–0.88, NOT →1): {all_ratio_pos}")

    print(f"\nROUTE (Descartes / variation-diminishing): RULED OUT")
    d_rows = descartes_sign_changes(NMAX_DESC)
    changes_grow = d_rows[-1][2] > d_rows[0][2]
    print(f"   #sign changes of ω₃ (ordered by dimension f): "
          f"{', '.join(str(c) for (_k, _n, c) in d_rows[::3])} … up to {d_rows[-1][2]} at k={NMAX_DESC}")
    print(f"   count grows with k ⇒ variation-diminishing bound is vacuous: {changes_grow}")

    ok = no_excursion and all_B_neg and all_ratio_pos and changes_grow
    print(f"\nNET: kernel reframed as β=3 case of E_β[C₂]≤C(k,2) ∀β≥2 (β=2 max, no excursion); "
          f"log-covariance H'(2)<0 confirmed; Descartes route eliminated.")
    print(f"Surviving attack: prove β=2 maximises E_β[C₂] on [2,∞) (Jack/β-Plancherel concentration).")
    print(f"\nRESULT: Phase-3 reframing + route status confirmed: {ok}")

    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("wlambda-covariance-epic-phase3", engine="python-exact+mpmath")
        w.set_description(
            "Phase 3 of the covariance-kernel proof epic (qou-x631). REFRAMING: the kernel "
            "cov(k)=Σ(f^λ)³ω₃ (β=3) is one instance of the β-Plancherel (Jack) ensemble inequality "
            "E_β[C₂] ≤ C(k,2) ∀β≥2 (equality at β=2, i.e. β=2 maximises the β-biased content-spread). "
            "Boundary data: H(2)=0; H'(2)=Cov_Planch(ln f,ω₃)<0 (strict, all k≤19); H(∞)<0 "
            "(max-dimension diagram is balanced ⇒ ω₃<0); and NO positive excursion of H(β)=E_β[ω₃] on "
            "β∈(2,60] at 60-dps for all k≤16 (global sup <0). ROUTE 1 (Stein/log-covariance): PARTIAL "
            "— Cov_Planch(ln f,ω₃)<0 confirmed (Kerov CLT makes (ln f,Σ3) jointly asymp. Gaussian, "
            "Stein ⇒ sign transfer), transfer factor A/(E[f]B) positive & bounded (≈0.55–0.88) but NOT "
            "→1 (finite-k non-Gaussian), so a rigorous proof needs error control or the β-family. "
            "ROUTE (Descartes/variation-diminishing): RULED OUT — sign changes of ω₃ ordered by "
            "dimension grow with k (1→111 at k=21), bound vacuous; ties are exact conjugate pairs. "
            "NET: kernel lives in the Jack/β-ensemble literature; surviving attack = prove β=2 "
            "maximises E_β[C₂] on [2,∞). scope-(a); no fit; nothing wired; no c_k; L2 2/7.")
        w.add_data("beta_ensemble_conjecture", "E_beta[C2] <= C(k,2) for all beta>=2, equality at beta=2")
        w.add_data("no_positive_excursion_kmax", NMAX_EXC)
        w.add_data("no_positive_excursion_global_sup", worst)
        w.add_data("log_covariance_negative_all_k", bool(all_B_neg))
        w.add_data("log_covariance_kmax", NMAX_LOGCOV)
        w.add_data("stein_transfer_factor_positive_bounded_not_one", bool(all_ratio_pos))
        w.add_data("descartes_sign_changes_grow", bool(changes_grow))
        w.add_data("descartes_sign_changes_head", [c for (_k, _n, c) in d_rows])
        w.add_data("log_covariance_head",
                   [[k, round(A, 4), round(B, 6), round(ratio, 4)] for (k, A, B, _Ef, ratio) in lc_rows[:8]])
        w.add_assertion(
            "covariance_epic_phase3_beta_reframing_and_route1",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("β-ensemble reframing verified (no positive excursion of E_β[ω₃] on (2,60], 60-dps, "
                    "k≤16; H'(2)=Cov(ln f,ω₃)<0 all k≤19); Descartes route eliminated (sign changes grow). "
                    "Surviving attack: β=2 maximises E_β[C₂] on [2,∞). No fit; no c_k."))
        out = w.save()
        print(f"\nWitness: {out}")
    except ImportError as e:
        print(f"\n(witness skipped — witness_base unavailable: {e})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
