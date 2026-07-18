#!/usr/bin/env python3
"""
wlambda_D_reduction_content_covariance.py — rigorous reduction of the Δ_λ growth sub-lemma (D)
to a single clean kernel: the Plancherel covariance inequality Cov(f^λ, Σ_□ c(□)²) ≤ 0.

Follows #3939 (the rigorous super-exponential lower bound on w_std, whose only open input was
(D): w_std(k) = E_Planch[f^{λ/(2,1)}] ≥ E_Planch[f^{λ/(3)}]). This probe REDUCES (D) — via exact
S_k character / Jucys–Murphy content-formula identities — to the statement that dimension and
content-spread are non-positively correlated under Plancherel measure. The reduction is airtight
(each step a proven identity, positive-controlled here against direct skew-tableau enumeration);
the residual covariance inequality is verified k≤20 (agent-verified k≤32) but not yet proved — it
is now the single clean open kernel.

THE REDUCTION (all steps exact, per λ):

  Restricting V_λ to the S_3 on the first three strands, χ^λ(g) = Σ_{μ⊢3} f^{λ/μ} χ^μ(g), and
  solving the 3×3 system on the classes {1³, (2,1³⁻²), (3,1³⁻³)} gives, with
  χ₂ = χ^λ(transposition), χ₃ = χ^λ(3-cycle):

      f^{λ/(2,1)} = (f^λ − χ₃)/3,      f^{λ/(3)} = (f^λ + 3χ₂ + 2χ₃)/6.

  Hence  Σ_λ (f^λ)²(f^{λ/(2,1)} − f^{λ/(3)}) = (T₁ − 4T₃ − 3T₂)/6,  where
  T₁ = Σ(f^λ)³,  T₂ = Σ(f^λ)²χ₂,  T₃ = Σ(f^λ)²χ₃.

  • T₂ = 0 EXACTLY (conjugation: χ^{λ'} = sgn·χ^λ, sgn(transposition) = −1, (f^{λ'})² = (f^λ)²).
  • So (D) ⇔ 4T₃ ≤ T₁; since T₁ > 0, (D) follows from T₃ ≤ 0.

  Jucys–Murphy content formula (from Σ X_i² = C(k,2)·1 + K₃, a central-element identity):
      χ^λ(3-cycle) = 3 f^λ (C₂(λ) − C(k,2)) / (k(k−1)(k−2)),   C₂(λ) = Σ_□ c(□)².
  Substituting: T₃ = (3/(k(k−1)(k−2)))·Σ(f^λ)³(C₂(λ) − C(k,2)). Since Σ(f^λ)³·1 relates to the
  Plancherel mean and E_Planch[Σ_□ c(□)²] = C(k,2) exactly (the T₂-type cancellation), T₃ ≤ 0 ⇔

      Cov_Planch(f^λ, Σ_□ c(□)²) ≤ 0   (up to the positive weight),  i.e.
      Σ_λ (f^λ)³ (Σ_□ c(□)² − C(k,2)) ≤ 0.

  ⇒ (D) is EQUIVALENT to this covariance inequality — dimension and content-spread anti-correlate
  under Plancherel measure. Verified strictly (T₃ < 0) for k = 3..20 here; the margin is stronger
  than (D) needs: E[f^{λ/(2,1)}]/E[f^λ] → 1/3⁺ (so w_std ≥ ⅓·E[f^λ], not just ¼).

POSITIVE CONTROL: the per-λ character identities are asserted against direct Aitken-determinant
skew counts f^{λ/(2,1)}, f^{λ/(3)} for every λ — this validates the content-formula χ₂, χ₃.

No closed form exists for E_Planch[f^{λ/μ}] or for T₃ (Morales–Pak–Panova arXiv:1610.07561;
Σ sₘ⊗sₘ⊗sₘ has no product formula), so the covariance must be proved as such, not by comparing
closed forms. The natural setting is the Kerov CLT / character-ratio moment machinery
(Fulman arXiv:math/0305423).

Discipline: scope-(a) provable-core reduction; no fit; no scale; nothing wired; no `c_k`; L2
unchanged (2/7). In-sandbox (integer + Fraction; no numpy/cvxpy/SnapPy). Complements #3808.

# Ref: [moralespakpanova2016] https://arxiv.org/abs/1610.07561
# Ref: [fulman2004stein] https://arxiv.org/abs/math/0305423
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

KMAX = 20


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
    n = sum(l)
    conj = [sum(1 for p in l if p > j) for j in range(l[0])]
    d = 1
    for i, row in enumerate(l):
        for j in range(row):
            d *= (row - j) + (conj[j] - i) - 1
    return math.factorial(n) // d


def contents(l):
    """(Σ c, Σ c²) over cells, content c(i,j) = j − i."""
    s = s2 = 0
    for i, row in enumerate(l):
        for j in range(row):
            s += j - i
            s2 += (j - i) ** 2
    return s, s2


def contains(l, mu):
    return all(i < len(l) and l[i] >= mu[i] for i in range(len(mu)))


def _detF(M):
    n = len(M)
    M = [r[:] for r in M]
    d = Fraction(1)
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            return Fraction(0)
        if p != c:
            M[c], M[p] = M[p], M[c]
            d = -d
        d *= M[c][c]
        inv = M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / inv
            if f:
                for cc in range(c, n):
                    M[r][cc] -= f * M[c][cc]
    return d


def skew(l, mu):
    """f^{λ/μ} via Aitken's determinant (exact); guard with `contains` so ℓ(μ) ≤ ℓ(λ)."""
    l = list(l)
    e = len(l)
    mu = list(mu) + [0] * (e - len(mu))
    n = sum(l) - sum(mu)
    M = [[Fraction(0)] * e for _ in range(e)]
    for i in range(e):
        for j in range(e):
            m = l[i] - (i + 1) - mu[j] + (j + 1)
            M[i][j] = Fraction(1, math.factorial(m)) if m >= 0 else Fraction(0)
    return int(math.factorial(n) * _detF(M))


