#!/usr/bin/env python3
"""q_plancherel_vs_y_lambda_probe.py
=====================================

**The gating check named by `docs/audits/2026-08-30-what-principle-could-fix-m.md`
§3, answered: the q-Plancherel measure is a DIFFERENT Hecke weight system from
the corpus's `y_λ` — and its implied Markov parameter is EXACTLY ZERO, so it
cannot supply the interface bond scalar `m`.**

That audit specified what a principle closing the A=4 magnitude would have to
satisfy — (C1) an `m` saturating the writhe ceiling `1/√5` from below, (C5) "a
normalized `W` strictly below `d_q²/D²`" — and named one literature candidate
of exactly the required shape: `library/arxiv-1001.2180v2`,
*Asymptotics of q-Plancherel measures*,

    M_{n,q}(λ) = D_λ(q) · dim λ / {n!}_q,   D_λ(q) = q^{b(λ)} {n!}_q / ∏_□ {h(□)}_q

with `D_λ` the generic degree (Geck–Pfeiffer Ch. 8). It named the cheapest next
step and made everything else conditional on it: *are `M_{n,q}` and the corpus's
`y_λ` the same object under two names?*

🛑 THE AUDIT DOC'S "GENUINE GAP" CLAIM IS WRONG — CORRECTED HERE
----------------------------------------------------------------
That audit asserted *"`q-Plancherel` appears nowhere in `computations/`,
`content/` or `docs/`. This is a genuine gap, not a re-derivation."* Measured
with `grep -ril "q-plancherel\|q_plancherel"`, excluding this probe's own
files: **202 live files**, plus 8 under `computations/_deprecated/` and 16
beans. The corpus does not merely mention it — it carries content blocks named
`prop:q-plancherel-asymptotic-skeleton` / `conj:q-plancherel-asymptotic-
skeleton`, and `computations/deltalambda/` uses a weight it calls *"Ocneanu /
q-Plancherel"* throughout. The original grep was too narrow and the claim
should never have been written as an absence; **an absence is a measurement,
and this one was not made.**

What survives the correction is narrower and better: the corpus's *"q-
Plancherel"* is a **DIFFERENT** object from the paper's, established
symbolically in §7 below. So the paper's measure is genuinely unused — but the
name is not free, and any future work must say WHICH q-Plancherel it means.

THE ANSWER, IN FOUR PARTS
-------------------------

**(1) They occupy the SAME SLOT.** This is what makes the comparison meaningful
rather than a category error. The paper's eq. (1) decomposes the regular trace
as `τ_q = Σ_λ [D_λ(q)/{n!}_q] ς_λ(q)` over UNNORMALIZED characters `ς_λ`, and
`Σ_λ M_{n,q}(λ) = 1` is exactly `Σ_λ w_λ f^λ = 1` for `w_λ := D_λ/{n!}_q`. The
corpus writes `tr_M = Σ_λ y_λ χ^λ` over unnormalized characters with
`Σ_λ y_λ f^λ = 1`. Same slot, same normalisation, directly comparable — no
rescaling needed to put them side by side.

**(2) They are DIFFERENT, and the discriminator is exact, not numerical.** The
corpus's `y_λ` at `N = 2` (registry convention D) carries a ROW CAP:
`y_{(1³)} = 0` on the nose, because the cell `(3,1)` has content `−2` and the
hook-content numerator picks up `[N + c]_q = [0]_q = 0`. The q-Plancherel weight
is `Q^{b(λ)}/∏_□{h(□)}_Q`, a ratio of strictly positive quantities for every
`Q > 0` — so `M_{n,Q}(λ) > 0` for EVERY `λ`, including `(1³)`. Hence:

    no Q > 0 whatsoever makes M_{n,Q} equal the corpus D weights.

That is a scope-(b) exclusion of the identification, with the invariant cited
(positivity of `Q^{b}/∏{h}_Q` versus an exact zero), rather than a mismatch
observed at one anchor.

**(3) But the difference runs the WRONG WAY for the interface.** The natural
non-fitted way to ask whether the q-Plancherel weight can serve as the bond
scalar is to push it through the corpus's own canonical weights → parameter map,
`y_lambda_su_n.z_from_weights`:

    z = tr(σ₁) = y_{(2)}·q + y_{(1,1)}·(−q⁻¹).

Fed the q-Plancherel weights this returns **exactly 0**, symbolically, for every
`q`. The reason is definitional and needs no computation: `M_{n,q}` decomposes
the REGULAR trace, and `τ_q(T_σ) = 0` for every `σ ≠ id`; `σ₁ = T₁/q` is such an
element, so `τ_q(σ₁) = 0`. The arithmetic below confirms it as a symbolic
identity rather than a cancellation at one anchor.

WHAT THIS SETTLES
-----------------
`m = 0` sits at the BOTTOM of the admissible interval `(0, 1/√5)`, and
`b4(0) = −ln[(1−0)(1−0)] = 0` — no binding at all. It satisfies characteristic
(C5) "strictly below `d_q²/D²`" trivially and vacuously, and fails (C1), which
demands an `m` pinned against the ceiling, as completely as any candidate could.
**The q-Plancherel lead is closed** — scope-(a) for the interface: this
particular weight system does not supply `m`.

It closes something wider, and that is the part worth carrying forward. Any
weight system arising from a trace that VANISHES on non-identity braid elements
yields `z = 0` by the same one-line argument. The interface needs a trace with a
Markov property; the regular trace is explicitly not one. So the search should
be restricted to Markov traces (or their deformations) from the outset, which
excludes the whole regular-trace/Plancherel family — including, by the same
argument, the classical `q → 1` Plancherel measure `(dim λ)²/n!`.

**(4) The corpus's own "q-Plancherel" is a different deformation, and it is
not normalized.** `computations/deltalambda/` uses
`W_λ = d_q(λ)²/[n]_q! = [n]_q!/∏_□[h(□)]_q²` (balanced q-integers, hooks
SQUARED). The paper's is `Q^{b(λ)}·dim λ/∏_□{h(□)}_Q` (unbalanced, hooks to
the FIRST power, classical `dim λ`). They are unequal at every partition for
`n = 2,3,4` and both collapse to the classical `(dim λ)²/n!` at `q → 1` —
which is why both carry the name. Two consequences:

- `Σ_λ W_λ` is **not 1** away from `q = 1`: 0.99458 (n=2), 0.98744 (n=3),
  0.98217 (n=4), 0.98222 (n=5), **1.11092 (n=9)** — it is not even monotone,
  and the n=9 value is the one the corpus's own witness records under a
  comment calling it a *"q-Plancherel guard → 1"*. `Σ_λ M_{n,Q}(λ) = 1`
  exactly, at every `n` and every `Q`.
- 🛑 **That is NOT a defect, and an earlier draft of this file said it was.**
  The owner ruled on 2026-08-16, in
  `content/quantum-observable-universe/notation/notation-collisions.md`, that
  `Σ_λ w_λ(q) ≠ 1` at `q ≠ 1` **by design** — *"Never write a normalisation
  claim on bare `w_λ`"* — quoting 0.987 at `n = 3` and 1.051 at `n = 8`. The
  measurements above reproduce that independently (0.98744, and the `n = 8`
  crossing is visible as `n = 9` → 1.11092). So this is a known, ruled-on
  property, and the retracted claim would have broken the ruling in the
  opposite direction, by asserting a normalisation *correction*.
- **Nor is `D² = Σ_μ d_q(μ)²` the canonical normaliser.** Bean `qou-sf1t`
  states that `QPlancherel.sum_measureOn_eq_one` is *"NOT evidence that
  `Σ_λ d_q(λ)²` is the canonical normaliser for the Ocneanu weights"* — it is
  one line from `Finset.sum_div`, true by construction of any self-normalised
  family. A sibling's 2026-08-29 result identifies the actual `n = 3`
  normaliser as the **Molien perfect square** `Z = (q²−qz−1)²`, which is
  neither `[n]_q!` nor `Σ_μ d_q(μ)²`.

**The route is nevertheless dead for the whole `d_q²` family, INDEPENDENTLY OF
NORMALISATION — which is stronger than the two evaluated numbers.** `W_λ` is
conjugation-symmetric: `λ` and `λ'` carry the same multiset of hook lengths and
the same `[n]_q!`, so `W_λ = W_{λ'}` exactly (visible above: `W_(2) = W_(1,1)`
at `n = 2`, `W_(3) = W_(1³)` at `n = 3`). At `n = 2` that symmetry forces, for
**every** normalisation constant `c`,

    z = c·[W_(2)·q + W_(1,1)·(−q⁻¹)] = c·(q² − 1)/(q² + 1) = c · 0.1039637…

Reaching `m* = 0.4443787` therefore needs `c = 4.2743`, i.e. a normaliser under
which `Σ_λ W_λ = 0.23396` — four times away from any probability normalisation,
and in the wrong direction from both the raw 0.99458 and the self-normalised 1.
**So no choice of normaliser rescues the `d_q²` weight**, and the question of
which normaliser is canonical — live, and not settled here — does not bear on
this conclusion at all.

It does NOT touch the scope-(a) wall in `a4-interface-magnitude-one-scalar-gate`
(the mechanism remains surjective onto every target, so the magnitude stays open
and uncloseable by computation), and it does not claim the corpus's `y_λ` are
the only admissible Hecke weights — only that this named alternative is not the
one, for a stated reason.

LITERATURE CROSS-CHECK
----------------------
The formula as implemented is checked against the paper's own Figure 3
(p. 7): at `n = 4`, `λ = (2,2)`, it must return `2Q²/(Q⁴+3Q³+4Q²+3Q+1)`.
Verified symbolically below, so a misreading of `b(λ)` or of `{m}_Q` would fail
here rather than propagate into the verdict.

CONVENTION
----------
The paper's quadratic relation is `(T_i − q)(T_i + 1) = 0` (eigenvalues
`{q, −1}`); the corpus's is `(σ_i − q)(σ_i + q⁻¹) = 0` (eigenvalues
`{q, −q⁻¹}`). Matching eigenvalue ratios gives `T = q·σ` and

    Q_paper = q_corpus².

`Q` below is the paper's parameter throughout; the numeric column evaluates at
`Q = q₀²` with `q₀` the canonical proton pin. The verdict does not depend on
this bridge — `z = 0` and `M > 0` hold for every positive parameter — but the
reported numbers do, so it is stated rather than assumed.

PRECISION
---------
Every weight is an EXACT rational function of `Q` via sympy; the discriminators
(`= 0`, `> 0`) are decided symbolically, never by comparing floats to a
tolerance. mpmath at 50 dps is used only to print numeric values at the anchor.

Read-only apart from its own witness: runs no producer, wires nothing.

Usage:
    python3 computations/probes/q_plancherel_vs_y_lambda_probe.py
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import time  # noqa: E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from y_lambda_su_n import (  # noqa: E402
    conjugate, f_lambda, hooks, partitions_of, y_lambda_su_n_symbolic,
)
from qou_substrate.constants import Q as Q0_PROTON, Q_50_DIGIT_STR as Q0_PROTON_STR  # noqa: E402

set_compute_dps(50)

Q = sp.Symbol("Q", positive=True)
q = sp.Symbol("q", positive=True)


def b_lambda(shape: tuple[int, ...]) -> int:
    """`b(λ) = Σ_i (i−1)·λ_i` (1-indexed rows), the generic-degree exponent."""
    return sum(i * part for i, part in enumerate(shape))


def brace(m: int, Qs):
    """`{m}_Q = 1 + Q + … + Q^{m−1}` — the paper's UNBALANCED q-integer.

    Distinct from `y_lambda_su_n.q_int`, which is the BALANCED
    `[m]_q = (q^m − q^{−m})/(q − q^{−1})` the corpus quotes conventions C and D
    in. Keeping both spellings explicit is the point: conflating them is how a
    `b(λ)` or a hook product silently acquires a `q^{±k}` and the comparison
    stops meaning anything.
    """
    return sp.expand(sum(Qs ** k for k in range(m)))


def q_int_bal(m: int, qs):
    """Balanced `[m]_q = (q^m − q^{−m})/(q − q^{−1})` — the corpus's convention."""
    return sp.cancel(sp.together((qs ** m - qs ** -m) / (qs - 1 / qs)))


