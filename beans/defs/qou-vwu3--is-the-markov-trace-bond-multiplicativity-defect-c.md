---
# qou-vwu3
title: Is the Markov-trace bond-multiplicativity defect CHARGE-sensitive? The n=4 cross term is derived on BARE generators; the production bonds are charge-dressed
status: in-progress
pr: 8278
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-14T17:46:48Z
updated_at: 2026-11-15T17:10:00Z
parent: qou-v2om
---

## ANSWERED 2026-09-14 — the defect IS charge-sensitive, and its charge dependence is ONE bond factor

Probe: `computations/probes/dressed_interleaved_cross_term_charge_parity_probe.py`
(11/11, exact sympy over `ℚ(q,d₀,d₁,d₂)`, zero raw float64 in the witness).
Lean: `QOU/MassTheory/BondChannelTzParity.lean` §7, 7 theorems, sorry-free,
axioms `[propext, Classical.choice, Quot.sound]`.

### First, the name was wrong and it matters

I had called the target "a non-Markov-invariant functional". The Markov trace **is**
Markov-invariant. What fails is **bond-multiplicativity** — on an interleaved word
class the trace of a product of bond letters is not the product of their traces, and
the defect depends on the ORDER of the letters. That order-dependence is the
exchange-sensitivity the arc wants, and it is a property of the *existing* trace, not
of a new object. Chasing a "new functional" would have been chasing nothing.

### The derivation

`qou-kru4` establishes the defect on **bare** generators at `n = 4`:
`tr(g₀g₁g₀g₂g₁) − tr(g₀²g₁²g₂) = z(z² − hz − 1)`, negative at convention D.
Production bonds are **charge-dressed**: `b_i = σ_i + d_i·1` with `d_pp = 0`,
`d_pn = −h(½ − δ/4)`, `d_nn = −h`. Nobody had asked whether the defect sees charge.

Dressing the letters and splitting under the charge conjugation `M : d ↦ −h − d`
(an involution exchanging `d_pp` and `d_nn`):

    mirror-ODD part ≠ 0        — so the defect IS charge-sensitive
    odd part = −(q⁴+q²+1)(2d₂q + q²−1) / (2q(q²+1)²)

Since `q² − 1 = qh`, the numerator is `q(2d₂ + h)`, vanishing exactly at the
charge-symmetric midpoint `d₂ = −h/2`. That shape says the whole thing factors, and
it does, **exactly**:

    Δ(d₀,d₁,d₂) = (z + d₂) · (z² − h z − 1) = f₂ · (convention-D Markov defect)

with **`d₀` and `d₁` absent from `Δ` entirely**. The two *interleaved* bonds drop
out; only the Markov-**peeled** bond survives. Control: setting `d = 0` reproduces
the recorded `−q³(q²−q+1)(q²+q+1)/(q²+1)³` exactly, so the harness is the verified one.

### Why this PRUNES, and it is the point

`z² − hz − 1` is a function of `q` alone — charge-**blind**. Multiplying by a
charge-blind scalar cannot move a mirror odd/even ratio, so

    Δ_odd/Δ_even  ==  f₂_odd/f₂_even       identically

and the interleaved word class inherits the bond channel's isospin parity **verbatim**
— the same structure `bondOfTz_even_iff_classical` proves cannot be even at any
`q > 1`, and the same α-free discriminant that misses by 19.0 % (`qou-1pig`).

**So the word-class route can supply MAGNITUDE and provably cannot supply a different
CHARGE STRUCTURE.** That is not a disappointment for `qou-kru4`, whose interest in it
is the extensive term (the defect is negative ⇒ extra binding) — it is a clean
separation of what that route can and cannot do.

Lean §7 states the general principle rather than the instance:
`parity_ratio_const_mul` — *any* nonzero charge-blind multiplier leaves the ratio
fixed. So **every** future proposal of the shape "keep the bond factor, multiply it
by a new scalar" is excluded from fixing the parity, whatever the scalar is.
`crossTerm_even_iff` and `crossTerm_oddPart_ne_zero` transfer §3's exclusion;
`markovDefect_ne_zero` discharges the nonvanishing hypothesis for every `q > 0`.

