# GAP-A-3 / GAP-A-4 feasibility assessment (scoping)

**Date:** 2026-05-31
**Branch:** `claude/gap-a3-a4-feasibility-2026-05-31`
**PR:** [#1591](https://github.com/litlfred/qou/pull/1591)
**Audience:** any agent picking up the Δ_λ-gated per-isotope binding problem
**Verdict (short):** **Both GAP-A-3 and GAP-A-4 reduce to Δ_λ.** Neither has a
parameter-free path that is independent of the open Δ_λ(K) determination — the
gating audit's warning ("requires a per-partition selector = Δ_λ itself") is
**confirmed against the actual probe witnesses**, with the precise circularity
located below. No genuinely structural (representation-theoretic) rule was found
that escapes the reduction. This is reported as the honest blocker, **not**
papered over with a fit.

This document scopes the two productive non-fit directions named in
[`docs/audits/2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md)
§"What needs to happen for Δ_λ closure" item 1, and in
[`docs/audits/2026-05-09-gap-a-3-a-4-guidance.md`](2026-05-09-gap-a-3-a-4-guidance.md).

---

## 1. Precise statements of the two GAPs

### GAP-A-3 — brane-tower level selector `n_⋆(K)`

Source: `conj:brane-level-selection`, `rem:mass-endomorphism-jet-tower`, and
the guidance doc §"GAP-A-3".

The mass tower is *a priori* an infinite sum over jet levels:

$$
  \mathfrak{m}(K) \;=\; \bigl|\textstyle\prod V^{(0)}\bigr|
  \;+\; \sum_{n=0}^{\infty}\bigl[\,\Sigma_1^{(n)} + z^2\,\Sigma_2^{(n)}\,\bigr].
$$

For a *confined* particle the physical mass should depend on only **finitely
many** levels — the tower "saturates" at some `n_⋆(K)`. **GAP-A-3 asks for an
explicit categorical formula for `n_⋆(K)`.** A correct `n_⋆` rule must be a
representation-theoretic / topological invariant of `K` (GS Coxeter length,
SDP rank, JSJ depth, active-block count, …), **not** a value picked to match the
binding energy.

### GAP-A-4 — per-block structural prefactor `ρ`

Source: [`conj:rho-prefactor-structural`](../../content/quantum-observable-universe/mass-theory/conj-rho-prefactor-structural.md),
guidance doc §"GAP-A-4", and the derivation-audit.

The mass formula carries an overall scalar `ρ(𝔥) ∈ ℤ_{>0}`:

$$
  B(\mathfrak{H}) \;=\; m_e \cdot \rho(\mathfrak{H}) \cdot M(\mathfrak{H})\big|_{q=q_0}.
$$

Currently `ρ` is a per-atom by-product of the Wedderburn SDP search:
`ρ_p = ρ_n = ρ_D = 1`, `ρ_T = ρ_{³He} = 2`. The conjecture proposes
`ρ(𝔥) = dim_q(λ*(T_w))` (round-to-nearest), where `λ*` is the dominant
Wedderburn block (the `λ` maximising `|y_λ(q₀)·χ^λ(T_w)|`). **GAP-A-4 asks for
a structural derivation of `ρ` from categorical data** — no per-atom re-tuning.

### Why the two GAPs are intertwined (the gating audit's coupling claim)

Per the guidance doc §"Joint GAP-A-3 + GAP-A-4 attack" and the gating context
audit, `n_⋆(K)` and `ρ(K)` are *multiplicative prefactors on the truncated
tower*:

$$
  \rho(K)\,\Bigl|\,\textstyle\sum_{n=0}^{n_\star}\,\text{level-}n\,\Bigr|
  \;=\; M(K)/m_e .
$$

Both sit on the *same* underdetermined equation that defines Δ_λ. The §2–§3
verifications below show that each GAP's "structural fix", when followed to its
endpoint, lands on the per-partition `Δ_λ(K)` profile.

---

## 2. What scaffold already exists (survey 2026-05-31)

The Δ_λ / ρ / brane-tower problem is **heavily scaffolded** already — this is
not a green field. Inventory of `computations/`:

| Component | File(s) | State |
|---|---|---|
| Δ_λ canonical formula | [`rho-k-h3a-refinement.md/.lean`](../../content/quantum-observable-universe/mass-theory/rho-k-h3a-refinement.md) | ✓ defined; `class RhoKH3ARefinement` axiomatises the identity |
| GAP-A-4 conjecture block | [`conj-rho-prefactor-structural.md/.lean/.ts`](../../content/quantum-observable-universe/mass-theory/conj-rho-prefactor-structural.md) | ✓ stated; Lean `class` with the `|ρ − dim_q(λ*)| ≤ 1/2` field |
| GAP-A-4 verifier | `rho_prefactor_structural_verifier.py` + `rho-prefactor-structural-verifier.witness.json` | ✓ **falsifies** simple form (§3.2) |
| Δ_λ closure-attempt scripts | `rho_k_h3a_{lp_dual,co_casimir,frobenius_pairing,crystal,wenzl_bridge,gg_trajectory}.py` | ✓ all six+ ansätze implemented |
| Δ_λ probe witnesses (~20) | `delta-lambda-*.witness.json` | ✓ empirical-tabulation, bar-invariance, 2-row-stratum, JSJ-phase3, etc. |
| Option E (crystal weight) probes | `option_e_{deuteron,multi_isotope}_delta_lambda_probe*.py` + 3 witnesses | ✓ latest direct attack (§3.1) |
| Brane-tower (GAP-A-3) scripts | `canonical_brane_tower.py`, `brane_tower_isospin_diagnosis.py`, `brane_tower_two_avenues_probe.py`, `proton_brane_tower_correction_probe.py` | ✓ tower assembled; n_⋆ rule **not** present |
| n_⋆ scalar-rule refutation | (PR #638, `conj:brane-tower-z-habiro` closed by refutation) | ✓ no single scalar n_⋆ works |
| Option E Lean scaffolding | `lusztig-canonical-basis-q-eq-1.lean`, `kashiwara-jones-c4-categorical.lean`, `crystal-basis-resolves-mass-tower-open-problems.lean` | ✓ stubs (research-grade) |

**What is missing** (the genuine open items): (a) an `n_⋆(K)` formula that is a
categorical invariant; (b) a `ρ(K)` rule that distinguishes Markov-equivalent
braids; (c) the crystal-vertex trace `ρ_w(K)` that Option E needs. All three,
as shown in §3, are the Δ_λ(K) determination wearing different hats.

---

## 3. Feasibility verdict per GAP (verified against witnesses)

### 3.1 GAP-A-3 — reduces to Δ_λ. **No parameter-free path.**

**Refutation of the scalar `n_⋆` rule (established, PR #638).** No single
integer `n_⋆(K)` reproduces the binding across the light isotopes. The gating
audit records this: the structural alternative to a scalar `n_⋆` is a
*per-partition* selector — i.e. a different truncation/weight per Wedderburn
block λ ⊢ 3A — which is **exactly the content of Δ_λ(K)**.

**The brane-tower pathology (verified, `brane-tower-isospin-diagnosis.witness.json`).**
The assembled tower is not merely "missing a level rule"; it is numerically
pathological at q₀. Verdict field from the witness:

> "Brane-tower Σ Φ_q(|V̂_i|) is the pathology source. The formula faithfully
> reproduces |V̂_i| from the Wedderburn construction, but Φ_q's divergence near
> x=1 amplifies small p/n asymmetries by 10⁵×. Not a software bug — a feature
> of the formula as stated."

So even with a level selector, the tower's Φ_q amplifies per-generator
p/n asymmetries (the predicted T − ³He isospin splitting comes out −737 MeV vs
CODATA +0.019 MeV). A level rule does not fix this; the cure lives in the
per-block structure (Δ_λ), or in a different (non-tower) route entirely.

**Verdict GAP-A-3:** The only candidate that survives the scalar-rule
refutation is a per-partition truncation/weight = Δ_λ(K). **GAP-A-3 ⊆ Δ_λ.**
No representation-theoretic single-number invariant (GS length, SDP rank, JSJ
depth) was found that closes the binding without per-block tuning. **Circular.**

### 3.2 GAP-A-4 — reduces to Δ_λ. **No parameter-free path.** (Strongest result.)

This is the cleanest, most quantitative reduction, traced to
`rho-prefactor-structural-verifier.witness.json` (`allPassed: True`,
`scriptFile: rho_prefactor_structural_verifier.py`).

**The braid-strand-count impossibility theorem (verified).** At the braid
strand count `H_3`, the canonical operators for **proton, neutron, and ³He are
Markov-equivalent** — their braid words are mutual inverses, so their per-λ
character profiles are *bit-for-bit identical*. From the witness
`per_atom_analysis` (dominant λ* and the per-block (χ, y_λ) for each atom):

| atom | dominant λ* | χ^{[2,1]} | y_wenzl | \|y·χ\| | observed ρ |
|------|-------------|-----------|---------|--------|-----------|
| proton  | [2,1] | 1.994185810381214 | 0.2809296339798641 | 0.560220… | **1** |
| neutron | [2,1] | 1.994185810381214 | 0.2809296339798641 | 0.560220… | **1** |
| ³He     | [2,1] | 1.994185810381214 | 0.2809296339798641 | 0.560220… | **2** |
| ²H (6₂) | [3]   | 1.232052482588431 | 0.4153957863345666 | 0.511789… | **1** |

proton/neutron/³He share **every** (χ_λ, y_λ) value yet split ρ ∈ {1, 1, 2}.
The verifier's `summary.verdict`:

> "0 of 5 candidate rules reproduce ρ for all 4 atoms… Atoms in the falsifying
> subset are Markov-equivalent at the braid strand count yet have distinct ρ —
> **no (chi, y)-only rule can distinguish them.**"

Five candidate rules (`exact dim_q`, `round dim_q`, `floor dim_q`,
`hook-special-case`, `classical d_λ`) all fail. This is a *theorem*, not a
failed fit: any function of the H_3-level character data is constant across
{p, n, ³He}, so it cannot produce a non-constant ρ.

**The proposed "structural fix" is Δ_λ in disguise (the circularity).** The
verifier's `structural_finding` says ρ must instead be read off the dominant
λ* ⊢ 3·A of the **binding operator** `K` in the atomic decomposition

$$
  T_w(\mathfrak{H}) \;=\; \underbrace{K(\mathfrak{H})}_{\in\,H_{3A}(q_0)}
  \cdot \bigotimes_{i=1}^{A} T_w(\text{nucleon}_i).
$$

But `K(𝔥)`'s per-block Wedderburn decomposition over `λ ⊢ 3A` — the very thing
that would carry the ρ information — **is** the object `Δ_λ(K)`. To know
`λ*(K)` (hence ρ) you must know `K`'s block content; determining `K`'s block
content from substrate + constituents is the open Δ_λ(K) problem. The conjecture
block's own "Closure path via the canonical-knot-id" confirms this: GAP-A-4
"closes *as a corollary* of GAP-A-1" once the canonical `T_w` (= the binding
operator at H_{3A}) is uniquely fixed — and the SDP that fixes `T_w` is the same
underdetermined system that defines Δ_λ.

**Verdict GAP-A-4:** **GAP-A-4 ⊆ Δ_λ ∪ GAP-A-1.** The H_3-level form is *proved*
impossible; the H_{3A} form requires the binding operator `K`, whose per-block
profile is Δ_λ(K). **Circular** with respect to Δ_λ (and additionally gated on
GAP-A-1 canonical-knot identification).

### 3.3 Option E (crystal weight) — the most promising non-fit candidate — does not (yet) escape

Option E proposes `Δ_λ(K) = Σ_w n^w_λ · ρ_w(K)` (KL multiplicities × canonical-
basis trace at crystal vertices). It is *structurally motivated* (not a fit) and
is the framework's preferred research direction. **But it is not yet a parameter-
free closure**, and the latest probe data confirms it has not closed:

From `option-e-multi-isotope-delta-lambda-probe-v3.witness.json`
(`leading_order_rule: content_sum_negated`, the best *substrate-only* rule):

| atom | B_pred (MeV) | B_target (MeV) | rel error |
|------|-------------|----------------|-----------|
| D    | −1.838 | 2.225 | 17.4 % (sign also wrong) |
| T    | −1.113 | 8.482 | 86.9 % |
| ³He  | −2.112 | 7.718 | 73.0 % |

The v3 probe then tested five **per-knot offset corrections** "derived from
substrate data (no AME fitting)". The `best_offset` (`minus_dim_max_over_A`)
still gives `max_rel_error 53.99 %`, `uniform_closure_10pct: false`. One offset
(`negated_tr_M_inverse`) happens to hit D to 5.6 % — but it is a tr_M-derived
algebraic term, not a binding derivation, and it does **not** close T or ³He.
The pattern is the recurring one: an offset that accidentally lands one atom
fails the others, because there is no single structural rule — the residual is
genuinely per-(λ, K). **Option E remains open** (its `ρ_w(K)` crystal trace is
itself unimplemented — see the Option E audit's "Crystal vertex weights ρ_w:
NOT EXIST"), and until `ρ_w(K)` is derived it cannot be distinguished from a
per-block fit. It is the right place to keep pushing, but it is **not** a closure
today.

---

## 4. The precise circularity (one paragraph)

The atomic mass formula
`ρ_K = ρ_K^LO + (1/|tr_M(𝓑_K)|) Σ_{λ⊢3A} y_λ χ^λ(𝓑_K) Δ_λ(K)`
gives, per atom K, **one** equation (the known binding `B(K) = m_e·Σ y_λ χ^λ Δ_λ`)
in **p(3A)** unknowns `{Δ_λ(K)}` (p(6)=11 for D, p(9)=30 for T/³He, p(12)=77 for
⁴He). It is wildly underdetermined. GAP-A-3 ("which levels / how to truncate")
and GAP-A-4 ("the overall ρ prefactor") are both attempts to supply the missing
structural constraint *without* solving for Δ_λ. The witnesses show each attempt
collapses back:

- GAP-A-3's scalar `n_⋆` is refuted; its surviving per-partition form *is* the
  Δ_λ weight profile.
- GAP-A-4's `f(χ_λ, y_λ)` form is *proved* unable to distinguish Markov-
  equivalent atoms (p/³He identical at H_3, ρ ∈ {1,2}); its surviving H_{3A}
  form needs the binding operator K whose block content *is* Δ_λ(K).

So both GAPs are restatements of "determine the per-partition Δ_λ(K)", which is
the open R&D. **There is no shortcut through A-3 or A-4 that does not pass
through Δ_λ.** This is the gating audit's warning, now verified.

---

## 5. Did any genuinely structural rule emerge? No (and why no probe was authored)

Per the task's discipline gate: a probe witness is warranted **only** if a
genuinely parameter-free structural rule appears. None did. Every candidate
examined either:

1. is refuted (scalar n_⋆; the 5 ρ-rules; the 6 prior Δ_λ ansätze);
2. is proved impossible at the relevant strand count (any `f(χ, y)` at H_3); or
3. requires an object (binding operator K / crystal trace ρ_w(K)) that is itself
   the Δ_λ determination.

Authoring a new probe that picks Δ_λ to match `B_AME` would be the **7th fit**
the Δ_λ gate forbids — and would be caught by the production-vs-exploratory
discipline review. **So no probe script / witness is shipped on this branch.**
The deliverable is this honest blocker assessment.

---

## 6. Where the genuinely non-fit effort should go (forward, not this branch)

Neither A-3 nor A-4 is independently closable; the productive non-circular work
is **upstream of both**:

1. **GAP-A-1 (canonical-knot identification) first.** GAP-A-4's own closure path
   says ρ "closes as a corollary of GAP-A-1" — once the canonical binding
   operator `T_w(K) ∈ H_{3A}` is *uniquely fixed by the R5-full SDP from
   substrate + constituents alone* (no AME), its dominant λ* is determined and ρ
   follows. The open piece is the SDP "binding-K solver mode" that finds `K`
   without fitting. This is the single highest-leverage item: it would
   simultaneously give `K` (⇒ ρ via A-4) and `K`'s block profile (⇒ Δ_λ).

2. **Option E crystal trace `ρ_w(K)` derivation.** Implement the canonical-basis
   trace at crystal vertices (currently "NOT EXIST" per the Option E audit) so
   `Δ_λ(K) = Σ_w n^w_λ ρ_w(K)` becomes *computable* and therefore *falsifiable*
   as a structural identity rather than a fit. This is the framework's preferred
   direction and is genuinely parameter-free *if* ρ_w is derived from KLR /
   Lecouvey structure (not chosen to match B_AME).

3. **Independent route: bypass Δ_λ via Path B (Borromean tower extension).** The
   gating audit's Path D→Path B swap removes the Δ_λ gate entirely at the cost of
   opening the per-atom λ(K) substrate-derivation. The cheat-sheet's A≥3 campaign
   (per-rep q-Reeb phase, μ₀ = m_e/(3(q−q⁻¹)/2) derived) already closes the A=3
   mirror pair to 2 % and B_D to −9 % with **0 free params** — a non-Δ_λ route
   worth comparing head-to-head with the Δ_λ approach.

None of (1)–(3) is "add a 7th Δ_λ ansatz". All three attack the structural
upstream that A-3 and A-4 silently presuppose.

---

## 7. Cross-references

- [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md) — the gate (this doc verifies its item-1 warning)
- [`docs/audits/2026-05-09-gap-a-3-a-4-guidance.md`](2026-05-09-gap-a-3-a-4-guidance.md) — original GAP attack plan
- [`docs/audits/2026-05-25-option-e-crystal-weight-delta-lambda.md`](2026-05-25-option-e-crystal-weight-delta-lambda.md) — Option E scaffolding
- [`docs/audits/2026-05-25-delta-lambda-K-dependence-reframing.md`](2026-05-25-delta-lambda-K-dependence-reframing.md) — Δ_λ(K) is canonical; ⛔ no global Δ_λ
- [`content/quantum-observable-universe/mass-theory/conj-rho-prefactor-structural.md`](../../content/quantum-observable-universe/mass-theory/conj-rho-prefactor-structural.md) — GAP-A-4 conjecture
- [`content/quantum-observable-universe/mass-theory/rho-k-h3a-refinement.md`](../../content/quantum-observable-universe/mass-theory/rho-k-h3a-refinement.md) — Δ_λ formal definition
- `computations/rho-prefactor-structural-verifier.witness.json` — GAP-A-4 H_3-impossibility (the §3.2 data)
- `computations/option-e-multi-isotope-delta-lambda-probe-v3.witness.json` — Option E §3.3 data
- `computations/brane-tower-isospin-diagnosis.witness.json` — GAP-A-3 Φ_q pathology (§3.1)