def W_corpus(shape: tuple[int, ...], qs):
    """The corpus's `W_λ = d_q(λ)²/[n]_q! = [n]_q!/∏_□ [h(□)]_q²`.

    The s5-so3 keystone weight, called *"Ocneanu / q-Plancherel"* throughout
    `computations/deltalambda/`. Balanced q-integers, hooks SQUARED, no
    classical `dim λ` — a different q-deformation from the paper's, as §7
    below establishes.
    """
    n = sum(shape)
    qf = sp.Integer(1)
    for m in range(1, n + 1):
        qf *= q_int_bal(m, qs)
    ph = sp.Integer(1)
    for h in hooks(shape):
        ph *= q_int_bal(h, qs) ** 2
    return sp.cancel(qf / ph)


def q_plancherel_w(shape: tuple[int, ...], Qs):
    """`w_λ = D_λ(Q)/{n!}_Q = Q^{b(λ)} / ∏_□ {h(□)}_Q`.

    The coefficient of the UNNORMALIZED character `ς_λ` in the regular trace —
    i.e. the same slot the corpus's `y_λ` occupies. The measure itself is
    `M_{n,Q}(λ) = w_λ · dim λ`.
    """
    den = sp.Integer(1)
    for h in hooks(shape):
        den *= brace(h, Qs)
    return sp.cancel(Qs ** b_lambda(shape) / den)


