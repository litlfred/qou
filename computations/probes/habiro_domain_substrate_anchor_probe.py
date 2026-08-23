#!/usr/bin/env python3
"""
Probe — the Habiro ring's domain, measured at the substrate anchor.

Companion to [`2026-08-10-keystone-literature-scoping-wrt-domain.md`], upgrading
its central claim from search tier to read tier + numerics. The keystone's open
object is the archimedean continuation of a colored Σ(2,3,5) WRT series to the
substrate `q₀ ≈ 1.10998`. Beliakova–Le (arXiv:1106.6298 §1, uploaded by the owner
2026-08-10) define the Habiro ring as the `(q;q)_k`-adic completion

    Ẑ[q] := lim←_k  Z[q] / ((q;q)_k),      (q;q)_k = ∏_{j=1..k} (1 − q^j)

and state — quoted, not paraphrased —

    "Every element f(q) ∈ Ẑ[q] can be considered as a function whose domain is
     the set of roots of unity."

Habiro's unified invariant `J_M` is an element of that ring, evaluating at any
root of unity to the WRT invariant there.

This probe measures WHY, because the mechanism is what decides whether the
keystone's continuation is a gap in our bookkeeping or a category error. An
element is an infinite sum `Σ_k f_k(q)·(q;q)_k`, so its convergence is governed
by `(q;q)_k`, and that factor behaves in three completely different ways:

  root of unity  order n ⇒ (ξ;ξ)_k = 0 for k ≥ n ⇒ the sum TERMINATES. This is
                 not a convention; it is why the domain is what it is.
  |q| < 1        (q;q)_k → (q;q)_∞ ≠ 0, bounded ⇒ the sum MAY converge
                 (necessary, NOT sufficient — the f_k still matter).
  |q| > 1        |(q;q)_k| grows super-exponentially ⇒ generically DIVERGES.

The substrate anchor `q₀ ≈ 1.10998` is real and `> 1`: the third regime.

## What this settles, and what it does not

SETTLES (read tier + measured): a Habiro-ring element is not a function at the
substrate anchor, and the reason is structural — the completion that makes roots
of unity work is the same one that makes real `q > 1` diverge. So "continue the
unified WRT invariant to q₀" is not a harder version of evaluating it; it is
asking for something the object does not have. Two of the three uploaded papers
independently keep everything at roots of unity: Dimofte–Garoufalidis
(arXiv:1511.05628 §1) define a quantum modular form as "a complex valued function
f on the set of complex roots of unity ... with a formal power series expansion
φ_ζ(ℏ) ∈ C[[ℏ]] at each complex root of unity ζ" — asymptotics NEAR roots of
unity, not values at |q|>1; and Lovejoy–Osburn–Störzer (arXiv:2605.15740, 2026)
recast Habiro's unified WRT as "an identity for a q-hypergeometric series at
roots of unity", including Hikami's Brieskorn-sphere cases — the Σ(2,3,5) family
itself.

DOES NOT SETTLE: whether some OTHER object (a state integral, an analytic
q-series) reproduces `W_λ` at q₀. This probe is about the Habiro/unified-WRT
route only. Scope-(a) on that route; it excludes no ingredient elsewhere.

## The lead this opens — the bar-conjugate point

`1/q₀ ≈ 0.9009 < 1` sits in the CONVERGENT regime, and the framework already
threads a bar-involution `q ↔ q⁻¹` through everything (bar-even/bar-odd channels,
the `θ_{λ'} = θ_λ⁻¹` chirality law, the Q_β cosh/sinh split). So the natural
question is whether the unified-WRT series converges at the bar-conjugate of the
substrate anchor and can be bar-transported back.

Stated as a LEAD, not a result, and with its own caveat: bounded `(q;q)_k` is
NECESSARY but NOT SUFFICIENT. Convergence of `Σ_k f_k·(q;q)_k` also needs the
`f_k` not to grow faster, and Habiro elements are only specified up to the
completion, so a convergent evaluation at `|q|<1` is not automatic and is not
implied by anything measured here.

NO WITNESS: pure q-Pochhammer arithmetic at mpmath precision from the canonical
50-dps q₀, reproducible from the printed table; nothing here feeds production.

Bean qou-1nvh follow-on; owner-supplied literature, commit 95accb15.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _Path, _bridge

import sys

import mpmath as mp
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def qpoch(q, k):
    """(q;q)_k = prod_{j=1..k} (1 - q^j) — the Habiro completion's defining factor."""
    p = mp.mpf(1) if not isinstance(q, mp.mpc) else mp.mpc(1)
    for j in range(1, k + 1):
        p *= 1 - q ** j
    return p


