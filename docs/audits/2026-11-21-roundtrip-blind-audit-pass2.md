# Round-trip blind audit, pass 2 (2026-11-21)

Bean epic `qou-ncxf`. Owner ruling on the PR #8819 follow-up (2026-11-21):
run pass 2 on the next 20 blocks, restore the honest `sorry` in
`confinement_categorical`, and restate the nine pass-1 disclosed blocks to
what their Lean proves. This document records all three.

## 1. Method

Sampler: `scripts/roundtrip-blind-sample.py 20 --offset 15`. Population 419
eligible provable blocks (statement `.md`, a proof block with a non-empty
`.md`, a `qou:` `lean.ref` naming a theorem/lemma that is not `: True` and
contains no `sorry`). Order: sha256(label). Pass 1 consumed the first 15.
Five labels in the window were skipped as `decl-not-found` and the sampler
moved on:

- `prop:borromean-hopf-energy-crossover`
- `prop:frobenius-pairing-exists`
- `prop:unified-curvature-rank-mass-formula`
- `prop:hadron-half-life`
- `prop:q-rogers-pentagon-archimedean`

A `decl-not-found` lean.ref is itself a finding for the ref audit of
PR #8819; it is not re-litigated here.

Four blind legs, each by a separate agent that saw only its own input:

| leg | input | output |
|---|---|---|
| RT-1 A | Lean statement, comments stripped, decl renamed `thm` | English statement |
| RT-2 B | Lean proof term | narrative of the proof, and where its content lives |
| RT-3 A | `.md` proof only | inferred statement |
| RT-3 B | `.md` statement only | proof obligations and flags |

Adjudication against the real blocks is mine and is **not** blind.
Every Class-A or narrative finding below that is called "verified" was
checked by me against the file named; the rest are agent findings recorded
as such.

### Packet limitations (fixed or noted)

- **Statement split.** The sampler cut the Lean statement at the first
  `:=`, which for C05, C13 and C14 fell inside a `haveI :=` / `let :=` in
  the statement, so RT-1 A saw a truncated statement. Fixed in this PR: the
  cut now skips a `:=` preceded on its line by `let` / `have` / `haveI` /
  `letI`.
- **Renaming in context.** Renaming the target to `thm` also rewrote
  structure field names in the context (`claim_thm`, `thm_axiom`). RT-2 B
  reported "name mismatch" for C09 and C12 on that basis; those two
  findings are packet artifacts and are discarded.
- **Dotted names / empty context.** C01 and C03 needed hand patching
  (dotted theorem name not renamed; structure context empty).

## 2. Results

Classes: **A** the Lean conclusion is assumed (a hypothesis or class field is
returned); **T** the Lean is a tautology / `rfl` on a definition; **B** the
Lean is weaker than the `.md` claim; **C** the narrative proof does not prove
the statement; **E** an empirical value inside a formal result.

