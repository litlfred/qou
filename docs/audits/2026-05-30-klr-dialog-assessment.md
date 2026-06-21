# KLR / crystal-bases dialog assessment — what (if anything) is actionable

**Date:** 2026-05-30
**Branch:** `claude/sleepy-carson-Lj3RA`
**Trigger:** long external AI dialog re-pitching Khovanov-Lauda-Rouquier (KLR) algebras + Kashiwara crystal bases as (i) a compute-speedup for Gröbner-Shirshov reduction, (ii) a positivity-by-construction layer, (iii) the closure for Δ_λ via Option E.
**Audience:** anyone evaluating whether the dialog content should land in the paper, the Lean formalization, or the compute pipeline.
**Bottom-line up front:** ~60% textbook-accurate; ~70% already encoded in AGENTS.md §7b; ~10% genuine new leverage. The load-bearing claims (compute speedup, dilog-transcendence uniqueness on the electron knot, Δ_λ resolution) do not survive contact with the framework. The proof-simplification audit (below) **finds 0/6 candidates that would meaningfully shorten** existing proofs.

## What the dialog proposed

1. Re-realize the QOU substrate as KLR modules (via Brundan-Kleshchev cyclotomic isomorphism: cyclotomic KLR ≅ cyclotomic Hecke/Ariki-Koike — note: KLR *categorifies* the negative half of U_q(g), not H_n(q) directly).
2. Replace Gröbner-Shirshov / Diamond-Lemma normal-form computation with Kashiwara crystal-graph traversal.
3. Recover positivity of trace coefficients automatically (dim Hom between graded projective KLR modules).
4. Define the cemetery group as a localizing Serre subcategory annihilated by ω.
5. Use Type B folding for chirality / CPT (Z/2Z bar-involution).
6. Argue existence/uniqueness of the Archimedean functor via Bloch-Wigner / dilog transcendence at 3rd or 5th roots of unity.
7. Suggest mass = polynomial · m_0 with m_0 the Planck mass / Higgs VEV.
8. Re-propose Option E (Kashiwara crystal at q→1) as the Δ_λ closure.

## Mathematical assessment

### What is correct (textbook)

- KLR algebras (Khovanov-Lauda 2008, Rouquier 2008) categorify the negative half of U_q(g) for g symmetrizable Kac-Moody.
- Brundan-Kleshchev (2009): cyclotomic KLR ≅ cyclotomic Hecke (Ariki-Koike).
- Canonical-basis positivity for Hecke algebras / Soergel bimodules (Elias-Williamson 2014).
- Type A_{n-1} Schur-Weyl duality between H_n(q) on n strands and U_q(sl_N) on the N-dim fundamental representation.
- Kashiwara crystals at q→0; Lusztig global crystal basis flatness over Z[q, q^{-1}].
- Type B folding gives a Z/2Z-symmetric crystal whose normal forms are bar-involution invariant.

### What is wrong or off

1. **Mis-frames the QOU mass formula.** Dialog repeatedly writes `m = m_0 · P_K(q_0)` with `m_0` as Planck mass or Higgs VEV. The canonical QOU formula since 2026-05-23 (commit `ffdd84409`) is

       m(K) = m_e · VolDensity(K, q_0)

   — a single per-knot evaluation with `m_e` as CAL-1 anchor. The factor the dialog calls `m_0` is exactly the **purged** `λ_scale`. See [`docs/lambda-scale-absorbed-into-vol-density.md`](../lambda-scale-absorbed-into-vol-density.md).

2. **Trefoil is not hyperbolic.** The dialog's "uniqueness of ω via dilog transcendence at 3rd/5th roots of unity" pitch evaluates Bloch-Wigner D(z) on the knot complement. The trefoil complement is Seifert-fibered, so D(z) = 0 there. The argument applies to the figure-eight (Z[ω], ω primitive 6th root), not to the electron knot ansatz. The dialog acknowledges this then proceeds anyway.

3. **Crystal-graph closure is on the failed-ansatz list.** Per [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md) § "Closure attempts (six ansätze, all failed)" and the 2026-05-29 retraction at the bottom of that doc:

   > The six prior failed ansätze (Frobenius co-Casimir, Demazure, LP-Plancherel, LP-Frobenius, **crystal**, augmented Markov) all failed because they tried to derive Δ_λ from single-nucleon data or from q-dependent algebraic expressions.

   The dialog's Option E re-pitch does not address this failure mode.

4. **"GS → crystal traversal speedup" is unsupported.** Canonical-basis / crystal-graph construction is itself expensive (Soergel bimodules, W-graphs, cell decomposition). The dialog supplies no benchmark, no algorithm, no scaling estimate. The current `VolDensity` + LP/SDP pipeline (`lp_dual_solver.py`, `solve_psd_operator_selection_sdp`) already factors the expensive bits.

