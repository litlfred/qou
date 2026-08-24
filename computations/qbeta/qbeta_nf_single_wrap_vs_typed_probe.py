#!/usr/bin/env python3
"""The Q_β counit chain rests on the SINGLE-WRAP nucleon NF, not the typed one —
and the difference between them is 3.6x larger than the phase it is used to derive.

Bean `qou-pdix`.  Written to close a residual I named in commit `17afd55cbe`, and
it does not close it — it shows the residual is real and load-bearing.

## What the previous commit claimed, and what it missed

`17afd55cbe` settled why `evalMap h w = h²/2 − h·w` is affine in the crossing
weight: the `N=0` neutron−proton NF difference

    (n − p) = [h²/2, −h/2, −h/2, 0, 0, 0]      basis [γ, σ₀, σ₁, L₊, L₋, e⁻]

has support only on crossing-numbers `{0,1}`, and `tr_M(eᵢ) = z^{#cr(eᵢ)}`, so
`deg_z E = 1` by construction.  It then named the residual: the vector is
asserted in `docs/audits/2026-06-16-...counit-vs-trace.md` and transcribed
downstream, nothing recomputes it, and *"the one thing that would overturn it is
a nonzero L₊/L₋/e⁻ coefficient in the difference"*.

**That coefficient is nonzero, and the corpus has said so since 2026-05-11.**

## Recomputed, not transcribed

This probe reimplements `pyhecke.gram.hm` (the GB reduction tables) and
`pyhecke.atom.build_nucleon_nf` symbolically over `ℚ(h)` and **validates against
the live `PROTON_NF` / `NEUTRON_NF`** — agreement to float64 epsilon, so the
symbolic run is the same construction, not a lookalike.  Result:

    typed 6-term (live build_nucleon_nf):
      (n − p) = [ h(2h⁴+h²−2)/4, h²(h²+1)(2h²+1)/4, h²(h²−h+1)(h²+h+1)/4,
                  −h⁵/4, h(h²+1)(h⁴−2)/4, −h⁴(h²+2)/4 ]
      support = ALL SIX indices ⇒ crossing-numbers {0,1,2,3} ⇒ deg_z E = 3

Nothing cancels.  In particular `L₊` does **not** cancel, which is the exact
line the 2026-06-16 audit leans on (*"the leading L₊ term cancels (both have
coefficient 1)"*) and which I quoted without checking.

## These are two different objects, and the corpus already knew

`docs/audits/2026-05-11-q-beta-residual-decomposition.md` §1 names both and the
factor between them:

  | basis-change typed-vs-single-wrap | **1.00579** | *"Typed-crossings 6-term
  NF picks up nonzero L±, e⁻ contributions that exactly cancel at single wrap"* |

Both of its numbers reproduce here from the symbolic run:

    single-wrap   ε(n−p) = h(h−2)/2      |ε| = 0.187207   (audit: 0.18721)
    typed 6-term  ε(n−p) = h(h⁶+2h⁵+2h⁴+2h³−h²+2h−4)/4
                                          |ε| = 0.188291   (audit: 0.18829)

So the audit vector is **the single-wrap NF**.  It was never wrong; it is a
different, explicitly simpler object from the one the live mass compute uses.

## The consequence for branch 3 — my abelian deflation is scope-limited

  * **On the single-wrap NF**, `deg_z E = 1`, the `d²` term vanishes, and the
    counit-minus-trace gap really is an abelian period.  That result stands, and
    reading (a) of the earlier fork stands **for that object**.
  * **On the typed NF**, `deg_z E = 3`.  The gap carries genuine second- *and*
    third-order weight structure, so it is **not** abelian and the non-abelian
    Stokes framing is **not** deflated there.

I recorded "branch 3's target is a period, not a curvature integral" without
that qualifier.  It needs one.

## The sharper point: the NF choice is BIGGER than the phase

The ladder needs an `N=1` factor of `0.99839767`, i.e. a **0.160 %** correction.
The single-wrap-vs-typed ambiguity in the very object it corrects is **0.579 %**
— **3.6×** larger, and of the same sign class.

    |ε_typed − ε_single| / |ε_single| = 0.579 %        vs        1 − N1 = 0.160 %

That is a scope-(a) negative for the whole derivation programme, not just for
branch 3: **a 0.16 % phase cannot be derived from an object whose own NF
convention is unsettled at 0.58 %.**  Whichever NF is canonical has to be
settled first, and settling it moves the target by more than the target.

Neither is declared canonical here.  The 2026-05-11 audit treats the 1.00579 as
a factor still to be *explained* (it pairs it with the `N=0` brane-tower residual
1.00168 to make the full 1.00744), so the corpus itself leaves the choice open.

## Scope

Scope-(a) throughout: this constrains what a derivation may rest on.  It refutes
no ingredient, declares no NF canonical, and proposes no `c_k`.  What it
establishes is that two named corpus objects disagree by more than the effect
under study, and that the affineness result holds for exactly one of them.

Exact `ℚ(h)` symbolic throughout; the numeric lines are mpmath at 50 dps from the
proton-pinned `q₀` (owner directive 2026-08-07).  No float64 arithmetic — the
float64 comparison against the live constants is a *validation of provenance*,
tolerance `1e-15`, and no result depends on it.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

_ROOT = Path(__file__).resolve().parents[2]
for _p in (_ROOT / "tools" / "pyhecke" / "python",
           _ROOT / "tools" / "qou-substrate" / "python",
           _ROOT / "computations", _ROOT / "computations" / "substrate"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

h = sp.symbols("h")

# Crossing numbers of the NF basis, in `hm`'s index order.  Index order is
# established below by reducing the words themselves, not assumed.
_WORDS = {0: (), 1: (0,), 2: (1,), 3: (1, 0), 4: (0, 1), 5: (0, 1, 0)}


def hm(nf, c, d, gen):
    """Symbolic transcription of `pyhecke.gram.hm` — the GB reduction tables."""
    r = [sp.Integer(0)] * 6
    if gen == 0:
        tables = [(0, [(1, c), (0, d)]), (1, [(1, c * h), (0, c), (1, d)]),
                  (2, [(3, c), (2, d)]), (3, [(3, c * h), (2, c), (3, d)]),
                  (4, [(5, c), (4, d)]), (5, [(5, c * h), (4, c), (5, d)])]
    else:
        tables = [(0, [(2, c), (0, d)]), (1, [(4, c), (1, d)]),
                  (2, [(2, c * h), (0, c), (2, d)]), (3, [(5, c), (3, d)]),
                  (4, [(4, c * h), (1, c), (4, d)]), (5, [(5, c * h), (3, c), (5, d)])]
    for si, tgts in tables:
        if nf[si] == 0:
            continue
        for ti, co in tgts:
            r[ti] += nf[si] * co
    return [sp.expand(x) for x in r]


def nf_of_word(w):
    nf = [sp.Integer(1)] + [sp.Integer(0)] * 5
    for g in w:
        nf = hm(nf, sp.Integer(1), sp.Integer(0), g)
    return nf


def build_nucleon(quarks, gluon=True):
    """Symbolic transcription of `pyhecke.atom.build_nucleon_nf`."""
    nf = [sp.Integer(1)] + [sp.Integer(0)] * 5
    if gluon:                                   # B₃ = (σ₀σ₁⁻¹)³ confinement
        for _ in range(3):
            nf = hm(nf, sp.Integer(1), sp.Integer(0), 0)
            nf = hm(nf, sp.Integer(1), -h, 1)
    for (i, j) in ((0, 1), (0, 2), (1, 2)):     # quark pairwise crossings
        qi, qj = quarks[i], quarks[j]
        if qi == qj == 'u':
            nf = hm(nf, sp.Integer(1), sp.Integer(0), i)
        elif qi == qj == 'd':
            nf = hm(nf, sp.Integer(1), -h, i)
        else:
            nf = hm(nf, sp.Integer(1), -h / sp.Integer(2), i)
    return nf


def main() -> int:
    failures: list[str] = []

    def check(name, ok, detail):
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
        if not ok:
            failures.append(name)

    print("Assertions (exact ℚ(h) symbolic; numerics mpmath @ 50 dps):")

    # ---- 1. the NF basis index order, reduced not assumed ----
    ident = {i: nf_of_word(w) for i, w in _WORDS.items()}
    diag = all(ident[i][i] == 1 and all(ident[i][j] == 0 for j in range(6) if j != i)
               for i in _WORDS)
    ncr = {i: len(w) for i, w in _WORDS.items()}
    check(
        "1. basis index order established by reducing the words themselves",
        diag and ncr == {0: 0, 1: 1, 2: 1, 3: 2, 4: 2, 5: 3},
        f"words {_WORDS} reduce to the unit vectors; crossing numbers {ncr}. "
        "NOTE index 3 = σ₁σ₀ = L₋ and index 4 = σ₀σ₁ = L₊ — the audit's written "
        "order [γ,σ₀,σ₁,L₊,L₋,e⁻] swaps 3/4 relative to `hm`; immaterial to "
        "support/degree, recorded so the two orders are not silently conflated",
    )

    # ---- 2. PROVENANCE: the symbolic build IS the live pyhecke construction ----
    typed_p, typed_n = build_nucleon(['u', 'u', 'd']), build_nucleon(['u', 'd', 'd'])
    try:
        from pyhecke.atom import NEUTRON_NF, PROTON_NF
        from pyhecke.gram import h as _gh
        hf = sp.Float(repr(_gh), 20)
        devp = max(abs(float(x.subs(h, hf)) - y) for x, y in zip(typed_p, PROTON_NF))
        devn = max(abs(float(x.subs(h, hf)) - y) for x, y in zip(typed_n, NEUTRON_NF))
        check(
            "2. symbolic build reproduces the LIVE PROTON_NF / NEUTRON_NF",
            devp < 1e-15 and devn < 1e-15,
            f"max|dev| proton {devp:.2e}, neutron {devn:.2e} (float64 eps). "
            "Provenance validation only — no result below depends on it",
        )
    except Exception as exc:                                  # pragma: no cover
        check("2. symbolic build reproduces the LIVE PROTON_NF / NEUTRON_NF",
              False, f"pyhecke unavailable: {exc}")

    # ---- 3. the TYPED difference has FULL support — nothing cancels ----
    dt = [sp.expand(a - b) for a, b in zip(typed_n, typed_p)]
    supp_t = [i for i, x in enumerate(dt) if x != 0]
    check(
        "3. typed 6-term (n-p) has FULL support — L±, e- do NOT cancel",
        supp_t == [0, 1, 2, 3, 4, 5] and max(ncr[i] for i in supp_t) == 3,
        f"(n-p)_typed = {[sp.factor(x) for x in dt]}; support {supp_t}, "
        f"max crossing-number {max(ncr[i] for i in supp_t)} ⇒ deg_z E = 3",
    )

    # ---- 4. ... so the typed gap is NOT abelian: d^2 AND d^3 both survive ----
    w0s, ds = sp.symbols("w0 d")
    E_typed = sum(dt[i] * (w0s + ds) ** ncr[i] for i in range(6))
    dep = sp.expand(sum(dt[i] * w0s ** ncr[i] for i in range(6)) - E_typed)
    c2, c3 = (sp.Poly(dep, ds).coeff_monomial(ds ** k) for k in (2, 3))
    check(
        "4. the TYPED gap carries second- AND third-order weight structure",
        sp.simplify(c2) != 0 and sp.simplify(c3) != 0,
        f"d^2 coeff = {sp.factor(c2)}; d^3 coeff = {sp.factor(c3)}. So the "
        "abelian deflation of branch 3 holds for the SINGLE-WRAP NF only",
    )

    # ---- 5. the single-wrap NF is the audit vector, and IS affine ----
    single = [h ** 2 / 2, -h / 2, -h / 2, 0, 0, 0]
    supp_s = [i for i, x in enumerate(single) if x != 0]
    E_s = sum(single[i] * (w0s + ds) ** ncr[i] for i in range(6))
    dep_s = sp.expand(sum(single[i] * w0s ** ncr[i] for i in range(6)) - E_s)
    check(
        "5. the single-wrap NF has support {0,1} and IS affine (deg_z = 1)",
        max(ncr[i] for i in supp_s) == 1
        and sp.Poly(dep_s, ds).coeff_monomial(ds ** 2) == 0,
        f"support {supp_s}, max crossing-number {max(ncr[i] for i in supp_s)}; "
        f"d^2 coeff = {sp.Poly(dep_s, ds).coeff_monomial(ds ** 2)}. The 2026-06-16 "
        "audit vector is the SINGLE-WRAP NF — a different object from the typed one",
    )

    # ---- 6. both counits reproduce the 2026-05-11 audit's quoted values ----
    mp.mp.dps = 50
    from qou_substrate.constants import q_at                  # proton pin
    q0 = q_at(50)
    hnum = q0 - 1 / q0
    eps_s = sp.lambdify(h, sp.expand(sum(single)), "mpmath")(hnum)
    eps_t = sp.lambdify(h, sp.expand(sum(dt)), "mpmath")(hnum)
    check(
        "6. both counits reproduce the 2026-05-11 audit's 0.18721 / 0.18829",
        abs(abs(eps_s) - mp.mpf("0.18721")) < mp.mpf("5e-6")
        and abs(abs(eps_t) - mp.mpf("0.18829")) < mp.mpf("5e-6"),
        f"single-wrap |eps| = {mp.nstr(abs(eps_s), 12)} (audit 0.18721); "
        f"typed |eps| = {mp.nstr(abs(eps_t), 12)} (audit 0.18829)",
    )

    # ---- 7. the NF ambiguity is LARGER than the phase it is used to derive ----
    amb = abs((eps_t - eps_s) / eps_s)
    phase = 1 - mp.mpf("0.9983976687192552")          # 1 - N1_req, the ladder's need
    check(
        "7. the single-wrap-vs-typed ambiguity is 3.6x LARGER than the N=1 phase",
        amb > phase,
        f"|eps_typed - eps_single|/|eps_single| = {mp.nstr(amb*100, 6)}% vs "
        f"1 - N1_req = {mp.nstr(phase*100, 6)}%; ratio {mp.nstr(amb/phase, 4)}x. "
        "A 0.16% phase cannot be derived from an object whose NF convention is "
        "unsettled at 0.58%",
    )

    # ---- 8. and the audit's own 1.00579 basis-change factor is exactly this ----
    check(
        "8. the ambiguity IS the audit's 1.00579 basis-change factor",
        abs((1 + amb) - mp.mpf("1.00579")) < mp.mpf("5e-6"),
        f"1 + ambiguity = {mp.nstr(1+amb, 8)} vs the 2026-05-11 audit's 1.00579 "
        "('typed-crossings 6-term NF picks up nonzero L±, e- contributions that "
        "exactly cancel at single wrap') — same object, recomputed from scratch",
    )

    print()
    if failures:
        print(f"FAILED {len(failures)}/8: {', '.join(failures)}")
        return 1
    print("8/8 assertions hold.")
    print()
    print("READING: the Q_beta counit chain rests on the SINGLE-WRAP NF. The")
    print("affineness -- hence the abelian deflation of branch 3 -- holds for that")
    print("object and NOT for the typed 6-term NF the live mass compute uses, whose")
    print("difference has full support. The two disagree by 0.579%, which is 3.6x")
    print("the 0.160% N=1 phase under derivation. Scope-(a): settle which NF is")
    print("canonical before deriving anything at this precision.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