At the proton pin, on the ³H/³He mirror bond pattern (scope (a), `n = 4`, not a
nucleus): `Δ(pn,pn,nn) = −0.30381145162`, `Δ(pn,pn,pp) = −0.46117158032`,
difference `0.15736012870`.

### Scope

**(b)** for this cross term: the invariant is the exact factorisation, and a
charge-blind factor cannot change a ratio. **(a)** as a statement about word-class
routes in general — this is one interleaved word at `n = 4`, and other classes at
higher `n` need not factor this way. Which word class a nucleus is remains `qou-5vhf`;
the production atom word is sequential, so **no production number moves**.


## 🛑 SAME DAY — the n=4 prune does NOT generalise. Reopened.

Tested immediately, because a prune is only a prune if it survives a longer word.
At `n = 5` with **two** re-crossings (`b₀b₁b₀b₂b₁b₃b₂` against `b₀²b₁²b₂²b₃`, same
generator multiset), symbolic in `q`, 2 seconds:

    Δ₅ = f₃ · (z² − h z − 1) · ( f₀² + f₂² + (q⁴+1)/(q²+1)² )

verified exactly. Three structural facts:

- the **peeled** bond `f₃` still factors out **linearly**, exactly as at `n = 4`;
- the **interleaved** bonds `f₀`, `f₂` now enter at **degree 2** — additively, with
  **no `f₀f₂` cross term**;
- `d₁`, the one generator that never re-crosses after a neighbour, is **absent at
  both `n`**.

**Consequence, and it reverses this bean's headline.** A quadratic has a
charge-DEPENDENT mirror-even part, so the parity ratio is no longer forced —
measured, `Δ₅ odd/even ≠ f odd/even`, where at `n = 4` it was equal and that
equality *was* the whole prune. `parity_ratio_const_mul` is unconditional and
untouched; what is word-specific is the *premise* that the cross term has the shape
"bond factor × charge-blind scalar". At `n = 4` it does. At `n = 5` it does not.

**So the word-class route is OPEN at `n = 5`, and the interesting object is the sum
of squares.** The `n=4` answer stands as recorded — it closes that cross term, and it
closes the mechanism wherever a construction genuinely has that shape.

Probe now 15/15. Lean §7 carries the scope caveat so the theorem cannot be cited as
closing the route.

**Open, in order:**
- [ ] Split `Δ₅` under the mirror and report the odd/even ratio against the bond
      factor's and against the AME target. It is a derived number — `f₀`, `f₂`, `f₃`
      and `c(q)` are all fixed by `q₀`, nothing chosen.
- [ ] Is `f₀² + f₂²` (sum of squares, no cross term) a general pattern or an `n=5`
      accident? `n = 6` decides, and the probe runs in seconds.
- [ ] Which word class a nucleus actually is — `qou-5vhf`, unchanged. The production
      atom word is sequential, so none of this moves a production number yet.


## Both open items ANSWERED — 2026-09-14 second tranche

Probe now **20/20**; Lean §8 adds 7 theorems, sorry-free, axioms
`[propext, Classical.choice, Quot.sound]`. Sweep 7 ok / 0 RED.

### Item 1 — the parity ratio in closed form, and it CAPS

The `n = 4` ratio is not merely "inherited from the bond factor" (§7) — it is

    odd/even  =  ((q⁴ − 1)/(q⁴ + 1)) · T_z        EXACTLY

so on the physical range `|T_z| ≤ 1` it is **capped** at `(q⁴−1)/(q⁴+1)`, attained
only at the pure like-pairs. At the proton anchor the cap is **0.205704077252**.

Enumerated over **all 27** `(d₀,d₂,d₃)` assignments — nothing selected — the `n=4`
achievable range is exactly `[−0.2057040773, +0.2057040773]`, and the AME target
(derived, not transcribed: `b3_asym/b3_sym = 0.267754902581`) **exceeds the cap by
30.17 %**. So this is a scope-**(b)** exclusion with the invariant named: *no bond
assignment whatsoever* lets the `n = 4` interleaved cross term reach the observed
mirror-asymmetry ratio.

