# tr-decay theorem (qou-o6ov) and the Δ_λ magnitude gate — honest status

**Date:** 2026-08-30
**Directive (owner):** work the theorem and the magnitude gate.

This records concrete progress on the theorem and a **correct scoping** of the
magnitude gate — the latter deliberately *not* a rushed μ₄ computation, because a
subtly-wrong one would pollute a Lean-backed epic (see §2).

## 1. The tr-decay theorem (`qou-o6ov`) — refined, two routes closed

**The theorem, corrected.** As first stated — *"|tr(ρ_λ Ω₂_λ)| decays with
b(λ)=n−λ₁"* — it is **false as literally written.** Measured: `|tr(10,2)| =
12634 > |tr(11,1)| = 12211` at A=4 (a bump at b=2). The bump tracks `dim` (which
peaks mid-sector, e.g. dim(7,5)=297 > dim(11,1)=11). The quantity that actually
decays is **`|tr|/dim`** (A=4 2-row: 1110, 234, 71, 28, 19, 22 by b) — equivalently
the y-weighted contribution `c_λ = y_λ·tr`. **Correct statement:
`|tr(ρ_λ Ω₂_λ)|/dim_λ` decays with `b(λ)`.**

**Two proof routes closed (both negatives):**

- **Kerov–Olshanski content-polynomiality — REFUTED** (merged #6291). `tr/dim` is
  not a low-degree polynomial in the content power-sums (A=3, max rel resid stalls
  at 0.08 over 9 terms, no collapse). `ρ·Ω₂` is neither central nor a group-algebra
  element, so the polynomial-functions-on-Young-diagrams framework does not apply.
- **2-row closed-form decay — NOT CLEAN.** The 2-row sector (91% of the
  contribution, closed-form characters exist) does not give a simple decay law:
  `tr(ρ_{(n-j,j)}Ω₂)` is non-monotonic (A=4 ratios drift 0.51–1.03; A=3 sign-flips
  at (5,4)). So there is no tidy closed form to bound in that sector.

**Remaining route:** the cluster/cumulant connected-diagram cancellation
(`tr(Ω₂)=0`), tied to the ingested Procacci–Yuhjtman / Rebenko papers. This is the
open work; the two easy routes are ruled out.

## 2. The Δ_λ magnitude gate — status and the ONE concrete open step

**This is a mature, Lean-backed front (epic `qou-xu6t`), not a fresh gap.** Current
state (from `ursell-slot-alignment.witness.json`, `qou-6ind`):

- The many-body binding **magnitude** is the open item (the per-partition Δ_λ value
  is proved: `(−1)^{n(λ)}·dim`). The missing object is a *super-pairwise additive
  extensive* term; six ansätze failed by trying to force it into a per-block
  intensive weight.
- The cluster/cumulant attack indexes **residual-simplex moments** `μ_k` by particle
  count (`M(A)=Σ_k μ_k C(A,k)`) and **subset-trace mixed differences** `Δᵐg` by bond
  count. Lean-proved, sorry-free: `mu4_unconstrained_below_four`,
  `triangle_moment_decomp`, `moment_pos_of_triple_dominated`,
  `moment_eq_{pair,triple}_iff`.
- Result at A=3: the μ₃ **sign obstruction (#4404) SURVIVES** the Ursell slot
  correction, and the magnitude gap **WIDENS** to 8.04× (T) / 7.70× (³He). No μ₄
  ladder-alternation is inferable — **A=3 data carries no 4-body information**
  (`C(A,4)=0` for A<4).

**The one concrete open step:** compute **μ₄ at A=4** — the 4-body residual-simplex
moment — which needs the **64 subset traces over K₄'s 6 bonds** at H₁₂. The witness
states plainly: *"not done here."*

**Why I did not just compute it (integrity, not punting).** The probe's kernel
`g_of(subset)=perblock(w)` filters the braid word by which *bonds* are in the
subset. For A=3 the 3 bonds are 2 p/n chain interfaces + 1 BKL **band bond** ("c").
For A=4 the 6 bonds are the complete graph K₄: 3 chain interfaces
(`atom_braid_word_3A(2,2)` generators 2,5,8) **plus 3 band bonds for the
non-adjacent pairs (0↔2, 0↔3, 1↔3)**. Constructing those three band bonds correctly
is `qou-xu6t`'s `band_word`/flavour-template machinery; a naive A=4 word that omits
or mis-places them yields a subtly-wrong μ₄ — the worst outcome for a Lean-backed
epic. So the correct contribution is to **build the 6-bond A=4 word with the epic's
band-bond construction**, then reuse `g_of`/the Möbius assembly unchanged.

**Feasibility (good news):** `perblock` is a *Markov*-type trace of a Hecke word,
not the germ trace — so the 64 A=4 subset traces are **character-route cheap at
H₁₂** (unlike this session's Magnus germ compute, which is why μ₄-at-A=4 is
tractable where the Magnus H₁₂ tail is not). The blocker is *correctness of the
6-bond construction*, not compute cost.

## 3. Bottom line

- **Theorem:** real progress — statement corrected to `|tr|/dim`, two proof routes
  closed, cluster/cumulant route isolated as the remaining one. Proof open.
- **Magnitude gate:** correctly scoped — the single open step is μ₄ at A=4 (64
  K₄-bond subset traces, character-route-cheap), gated on building the 3 non-adjacent
  band bonds with `qou-xu6t`'s machinery. Coordinate with that epic before computing;
  do **not** ship a naive A=4 word. Offered infrastructure: the H₁₂ trace tooling
  from this session.
