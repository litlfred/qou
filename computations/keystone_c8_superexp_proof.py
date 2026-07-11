#!/usr/bin/env python3
"""
keystone_c8_superexp_proof.py — PROVE the s5-so3 keystone necessary-condition C8
(super-exponential growth of the Plancherel-weighted branched sum), upgrading it
from "verified k≤10" to a rigorous super-exponential lower bound.

Owner: "open s5-so3 gate" (2026-07-11). The gate is owner-reversed for the geometric
W_λ construction; this note discharges the C8 Lean target flagged in
docs/audits/2026-07-11-keystone-wlambda-superexp-necessary-condition.md §"Honest scope".

C8 object (at q=1, the Plancherel limit W_λ = f^λ²/k!):
    w_std(k) = Σ_{λ⊢k} W_λ · f^{λ/(2,1)} = (1/k!) Σ_λ (f^λ)² f^{λ/(2,1)} = E_Planch[f^{λ/(2,1)}].
C8 requires w_std super-exponential.

PROOF (three exact/classical steps):
  (A) Exact identity:  S1(k) := Σ_{λ⊢k} f^λ f^{λ/(2,1)} = k!/3.
      (The classical branching identity Σ_λ f^λ f^{λ/μ} = k!·f^μ/|μ|!, with
      μ=(2,1): f^μ=2, |μ|!=6 ⇒ k!·2/6 = k!/3. Verified exact k=3..11 below.)
  (B) Cauchy–Schwarz with weights g_λ = f^{λ/(2,1)} ≥ 0:
      (Σ_λ f^λ g_λ)² ≤ (Σ_λ (f^λ)² g_λ)(Σ_λ g_λ)
      ⇒ (k!/3)² ≤ (k!·w_std)·(Σ_λ f^{λ/(2,1)})
      ⇒ w_std(k) ≥ k! / (9 · Σ_{λ⊢k} f^{λ/(2,1)}).
  (C) Σ_{λ⊢k} f^{λ/(2,1)} ≤ Σ_{λ⊢k} f^λ = I(k)  (skew SYT ≤ straight SYT:
      prepending a fixed SYT of (2,1) injects SYT(λ/(2,1)) ↪ SYT(λ); and
      Σ_λ f^λ = I(k) is the involution/telephone number, the q=1 value of the
      QOU na-Stokes period S(n) = Σ_λ dim_q(λ)).
  ⇒  w_std(k) ≥ k! / (9 · I(k)),  and k!/I(k) is super-exponential
     (I(k) ~ (k/e)^{k/2} e^{√k−1/4}/√2, k! ~ (k/e)^k √(2πk) ⇒ k!/I(k) ~ (k/e)^{k/2}·poly).
  QED (super-exponential growth class of w_std).

This is the μ/e ↔ binding cross-link's provable core: I(k) = S(n)|_{q=1} is the same
involution-number family as the QOU binding period a_D^(n) = S(n)/n. No fit; adds a
proof of an existing necessary condition, does NOT construct the geometric W_λ.

EXPLORATORY — no production wiring, no fitted constant, no tier change.
Audit: docs/audits/2026-07-11-keystone-c8-superexp-proof.md
"""
from __future__ import annotations
import sys
from math import factorial
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent / "substrate"))


def parts(n, m=None):
    m = n if m is None else m
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for r in parts(n - k, k):
            yield (k,) + r


def conj(l):
    return tuple(sum(1 for x in l if x > j) for j in range(l[0])) if l else ()


def fdim(lam):
    if not lam:
        return 1
    n = sum(lam)
    c = conj(lam)
    p = 1
    for i, r in enumerate(lam):
        for j in range(r):
            p *= (r - 1 - j) + (c[j] - 1 - i) + 1
    return factorial(n) // p


def contains(lam, mu):
    return len(mu) <= len(lam) and all(mu[i] <= lam[i] for i in range(len(mu)))


def skew(lam, mu):
    if not contains(lam, mu):
        return 0
    if sum(lam) == sum(mu):
        return 1
    t = 0
    for i in range(len(lam)):
        if lam[i] > (lam[i + 1] if i + 1 < len(lam) else 0) and lam[i] > (mu[i] if i < len(mu) else 0):
            nl = list(lam)
            nl[i] -= 1
            while nl and nl[-1] == 0:
                nl.pop()
            t += skew(tuple(nl), mu)
    return t