Internal check that passed on the way: `pn,nn,nn` and `nn,pn,nn` agree to all
digits, confirming `d₀` and `d₂` enter symmetrically as the `f₀²+f₂²` form requires.

**Deliberately NOT formalised: the comparison to AME.** Lean carries the cap as
pure algebra; what the cap is worth is an empirical question and belongs in the
probe and this bean. (Owner preference: empirical predictions do not enter formal
proofs.)

### Item 2 — NO. The sum of squares is an `n = 5` accident.

At `n = 6` with **three** re-crossings (`b₀b₁b₀b₂b₁b₃b₂b₄b₃`), symbolic in `q`,
14 s:

- **cross terms appear** — `d₀d₁`, `d₀d₃`, `d₂d₃` all carry nonzero coefficients,
  where `n=5` had `f₀² + f₂²` **additively with no `f₀f₂` term**;
- **`d₁` no longer drops** — degrees are `[2,2,2,2,1]` in `(d₀,d₁,d₂,d₃,d₄)`,
  against `[2,0,2,1]` at `n=5`. So "the never-recrossed bond drops out" is also
  not general.

**What DOES generalise, now 3-for-3:** the Markov-**peeled** bond factors out
linearly, `Δ_n = f_last · (z²−hz−1) · K_n`, at `n = 4, 5, 6`.

### 🛑 The fit hazard this exposes, and it is the more important half

Max `|ratio|` over all assignments, at the proton anchor:

    n = 4   0.2057040773      AME target NOT reachable
    n = 5   0.3928278687      reachable
    n = 6   0.4935268768      reachable

The envelope **grows strictly with word length** and is bounded by 1 — since
`ratio = (a−b)/(a+b)` with `b` the mirror image, `|ratio| < 1` exactly while `a`
and `b` share a sign, and the bound is approached as more dressings enter the
kernel. **A long enough word can be made to bracket any target below 1.** So the
`n = 4` cap is a real exclusion, and `n ≥ 5` is **not a prediction**: reaching the
observed ratio by choosing `n`, or by choosing the assignment, is selection
against the target and is forbidden (§NO FITTING). No assignment at `n = 5` even
equals the target — the nearest bracket it at `0.2058` and `0.3022`.

### Status

Items 1 and 2 are closed. Bean stays **`todo`**: item 3 is unchanged and is the
one that matters — **which word class a nucleus actually is** (`qou-5vhf`). Until
that is derived independently, nothing here predicts anything, and the production
atom word is sequential, so no production number moves.

## 2026-11-15 — re-scoped by the γγ rule

The owner ruled that the γγ selection rule also covers the nuclear bond letters. Any number in this bean computed on the single-crossing interface letters of `atom_braid_word_3A` (`d_k`, `μ_e`, the chain law `∏(z_D + d_k)`, the `b₃` magnitudes −1.2277 / −0.7973 MeV, or a sign map on that word) is now a record of a superseded word, not a current result. Lean results stated for generic bond weights are unaffected. The redo waits on a γγ-selected word per nucleus (PR #7876). Record: `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`. The bean stays open.

## Progress Update (PR #8278 — `status: in-progress`)

- [x] Formalized pure Lean 4.24.0 module(s) (`QOU/MassTheory/IsospinChannelReachabilityAndB3ChainSign.lean`, `QOU/MassTheory/PeeledMarkovDefectAndHigherInterleaving.lean`, `QOU/MassTheory/GradedLogPairCancellationAndH3TowerCollapse.lean`) with `0 sorry` and `0` findings across all 6 static vacuity audits.
- [x] Added 50-dps `mpmath` probe `computations/probes/isospin_b3chain_markov_defect_logjet_h3tower_probe.py` and 2-commit stamped witness `computations/probes/isospin-b3chain-markov-defect-logjet-h3tower-probe.witness.json` (`allPassed: true`, `0` raw `float64`).
- [x] Opened and signed [PR #8278](https://github.com/litlfred/qou/pull/8278) (`ready: b3288da132ea8d0d185d184a5e18432c89e4858e`).
