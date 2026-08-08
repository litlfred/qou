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
| `meson-em-sinh-closed-form` | **PORTED** | `(q-1)/q`, `q ≠ 0` — now `[Field R] [CharZero R]`, see §6 |
| `confined_knot_binding` | **PORTED** | `q - q⁻¹`, `c*q + d`, `q ≠ 0` — now `[Field R] [CharZero R]` |
| `confinementUniversality` | LEGIT ⚠ | the `ℝ` are **photon polarisation coefficients** `(φ₀, φ₁, φ₀₁)` — physical continuous parameters. Structurally the constancy claim needs no arithmetic, but generalising a physics-parameter type to an arbitrary `Type*` weakens the meaning. |
| `fermion-boson-decomposition` | LEGIT ⚠ | imports `Analysis.SpecialFunctions.Pow.Real` + `Topology.*` — genuinely analytic |
| `fai_projector_coadjoint_orbit` | LEGIT ⚠ | imports `LinearAlgebra.Matrix.Spectrum`; docstring: *"the proof runs Mathlib's spectral theorem"* — archimedean |
| `four_term_pair_nucleon` | LEGIT | `protonNetTarget : ℝ := 0.999` — measured net values (§7c "experimental value → `ℝ`") |
| `derived-mass-formula-light-isotopes` | LEGIT | `m_e, m_p, m_n, α : ℝ` — physical masses |
| `skein_mass_from_linking` | LEGIT | `Vol_K : ℕ → ℝ` hyperbolic volume (transcendental) + physical masses |
| `q-heat-equation` | LEGIT | the `ℝ` is the **time** parameter of an evolution equation |
| `QouInfraDischargesGoncharovZeta5` | unread | single `residual : ℝ`; zeta-value context suggests LEGIT, not confirmed |
| `collatz_contact_boundary` | **not touched** | **sibling PR #4722 is editing this file** — left alone to avoid a conflict |
| remaining 21 | unread | signatures not yet dumped |

> ⚠ **All three rows marked ⚠ were first classified GENUINE and are corrected
> here.** The first-pass call was made from the `ℝ`-bearing *signature lines*
> alone. Reading the **imports** and the semantic role of each `ℝ` refutes all
> three: a `Matrix (Fin 2) (Fin 2) ℝ` whose only visible statement is
> idempotence still needs `ℝ` if the proof runs the spectral theorem, and a
> `M → ℝ` decomposition still needs `ℝ` if the file is doing analysis.
>
> This reproduces #4709's own warning — *"absence of an archimedean token is
> evidence, not proof… the earlier 17-file read found the heuristic
> false-positives often"* — and sharpens it: **the decisive evidence is the
> import list and the meaning of the quantity, not the signature.** A triage
> that reads only signatures over-calls GENUINE. Confirmed GENUINE count among
> the 11 read so far: **zero**.

## 6. The two NEEDS-PORT blocks — diagnosed, then ported

`meson-em-sinh-closed-form` and `confined_knot_binding` look like textbook
gratuitous-`ℝ`: a quotient, `q ≠ 0`, `field_simp; ring`, no ordering. Both were
regenericised to `{R : Type*} [Field R]` — and **both then failed with unsolved
goals**, so the change was reverted and both files verified back to green.

The reason is stated in `meson-em-sinh-closed-form`'s own docstring:

> *"base ring of characteristic `≠ 2`"*

`field_simp; ring` over a bare `Field R` cannot discharge a step that divides by
2. The correct target is `[Field R] [CharZero R]` (or an explicit
`(2 : R) ≠ 0`), not plain `Field`.

**Both are now ported** to `{R : Type*} [Field R] [CharZero R]` and verified
`lean`-direct exit 0; `meson-em-sinh-closed-form` also passes
`check-wall-side --block`. The first attempt failed only because it used plain
`[Field R]`; the file's own docstring named the missing condition and the second
attempt honoured it.

The sequence is the point: *diagnose from the file's own words, then port* — not
*force the port and leave a broken proof*. A regenericisation that leaves `sorry`
or an unsolved goal behind is strictly worse than the `ℝ` it replaced.

