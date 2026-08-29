#!/usr/bin/env python3
"""fake_degree_via_telescope_probe.py — normalizedSum n q = 1 CLOSES via the corpus
general-X Macdonald telescope at X=0 (beans qou-3quc / qou-x4zl / qou-ognw).

## The closure (this probe's claim)

The open residual of the general-n fake-degree identity was `normalizedSum n q = 1`,
where `normalizedSum n q = Σ_{λ⊢n} f^λ · q^{-κ_λ} / hookProd_q(λ)` (balanced q-brackets,
`κ_λ = Σ contents`). It is NOT open: it follows from the corpus's already-proved
general-X telescope

    QOU.MathlibExt.MacdonaldTelescopeGeneralX.telescope_generalX :
      Σ_{|ν|=n} f^ν · schurElement Q X ν.rowLens = ((1-X)/(1-Q))^n   (all X, Q>1)

via TWO facts, both verified here EXACTLY (sympy, no float):

  1. CONVENTION BRIDGE (per-λ): the balanced fake-degree summand equals the
     Macdonald Jones-Markov coefficient at Q=q^2, X=0:
        q^{-κ_λ}/hookProd_q(λ)  =  jonesMarkovCoeff(q^2, 0, λ)
                                =  schurElement(q^2, 0, λ) · (1-q^2)^n.
  2. TELESCOPE AT X=0: Σ_{|ν|=n} f^ν schurElement(q^2, 0, ν) = (1/(1-q^2))^n.

Chaining: normalizedSum n q = Σ f^λ jonesMarkovCoeff(q^2,0,λ)
        = (1-q^2)^n · Σ f^λ schurElement(q^2,0,λ) = (1-q^2)^n · (1/(1-q^2))^n = 1.

So `qou-3quc` closes by the telescope route; the induction/addable-box-(B) route
(MolienFakeDegreeInduction, AddableBoxHookOneRow) becomes an independent second
proof, not the path. The remaining Lean work is MECHANICAL (no open math): the
per-λ convention bridge (balanced hookProd <-> schurElement(q^2,0)) and the
Nat.Partition <-> YoungDiagram carrier bridge (PartitionsOfBridge / SYTEnum).

-- Ref: content/.../QOU/MathlibExt/MacdonaldTelescopeGeneralX.lean (telescope_generalX, all X)
-- Ref: content/.../QOU/MathlibExt/WenzlSchurElement.lean (schurElement, jonesMarkovCoeff)
-- Ref: content/.../QOU/MathlibExt/MolienFakeDegreeGeneralN.lean (normalizedSum, the residual)
"""
from __future__ import annotations

import sys
from math import factorial
from pathlib import Path

import sympy as sp

_COMP = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(_COMP / "qbeta"), str(_COMP), str(_COMP / "substrate")]
import _path_bridge  # noqa: F401,E402

q = sp.Symbol("q")
Q = q ** 2


def parts(n):
    def h(n, mx):
        if n == 0:
            yield ()
            return
        for k in range(min(n, mx), 0, -1):
            for r in h(n - k, k):
                yield (k,) + r
    return list(h(n, n))


def cells(lam):
    return [(i, j) for i in range(len(lam)) for j in range(lam[i])]


def hook(lam, i, j):
    arm = lam[i] - j - 1
    leg = sum(1 for r in range(i + 1, len(lam)) if lam[r] > j)
    return arm + leg + 1


def flam(lam):
    if not lam:
        return 1
    p = 1
    for c in cells(lam):
        p *= hook(lam, *c)
    return factorial(sum(lam)) // p


def qbal(m):
    return sp.cancel((q ** m - q ** (-m)) / (q - q ** (-1)))


def kappa(lam):
    return sum(j - i for (i, j) in cells(lam))


def hookprod_bal(lam):
    p = sp.Integer(1)
    for c in cells(lam):
        p *= qbal(hook(lam, *c))
    return sp.cancel(p)


def w_mine(lam):
    return sp.cancel(q ** (-kappa(lam)) / hookprod_bal(lam))


def nLambda(lam):
    return sum(i * lam[i] for i in range(len(lam)))


def schurElement0(lam):
    """schurElement(q^2, X=0, lam) = Q^{n(lam)} / prod(1 - Q^h)."""
    den = sp.Integer(1)
    for (i, j) in cells(lam):
        den *= (1 - Q ** hook(lam, i, j))
    return sp.cancel(Q ** nLambda(lam) / den)


def jonesMarkovCoeff0(lam):
    """jonesMarkovCoeff(q^2, 0, lam) = schurElement(q^2,0,lam) / wenzlNorm, wenzlNorm=(1/(1-Q))^n."""
    n = sum(lam)
    wn = (sp.Integer(1) / (1 - Q)) ** n
    return sp.cancel(schurElement0(lam) / wn)


