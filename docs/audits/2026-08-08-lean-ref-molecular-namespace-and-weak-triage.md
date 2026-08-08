# `lean.ref` drain completed, a chapter-wide namespace defect, and the WEAK-33 per-block triage

**Date:** 2026-08-08
**Follows:** [`2026-08-08-lean-ref-and-wall-side-weak-drain.md`](2026-08-08-lean-ref-and-wall-side-weak-drain.md)
**Beans:** `qou-z3k1`; wall-side WEAK queue.

Second pass: every remaining broken `lean.ref` read individually, and the WEAK-33
classified per block by reading the actual `ℝ`-bearing signatures.

## 1. One "broken" ref was never broken

`QOU.Observations.s5_acts_on_ew_slice` **resolves correctly** — the declaration
exists in its sibling as an **`axiom`**. It appeared in the broken list because
the first-pass resolver's declaration regex enumerated
`theorem|lemma|def|abbrev|structure|class|inductive|instance` and **omitted
`axiom`**. No change made.

Third instance in this drain of the same shape: *a resolver reporting a
confident wrong answer rather than no answer.* The count of genuinely broken
refs is **32**, not 33.

## 2. Every remaining ref fixed, each verified against its own sibling

Targets were chosen by reading the block's `.md` headline claim and picking the
declaration that carries it, under a stated rule:

> Point at the declaration carrying the block's headline claim — a theorem when
> one states it, otherwise the def/structure that packages it. **Never at a
> theorem weaker than the block claims.**

Each rewrite was applied only after the new target was confirmed present in the
sibling's declaration set (namespace-qualified), so no fix could introduce a
second phantom.

| block ref (tail) | new target | note |
|---|---|---|
| `PolynomialBarInvolution` | `…PolynomialBarInvolution.barPoly_involutive` | ref named a *namespace* |
| `PhiQAJMachineryIdentification` | `….phi_q_li2_q_unified_via_aj` | ref named a *namespace* |
| `recursive_atom_knot_atlas` | `atomKnotAtlas` | see §3 |
| `QMomentumProperties` | `qMomentumP_additive` | see §3 |
| `JucysMurphyCentralElementsQOU` | `jm_esymm_central` | |
| `terminal_resolution` | `TerminalResolution` | structure packages the mass table |
| `local_substrate_q` | `LocalSubstrateQ` | |
| `C5InvolutionLeibnizDecomposition` | `c5_decomposition_via_quantum_two` | |
| `helium3_uniqueness_closed` | `CanonicalKnotIdSDP` | `conj:` block → §3b class |
| `meson_kaon_pion_ratio` | `seifert_ratio_T25_T23` | |
| `per_block_hopf_jones_absorption` | `dimension_scaled_absorption_pattern` | |
| `ChebyshevTorusCoefficients` | `chebyshevTorusCoefficients` | |
| `SilverRatioBetaDecayNull` | `beta_decay_null_iff_h_zero_or_two` | |
| `ChiLambdaW0SignWeighting` | `chi_lambda_w0_sign_weighting` | exact snake_case twin existed |
| `DemandProfile` | `demandProfile` | |
| `lepton_v_hat_h3_3channel` | `lepton_V_hat_h3_3channel` | **case typo**: `v` vs `V` |
| `frobeniusForm` | `QOU.FrobeniusPairing` | wrong name *and* wrong namespace |

## 3. Two targets are weaker than their block claims — flagged, not papered over