| # | label | Lean | narrative / statement |
|---|---|---|---|
| C01 | `prop:q-heat-equation-unique` | genuine | C (minor): assumes semisimplicity; statement leaves Δ_q, the space and the notion of solution implicit |
| C02 | `prop:x5-z5-automorphism` | genuine | minor: primitivity of ζ₅ unstated |
| C03 | `prop:atom-knot-unique` | **T** (structure ext) | C: treats the Hecke quadratic relation as Reidemeister II, an isotopy it is not; equal Hecke images do not give isotopic closures |
| C04 | `prop:pieri-photon-shift` | **A** (field `support_subset`) | C: misses the a = n case and the third induced component; tower levels mixed. Uses the correct photon σ_aσ_b⁻¹ |
| C05 | `prop:confinement-categorical` | **A** (field `confinement_ident`) → **fixed: honest `sorry`** | statement undefined objects (filtration, "colored") |
| C06 | `lem:qou-exists-axiom-2` | **A** (hom_dim from two fields, 1 − 1 = 0) | standard Schur fact |
| C07 | `prop:p-bandwidth-bound` | **A** (iff from two fields) | ill-posed: P is a property of a family, not one link; Planck-time cost in the claim |
| C08 | `prop:binding-error-amplification` | genuine | minor: label `M_atom` reused for nuclear mass; garbled corollary sentence |
| C09 | `prop:frobenius-relation` | **A** (field `claim_frobenius_relation`) | **C, verified**: pairs a map A⊗A → A⊗A with a single test element c ∈ A, and equates μ(b₁⊗b₂) terms with no argument. Also conflicts with C10 if the pairing is the Markov trace (degenerate on H_n, n ≥ 3) |
| C10 | `prop:markov-trace-frobenius-selection` | genuine (derivation from moment equations) | (ii) stated for all n, proved at n = 3, numerical for n ≤ 7 |
| C11 | `prop:alpha-shift-torus-knot` | **T** (`rfl` on `alphaShift = k(p−1)`; class unused) | α(T_{p,k}) presented as a knot invariant but defined from one braid; T_{p,k} ≅ T_{k,p} gives k(p−1) vs p(k−1) |
| C12 | `prop:wigner-coefficient-derivation` | **A + E, verified**: discharged by `axiom wigner_coefficient_axiom` stating \|[5]_q!·m_e − 68.896\|/68.896 < 0.03 at `q₀ = 1.109978595554181` | E: an empirical 3 % bound inside a formal result, at the retired CODATA-2018 muon pin; the narrative calls 68.9 fitted. "Term 9" of a "seven-term" formula |
| C13 | `prop:positive-definite-dagger` | **B (weaker), corrected 2026-11-21**: the Lean checks only the scalar case z•1 on ℂ², f†f = \|z\|²·1; an earlier version of this table said "genuine" | **C, verified**: "non-degeneracy forces ⟨f,f⟩ ≠ 0" is false (isotropic vectors); "pivotal ⇒ S² = id" is not general; ⟨f,f⟩ = s² is asserted, not shown; positivity of ∫_A is not a hypothesis |
| C14 | `thm:gauge-conformal-invariance` | genuine but trivial cancellation | statement vacuous with α unconstrained; physics prose |
| C15 | `prop:cell-depth-truncation` | genuine | item 4 rests on unformalised Kazhdan–Lusztig facts, as stated |
| C16 | `prop:genus-maximal-descent` | conjunct 2 **A** (projects hypothesis `hhurwitz`); conjunct 1 arithmetic | "maximal genus consistent with the Hurwitz bound" is meaningless (the bound holds for every g ≥ 2; Bring's curve has 120 automorphisms, not 252) |
| C17 | `prop:skew-poisson-integration` | **A** (three claim fields) | "skewed-Poisson" undefined; Frobenius relation vs bialgebra compatibility conflated |
| C18 | `lem:mi-sw-abelianisation-cartan` | **A** (four fields + ext) | H, E± span sl₂(ℂ), not su(2); a gauge-dependent A⁰ equated with λ_SW |
| C19 | `prop:h3-frobenius-casimir-markov-trace` | genuine | clean. **An agent report that item 4 writes [3]!/[3] as 1/[2] instead of [2] is wrong**: item 4 is a sum of 1/dim_q, and dim_q(2,1) = [3]!/[3] = [2], so 1/[2] is correct; 1 + 1/[2] = (q²+q+1)/(q²+1) checks |
| C20 | `lem:bring-cone-reeb-quaternionic-twist` | genuine (ring identities) | **An agent report of a sign error is wrong**: the `.md` defines [M_x,M_y] := M_y∘M_x − M_x∘M_y, the same order as the Lean, and (p·i)·j − (p·j)·i = 2·(p·k). Remaining flags: "Reeb flow is the geodesic flow" vs the Boothby–Wang fibre rotation; degree of α∧(dα)ⁿ; singular cone vertex |

Tally: Class A in 9 of 20 (C04, C05, C06, C07, C09, C12, C16 partial, C17,
C18), tautology in 2 (C03, C11), genuine Lean in 9 (C01, C02, C08, C10, C13,
C14, C15, C19, C20). Pass 1 found Class A in roughly the same proportion.

### Old-premise check (the owner's 2026-11-21 instruction)

Only **C12** rests on a superseded input: the retired CODATA-2018 muon pin
`1.109978595554181` and a fitted 68.896 MeV. C04's narrative uses the
current photon form σ₀σ₁⁻¹. No block in this window uses the old σ₀σ₁
photon, the trefoil electron as primary, or T(2,n_s).

## 3. Restatements (owner ruling: "Restate to what Lean proves")

Each `.md` statement now says only what its `lean.ref` theorem proves, and
each `.ts` caveat note opens with "Statement restated 2026-11-21 …".

| block | bean | new statement (summary) |
|---|---|---|
| `prop:unstable-atom-decay-channel` | `qou-ni0g` | off the boundary variety and given the LP-duality selection input: minimisers coincide; IVT crossing for continuous E. Existence of λ* not claimed |
| `prop:su2-emergence-dagger-unitarity` | `qou-1iit` | a 2×2 matrix preserving the standard Hermitian product lies in U(2); the categorical identification is a stated hypothesis |
| `prop:mobius-energy-frobenius-kernel` | `qou-n3xv` | given the Hodge-star and Killing-form reductions as hypotheses, K_FH → 1/r² |
| `prop:golden-quartet-galois` | `qou-k9tf` | root set of x⁴ − 3x² + 1, φ·(1/φ) = 1, √5 ↦ −√5 substitutions; orbit/action facts named as informal |
| `prop:alpha-em-shift-multiplicative-chain` | `qou-tdhw` | the index identity [α_shift(T_{2,9}), α_shift(T_{3,5})] = [9, 10]; α_EM left to `prop:em-coupling-projection` |
| `prop:crossed-module-euler-characteristic` | `qou-zxuy` | the Borromean quaternion h² trace is −12 by finite computation over ℤ[i]; the match with dim V·χ(Σ₄) is recorded, not derived |
| `prop:staircase-corner-hook` | `qou-pwo1` | for ρ_k = (k,…,1), arm = leg = k − 1, so the corner hook is 2k − 1 |
| `prop:c5-involution-leibniz-decomposition` | `qou-xxa9` | defines c₅^dec = −b² − 1/2 and proves c₅^dec = −3/2 + 1/[2]_q²; not identified with the ladder rung c₅ |
| `prop:confinement-categorical` | `qou-mtc9` | statement unchanged; the Lean now states it with an honest `sorry` (field `confinement_ident` deleted a second time) |

The beans stay open: each restatement narrows a claim to what is proved and
leaves the original, stronger claim unproved.

## 4. Verification of this PR

- Render-QA grep battery on the eight edited math `.md` files: balanced
  `$`, `$$` and braces; no `+`/`-`/`*` list-hijack line inside a `$$` block.
  The pipeline render was not run.
- `c5` identity checked by hand: b² = (q⁴+q²+1)/(q²+1)² = 1 − q²/(q²+1)²,
  and b²(1+√2) = (21+14√2)/(24+16√2) = 7/8.
- `confinement_categorical.lean`: lean-direct and `#print axioms` result is
  recorded in the PR body (expected `sorryAx`).
- `.qa.json` sidecars of the edited blocks will show source-hash drift;
  `qa-sweep` does not load at the pinned platform (bean `qou-4jhp`).

## 5. New findings to bean

- C12: an `axiom` carrying a numeric empirical bound at a retired pin.
- C09, C13: narrative proofs that do not prove the statement.
- C03, C11: tautological Lean behind a substantive-sounding statement.
- C04, C06, C07, C16, C17, C18: Class A projections.
- Sampler: five `decl-not-found` refs in the window.

## 6. Fixes applied (owner instruction 2026-11-21: "Fix the issues that you found")

Every Lean change below was checked with lean-direct
(`-DautoImplicit=false -s 65536`) and `#print axioms`; `lake build` was not used.

| ID | Block | Lean | Narrative / manifest |
|---|---|---|---|
| C01 | `prop:q-heat-equation-unique` | unchanged (proves only that `dt_u` is determined by `dq_u`; `.ts` caveat says so) | statement made explicit: algebraic direct sum of finite-dimensional Δ_q-stable pieces, componentwise solutions; proof by `exp(tΔ)π_j u(t)` constant, no semisimplicity |
| C02 | `prop:x5-z5-automorphism` | unchanged | primitivity of ζ₅ stated; order checked at the point (2, √31); inverse φ₅⁴ and extension to the projective model |
| C03 | `prop:atom-knot-unique` | unchanged (structure ext; `.ts` caveat) | restated: same Hecke image gives the same Markov trace; isotopy not claimed (mutants) |
| C04 | `prop:pieri-photon-shift` | field `support_subset` deleted; `sorry` + `-- Ref:` (axioms: `sorryAx`) | split by tower level; three-row component (λ₁, λ₂, 1) added and shown to vanish on V^⊗(n+1); case a = n excluded; proof via central idempotents and branching |
| C06 | `lem:qou-exists-axiom-2` | field `total_hom_dim_eq` deleted; `sorry` (axioms: `sorryAx`) | proof of the sl₂ adjoint statement by Schur; the O_q(G) Peter–Weyl reading recorded as failing (one invariant per dominant weight) |
| C07 | `prop:p-bandwidth-bound` | unchanged: hypothesis-carried iff, §3b-cond item 5 pattern | `.ts` caveat |
| C08 | `prop:binding-error-amplification` | unchanged | `M_bound` for the nuclear mass; corollary now states mass precision ε·B/M_bound (B/M_bound = 0.12 % to 0.76 % for ²H to ⁴He) |
| C09 | `prop:frobenius-relation` | field `claim_frobenius_relation` deleted; `sorry` (axioms: `sorryAx`) | proof rewritten through the copairing; the relation reduces to associativity (Kock 2004 §2.3) |
| C11 | `prop:alpha-shift-torus-knot` | unchanged (`rfl`; `.ts` caveat) | α_shift defined on the braid β_{p,k}; maximality only for the six checked pairs; T_{p,k} ≅ T_{k,p} gives different values |
| C12 | `prop:wigner-coefficient-derivation` | `axiom wigner_coefficient_axiom` deleted; theorem now proves only the product expansion of [5]_q!·m_e (no sorry) | 67.1 vs 68.9 numbers removed from the proof; the false header Σ dim_q² = [n]_q! corrected |
| C13 | `prop:positive-definite-dagger` | unchanged (scalar check; `.ts` caveat) | S² = id and positivity of h(f, g) = ∫μ(S(f)⊗g) are now hypotheses; isotropic counterexample x₁y₂ + x₂y₁ recorded |
| C16 | `prop:genus-maximal-descent` | conjunct 2 now derived from Hurwitz at g = 4 (no sorry) | "maximal genus" sentence replaced: the bound holds for all g ≥ 2; Bring's curve has S₅, order 120 |
| C17 | `prop:skew-poisson-integration` | three claim fields deleted; `sorry` (axioms: `sorryAx`) | `.ts` caveat ("skewed-Poisson" undefined) |
| C18 | `lem:mi-sw-abelianisation-cartan` | unchanged: §3b-cond item 5 pattern | su(2) → sl₂(ℂ) = su(2)⊗ℂ; gauge dependence of A⁰ stated; two list-hijack `+` lines inside `$$` fixed |
| C20 | `lem:bring-cone-reeb-quaternionic-twist` | unchanged | Boothby–Wang Reeb flow (fibre rotation) separated from the Liouville Reeb flow (geodesic); qc condition stated on the rank-4n kernel; cone is a manifold only away from its vertex |

Not changed: C10, C14, C15, C19 (no defect needing a fix, or the scope is
already stated).

**New finding while fixing C17.** The sibling content block
`models-of-qous/skew-poisson-integration.lean` carries vacuous Bool-flag
fields (`reduction_ok : reduction_holds = true`, `strong_mult_ok`): the class
stores the flag and the proof reads it back. Same defect family as Class A,
not fixed here.

Render QA: grep battery (balanced `$`/`$$`/braces, `\bigl`/`\bigr`,
`\begin`/`\end`, no list-hijack line inside `$$`) clean on all 29 edited
content `.md` files. The pipeline render was not run.

**QA response (review on #8888, 2026-11-21).** Four major findings, all
addressed:

| finding | fix |
|---|---|
| The C04, C05 and C06 `sorry`s cannot be closed as stated: the class fields (`oneBoxShift`, `support_after`; `pi_centre`, `observable`, `integral`, `e_block`, `E_infinity_00`; the free ℕ `total_hom_dim`) are unconstrained, so a counterexample instance exists | each docstring now says so and names the strengthening the class needs (q-Pieri plus Young-lattice data; Hochschild/centre data; the sl₂ adjoint module). The classes are not strengthened here: Mathlib lacks the machinery |
| C09: the content sibling `quantum-universes/frobenius-relation.lean` still proved the relation by projecting a field, and `lean.ref` resolution picks the sibling first | sibling deleted (no consumers); the ref now resolves to `lean/QOU/frobenius_relation.lean` (`sorry`); stale `leanSource` dropped from the `.jsonld` |
| The Wigner 2026-10-11 author note still said the axiom discharges the theorem | note now says it did until 2026-11-21, when the axiom was deleted |
| C16: the `.md` said tr(id) = −6 determines χ(M₀), while both Leans take χ = −6 as input | `.md` states the identification as a hypothesis; the sibling's module, structure and `genus_unique` docstrings no longer claim "maximal" (lean-direct exit 0, axioms `propext, Classical.choice, Quot.sound`) |

**QA follow-up (review comment 7065408011).** Same shadowing defect for C06:
the content sibling `quantum-observable-universes/qou-exists-axiom-2.lean`
proved only that a fibre functor exists (`⟨Q.fibreFunctor⟩`), and `lean.ref`
resolved to it, which hid the library `sorry`. Sibling deleted (no consumers);
stale `leanSource` dropped from the `.jsonld`.

**QA follow-up 2 (2026-11-21).** The `lean.ref` resolver picks a sibling
`.lean` by path alone, so two more siblings shadowed library `sorry`s:

- `mass-theory/confinement-categorical.lean` (decls `confinement_survives_only_centre`,
  `not_int_factors_through_centre_unconstrained`, `int_factors_through_centre_of_invariant`)
  moved unchanged to `lean/QOU/WedderburnMass/ConfinementCentreProjection.lean`
  (lean-direct exit 0; axioms `propext, Classical.choice, Quot.sound`).
- `models-of-qous/skew-poisson-integration.lean` deleted: no consumers, only
  the Bool-flag structures noted above and lemmas of the form `d * d = d ^ 2`.

C06 now has a real proof. `exists_axiom_2_observability` states, over a
field with `2 ≠ 0`, that the adjoint module of `𝔰𝔩₂` has trivial invariant
submodule (`maxTrivSubmodule = ⊥`, i.e. `Hom(𝟙, V₁) = 0`); sorry-free, axioms
`propext, Classical.choice, Quot.sound`. The generic-`q` step for
`U_q(𝔰𝔩₂)` is cited. `2 ≠ 0` is needed: in characteristic 2 the identity is
traceless and central.

Still open on C09 (frobenius-relation): `compute-prop-has-probe` and
`compute-prop-has-consumer` fail because the checker passes sorry-free Lean
outright, and otherwise asks for a probe or for the I1 audit witness at
`folio-assistant/computations/i1-no-probe-audit.witness.json`, which the
light platform does not carry (the qou copy predates the `content/` →
`folio/` rename). An algebraic identity has no numerical prediction; the
honest fix is a sorry-free proof, which needs the pairing/copairing axioms
the context class lacks.

**C09 closed (2026-11-21).** `QOU.frobenius_relation` is now sorry-free
(axioms `propext, Quot.sound`). The context class of bare types is replaced by
`FrobeniusCopairingData`: an `R`-algebra `A` with form `ε`, copairing `γ` and
the snake identity. `Δ_μ := (μ ⊗ id) ∘ (id ⊗ γ)`, and the theorem states
`(μ ⊗ id) ∘ (id ⊗ Δ_μ) = Δ_μ ∘ μ` as linear maps `A ⊗ A → A ⊗ A`, proved by
associativity. That `Δ_μ` is the transpose of `μ` under the pairing is cited
(Kock 2004, §2.3), not formalised. This replaces the open note above on the
frobenius compute checks, which pass sorry-free Lean.

**C13 (positive-definite-dagger), full proof (owner: "Prove all three fully").**
`QOU.frobenius_dagger_positive_definite` now works over an `R`-algebra with
Frobenius form `ε` and an involutive unital anti-homomorphism `S`
(`FrobeniusAntipodeData`). Over an ordered field, assuming `h(f, g) = ε(S(f) g)`
is positive definite, it proves: the adjoint formula `h(x a, b) = h(a, S(x) b)`,
uniqueness of that adjoint, `S` fixing the scalars, and `f† ∘ f > 0` for
`f ≠ 0`. lean-direct exit 0, axioms `propext, Classical.choice, Quot.sound`.
The scalar `ℂ²` check is gone. A root-namespace duplicate of the old scalar
theorem survives in `lean/QOU/scratch_matrix.lean` (not imported by `QOU.lean`).