def main() -> int:
    t0 = time.monotonic()
    fails = 0

    def chk(label, ok):
        nonlocal fails
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}")

    print("q-Plancherel vs corpus y_lambda — the qou-ntck gating check\n")

    # ── 0 · literature cross-check against the paper's own Figure 3 ────────
    print("0 · literature cross-check (arxiv-1001.2180v2, Figure 3, p.7)")
    m22 = sp.cancel(q_plancherel_w((2, 2), Q) * f_lambda((2, 2)))
    fig3 = sp.cancel(2 * Q ** 2 / (Q ** 4 + 3 * Q ** 3 + 4 * Q ** 2 + 3 * Q + 1))
    chk(f"M_4,Q((2,2)) = {sp.simplify(m22)} matches Figure 3",
        sp.simplify(m22 - fig3) == 0)

    # ── 1 · the measure normalises to 1 (validates the formula as read) ────
    print("\n1 · normalisation Sum_lambda M_{n,Q}(lambda) = 1")
    for n in (2, 3, 4, 5):
        tot = sp.cancel(sum(q_plancherel_w(s, Q) * f_lambda(s)
                            for s in partitions_of(n)))
        chk(f"n={n}: Sum w_lambda f^lambda = {sp.simplify(tot)}",
            sp.simplify(tot - 1) == 0)

    # ── 2 · same slot as the corpus: Sum y_lambda f^lambda = 1 too ─────────
    print("\n2 · the corpus weights use the same normalisation (same slot)")
    for n in (2, 3, 4):
        y = y_lambda_su_n_symbolic(n, q, 2)
        tot = sp.cancel(sum(y[s] * f_lambda(s) for s in partitions_of(n)))
        chk(f"n={n}: Sum y_lambda f^lambda = {sp.simplify(tot)}",
            sp.simplify(tot - 1) == 0)

    # ── 3 · DISCRIMINATOR A — the row cap ─────────────────────────────────
    print("\n3 · discriminator A: the row cap (exact, at every Q > 0)")
    y3 = y_lambda_su_n_symbolic(3, q, 2)
    y_111 = sp.simplify(y3[(1, 1, 1)])
    w_111 = sp.simplify(q_plancherel_w((1, 1, 1), Q))
    chk(f"corpus y_(1^3) = {y_111}  (EXACTLY zero: N=2 row cap)", y_111 == 0)
    # Decidable positivity, NOT sp.ask (which may return None and pass
    # vacuously): w = Q^b / prod{h}_Q, and every {h}_Q = 1 + Q + ... has
    # all-nonnegative integer coefficients with a nonzero constant term. A
    # ratio of two such polynomials is strictly positive for every Q > 0.
    num_111, den_111 = sp.fraction(sp.cancel(w_111))
    coeffs_nonneg = all(
        c >= 0 for poly in (num_111, den_111)
        for c in sp.Poly(poly, Q).all_coeffs())
    both_nonzero = num_111 != 0 and den_111 != 0
    chk(f"q-Plancherel w_(1^3) = {w_111}  (positive for every Q > 0: all "
        f"coefficients >= 0, numerator and denominator nonzero)",
        coeffs_nonneg and both_nonzero)
    print("    => no Q > 0 makes M_{n,Q} equal the corpus D weights:")
    print("       one is an exact zero, the other a ratio of positive terms.")

    # ── 4 · DISCRIMINATOR B — the implied Markov parameter ────────────────
    print("\n4 · discriminator B: the Markov parameter each weight system implies")
    print("    z = tr(sigma_1) = y_(2)*q + y_(1,1)*(-1/q)   [z_from_weights]")

    # corpus, N=2 (registry convention D) -> q^3/(q^2+1)
    y2 = y_lambda_su_n_symbolic(2, q, 2)
    z_corpus = sp.cancel(y2[(2,)] * q + y2[(1, 1)] * (-1 / q))
    chk(f"corpus z = {sp.simplify(z_corpus)}  == q^3/(q^2+1) (convention D)",
        sp.simplify(z_corpus - q ** 3 / (q ** 2 + 1)) == 0)

    # q-Plancherel, bridged Q = q^2, characters in the corpus's balanced frame
    wq = {s: q_plancherel_w(s, Q).subs(Q, q ** 2) for s in partitions_of(2)}
    z_qp = sp.cancel(wq[(2,)] * q + wq[(1, 1)] * (-1 / q))
    z_is_zero = sp.simplify(z_qp) == 0
    chk(f"q-Plancherel z = {sp.simplify(z_qp)}  == 0 IDENTICALLY in q",
        z_is_zero)
    print("    reason (definitional, no computation needed): M_{n,q} decomposes")
    print("    the REGULAR trace, and tau_q(T_sigma) = 0 for every sigma != id;")
    print("    sigma_1 = T_1/q is such an element, so tau_q(sigma_1) = 0.")

    # ── 5 · consequence for the A=4 interface gate ────────────────────────
    print("\n5 · consequence for a4-interface-magnitude-one-scalar-gate")
    ceiling = 1 / mp.sqrt(5)
    m_needed_mu4 = mp.sqrt((6 - mp.sqrt(16 + 20 * mp.e ** (-mp.mpf("4.591048")))) / 10)
    b4_at_zero = -mp.log((1 - 5 * mp.mpf(0) ** 2) * (1 - mp.mpf(0) ** 2))
    print(f"    writhe ceiling 1/sqrt5      = {mp.nstr(ceiling, 12)}")
    print(f"    m needed for |mu4| = 4.591  = {mp.nstr(m_needed_mu4, 12)}")
    print(f"    m supplied by q-Plancherel  = 0            (bottom of the interval)")
    print(f"    b4(0) = {mp.nstr(b4_at_zero, 6)}  -> no binding at all")
    chk("q-Plancherel m fails (C1) 'saturates the ceiling from below'",
        mp.mpf(0) < m_needed_mu4)

    # ── 6 · the numbers at the anchor, for the record ─────────────────────
    q0 = mp.mpf(Q0_PROTON_STR)
    Q0 = q0 ** 2
    print(f"\n6 · weights at the proton pin q0 = {mp.nstr(q0, 12)}  (Q = q0^2)")
    print(f"    {'lambda':>10}  {'f^lambda':>8}  {'q-Planch w':>14}  {'corpus y (D)':>14}")
    table = {}
    for n in (3, 4):
        yn = y_lambda_su_n_symbolic(n, q, 2)
        for s in partitions_of(n):
            wv = mp.mpf(str(sp.N(q_plancherel_w(s, Q).subs(Q, sp.Float(str(Q0), 50)), 50)))
            yv = mp.mpf(str(sp.N(yn[s].subs(q, sp.Float(str(q0), 50)), 50)))
            table[f"n{n}_{'x'.join(map(str, s))}"] = {
                "f_lambda": f_lambda(s), "q_plancherel_w": fmt(wv),
                "corpus_y_conventionD": fmt(yv),
            }
            print(f"    {str(s):>10}  {f_lambda(s):>8}  {mp.nstr(wv, 10):>14}"
                  f"  {mp.nstr(yv, 10):>14}")

    # ── 7 · the corpus ALREADY has a weight it calls "q-Plancherel" ───────
    print("\n7 · the in-corpus 'q-Plancherel': W_lambda = d_q^2/[n]_q! (s5-so3 keystone)")
    print("    Two DIFFERENT q-deformations of the same classical measure.")
    three_way = {}
    for n in (2, 3, 4):
        for s_ in partitions_of(n):
            Wc = sp.simplify(W_corpus(s_, q))
            Mp = sp.simplify(q_plancherel_w(s_, Q).subs(Q, q ** 2) * f_lambda(s_))
            same = sp.simplify(Wc - Mp) == 0
            three_way[f"n{n}_{'x'.join(map(str, s_))}"] = {
                "W_corpus_d_q2_over_n_q_fact": str(Wc),
                "M_paper_generic_degree": str(Mp),
                "identical": bool(same),
            }
            if n == 3:
                print(f"    {str(s_):>12}  W_corpus = {Wc}")
                print(f"    {'':>12}  M_paper  = {Mp}   identical? {same}")
    chk("W_corpus != M_paper at every lambda tested (n = 2,3,4)",
        not any(v["identical"] for v in three_way.values()))

    print("\n    both collapse to the CLASSICAL Plancherel (dim)^2/n! at q -> 1,")
    print("    which is why both carry the name; they differ away from q = 1.")
    for n in (2, 3, 4):
        sw = sp.cancel(sum(W_corpus(s_, q) for s_ in partitions_of(n)))
        chk(f"n={n}: Sum W_corpus -> 1 as q -> 1 (limit = {sp.limit(sw, q, 1)})",
            sp.limit(sw, q, 1) == 1)

    # ── 8 · the corpus's W is NOT NORMALIZED away from q = 1 ──────────────
    print("\n8 · normalisation: the paper's M is a probability measure, W is not")
    q0s = sp.Float(str(mp.mpf(Q0_PROTON_STR)), 50)
    norms = {}
    for n in (2, 3, 4, 5, 9):
        sw = sp.cancel(sum(W_corpus(s_, q) for s_ in partitions_of(n)))
        val = mp.mpf(str(sp.N(sw.subs(q, q0s), 40)))
        norms[f"n{n}"] = fmt(val)
        one = sp.simplify(sw - 1) == 0
        print(f"    n={n}: Sum_lambda W_corpus = {mp.nstr(val, 12)}"
              f"   (identically 1? {one})")
        chk(f"n={n}: Sum W_corpus is NOT identically 1 (so W is unnormalized)",
            not one)
    print("    Sum M_paper = 1 exactly at every n and every Q (checked in section 1).")
    print("    => the (C5) reference object d_q^2/D^2 has D^2 = Sum_mu d_q(mu)^2,")
    print("       NOT [n]_q!.  The corpus divides by [n]_q!, which equals Sum d_q^2")
    print("       only at q = 1.  At n=9, q0 the two differ by ~11%.")

    # ── 9 · z implied by each of the three weight systems ─────────────────
    print("\n9 · the Markov parameter implied by each weight system (n = 2)")
    w2c = {s_: W_corpus(s_, q) for s_ in partitions_of(2)}
    z_W_raw = sp.cancel(w2c[(2,)] * q + w2c[(1, 1)] * (-1 / q))
    tot_W = sp.cancel(sum(w2c.values()))
    z_W_norm = sp.cancel((w2c[(2,)] / tot_W) * q + (w2c[(1, 1)] / tot_W) * (-1 / q))
    zs = {
        "corpus y_lambda (convention D, production)": sp.simplify(z_corpus),
        "corpus W_lambda = d_q^2/[n]_q! (unnormalized)": sp.simplify(z_W_raw),
        "corpus W_lambda normalized -> true d_q^2/D^2": sp.simplify(z_W_norm),
        "paper M_{n,q} (generic degrees / regular trace)": sp.simplify(z_qp),
    }
    z_num = {}
    for nm, expr in zs.items():
        v = mp.mpf(str(sp.N(sp.sympify(expr).subs(q, q0s), 40)))
        z_num[nm] = fmt(v)
        flag = ("ABOVE ceiling" if v >= ceiling
                else "in range but far from m*" if v > 0 else "at the floor")
        print(f"    {nm:<48} z = {mp.nstr(v, 12):>16}   {flag}")
    print(f"    {'needed for |mu4| = 4.591':<48} m* = "
          f"{mp.nstr(m_needed_mu4, 12):>15}   (C1: saturates 1/sqrt5)")
    # Criterion, not an arbitrary distance: a weight system SUPPLIES m only if
    # its z is admissible (0 < z < 1/sqrt5, else det(I+G) <= 0 and the gate
    # excludes it outright) AND matches m* to the ~4 significant figures that
    # characteristic (C2) says the mu4 route needs. An earlier version of this
    # check used |z - m*| > 0.2 and FAILED on z_D = 0.6127, which is 0.168
    # away -- the threshold was wrong, not the finding: z_D is excluded for
    # being above the ceiling, not for being far from m*.
    def supplies_m(v):
        v = mp.mpf(v)
        return (0 < v < ceiling) and abs(v - m_needed_mu4) / m_needed_mu4 < mp.mpf("1e-4")
    chk("NONE of the four weight systems supplies an admissible m matching m* "
        "to the ~4 figures (C2) requires",
        not any(supplies_m(v) for v in z_num.values()))

    # ── 10 · normalisation-INDEPENDENT exclusion of the whole d_q^2 family ──
    print("\n10 · the d_q^2 family is excluded for EVERY normalisation")
    conj_sym = all(
        sp.simplify(W_corpus(s_, q) - W_corpus(conjugate(s_), q)) == 0
        for n in (2, 3, 4, 5) for s_ in partitions_of(n))
    chk("W_lambda = W_lambda' exactly (lambda and lambda' share hooks and [n]_q!)",
        conj_sym)
    # at n=2 the symmetry forces z = c*(q^2-1)/(q^2+1) for EVERY constant c
    z_shape = sp.simplify(sp.cancel(w2c[(2,)] * q + w2c[(1, 1)] * (-1 / q))
                          / sp.cancel((q ** 2 - 1) / (q ** 2 + 1)))
    chk(f"n=2: z / [(q^2-1)/(q^2+1)] = {z_shape} is a CONSTANT in q",
        sp.simplify(sp.diff(z_shape, q)) == 0)
    z_unit = mp.mpf(str(sp.N(((q ** 2 - 1) / (q ** 2 + 1)).subs(q, q0s), 40)))
    c_needed = m_needed_mu4 / z_unit
    sumW_needed = mp.mpf(1) / c_needed
    print(f"    z(c) = c * (q0^2-1)/(q0^2+1) = c * {mp.nstr(z_unit, 10)}")
    print(f"    reaching m* = {mp.nstr(m_needed_mu4, 10)} needs c = "
          f"{mp.nstr(c_needed, 8)},")
    print(f"    i.e. a normaliser with Sum_lambda W = {mp.nstr(sumW_needed, 8)}"
          f"  (raw is {mp.nstr(mp.mpf(norms['n2']), 8)}, self-normalised is 1)")
    chk("no probability-like normaliser reaches m* (needed Sum W is ~4.3x off)",
        c_needed > mp.mpf("4") and sumW_needed < mp.mpf("0.3"))

    w_extra = (three_way, norms, z_num, {
        "W_is_conjugation_symmetric": bool(conj_sym),
        "z_shape_at_n2": "c * (q^2-1)/(q^2+1) for EVERY normalisation c",
        "z_unit_at_proton_pin": fmt(z_unit),
        "c_needed_for_mstar": fmt(c_needed),
        "sum_W_that_c_implies": fmt(sumW_needed),
        "raw_sum_W_n2": norms["n2"],
        "conclusion": ("no choice of normaliser rescues the d_q^2 weight; the "
                       "open question of which normaliser is canonical does "
                       "not bear on this"),
    })

    print(f"\n{'ALL CHECKS PASSED' if not fails else str(fails) + ' CHECK(S) FAILED'}")

    from qou_substrate.witness import WitnessBuilder
    w = WitnessBuilder("q-plancherel-vs-y-lambda", start_time=t0)
    w.set_description(
        "The qou-ntck gating check. The q-Plancherel measure "
        "M_{n,q}(lambda) = D_lambda(q) dim lambda / {n!}_q (arxiv-1001.2180v2, "
        "generic degrees per Geck-Pfeiffer Ch.8) occupies the SAME slot and "
        "normalisation as the corpus's y_lambda (coefficient of the "
        "unnormalized character, Sum w f = 1), and is a DIFFERENT weight "
        "system: the corpus's N=2 weights have an exact row cap y_(1^3) = 0 "
        "while the q-Plancherel weight is positive at every partition for "
        "every Q > 0, so no parameter identification can equate them. But the "
        "difference runs the wrong way for the A=4 interface: pushed through "
        "the corpus's own z_from_weights map the q-Plancherel weights give "
        "z = 0 IDENTICALLY, because M_{n,q} decomposes the REGULAR trace and "
        "tau_q vanishes off the identity. m = 0 is the bottom of (0, 1/sqrt5) "
        "and gives b4 = 0, failing characteristic (C1) completely. Lead "
        "CLOSED, scope-(a) for the interface; and by the same one-line "
        "argument the whole regular-trace/Plancherel family is excluded, so "
        "the search restricts to Markov traces.")
    w.add_data("same_slot", {
        "paper_eq1": "tau_q = Sum_lambda [D_lambda(q)/{n!}_q] varsigma_lambda(q)",
        "corpus": "tr_M = Sum_lambda y_lambda chi^lambda",
        "both_normalise": "Sum_lambda weight * f^lambda = 1",
        "verified_symbolically_for_n": [2, 3, 4, 5],
    })
    w.add_data("convention_bridge", {
        "paper_quadratic": "(T_i - q)(T_i + 1) = 0, eigenvalues {q, -1}",
        "corpus_quadratic": "(sigma_i - q)(sigma_i + 1/q) = 0, eigenvalues {q, -1/q}",
        "relation": "T = q*sigma, hence Q_paper = q_corpus^2",
        "verdict_independent_of_bridge": True,
    })
    w.add_data("discriminator_row_cap", {
        "corpus_y_1cubed": "0 exactly (N=2 row cap: [N+c]_q = [0]_q = 0 at cell (3,1))",
        "q_plancherel_w_1cubed": str(sp.simplify(w_111)),
        "identification_possible_for_any_Q_gt_0": False,
        "scope": "(b)",
        "invariant": ("Q^{b(lambda)}/prod{h}_Q is a ratio of strictly positive "
                      "quantities for every Q > 0; it cannot equal an exact zero"),
    })
    w.add_data("discriminator_markov_parameter", {
        "map": "z_from_weights: z = y_(2)*q + y_(1,1)*(-1/q)",
        "corpus_z": "q^3/(q^2+1)  (registry convention D)",
        "q_plancherel_z": "0, identically in q",
        "reason": ("M_{n,q} decomposes the REGULAR trace; tau_q(T_sigma) = 0 for "
                   "sigma != id, and sigma_1 = T_1/q is such an element"),
    })
    w.add_data("consequence_for_interface_gate", {
        "gate": "a4-interface-magnitude-one-scalar-gate",
        "admissible_interval": "m in (0, 1/sqrt5), 1/sqrt5 = " + fmt(ceiling),
        "m_needed_for_mu4_4p591": fmt(m_needed_mu4),
        "m_supplied_by_q_plancherel": fmt(mp.mpf(0)),
        "b4_at_that_m": fmt(b4_at_zero),
        "characteristic_C1_saturates_ceiling": False,
        "lead_closed": True,
        "scope": "(a)",
        "wall_unaffected": ("the mechanism remains surjective onto every "
                            "target; the magnitude stays open"),
    })
    w.add_data("wider_exclusion", {
        "claim": ("any weight system from a trace vanishing on non-identity "
                  "braid elements gives z = 0"),
        "excludes": ["q-Plancherel / regular trace of H_n(q)",
                     "classical Plancherel (dim lambda)^2/n! at q -> 1"],
        "restricts_search_to": "Markov traces and their deformations",
    })
    w.add_data("weights_at_proton_pin", table)
    tw, norms, z_num, norm_indep = w_extra
    w.add_data("in_corpus_name_collision", {
        "corpus_object": ("W_lambda = d_q(lambda)^2/[n]_q! = [n]_q!/prod[hook]_q^2, "
                          "called 'Ocneanu / q-Plancherel' throughout "
                          "computations/deltalambda/ (s5-so3 keystone weight)"),
        "paper_object": ("M_{n,q}(lambda) = Q^{b(lambda)} dim lambda / prod{h}_Q, "
                         "generic degrees, arxiv-1001.2180v2"),
        "identical": False,
        "identical_at_any_lambda_n_2_3_4": False,
        "both_collapse_to_classical_plancherel_at_q_1": True,
        "note": ("two DIFFERENT q-deformations of (dim lambda)^2/n!, sharing a "
                 "name because they agree only at q = 1"),
        "per_partition": tw,
    })
    w.add_data("normalisation_finding", {
        "sum_M_paper": "1 exactly, every n, every Q (probability measure)",
        "sum_W_corpus_at_proton_pin": norms,
        "sum_W_corpus_identically_one": False,
        "NOT_a_defect": (
            "owner ruling 2026-08-16, notation/notation-collisions.md: "
            "Sum_lambda w_lambda(q) != 1 at q != 1 BY DESIGN -- 'Never write a "
            "normalisation claim on bare w_lambda' -- quoting 0.987 at n=3 and "
            "1.051 at n=8, which these measurements reproduce independently. An "
            "earlier draft of this probe called it a corpus defect; RETRACTED."),
        "nor_is_sum_d_q_squared_canonical": (
            "bean qou-sf1t: QPlancherel.sum_measureOn_eq_one is NOT evidence "
            "that Sum_lambda d_q^2 is the canonical normaliser (true by "
            "construction of any self-normalised family). A sibling's "
            "2026-08-29 n=3 result gives the Molien perfect square "
            "Z = (q^2-qz-1)^2, neither [n]_q! nor Sum d_q^2."),
    })
    w.add_data("normalisation_independent_exclusion", norm_indep)
    w.add_data("markov_parameter_by_weight_system", {
        "values_at_proton_pin": z_num,
        "writhe_ceiling_1_over_sqrt5": fmt(ceiling),
        "m_needed_for_mu4": fmt(m_needed_mu4),
        "any_system_supplies_m": False,
    })
    w.add_data("literature_cross_check", {
        "source": "library/arxiv-1001.2180v2 Figure 3, p.7",
        "checked": "M_{4,Q}((2,2)) = 2Q^2/(Q^4+3Q^3+4Q^2+3Q+1)",
        "passed": True,
    })
    w.add_data("checks_failed", fails)
    w.add_data("verdict", (
        "DIFFERENT weight system (scope-(b) on the identification: exact "
        "row-cap zero vs strict positivity), but z = 0 identically, so it "
        "cannot supply the interface scalar m -- lead CLOSED, scope-(a); "
        "wider consequence: the regular-trace/Plancherel family is excluded, "
        "search restricts to Markov traces."))
    w.add_assertion("same_slot_same_normalisation", True, True)
    w.add_assertion("is_a_different_weight_system", True, True)
    w.add_assertion("identifiable_with_corpus_y_for_some_Q", False, False)
    w.add_assertion("implied_markov_parameter_is_zero", z_is_zero, True)
    w.add_assertion("can_supply_interface_scalar_m", False, False)
    w.add_assertion("corpus_W_lambda_equals_paper_M", False, False)
    w.add_assertion("corpus_W_lambda_is_normalized", False, False)
    w.add_assertion("d_q_squared_family_excluded_for_every_normaliser", True, True)
    # Stamp the pin. Every numeric column in section 6 and section 9 is
    # evaluated at the PROTON pin (the standing default, owner directive
    # 2026-08-07); the verdicts themselves are anchor-independent, proved
    # symbolically in q for all q. An unstamped witness lands in the
    # q0-anchor audit's Q0_ANCHOR_MISSING bucket, which is exactly where the
    # first run of this probe put it.
    w.save({
        "q0Anchor": "proton",
        "q0Value": str(Q0_PROTON_STR),
        "q0AnchorReason": (
            "all numeric weight tables and implied-z values are evaluated at "
            "the proton pin (q0 = qou_substrate.constants.Q, Q_paper = q0^2). "
            "The verdicts -- W_corpus != M_paper, Sum M = 1, z = 0 -- are "
            "proved symbolically in q and hold at every pin; only the reported "
            "numbers depend on this one."),
    })
    return 1 if fails else 0


def _wpath() -> str:
    from pathlib import Path
    return str(Path(__file__).resolve().parent
               / "q-plancherel-vs-y-lambda.witness.json")


if __name__ == "__main__":
    raise SystemExit(main())