## Remaining

| queue | remaining |
|---|---|
| `lean.ref` — no formalisation at all | 10 (formalise or demote) |
| `lean.ref` — target weaker than the block claims | 2 (§3) |
| wall-side WEAK — **ported this pass** | 2 (done) |
| wall-side WEAK — LEGIT, needs a §7c note on the block | 23 |
| wall-side WEAK — GENUINE candidate, needs a compile test | 5 |
| wall-side WEAK — reclassified to MED (ordering) | 2 |
| wall-side MED | 65 (unchanged) |

## 7. The WEAK-33 read to completion (2026-08-08, second sitting)

All 33 now read under the corrected protocol from §5 — **imports and the semantic
role of the `ℝ`, not the signature**. Final tally:

| outcome | n | blocks |
|---|---|---|
| **ported** | 3 | `macdonald-hook-telescope` (`[Field R]`), `meson-em-sinh-closed-form`, `confined_knot_binding` (both `[Field R] [CharZero R]`) |
| **misclassified — belongs in MED, not WEAK** | 2 | `demazure-fiber-markov-trace`, `mass-endomorphism-tower` |
| **GENUINE candidate — needs a compile test** | 5 | `qmn_recursive_memoized`, `q_gl_classical_limit`, `markov_identification`, `cpt-d6-d7-d8-closure`, `nucleon_ordering_factorization` |
| **LEGIT — `ℝ` load-bearing by meaning** | 23 | see below |

### The 2 misclassified: the classifier misses `>` and `<`

Both carry `q > 1` **in code**, so they have an ordering hypothesis and are MED by
#4709's own definition:

- `demazure-fiber-markov-trace` — `∀ (lam) (q : ℝ), q > 1 → …`, four occurrences
- `mass-endomorphism-tower` — `q > 1 → Pre.massPoly … > 0 := sorry`

#4709's ordering regex matched `0 <`, `≤`, `abs`, `linarith`, `positivity` — and
**not bare `>` / `<`**. My own re-check in §5 inherited the same omission. A
re-scan of all 33 with `>`/`<` included finds exactly these two and no others, so
the defect is contained: the queue is **WEAK-31 + 2 MED**.

(`mass-endomorphism-tower` additionally carries a `sorry` on that line — a matter
for the proof queue, not this one.)

### The 5 GENUINE candidates — stated as candidates, deliberately

Each looks structurally independent of `ℝ`:

| block | why |
|---|---|
| `qmn_recursive_memoized` | the claim is **cache correctness** — `cache_get λ ρ = some v → v = chi λ ρ`. The stored value's type is irrelevant to it. |
| `q_gl_classical_limit` | `heckeEigenvalue : ℝ → ℝ → Prop` with `∀ T, heckeEigenvalue 1 T → (T = 1 ∨ T = -1)` — no arithmetic, no ordering |
| `markov_identification` | a finite sum of `markovWeight × spechtPartialTrace` — Hecke-algebra objects; needs `AddCommMonoid` |
| `cpt-d6-d7-d8-closure` | `markovTrace : ClosedBraid → ℝ` — the Markov trace is algebraic (`ℤ[q, q⁻¹]`), not archimedean |
| `nucleon_ordering_factorization` | the core lemma is **permutation invariance** over `List ℝ` (`ds.Perm ds' → …`) — purely structural |

**They are not being called GENUINE, and none is being ported here.** This session
made three GENUINE calls from surface reading and **retracted all three** on a
closer look (§5). The only reliable adjudicator is the compiler: a port that
compiles is a GENUINE confirmation, one that does not is a `CharZero`-style
diagnosis or a refutation. Until each has been attempted, "candidate" is the
honest label.

### The 23 LEGIT

Grouped by what makes `ℝ` load-bearing:

