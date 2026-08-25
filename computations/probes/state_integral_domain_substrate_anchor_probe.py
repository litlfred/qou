#!/usr/bin/env python3
"""
Probe — is the substrate anchor inside the STATE-INTEGRAL domain?

Complement to
[`habiro_domain_substrate_anchor_probe.py`](habiro_domain_substrate_anchor_probe.py),
which showed the substrate anchor `q₀ ≈ 1.10998` is structurally OFF the Habiro
ring's domain (the `(q;q)_k`-adic completion diverges there:
`|(q₀;q₀)_80| ≈ 7.3e140`). That left one candidate standing in the keystone
route table — the analytic one. This probe checks it.

## The source

Garoufalidis–Kashaev, *Evaluation of state integrals at rational points*
(arXiv:1411.6062v2, owner-supplied). A 1-dimensional state-integral is

    I_{A,B}(b) = ∫_{ℝ+iε} Φ_b(x)^B e^{−Aπix²} dx,     B > A > 0,

described in §1.1 as **"an absolutely convergent integral ... for a complex
number b with b² ∉ ℝ≤0"**. That is the whole point of the contrast: a state
integral is a genuine analytic function of `b`, where a Habiro element is a
function on roots of unity only.

Conventions, and one of them is inferred — flagged rather than buried:
  * `q = e^{2πiτ}`, `q̃ = e^{−2πi/τ}` — quoted from §1.1.
  * `τ = b²` — the standard Faddeev convention, NOT quoted in the extracted
    text. It is consistent with the paper's own rational-point setup
    (`b = √(M/N)` ⇒ `b²` rational ⇒ `|q| = 1`, i.e. the roots of unity where
    their evaluation theorem lives), which is why it is used here. **If a reader
    finds the paper uses a different normalisation, the arithmetic below moves.**

## What is computed

Map the substrate anchor through `q₀ = e^{2πiτ}` and test the paper's stated
convergence condition:

    q₀ real > 1  ⇒  2πiτ = ln q₀ ∈ ℝ>0  ⇒  τ = −i·ln(q₀)/(2π)   purely imaginary

so `b² = τ` is purely imaginary and **`b² ∉ ℝ≤0` holds**. The substrate anchor is
inside the convergence domain.

Also verified: the volume constant in the paper's headline 4₁ identity,
`V = 2·Im(Li₂(e^{iπ/3})) = 2.0298832…`, is *the corpus's own* `Vol(4₁) =
2·Cl₂(π/3)` — the CAL-2 muon anchor — to 30+ digits.

## What this establishes, and what it does NOT

ESTABLISHES: route selection. The Habiro/unified-WRT route cannot reach `q₀` (a
structural fact about its completion); the state-integral route *can*, in the
sense that the substrate anchor satisfies the stated convergence condition. So
the keystone's archimedean-continuation problem should be attacked on the
analytic side, and the corpus already holds the kernel (Faddeev `Φ_q`,
cheat-sheet §4).

DOES NOT ESTABLISH, and these matter:
  1. **Convergence is not identification.** That `I_{A,B}(b)` converges at the
     substrate anchor says nothing about whether any state integral reproduces
     `W_λ = d_q(λ)²/[n]_q!`. Necessary, wildly insufficient.
  2. **The paper's EVALUATION theorem does not apply here.** Its results are at
     *rational* `b² = M/N`, expressed via Rogers + cyclic dilogarithm and finite
     state-sums *at roots of unity*. Our `b²` is purely imaginary, not rational —
     only the convergence statement transfers, not the evaluation machinery.
  3. **No Σ(2,3,5) state integral is exhibited.** The keystone needs a colored
     WRT series for that specific Brieskorn sphere. Nothing here supplies one.

## Observation, explicitly NOT a result (anti-numerology)

The paper's headline identity reads

    I_{1,2}(1) = (e^{iπ/6}/√3)·(e^{V/2π} − e^{−V/2π}) = (e^{iπ/6}/√3)·2·sinh(V/2π)

with `V = Vol(4₁)`. So the framework's CAL-2 muon anchor volume appears in the
literature inside a **sinh** — and the framework independently carries a bar-odd
`sinh` / bar-even `cosh` split (AGENTS.md: `Q_β` is "the bar-odd `sinh` partner
of the bar-even `cosh` meson scale `m_π`").

That is an appearance-level echo at `b = 1`, which is NOT the substrate anchor,
and `2·sinh(V/2π) = 0.6574…` is not matched to any framework quantity here. Per
the corpus anti-numerology discipline it is recorded as something to look at with
a specific question in hand, and must not be cited as a correspondence. Two
independent objects containing `Vol(4₁)` is the expected state of affairs when
one of them is *defined* by the figure-eight knot.

NO WITNESS: convention-dependent arithmetic on published constants; the printed
table reproduces it.

Bean qou-1nvh follow-on; owner-supplied literature.
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
I = mp.mpc(0, 1)


def main() -> int:
    from q_parameter import Q_50_DIGIT_STR as Q50
    q0 = mp.mpf(str(Q50))

    # q = e^{2 pi i tau}  =>  tau = ln(q)/(2 pi i);  Faddeev convention tau = b^2.
    tau = mp.log(q0) / (2 * mp.pi * I)
    b2 = tau

    print("State-integral domain at the substrate anchor  (arXiv:1411.6062 §1.1)\n")
    print("  I_{A,B}(b) = int Phi_b(x)^B e^{-A pi i x^2} dx")
    print("  \"an absolutely convergent integral ... for a complex number b with")
    print("   b^2 not in R_{<=0}\"\n")
    print(f"  q0   = {mp.nstr(q0, 15)}   (real > 1)")
    print(f"  tau  = ln(q0)/(2 pi i) = {mp.nstr(tau, 12)}")
    print(f"  b^2  = tau            = {mp.nstr(b2, 12)}   [convention tau = b^2, INFERRED]")
    print(f"\n  Re(b^2) = {mp.nstr(mp.re(b2), 8)}    Im(b^2) = {mp.nstr(mp.im(b2), 8)}")

    in_bad_set = abs(mp.im(b2)) < mp.mpf("1e-25") and mp.re(b2) <= 0
    converges = not in_bad_set
    print(f"  b^2 in R_{{<=0}}?  {in_bad_set}      => state integral converges: {converges}")
    print("\n  => the substrate anchor is INSIDE the state-integral domain, where it is")
    print("     structurally OUTSIDE the Habiro ring's (see the companion probe).")

    # The volume constant of the paper's headline 4_1 identity is the corpus's own.
    V_paper = 2 * mp.im(mp.polylog(2, mp.exp(I * mp.pi / 3)))
    V_corpus = 2 * mp.clsin(2, mp.pi / 3)
    delta = abs(V_paper - V_corpus)
    print(f"\n  V = 2*Im(Li2(e^{{i pi/3}}))  = {mp.nstr(V_paper, 15)}   [paper: 2.0298832...]")
    print(f"  Vol(4_1) = 2*Cl2(pi/3)     = {mp.nstr(V_corpus, 15)}   [corpus, CAL-2 anchor]")
    print(f"  |difference|               = {mp.nstr(delta, 3)}  -> same constant")

    sinh_form = 2 * mp.sinh(V_paper / (2 * mp.pi))
    print(f"\n  OBSERVATION (not a result): the paper's identity is")
    print(f"    I_{{1,2}}(1) = (e^{{i pi/6}}/sqrt3) * 2 sinh(V/2pi),   2 sinh(V/2pi) = "
          f"{mp.nstr(sinh_form, 12)}")
    print("  i.e. the CAL-2 anchor volume appears inside a SINH, and the framework")
    print("  independently carries a bar-odd sinh / bar-even cosh split. This is at")
    print("  b = 1, NOT the substrate anchor, and is matched to nothing here. Recorded")
    print("  as a question to carry, not a correspondence (anti-numerology).")

    ok = converges and delta < mp.mpf("1e-25")
    print(f"\n  checks: anchor-in-domain={converges}  volume-identity={delta < mp.mpf('1e-25')}")
    print("\n(no witness by design; convention-dependent arithmetic on published constants.)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