def main() -> int:
    N = 5
    conv_ok = True
    tel_ok = True
    norm_ok = True
    for n in range(1, N + 1):
        # (1) convention bridge per-lambda
        for lam in parts(n):
            if sp.simplify(w_mine(lam) - jonesMarkovCoeff0(lam)) != 0:
                conv_ok = False
        # (2) telescope at X=0
        tel = sp.cancel(sum(flam(lam) * schurElement0(lam) for lam in parts(n)))
        if sp.simplify(tel - (sp.Integer(1) / (1 - Q)) ** n) != 0:
            tel_ok = False
        # (chain) normalizedSum = 1
        ns = sp.cancel(sum(flam(lam) * w_mine(lam) for lam in parts(n)))
        if sp.simplify(ns - 1) != 0:
            norm_ok = False
    print(f"[{'PASS' if conv_ok else 'FAIL'}] (1) q^-kappa/hookProd_q(lam) = jonesMarkovCoeff(q^2,0,lam)  (n<=  {N})")
    print(f"[{'PASS' if tel_ok else 'FAIL'}] (2) Sum f^lam schurElement(q^2,0,lam) = (1/(1-q^2))^n  (telescope@X=0)")
    print(f"[{'PASS' if norm_ok else 'FAIL'}] (chain) normalizedSum n q = 1")
    ok = conv_ok and tel_ok and norm_ok
    print(f"\nVERDICT: normalizedSum n q = 1 CLOSES via telescope_generalX@X=0 + the "
          f"(q^2,X=0) convention bridge {'CONFIRMED' if ok else 'FAILED'} for n<={N}. "
          f"qou-3quc closes by the telescope route; addable-box (B) is a second proof.")

    try:
        from witness_base import WitnessBuilder
    except Exception:
        return 0 if ok else 1
    w = WitnessBuilder("fake-degree-via-telescope", engine="sympy")
    w.set_description(
        "beans qou-3quc/qou-x4zl: normalizedSum n q = 1 (the open general-n fake-degree "
        "residual) CLOSES via the corpus general-X Macdonald telescope at X=0. Per-lambda: "
        "q^-kappa/hookProd_q(lam) = jonesMarkovCoeff(q^2,0,lam) = schurElement(q^2,0,lam)*(1-q^2)^n; "
        "telescope_generalX@X=0: Sum f schurElement(q^2,0) = (1/(1-q^2))^n; chain gives 1. "
        "Verified exact n<=5. Remaining Lean work is MECHANICAL bridging (convention + "
        "Nat.Partition<->YoungDiagram carrier), no open math. Nothing wired."
    )
    w.set_audit_only("docs/audits/2026-08-29-normalizedsum-closes-via-telescope.md")
    w.add_data("route", "normalizedSum = (1-q^2)^n * Sum f schurElement(q^2,0) = (1-q^2)^n*(1/(1-q^2))^n = 1")
    w.add_data("free_parameters", 0)
    w.add_assertion("convention_bridge_q2_X0", 1 if conv_ok else 0, 1,
                    source="q^-kappa/hookProd_q(lam) = jonesMarkovCoeff(q^2,0,lam), exact n<=5")
    w.add_assertion("telescope_at_X0", 1 if tel_ok else 0, 1,
                    source="Sum f schurElement(q^2,0) = (1/(1-q^2))^n, exact n<=5")
    w.add_assertion("normalizedSum_eq_one", 1 if norm_ok else 0, 1,
                    source="chain closes normalizedSum n q = 1, exact n<=5")
    # q0-INDEPENDENT, producer-declared. This probe never evaluates at a
    # substrate pin: `q` is a sympy Symbol throughout, there is no
    # `q_parameter` import, and `normalizedSum n q = 1` is an identity in the
    # indeterminate. Stamping it `proton` would assert a pin the computation
    # does not have; omitting the field leaves it in Q0_ANCHOR_MISSING, where
    # it took the q0-anchor refill ratchet RED on main as the one NEW
    # unbaselined witness. `independent` is producer-declared only -- see
    # `qou_substrate/witness.py`, and `hecke-a1-tail-schedule` for the same
    # symbolic-parameter case.
    out = w.save({
        "q0Anchor": "independent",
        "q0AnchorReason":
            "Symbolic identity in the indeterminate q (sympy Symbol; no "
            "q_parameter import and no numeric evaluation anywhere in the "
            "producer). normalizedSum n q = 1 holds for all q, so no "
            "substrate pin applies and no q0Value exists to record.",
    })
    print(f"witness -> {out}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