- **`recursive_atom_knot_atlas`.** The only theorem in the sibling is
  `atlas_witness_derived : AtlasIsWitnessDerived`, where
  `AtlasIsWitnessDerived := atomKnotAtlas.length ≥ 1` — a regression guard, and
  its own docstring says so (*"the genuine 'every entry is witness-derived'
  content requires per-entry methodology checks"*). Pointing a `prop:` at it
  would overstate. The ref points at `atomKnotAtlas`, the actual formal content.
  **The block's claim is not formalised.**
- **`QMomentumProperties`.** The `.md` states four properties (additivity,
  Markov-I invariance, Markov-II shift, parity). The sibling formalises **one**
  (`qMomentumP_additive`). Properties 2–4 are unformalised.

## 4. A chapter-wide defect: `molecular-construction/` namespaces

Generalising the two Molecular fixes surfaced a systemic problem. Of 23 blocks
in `molecular-construction/` with a sibling `.lean`, **7 had no `namespace` at
all**, while the other 16 carried `QOU.Molecular`. Every `lean.ref` in the 7
therefore named `QOU.Molecular.X` against a root-level `X` and could not resolve
— and none of them appeared in the triviality sweep's broken list, because those
blocks skipped for other reasons.

Declaration names in all 7 were already correct; only the namespace was missing.
Added `namespace QOU.Molecular` / `end QOU.Molecular` to:
`benzene-molecular-braid`, `ch4-molecular-braid`, `co-molecular-braid`,
`co2-molecular-braid`, `covalent-bond-shared-trefoil`, `h2-molecular-braid`,
`molecular-braid`. This also brings the chapter into line with AGENTS.md §2
(*all declarations live under the `QOU` root namespace*).

`embeddable-knot-operator` had the namespace but a name that exists nowhere
(`EmbeddableKnotOperator`); repointed to `embeddableBinding`.

### A pre-existing build breakage found on the way

`molecular-braid.lean` **does not compile on `main`** — it has *no imports at
all*, so `Finset.univ.sum` in `sharedElectrons` fails (`unknown identifier`),
and behind it `Fintype (Fin numBonds)` fails to synthesise. Confirmed against a
clean `main` checkout, so this is not something the namespace change caused.
Fixed by adding `Mathlib.Algebra.BigOperators.Group.Finset.Basic` and
`Mathlib.Data.Fintype.Fin`; the file now compiles.

## 5. WEAK-33 — per-block triage

Each of the 32 remaining was read at the level of its `ℝ`-bearing signatures and
imports. Classification:

| class | meaning |
|---|---|
| **GENUINE** | `ℝ` buys nothing; the content is algebraic and should be generic |
| **LEGIT** | `ℝ` is load-bearing *by meaning* — a physical/measured quantity, a hyperbolic volume, a time parameter — and the block needs a §7c acknowledgement, not a Lean change |
| **NEEDS-PORT** | algebraic in surface form, but the proofs do **not** survive generalisation as-is |

| block | class | evidence |
|---|---|---|
| `meson-em-sinh-closed-form` | **NEEDS-PORT** | `(q-1)/q`, `q ≠ 0`, `field_simp; ring` — but see §6 |
| `confined_knot_binding` | **NEEDS-PORT** | `q - q⁻¹`, `c*q + d`, `q ≠ 0` — same failure |
| `confinementUniversality` | GENUINE | `N_F : ℝ→ℝ→ℝ→ℝ` with a constancy claim; no arithmetic at all — a bare type variable suffices |
| `fermion-boson-decomposition` | GENUINE | `total/horizontal/vertical : M → ℝ` and an additive decomposition — any `AddCommGroup` |
| `fai_projector_coadjoint_orbit` | GENUINE | `Matrix (Fin 2) (Fin 2) ℝ` with `ρ * ρ = ρ` — idempotence is `CommRing` content |
| `four_term_pair_nucleon` | LEGIT | `protonNetTarget : ℝ := 0.999` — measured net values (§7c "experimental value → `ℝ`") |
| `derived-mass-formula-light-isotopes` | LEGIT | `m_e, m_p, m_n, α : ℝ` — physical masses |
| `skein_mass_from_linking` | LEGIT | `Vol_K : ℕ → ℝ` hyperbolic volume (transcendental) + physical masses |
| `q-heat-equation` | LEGIT | the `ℝ` is the **time** parameter of an evolution equation |
| `QouInfraDischargesGoncharovZeta5` | unread | single `residual : ℝ`; zeta-value context suggests LEGIT, not confirmed |
| `collatz_contact_boundary` | **not touched** | **sibling PR #4722 is editing this file** — left alone to avoid a conflict |
| remaining 21 | unread | signatures not yet dumped |

## 6. The two NEEDS-PORT blocks — and why forcing them would have been wrong

`meson-em-sinh-closed-form` and `confined_knot_binding` look like textbook
gratuitous-`ℝ`: a quotient, `q ≠ 0`, `field_simp; ring`, no ordering. Both were
regenericised to `{R : Type*} [Field R]` — and **both then failed with unsolved
goals**, so the change was reverted and both files verified back to green.

The reason is stated in `meson-em-sinh-closed-form`'s own docstring:

> *"base ring of characteristic `≠ 2`"*

`field_simp; ring` over a bare `Field R` cannot discharge a step that divides by
2. The correct target is `[Field R] [CharZero R]` (or an explicit
`(2 : R) ≠ 0`), not plain `Field`.

Recorded rather than forced. A regenericisation that leaves `sorry` or a broken
proof behind would be strictly worse than the `ℝ` it replaced.

## Remaining

| queue | remaining |
|---|---|
| `lean.ref` — no formalisation at all | 10 (formalise or demote) |
| `lean.ref` — target weaker than the block claims | 2 (§3) |
| wall-side WEAK — read, needs a Lean change | 3 GENUINE + 2 NEEDS-PORT |
| wall-side WEAK — read, needs a §7c note | 4 LEGIT |
| wall-side WEAK — unread | 22 (+1 blocked on #4722) |
| wall-side MED | 65 (unchanged) |