def involution(k):
    x = [1, 1]
    for n in range(2, k + 1):
        x.append(x[-1] + (n - 1) * x[-2])
    return x[k]


MU = (2, 1)


def main() -> int:
    print("=== C8 super-exp PROOF: w_std(k) ≥ k!/(9·I(k)), super-exponential ===\n")
    print(f"{'k':>3}{'w_std':>11}{'S1':>12}{'k!/3':>12}{'Σf/(21)':>9}{'I(k)':>8}"
          f"{'LB=k!/9I':>11}{'w≥LB':>6}{'ratio':>8}")
    all_ok = True
    prev = None
    rows = {}
    for k in range(3, 13):
        P = list(parts(k))
        wstd = sum(fdim(l) ** 2 * skew(l, MU) for l in P) / factorial(k)
        S1 = sum(fdim(l) * skew(l, MU) for l in P)
        Sg = sum(skew(l, MU) for l in P)
        Ik = involution(k)
        kfact3 = factorial(k) // 3
        lb = factorial(k) / (9 * Ik)
        ok = (S1 == kfact3) and (Sg <= Ik) and (wstd >= lb - 1e-9)
        all_ok &= ok
        rr = f"{lb / prev:.3f}" if prev else "—"
        rows[k] = {"w_std": wstd, "S1": S1, "Sg": Sg, "I": Ik, "lb": lb}
        print(f"{k:>3}{wstd:>11.2f}{S1:>12}{kfact3:>12}{Sg:>9}{Ik:>8}{lb:>11.2f}"
              f"{'✓' if wstd >= lb else '✗':>6}{rr:>8}")
        prev = lb

    print(f"\n  (A) S1 = k!/3 exact: {all(rows[k]['S1'] == factorial(k)//3 for k in rows)}")
    print(f"  (C) Σf^(λ/(2,1)) ≤ I(k): {all(rows[k]['Sg'] <= rows[k]['I'] for k in rows)}")
    print(f"  ⇒ w_std ≥ k!/(9 I(k)); LB ratios rise ({rows[3]['lb']:.2f}→{rows[12]['lb']:.1f}, "
          f"ratio {rows[12]['lb']/rows[11]['lb']:.2f}) → super-exponential.")
    print(f"\nVERDICT: {'C8 PROVED (super-exp lower bound)' if all_ok else 'FAIL'}. "
          "The bound uses only the exact identity S1=k!/3, Cauchy–Schwarz, and Σf≤I(k).")

    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("keystone-c8-superexp-proof", engine="python-exact")
        wb.set_description(
            "PROOF of s5-so3 keystone necessary-condition C8: the Plancherel-weighted "
            "branched sum w_std(k)=E_Planch[f^(λ/(2,1))] grows super-exponentially. Chain: "
            "(A) exact identity Σ f^λ f^(λ/(2,1))=k!/3; (B) Cauchy–Schwarz ⇒ w_std≥k!/(9Σf^(λ/(2,1))); "
            "(C) Σf^(λ/(2,1))≤I(k) ⇒ w_std≥k!/(9 I(k)), super-exp (I(k)=involution#=S(n)|q=1). "
            "Upgrades C8 from verified-k≤10 to proved growth class. No fit; adds a test-proof, "
            "does not construct geometric W_λ.")
        wb.add_data("bound_table", {str(k): {kk: (float(vv) if kk in ('w_std', 'lb') else int(vv))
                                             for kk, vv in v.items()} for k, v in rows.items()})
        wb.add_assertion(
            name="c8_superexp_lower_bound_proved",
            computed=str(int(all_ok)), expected="1", tolerance=0,
            source=("S1=k!/3 exact (k=3..12), Σf^(λ/(2,1))≤I(k), Cauchy–Schwarz ⇒ "
                    "w_std(k)≥k!/(9 I(k)); k!/I(k) super-exponential. Proves C8's growth class."))
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:
        print(f"\n(witness emit skipped: {e})")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
