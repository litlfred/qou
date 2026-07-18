# A_ω fork resolution — both branches converge on the anchor-invariance prune

**Date:** 2026-07-18 · **PR:** #3813 · **Axis:** c₃ bar-odd S / A_ω (1ppq-qbeta)

Consolidates the resolution of the A_ω fork after the 2026-07-18 4₁ 3d-index
work established (scope-(b), cited invariant) that **4₁ is amphichiral ⇒ CS = 0
⇒ the bar-odd datum is not in the u=0 index**. The owner steered the two live
branches: **(1)** deformed (u≠0) median resummation, **(2)** a non-amphichiral
knot (5₂). Both were scoped + tested. They converge on a single Lean-proved
fact.

## The unifying invariant (Lean-proved, sorry-free)

`QOU.QBeta.SRigidity.no_anchor_invariant_realizes_swing`
([`SRigidityPrune.lean:50`](../../content/quantum-observable-universe/lean/QOU/QBeta/SRigidityPrune.lean)):
if a candidate `g : D → R` consumes an anchor-invariant datum
(`datum a = datum a'`) then `g ∘ datum` is anchor-constant, so it cannot equal a
target `S` that swings (`S a ≠ S a'`). Applied: `S` swings 2.44% between the
proton/muon anchors while `q₀` moves ~1e-8 (a ~2×10⁶ sensitivity), so **no
anchor-invariant datum realizes the swing**. This subsumes both fork branches.

## Branch 1 — deformed median resummation: directly computed anchor-blind

Probe [`qbeta_c3_deformed_median_discontinuity_probe.py`](../../computations/probes/qbeta_c3_deformed_median_discontinuity_probe.py)
(2/2). The corpus had *inferred* "no median split" from the 88°-off-ray argument
but never computed the lateral Borel sums. Directly computed, on the committed
deformed κ̃-tower (Borel–Padé[2/2] at the substrate meridian):

- **on-ray** Laplace reproduces the committed `Im 𝔙̃_b = 0.058549995`;
- **lateral** discontinuity `|S_+ − S_−|` scales **linearly** with the straddle
  `δ` (ratios 1.988, 1.997 ≈ 2 as `δ → 0`) ⇒ **smooth, no Stokes jump** on the
  physical substrate ray (a genuine jump would be `δ`-constant, ratio ≈ 1);
- the across-singularity Stokes magnitude `|2πi·Res| = 0.656 ≈ Vol(4₁)/π = 0.646`
  (action-consistent, **anchor-blind**, ~2 sig figs — not a new identification,
  per modular-resurgence T3).

The deformed median resummation is single-valued + anchor-blind ⇒ excluded by
the prune. Reinforced three ways in the corpus (the ξ-frame phase law
`κ̃_n/ξⁿ ∈ (−i)ⁿ·ℝ` to 6e-20; the 88°-off-ray Borel; the saddle `Im 𝔙 = 0`
exactly at both anchors).

## Branch 2 — non-amphichiral 5₂: the writhe is the bar-odd home

Probe [`qbeta_5two_reeb_trace_probe.py`](../../computations/probes/qbeta_5two_reeb_trace_probe.py)
(4/4). Two exact findings:

1. **The q-Reeb trace does NOT carry chirality.** Both `τ_{4₁}(q)` and
   `τ_{5₂}(q)` on the `H₃` block `V_{(2,1)}` are **bar-even** (bar-odd part = 0),
   because `(2,1)` is self-conjugate ⇒ its character is bar-symmetric for every
   braid. So no knot's q-Reeb trace on this block carries a bar-odd part.
2. **The bar-odd datum is the WRITHE**, in the conjugate-pair `(3)/(1,1,1)`
   blocks: `D_odd = ½(χ₍₃₎ − χ₍₁,₁,₁₎)` is `0` for amphichiral 4₁ (writhe 0) and
   `½(q²−q⁻²) ≠ 0` for chiral 5₂ (writhe 2) — a genuine bar-odd sinh-object. At
   the substrate `D_odd(5₂) = sinh(2·ln q₀) = sinh(u_sub) ≈ 0.2102`, literally
   the bar-odd sinh at the deformed-tower meridian.

So 5₂ *does* supply the nonzero bar-odd home 4₁ structurally lacks — but
`D_odd(q₀)` is anchor-smooth (swing 2.4e-8), so its **value** is not the S-swing:
the same anchor-invariance prune binds. (Building 5₂'s full `𝔙_q(5₂)` further
needs its H₅(q) cell + Markov trace + verified CS(5₂) — the flagged obstacle.)

## Where the swing actually lives

The bar-odd swing is intrinsically the **anchor-dependent quantum `𝔙_q` at q₀** =
the `1/u³` ladder-inversion of a smooth numerator `N_odd = S·u³`
(`QOU.QBeta.BarOddLadderShape`; KC21/KC22): the swing and sign-flip are
representational (the `1/u³` amplification of a smooth numerator crossing zero at
`q*`), pinned in precision by the **experimental Q_β** (`dq*/dQ_β ≈ −0.54`), not
by any resummation or knot choice.

The one genuinely-open target is the geometric **`Im 𝔙_q → N_odd` normalization**
(the capstone — where the anchor-dependence enters). The odd-channel D-ladder
q-Borel/Écalle acceleration (sibling #3818) operates on `D(u)` where the swing
lives.

## Net

Neither fork branch produces the swing directly, both for the same Lean-proved
reason (anchor invariance). 5₂'s writhe = `sinh(u_sub)` is a satisfying
identification of the *bar-odd home* 4₁ lacks, but not the swing. The swing is a
representational property of the anchor-dependent quantum volume; its geometric
closure is the `Im 𝔙_q → N_odd` normalization capstone. No c_k wired; no fit;
scope-(a) throughout; the 2·Vol(4₁)=4.06 ≈ |ratio −4.0751| (0.38%) coincidence
remains anti-numerology, **not wired**.