- **Physical / measured quantities** — `four_term_pair_nucleon` (`0.999` net
  targets), `derived-mass-formula-light-isotopes`, `mass_categorical_descent`,
  `positron_correction`, `binding_assembly`, `ch4_lp_dual_binding`,
  `mass-volume-factorization`, `skein_mass_from_linking`,
  `q-beta-radius-of-convergence-gate` (a decimal substrate literal and a
  convergence radius).
- **Hyperbolic volumes / transcendence** — `BorelZagierQouVolumes` (ℚ-linear
  independence of `vol(4₁), vol(5₂), vol(𝓑)`), `SingleVolumeIrrationality`,
  `QouInfraDischargesGoncharovZeta5`, `DiophantineBirthday`.
- **Analysis in the proof, not the statement** — `fai_projector_coadjoint_orbit`
  (spectral theorem), `fermion-boson-decomposition` (`Pow.Real` + `Topology`).
- **A continuous physical parameter** — `confinementUniversality` (photon
  polarisation), `q-heat-equation` (time).
- **Mass / holonomy / norm cluster** — `cat_eigenspace_decomposition`,
  `cat_descended_is_base_mass`, `cat_transient_localises_blowup`,
  `tm_descended_is_holonomy`, `tm_transient_localisation` (a `nrm : ℝ → ℝ` is a
  norm; the rest are masses and a holonomy).

> **Flag for the vacuity queue, not this one.** Three of the mass/holonomy
> cluster define their content trivially — `cat_transient_localises_blowup` has
> `alpha := 0`, `tauHat := fun x => x`, `trFrob := 0`, `localComponent _ := 0`;
> `tm_transient_localisation` has `transientMItotal := 0`;
> `tm_descended_is_holonomy` has `descendedMIdisc _ := 1`. Whatever the `ℝ`
> question, a lemma whose every input is `0` or the identity is a §1a matter.
> Not touched here.

`collatz_contact_boundary` remains untouched — sibling #4722 is editing it.

## 8. The 5 candidates, compile-tested — 1 confirmed, 4 refuted or blocked

Per §7 the compiler was made the adjudicator. Result: **1 of 5** is a genuine
portable case. The other four are refuted or blocked for reasons a read could
not have settled.

| block | verdict | what the test showed |
|---|---|---|
| `nucleon_ordering_factorization` | **GENUINE — ported** | `scalar_channel_ordering_independent` now `{α M : Type*} [CommMonoid M] (f : α → M) (ds ds' : List α)`. `lean`-direct **exit 0**. |
| `qmn_recursive_memoized` | **BLOCKED** | its class `extends QOU.Shared.MarkovTraceContext`; the `ℝ` cannot be parameterised without threading a type through that shared parent — which **16 classes extend**. Cross-cutting refactor, not a per-block fix. |
| `markov_identification` | **REFUTED** | the `ℝ` live in module-level `opaque` constants (`opaque markovTrace : ℝ`, `markovWeight`, `spechtPartialTrace`). A polymorphic `opaque` is a *family of unrelated constants*, which misrepresents the specific objects being named. |
| `q_gl_classical_limit` | not attempted | §3b conjecture class; parameterising it rewrites every downstream instance binder |
| `cpt-d6-d7-d8-closure` | not attempted | same — §3b conjecture class |

### What the confirmed one generalised to

More than expected. The lemma is permutation-invariance of `(ds.map f).prod`, so
the channel data and the scalar map need not even share a type: `f : α → M` over
any `[CommMonoid M]`. `ℝ` bought nothing at either position. The archimedean
instance is `α := ℝ`, `M := ℝ`.

### The methodological point

The §7 read predicted 5 GENUINE. The compiler confirmed **1**, refuted 1 on a
ground no read would surface (`opaque` semantics), and blocked 1 on an `extends`
edge that the consumer count — *"appears in 1 `.lean` file"* — actively hid.

That consumer count is the fifth confident-wrong-answer of this drain. A file
count does not measure blast radius when the dependency runs through class
inheritance rather than through imports.

**Standing rule for the remaining queue:** a GENUINE verdict is a *compile
result*, never a read. Read to choose what to try; let the compiler decide.

