# Exposition-drain needs_owner ledger (2026-07-12)

The exposition drain was a swarm sweep applying the Milnor H1–H8 exposition
gate (economy, concrete-before-abstract, why-before-what, uncluttered
notation, linear argument, prose-carries-argument, surgical cleanliness,
respect for the reader) plus the deterministic defect batteries
(lean-mention-in-prose, status/draft markers, proof-sketch-vs-kind,
render-battery) to every narrative `.md` block across all 34 chapters of
`content/quantum-observable-universe/`. It ran in two waves: July 4
(PRs #3301–#3326) and July 11–12 (PRs #3589–#3635). The swarm operated
under a strict do-not-touch-derivations mandate: no statement, equation,
hypothesis, derivation step, or numerical value could be edited. This
ledger consolidates every item the swarm flagged as `needs_owner`,
"flagged for owner", or "deliberately unchanged" — findings the swarm was
not authorized to fix — into one document for owner disposition.

Items already resolved between waves are excluded. In particular, PR
[#3626](https://github.com/litlfred/qou/pull/3626) (owner-approved math
fixes) closed four items flagged by #3614/#3615: the wrong Bring's-curve
defining equations in `fivefold-sheets-golden-ratio`, the Σ₄/𝓔_q mislabel
in `outro-brings-surface`, the three-way Markov-z definition collision,
and the `\{6 \text{points}\}` spacing defect.

File paths below are relative to `content/quantum-observable-universe/`
unless prefixed otherwise.

## 1. Mathematical errors / open math questions

| File | Defect | Source |
|---|---|---|
| `braids-and-knots/markov-axioms-primitive.md` (axiom 4) + `braids-and-knots/hecke-satisfies-blitvic-hypothesis-proof.md` | The corpus convention that both Markov stabilisations carry the same $z$ (axiom 4; the Blitvić proof's $\mathrm{tr}_M(\sigma_i^{-1}) = z$) is in tension with the Hecke quadratic relation, under which $\sigma_i^{-1} = \sigma_i - (q - q^{-1})$ gives $\mathrm{tr}_M(\sigma_i^{-1}) = z - (q - q^{-1}) \approx 0.290$ at $q_0$ — which is what the pyhecke NF reduction actually computes. Reconciling is a substantive math decision. | [#3626](https://github.com/litlfred/qou/pull/3626) |
| `appendix-surreals/hoefsmit-is-surreal-construction.md` + its proof block | Proposition states a "canonical injective embedding $\Phi$" while the proof block refers to "the bijection $\Phi$" — internal inconsistency inside the derivation. | [#3589](https://github.com/litlfred/qou/pull/3589) |
| `braids-and-knots/` (corpus-wide) | Residual $\tau_M$ occurrences: #3626 normalized $\tau_M \to \mathrm{tr}_M$ in `markov-axioms-primitive.md` only; a corpus sweep for remaining $\tau_M$ remnants was not performed. | [#3615](https://github.com/litlfred/qou/pull/3615), [#3626](https://github.com/litlfred/qou/pull/3626) |
| `appendix-transfer-matrices/tm-heavy-atom-examples.md` | Heavy, conjecture-dependent numbers ("conjectures C1–C3 need verification"); Q-value algorithm and worked numbers are derivation content the swarm could not restructure. | [#3307](https://github.com/litlfred/qou/pull/3307) |

## 2. Purged-symbol ghosts (λ_scale in display math)

The factor `λ_scale` was absorbed 2026-05-23 (standing purge, AGENTS.md).
Three display-math sites survive; display math was out of scope for the
swarm.

| File | Defect | Source |
|---|---|---|
| `mass-theory/reidemeister-mass-invariance.md` | Purged `λ_scale` appears in display math (the `m_bare` formula, ~line 30). | [#3631](https://github.com/litlfred/qou/pull/3631) |
| `particle-interactions/categorical-proton-properties.md` | Display math still carries `λ_scale`; owner's canonical replacement needed. | [#3627](https://github.com/litlfred/qou/pull/3627) (commit `f0dd212`) |
| `mass-theory/borromean-baryon-mass-formula.md` | `λ_scale` in the display-math mass formula and throughout the prose — the block *is* the common-scale hypothesis. Owner ruling needed: deprecation authorNote vs rewrite against the canonical-mass guardrail doc. | [#3634](https://github.com/litlfred/qou/pull/3634) |

(The prose-level `λ_scale` in `particle-interactions/borromean-reidemeister-intro.md` was removed in #3627.)

## 3. Proof-sketch-vs-kind (provable-kind blocks presenting sketches)

Provable kinds (`proof`, `proposition`) whose bodies present a sketch or a
pointer instead of a complete argument. Options per block: supply the full
argument, re-kind/demote, or accept the sketch label.

| File | Defect | Source |
|---|---|---|
| `q-geometric-langlands/hasse-weil-bound-proof.md` | `proof` kind; body opens "Proof sketch." and closes by appealing to "Weil's framework" without the Castelnuovo–Severi / Hodge-index details. | [#3613](https://github.com/litlfred/qou/pull/3613) |
| `braids-and-knots/figure-eight-reeb-rotation-proof.md` | `proof` kind labelled "Proof sketch." | [#3615](https://github.com/litlfred/qou/pull/3615) |
| `particle-interactions/confinement-frobenius-reciprocity.md` | Proposition carrying a `## Sketch of Proof`. | [#3627](https://github.com/litlfred/qou/pull/3627) |
| `mass-theory/` — 10 blocks: `markov-trace-frobenius-selection-proof`, `mass-categorical-descent-proof`, `pieri-photon-shift-proof`, `prop-rigid-monoidal-structural-gap-invariance-proof`, `q-beta-direction-sanity-gate-proof`, `q-beta-q-eq-one-shadow-gate-proof`, `q-beta-radius-of-convergence-gate-proof`, `residue-at-root-proof`, `wedderburn-mass-formula-proof` (kind `proof`, present "Proof sketch"); `vol-through-tau` (proposition with "**Sketch.**") | Complete arguments not verifiably present; not converted. | [#3631](https://github.com/litlfred/qou/pull/3631) |
| `mass-theory/q-bessel-c-k-recurrence-cfinite.md`, `mass-theory/q-bessel-second-order-qdifference.md` | One-sentence "proofs" that are Lean citations. | [#3631](https://github.com/litlfred/qou/pull/3631) |
| `mass-theory/t-beta-markov-frobenius-collapse-proof.md`, `mass-theory/t-beta-markov-frobenius-collapse-general-proof.md` | Proof bodies are pointers to Lean proofs; stripping the apparatus would empty them. | [#3631](https://github.com/litlfred/qou/pull/3631) |
| `appendix-transfer-matrices/tm-inductive-construction.md` | "Gröbner–Shirshov normal form (inductive proof)" section is proof content living in a `prose` block. | [#3307](https://github.com/litlfred/qou/pull/3307) |

## 4. Kind/banner mismatches

Blocks whose `.ts` kind and `.md` banner disagree (conjecture-kind blocks
titled Theorem/Proposition, or a remark carrying a Conjecture banner).
Changing the claim label was out of swarm scope.

| File | Defect | Source |
|---|---|---|
| `particle-interactions/hecke-anyonic-substrate.md` | Theorem/Proposition header on a conjecture-kind block. | [#3627](https://github.com/litlfred/qou/pull/3627) (commit `f0dd212`) |
| `particle-interactions/cpt-orbit-closure-density.md` | Theorem/Proposition header on a conjecture-kind block. | [#3627](https://github.com/litlfred/qou/pull/3627) (commit `f0dd212`) |
| `particle-interactions/geom-universality.md` | Theorem/Proposition header on a conjecture-kind block. | [#3627](https://github.com/litlfred/qou/pull/3627) (commit `f0dd212`) |
| `mass-theory/block-multiplicativity-v-free.md` | `.ts` kind is `remark` but the body opens "**Conjecture (…)**"; also carries a classical-limit proof sketch (fine for a conjecture, not for a remark). | [#3634](https://github.com/litlfred/qou/pull/3634) |
| `stochastic-mechanics/reverse-limit-q-to-infinity.md` | Kind is `conjecture` but the banner reads "**Theorem (…)**"; residual `## Open R&D` lists Lean-authoring tasks. | [#3325](https://github.com/litlfred/qou/pull/3325) |

## 5. Orphan `.md` without `.ts` manifest

Files outside the pipeline (no manifest sibling); not validated, not
rendered, not QA-swept. Owner call per file: integrate as a proper
`.ts + .md` triple, or remove.

| File | Defect | Source |
|---|---|---|
| `braids-and-knots/jsj-decomposition-linearity.md` | No `.ts` manifest; YAML frontmatter instead of a block manifest; Lean code fence pasted into prose; unhedged claims (JSJ volume additivity, "Vol ≈ 13.948" proton block, "$c \gg 1000$" scaling). The referenced `QOU/BraidsKnots/LinearJSJVolume.lean` does exist. | [#3615](https://github.com/litlfred/qou/pull/3615) |
| `information-theory/computational-spacetime-observer.md` | No `.ts` manifest; full embedded `lean` code fence plus heavy intensifiers; left untouched as non-pipeline content. | [#3603](https://github.com/litlfred/qou/pull/3603) |
| `mass-theory/active-set-trace-concentration.md` | No `.ts` sibling; excluded from the audit as an orphan. | [#3634](https://github.com/litlfred/qou/pull/3634) |
| `mass-theory/flavor-split-habiro-derivation.md` | No `.ts` sibling (a `.lean` sibling exists); excluded from the audit as an orphan. | [#3634](https://github.com/litlfred/qou/pull/3634) |

## 6. Notation-register collisions / drift

| File | Defect | Source |
|---|---|---|
| `appendix-knot-operations/hecke-operations.md` vs `appendix-transfer-matrices/tm-knot-pairs.md` | The Hecke amplitude $q - q^{-1}$ is denoted "HA" (acronym, glossed as $h$) in one appendix and "$H_A$" in the other; neither form is in the notation register (which restricts the $H_q$ family). One symbol should be canonized. **Resolved 2026-07-12** (`claude/ledger-s6-notation-2026-07-12`): canonized $h_{\mathrm{A}}$ — 33 blocks swept, register row added to Table 3, collision note added; the algebra $H_A(q)$ (with argument) and the compute-layer witness keys are unchanged. | [#3316](https://github.com/litlfred/qou/pull/3316), [#3307](https://github.com/litlfred/qou/pull/3307) |
| `quantum-observable-universes/observation-physical-roles.md` | Bare $E$ used for "the field", colliding with the register rule "$E$ alone = not used"; fix requires choosing a register-compliant symbol. **Resolved 2026-07-12** (`claude/ledger-s6-notation-2026-07-12`): the field is a local section of the state bundle — replaced with $\mathcal{S}$, the register's replacement for the deprecated old-tuple $E$. | [#3629](https://github.com/litlfred/qou/pull/3629) |
| `quantum-observable-universes/complex-substrate-interpretation.md`, `weight-decomposition-su2.md`, `spin-half-representation.md`, `reeb-u1-chart-swap.md`, `reeb-u1-five-roles.md` | $\varTheta$ used as a torus/phase angle while the register reserves $\varTheta$ for the contact form; corpus-wide rename decision. **Proposed resolution (2026-07-12):** rename the torus/phase-angle uses to $\vartheta$ (script lowercase theta; $q = \lvert q\rvert e^{i\vartheta}$, $\rho_\vartheta$), which is visually an angle, unclaimed in the register, and near-unused in the corpus (4 existing $\vartheta$ occurrences vs 141 bare $\theta$); blast radius is exactly the 16 occurrences in these 5 files (the other 373 $\varTheta$ occurrences across 132 files are the contact form and stay). | [#3629](https://github.com/litlfred/qou/pull/3629) |
| `quantum-observable-universes/spectral-chart-correspondence.md` vs `q-laplacian-spectral-tower.md` | $\kappa$ as chart-transition coordinate collides with $\kappa$ as root-of-unity order. **Proposed resolution (2026-07-12):** keep $\kappa$ for the chart-transition gluing scalar ($z\,w = \kappa = q^{-1}$ — the more entrenched use: `spectral-chart-correspondence`, `affine-chart-origin-of-i-and-q`, `substrate-parameter-su2`, `canonical-action-obstruction`, `complex-substrate-interpretation`, ~5 files) and rename the root-of-unity order to $r$ ($q = e^{i\pi/r}$, $\mathbb{Q}(\zeta_r)$ — standard in the quantum-topology literature, and $r$ was freed for generic contexts by the 2026-06-04 $\check{q}$ rename); blast radius 5 occurrences in 2 files (`q-laplacian-spectral-tower`, `q-laplacian-consumers`). | [#3629](https://github.com/litlfred/qou/pull/3629) |
| `particle-interactions/hadron-proton-example.md` vs the confinement blocks | 0- vs 1-indexed braid-generator convention split between blocks in the same chapter. **Proposed resolution (2026-07-12):** canonize the 0-indexed convention $\sigma_0, \ldots, \sigma_{n-2}$ (the chapter majority — 46 `particle-interactions` blocks use $\sigma_0$, matching the compute layer) and re-index the 5 one-indexed blocks (`hadron-proton-example` — $(\sigma_1^{-1}\sigma_2)^3 \to (\sigma_0^{-1}\sigma_1)^3$ — plus `box-braid-irreducibility`(+`-proof`), `ew-slot-far-commutation-obstruction`, `lepton-meson-parallel`), with a register row recording the convention; the math is index-shift invariant, but each of the 5 blocks' displays and any `.lean`/witness siblings keyed to generator indices must be re-checked, hence not swept mechanically here. | [#3627](https://github.com/litlfred/qou/pull/3627) (commit `f0dd212`) |
| `glossary/glossary-hom-set.md` | Cites the Mathlib hom type as `CategoryTheory.Category.Hom X Y`; the actual Mathlib declaration is `Quiver.Hom` (`Category` extends `CategoryStruct` extends `Quiver`). **Resolved 2026-07-12** (`claude/ledger-s6-notation-2026-07-12`): citation corrected to `Quiver.Hom X Y` with the extends-chain and the `⟶` notation, verified against the pinned Mathlib source. | drain triage (not recorded in a fetched PR body) |
| `braids-and-knots/` and downstream | $\tau_M$ vs $\mathrm{tr}_M$ remnants — see the sweep item in §1. | [#3615](https://github.com/litlfred/qou/pull/3615), [#3626](https://github.com/litlfred/qou/pull/3626) |

## 7. Step-count / internal-consistency errors

| File | Defect | Source |
|---|---|---|
| `particle-interactions/derived-atom.md` | Announces 5 steps; the text has 6. | [#3627](https://github.com/litlfred/qou/pull/3627) (commit `f0dd212`) |
| `particle-interactions/o16-derived-nf.md` | Announces 5 steps; the text has 4. | [#3627](https://github.com/litlfred/qou/pull/3627) (commit `f0dd212`) |
| `particle-interactions/nucleon-nf-observability.md` | Announces "four"; the text has three. | [#3627](https://github.com/litlfred/qou/pull/3627) (commit `f0dd212`) |
| `quantum-observable-universes/categorical-q-ext-deriv-exists.md` | A "**Strategy.**" proof-scaffold paragraph and the fragment sentence "Uniqueness is ([link])." sit inside the proposition statement block; moving them to the proof sibling is restructuring. | [#3629](https://github.com/litlfred/qou/pull/3629) |
| `mass-theory/three-halves-structural-factor.md` | `## Lean` section contains a garbled sentence ("canonical cross-checks at exact representation exact algebraic structures verify…") mixed with witness links. | [#3631](https://github.com/litlfred/qou/pull/3631) |
| `quantum-observable-universes/q-resolvent-properties.md` | $t$ appears unbound in the defining display $R_q(s) = \mathrm{tr}_M(\exp_q(-s\,\cdot)\cdot\exp(-t\,\widehat{\Delta_q}))$ — the left side does not depend on $t$ and no integral/limit binds it. | drain triage (not recorded in a fetched PR body) |
| `appendix-qvalues/qvalue-benchmark-table.md` (line 45) | `$\deltaQ$` is an undefined LaTeX macro (should be `\delta Q` / `\delta\mathcal{Q}`, cf. line 50); render-breaker inside the error-propagation derivation note. | [#3306](https://github.com/litlfred/qou/pull/3306) |
| `stochastic-mechanics/q-beta-gamma-gamma-canonical-derivation.md` | Broken possessive references — "tracking through 's selection theorem" / "(Track C per  plan)" with the name missing; cannot be fixed without inventing the referent. Also "Following the user's direction" process voice. | [#3325](https://github.com/litlfred/qou/pull/3325) |
| `brings-surface/approach-to-exceptional-divisor.md` | Stray cross-ref fragment "(Picard--Lefschetz thimble §setup)". | [#3614](https://github.com/litlfred/qou/pull/3614) |
| `appendix-qvalues/im-complex-volume-intro.md`; `introduction/chapter-overview.md`; `mass-endomorphism/markov-trace-axiomatic-closed-form-table2-data.md`, `rho-k-graded-expansion-table2-data.md` | Pre-existing `\operatorname{Re}`/`\operatorname{Im}` (or `\operatorname` in `*-data.md` tables) inside math the swarm did not author; KaTeX render-gate concern. | [#3306](https://github.com/litlfred/qou/pull/3306), [#3318](https://github.com/litlfred/qou/pull/3318), [#3635](https://github.com/litlfred/qou/pull/3635) |

## 8. authorNotes migrations / apparatus entangled with content

Blocks where Lean/status apparatus is interwoven with load-bearing content
(conjecture-class axiomatisation per §3b, honesty gaps, tracker metadata),
so a strip would remove substance. Owner dispositions: §4d `authorNotes`
migration, retitle/partial strip, or accept as intentional apparatus
content.

### Whole-block / structural decisions

| File | Defect | Source |
|---|---|---|
| `predicted-spectra/cl2-pentagon-and-faddeev-partial.md` | The entire block is a formalization-status report (boundary-case Lean theorems, §3b-cond scaffolding); gutting the apparatus would remove the subject matter — whole-block re-scope decision. | [#3604](https://github.com/litlfred/qou/pull/3604) |
| `quantum-observable-universes/g-action-on-substrate.md` | `### Audit impact` section is work-tracking register in scholarly prose but anchors `#tbl:g-action-on-substrate-table3-data`; removal would orphan the table. | [#3629](https://github.com/litlfred/qou/pull/3629) |
| `quantum-observable-universes/categorical-reeb.md` vs `categorical-reeb-derivation.md` | Two definition blocks both defining "categorical Reeb derivation" with different characterisations (T-action generator vs Frobenius–Hopf normalization + Leibniz); consolidation is a technical decision. | [#3629](https://github.com/litlfred/qou/pull/3629) |
| `organic-chemistry/ring-closure-superstability.md` | Opening paragraph verbatim-duplicates `ring-closure-barrier.md` (lines 50–57, the braid-word claim $\sigma_i^2 \to (\sigma_1\cdots\sigma_{N-1})^2$); the duplicate carries a mathematical statement, so removal was not authorized. | [#3317](https://github.com/litlfred/qou/pull/3317) |
| `brings-surface/inter-nucleon-channel-color-tube.md`, `c-from-color-flavor-swap.md` | Tracker-shaped conjectures: "Lean axiomatisation (sketch)" sections, PR/skill-file/line-number references, "Open R&D" / "promote to proposition" workflow prose. Candidate for authorNotes/`.ts` migration but load-bearing for the canonical-watcher/duality-tracker workflow. | [#3614](https://github.com/litlfred/qou/pull/3614) |
| `brings-surface/brings-surface-orphan-reconnect-intro.md` | Entire block is a Phase-7 orphan-audit draft marker; rewrite or remove. | [#3614](https://github.com/litlfred/qou/pull/3614) |
| `introduction/authors-note.md` | Front-matter formalization-coverage stats (Lean/sorry/Mathlib mentions) kept as deliberate disclosure; owner may prefer migrating the stats elsewhere. | [#3318](https://github.com/litlfred/qou/pull/3318) |

### PR-number tables and branch-pinned links

| File | Defect | Source |
|---|---|---|
| `mass-theory/bring-residue-resolvent.md` | Consumer table keyed by PR numbers (`#1444/#1445/#1455`); removal would restructure the table. Also a §3b-cond `## Lean structure` section. | [#3634](https://github.com/litlfred/qou/pull/3634) |
| `mass-theory/binding-alpha-shift-extension.md` | `open (#1485)` table cell + §3b-cond `## Lean structure` section. | [#3634](https://github.com/litlfred/qou/pull/3634) |
| `mass-theory/a8-partition-function-identity.md` | Branch-pinned blob URLs (`claude/qbeta-habiro-followup-2026-06-01`) in cross-refs. | [#3634](https://github.com/litlfred/qou/pull/3634) |

### Lean-in-proof-body / lean-mention entangled with argument

| File | Defect | Source |
|---|---|---|
| `appendix-surreals/kashaev-surreal.md`, `spectral-normal-form.md`, `os-reflection-positivity-from-reeb.md`, `q-collatz-interpretation.md`, `hoefsmit-is-surreal-construction-proof.md`, `surreal-appendix-conclusion.md`, `bigbang-heatdeath.md` | Lean-in-prose inside conjecture proof-strategy / proof bodies where the formalizability discussion is arguably scholarly content in a speculative appendix. | [#3589](https://github.com/litlfred/qou/pull/3589) |
| `appendix-surreals-archimedean/diophantine-birthday.md` | "Required infrastructure" / "Provability assessment" prose names Lean/mathlib explicitly, woven into the conjecture's proof strategy. | [#3323](https://github.com/litlfred/qou/pull/3323) |
| `molecular-construction/ice-pauling-residual-proof.md`, `h2o-bond-angle-shift-proof.md`, `symmetric-block-domain-weight.md` | Lean mentions carry the exact-over-ℚ / over-ℝ rigor boundary as content inside proof bodies. | [#3592](https://github.com/litlfred/qou/pull/3592) |
| `predicted-spectra/type-b-folded-crystal-combinatorics.md`, `gram-kappa-spectral-interpretation.md`, `em-coupling-*` blocks | Lean mentions entangled with substantive content (table pointer, base-ring specialization, §3b-cond conditional-theorem banners, κ-caveats). | [#3604](https://github.com/litlfred/qou/pull/3604) |
| `braids-and-knots/jones-markov-trace-formalization-note.md`, `bar-involution-grading-lean-proofs.md`, `braid-link-types.md`, `markov-trace-inductive-limit.md`, `figure-eight-reeb-novelty-note.md`, `pion-half-figure-eight-formalization-note.md` | Lean-centric remarks whose subject is the formalization; §4d authorNotes-migration candidates. | [#3615](https://github.com/litlfred/qou/pull/3615) |
| `climax-volume-mass/selection-rule-anchors-c1-c3.md`, `selection-rule-c2-prediction.md`, `coulomb-strong-ratio-q-rational-proof.md` | `## Lean proof structure` / `## Proof (Lean-formalised)` sections whose bodies are the algebraic derivation; Lean framing cannot be stripped without risking proof content. | [#3324](https://github.com/litlfred/qou/pull/3324) |
| `stochastic-mechanics/lusztig-canonical-basis-q-eq-1.md` | `## Open R&D` items name "in Lean" / "Lean class"; apparatus-heavy conjecture-R&D content. | [#3325](https://github.com/litlfred/qou/pull/3325) |
| `stochastic-mechanics/F3-eps6-leading-eq-neg-2b-cubed.md` | Heavy lean-mention (tactic names, "no sorrys", "Lean stub") plus a `## Proof` derivation body. | [#3325](https://github.com/litlfred/qou/pull/3325) |
| `stochastic-mechanics/markov-closure-map-axiomatic.md` | `## Lean encoding` section describing class fields and "type axiom"; Track-C status framing throughout. | [#3325](https://github.com/litlfred/qou/pull/3325) |
| `mass-theory/meson-kaon-pion-hecke-seifert-proof.md` | `## Lean structure` section carries the honesty-gap table ($n_q = 2$ not derived) intertwined with apparatus; recommend authorNotes migration, not a prose strip. | [#3631](https://github.com/litlfred/qou/pull/3631) |
| `mass-theory/q-zero-complex-extension-proof.md` | Proof argues via AGENTS.md §7c and Lean-file typing (apparatus woven into the argument). | [#3631](https://github.com/litlfred/qou/pull/3631) |
| `mass-theory/prolonged-periods-fixed-depth-proof.md` | Mathlib lemma names (`mul_smul_comm`, `map_sum`, `map_smul`) woven into derivation prose. | [#3631](https://github.com/litlfred/qou/pull/3631) |
| `mass-theory/poincare-lefschetz-borromean.md` | Prose links an agent skill file (`.claude/skills/local/canonical-watcher.md` §Slot J) plus a `## Open R&D` Lean roadmap. | [#3631](https://github.com/litlfred/qou/pull/3631) |
| `mass-theory/lepton-mass-tower-canonical.md`, `q-beta-c3-continuum-geometry.md` | Resolution/CORRECTION banners in prose; §4d authorNotes migration is a `.ts` edit, out of scope for a prose-only pass. | [#3631](https://github.com/litlfred/qou/pull/3631) |
| `mass-theory/reeb-linking-cwf-normalization.md` | Process-voice honesty sentence ("axiomatization is not proof … production wiring") kept per anti-laundering; owner call on rewording. | [#3631](https://github.com/litlfred/qou/pull/3631) |
| `mass-theory/mass-tower-deeper-fillers.md`, `lp-duality-hypothesis-class.md`, `topological-mass-formula.md`, `ck-extraction-from-algebraic-rules.md` | Blocks whose subject is Mathlib/Lean scaffolding (or a Lean pointer mid-derivation); flagged for possible relocation. | [#3631](https://github.com/litlfred/qou/pull/3631), [#3634](https://github.com/litlfred/qou/pull/3634) |
| `mass-theory/gs-*` (six conjecture blocks), `borromean-bloch-group-element.md` | §3b "Lean encoding / Conjectural status" mini-sections and a `## Lean axiomatisation (sketch)`; they document the conjecture-class axiomatisation per convention — migrating to authorNotes is a structural decision. | [#3634](https://github.com/litlfred/qou/pull/3634) |
| `mass-endomorphism/` — 13 clusters: `binding-qbeta-complex-volume`, `channel-rotation-askey-lit`, `whipple-rotation-intertwining`, `conj-qbeta-c-k-closed-forms`, `complex-volume-intro`, `chi-per-irrep-cyclotomic-closed-forms`, `chi-v111-via-sign-substitution`, `chi-v21-hoefsmit-matrix-derivation`, `chi-v3-closed-form-proof`, `qbeta-per-block-chi-closed-forms-proof`, `qbeta-delta-tau-surrogate-taylor-coefficients`, `qbeta-canonical-markov-weights-explicit-instance(-proof)`, `qbeta-delta-tau-canonical-conditional-q2-minus-1-factor-proof`, `tau-M-asymptotic-rep-theory-proof`, `u-coordinate-discharges`, `multi-link-jones-q1-extension`, `hecke-algebra-type-scaffold`, `markov-trace-operator-construction`, `conj-rho-k-pair-gen-canonical-form`, `color-spacetime-s5-factorization` | Lean/sorry apparatus in prose that sits in or feeds the binding-qbeta / Askey–Wilson conditional-class cluster (hot zone at drain time); several blocks' entire content documents the Lean class scaffold — stripping would gut them. | [#3635](https://github.com/litlfred/qou/pull/3635) |
| `appendix-qvalues/proton-mass-substrate-identity.md` | `## Open work for full categorical proof`, `## Sub-ppm precision frontier`, and tier/do-not-wire caveats read as status apparatus but are intertwined scholarly caveats about the derivation's epistemic state. | [#3306](https://github.com/litlfred/qou/pull/3306) |
| `information-theory/gas-constant-derivation.md` | Intensifier-laden prose woven into a live derivation body ($R_q$ displays); untouchable without risking the derivation. | [#3603](https://github.com/litlfred/qou/pull/3603) |

## Disposition guide

Sections 5, 6, and 7 are mostly quick mechanical fixes: the four orphan
`.md` files need an integrate-or-remove call and then ~30 minutes each of
manifest work; the notation items need one symbol decision each (the
$\varTheta$ rename is the only corpus-wide one); the step-count,
undefined-macro, and unbound-$t$ items are one-line edits once the intended
reading is confirmed. Section 2 is three targeted display-math edits, but
each requires the owner's canonical replacement for `λ_scale` (the
`borromean-baryon-mass-formula` block needs a scope ruling, not just an
edit). Section 4 is five one-word kind-or-banner decisions. Sections 1
and 3 are genuine math decisions: the Markov axiom-4 same-$z$ tension is
the highest-stakes item (it touches the trace axioms the pyhecke compute
implements), and each sketch-vs-kind block needs prove/demote/accept
adjudication. Section 8 is the long tail: mostly §4d authorNotes
migrations that require `.ts` edits and per-block judgment about what is
apparatus and what is load-bearing content; none is urgent, all are
approvable in batches.