def main() -> int:
    from q_parameter import Q_50_DIGIT_STR as Q50
    q0 = mp.mpf(str(Q50))
    qbar = 1 / q0

    print("Habiro-ring domain at the substrate anchor  (bean qou-1nvh; arXiv:1106.6298)\n")
    print("  Habiro ring  Z^[q] := lim<-_k Z[q]/((q;q)_k),  (q;q)_k = prod_{j=1..k}(1-q^j)")
    print("  Beliakova-Le §1: \"Every element f(q) in Z^[q] can be considered as a")
    print("  function whose domain is the set of roots of unity.\"\n")
    print(f"  q0    = {mp.nstr(q0, 12)}   substrate anchor, real > 1")
    print(f"  1/q0  = {mp.nstr(qbar, 12)}   bar-conjugate, < 1\n")

    print("An element is a sum  S = sum_k f_k(q)*(q;q)_k , so (q;q)_k governs convergence:\n")
    print("|  k | (q0;q0)_k  [substrate] | (1/q0;1/q0)_k  [bar-conj] |")
    print("| --: | --------------------: | ------------------------: |")
    for k in (1, 2, 5, 10, 20, 30, 50, 80):
        print(f"| {k:>3} | {mp.nstr(abs(qpoch(q0, k)), 8):>21} | "
              f"{mp.nstr(abs(qpoch(qbar, k)), 8):>25} |")

    inf_bar = mp.qp(qbar)
    print(f"\n  (1/q0;1/q0)_inf = {mp.nstr(inf_bar, 12)}   -> CONVERGES, nonzero")

    # Root of unity: the factor is eventually exactly zero, which is the whole
    # mechanism behind the domain statement.
    n = 5
    z = mp.exp(2j * mp.pi / n)
    vals = [abs(qpoch(z, k)) for k in (n - 1, n, n + 1)]
    print(f"  at a primitive {n}th root of unity, |(z;z)_k| for k = {n-1},{n},{n+1}: "
          + ", ".join(mp.nstr(v, 4) for v in vals))
    print(f"    -> zero for k >= {n} (to working precision): the sum TERMINATES.")

    # Verdicts, computed rather than asserted.
    grows = abs(qpoch(q0, 80)) > abs(qpoch(q0, 20)) > 1
    bounded = abs(qpoch(qbar, 80)) < 1 and abs(inf_bar) > 0
    terminates = vals[1] < mp.mpf("1e-30") < vals[0]

    print("\n## Verdict\n")
    print(f"- root of unity: terminates      {terminates}")
    print(f"- |q| < 1  (1/q0): bounded       {bounded}   -> convergence POSSIBLE, not implied")
    print(f"- |q| > 1  (q0):   diverges      {grows}   -> |(q0;q0)_80| ~ "
          f"{mp.nstr(abs(qpoch(q0, 80)), 4)}")
    print("\n- So the substrate anchor is OFF the Habiro ring's domain, and structurally so:")
    print("  the (q;q)_k-adic completion that makes roots of unity evaluable is the same")
    print("  one that makes real q > 1 diverge. Continuing a unified-WRT element to q0 is")
    print("  not a harder evaluation — it asks for something the object does not have.")
    print("  Scope-(a): about the Habiro/unified-WRT route only; excludes nothing else.")
    print("\n- LEAD (not a result): 1/q0 lies in the convergent regime, and the framework")
    print("  already threads a bar-involution q <-> 1/q. Whether the unified-WRT series")
    print("  actually converges there needs the f_k, which this does not touch — bounded")
    print("  (q;q)_k is necessary, not sufficient.")

    ok = terminates and bounded and grows
    print(f"\n(no witness by design; all three regimes reproduce: {ok})")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