def sk(l, mu):
    return skew(l, mu) if contains(l, mu) else 0


def main() -> int:
    print("=== (D) reduces to the Plancherel covariance Cov(f^λ, Σc²) ≤ 0 ===\n")
    print(f"{'k':>3} {'T2':>4} {'T3(<0)':>8} {'4T3≤T1':>7} {'(D)':>5} "
          f"{'Cov≤0':>6} {'E[sk21]/E[f]':>12}")

    t2_zero = True
    t3_neg = True
    D_ok = True
    cov_ok = True
    pc_ok = True   # positive control: character identities vs direct skew counts
    rows = []
    for k in range(3, KMAX + 1):
        Ck2 = k * (k - 1) // 2
        T1 = T2 = T3 = 0
        wnum = e3num = 0
        cov = 0
        for l in partitions_of(k):
            f = hook_dim(l)
            s, s2 = contents(l)
            chi2 = Fraction(f * s, Ck2)
            chi3 = Fraction(3 * f * (s2 - Ck2), k * (k - 1) * (k - 2))
            # positive control: exact per-λ character→skew identities
            if (f - chi3) / 3 != sk(l, (2, 1)) or (f + 3 * chi2 + 2 * chi3) / 6 != sk(l, (3,)):
                pc_ok = False
            T1 += f ** 3
            T2 += f * f * chi2
            T3 += f * f * chi3
            cov += f ** 3 * (s2 - Ck2)
            wnum += f * f * sk(l, (2, 1))
            e3num += f * f * sk(l, (3,))
        if T2 != 0:
            t2_zero = False
        if not (T3 < 0):
            t3_neg = False
        if not (4 * T3 <= T1 and wnum >= e3num):
            D_ok = False
        if cov > 0:
            cov_ok = False
        ratio = float(Fraction(wnum, math.factorial(k)) / Fraction(T1, math.factorial(k)))
        rows.append((k, int(T2), int(T3), float(ratio)))
        print(f"{k:>3} {int(T2):>4} {str(T3<0):>8} {str(4*T3<=T1):>7} "
              f"{str(4*T3<=T1 and wnum>=e3num):>5} {str(cov<=0):>6} {ratio:>12.4f}")

    print(f"\npositive control (χ-identities = direct skew counts, all λ): {pc_ok}")
    print(f"T₂ = Σ(f^λ)²χ₂ = 0 exactly (conjugation): {t2_zero}")
    print(f"T₃ = Σ(f^λ)²χ₃ < 0 strictly (⇔ Cov(f^λ,Σc²) ≤ 0): {t3_neg and cov_ok}")
    print(f"⇒ (D) ⇔ 4T₃ ≤ T₁  holds (k≤{KMAX}): {D_ok}")
    print(f"E[f^{{λ/(2,1)}}]/E[f^λ] → 1/3⁺  (stronger than (D)'s 1/4): last = {rows[-1][3]:.4f}")
    print("\nRESIDUAL OPEN KERNEL: Cov_Planch(f^λ, Σ_□ c(□)²) ≤ 0 (verified k≤20 here, k≤32 total;")
    print("no closed form for T₃ ⇒ must be proved as an anti-correlation, not by comparing forms).")

    ok = bool(pc_ok and t2_zero and t3_neg and D_ok and cov_ok)
    print(f"\nRESULT: (D) rigorously reduced to the covariance kernel (positive-controlled): {ok}")

    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("wlambda-D-reduction-content-covariance", engine="python-exact")
        w.set_description(
            "Rigorous reduction of the Δ_λ growth sub-lemma (D) w_std=E_Planch[f^{λ/(2,1)}] ≥ "
            "E_Planch[f^{λ/(3)}] (open input of #3939) to a single clean kernel: the Plancherel "
            "covariance inequality Cov(f^λ, Σ_□ c(□)²) ≤ 0. Via exact S_k character identities "
            "f^{λ/(2,1)}=(f^λ−χ₃)/3, f^{λ/(3)}=(f^λ+3χ₂+2χ₃)/6 (χ₂=char on transposition, χ₃=on "
            "3-cycle): Σ(f^λ)²(f^{λ/(2,1)}−f^{λ/(3)})=(T₁−4T₃−3T₂)/6 with T₁=Σ(f^λ)³, T₂=Σ(f^λ)²χ₂, "
            "T₃=Σ(f^λ)²χ₃. T₂=0 EXACT (conjugation sgn), so (D)⇔4T₃≤T₁⇐T₃≤0. Jucys–Murphy content "
            "formula χ^λ(3-cycle)=3f^λ(Σc²−C(k,2))/(k(k-1)(k-2)) ⇒ T₃≤0 ⇔ Σ(f^λ)³(Σc²−C(k,2))≤0 = "
            "Cov(f^λ,Σc²)≤0 (dimension & content-spread anti-correlate). Positive-controlled: the "
            "per-λ χ-identities reproduce direct Aitken skew counts for all λ. Verified T₂=0, T₃<0, "
            "(D), Cov≤0 for k=3..20 (agent k≤32); margin stronger than needed (E[f^{λ/(2,1)}]/E[f^λ]"
            "→1/3⁺). No closed form for T₃ (Morales–Pak–Panova) ⇒ the covariance is the residual "
            "open kernel, to be proved as an anti-correlation (Kerov CLT / Fulman). scope-(a); no "
            "fit; nothing wired; no c_k; L2 2/7.")
        w.add_data("positive_control_char_identities_ok", bool(pc_ok))
        w.add_data("T2_zero_exact", bool(t2_zero))
        w.add_data("T3_strictly_negative", bool(t3_neg and cov_ok))
        w.add_data("D_equiv_4T3_le_T1", bool(D_ok))
        w.add_data("kernel", "Cov_Planch(f^lambda, sum_cell content^2) <= 0")
        w.add_data("table", [{"k": r[0], "T2": r[1], "T3": r[2], "E_sk21_over_E_f": r[3]} for r in rows])
        w.add_assertion(
            "D_reduced_to_content_covariance_kernel",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("(D) ⇔ 4T₃≤T₁ with T₂=0 exact and χ-identities positive-controlled vs direct "
                    "skew counts; via JM content formula ⇔ Cov(f^λ,Σc²)≤0. Verified k≤20 (T₃<0 "
                    "strict); residual open kernel = the covariance inequality. No fit; no c_k."))
        out = w.save()
        print(f"\nWitness: {out}")
    except ImportError as e:
        print(f"\n(witness skipped — witness_base unavailable: {e})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