5. **Cemetery group as Serre subcategory** is a rebranding, not new content. The current cemetery-group narrative already characterizes the off-diagonal terms that annihilate under the trace; calling that "a localizing subcategory" adds no new prediction, no new compute, no new constraint.

6. **Non-abelian anyons everywhere on S¹** overstates: anyon non-abelianness requires specific levels (Ising k=2, Fibonacci k=3, etc.). Our substrate `q_0 ≈ 1.1097` isn't on the unit circle anyway.

### What is already in AGENTS.md §7b (dialog is rediscovering)

The three "structural shortcuts" the dialog spends pages on are already authoring guidance in §7b:

- **Type B folding for chirality / CPT** — matter/antimatter pairing as fixed points of the folded crystal.
- **KLR → KL basis for the classical limit** — q→1 collapses braid statistics to symmetric-group statistics.
- **Demazure sub-crystals for resonances** — incomplete topological states for unstable intermediaries.

The dialog's "new propositions" map almost 1-to-1 onto these existing entries.

### What is genuine new leverage (small)

- **Positivity-as-free-theorem framing.** If a thin KLR layer is ever added to the Lean formalization, the Markov-trace coefficient positivity becomes automatic (dim Hom ≥ 0) rather than a per-block lemma. Clean, not load-bearing — current positivity arguments in the paper are not bottlenecks.
- **Option E direction reinforcement.** Listed productive in AGENTS.md alongside GAP-A-3 / GAP-A-4. The dialog reinforces the direction but does not advance it. Relaunch criteria are recorded below.

## Option E (Kashiwara crystal Δ_λ closure) — status & relaunch criteria

### Current state

- Original gating doc (2026-05-18) marked Option E as TBD.
- 2026-05-26 claimed a deuteron closure via the per-λ formula `B = m_e · |Σ y_λ · χ^λ · sgn(w₀) · f^λ|`.
- 2026-05-29 **retraction**: the full evaluation undershoots every light isotope by 70-90% (D −82.9%, T −77.5%, ³He −69.6%, ⁴He −89.3%); the "zero free parameters" label was false — the `C_knot = 5.852` factor in the deuteron probe was fit to AME, not eliminated.
- **The Δ_λ gate remains open for all A, including the deuteron.**

### Failure mode

Per the retraction:

> The six prior failed ansätze (Frobenius co-Casimir, Demazure, LP-Plancherel, LP-Frobenius, crystal, augmented Markov) all failed because they tried to derive Δ_λ from single-nucleon data or from q-dependent algebraic expressions. The correct Δ_λ is categorical (q-independent: sign × dimension) and the q-dependent geometric correction lives inside χ^λ via the interface operator.

### What a relaunch would need to be different

1. **Per-partition derivation, not single-nucleon.** Take seriously that Δ_λ varies non-trivially across λ ⊢ 3A; do not reduce to single-nucleon scaffolding.
2. **q-independent / categorical.** Do not absorb q-dependent corrections; those live inside χ^λ via the interface operator.
3. **Joint GAP-A-3 / GAP-A-4 progress.** Per the gating doc: GAP-A-3 (brane-tower level selector) and Δ_λ are the same problem; resolving GAP-A-4 (`conj:rho-prefactor-structural`) co-resolves Δ_λ. A bare crystal attempt that ignores these conjectures is doomed to recapitulate the prior failure.
4. **Conditional-on-class formalization** (AGENTS.md §3b-cond). If a candidate categorical Δ_λ rule is identified, axiomatise it as a Lean class (cf. PR `86fec9f5` wrapping `slater_strict_complementarity_kernel_axiom` as a class) so the downstream binding theorems remain rigorous-conditional rather than fit-anchored.
5. **No 7th fit-based ansatz.** Per AGENTS.md Δ_λ gate warning — the three-calibration discipline review catches numerological fits.

### Recommendation

**Do not relaunch Option E as a fresh compute / probe sweep until:**

