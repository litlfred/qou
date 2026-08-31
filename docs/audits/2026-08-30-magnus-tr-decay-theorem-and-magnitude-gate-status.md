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

## 2. The Δ_λ magnitude gate — CORRECTED (my "μ₄ not done" was a stale over-claim)

> **🛑 CORRECTION (2026-08-30, same day, after a proper corpus-grep).** The
> version of this section first committed (PR #6298) declared *"the ONE concrete
> open step is μ₄ at A=4 — not done here"*. **That is wrong.** μ₄-at-A=4 **IS
> done**: `helium4_mu4_cluster_moment_probe.py` (GAP-8, bean `qou-6wil`) computes
> all 2⁶=64 subset traces at H₁₂ (77 partitions) with exactly the generalized BKL
> band bonds for the 3 non-adjacent pairs (0↔2, 1↔3, 0↔3) and the ⁴He-derived
> (p,p,n,n) flavour templates — the construction I proposed "needed building"
> already exists. Result: **μ₄/μ₃ = −1.0206 vs target −9.7522 — the alternation is
> REPRODUCED, the magnitude ratio is off by 9.56×.** I quoted the
> `ursell-slot-alignment` witness's "not done here" (which meant *in that probe*)
> and failed to grep `helium4_mu4_cluster_moment` — which was in my own earlier
> `ls`. This is the precise "declared open against a closed corpus item" failure
> AGENTS.md's corpus-grep rule exists to prevent, and I hit it in a doc *about*
> being careful.

**The ACTUAL frontier is the ~10× magnitude gap, attacked from many routes.** The
sign/alternation structure of the cluster ladder is now confirmed at A=4; what
remains open is the **magnitude**, and it is an extensively-worked front — beans
`qou-gnow`/`qou-j3bs` (MAGNITUDE ATTACK A/B), `qou-mssy` (two-channel),
`qou-6r6d`/`qou-avv6` (A=3 ROUTE 2/5), `qou-8ex3` (GAP-8 Habiro/cyclotomic),
`qou-w49j` (T5), plus successor probes `a4_brunnian_magnitude_vs_mu4`,
`mu4_rhoF_cluster_derivation`, `mu4_vs_nuclear_4n_force_bound`. This is **not** a
place for a parachuted bounded contribution; the epic `qou-xu6t` owns it.

**Honest conclusion for this directive:** I cannot meaningfully advance the
magnitude gate in a session — it is large, mature, multi-route, and already past
the step I mis-scoped as open. The correct move is to defer to `qou-xu6t`, not
duplicate it. The one thing this session's infrastructure genuinely offers is the
mpfr 3.8× / sparse H₁₂ tooling, if any of those magnitude probes is compute-bound.

### Historical (the mis-scoped detail, kept for the record)
The earlier state I read (from `ursell-slot-alignment.witness.json`, `qou-6ind`):

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

## 3. Bottom line (corrected)

- **Theorem (`qou-o6ov`):** real progress — statement corrected to `|tr|/dim`, two
  proof routes closed (Kerov–Olshanski refuted; 2-row not clean), cluster/cumulant
  route isolated as the remaining one. Proof open. This stands.
- **Magnitude gate:** my "μ₄-at-A=4 is the one open step, not done" was **WRONG** —
  μ₄-at-A=4 is done (GAP-8/`qou-6wil`: alternation reproduced, magnitude off 9.56×),
  and the real frontier — the ~10× **magnitude** gap — is a large, mature,
  multi-route front (`qou-xu6t`; a dozen MAGNITUDE-ATTACK beans + successor probes).
  I cannot meaningfully advance it in a session and should not duplicate it. The
  honest contribution here is the correction itself and deferring to the epic;
  the session's mpfr/sparse H₁₂ tooling is offered if any magnitude probe is
  compute-bound.
- **Process note:** this correction was caught by a proper six-path corpus-grep
  that I should have run *before* writing §2 the first time. The lesson is the one
  already in AGENTS.md — grep `computations/` fully (not one witness's "not done
  here") before declaring anything open.