- A categorical, q-independent, per-partition Δ_λ candidate is sharpened on paper.
- The candidate is tied to GAP-A-3 or GAP-A-4 progress, not derived in isolation.
- A specific testable prediction beyond the deuteron is identified up front (so we don't repeat the deuteron-only over-claim cycle).

In the meantime, **Track B (recursive ρ_ξ for branching combiner)** remains the productive non-Δ_λ-gated work per the original gating doc.

## Proof-simplification audit — findings

**0/6 candidates meaningfully shortened.** Existing GS / positivity / bar-involution arguments are already minimal — one-line Diamond-Lemma citations, direct ring algebra over `CommRing` / `Field`, one-line class-axiom invocations. The proof sites where KLR positivity *would* apply (per-knot integer Wedderburn-block dimensions) are stated as content claims with no proof step to compress.

### Audited candidates

| # | Location | Current technique | Verdict |
|---|----------|-------------------|---------|
| 1 | [`particle-interactions/groebner-shirshov-energy.md:65-73`](../../content/quantum-observable-universe/particle-interactions/groebner-shirshov-energy.md) + sibling `.lean:80-95` | One-line Bergman Diamond-Lemma citation; `energy_path_independent` axiomatized in Lean | **NO** — already a cited black box; KLR / crystal would just substitute one citation for another. |
| 2 | [`braids-and-knots/hecke-normal-form.md:15-28`](../../content/quantum-observable-universe/braids-and-knots/hecke-normal-form.md) | Single-clause Diamond-Lemma appeal; already cross-refs Brundan-Kleshchev crystal traversal as engine alternative | **MAYBE for the compute engine, NO for the proof** — no proof step to shorten. |
| 3 | [`observations/centered-hecke-variance-positive.md:31-34`](../../content/quantum-observable-universe/observations/centered-hecke-variance-positive.md) | Direct algebra: `(q^{1/2}+q^{-1/2})^2 > 4` | **NO** — this is an *archimedean* bound on real `q > 0`, not a `dim Hom ≥ 0` statement. KLR positivity does not supply substrate-dependent inequalities. |
| 4 | [`braids-and-knots/bar-involution.md:228-313`](../../content/quantum-observable-universe/braids-and-knots/bar-involution.md) (33 theorems) | One-line ring-algebra identities over `CommRing` / `Field` | **NO** — Type B folding would buy bar-invariance only at the structural-theorem level; the 33 downstream sign-rule / projection / even-power lemmas are already maximally short. |
| 5 | [`lean/QOU/frobenius_dagger_positive_definite.lean:45-57`](../../content/quantum-observable-universe/lean/QOU/frobenius_dagger_positive_definite.lean) | `claim_dagger_positive` axiomatized in the class; theorem is one line | **NO** — no proof to shorten; already a class-axiom invocation. |
| 6 | [`observations/trace-locality-meets-gs-nonlocality.md:86-93`](../../content/quantum-observable-universe/observations/trace-locality-meets-gs-nonlocality.md) | Cites Jones-Markov + GS + Wenzl factorisation | **NO** — content claim about Wenzl's product factorisation; KLR layer offers no analog. |

### Why no shortening

Two structural reasons the dialog's "simpler proofs" pitch lands empty for QOU as it stands:

1. **The GS / Diamond-Lemma machinery is already abstracted to one-line citations** in current QOU proofs. There is no S-polynomial overlap case-analysis on disk for crystal traversal to replace; the heavy lifting is delegated to the sibling `unital-groebner-bases` paper and to Bergman.
2. **The positivity claims that actually appear are archimedean** (bounds on real `q > 0`) **or already class-axiomatised**, not categorical `dim Hom ≥ 0` claims. KLR positivity supplies the wrong shape of fact: it would give integer non-negativity of Wedderburn-block dimensions, but the paper's positivity needs are about substrate-evaluated trace coefficients.

### What this leaves

The AGENTS.md §7b shortcuts (Type B folding, KLR → KL classical limit, Demazure resonances) remain a sound **authoring guide for new work** — for any *future* proof that would otherwise have to construct positivity by hand, the §7b guidance still applies. They yield **no measurable shortening of the proofs already on disk.**

The single near-miss (Candidate 2, `hecke-normal-form.md`) already cross-references the crystal-graph engine alternative; if the compute pipeline ever ports `groebner-shirshov-engine` to a crystal-traversal backend, the proof side will not need changes.

## Cross-references

- [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) §Refutations item 4 — the **period / z-Habiro axis** (cyclotomic-Galois, `Li₃(ζ₅)`) is orthogonal to the q-side keystone coupling; do not re-aim a period identity at the keystone (same archimedean-re-register failure mode as this dialog's dilog/Bloch–Wigner pitch).
- [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md) — Δ_λ gate, six ansätze, 2026-05-29 retraction.
- [`docs/lambda-scale-absorbed-into-vol-density.md`](../lambda-scale-absorbed-into-vol-density.md) — why `m = m_e · VolDensity(K, q_0)` is single-eval; no separate `m_0`.
- [`docs/precision-goals.md`](../precision-goals.md) — L1 / L2 precision targets the Δ_λ closure would help reach.
- [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md) — substrate → archimedean pipeline; KLR layer would sit between Hecke and Wedderburn.
- AGENTS.md §7b — Symmetric-crystal techniques (KLR / Kashiwara) authoring guidance.
- AGENTS.md §3b-cond — conditional-on-class exception for conjecture axiomatisation.
- `computations/binding_K_direct.py` — Δ_λ-gated binding formula.
- `computations/lp_dual_solver.py` — current LP/SDP infrastructure the dialog's "speedup" pitch would replace.
