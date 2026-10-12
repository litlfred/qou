# Milnor-voice exposition audit — Chapters 1 and 2 (2026-10-10)

**What this is.** An `expo-milnor-clarity` audit (the eight Milnor hallmarks H1–H8 of `.claude/skills/local/one-voice-style-guide.md` §"The Milnor exposition standard", scored 0–2 each by the rubric of `docs/requirements/2026-07-04-folio-assistant-proof-narrative-checkers.md` §5A) of every content block in Part I Chapter 1 (`folio/quantum-observable-universe/quantum-universes/`) and Chapter 2 (`folio/quantum-observable-universe/quantum-observable-universes/`). **No block prose was edited** (owner rule: ask before changing things); every non-pass verdict carries a suggested rewrite for the owner to accept or reject.

**Scope note — the introduction was not audited.** The paper manifest (`quantum-observable-universe.ts`) lists `introduction` as front matter, ahead of Part I, so it was treated as outside "Chapter 1". If the owner meant the introduction to count as Chapter 1, it is the next directory to run; nothing here depends on that choice.

Corpus state: `origin/main` at `2a34fae18dd`. Rater: `local/expo-milnor-rater` v1.0 (Claude Opus 5.5), one pass, one reviewer — so every score below is a single agent's judgement, recorded with its per-dimension vector so a second rater can re-score rather than re-guess.

## 1. Headline

- **376 blocks** read: Ch 1 62, Ch 2 314.
- **192 scored** on H1–H8; **184 `n/a`** — 72 because their kind (`proof`, `table`) is outside the criterion's `applies_to` (`EXPO_NARRATIVE_KINDS` in `cat-harness/content/pipeline/qa-criteria-registry.ts`), 112 because their prose is under the §5A ~50-word threshold (whitespace word count of the `.md`).
- Of the scored blocks: **pass 0 · warn 64 · fail 128**. The gate is the owner's strict one (pass only at 16/16; warn 12–15; fail ≤ 11). Highest score 15/16 (4 blocks).
- Per chapter: Ch 1 — warn 27, fail 20, n/a 15; Ch 2 — warn 37, fail 108, n/a 169.
- Score distribution (T: count): 5: 4, 6: 2, 7: 15, 8: 25, 9: 27, 10: 34, 11: 21, 12: 27, 13: 16, 14: 17, 15: 4.

Dimensions scored below 2 (of 192 scored blocks), and scored 0:

| | H1 economy | H2 concrete-first | H3 why-first | H4 notation | H5 linear | H6 prose carries | H7 right tool | H8 respect |
|---|---|---|---|---|---|---|---|---|
| < 2 | 86 | 141 | 131 | 151 | 132 | 23 | 148 | 157 |
| = 0 | 6 | 5 | 0 | 34 | 17 | 0 | 23 | 37 |

**How to read this.** The verdicts are about *exposition*, not correctness, per §5A. Where reading a block for exposition exposed what looks like a mathematical problem (a mistyped composite, a claim contradicted by a neighbouring block), it is recorded separately as a `needs_owner (content)` note — §4 — and was **not** scored as a correctness finding and **not** edited, per the `exposition-swarm-drain` DO-NOT-TOUCH-DERIVATIONS rule.

## 2. Top 5 worst blocks

1. **`frobenius-hopf-substrate`** (definition, Ch 2 — Quantum Observable Universes) — T = 5/16, vector [0, 0, 1, 0, 1, 2, 0, 1]. H4/H5: the Frobenius form is $\lambda$ and the braiding $\beta$ (the rest of Chapters 1-2 use $\int_A$ and $c$); axiom 3 (L24) calls '$\mu\circ\Delta=(\Delta\otimes\mathrm{id})\circ\alpha\circ(\mathrm{id}\otimes\mu)$' a property of $\lambda$, though $\lambda$ does not occur in it and the two sides have different source and target, and it uses the Hopf $\Delta$ that ex:frobenius-relation-su2 says is *not* the Frobenius coproduct. H1/H7: L21-23 and L40-42 add ~250 words of commentary — including drafting history ('An earlier version of this definition...') and a Lean structure name. H2/H3: no example and no purpose.
2. **`dilog-pentagon-is-associator`** (proposition, Ch 2 — Quantum Observable Universes) — T = 5/16, vector [0, 1, 1, 1, 0, 2, 0, 0]. H5/H8: the 'if and only if' (L1-7) holds because a '$q$-dilogarithm datum' is defined as something satisfying the five-term relation (L20 'the reverse reads the datum's five-term field') — a tautology presented as 'the precise sense in which the $q$-dilogarithm is forced by the rigid-monoidal axioms' (L9), which L24 then says is not proved. The five-term functional equation is called 'the Mac Lane pentagon' (L1). L9 cites prop:q-dilogarithm-exists for uniqueness. L18-20 is a Lean section in prose.
3. **`g-action-on-substrate`** (conjecture, Ch 2 — Quantum Observable Universes) — T = 5/16, vector [1, 1, 1, 0, 1, 1, 0, 0]. H4/H7: the block introduces $\mathcal N_{\rm sym}$, $\mathrm{tr}_F$, $e^{\rm EW}_{\rm sym}$, $e_H$, $\varrho_\Phi$, $T(2,4)$, $T(2,6)$, $\hbar_q$ and 'Anchor II' without definition, and presumes the electroweak sector ($W^\pm$, $Z$, Higgs VEV $v\approx246$ GeV) as background. H8: L52-55 the trace of a product is factored into a product of $q$-dimensions with no argument, and L69 multiplies $[4]_q$ twice for $W^+$ and $W^-$ while L54 forms a direct sum. L87 lists candidate corrections to a $-1.81\%$ residual.
4. **`photon-wavefront-example`** (example, Ch 2 — Quantum Observable Universes) — T = 5/16, vector [1, 1, 1, 0, 1, 1, 0, 0]. H4: the torsion phase is called $\tau(y)$ (L8), the paper's symbol for the fibre functor; $\lambda$ (L11) is a wavelength; $\varphi_i\sigma_i$, 'colour content', 'the exceptional divisor', $K_{\mathrm{mat}}$ are undefined. H8/H7: the phase formula $\tau(y)=\hbar_q\mathrm{Vol}(K_{\mathrm{mat}})\eta^2kw$ (L8) and its colour correction (L24) are posited, not derived from $\mathcal D_\nabla\psi=0$; L27 claims 'a measurable signature distinct from classical birefringence'.
5. **`substrate-parameter`** (definition, Ch 2 — Quantum Observable Universes) — T = 6/16, vector [2, 1, 1, 0, 0, 1, 1, 0]. H5/H8: L19 defines $q$ as 'the unique value for which $d_q$ acts as $q^{-1}d$ on horizontal forms and as $d$ on vertical forms' — but $d_q$ is defined at L4 for every $q$ by exactly that formula, so every $q$ satisfies it; the definition is circular. H4: prop:braiding-eigenvalue-extraction already defines $q:=\lambda_+$; this is a second, different definition of the same symbol. H6: the tikz diagram (L7-17) is decorated with phantom limit labels and carries no content.

## 3. Cross-cutting findings

These recur across many blocks, so fixing them once (a notation decision, a definition consolidated) would lift many scores together. Each is a finding, not a change made.

1. **The substrate parameter $q$ is defined four ways in Chapter 2** — as the braiding eigenvalue on $S^2V$ (`braiding-eigenvalue-extraction`), circularly as 'the unique value for which $d_q$ acts as …' (`substrate-parameter`), as 'the deformation parameter of $A$' with $q\in\mathbb C^*$ (`substrate-parameter-planck`), and as $1+|\langle L_\varTheta,F_A^+\rangle|$ (`levi-generalisation`). Chapter 1 (`quantum-universe`) says $q$ is emergent, read from the twist. H4/H5 in every block that uses $q$.
2. **One operator, several glyphs and definitions.** The Dirac operator is $\mathcal D_\nabla$, $D_\nabla$ and $\mathfrak D_\nabla$ in different blocks; $d_q$ is defined twice with the same formula and given a third, contact-form formula; the Reeb derivation is defined twice (`categorical-reeb`, `categorical-reeb-derivation`) with different conditions; the Frobenius form is $\int_A$ in Ch 1 and $\lambda$ in `frobenius-hopf-substrate`/`substrate-preamble`; the braiding is $c$ and $\beta$.
3. **Symbol collisions with reserved glyphs** (AGENTS §7aa register): $\tau$ (fibre functor) reused for a torsion phase, a complex time and $\tau_\infty$; $\varTheta$ (Maurer–Cartan/contact form) reused as a torus angle; $\lambda$ (Wedderburn block) reused for braiding eigenvalues, a normalisation scalar, resolvent eigenvalues and a wavelength; $\sigma$ (braid generator) for the flip; $q_0$ (calibrated value) for a root-of-unity specialisation; $A$ for an operator; $\mathbb F_q$.
4. **The two coproducts.** `ex:frobenius-relation-su2` carefully separates the Frobenius coproduct $\Delta_\mu$ (diagonal) from the Hopf coproduct; `ex:frobenius-su2` gives a different, convolution formula for the same $\Delta_\mu$; `qu-consequences-intro` and `frobenius-hopf-substrate` axiom 3 conflate them. This is the defect class the swarm-drain skill records as its own incident (PR #3301).
5. **Physics presumed rather than introduced.** Many Ch 2 blocks attach physical conclusions to algebra without a construction (spin–statistics from a weight grading, 'quantum energy' for $\hbar_q$, 'arrow of time', Turing-completeness, Heisenberg, Wilson loops, Osterwalder–Schrader, electroweak sector). The primary-reader ruling (style guide, 2026-09-15) asks that physics names be introduced as names for constructions with the reading in a follow-on remark.
6. **Proof-assistant and drafting apparatus in prose.** Lean declaration names, Lean file paths, 'the Lean sibling', 'carrier', 'inhabited', and 'an earlier version of this definition' appear in scored blocks (listed in §4). A generic 'Archimedean specialisation' boilerplate paragraph is appended to `categorical-q-ext-deriv-unique`, a purely algebraic statement.
7. **Statements that are true by construction stated as results** (H8): existence of an explicit composite (`categorical-q-ext-deriv-exists`, `frobenius-pairing-exists`), uniqueness 'by the formula' (`categorical-dirac-operator-unique`), the zero solution as existence (`q-dilogarithm-exists`), a tautological iff (`dilog-pentagon-is-associator`), monotonicity of $1-1/q$ as an energy theorem (`observation-energy`).
8. **Section intros carry formulas the next blocks restate** (`qu-structures-intro`, `categorical-action-intro`), against the style guide's instruction that the categorical action 'must be motivated before it is displayed'.
9. **What already works.** `vector-calculus-bridge` is close to the reminder-remark the primary-reader ruling asks for; `tqft-context` frames the Li theorem with exactly the scope H7 wants; `frobenius-relation-su2` and `categorical-connection-su2` are good worked examples; `q-codifferential-formula`, `scheme-notation` and `spin-half-representation` miss perfect by one notational point each.

## 4. Items for the owner that are not exposition

Found while reading for exposition; recorded in the sidecar `evidence` field after 'Also:' and listed here so they are not lost. **Default if nothing is done:** nothing changes; the blocks keep their current text and the sidecar verdicts keep naming these items. These are observations from one read, not verified mathematics — each needs a check before any edit. My judgement: the ones that contradict a neighbouring block (the two coproducts, the two spectra of $\Delta_q$, the self-duality theorem vs its own example, the four definitions of $q$) are the cheapest to settle and the most visible to a referee.

- `quantum-universe` — proof-no-lean-mention-in-prose: L38 names the Lean declaration `QOU.AlgebraicSubstrate.IsQGeneric` and the Lean class `CommRing` in prose.
- `quantum-universe-axiom-motivation` — voice: L19 drafting-history leak ('earlier drafts').
- `frobenius-pairing-su2` — needs_owner (content, not exposition): with the stated bilinear pairing, L22 $\langle\alpha,\alpha\rangle_A=\int\alpha^2=0$ under Haar measure, not $\tfrac12$; the value $\tfrac12$ is $\langle\alpha,\bar\alpha\rangle_A$. L27-31 coevaluation also pairs $D$ with $\overline{D}$. Derivation not edited; owner to confirm which pairing is intended.
- `hochschild-homology` — proof-no-lean-mention-in-prose: L19 names `HochschildZero R A`, `hochschildClass_mul_comm`, `traceOnHochschildZero` and 'the Lean sibling'.
- `chern-character` — proof-no-lean-mention-in-prose: L31 'proved in the Lean carrier (`dimQK0_eq_evDimQ_chernCharacter`)'.
- `su2-characters-and-quantum-dimension` — proof-no-lean-mention-in-prose: L17 'The Lean sibling proves ... `su2Character_one` ...'.
- `frobenius-relation-su2` — needs_owner (content): L9 itself shows $\Delta_\mu$ does not land in $A\otimes A$ for $A=\mathcal O(\mathrm{SU}(2))$, so this $A$ is not a Frobenius algebra in $\mathrm{Vect}$ in the finite sense prop:frobenius-relation needs. Derivation not edited.
- `simple-objects-V` — needs_owner (content): L3's 'iff τ(X) is a simple module' is false in the running example (τ(V)=C^2).
- `quantum-observable-universe` — proof-no-lean-mention-in-prose: L34-36 cite `lean/QOU/BraidsAndKnots/VolumeConstraintForcesFibreTwo.lean` and two Lean lemma names; L24 drafting-history leak ('Earlier statements of this definition').
- `qou-axioms-physical-reading` — needs_owner (content): L11's physical gloss of c_1 (orientability) and c_2 (phase around loops) needs checking.
- `frobenius-su2` — needs_owner (content): inconsistent with ex:frobenius-relation-su2 — two different formulas for Δ_μ on O(SU(2)).
- `volume-from-rigidity` — needs_owner (content): the statement 'symplectic self-duality forces rank 2' is false without the Λ²V ≅ 1 hypothesis (C^4 with a symplectic form is a counterexample in Rep(Sp(4))).
- `su2-emergence` — proof-no-lean-mention-in-prose: L22-24 '## Lean structure' names `SU2EmergenceRankForced.lean` and four Lean declarations; L16 drafting-history leak.
- `g-action-on-substrate` — needs_owner (content/anti-fit): the L52-72 factorisation and the [4]_q^2 for a direct sum are unexplained; L87 lists post-hoc correction candidates for the residual (AGENTS.md anti-fit discipline).
- `adjoint-trace` — needs_owner (content): L6 type mismatch (μ applied to V⊗V^∨) and L14 Killing-form identity as written.
- `fiber-adjoint-su2` — needs_owner (content): Hermitian vs skew-Hermitian in L5/L10.
- `substrate-parameter` — needs_owner (content): two inconsistent definitions of q (here vs prop:braiding-eigenvalue-extraction); L19 is circular.
- `frobenius-hopf-substrate` — proof-no-lean-mention-in-prose: L42 names `FrobeniusHopfData` and 'The formalization'; drafting-history leak ('An earlier version'). needs_owner (content): L23 says the antipode identity μ(S⊗id)Δ = ηε 'forces A to be trivial whenever the scalars form a field' — group algebras over a field are counterexamples as stated; L24 axiom 3 is mistyped.
- `brings-coordinate-ring` — needs_owner (content): S_5 acting by permutations does not preserve the q-commutation relations x_i x_j = q x_j x_i (i<j) for q ≠ ±1.
- `categorical-reeb-derivation` — needs_owner (content): ξ_q^{Ω_q} = id_A is impossible for a derivation (ξ_q(1)=0); duplicate definition of the Reeb derivation.
- `rigid-dualizing-complex` — needs_owner (content): L4 states the inverse dualizing complex as the rigidity condition.
- `rigid-dualizing-brings` — needs_owner (content): dualizing vs inverse dualizing complex (L5 vs L19-22); algebra mismatch with title.
- `substrate-self-duality` — needs_owner (content): conflicts with ex:rigid-dualizing-brings (A_σ[-3]).
- `c-quantum-observable-universe` — needs_owner (content): 'Γ_c(M, S) = 0' for a P^1-bundle is not well-defined.
- `archimedean-realisations` — needs_owner (content): rank of H (4 vs 2) depends on dim M, which is not stated.
- `categorical-dirac-operator` — needs_owner (content): type mismatch of the two summands.
- `categorical-lagrangian` — needs_owner (content): D_∇^2 and the sum are not typed as endomorphisms of A.
- `photon-wavefront-example` — needs_owner (content/anti-fit): the torsion-phase formula is posited, not derived; L27 asserts a measurable prediction.
- `categorical-q-ext-deriv-unique` — boilerplate: L14 generic 'Archimedean specialisation' stamp that does not match the block.
- `two-observer-parallelogram` — needs_owner (content): commutator of elements of the commutative ring End(1) ≅ R.
- `germ-commutator-q-curvature` — needs_owner (content): the commutator vanishes for commutative A, which includes the archimedean realisation.
- `observation-fermion-action` — needs_owner (content): G-equivariance contradicts the claimed mixing of Sym^2 V and Λ^2 V.
- `q-laplacian-spectral-tower` — needs_owner (content): eigenvalue claim is unsupported as stated.
- `brings-geometric-connection` — needs_owner (content): contact structure on a 2-dimensional surface.
- `categorical-self-duality` — proof-no-lean-mention-in-prose: L10-14 discuss `QOU.categorical_self_duality` and `CategoricalInstanton`. needs_owner (content): 'critical point ⟹ instanton' needs a minimising hypothesis.
- `self-dual-ses` — needs_owner (content): ⋆_q^2 = q^2 ⋆^2 is not an involution; dimension 4 vs 3.
- `q-resolvent-properties` — needs_owner (content): spectrum disagrees with prop:q-laplacian-spectral-tower.
- `q-exponential-realisations` — needs_owner (content): 1/[n]_q! is not in the Habiro ring.
- `q-dilogarithm-exists` — proof-no-lean-mention-in-prose (vocabulary): 'carrier', 'inhabitation', 'witness' — Lean idiom in prose.
- `dilog-pentagon-is-associator` — proof-no-lean-mention-in-prose: L15, L18-20 name `QOU.BringsSurface.PentagonTwist.assoc_pentagon`, `pentagon_iff_isDilog`, `#print axioms`, Mathlib, `QRogersAnalyticContinuation`.
- `levi-generalisation` — needs_owner (content): a fourth, curvature-based formula for q(p) with no derivation.

## 5. Where the verdicts are recorded, and one placement choice

**Location.** Each block's verdict is appended to its own `block-qa/v1` sidecar, `<block>.qa.json` beside the `.md`, under `criteria["expo-milnor-clarity"]`. That is the location the platform's readers resolve for this repository: `qa-paths.existingBlockQaPath` tries `test/results/block-qa/…` first and falls back to the sibling, and this repository has no `test/results/block-qa/` tree (the 2026-10-04 platform-pin note records the derived corpus living on the `qa-reports` branch). The platform's own writer, `qa-agent-entry.ts`, was **not** used, because it writes to the results tree and to a `test/attestations/block-qa/` store — which would have created both trees for 376 blocks, i.e. migrated this repository's verdict storage. That is an owner decision, not part of an audit.

**Entry shape.** `field_hash` from the platform's `hashBlockFiles` (md, ts, and the Lean file resolved through `lean.ref`, with `lean_statement`); `result`; `severity` (`major` for fail, `minor` for warn); `score: {value: T, max: 16, rubric: {H1..H8}}`; `evidence` (quoted line-level finding); `notes` (vector, weakest dimensions, suggested rewrite, pointer to this doc); `reviewer: {kind: agent, id: local/expo-milnor-rater, version: 1.0}`; `reviewed_sha` = the corpus commit above. Every write was checked to change nothing in the sidecar except the one appended entry and the top-level `updated_at` (parsed before/after and compared).

**Verified, not inferred, that the docs reader picks them up.** Calling the platform's `readWitnessDoc("block", …)` (the function `gen-docs-pages.ts` uses for the per-block QA badge and panel) on all 376 blocks returns this verdict as the criterion's result with `freshness: "fresh"` for every block: warn 64, fail 128, n/a 184. `publish-block-qa.ts` decides freshness by `field_hash`, which these entries carry, so it counts them too (inferred from its source, not run). What was **not** verified is the rendered site itself: the docs build was not run.

**The placement choice (a decision for the owner).**

- *What it is.* The panel reads the **first** entry in a criterion's array as the effective verdict (`qa-witness.ts` `projectEntryArrays`). 326 of these sidecars already held an `expo-milnor-clarity` entry from 2026-07-19 — `local/qa-agent-drain`, model `gemini-3.1-pro`, notes `[EXPIRED-NO-FIELD-HASH] Looks good. Heuristically verified.` — which the sidecars' own `$expired` note says 'adjudicate nothing'. The platform's `insertAdjudication` would place a *different* reviewer's verdict **after** an existing one, leaving that expired `pass` as the displayed result.
- *What I did.* Placed the new verdict **first**, so the panel shows it; the expired entry is kept, unchanged, second. Without this the owner's stated goal (results visible in the per-block report) is not met: every block would still display 'pass'.
- *Option A — keep it (my recommendation).* Costs nothing further. Risk: it departs from `insertAdjudication`'s 'a different reviewer keeps its place' rule for this one criterion; if the platform later re-sorts by that rule, the expired pass would lead again. Commits to treating expired, hash-less entries as non-adjudicating, which is what their own note says.
- *Option B — reorder to platform order.* A one-line script per sidecar moves the new entry to the end. Restores the platform rule exactly; the panel then shows the expired 'pass' for 326 blocks and these verdicts only as history.
- *Option C — drop the expired entries.* Removes 326 hash-less entries; both orders then agree. Destroys a historical record the `$expired` note deliberately keeps (bean `qou-pwut`), so I would not.
- *Default if you say nothing:* A stays in place.

One `warn` was replaced as the leading verdict by an `n/a`: `categorical-lichnerowicz-proof` (kind `proof`) carried an expired `warn` ('Block is quite long'). The `n/a` is a genuine scope ruling — proofs are outside `applies_to` — not a distrust-clear; `qa-flag-preservation-audit.ts` reports both chapter trees clean (62 and 314 sidecars) and `scripts/qa-duplicate-verdict-check.py` reports no contradictions in them.

## 6. Summary table (scored blocks)

Order follows the chapter manifests. Columns H1–H8 are the 0–2 scores; T is the total.

### Ch 1 — Quantum Universes — `quantum-universes/`

| block | kind | H1 | H2 | H3 | H4 | H5 | H6 | H7 | H8 | T | result | worst issue |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `quantum-universes-intro` | prose | 1 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 13 | warn | H5: chapter numbering contradicts itself — L15 'imposed in Chapter 2' vs L33 '[Chapter 3](#chap:qou)'. |
| `scheme-notation` | prose | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 15 | warn | H4: L3 '$\mathbb{F}_q$' reuses $q$, the paper's substrate parameter, as a field order. |
| `rigid-monoidal-intro` | prose | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 10 | fail | H5/H2: L5 'We keep two examples in view: the polynomial ring $\mathbb{C}[z]$ and the coordinate ring' names algebras, not monoidal categories, then 'Objects have tensor products and a unit over a base |
| `snake-identity` | definition | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 14 | warn | H2/H3: the definition gives no instance and no purpose; the reader meets two tikz diagrams before learning what they say in $\mathrm{Vect}$ (L1-33). |
| `rigid-monoidal-category` | definition | 1 | 1 | 1 | 1 | 2 | 1 | 0 | 1 | 8 | fail | H7: one definition block carries monoidal, rigid, $R$-linear, braided, symmetric and exterior-power definitions; |
| `monoidal-justification` | remark | 1 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 12 | warn | H7/H8: L5 'The category of superselection sectors is automatically rigid braided monoidal' and 'Locality and covariance force the monoidal structure' assert a deep theorem (Doplicher–Haag–Roberts) as obvious, uncited. |
| `rigid-monoidal-vect` | example | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 13 | warn | H5/H8: L1 'Both arise as representations of a function algebra' is inaccurate as stated — $\mathrm{Vect}_{\mathbb{C}}$ is not the representation category of $\mathbb{C}[z]$, and $\mathrm{Rep}(\mathrm{ |
| `quantum-universe-intro` | prose | 1 | 2 | 1 | 1 | 1 | 2 | 1 | 1 | 10 | fail | H5: L1 'a quantum universe is a triple $(\mathbf{C},A,\tau)$' omits the differential calculus that sec:qou-intro L14 lists as part of the definition; |
| `quantum-universe` | definition | 0 | 1 | 1 | 1 | 1 | 2 | 0 | 1 | 7 | fail | H7/H1: the definition (L1-24) is followed by ~400 words of ground-ring discussion (L26-41) — cyclotomic units, the initial q-generic ring, 'past the archimedean wall' — that the definition itself does not need. |
| `quantum-universe-axiom-motivation` | remark | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 13 | warn | H1/H7: L19-23 'This axiom is what earlier drafts asserted, less directly, as a numerical identity' leaks drafting history, and the co-Casimir paragraph introduces $\mathrm{tr}_M$ and $C_{\dim_q}$ (H4) |
| `tau-notation` | prose | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 12 | warn | H8/H1: three bullets justify the choice of a letter (L3-5) — ceremony. |
| `frobenius-pairing` | definition | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 14 | warn | H4: L18-22 uses $\rho^{-1}$, $\alpha^{-1}$ and $\lambda_A$ for the unitors/associator, while def:rigid-monoidal-category writes the left unitor $\ell_X$; |
| `frobenius-pairing-exists` | proposition | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 1 | 12 | warn | H8: L3 'The non-degenerate Frobenius pairing ... exists as a morphism in $\mathbf{C}$. |
| `quantum-universe-frobenius-pairing-unique-intro` | prose | 1 | 1 | 2 | 1 | 1 | 2 | 2 | 1 | 11 | fail | H4/H5: L1 'Pinning the Frobenius pairing on the fundamental object $A$' — the fundamental object is $V$ (def:fundamental-object), $A$ is the Frobenius–Hopf object. |
| `frobenius-pairing-unique` | proposition | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 14 | warn | H7: the hypothesis '$A$ simple' (L1) is the load-bearing one but the block does not say in what sense (simple object of $\mathbf{C}$, or simple algebra) — $\mathcal{O}(\mathrm{SU}(2))$, the running example, is simple in neither… |
| `frobenius-pairing-su2` | example | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 13 | warn | H5: L10 calls the matrix coefficients an 'orthonormal basis' and L14 gives them norm $1/(2j+1)$. |
| `frobenius-geometric-role` | remark | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 13 | warn | H4/H5: L3 identifies $\Omega^1(A)$ with 'the Kähler differentials', while sec:quantum-universe-intro and ex:quantum-universe-su2 use the left-invariant calculus — two different modules. |
| `quantum-universe-su2` | example | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 13 | warn | H1/H7: item (v) (L11) is a single 230-word paragraph covering the flip, the $R$-matrix, the Hecke relation, the Haar state and the left-covariant calculus. |
| `higher-forms` | definition | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 11 | fail | H5/H4: L7 'For an object $V$, $\Lambda^k V$ denotes its $k$-th exterior power' is unrelated to the forms being defined and introduces notation the block never uses. |
| `higher-forms-su2` | example | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 1 | 12 | warn | H4/H5: L1 writes $\Omega^1(A)=\mathrm{span}\{\omega_i\}$ and L4 writes $\Omega^1(A)=A\otimes\mathrm{span}\{\omega_i\}$. |
| `fundamental-object` | definition | 2 | 2 | 1 | 1 | 1 | 2 | 1 | 1 | 11 | fail | H8: L7 'Under a fibre functor the volume constraint forces $\mathrm{rank}(V)=2$' states a theorem without its source and before the volume constraint is defined. |
| `tannaka-dual` | definition | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 14 | warn | H7: L5 invokes Deligne's neutral-Tannakian reconstruction 'over $R$', but Deligne's theorem is over a field; |
| `unit-simplicity` | remark | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 12 | warn | H5/H8: L3 'The space ... $\mathrm{Hom}(\Lambda^2V,\mathbf 1)$ is one-dimensional over $R$. |
| `hochschild-homology` | definition | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 12 | warn | H2/H3: the definition opens with $\mathrm{Tor}^{A^e}$ (L6) and only at L19 says why the paper needs it (traces live in $HH_0$); |
| `grothendieck-group-of-a-qou` | definition | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 13 | warn | H5: L11 defines $\dim_q$ via the trace 'of a rigid monoidal category', but a quantum universe need not be rigid (def:quantum-universe L24); |
| `chern-character` | definition | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 2 | 12 | warn | H7/H1: L31 ends with a defensive aside about the base curve's Euler characteristic that the definition does not need. |
| `su2-characters-and-quantum-dimension` | example | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 14 | warn | H7/H1: L19 adds two 'consequences' — that $-6$ cannot be a quantum dimension, and a divergent-series remark about $\mathcal O(\mathrm{SU}(2))$ — that serve later chapters' arguments, not this example. |
| `qu-consequences-intro` | prose | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 1 | 11 | fail | H4/H5: L1 introduces the Hopf comultiplication 'built from the group-multiplication rule' and L3 the Frobenius comultiplication $\Delta_\mu$ 'dual to $\mu$', and L1 says both 'follow directly from the Frobenius pairing' — the t… |
| `frobenius-relation` | proposition | 2 | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 11 | fail | H5: L1 'This compatibility makes $A$ a Frobenius algebra' — no compatibility has been stated yet. |
| `frobenius-relation-su2` | example | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 14 | warn | H8: L9 concedes that for $\mathrm{SU}(2)$ $\Delta_\mu(f)$ is 'a distribution', i.e. |
| `involutive-structure` | definition | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 9 | fail | H6/H1: three tikz diagrams (L6-41) restate one-line equations; |
| `positive-definite-dagger` | proposition | 2 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 11 | fail | H5: L9 'The Frobenius dagger satisfies $S^2=\mathrm{id}$ and restricts to $S=\dagger$ on $\mathrm{End}(\mathbf 1)$' — a property of $S$ is attributed to $\dagger$, and 'restricts to $S=\dagger$' does not parse. |
| `positive-dagger-su2` | example | 2 | 2 | 1 | 1 | 1 | 2 | 1 | 2 | 12 | warn | H5: the proposition concerns $f\colon\mathbf 1\to X$ (prop:positive-definite-dagger L9) but the example tests endomorphisms of $V$ (L7); |
| `dagger-notation` | remark | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 14 | warn | H4: L5 writes the physicist's adjoint as $A^\dagger_{\mathrm{phys}}$, reusing $A$, the Frobenius–Hopf object. |
| `tannaka-krein-overview` | remark | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 1 | 11 | fail | H8/H7: L5 'Any two fibre functors are isomorphic' is false as a general statement (it holds over an algebraically closed field, or fpqc-locally); |
| `axiom-independence` | remark | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 14 | warn | H5: L3 argues that the fibre functor is not supplied by Deligne's theorem, which bears on the fibre-functor datum, not on axiom 1 (well-founded braiding order); |
| `qu-structures-intro` | prose | 1 | 1 | 2 | 0 | 1 | 1 | 0 | 1 | 7 | fail | H4/H7: a 300-word section intro introduces $\nabla$, $F_\nabla$, $\mathrm{Ad}(A)$, $J^1(A)=A\otimes_{\mathbf C}\Omega^1(A)$, $\star$, $\alpha^*$, $\mathrm{vol}$, $\pi$, $[\pi,\pi]_{\mathrm{SN}}$ and the HKR map — formulas that … |
| `categorical-connection` | definition | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 14 | warn | H6: the Leibniz triangle (L7-14) is labelled '$\nabla\otimes1+1\otimes\nabla$' but its target is $A\otimes\Omega^1(A)$, so the diagonal arrow needs a multiplication the label omits; |
| `categorical-connection-exists` | proposition | 1 | 1 | 2 | 1 | 1 | 2 | 2 | 1 | 11 | fail | H4/H5: L3 types the connection as $\nabla\colon A\to\Omega^1(A)$, while def:categorical-connection has $\nabla\colon A\to A\otimes\Omega^1(A)$. |
| `categorical-connection-su2` | example | 2 | 2 | 1 | 2 | 1 | 2 | 1 | 1 | 12 | warn | H8: L34 'Since $\mathrm{SU}(2)\cong S^3$ is connected, all monodromy is trivial' — triviality of monodromy of a flat connection needs simple connectivity. |
| `categorical-jet` | definition | 2 | 1 | 2 | 0 | 1 | 2 | 1 | 1 | 10 | fail | H4/H5: L4 defines $J^1(A):=A\otimes_{\mathbf C}\Omega^1(A)$ (tensor 'over' a category), yet the extension at L13 has $A\otimes\Omega^1(A)$ as a proper subobject of $J^1(A)$ with quotient $A$ — the two descriptions of $J^1(A)$ a… |
| `categorical-hodge-star` | definition | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 8 | fail | H4: $n$ (L1) is never defined; $\alpha^*=S(\alpha)$ (L20) applies the antipode of $A$ to a form; |
| `hodge-su2` | example | 1 | 2 | 1 | 1 | 2 | 2 | 1 | 2 | 12 | warn | H1/H4: L7 discusses self-dual 2-forms, which do not arise in dimension 3, and refers to '$\dim H=4$' with $H$ undefined. |
| `poisson-object` | definition | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 9 | fail | H5/H8: L11 'The Frobenius self-duality $A\cong A^\vee$ induces an identification $\Omega^1(A)^\vee\cong\Omega^1(A)$' — self-duality of $A$ does not imply self-duality of $\Omega^1(A)$. |
| `poisson-hkr-connection` | remark | 1 | 1 | 1 | 0 | 1 | 2 | 0 | 1 | 7 | fail | H4/H7: in 190 words the remark introduces $\mathrm{Mod}(\mathbb F_p)$, $\mathcal O(H)$, $\pi_<$, $HH^2(\mathcal U_q,\mathrm{Ad})$, $\phi_1$, $\Gamma(\Lambda^2T_A)$ and a 'non-commutative formal group $G/\mathbb Z_p$', none defi… |
| `outro-quantum-universes` | prose | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 1 | 11 | fail | H5: L3 says the next chapter adjoins 'the substrate parameter $q$ and the Reeb derivation $\xi$', but sec:qou-definition-intro says Chapter 2 imposes rigidity, non-degenerate integration, observability, measurability and the vo… |
| `simple-objects-V` | remark | 2 | 1 | 1 | 1 | 0 | 2 | 2 | 1 | 10 | fail | H5: L3 'X is simple if and only if $\tau(X)$ is a simple module' contradicts L5, where the simple object $V$ has $\tau(V)$ a rank-2 free module (not simple). |

### Ch 2 — Quantum Observable Universes — `quantum-observable-universes/`

| block | kind | H1 | H2 | H3 | H4 | H5 | H6 | H7 | H8 | T | result | worst issue |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `qou-definition-intro` | prose | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 13 | warn | H5: L1 'the QOU on $\mathrm{SU}(2)$ exactly satisfies these constraints over an arbitrary commutative ring', but ex:quantum-universe-su2(v) shows classical $\mathrm{SU}(2)$ (symmetric braiding) does not satisfy the well-orderin… |
| `quantum-observable-universe` | definition | 0 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 8 | fail | H1/H7: L24-44 is a 20-line editorial note on how 'earlier statements of this definition' read condition 5, with a dimension table and a Lean file path — material for a remark, not the definition. |
| `qou-axioms-physical-reading` | remark | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 13 | warn | H8: L11 'The vanishing of $c_1$ makes the adjoint bundle orientable' — orientability is governed by $w_1$, and a complex bundle is always orientable; |
| `qou-exists-axiom-3` | lemma | 1 | 1 | 1 | 1 | 1 | 2 | 0 | 1 | 8 | fail | H5: titled 'Axiom 3' but def:quantum-observable-universe numbers Chern-class vanishing as condition 4 (Observability is 3). |
| `braiding-induced-ordering` | proposition | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 11 | fail | H5: L1 defines $\prec_c$ from the braiding, then L1's last sentence asserts well-foundedness of 'the degree-lexicographic order on reduced positive braid monomials' without saying this is $\prec_c$. |
| `fibre-functor-rigidity` | remark | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 10 | fail | H4: L1 'a rigid, passive role' reuses 'rigid', a defined term (duals). |
| `emergence-intro` | prose | 2 | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 12 | warn | H5: L1 'the four axioms of the quantum observable universe' — def:quantum-observable-universe lists five conditions. |
| `frobenius-su2` | example | 2 | 2 | 1 | 1 | 0 | 2 | 1 | 1 | 10 | fail | H5: this block gives $\Delta_\mu(f)(g,h)=\int_G f(xg)\overline{h(x)}\,dx$ and says the Frobenius relation 'encodes the associativity of convolution', while ex:frobenius-relation-su2 (Chapter 1) comput |
| `dagger-su2` | example | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 13 | warn | H4: $g$ is a group element (L1 '$f^\dagger(g)=\overline{f(g^{-1})}$') while $f$ ranges over both intertwiners $V_j\to V_k$ and functions on $\mathrm{SU}(2)$ in one paragraph. |
| `volume-from-rigidity` | lemma | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 0 | 8 | fail | H8: L1 'This alternating condition forces $\mathrm{rank}(V)=2$' is asserted, and the following sentences instead derive $\mathrm{rank}(\Lambda^2V)=1$ from non-degeneracy of $\epsilon$, i.e. |
| `su2-volume-from-rigidity` | example | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 14 | warn | H5: L1 'restricting the gauge group from $\mathrm{GL}(2,\mathbb C)$ to at least $\mathrm{SL}(2,\mathbb C)$' — the constraint shrinks the group, so it lands *inside* $\mathrm{SL}(2,\mathbb C)$. |
| `su2-emergence` | theorem | 1 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 12 | warn | H5: L14 'so $G\subseteq\mathrm{SU}(2)$ — or its split real form $\mathrm{SL}(2,\mathbb R)$' contradicts the displayed conclusion $G\subseteq\mathrm{SU}(N)$. |
| `su2-emergence-example` | example | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 14 | warn | H8: L1 'Any tensor automorphism $g$ must preserve $\epsilon$' — the reason (naturality: $\epsilon$ is a morphism of $\mathbf C$) is the load-bearing step and is not given. |
| `spin-labels` | proposition | 2 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 10 | fail | H5/H8: L1 'Because $G\cong\mathrm{SU}(2)$' — thm:su2-emergence gives only $G\subseteq\mathrm{SU}(2)$ under a realisation hypothesis; |
| `spin-labels-su2` | example | 1 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 13 | warn | H5: L20 '$\mathbb C[z]=\bigoplus_n\mathrm{Sym}^nV$ serves as the coordinate ring of $\mathbb P(V)$' — $\bigoplus\mathrm{Sym}^n\mathbb C^2$ is $\mathbb C[z_0,z_1]$, the homogeneous coordinate ring; |
| `spin-half-representation` | remark | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 15 | warn | H4: L10 writes the torus angle as $\theta_q$; the subscript $q$ is unexplained, and the torus $T$ is used both as a set and as an element acting on $e_\pm$. |
| `g-action-on-substrate` | conjecture | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 5 | fail | H4/H7: the block introduces $\mathcal N_{\rm sym}$, $\mathrm{tr}_F$, $e^{\rm EW}_{\rm sym}$, $e_H$, $\varrho_\Phi$, $T(2,4)$, $T(2,6)$, $\hbar_q$ and 'Anchor II' without definition, and presumes the e |
| `weight-decomposition-intro` | prose | 1 | 1 | 2 | 2 | 1 | 2 | 1 | 0 | 10 | fail | H8: L1 'This splitting establishes the geometric origin of spin-statistics directly from the categorical structure' and 'horizontal forms ... |
| `maximal-torus` | definition | 2 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 8 | fail | H5: circular — L1 defines the weight subcategory as sums of 'the weight spaces of $V$', and then defines $T$ as the subgroup acting diagonally on those weight spaces; |
| `maximal-torus-su2` | example | 2 | 2 | 1 | 0 | 2 | 2 | 2 | 2 | 13 | warn | H4: L1 writes the torus angle as $\varTheta$, the symbol the paper reserves for the Maurer–Cartan/Reeb 1-form ($\varTheta=g^{-1}dg$, $\varTheta_A$). |
| `weight-decomposition` | definition | 2 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 12 | warn | H6: the tikz diagram (L3-12) draws a hook $\Omega^k_H\hookrightarrow\Omega^k_V$ labelled '$\oplus$', which is not a map in the decomposition; |
| `weight-decomposition-su2` | example | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 14 | warn | H4: L6-7 parametrise the torus by $\theta_q$, with an unexplained subscript $q$ on a classical angle; |
| `vectors-hadrons-intro` | prose | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 10 | fail | H4/H7: the roadmap names 'the Pawlowski–Leitner canonical basis', 'the unital Gröbner–Shirshov route', 'fibre integration commutes with the intertwiner expansion of hadron states' — none introduced or cited. |
| `adjoint-trace` | remark | 2 | 1 | 1 | 0 | 1 | 2 | 1 | 1 | 9 | fail | H4/H5: L6 composes $\int_A\circ\mu\circ(f\otimes\mathrm{id}_{V^\vee})\circ\mathrm{coev}_V$, applying the multiplication $\mu$ of $A$ to $V\otimes V^\vee$; |
| `pawlowski-leitner-basis` | proposition | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 9 | fail | H4: L14 the vector $e_+^{\otimes(j+m)}\otimes e_-^{\otimes(j-m)}$ has $m$ undefined and is not highest-weight unless $m=j$; |
| `pawlowski-leitner-inner-product` | proposition | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 9 | fail | H4/H5: L16 the arrow '$\phi^\dagger\circ\psi\otimes\mathrm{id}$' lands in $A\otimes V_j^\vee$, i.e. |
| `differential-structures-intro` | prose | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 10 | fail | H8/H5: L1 'Each of these structures is forced by the QOU axioms' and '... |
| `categorical-reeb` | definition | 2 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 8 | fail | H2/H3: no picture of the Reeb field (the Hopf circle on $S^3=\mathrm{SU}(2)$) and no purpose stated. |
| `categorical-reeb-exists` | theorem | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 9 | fail | H6/H5: the tikz square (L3-12) asserts $\varTheta_A\circ\xi=\iota_\xi\circ d$ with $\varTheta_A\colon A\to A$, which is neither of the two constraints in the statement and retypes $\varTheta_A$ (a 1-form). |
| `reeb-su2` | example | 2 | 2 | 1 | 1 | 1 | 2 | 1 | 2 | 12 | warn | H5: L1 ends with '$\iota_\xi d\varTheta=0$', which is not the vertical-generator condition '$\pi_V\circ d=\iota_\xi d\varTheta_A$' of def:categorical-reeb that this example is meant to instantiate. |
| `categorical-reeb-brings` | example | 1 | 1 | 1 | 0 | 1 | 2 | 1 | 1 | 8 | fail | H4/H5: L1 starts on 'the Bring coordinate ring $\mathcal O_q(\mathcal B)$' and then works on $A=\mathcal O_q(\mathrm{SU}(2))$ without saying how the two relate; |
| `contact-affine-chart` | definition | 2 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 8 | fail | H4/H5: L4 writes points of $\mathbb P(V)$ as classes $[\alpha]$ of differential forms and L11 defines $Z$ as a ratio of forms ($\alpha_H/\iota_\xi\alpha$) that is said (L25) to take values in a distribution — the objects being … |
| `differential-structures-fiber-adjoint-intro` | prose | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 10 | fail | H4/H1: a four-sentence roadmap naming 'the projector onto coadjoint orbits', 'the substrate's radial coordinate', 'the fibre-functor atlas' without saying what any is or why the section needs it. |
| `fibre-functor-atlas` | proposition | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 1 | 12 | warn | H7/H8: L1 concludes that fibre functors form 'a $G$-gerbe', a heavy notion for the primary reader, with no framing of why it is the right tool and no reference; |
| `fibre-functor-atlas-affine-charts` | remark | 2 | 1 | 2 | 1 | 2 | 2 | 1 | 1 | 12 | warn | H8: L1 'the $G$-gerbe of fibre functors is precisely the affine atlas of the quantum universe' turns an analogy into an identity. |
| `substrate-radial-coordinate` | proposition | 2 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 7 | fail | H8/H5: L1 'As $q\to\infty$ ... $Z\to0$; as $q\to1$ ... $Z\to\infty$' — $Z$ (def:contact-affine-chart) is defined with no dependence on $q$, and no argument or citation is given. |
| `fiber-adjoint-involution` | proposition | 2 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 7 | fail | H4/H5: L1 calls $\sigma\colon\mathbb P(V)\hookrightarrow\mathrm{Ad}(A)$ 'an involution', but a map between two different objects cannot be one. |
| `fiber-adjoint-su2` | example | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 14 | warn | H5: L5 $vv^\dagger/\\|v\\|^2-\tfrac12\mathrm{id}$ is Hermitian, but is placed in $\mathfrak{su}(2)$ (skew-Hermitian) and identified with the orbit of $\tfrac12\mathrm{diag}(i,-i)$; |
| `connection-su2` | example | 1 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 13 | warn | H1: repeats the material of ex:categorical-connection-su2 (Chapter 1) in less detail. |
| `substrate-parameter-intro` | prose | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 1 | 11 | fail | H4/H8: L1 'This links the microscopic categorical data directly to the macroscopic fluid parameter' — no fluid parameter has been introduced; |
| `braiding-eigenvalue-extraction` | proposition | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 1 | 12 | warn | H5/H8: L3-6 'We define ... $q:=\lambda_+$, $\lambda_-=-q^{-1}$' presents the second equation as part of a definition, though $\lambda_-$ was already determined; |
| `braiding-eigenvalue-extraction-novelty` | remark | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 14 | warn | H4: L3 'the CAL-2 calibration', L5 'archimedean level', L7 'the macroscopic fluid PDE' are project terms not explained to a reader meeting them here; |
| `spectral-chart-correspondence` | proposition | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 10 | fail | H8: L1 asserts that the transition coordinate $\kappa$ in $zw=\kappa$ 'equals $\lambda_+^{-1}=-\lambda_-=q^{-1}$' with no argument; |
| `substrate-parameter` | definition | 2 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 6 | fail | H5/H8: L19 defines $q$ as 'the unique value for which $d_q$ acts as $q^{-1}d$ on horizontal forms and as $d$ on vertical forms' — but $d_q$ is defined at L4 for every $q$ by exactly that formula, so every $q$ satisfies it; |
| `substrate-parameter-limits-and-lusztig` | remark | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 10 | fail | H4/H7: '$q\colon M\to k^\times$' (L1) uses $M$ and $k$ undefined, and the Lusztig integral form $\mathcal U^{\mathbb Z}_q(\mathfrak{su}(2))$ is dropped in without saying what it is for (and is usually |
| `substrate-parameter-unique` | theorem | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 0 | 9 | fail | H8: L1 states a theorem about $q\in\mathrm{End}(\mathbf1)$ and then asserts, as part of the theorem, that 'the substrate parameter is a field $q\colon M\to\mathbb R_{>0}$ that varies ... |
| `substrate-parameter-su2` | example | 2 | 2 | 1 | 0 | 2 | 2 | 1 | 1 | 11 | fail | H4: L1 uses $q_0$ for an arbitrary specialisation, including $q_0=e^{\pi i/\kappa}$, while the paper reserves $q_0$ for the calibrated value $\approx1.10998$; |
| `substrate-parameter-brings` | example | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 10 | fail | H5: L1 'On Bring's surface, $V\otimes V\cong V_1\oplus V_0$' — a tensor decomposition is a statement about the category, not about a surface; |
| `quantum-universe-explication` | prose | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 1 | 11 | fail | H8: L1 'Every subsequent physical feature—commutators, Reeb derivations, and action traces—is governed strictly by this single categorical parameter' overclaims (the paper's own calibrations are three). |
| `q-hodge-star` | definition | 2 | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 10 | fail | H4: $\wedge_q$ (L4) is not defined; '$n$' is undefined (as in def:categorical-hodge-star); |
| `q-deformed-commutator` | definition | 2 | 1 | 1 | 0 | 1 | 2 | 1 | 0 | 8 | fail | H8: the definition sets $[\hat X,\hat P]_q:=J\hbar_q(p)$ without defining $\hat X$, $\hat P$ (as operators on what), the Levi distribution $H$, $M$ or $p$ — it assigns a value to a commutator of undefined objects. |
| `heisenberg-commutator-prop` | proposition | 2 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 11 | fail | H8: the proposition records the two limits of $1-q^{-1}$ (L3-4), immediate from def:q-deformed-commutator, under physics labels ('maximal uncertainty'); |
| `heisenberg-commutator` | remark | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 0 | 9 | fail | H8: L3 'As $q\to1$, the observer sits at the base of the Reeb fibre ... |
| `algebraic-substrate-intro` | prose | 1 | 1 | 2 | 0 | 2 | 2 | 1 | 1 | 10 | fail | H4: a 119-word intro names the $q$-zeta function, the Chebyshev function of the Reeb flow, the Hasse–Weil bound, 'the obstruction to classicality' and 'the unit particle as a categorical invariant', none explained. |
| `substrate-preamble` | prose | 1 | 1 | 1 | 0 | 1 | 2 | 1 | 1 | 8 | fail | H4: L3 names the Frobenius form $\lambda$ (elsewhere $\int_A$; |
| `frobenius-hopf-substrate` | definition | 0 | 0 | 1 | 0 | 1 | 2 | 0 | 1 | 5 | fail | H4/H5: the Frobenius form is $\lambda$ and the braiding $\beta$ (the rest of Chapters 1-2 use $\int_A$ and $c$); |
| `brings-coordinate-ring` | definition | 2 | 2 | 1 | 2 | 1 | 2 | 1 | 1 | 12 | warn | H5: L29 says the $S_5$ permutation action descends to $\mathcal O_q(\mathcal B)$ by algebra automorphisms, but swapping $x_i,x_j$ turns $x_ix_j=qx_jx_i$ into $x_jx_i=qx_ix_j$, so permutations do not preserve the relations of L2… |
| `substrate-parameter-planck` | definition | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 10 | fail | H4/H5: this is the third definition of $q$ in the chapter — 'the deformation parameter of $A$', with $q\in\mathbb C^*$ (L1) — alongside $q:=\lambda_+$ (prop:braiding-eigenvalue-extraction) and $q\in\mathrm{End}(\mathbf1)$ (def:… |
| `categorical-reeb-derivation` | definition | 2 | 1 | 1 | 0 | 0 | 2 | 1 | 0 | 7 | fail | H4: a second 'categorical Reeb derivation' ($\xi_q$) beside def:categorical-reeb ($\xi$), with different defining conditions. |
| `reeb-flow-bridge` | remark | 1 | 2 | 1 | 1 | 1 | 2 | 1 | 0 | 9 | fail | H8: L6-8 assert correspondences — prime ideals of $\mathcal O_q(\mathcal B)$ ↔ closed Reeb orbits; |
| `reeb-contact-universal-computer` | remark | 1 | 1 | 1 | 1 | 1 | 2 | 0 | 0 | 7 | fail | H7/H8: L3-5 invoke Cardona–Miranda–Peralta-Salas–Presas (existence of *some* Turing-complete Reeb flow on a contact 3-manifold) and conclude that 'every fibre $\mathcal S_p$ inherits the structural ca |
| `rigid-dualizing-complex` | definition | 2 | 0 | 1 | 0 | 1 | 2 | 0 | 1 | 7 | fail | H7: derived categories, injective dimension, $R\mathrm{Hom}_{A^e}$ and Van den Bergh duality arrive with no statement of what the dualizing complex is for and no simple case (for a smooth projective curve it is $K[1]$). |
| `rigid-dualizing-brings` | example | 1 | 2 | 1 | 1 | 0 | 2 | 1 | 0 | 8 | fail | H5: L1 promises the complex 'for Bring's coordinate ring' and L3 sets $A=\mathcal O_q(\mathrm{SU}(2))$. |
| `substrate-self-duality` | theorem | 2 | 1 | 1 | 1 | 0 | 2 | 1 | 1 | 9 | fail | H5: L1 states $A\simeq\omega_A^\bullet$ for the substrate, while ex:rigid-dualizing-brings computes $\omega_A^\bullet\cong A_\sigma[-3]$ (Nakayama-twisted and shifted) for the running $q$-deformed exa |
| `substrate-self-duality-physical` | remark | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 1 | 12 | warn | H5: L1 'The Frobenius form $\lambda$ is the unique trace that makes $A$ its own dualizing object' contradicts prop:frobenius-pairing-unique (unique up to scalar). |
| `archimedean-intro` | prose | 2 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 11 | fail | H3/H7: L1 announces CR geometry, contact manifolds and pseudo-Hermitian structures — heavy tools for the primary reader — without saying why the archimedean realisation needs them. |
| `c-quantum-universe` | example | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 10 | fail | H5: L1 'A quantum universe over $K$ is realised by the 4-tuple $(\mathbf C,\varTheta,G,\mathcal S)$' — the relation between this 4-tuple and the triple $(\mathbf C,A,\tau)$ of def:quantum-universe is never stated; |
| `c-quantum-observable-universe` | example | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 0 | 9 | fail | H8: L6 '$\Gamma_c(M,\mathcal S)=0$' — sections of a $\mathbb P^1$-bundle do not form a vector space, so 'vanishing' has no meaning as stated; |
| `archimedean-realisations` | remark | 2 | 1 | 1 | 0 | 1 | 2 | 0 | 0 | 7 | fail | H5/H8: L3 'the rank-4 distribution $H=\ker\varTheta$' — on the 3-manifold $\mathrm{SU}(2)$ a contact distribution has rank 2; |
| `categorical-dirac-operator-intro` | prose | 2 | 1 | 2 | 1 | 2 | 2 | 1 | 1 | 12 | warn | H8: L1 'This formula defines a unique morphism in $\mathbf C$ once $\nabla$, $q$, and $\xi$ are fixed' belabours the triviality that a formula defines a map; |
| `categorical-dirac-operator` | definition | 2 | 1 | 1 | 0 | 0 | 2 | 1 | 1 | 8 | fail | H4/H5: L6 adds $q^{-1}\nabla$, a map $A\to A\otimes\Omega^1(A)$, to $(1-q^{-1})\iota_\xi\nabla$, a map $A\to A$, and declares the sum $A\to\Omega^1(A)$ — three different targets. |
| `categorical-dirac-operator-unique` | proposition | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 0 | 10 | fail | H8: the proposition says the operator 'is uniquely determined by the formula' and that anything equal to the formula equals it — a tautology stated as a result. |
| `categorical-lagrangian-intro` | prose | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 10 | fail | H4/H5: L1 places $\psi^*\otimes\mathcal D_\nabla\psi$ in $\mathrm{End}_{\mathbf C}(A)$, but $\psi^*\colon A\to\mathbf1$ tensored with $\mathcal D_\nabla\psi\colon\mathbf1\to\Omega^1(A)$ is a map $A\to\Omega^1(A)$. |
| `categorical-lagrangian` | definition | 2 | 1 | 1 | 1 | 0 | 2 | 1 | 1 | 9 | fail | H5: L6 squares $\mathcal D_\nabla$, whose source and target differ ($A\to\Omega^1(A)$), and L8 adds a map $A\to\Omega^1(A)$ to it, while L9 asserts the sum is in $\mathrm{End}_{\mathbf C}(A)$. |
| `categorical-action-intro` | prose | 1 | 1 | 2 | 0 | 1 | 1 | 1 | 1 | 8 | fail | H4/H6: L3 displays the gravity, gauge and matter terms with $R_{\int}$, $\wedge_q$, $\star_q$, $\mathrm{tr}_A$ and a scalar named $\lambda$ (again the block index) — before any is defined (they are de |
| `categorical-action` | definition | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 13 | warn | H4/H5: L6-13 use $\mathrm{ev}_A\colon A^\vee\otimes A\to\mathbf1$ and $\mathrm{coev}_A\colon\mathbf1\to A\otimes A^\vee$, the opposite conventions to def:snake-identity, and the composite $(\mathrm{id |
| `categorical-action-notation` | prose | 2 | 1 | 1 | 0 | 2 | 2 | 1 | 1 | 10 | fail | H4: L3 '$\nabla_{\int}(a)=\int_A(a_{(1)})\otimes a_{(2)}-a\otimes1$' subtracts an element of $A\otimes A$ from one of $\mathbf1\otimes A$; |
| `categorical-action-notation-su2` | example | 2 | 2 | 1 | 1 | 1 | 2 | 1 | 1 | 11 | fail | H8: L3 calls the categorical trace on $\mathrm{End}(\mathcal O(\mathrm{SU}(2)))$ 'the usual matrix trace' $\sum_m\langle j,m\|T\|j,m\rangle$ — $A$ is infinite-dimensional and a single $j$ is fixed with no explanation; |
| `qou-canonical-action` | proposition | 1 | 1 | 2 | 0 | 1 | 1 | 1 | 1 | 8 | fail | H4/H5: L10 equates an operator $\mathcal D_\nabla^2$ with a sum containing a partial trace $\mathrm{tr}_A(F\wedge_q\star_qF)$, and L17-19 then wrap $\int_A\mathrm{tr}_A$ around it again; |
| `canonical-action-obstruction` | remark | 2 | 1 | 1 | 0 | 1 | 2 | 0 | 1 | 8 | fail | H5: L1 'The observability axiom ... ensures that the trace ... |
| `variational-equations-intro` | prose | 2 | 1 | 2 | 1 | 2 | 2 | 1 | 1 | 12 | warn | H8: L1 'to predict a material-dependent torsion phase shift' presents a physical prediction in a section intro without flagging it as the comparison point. |
| `variational-equations` | proposition | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 9 | fail | H8/H6: three field equations are stated with no indication of how they follow (e.g. |
| `wavefront-propagation` | remark | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 0 | 9 | fail | H8: L5 'transported along geodesics of the connection $\nabla$', L8 'the Gaussian beam waist $w_0$ is fixed by $q$', 'At a material boundary, $F_\nabla\ne0$' and 'The on-shell condition eliminates the matter term ... |
| `photon-wavefront-example` | example | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 5 | fail | H4: the torsion phase is called $\tau(y)$ (L8), the paper's symbol for the fibre functor; |
| `categorical-q-ext-deriv` | definition | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 1 | 11 | fail | H1: the same operator $d_q$ is defined in def:substrate-parameter (same formula). |
| `categorical-q-ext-deriv-exists` | proposition | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 0 | 10 | fail | H8: the proposition asserts that an explicit composite of morphisms of $\mathbf C$ 'exists as a morphism in $\mathbf C$' — true by construction, stated as a result. |
| `categorical-q-ext-deriv-unique` | proposition | 0 | 1 | 1 | 2 | 1 | 2 | 0 | 1 | 8 | fail | H1/H7: L14 is a generic 'Archimedean specialisation' paragraph ('real-valued physical observables, real-analytic bounds, transcendental constants ...') appended to a purely algebraic uniqueness statement it does not describe. |
| `fermion-boson-decomposition` | definition | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 10 | fail | H4: $\Delta_q$ (L1) is used without definition; 'the space of particles' names $\ker\Delta_q$ by a physics word. |
| `categorical-point` | definition | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 1 | 12 | warn | H5: L1 defines a point as a morphism $p\colon\mathbf1\to A$ (an element of $A$) and then says it 'corresponds to evaluation at $p\in M$', which is a map $A\to\mathbf1$; |
| `categorical-point-explication` | prose | 1 | 2 | 1 | 1 | 1 | 2 | 2 | 1 | 11 | fail | H1: restates def:categorical-point (point, augmentation ideal, germ). |
| `observation` | definition | 1 | 1 | 1 | 0 | 1 | 2 | 0 | 1 | 7 | fail | H4/H7: the definition requires a state bundle $\mathcal S\to M$, an 'open causal neighbourhood', $\mathrm{Ad}(J^1\mathcal S)$, 'the colour fibre', and a Hopf-coaction formula for $\delta q$, none defined in Chapters 1-2 at this… |
| `observation-physical-roles` | remark | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 12 | warn | H1: repeats L7 of def:observation almost verbatim. H8: 'the observation perturbs $q$, which shifts the Reeb flow, which changes what the next observation reads' is a causal story with no construction behind it; |
| `observation-energy` | proposition | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 0 | 8 | fail | H8: the computation $\hbar_{q+\delta q}-\hbar_q=\delta q/(q(q+\delta q))>0$ (L4) is the monotonicity of $1-1/q$; |
| `two-observer-parallelogram` | remark | 1 | 1 | 1 | 1 | 0 | 2 | 1 | 0 | 7 | fail | H5/H8: L4 forms the commutator $[q_1'(p),q_2'(p)]$ of two values of the substrate parameter, which lives in $\mathrm{End}(\mathbf1)\cong R$, a commutative ring, so the commutator is zero; |
| `germ-commutator-q-curvature` | proposition | 1 | 1 | 2 | 1 | 0 | 2 | 1 | 0 | 8 | fail | H5/H8: L9 '$[\delta q_1,\delta q_2]=F_q$' — increments in $A/\mathfrak m_p^2$, which for the archimedean model $A=C^\infty(M)$ is commutative, so the left side vanishes identically; |
| `q-harmonic-flow` | conjecture | 2 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 11 | fail | H4: $\Delta_q$ here (L6, an operator on the scalar function $q$) is a different object from $\Delta_q=d_q\delta_q+\delta_qd_q$ on forms (def:fermion-boson-decomposition, rem:q-laplacian-interpretation); |
| `observation-fermion-action` | remark | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 0 | 9 | fail | H8: L9 'the Ad action conjugates the antisymmetric component by $G$, mixing the fermionic state with the bosonic eigenspace' — $\mathrm{Sym}^2V$ and $\Lambda^2V$ are $G$-subrepresentations, so the $G$ action does not mix them; |
| `geometric-interpretations-intro` | prose | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 10 | fail | H8/H4: L1 'identifies equilibrium between the spatial environment and internal quantum spin' and 'Coriolis cross-coupling' are metaphors offered as identifications; |
| `vector-calculus-bridge` | remark | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 15 | warn | H4 (minor): L5 'the curl $d\alpha$ on a 1-form' and 'gradient $df$' identify forms with vector fields without the $\sharp$/$\star$ that does it (the curl is $\star d\alpha$ in dimension 3); |
| `q-laplacian-interpretation` | remark | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 13 | warn | H8: L3 'the field $\alpha$ is in equilibrium between its spatial environment and its internal quantum spin' and L7 'A $q$-harmonic form ... |
| `q-codifferential-formula-prop` | proposition | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 10 | fail | H4/H5: L1 writes $d_q=q^{-1}d+(1-q^{-1})\varTheta\wedge\mathcal L_\xi$, a third formula for $d_q$ beside $q^{-1}d+(1-q^{-1})\pi_Vd$ (def:categorical-q-ext-deriv); |
| `q-codifferential-formula` | remark | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 15 | warn | H8 (minor): L2-4 'each operation is replaced by its geometric mirror' presents the adjoint rule as a recipe; |
| `q-laplacian-expansion` | remark | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 14 | warn | H8: the three labels 'classical core', 'quantum spin core', 'interference between macroscopic spatial motion and internal spin' (L3-5) name terms of an operator expansion with physical words that the block does not justify. |
| `q-laplacian-spectral-tower` | proposition | 2 | 1 | 1 | 2 | 1 | 2 | 0 | 0 | 9 | fail | H8: L1 asserts that $\Delta_q$ 'has eigenvalues given by the $q$-integer tower $[k]_q^2$' with no space (forms on which manifold?), no multiplicities, and no argument. |
| `q-laplacian-consumers` | remark | 1 | 1 | 2 | 0 | 1 | 2 | 1 | 1 | 9 | fail | H4/H5: a remark listing uses of the tower in later chapters — '$q$-Navier–Stokes dissipation', 'Markov trace / Gram blocks', 'the lifting obstruction tower caps at $r-1$' — none introduced, with '$[k] |
| `hodge-laplacian-relation` | remark | 2 | 1 | 1 | 2 | 2 | 2 | 1 | 1 | 12 | warn | H8: L1 asserts that $\Delta_q$ is formally self-adjoint and L3 that $\ker\Delta_q$ 'is a well-defined subspace with a canonical complement' — the complement needs Hodge theory (elliptic operator, compactness), not formal self-a… |
| `categorical-lichnerowicz` | proposition | 2 | 1 | 1 | 0 | 1 | 2 | 1 | 0 | 8 | fail | H4: the Dirac operator is written $\mathfrak D_\nabla$ here, $\mathcal D_\nabla$ in its definition and $D_\nabla$ in the notation block — three glyphs, one operator; |
| `q-harmonic-particle` | remark | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 12 | warn | H5: L1 cites 'positive-definiteness of $\Delta_q$' — a positive-definite operator has zero kernel, so there would be no $q$-harmonic forms; |
| `brings-geometric-connection` | remark | 1 | 1 | 1 | 2 | 1 | 2 | 1 | 0 | 9 | fail | H8: L1 promises that the contact structure, Reeb field and $q$ 'reduce to explicit formulas' and 'computable eigenvalue problems' on Bring's surface but gives none. |
| `complex-substrate-interpretation` | remark | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 1 | 10 | fail | H4: L9 writes the root-of-unity specialisation as $q_0=e^{\pi i/\kappa}$, reusing $q_0$ (the calibrated real value) and $\kappa$. |
| `categorical-self-duality` | proposition | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 0 | 10 | fail | H8: L1-7 'Every connection that is a critical point of the categorical Yang–Mills functional is an instanton' — classically false (non-self-dual Yang–Mills critical points exist on $S^4$, Sibner–Sibne |
| `instanton-on-shell` | remark | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 0 | 9 | fail | H4/H5: L4 writes $c_2(A)$ (a Chern class of the algebra object?) where the bundle is $\mathrm{Ad}(A)$, and L7 sets the operator $\mathcal D_\nabla^2$ equal to the number $c_2(A)$. |
| `self-dual-ses` | remark | 2 | 1 | 1 | 1 | 0 | 2 | 1 | 1 | 9 | fail | H5: L1 'The $q$-Hodge star $\star_q$ is an involution on $\Omega^2(A)$' — $\star_q$ maps $\Omega^2\to\Omega^{n-2}$, so this needs $n=4$, while the running $\mathrm{SU}(2)$ calculus has $n=3$ (ex:hodge-su2 says the self-dual spl… |
| `hopf-non-cocommutativity` | remark | 2 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 11 | fail | H4: L1 writes the flip as $\sigma$, the paper's symbol for the Hecke/braid generator $\sigma_i$ (AGENTS §7a); |
| `categorical-dq-squared` | proposition | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 10 | fail | H4: $\omega_V$ 'the curvature of the weight decomposition' and $\wedge_q$ (L4) are undefined; |
| `q-torsion-existence` | remark | 2 | 1 | 1 | 0 | 1 | 2 | 0 | 1 | 8 | fail | H4/H7: in 52 words the remark invokes Legendrian submanifolds, KAM-type persistence, and 'the failure of the Frobenius structure on $H$' — 'Frobenius' here is the integrability theorem, colliding with the paper's Frobenius alge… |
| `quantum-torsion-motivation` | remark | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 0 | 12 | warn | H8: L5 'The spinor sign rule follows. The first $360^\circ$ rotation addresses the physical state in space; |
| `q-heat-equation` | definition | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 10 | fail | H4/H5: L1 takes the archimedean 4-tuple $(\mathbf C,\varTheta,G,\mathcal S)$ as 'a quantum observable universe' (def:quantum-observable-universe is a triple $(\mathbf C,A,\tau)$); |
| `q-heat-equation-elaboration` | remark | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 7 | fail | H8: L1 'The Reeb time $t$ evolves at fixed cosmological time $q$' treats the substrate parameter as a time without construction. |
| `categorical-laplace-transform` | definition | 2 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 6 | fail | H4: $\mathcal L$ collides with the Lagrangian $\mathcal L_q$ of def:categorical-lagrangian; |
| `q-resolvent-properties` | remark | 2 | 1 | 1 | 0 | 0 | 2 | 1 | 1 | 8 | fail | H5: L13 gives the eigenvalues of $\Delta_q$ on the $j$-isotypic part as $[j]_q[j+1]_q(1-q^{-1})^2$, while prop:q-laplacian-spectral-tower gives $[k]_q^2$; |
| `laplace-fourier-wick-rotation` | remark | 2 | 1 | 1 | 0 | 1 | 2 | 1 | 1 | 9 | fail | H4: L7 '$\tau=t+i\varTheta$' reuses $\tau$ (the fibre functor) and $\varTheta$ (the contact form) as complex time and its imaginary part; |
| `q-exp-entire` | proposition | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 14 | warn | H3/H2: the proposition does not say why entireness matters (e.g. |
| `beta-eq-ln-q-dictionary` | proposition | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 13 | warn | H8: L7-19 state as a proposition that $E=-\ln y/\ln q$ solves $e^{-\beta E}=y$, that it reverses order, and that $\sum d_\lambda e^{-\beta E_\lambda}=\sum d_\lambda y_\lambda$ — each true by definition. |
| `q-exponential-realisations` | remark | 2 | 1 | 1 | 0 | 1 | 2 | 0 | 1 | 8 | fail | H4/H7: 'the free grouplike on the primitive generator of the Reeb flow', 'the Habiro ring $\widehat{\mathbb Z[q]}[[x]]$', 'cyclotomic-projection' — heavy, undefined, unframed. |
| `q-exponential-unique` | proposition | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 9 | fail | H1/H8: L8-15 discuss 'the accompanying proof' and which of its steps the hypotheses encode — commentary on a proof inside a proposition; |
| `q-exp-finite-field-obstruction` | remark | 2 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 11 | fail | H8: L1 '$\exp_q$ nonetheless exists as a symbol in the formal Hopf algebra $\mathcal H_q\otimes\mathbb F_p$' is not explained. |
| `q-exp-p-adic` | remark | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 14 | warn | H3: no reason given for the $p$-adic case. H4 (minor): '$[n]_q!$' here is the Jackson factorial of the unbalanced $q$-integers, while prop:q-exp-entire uses balanced ones; |
| `q-logarithm-unique` | proposition | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 9 | fail | H1/H7: L7-16 are commentary on 'the accompanying proof' and on why rigidity 'is not available here', invoking Milnor–Moore unframed. |
| `q-dilogarithm` | definition | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 10 | fail | H5: the definition asserts 'the unique level-2 primitive ... normalised by the pentagon relation', while prop:q-dilogarithm-unique proves uniqueness only under a rigidity hypothesis and prop:q-dilogarithm-exists exhibits the ze… |
| `q-dilogarithm-pentagon-associator` | remark | 0 | 1 | 2 | 1 | 1 | 2 | 0 | 1 | 8 | fail | H1/H7: 478 words covering the pentagon, Faddeev–Kashaev, the modular double, the 'bar-even face that drives mass and binding', the 'bar-odd face carrying the decay observable', a Hopf–Drinfeld pairing and resurgence — far beyon… |
| `q-dilogarithm-exists` | proposition | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 0 | 9 | fail | H8: the proposition states that the structure 'is inhabited' and L6-9 concede the witness is the zero map, which 'satisfies the five-term relation without being the intended solution' — a vacuous existence statement presented a… |
| `q-dilogarithm-unique` | proposition | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 10 | fail | H8: the hypothesis 'the only $f$ satisfying the relation is $f=0$' (L4-11) is the conclusion for differences, so the proposition is a restatement; |
| `dilog-pentagon-is-associator` | proposition | 0 | 1 | 1 | 1 | 0 | 2 | 0 | 0 | 5 | fail | H5/H8: the 'if and only if' (L1-7) holds because a '$q$-dilogarithm datum' is defined as something satisfying the five-term relation (L20 'the reverse reads the datum's five-term field') — a tautology |
| `generating-functions-solve-reeb-flow` | remark | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 0 | 9 | fail | H8: L7 'These three functions are the unique algebraic objects in the Habiro completion satisfying the categorical evolution equations' — no uniqueness result is cited, and prop:q-dilogarithm-unique is conditional. |
| `archimedean-realisation-volume-compatibility` | conjecture | 2 | 0 | 1 | 0 | 1 | 2 | 0 | 1 | 7 | fail | H4/H7: the conjecture uses the Habiro ring, a 'motivic volume class' $\mu(\beta)$ in an undefined $\widehat{\mathcal M}$, a realisation $\mathcal R_{\mathrm{top}}$, $V_0(\beta)$ and $\tau_\infty$ (reusing $\tau$), none defined. |
| `braiding-unit-circle-convention` | remark | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 10 | fail | H5: L1 calls it 'the inside-unit-circle convention' while assigning $q:=\lambda_+$, which L1 then says 'lies outside the unit circle'. |
| `i-as-braiding-orientation` | remark | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 0 | 9 | fail | H8: L1 'The imaginary unit $i$ serves as the orientation of the braiding' and L5 'Negating $i$ equates to flipping the crossing orientation' are identifications with no construction; |
| `affine-chart-origin-of-i-and-q` | remark | 2 | 1 | 1 | 1 | 0 | 2 | 1 | 0 | 8 | fail | H5: L5 '$\rho_{\pi/2}=i\,\mathrm{id}_V$ operates as the square root of $\iota$' — $i\,\mathrm{id}_V$ acts on $V$ while $\iota(z)=z^{-1}$ acts on a chart of $\mathbb P(V)$, and on $\mathbb P(V)$ a scalar acts trivially. |
| `reeb-u1-chart-swap` | proposition | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 10 | fail | H5: L7 'The chart-swap one-parameter subgroup' — the chart swap $z\mapsto z^{-1}$ is an involution, not a one-parameter subgroup; |
| `reeb-u1-five-roles` | remark | 1 | 1 | 1 | 1 | 1 | 2 | 0 | 0 | 7 | fail | H5: item 4 gives the Reeb flow as $Z\mapsto e^{-t}Z$, a real scaling, while prop:substrate-radial-coordinate gives $\mathcal L_\xi Z=J\hbar_qZ$, a rotation. |
| `categorical-coordinate-ring` | proposition | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 10 | fail | H5: L1 takes $q\in R^\times$ (the family is indexed by $q\in R^\times$) and then forms $R[q,q^{-1}]$, which equals $R$ if $q\in R$; |
| `tqft-context` | remark | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 1 | 12 | warn | H8: L3 'The condition $\mathrm{Hom}(\mathbf1,\mathrm{Ad}(A))=0$ acts as the categorical contact condition. |
| `levi-generalisation` | remark | 2 | 1 | 1 | 0 | 1 | 2 | 0 | 0 | 7 | fail | H8/H4: L3 '$q(p)=1+\|\langle L_\varTheta,F_A^+\rangle\|\ge1$' defines the substrate parameter by a curvature pairing — a fourth definition of $q$, unexplained, with $F_A^+$ undefined; |
| `schrodinger-jet-coaction` | remark | 2 | 1 | 1 | 0 | 1 | 2 | 1 | 1 | 9 | fail | H4: $\mathcal S_{\mathrm{lin}}$, $D_A$, $V_q$ (also the letter of the fundamental object) and $\hat H_q$ are undefined; |

## 7. Per-block findings and suggested rewrites

Line numbers refer to the block's `.md` at the corpus commit above. Suggested rewrites are proposals only; derivation bodies are left alone and flagged rather than rewritten.

### Ch 1 — Quantum Universes

#### `quantum-universes-intro` — prose `sec:qou-intro` — T = 13/16 (warn)

- **Scores:** H1 1, H2 2, H3 2, H4 2, H5 1, H6 2, H7 1, H8 2
- **Evidence:** H5: chapter numbering contradicts itself — L15 'imposed in Chapter 2' vs L33 '[Chapter 3](#chap:qou)'. H1/H7: L14-19 digression on duals and which later constructions use them interrupts the roadmap.
- **Suggested rewrite:** Replace L14-19 with: 'Duals are not part of this definition; they enter in Chapter 2 with the quantum observable universe.' Make L33 read 'Chapter 2' (or fix L15) so both refer to the same chapter.

#### `scheme-notation` — prose `sec:scheme-notation` — T = 15/16 (warn)

- **Scores:** H1 2, H2 2, H3 2, H4 1, H5 2, H6 2, H7 2, H8 2
- **Evidence:** H4: L3 '$\mathbb{F}_q$' reuses $q$, the paper's substrate parameter, as a field order.
- **Suggested rewrite:** L3: write '$\mathbb{F}_p$' (or '$\mathbb{F}_{p^k}$') so $q$ keeps one meaning.

#### `rigid-monoidal-intro` — prose `sec:rigid-monoidal-intro` — T = 10/16 (fail)

- **Scores:** H1 1, H2 1, H3 2, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H5/H2: L5 'We keep two examples in view: the polynomial ring $\mathbb{C}[z]$ and the coordinate ring' names algebras, not monoidal categories, then 'Objects have tensor products and a unit over a base ring, making the category $R$-linear' is a non-sequitur (tensor products do not make a category $R$-linear). H7: L1 'Superselection-sector analysis of local observables forces the same' drops a heavy result (Doplicher–Roberts) with no framing; it also duplicates rem:monoidal-justification (H1).
- **Suggested rewrite:** Cut the superselection sentence from L1 (the remark carries it). Rewrite L5: 'Two examples stay in view: finite-dimensional vector spaces $\mathrm{Vect}_{\mathbb{C}}$, and finite-dimensional representations of $\mathrm{SU}(2)$. In each, objects can be tensored and there is a unit; hom-sets are vector spaces, so the category is $\mathbb{C}$-linear. Every object $V$ has a dual $V^\vee$, and a braiding exchanges tensor factors; for these two examples the braiding is the flip, which is symmetric.'

#### `snake-identity` — definition `def:snake-identity` — T = 14/16 (warn)

- **Scores:** H1 2, H2 1, H3 1, H4 2, H5 2, H6 2, H7 2, H8 2
- **Evidence:** H2/H3: the definition gives no instance and no purpose; the reader meets two tikz diagrams before learning what they say in $\mathrm{Vect}$ (L1-33).
- **Suggested rewrite:** Append after L35: 'In $\mathrm{Vect}_{\mathbb{C}}$ with basis $e_i$ and dual basis $e^i$, $\mathrm{coev}(1)=\sum_i e^i\otimes e_i$ and the left identity reads $v=\sum_i e^i(v)\,e_i$: the snake identities are the statement that a basis and its dual basis reconstruct every vector.' Open with one sentence of purpose: 'A dual is an object that can be bent back into an input; the snake identities make bending and unbending inverse.'

#### `rigid-monoidal-category` — definition `def:rigid-monoidal-category` — T = 8/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 1, H5 2, H6 1, H7 0, H8 1
- **Evidence:** H7: one definition block carries monoidal, rigid, $R$-linear, braided, symmetric and exterior-power definitions; L31 'without quasi-zeros' is a technicality with no framing; the exterior power (L33) is unrelated to rigidity. H8 gap: L1 'natural isomorphisms expressing associativity and unitality' omits the pentagon/triangle coherence that makes them a monoidal structure, and L33 names the hexagon axioms without stating them.
- **Suggested rewrite:** Split into: (a) monoidal category with one sentence 'subject to the pentagon and triangle coherence axioms [cite Mac Lane / EGNO §2.1]'; (b) rigid; (c) braided/symmetric with the two hexagon identities displayed; move $\Lambda^k V$ to the block that first uses it. Either drop 'without quasi-zeros' here or add one clause saying what fails without it.

#### `monoidal-justification` — remark `rem:monoidal-justification` — T = 12/16 (warn)

- **Scores:** H1 1, H2 2, H3 2, H4 2, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H7/H8: L5 'The category of superselection sectors is automatically rigid braided monoidal' and 'Locality and covariance force the monoidal structure' assert a deep theorem (Doplicher–Haag–Roberts) as obvious, uncited. H5: L5 opens 'Take an electric charge and its conjugate anticharge.' and the next sentence does not use it. H1: largely repeats sec:rigid-monoidal-intro L1.
- **Suggested rewrite:** Rewrite paragraph 2: 'In algebraic quantum field theory the same structure is a theorem: Doplicher, Haag and Roberts showed that, under locality and covariance, superselection sectors form a rigid braided monoidal category [cite DHR 1971/1974]. Tensor product is composition of charges, the braiding is exchange statistics, and the dual of a charge is its anticharge.' Remove the duplicate sentence from the section intro.

#### `rigid-monoidal-vect` — example `ex:rigid-monoidal-vect` — T = 13/16 (warn)

- **Scores:** H1 2, H2 2, H3 2, H4 2, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H5/H8: L1 'Both arise as representations of a function algebra' is inaccurate as stated — $\mathrm{Vect}_{\mathbb{C}}$ is not the representation category of $\mathbb{C}[z]$, and $\mathrm{Rep}(\mathrm{SU}(2))$ is comodules over $\mathcal{O}(\mathrm{SU}(2))$, not modules. L3 gives ev but not coev, so rigidity is asserted, not shown.
- **Suggested rewrite:** L1: 'Both are categories of comodules over a commutative Hopf algebra: $\mathbb{C}$ (the trivial group) and $\mathcal{O}(\mathrm{SU}(2))$.' Drop the $\mathbb{C}[z]$ sentence or say what role it plays. L3: add 'and $\mathrm{coev}(1)=\sum_i e^i\otimes e_i$ for any basis $e_i$.'

#### `quantum-universe-intro` — prose `sec:quantum-universe-intro` — T = 10/16 (fail)

- **Scores:** H1 1, H2 2, H3 1, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H5: L1 'a quantum universe is a triple $(\mathbf{C},A,\tau)$' omits the differential calculus that sec:qou-intro L14 lists as part of the definition; L1 'The triple is non-empty' (meaning: an instance exists) is imprecise. H8: L5 'The simplicity of the unit object $\mathbf{1}$ forces the uniqueness of the volume form' asserts a result with no indication why. H4: L5 introduces $\omega_1,\omega_2,\omega_3$ with no definition.
- **Suggested rewrite:** L1: 'a quantum universe consists of an $R$-linear braided monoidal category $\mathbf{C}$, a Frobenius–Hopf object $A$, a fibre functor $\tau$, and a differential calculus on $A$; $\mathcal{O}(\mathrm{SU}(2))$ shows the axioms are consistent.' L5: 'Because $\mathrm{End}(\mathbf{1})=R$, any two volume forms differ by a scalar (prop:volume-form-unique).' Name the $\omega_i$ as the left-invariant Maurer–Cartan 1-forms.

#### `quantum-universe` — definition `def:quantum-universe` — T = 7/16 (fail)

- **Scores:** H1 0, H2 1, H3 1, H4 1, H5 1, H6 2, H7 0, H8 1
- **Evidence:** H7/H1: the definition (L1-24) is followed by ~400 words of ground-ring discussion (L26-41) — cyclotomic units, the initial q-generic ring, 'past the archimedean wall' — that the definition itself does not need. H4/H5: axiom 1 (L8) orders 'the Hecke basis of $A$', a notion not defined for a general Frobenius–Hopf object; axiom 3 (L10) says the self-duality is supplied 'in axiom 2', but axiom 2 (L9) states no non-degeneracy. H1: item 2 (L4) and axiom 2 (L9) both declare the Frobenius–Hopf structure.
- **Suggested rewrite:** Keep L1-24 as the definition. Move L26-41 to a follow-on remark 'On the ground ring' (the $\mathbb{Z}[q,q^{-1}]$ cyclotomic example is good material for it). In axiom 1 say what the Hecke basis is or cite where it is defined; in axiom 3 cite the non-degeneracy hypothesis by name. Merge item 2 and axiom 2. Replace the Lean identifier at L38 with the mathematical property ('$q$ and every $\Phi_d(q)$, $d\ge2$, are units').
- **Also:** proof-no-lean-mention-in-prose: L38 names the Lean declaration `QOU.AlgebraicSubstrate.IsQGeneric` and the Lean class `CommRing` in prose.

#### `quantum-universe-axiom-motivation` — remark `rem:quantum-universe-axiom-motivation` — T = 13/16 (warn)

- **Scores:** H1 1, H2 2, H3 2, H4 1, H5 2, H6 2, H7 1, H8 2
- **Evidence:** H1/H7: L19-23 'This axiom is what earlier drafts asserted, less directly, as a numerical identity' leaks drafting history, and the co-Casimir paragraph introduces $\mathrm{tr}_M$ and $C_{\dim_q}$ (H4) with no definition in a remark meant to motivate axioms in 'the loosest terms'.
- **Suggested rewrite:** Delete 'This axiom is what earlier drafts asserted, less directly, as a numerical identity.' Either drop the co-Casimir display or introduce $\mathrm{tr}_M$ as 'the Markov trace' with a one-clause gloss before the formula.
- **Also:** voice: L19 drafting-history leak ('earlier drafts').

#### `tau-notation` — prose `sec:tau-notation` — T = 12/16 (warn)

- **Scores:** H1 1, H2 2, H3 2, H4 1, H5 2, H6 2, H7 1, H8 1
- **Evidence:** H8/H1: three bullets justify the choice of a letter (L3-5) — ceremony. L1 calls $\tau$ 'the forgetful functor' though the definition makes it an abstract fibre functor; L5 'It parameterises the emergence of $R$-modules from the abstract category' is unexplained.
- **Suggested rewrite:** Reduce to: 'We write $\tau$ for the fibre functor, keeping $\omega$ free for differential forms. The letter also recalls Tannaka: the gauge group is $\mathrm{Aut}^{\otimes}(\tau)$.'

#### `frobenius-pairing` — definition `def:frobenius-pairing` — T = 14/16 (warn)

- **Scores:** H1 1, H2 2, H3 2, H4 1, H5 2, H6 2, H7 2, H8 2
- **Evidence:** H4: L18-22 uses $\rho^{-1}$, $\alpha^{-1}$ and $\lambda_A$ for the unitors/associator, while def:rigid-monoidal-category writes the left unitor $\ell_X$; $\lambda$ also indexes Wedderburn blocks. H1: L25 repeats L1 ('recovers the quantum-dimension pairing'), a term never defined.
- **Suggested rewrite:** Write the composite with the unitor names of def:rigid-monoidal-category ($\ell$, $\rho$) or suppress coherence isomorphisms ('suppressing associators and unitors'). Delete L25 or replace with one line saying what the quantum-dimension pairing is.

#### `frobenius-pairing-exists` — proposition `prop:frobenius-pairing-exists` — T = 12/16 (warn)

- **Scores:** H1 1, H2 1, H3 2, H4 2, H5 2, H6 2, H7 1, H8 1
- **Evidence:** H8: L3 'The non-degenerate Frobenius pairing ... exists as a morphism in $\mathbf{C}$. Its adjoint $A\to A^\vee$ is an isomorphism' — existence of the composite is trivial; non-degeneracy is the content, and the block does not say which axiom supplies it. H1: L1 and L3 state the same thing twice.
- **Suggested rewrite:** Single statement: 'Let $(\mathbf{C},A,\tau)$ be a quantum universe. The composite $\int_A\circ\mu$ is non-degenerate: its adjoint $A\to A^\vee$ is an isomorphism.' Then one sentence naming the hypothesis used (the Frobenius–Hopf axiom).

#### `quantum-universe-frobenius-pairing-unique-intro` — prose `sec:quantum-universe-frobenius-pairing-unique-preamble` — T = 11/16 (fail)

- **Scores:** H1 1, H2 1, H3 2, H4 1, H5 1, H6 2, H7 2, H8 1
- **Evidence:** H4/H5: L1 'Pinning the Frobenius pairing on the fundamental object $A$' — the fundamental object is $V$ (def:fundamental-object), $A$ is the Frobenius–Hopf object. L1 'The pairing is unique, forcing its explicit $\mathrm{SU}(2)$ form' overstates (unique up to a scalar). H1/H8: L3-9 numbered roadmap restates the section's block list.
- **Suggested rewrite:** Replace with: 'The Frobenius pairing on $A$ is unique up to a scalar, so its $\mathrm{SU}(2)$ form is canonical once normalised, and every later construction inherits that choice. We prove uniqueness, compute the pairing on $\mathcal{O}(\mathrm{SU}(2))$, and record its role as integration.' Drop the list.

#### `frobenius-pairing-unique` — proposition `prop:frobenius-pairing-unique` — T = 14/16 (warn)

- **Scores:** H1 2, H2 1, H3 2, H4 2, H5 2, H6 2, H7 1, H8 2
- **Evidence:** H7: the hypothesis '$A$ simple' (L1) is the load-bearing one but the block does not say in what sense (simple object of $\mathbf{C}$, or simple algebra) — $\mathcal{O}(\mathrm{SU}(2))$, the running example, is simple in neither naive sense. H2: no instance.
- **Suggested rewrite:** Say which simplicity is meant and add: 'For $A=\mathcal{O}(\mathrm{SU}(2))$ the Frobenius forms are the scalar multiples of Haar integration.'

#### `frobenius-pairing-su2` — example `ex:frobenius-pairing-su2` — T = 13/16 (warn)

- **Scores:** H1 2, H2 2, H3 1, H4 1, H5 1, H6 2, H7 2, H8 2
- **Evidence:** H5: L10 calls the matrix coefficients an 'orthonormal basis' and L14 gives them norm $1/(2j+1)$. H4: L3 defines a bilinear pairing $\int fg$ and calls it 'the $L^2$ inner product', which is sesquilinear; complex conjugation is never notated.
- **Suggested rewrite:** L10: 'orthogonal basis'. L3: 'The Frobenius pairing is the bilinear form $\langle f,g\rangle=\int fg$; the $L^2$ inner product is $\langle \bar f,g\rangle$.'
- **Also:** needs_owner (content, not exposition): with the stated bilinear pairing, L22 $\langle\alpha,\alpha\rangle_A=\int\alpha^2=0$ under Haar measure, not $\tfrac12$; the value $\tfrac12$ is $\langle\alpha,\bar\alpha\rangle_A$. L27-31 coevaluation also pairs $D$ with $\overline{D}$. Derivation not edited; owner to confirm which pairing is intended.

#### `frobenius-geometric-role` — remark `rem:frobenius-geometric-role` — T = 13/16 (warn)

- **Scores:** H1 2, H2 1, H3 2, H4 1, H5 1, H6 2, H7 2, H8 2
- **Evidence:** H4/H5: L3 identifies $\Omega^1(A)$ with 'the Kähler differentials', while sec:quantum-universe-intro and ex:quantum-universe-su2 use the left-invariant calculus — two different modules. L6 'Differentiation and integration are therefore both internal to $A$' does not follow from the preceding sentence.
- **Suggested rewrite:** L3: 'the first-order differential calculus $\Omega^1(A)$' (no 'Kähler'). L6: 'Both operations are morphisms of $\mathbf{C}$ built from $A$ alone.' Add the $\mathrm{SU}(2)$ reading: $d$ is the Maurer–Cartan derivative, $\int_A$ is Haar integration.

#### `quantum-universe-su2` — example `ex:quantum-universe-su2` — T = 13/16 (warn)

- **Scores:** H1 1, H2 2, H3 2, H4 1, H5 2, H6 2, H7 1, H8 2
- **Evidence:** H1/H7: item (v) (L11) is a single 230-word paragraph covering the flip, the $R$-matrix, the Hecke relation, the Haar state and the left-covariant calculus. H4: L9 '$\partial_i f$' is never defined.
- **Suggested rewrite:** Split (v): first two sentences state that the flip is symmetric so axiom 1 fails at $q=1$; a separate paragraph introduces $\mathrm{Rep}(\mathrm{SU}_q(2))$ and $\check R(q)$. L9: '$\partial_i$ the left-invariant vector fields dual to $\omega_i$'.

#### `higher-forms` — definition `def:higher-forms` — T = 11/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 1, H5 1, H6 2, H7 2, H8 2
- **Evidence:** H5/H4: L7 'For an object $V$, $\Lambda^k V$ denotes its $k$-th exterior power' is unrelated to the forms being defined and introduces notation the block never uses. H2/H3: no purpose stated and no instance before the de Rham diagram.
- **Suggested rewrite:** Delete the $\Lambda^k V$ sentence. Open with: 'Forms of every degree let us state curvature ($d^2$ of a connection) and volume (top forms).' Point to ex:higher-forms-su2 in the first paragraph.

#### `higher-forms-su2` — example `ex:higher-forms-su2` — T = 12/16 (warn)

- **Scores:** H1 2, H2 2, H3 1, H4 1, H5 1, H6 2, H7 2, H8 1
- **Evidence:** H4/H5: L1 writes $\Omega^1(A)=\mathrm{span}\{\omega_i\}$ and L4 writes $\Omega^1(A)=A\otimes\mathrm{span}\{\omega_i\}$. H8: L9 the structure equation $d\omega_i=-\tfrac12\epsilon_{ijk}\omega_j\wedge\omega_k$ arrives with no source (Maurer–Cartan) or normalisation of the $\omega_i$.
- **Suggested rewrite:** L1: '$\Omega^1(A)$ is the free $A$-module on the left-invariant forms $\omega_1,\omega_2,\omega_3$.' L9: 'The Maurer–Cartan equation, with $\omega_i$ dual to the basis $\tfrac{i}{2}\sigma_i$ of $\mathfrak{su}(2)$, gives $d\omega_i=\dots$'.

#### `fundamental-object` — definition `def:fundamental-object` — T = 11/16 (fail)

- **Scores:** H1 2, H2 2, H3 1, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H8: L7 'Under a fibre functor the volume constraint forces $\mathrm{rank}(V)=2$' states a theorem without its source and before the volume constraint is defined. H4: $\epsilon$ is typed $V\otimes V\to\mathbf{1}$ (L3) and then as $\Lambda^2V\to\mathbf{1}$ (L5); the coform is called $\eta$, the Hopf unit's symbol. H5: L7 'every other simple object is an exterior or symmetric power of $V$' — for $\mathrm{SU}(2)$ the exterior powers above degree 2 vanish; only symmetric powers occur.
- **Suggested rewrite:** L5: 'an antisymmetric form $\epsilon\colon V\otimes V\to\mathbf 1$ (it factors through $\Lambda^2V$)'; rename the coform (e.g. $\epsilon^\vee$). L7: 'Once the volume constraint is imposed (Chapter 2) a fibre functor sends $V$ to a rank-2 module (prop:...); in $\mathrm{SU}(2)$, $V=\mathbb{C}^2$ and every simple object is a symmetric power $\mathrm{Sym}^n V$.'

#### `tannaka-dual` — definition `def:tannaka-dual` — T = 14/16 (warn)

- **Scores:** H1 2, H2 1, H3 2, H4 2, H5 2, H6 2, H7 1, H8 2
- **Evidence:** H7: L5 invokes Deligne's neutral-Tannakian reconstruction 'over $R$', but Deligne's theorem is over a field; the hypothesis needed over a ring is not stated. H2: no instance ($G=\mathrm{SU}(2)$ for $\tau$ the forgetful functor on $\mathrm{Rep}(\mathrm{SU}(2))$).
- **Suggested rewrite:** L5: 'When $R$ is a field and $(\mathbf C,\tau)$ is neutral Tannakian, Deligne's theorem gives ...; over a general ring we use only the group-valued functor $\mathrm{Aut}^\otimes(\tau)$.' Add: 'For the forgetful functor on $\mathrm{Rep}(\mathrm{SU}(2))$, $G=\mathrm{SU}(2)$.'

#### `unit-simplicity` — remark `rem:unit-simplicity` — T = 12/16 (warn)

- **Scores:** H1 1, H2 1, H3 2, H4 2, H5 1, H6 2, H7 2, H8 1
- **Evidence:** H5/H8: L3 'The space ... $\mathrm{Hom}(\Lambda^2V,\mathbf 1)$ is one-dimensional over $R$. This follows because $\mathrm{End}(\mathbf 1)\cong R$' — the conclusion also needs $\Lambda^2V\cong\mathbf 1$, which is not mentioned. L5 'Once chosen, the gauge symmetries lock it in place' has no content.
- **Suggested rewrite:** L3: 'Since $\Lambda^2V\cong\mathbf 1$ and $\mathrm{End}(\mathbf 1)\cong R$, $\mathrm{Hom}(\Lambda^2V,\mathbf 1)$ is free of rank one, so any other non-degenerate form is $c\,\epsilon$ with $c\in R^\times$.' Replace L5 with the $\mathrm{SU}(2)$ instance: $\epsilon$ is the determinant, fixed up to scale.

#### `hochschild-homology` — definition `def:hochschild-homology` — T = 12/16 (warn)

- **Scores:** H1 1, H2 1, H3 1, H4 2, H5 2, H6 2, H7 1, H8 2
- **Evidence:** H2/H3: the definition opens with $\mathrm{Tor}^{A^e}$ (L6) and only at L19 says why the paper needs it (traces live in $HH_0$); no small example ($\mathbb{C}[x]$ or $M_n(\mathbb C)$) anchors it. H7: the Hochschild-cohomology and deformation digression (L17) is not used here.
- **Suggested rewrite:** Open with L19's point: 'Every trace in this paper factors through $A/[A,A]$; Hochschild homology is the derived version of that quotient.' Add: 'For $A=M_n(\mathbb C)$, $HH_0=\mathbb C$ via the ordinary trace; for $A=\mathbb C[x]$, $HH_1=\mathbb C[x]\,dx$.' Move the $HH^n$ sentence to where deformations are used.
- **Also:** proof-no-lean-mention-in-prose: L19 names `HochschildZero R A`, `hochschildClass_mul_comm`, `traceOnHochschildZero` and 'the Lean sibling'.

#### `grothendieck-group-of-a-qou` — definition `def:grothendieck-group-of-a-qou` — T = 13/16 (warn)

- **Scores:** H1 1, H2 2, H3 2, H4 1, H5 1, H6 2, H7 2, H8 2
- **Evidence:** H5: L11 defines $\dim_q$ via the trace 'of a rigid monoidal category', but a quantum universe need not be rigid (def:quantum-universe L24); and L19 asserts $\dim_q[V_n]=[n+1]_q$ for the classical $\mathrm{Rep}(\mathrm{SU}(2))$, where the dimension is $n+1$. H4: 'rank' (L11) for the number of simple constituents clashes with module rank used elsewhere.
- **Suggested rewrite:** L11: 'When $\mathbf C$ is rigid, the quantum dimension ...'. L19: '... the rank of $[V_n]$ is $1$ and its dimension is $n+1$; in $\mathrm{Rep}(\mathrm{SU}_q(2))$ the quantum dimension is $[n+1]_q$.' Call the count 'length'.

#### `chern-character` — definition `def:chern-character` — T = 12/16 (warn)

- **Scores:** H1 1, H2 1, H3 2, H4 1, H5 2, H6 2, H7 1, H8 2
- **Evidence:** H7/H1: L31 ends with a defensive aside about the base curve's Euler characteristic that the definition does not need. H4: L11 places $p_\lambda$ in $\mathrm{End}(A)$ and then identifies $[p_\lambda]=[\mathrm{id}_{V_\lambda}]$ in $HH_0(\mathbf C)$ without saying how the algebra idempotent becomes a categorical identity. H2: the concrete instance is deferred to the next block.
- **Suggested rewrite:** Delete the last two sentences of L31. L11: 'the classes $[\mathrm{id}_{V_\lambda}]$ of the simple objects span $HH_0(\mathbf C)$' (drop $p_\lambda$ or state the correspondence). Add one line: 'For $\mathrm{Rep}(\mathrm{SU}(2))$, $\mathrm{ch}$ is the character (ex:su2-characters-and-quantum-dimension).'
- **Also:** proof-no-lean-mention-in-prose: L31 'proved in the Lean carrier (`dimQK0_eq_evDimQ_chernCharacter`)'.

#### `su2-characters-and-quantum-dimension` — example `ex:su2-characters-and-quantum-dimension` — T = 14/16 (warn)

- **Scores:** H1 1, H2 2, H3 2, H4 2, H5 2, H6 2, H7 1, H8 2
- **Evidence:** H7/H1: L19 adds two 'consequences' — that $-6$ cannot be a quantum dimension, and a divergent-series remark about $\mathcal O(\mathrm{SU}(2))$ — that serve later chapters' arguments, not this example.
- **Suggested rewrite:** End the example at '...the evaluation of a class function at the pivotal element.' Move the positivity remark and the divergent-series remark to the block on the base curve where they are used.
- **Also:** proof-no-lean-mention-in-prose: L17 'The Lean sibling proves ... `su2Character_one` ...'.

#### `qu-consequences-intro` — prose `sec:qu-consequences-intro` — T = 11/16 (fail)

- **Scores:** H1 1, H2 2, H3 2, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H4/H5: L1 introduces the Hopf comultiplication 'built from the group-multiplication rule' and L3 the Frobenius comultiplication $\Delta_\mu$ 'dual to $\mu$', and L1 says both 'follow directly from the Frobenius pairing' — the two coproducts are conflated. H8: L5 'the QU axioms are independent over arbitrary rings' is asserted with no gloss.
- **Suggested rewrite:** L1: 'Two coproducts appear: the Hopf coproduct $\Delta$ (from group multiplication) and the Frobenius coproduct $\Delta_\mu$ (dual to $\mu$). This section concerns $\Delta_\mu$.' L5: 'Finally, no QU axiom follows from the others (prop:axiom-independence).'

#### `frobenius-relation` — proposition `prop:frobenius-relation` — T = 11/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 2, H5 1, H6 1, H7 2, H8 1
- **Evidence:** H5: L1 'This compatibility makes $A$ a Frobenius algebra' — no compatibility has been stated yet. H6/H8: L22 'Sliding a multiplication past a comultiplication yields the same result as composing them' does not say what the diagram asserts; the second (mirror) Frobenius relation is not mentioned.
- **Suggested rewrite:** L1: 'Let $\Delta_\mu$ be the coproduct dual to $\mu$ under the Frobenius pairing.' After the diagram: 'Read on elements: multiplying by $a$ and then splitting equals splitting and then multiplying the left factor by $a$. Together with its mirror image, this is what it means for $A$ to be a Frobenius algebra.' Point to ex:frobenius-relation-su2 for the $\mathrm{SU}(2)$ check.

#### `frobenius-relation-su2` — example `ex:frobenius-relation-su2` — T = 14/16 (warn)

- **Scores:** H1 2, H2 2, H3 1, H4 2, H5 2, H6 2, H7 2, H8 1
- **Evidence:** H8: L9 concedes that for $\mathrm{SU}(2)$ $\Delta_\mu(f)$ is 'a distribution', i.e. not an element of $A\otimes A$, but the verification (L11-16) then proceeds as if it were, without saying in what space the relation is being checked. H3: L1 gives no purpose beyond 'we verify'.
- **Suggested rewrite:** After L9 add: 'So for the compact group the relation is checked in the space of distributions on $\mathrm{SU}(2)^2$; for a finite group the same computation is an identity in $A\otimes A$.'
- **Also:** needs_owner (content): L9 itself shows $\Delta_\mu$ does not land in $A\otimes A$ for $A=\mathcal O(\mathrm{SU}(2))$, so this $A$ is not a Frobenius algebra in $\mathrm{Vect}$ in the finite sense prop:frobenius-relation needs. Derivation not edited.

#### `involutive-structure` — definition `def:involutive-structure` — T = 9/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 1, H5 2, H6 1, H7 1, H8 1
- **Evidence:** H6/H1: three tikz diagrams (L6-41) restate one-line equations; the monoidal-compatibility square (L17-26) is mistyped — $(\mathrm{id}\otimes f)^\dagger$ is drawn $X\otimes Y\to X\otimes Z$, the direction of $\mathrm{id}\otimes f$. H4: L43 applies the antipode $S$ (a map on elements of $A$) to a morphism $f$. H3/H2: no purpose and no instance (conjugate transpose in $\mathrm{Vect}_{\mathbb C}$).
- **Suggested rewrite:** State the four axioms as displayed equations only, including $(f\otimes g)^\dagger=f^\dagger\otimes g^\dagger$. Open with: 'An involutive structure is the categorical form of the adjoint of a linear map; in $\mathrm{Vect}_{\mathbb C}$ with inner products it is $f\mapsto\bar f^{T}$.' Rewrite L43 to say on which morphisms the formula is defined.

#### `positive-definite-dagger` — proposition `prop:positive-definite-dagger` — T = 11/16 (fail)

- **Scores:** H1 2, H2 1, H3 2, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H5: L9 'The Frobenius dagger satisfies $S^2=\mathrm{id}$ and restricts to $S=\dagger$ on $\mathrm{End}(\mathbf 1)$' — a property of $S$ is attributed to $\dagger$, and 'restricts to $S=\dagger$' does not parse. H4: L1 writes the quantum universe as a pair $(\mathbf C,A)$; 'formally-real ordered field' is redundant. H7: why the antipode must be self-adjoint and pivotal is not said.
- **Suggested rewrite:** L9: 'Under these hypotheses $S^2=\mathrm{id}$, $\dagger$ is an involutive structure, and for every non-zero $f\colon\mathbf 1\to X$ the scalar $f^\dagger\circ f\in R$ is positive.' L1: '$(\mathbf C,A,\tau)$ ... $\mathrm{End}(\mathbf 1)\cong R$ an ordered field'.

#### `positive-dagger-su2` — example `ex:positive-dagger-su2` — T = 12/16 (warn)

- **Scores:** H1 2, H2 2, H3 1, H4 1, H5 1, H6 2, H7 1, H8 2
- **Evidence:** H5: the proposition concerns $f\colon\mathbf 1\to X$ (prop:positive-definite-dagger L9) but the example tests endomorphisms of $V$ (L7); L7 'For any endomorphism' then L13 'By Schur's lemma, $f=\lambda\,\mathrm{id}$' holds only for intertwiners. H7: L15 '$C^*$-tensor category ... the categorical shadow of the compactness of $\mathrm{SU}(2)$' is a heavy claim with no framing.
- **Suggested rewrite:** L7: 'For a morphism $f\colon\mathbf 1\to V^{\otimes 2}$ (an invariant vector $v$), $f^\dagger f=\|v\|^2>0$.' or say 'for any intertwiner'. L15: 'This positivity is what makes $\mathrm{Rep}(\mathrm{SU}(2))$ a $C^*$-tensor category; it uses the invariant inner product, which exists because $\mathrm{SU}(2)$ is compact.'

#### `dagger-notation` — remark `rem:dagger-notation` — T = 14/16 (warn)

- **Scores:** H1 2, H2 2, H3 1, H4 1, H5 2, H6 2, H7 2, H8 2
- **Evidence:** H4: L5 writes the physicist's adjoint as $A^\dagger_{\mathrm{phys}}$, reusing $A$, the Frobenius–Hopf object. L3 'derived from the Frobenius pairing' omits the antipode that the formula uses.
- **Suggested rewrite:** L5: '$T^\dagger_{\mathrm{phys}}$ ... for an operator $T$'. L3: 'built from the antipode and the Frobenius pairing'.

#### `tannaka-krein-overview` — remark `rem:tannaka-krein-overview` — T = 11/16 (fail)

- **Scores:** H1 1, H2 1, H3 2, H4 1, H5 2, H6 2, H7 1, H8 1
- **Evidence:** H8/H7: L5 'Any two fibre functors are isomorphic' is false as a general statement (it holds over an algebraically closed field, or fpqc-locally); presented without hypothesis or citation. H4: L8 'the CAL-2 calibration' is project jargon undefined for the reader; 'Woronowicz's reconstruction' is uncited.
- **Suggested rewrite:** L5: 'Over an algebraically closed field any two fibre functors are isomorphic, so $G$ is determined up to inner automorphism [Deligne 1990].' L8: 'The numerical value $q_0$ is an input calibrated against experiment (§...), not a consequence of the axioms.' Cite Woronowicz 1988.

#### `axiom-independence` — remark `rem:axiom-independence` — T = 14/16 (warn)

- **Scores:** H1 2, H2 2, H3 2, H4 2, H5 1, H6 2, H7 2, H8 1
- **Evidence:** H5: L3 argues that the fibre functor is not supplied by Deligne's theorem, which bears on the fibre-functor datum, not on axiom 1 (well-founded braiding order); no model is given where axiom 1 fails and the others hold. H8: L13 'In full generality, all four axioms are independent' concludes more than the paragraphs show.
- **Suggested rewrite:** Replace L3 with a model: 'The symmetric category $\mathrm{Rep}(\mathrm{SU}(2))$ satisfies axioms 2–4 but not axiom 1 (ex:quantum-universe-su2(v)).' End: 'Each axiom fails in a model of the other three.'

#### `qu-structures-intro` — prose `sec:qu-structures-intro` — T = 7/16 (fail)

- **Scores:** H1 1, H2 1, H3 2, H4 0, H5 1, H6 1, H7 0, H8 1
- **Evidence:** H4/H7: a 300-word section intro introduces $\nabla$, $F_\nabla$, $\mathrm{Ad}(A)$, $J^1(A)=A\otimes_{\mathbf C}\Omega^1(A)$, $\star$, $\alpha^*$, $\mathrm{vol}$, $\pi$, $[\pi,\pi]_{\mathrm{SN}}$ and the HKR map — formulas that the following definitions restate. L3 gives $J^1(A)$ both as a tensor product and as the middle term of an extension; L7 'the skew-Poisson structure of formal-group integration' is unexplained. H8: L3 'Every QU admits such a $\nabla$' and L5 '$\star^2=\mathrm{id}$' are asserted without hypotheses.
- **Suggested rewrite:** Cut to a roadmap with no formulas: 'This section builds differential geometry from the QU data alone: a connection and its curvature; the jet object, which packages a function with its first derivative; a Hodge star, built from the Frobenius form and a volume form; and an internal Poisson bracket, the first-order shadow of deforming $q$. On $\mathrm{SU}(2)$ these are the Maurer–Cartan connection, first jets, the Hodge star of the round metric, and the Poisson–Lie bracket.'

#### `categorical-connection` — definition `def:categorical-connection` — T = 14/16 (warn)

- **Scores:** H1 2, H2 2, H3 1, H4 2, H5 2, H6 1, H7 2, H8 2
- **Evidence:** H6: the Leibniz triangle (L7-14) is labelled '$\nabla\otimes1+1\otimes\nabla$' but its target is $A\otimes\Omega^1(A)$, so the diagonal arrow needs a multiplication the label omits; the displayed rule (L3) carries the content better than the diagram. H3: no purpose stated before the definition.
- **Suggested rewrite:** Open: 'A connection is a derivative that obeys the product rule; its failure to square to zero is curvature.' Drop the triangle or label the diagonal '$(\mu\otimes1)(1\otimes\nabla)+(\nabla\cdot)$' explicitly.

#### `categorical-connection-exists` — proposition `prop:categorical-connection-exists` — T = 11/16 (fail)

- **Scores:** H1 1, H2 1, H3 2, H4 1, H5 1, H6 2, H7 2, H8 1
- **Evidence:** H4/H5: L3 types the connection as $\nabla\colon A\to\Omega^1(A)$, while def:categorical-connection has $\nabla\colon A\to A\otimes\Omega^1(A)$. L1 calls $A$ 'the observable algebra' in a chapter where the universe is not yet observable, and 'carries the same differential geometry as a bundle with connection' overclaims.
- **Suggested rewrite:** Statement: 'Every quantum universe admits a categorical connection $\nabla\colon A\to A\otimes\Omega^1(A)$.' Motivation: 'On $\mathrm{SU}(2)$ the universal derivation $d$ is one; the proposition says a connection exists in general.'

#### `categorical-connection-su2` — example `ex:categorical-connection-su2` — T = 12/16 (warn)

- **Scores:** H1 2, H2 2, H3 1, H4 2, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H8: L34 'Since $\mathrm{SU}(2)\cong S^3$ is connected, all monodromy is trivial' — triviality of monodromy of a flat connection needs simple connectivity. H5/H7: the block computes a $\mathfrak{su}(2)$-valued form but never says how it is a morphism $A\to A\otimes\Omega^1(A)$; L34 'the natural transformation implementing parallel transport' is unexplained.
- **Suggested rewrite:** L34: 'Since $\mathrm{SU}(2)\cong S^3$ is simply connected, a flat connection has trivial holonomy.' Add after L3: 'As a categorical connection, $\nabla f=df=\sum_i(\partial_i f)\,\omega_i$; $\varTheta$ records the same data as a matrix of forms.'

#### `categorical-jet` — definition `def:categorical-jet` — T = 10/16 (fail)

- **Scores:** H1 2, H2 1, H3 2, H4 0, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H4/H5: L4 defines $J^1(A):=A\otimes_{\mathbf C}\Omega^1(A)$ (tensor 'over' a category), yet the extension at L13 has $A\otimes\Omega^1(A)$ as a proper subobject of $J^1(A)$ with quotient $A$ — the two descriptions of $J^1(A)$ are incompatible. L7 takes $\Omega^1(A)=\ker\mu$ (universal differentials) and calls it 'Kähler', while the running example uses the left-invariant calculus. L1 says 'along the connection' but $\nabla$ is never used.
- **Suggested rewrite:** Define $J^1(A)$ once, as the extension: 'the middle term of $0\to\Omega^1(A)\to J^1(A)\to A\to0$, split by $a\mapsto(a,da)$'. Add the classical picture: 'for $A=C^\infty(M)$, $J^1$ is the bundle of first jets, a function with its differential at each point.' Drop 'along the connection' or use $\nabla$ in the splitting.

#### `categorical-hodge-star` — definition `def:categorical-hodge-star` — T = 8/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 1, H5 1, H6 1, H7 1, H8 1
- **Evidence:** H4: $n$ (L1) is never defined; $\alpha^*=S(\alpha)$ (L20) applies the antipode of $A$ to a form; 'involution $\star\colon\Omega^k\to\Omega^{n-k}$' cannot be an involution unless $k=n-k$. H8/H7: L20 '$\star^2=\mathrm{id}$ follows from the non-degeneracy of $\int_A$ and the involutivity of the antipode' — in general $\star^2=\pm1$ depending on degree and signature; the claim is waved through. H6: a tikz square (L9-17) restates $\star^2=\mathrm{id}$.
- **Suggested rewrite:** Open with the classical case: 'On an oriented Riemannian $n$-manifold, $\star$ is defined by $\alpha\wedge\star\beta=\langle\alpha,\beta\rangle\mathrm{vol}$; we replace the metric by the Frobenius form.' Define $n$ as the top degree of $\Omega^\bullet(A)$; call $\star$ an isomorphism and state $\star\star$ with its sign, or restrict to the case proved. Delete the square.

#### `hodge-su2` — example `ex:hodge-su2` — T = 12/16 (warn)

- **Scores:** H1 1, H2 2, H3 1, H4 1, H5 2, H6 2, H7 1, H8 2
- **Evidence:** H1/H4: L7 discusses self-dual 2-forms, which do not arise in dimension 3, and refers to '$\dim H=4$' with $H$ undefined. H3: no statement of why the example matters (the classical cross-product correspondence).
- **Suggested rewrite:** Replace L7 with: 'This is the classical identification of 1-forms with 2-forms on a 3-manifold, the one behind the cross product.' Drop the self-dual sentence.

#### `poisson-object` — definition `def:poisson-object` — T = 9/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H5/H8: L11 'The Frobenius self-duality $A\cong A^\vee$ induces an identification $\Omega^1(A)^\vee\cong\Omega^1(A)$' — self-duality of $A$ does not imply self-duality of $\Omega^1(A)$. H4: $\pi$ is defined twice (L6, L19), and the bracket diagram pairs $\pi\in\Omega^2(A)$ with $\Omega^2(A)$ via '$\langle\pi,-\rangle$' without saying what pairing. $\Omega^1(A)^\vee$ requires duals, which a quantum universe need not have. H2/H3: no instance; L1 'We equip...' gives no reason.
- **Suggested rewrite:** Open: 'On a manifold a Poisson bracket is a bivector $\pi$ with $\{f,g\}=\pi(df,dg)$; for $\mathrm{SU}(2)$ the Poisson–Lie bracket is the first-order trace of $q$.' Add the hypothesis 'assume $\Omega^1(A)$ is dualisable'. Keep one definition of $\pi$; move the 'construction via pullback' to a remark with its extra hypothesis stated.

#### `poisson-hkr-connection` — remark `rem:poisson-hkr-connection` — T = 7/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 0, H5 1, H6 2, H7 0, H8 1
- **Evidence:** H4/H7: in 190 words the remark introduces $\mathrm{Mod}(\mathbb F_p)$, $\mathcal O(H)$, $\pi_<$, $HH^2(\mathcal U_q,\mathrm{Ad})$, $\phi_1$, $\Gamma(\Lambda^2T_A)$ and a 'non-commutative formal group $G/\mathbb Z_p$', none defined here. HKR is invoked as an isomorphism on $HH^2(A,A)$ (L6) without its smoothness hypothesis, for an algebra that at $q\neq1$ is noncommutative (def:hochschild-homology L21 says HKR then fails).
- **Suggested rewrite:** Reduce to the one point: 'Classically, a first-order deformation of a commutative algebra is a Hochschild 2-class, and for smooth $A$ the HKR theorem identifies it with a bivector [Loday]. The internal Poisson object is that bivector, defined inside $\mathbf C$ without passing through $\tau$.' Move the $\mathbb F_p$ model to the skew-Poisson chapter.

#### `outro-quantum-universes` — prose `None` — T = 11/16 (fail)

- **Scores:** H1 1, H2 2, H3 2, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H5: L3 says the next chapter adjoins 'the substrate parameter $q$ and the Reeb derivation $\xi$', but sec:qou-definition-intro says Chapter 2 imposes rigidity, non-degenerate integration, observability, measurability and the volume constraint; def:quantum-universe L28 says $q$ is emergent, not adjoined. L1 calls the Poisson bracket 'the concrete payoff of this chapter', which the chapter never presents as its goal.
- **Suggested rewrite:** L1: 'This chapter built the quantum universe and the differential vocabulary it supports: connection, jets, Hodge star, internal Poisson bracket.' L3: 'Chapter 2 adds rigidity, observability, measurability and the volume constraint, which together force the gauge group to be $\mathrm{SU}(2)$.'

#### `simple-objects-V` — remark `rem:simple-objects-V` — T = 10/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 0, H6 2, H7 2, H8 1
- **Evidence:** H5: L3 'X is simple if and only if $\tau(X)$ is a simple module' contradicts L5, where the simple object $V$ has $\tau(V)$ a rank-2 free module (not simple). L5 conflates categorical dimension with module rank.
- **Suggested rewrite:** L3: 'A faithful exact $\tau$ detects zero objects and isomorphisms; simplicity of $X$ is a statement in $\mathbf C$, not about $\tau(X)$.' L5: '$\tau(V)$ is free of rank 2, so $V$ has dimension 2.' Give $V=\mathbb C^2$ in $\mathrm{Rep}(\mathrm{SU}(2))$.
- **Also:** needs_owner (content): L3's 'iff τ(X) is a simple module' is false in the running example (τ(V)=C^2).

### Ch 2 — Quantum Observable Universes

#### `qou-definition-intro` — prose `sec:qou-definition-intro` — T = 13/16 (warn)

- **Scores:** H1 2, H2 1, H3 2, H4 2, H5 1, H6 2, H7 2, H8 1
- **Evidence:** H5: L1 'the QOU on $\mathrm{SU}(2)$ exactly satisfies these constraints over an arbitrary commutative ring', but ex:quantum-universe-su2(v) shows classical $\mathrm{SU}(2)$ (symmetric braiding) does not satisfy the well-ordering axiom; the claim needs $\mathrm{SU}_q(2)$. H8: 'identifying the categorical arrow of time' presents a physical reading as a result.
- **Suggested rewrite:** '...closes by checking the axioms on $\mathrm{Rep}(\mathrm{SU}_q(2))$.' 'We then show that a non-symmetric braiding well-orders the Hecke basis; remark ... reads this order as time.'

#### `quantum-observable-universe` — definition `def:quantum-observable-universe` — T = 8/16 (fail)

- **Scores:** H1 0, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H1/H7: L24-44 is a 20-line editorial note on how 'earlier statements of this definition' read condition 5, with a dimension table and a Lean file path — material for a remark, not the definition. H5: condition 4 (L6) uses categorical Chern classes $c_1,c_2$ before they are defined; L1 calls $\tau$ 'the forgetful functor' and re-requires faithfulness already in def:quantum-universe. H4: the diagram marks $\epsilon$ as an epimorphism (two heads) while the text requires an isomorphism.
- **Suggested rewrite:** Keep L1-22 with: '$\tau$ the fibre functor'; condition 4 citing def:categorical-chern-classes; condition 5's arrows drawn as isomorphisms. Move L24-44 to a remark 'Why an isomorphism in condition 5', stated as mathematics: 'an epimorphism $\Lambda^2V\to\mathbf1$ allows $\mathrm{rank}\,V=N\ge2$; an isomorphism forces $\binom N2=1$, i.e. $N=2$, and only then is $\epsilon$ a determinant.'
- **Also:** proof-no-lean-mention-in-prose: L34-36 cite `lean/QOU/BraidsAndKnots/VolumeConstraintForcesFibreTwo.lean` and two Lean lemma names; L24 drafting-history leak ('Earlier statements of this definition').

#### `qou-axioms-physical-reading` — remark `rem:qou-axioms-physical-reading` — T = 13/16 (warn)

- **Scores:** H1 1, H2 2, H3 2, H4 2, H5 2, H6 2, H7 1, H8 1
- **Evidence:** H8: L11 'The vanishing of $c_1$ makes the adjoint bundle orientable' — orientability is governed by $w_1$, and a complex bundle is always orientable; 'the vanishing of $c_2$ stops the volume form acquiring a phase around a non-contractible loop' is not a standard consequence and is not argued. H7: 'the non-abelian Stokes theorem' is invoked unframed.
- **Suggested rewrite:** L11: 'Vanishing Chern classes are an anomaly-freedom condition: they are the obstructions to the adjoint bundle being topologically trivial (prop:...). With them the non-abelian Stokes theorem applies, so surface-ordered integrals are independent of the chosen surface.'
- **Also:** needs_owner (content): L11's physical gloss of c_1 (orientability) and c_2 (phase around loops) needs checking.

#### `qou-exists-axiom-3` — lemma `lem:qou-exists-axiom-3` — T = 8/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 1, H5 1, H6 2, H7 0, H8 1
- **Evidence:** H5: titled 'Axiom 3' but def:quantum-observable-universe numbers Chern-class vanishing as condition 4 (Observability is 3). H7: L8 replaces the base category by $\mathbf{Rep}_k(\widehat{\mathfrak g})$ 'at level $k=\langle c_2,[M]\rangle$' — a heavy construction, with $M$ and $P$ undefined, in a lemma statement. H8: with $c_i(\mathrm{Ad}(A)):=c_i(\tau(\mathrm{Ad}(A)))$ the statement reduces to the hypothesis; the block does not say what is being proved.
- **Suggested rewrite:** Retitle 'Condition 4 (measurability)'. State: 'If the classical adjoint bundle has $c_1=c_2=0$, then the categorical Chern classes of $\mathrm{Ad}(A)$ vanish.' Move the level-$k$ sentence to a remark with $M$ and the WZW category introduced.

#### `braiding-induced-ordering` — proposition `prop:braiding-induced-ordering` — T = 11/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 2, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H5: L1 defines $\prec_c$ from the braiding, then L1's last sentence asserts well-foundedness of 'the degree-lexicographic order on reduced positive braid monomials' without saying this is $\prec_c$. H8: 'thereby identifying the categorical arrow of time' is a physical reading stated as part of a proposition.
- **Suggested rewrite:** 'If $c_{V,V}^2\ne\mathrm{id}$, ordering reduced positive braid monomials by degree and then lexicographically defines a well-ordering $\prec_c$ on the basis of $H_n(q)$.' Move 'arrow of time' to a remark.

#### `fibre-functor-rigidity` — remark `rem:fibre-functor-rigidity` — T = 10/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H4: L1 'a rigid, passive role' reuses 'rigid', a defined term (duals). H8/H5: L1 'Tannaka–Krein reconstruction pins the functor uniquely up to natural isomorphism' — Tannaka–Krein reconstructs the group from the functor; it does not make the functor unique, and killing infinitesimal automorphisms is not the same as uniqueness.
- **Suggested rewrite:** 'Observability, $\mathrm{Hom}(\mathbf1,\mathrm{Ad}(A))=0$, says $\tau$ has no infinitesimal automorphisms beyond those of the gauge group: the zeroth adjoint cohomology vanishes. So $\tau$ is rigid in the deformation-theoretic sense.' Drop the Tannaka sentence or state what it adds.

#### `emergence-intro` — prose `sec:emergence-intro` — T = 12/16 (warn)

- **Scores:** H1 2, H2 1, H3 2, H4 2, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H5: L1 'the four axioms of the quantum observable universe' — def:quantum-observable-universe lists five conditions. H8: L1 'The volume constraint and the dagger structure pin $G\cong\mathrm{SU}(2)$' overstates thm:su2-emergence, which gives $G\subseteq\mathrm{SU}(2)$ under an explicit realisation hypothesis.
- **Suggested rewrite:** L1: '...from the five conditions ... The volume constraint forces the fundamental object to have rank 2, and with the dagger the gauge group lies in $\mathrm{SU}(2)$ (thm:su2-emergence, under its realisation hypothesis).'

#### `frobenius-su2` — example `ex:frobenius-su2` — T = 10/16 (fail)

- **Scores:** H1 2, H2 2, H3 1, H4 1, H5 0, H6 2, H7 1, H8 1
- **Evidence:** H5: this block gives $\Delta_\mu(f)(g,h)=\int_G f(xg)\overline{h(x)}\,dx$ and says the Frobenius relation 'encodes the associativity of convolution', while ex:frobenius-relation-su2 (Chapter 1) computes the same $\Delta_\mu$ for the same $A$ as the diagonal $f(x)\delta_{x=y}$ and warns that it is not the group coproduct. The two examples of one object disagree.
- **Suggested rewrite:** Delete this block and cite ex:frobenius-relation-su2, or state which pairing (with or without conjugation) is used here and reconcile the two formulas.
- **Also:** needs_owner (content): inconsistent with ex:frobenius-relation-su2 — two different formulas for Δ_μ on O(SU(2)).

#### `dagger-su2` — example `ex:dagger-su2` — T = 13/16 (warn)

- **Scores:** H1 1, H2 2, H3 1, H4 1, H5 2, H6 2, H7 2, H8 2
- **Evidence:** H4: $g$ is a group element (L1 '$f^\dagger(g)=\overline{f(g^{-1})}$') while $f$ ranges over both intertwiners $V_j\to V_k$ and functions on $\mathrm{SU}(2)$ in one paragraph. H1/H3: a single 100-word paragraph with no stated purpose; L1 says the dagger comes 'from the antipode' and then uses the Hilbert-space adjoint without connecting them.
- **Suggested rewrite:** Split into two short paragraphs: (1) on $\mathrm{Rep}(\mathrm{SU}(2))$, $\dagger$ is the Hilbert adjoint for invariant inner products; (2) on $A$, it is $\phi\mapsto\overline{\phi(\,\cdot^{-1})}$, i.e. antipode then conjugation — 'which is why it comes from the antipode'. Use $\phi$ for functions.

#### `volume-from-rigidity` — lemma `lem:volume-from-rigidity` — T = 8/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 0
- **Evidence:** H8: L1 'This alternating condition forces $\mathrm{rank}(V)=2$' is asserted, and the following sentences instead derive $\mathrm{rank}(\Lambda^2V)=1$ from non-degeneracy of $\epsilon$, i.e. they assume what the lemma claims. A symplectic self-duality alone exists in every even rank. H4: 'rank' of an object of an abstract rigid category is undefined. H1: L19 'This construction intrinsically satisfies the volume form requirement' is empty.
- **Suggested rewrite:** State the lemma with its real hypothesis: 'If $V$ is simple, symplectically self-dual, and $\epsilon$ is an isomorphism $\Lambda^2V\cong\mathbf1$, then $\dim\tau(V)=2$.' Say 'rank' means $\dim\tau(V)$. Delete L19.
- **Also:** needs_owner (content): the statement 'symplectic self-duality forces rank 2' is false without the Λ²V ≅ 1 hypothesis (C^4 with a symplectic form is a counterexample in Rep(Sp(4))).

#### `su2-volume-from-rigidity` — example `ex:su2-volume-from-rigidity` — T = 14/16 (warn)

- **Scores:** H1 2, H2 2, H3 1, H4 2, H5 1, H6 2, H7 2, H8 2
- **Evidence:** H5: L1 'restricting the gauge group from $\mathrm{GL}(2,\mathbb C)$ to at least $\mathrm{SL}(2,\mathbb C)$' — the constraint shrinks the group, so it lands *inside* $\mathrm{SL}(2,\mathbb C)$. H3: the purpose (this is the volume constraint seen in coordinates) is not stated.
- **Suggested rewrite:** '...forces $\det g=1$, so $G\subseteq\mathrm{SL}(2,\mathbb C)$.' Open: 'In coordinates the volume constraint is the determinant.'

#### `su2-emergence` — theorem `thm:su2-emergence` — T = 12/16 (warn)

- **Scores:** H1 1, H2 1, H3 2, H4 1, H5 1, H6 2, H7 2, H8 2
- **Evidence:** H5: L14 'so $G\subseteq\mathrm{SU}(2)$ — or its split real form $\mathrm{SL}(2,\mathbb R)$' contradicts the displayed conclusion $G\subseteq\mathrm{SU}(N)$. H1: L16 'an earlier formulation derived "which subgroup" and reported it as though...' is drafting history. L22-24 is a Lean section inside a theorem block. H4: '$\mathbb{1}$' (L3) vs '$\mathbf 1$' everywhere else.
- **Suggested rewrite:** Delete the $\mathrm{SL}(2,\mathbb R)$ clause or make it a separate remark with the indefinite-signature hypothesis. Delete the 'earlier formulation' sentence. Move the Lean paragraph to the `.ts` lean.ref / an author note.
- **Also:** proof-no-lean-mention-in-prose: L22-24 '## Lean structure' names `SU2EmergenceRankForced.lean` and four Lean declarations; L16 drafting-history leak.

#### `su2-emergence-example` — example `ex:su2-emergence` — T = 14/16 (warn)

- **Scores:** H1 2, H2 2, H3 1, H4 2, H5 2, H6 2, H7 2, H8 1
- **Evidence:** H8: L1 'Any tensor automorphism $g$ must preserve $\epsilon$' — the reason (naturality: $\epsilon$ is a morphism of $\mathbf C$) is the load-bearing step and is not given.
- **Suggested rewrite:** 'Because $\epsilon$ is a morphism in $\mathbf C$, every tensor automorphism of $\tau$ commutes with it, so $\det g_V=1$.'

#### `spin-labels` — proposition `prop:spin-labels` — T = 10/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 1, H6 1, H7 2, H8 1
- **Evidence:** H5/H8: L1 'Because $G\cong\mathrm{SU}(2)$' — thm:su2-emergence gives only $G\subseteq\mathrm{SU}(2)$ under a realisation hypothesis; and equality of the group does not by itself index the simple objects of $\mathbf C$ (that needs $\mathbf C\simeq\mathrm{Rep}(G)$). H4: '$\mathrm{Ad}(A)$' appears with no definition in this block. H6: a tikz row (L3-10) repeats the sentence.
- **Suggested rewrite:** 'Assume $\mathbf C\simeq\mathrm{Rep}(\mathrm{SU}(2))$ via $\tau$ (Tannaka–Krein). Then the simple objects are $V_j$, $j\in\tfrac12\mathbb Z_{\ge0}$, of dimension $2j+1$; $V=V_{1/2}$, and the adjoint object $\mathrm{Ad}(A)$ (def:...) is $V_1$.' Drop the tikz row.

#### `spin-labels-su2` — example `ex:spin-labels-su2` — T = 13/16 (warn)

- **Scores:** H1 1, H2 2, H3 1, H4 2, H5 1, H6 2, H7 2, H8 2
- **Evidence:** H5: L20 '$\mathbb C[z]=\bigoplus_n\mathrm{Sym}^nV$ serves as the coordinate ring of $\mathbb P(V)$' — $\bigoplus\mathrm{Sym}^n\mathbb C^2$ is $\mathbb C[z_0,z_1]$, the homogeneous coordinate ring; $\mathbb C[z]$ is one affine chart. H1/H6: a tikz diagram of phantom '$\cong$' arrows (L3-12) restates the bulleted list below it.
- **Suggested rewrite:** L20: 'The polynomial ring $\mathbb C[z_0,z_1]=\bigoplus_n\mathrm{Sym}^nV$ is the homogeneous coordinate ring of $\mathbb P(V)$; its degree-$n$ part is $V_{n/2}$.' Delete the tikz block.

#### `spin-half-representation` — remark `rem:spin-half-representation` — T = 15/16 (warn)

- **Scores:** H1 2, H2 2, H3 2, H4 1, H5 2, H6 2, H7 2, H8 2
- **Evidence:** H4: L10 writes the torus angle as $\theta_q$; the subscript $q$ is unexplained, and the torus $T$ is used both as a set and as an element acting on $e_\pm$.
- **Suggested rewrite:** '$t_\theta=\mathrm{diag}(e^{i\theta},e^{-i\theta})$ acts by $t_\theta e_\pm=e^{\pm i\theta}e_\pm$.'

#### `g-action-on-substrate` — conjecture `conj:g-action-on-substrate` — T = 5/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 0, H5 1, H6 1, H7 0, H8 0
- **Evidence:** H4/H7: the block introduces $\mathcal N_{\rm sym}$, $\mathrm{tr}_F$, $e^{\rm EW}_{\rm sym}$, $e_H$, $\varrho_\Phi$, $T(2,4)$, $T(2,6)$, $\hbar_q$ and 'Anchor II' without definition, and presumes the electroweak sector ($W^\pm$, $Z$, Higgs VEV $v\approx246$ GeV) as background. H8: L52-55 the trace of a product is factored into a product of $q$-dimensions with no argument, and L69 multiplies $[4]_q$ twice for $W^+$ and $W^-$ while L54 forms a direct sum. L87 lists candidate corrections to a $-1.81\%$ residual.
- **Suggested rewrite:** Separate the conjecture (constraints G-1…G-4, stated with each symbol defined) from the numerical comparison (a remark marked as the comparison point with CODATA). Justify or flag the step 'trace of the product = product of $q$-dimensions'. Introduce the electroweak names as names for components of $A$, with the physical reading in a follow-on remark. Remove the speculative-correction list or move it to the bean tracker.
- **Also:** needs_owner (content/anti-fit): the L52-72 factorisation and the [4]_q^2 for a direct sum are unexplained; L87 lists post-hoc correction candidates for the residual (AGENTS.md anti-fit discipline).

#### `weight-decomposition-intro` — prose `sec:weight-decomposition-intro` — T = 10/16 (fail)

- **Scores:** H1 1, H2 1, H3 2, H4 2, H5 1, H6 2, H7 1, H8 0
- **Evidence:** H8: L1 'This splitting establishes the geometric origin of spin-statistics directly from the categorical structure' and 'horizontal forms ... correspond geometrically to bosons' are physical claims stated as consequences of a grading. H5: L1 splits forms into weight zero vs non-zero weight, then says 'mixed forms carry half-integer spin' — non-zero weights include integer spins.
- **Suggested rewrite:** 'Having labelled the simple objects by spin, we fix the maximal torus $T\subset G$ and grade differential forms by $T$-weight. A form splits uniquely into a weight-zero (horizontal) part and the rest (vertical).' Move the boson/fermion reading to a remark that states it as an interpretation.

#### `maximal-torus` — definition `def:maximal-torus` — T = 8/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 0, H6 1, H7 1, H8 1
- **Evidence:** H5: circular — L1 defines the weight subcategory as sums of 'the weight spaces of $V$', and then defines $T$ as the subgroup acting diagonally on those weight spaces; weight spaces presuppose a torus. Weight spaces of $\tau(V)$ are subspaces of a module, not objects of $\mathbf C$. H6: the tikz square (L7-16) does not encode the definition. H2: no picture first ($\mathrm{diag}(e^{i\theta},e^{-i\theta})$).
- **Suggested rewrite:** Define via a chosen decomposition: 'Fix a decomposition $\tau(V)=L_+\oplus L_-$ into rank-one summands. The maximal torus $T\subseteq G$ is the subgroup preserving each $L_\pm$; for $\mathrm{SU}(2)$, $T=\{\mathrm{diag}(e^{i\theta},e^{-i\theta})\}$.' Drop the tikz square.

#### `maximal-torus-su2` — example `ex:maximal-torus-su2` — T = 13/16 (warn)

- **Scores:** H1 2, H2 2, H3 1, H4 0, H5 2, H6 2, H7 2, H8 2
- **Evidence:** H4: L1 writes the torus angle as $\varTheta$, the symbol the paper reserves for the Maurer–Cartan/Reeb 1-form ($\varTheta=g^{-1}dg$, $\varTheta_A$).
- **Suggested rewrite:** '...acts on $e_\pm$ by $e^{\pm i\theta}$.'

#### `weight-decomposition` — definition `def:weight-decomposition` — T = 12/16 (warn)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 2, H6 1, H7 2, H8 2
- **Evidence:** H6: the tikz diagram (L3-12) draws a hook $\Omega^k_H\hookrightarrow\Omega^k_V$ labelled '$\oplus$', which is not a map in the decomposition; the equation $\alpha=\alpha_H+\alpha_V$ carries the content. H3/H2: no purpose and no instance stated (for $\mathrm{SU}(2)$: forms invariant under the circle vs the rest).
- **Suggested rewrite:** Replace the diagram with $\Omega^k(A)=\Omega^k_H(A)\oplus\Omega^k_V(A)$, $\alpha=\alpha_H+\alpha_V$. Open with: 'Grading forms by torus weight separates what the circle action sees from what it does not; on $\mathrm{SU}(2)\to S^2$ the weight-zero forms are those pulled back from the base.'

#### `weight-decomposition-su2` — example `ex:weight-decomposition-su2` — T = 14/16 (warn)

- **Scores:** H1 2, H2 2, H3 1, H4 1, H5 2, H6 2, H7 2, H8 2
- **Evidence:** H4: L6-7 parametrise the torus by $\theta_q$, with an unexplained subscript $q$ on a classical angle; L1 says each generator is rescaled 'by a phase' without saying which. H3: purpose not stated.
- **Suggested rewrite:** Use $\theta$; add 'with $t_\theta\cdot\alpha=e^{i\theta}\alpha$, $t_\theta\cdot\beta=e^{-i\theta}\beta$'.

#### `vectors-hadrons-intro` — prose `sec:vectors-hadrons-intro` — T = 10/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 1, H5 2, H6 2, H7 1, H8 1
- **Evidence:** H4/H7: the roadmap names 'the Pawlowski–Leitner canonical basis', 'the unital Gröbner–Shirshov route', 'fibre integration commutes with the intertwiner expansion of hadron states' — none introduced or cited. H3: the reason for building a basis of $\mathrm{Hom}(V_j,V^{\otimes n})$ (counting and pairing multi-strand states) is not stated. H8: 'hadron states' presumes physics.
- **Suggested rewrite:** 'Bound states of $n$ strands are intertwiners $V_j\to V^{\otimes n}$. We need a basis of these spaces and an inner product on them. The basis is indexed by two-row standard tableaux (as for $\mathfrak{sl}_2$ in Fulton–Harris §6), and the adjoint trace makes it orthogonal.'

#### `adjoint-trace` — remark `rem:adjoint-trace` — T = 9/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 0, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H4/H5: L6 composes $\int_A\circ\mu\circ(f\otimes\mathrm{id}_{V^\vee})\circ\mathrm{coev}_V$, applying the multiplication $\mu$ of $A$ to $V\otimes V^\vee$; L12's $\mathrm{coev}_V\colon\mathbf1\to V\otimes V^\vee$ has the opposite order to def:snake-identity. H8: L14 'recovers the Killing form: $\mathrm{tr}_{\mathrm{Ad}}(f)=\mathrm{tr}(\mathrm{ad}(f))=-2\,\mathrm{tr}_{\mathbb C^2}(f)$' — a trace is not the (bilinear) Killing form, and $\mathrm{tr}(\mathrm{ad}\,f)=0$ on $\mathfrak{su}(2)$.
- **Suggested rewrite:** State the trace as the ordinary categorical trace $\mathrm{ev}_V\circ(f\otimes\mathrm{id})\circ\mathrm{coev}_V$ with the conventions of def:snake-identity, and say where $\int_A$ enters. Replace the last sentence with the correct classical statement (e.g. $\langle X,Y\rangle=\mathrm{tr}(\mathrm{ad}X\,\mathrm{ad}Y)=4\,\mathrm{tr}_{\mathbb C^2}(XY)$).
- **Also:** needs_owner (content): L6 type mismatch (μ applied to V⊗V^∨) and L14 Killing-form identity as written.

#### `pawlowski-leitner-basis` — proposition `prop:pawlowski-leitner-basis` — T = 9/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H4: L14 the vector $e_+^{\otimes(j+m)}\otimes e_-^{\otimes(j-m)}$ has $m$ undefined and is not highest-weight unless $m=j$; the tikz chain $\Lambda^2V\hookrightarrow V^{\otimes n}$ (L6-8) is mistyped for $n>2$. 'PawLei' is a coined abbreviation. H7: 'canonical' basis attributed to Pawlowski–Leitner with no citation. H2: no small case ($n=2$: the singlet $e_+\otimes e_--e_-\otimes e_+$).
- **Suggested rewrite:** Give $n=2,3$ first: '$\mathrm{Hom}(V_0,V^{\otimes2})$ is spanned by $\epsilon^\vee$, the singlet; $\mathrm{Hom}(V_{1/2},V^{\otimes3})$ is two-dimensional, indexed by the tableaux of shape $(2,1)$.' Cite the source of the basis. Write the vector as $e_+^{\otimes(n/2+j)}\otimes e_-^{\otimes(n/2-j)}$ or define $m$. Spell out the name.

#### `pawlowski-leitner-inner-product` — proposition `prop:pawlowski-leitner-inner-product` — T = 9/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H4/H5: L16 the arrow '$\phi^\dagger\circ\psi\otimes\mathrm{id}$' lands in $A\otimes V_j^\vee$, i.e. $\mathrm{End}(V_j)$ is silently treated as a subobject of $A$ (stated only at L26). H8: L24 'the squared norm is a positive rational computable directly from the hook lengths' — the formula is not given. L26 'any categorical hadron state ... partial-wave amplitudes' and the closing sentence about $q_0$ are physics not supported by the block.
- **Suggested rewrite:** Write $\langle\phi,\psi\rangle=\mathrm{tr}(\phi^\dagger\psi)$ with $\mathrm{tr}$ the categorical trace on $\mathrm{End}(V_j)$; give the norm formula or cite it. Cut L26 to: 'So every intertwiner has a unique orthogonal expansion in the basis.'

#### `differential-structures-intro` — prose `sec:differential-structures-intro` — T = 10/16 (fail)

- **Scores:** H1 1, H2 1, H3 2, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H8/H5: L1 'Each of these structures is forced by the QOU axioms' and '... establishing the observability axiom directly from the Frobenius pairing' — an axiom is assumed, not established. H4: 'intrinsic contact affine chart', 'realize it physically within the left-covariant calculus' are undefined.
- **Suggested rewrite:** 'We now build first-order structure on $A$: a vector field $\xi$ generating the torus action (the Reeb derivation), the projective line $A/\ldots$ with its affine chart, and an involution relating $\mathbb P^1$ to a coadjoint orbit. For $\mathrm{SU}(2)$ these are the Hopf circle action, $S^2=\mathbb{CP}^1$, and the sphere as an orbit in $\mathfrak{su}(2)^*$.'

#### `categorical-reeb` — definition `def:categorical-reeb` — T = 8/16 (fail)

- **Scores:** H1 2, H2 0, H3 1, H4 1, H5 1, H6 1, H7 1, H8 1
- **Evidence:** H2/H3: no picture of the Reeb field (the Hopf circle on $S^3=\mathrm{SU}(2)$) and no purpose stated. H4/H5: L1 'π_V∘d = ι_ξ dϑ_A' equates a map $A\to\Omega^1_V(A)$ with an element of $\Omega^1(A)$; '$\varTheta_A$ the canonical 1-form dual to $\xi$' is used to define $\xi$'s own conditions (circular). H6: the tikz square restates the decomposition already given.
- **Suggested rewrite:** Open: 'On $\mathrm{SU}(2)\cong S^3$ the circle action $t_\theta$ is generated by a vector field $\xi$, the Reeb field of the contact form $\varTheta$ with $\varTheta(\xi)=1$; its orbits are the fibres of the Hopf map to $S^2$. We define the same pair categorically.' Write the first condition with matching types (e.g. $\pi_V(df)=\xi(f)\,\varTheta_A$).

#### `categorical-reeb-exists` — theorem `thm:categorical-reeb-exists` — T = 9/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 1, H6 1, H7 1, H8 1
- **Evidence:** H6/H5: the tikz square (L3-12) asserts $\varTheta_A\circ\xi=\iota_\xi\circ d$ with $\varTheta_A\colon A\to A$, which is neither of the two constraints in the statement and retypes $\varTheta_A$ (a 1-form). H8: 'unique' with no indication of what fixes the choice (normalisation only fixes scale).
- **Suggested rewrite:** Drop the diagram. 'There is a unique pair $(\xi,\varTheta_A)$ ... ; uniqueness comes from the rank-one torus and the normalisation $\varTheta_A(\xi)=1$.' Add: 'For $\mathrm{SU}(2)$ this is the Hopf vector field.'

#### `reeb-su2` — example `ex:reeb-su2` — T = 12/16 (warn)

- **Scores:** H1 2, H2 2, H3 1, H4 1, H5 1, H6 2, H7 1, H8 2
- **Evidence:** H5: L1 ends with '$\iota_\xi d\varTheta=0$', which is not the vertical-generator condition '$\pi_V\circ d=\iota_\xi d\varTheta_A$' of def:categorical-reeb that this example is meant to instantiate. H7/H4: 'the archimedean realization on a CR manifold $(M,\varTheta)$' introduces CR geometry and $M$ unannounced; 'acts as the left-invariant vector field' does not say which.
- **Suggested rewrite:** '...$\xi$ acts as the left-invariant vector field generated by $\tfrac12\mathrm{diag}(1,-1)$; its orbits are the Hopf circles.' State which condition of the definition $\iota_\xi d\varTheta=0$ verifies, or drop the CR sentence.

#### `categorical-reeb-brings` — example `ex:categorical-reeb-brings` — T = 8/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 0, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H4/H5: L1 starts on 'the Bring coordinate ring $\mathcal O_q(\mathcal B)$' and then works on $A=\mathcal O_q(\mathrm{SU}(2))$ without saying how the two relate; $\omega_\pm$, $e_3$, the Woronowicz calculus and 'the $8=2g$ independent cycles' arrive undefined. H8: 'precisely matching the fundamental modes' is unexplained. H3: no reason given for computing the Reeb derivation on Bring's curve here.
- **Suggested rewrite:** State the purpose first ('Bring's curve carries an $S_5$ action; we check that the Reeb derivation extends to it'), say whether $A$ is $\mathcal O_q(\mathcal B)$ or $\mathcal O_q(\mathrm{SU}(2))$, define $\omega_\pm$, and replace 'fundamental modes' with what is matched.

#### `contact-affine-chart` — definition `def:contact-affine-chart` — T = 8/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 0, H5 1, H6 1, H7 1, H8 1
- **Evidence:** H4/H5: L4 writes points of $\mathbb P(V)$ as classes $[\alpha]$ of differential forms and L11 defines $Z$ as a ratio of forms ($\alpha_H/\iota_\xi\alpha$) that is said (L25) to take values in a distribution — the objects being divided are never typed. L1 '$\mathbb P(V)$ the projective line object' is used before it is defined. H2: the classical picture (stereographic coordinate $z=z_1/z_0$ on $\mathbb{CP}^1$) is mentioned only as the last word.
- **Suggested rewrite:** Begin with the classical case: 'On $\mathbb{CP}^1$ the affine chart $\{z_0\ne0\}$ has coordinate $z=z_1/z_0$, stereographic projection from the pole.' Then give the categorical version with the type of $Z$ stated. Cite the definition of $\mathbb P(V)$.

#### `differential-structures-fiber-adjoint-intro` — prose `sec:differential-structures-fiber-adjoint-preamble` — T = 10/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 1, H5 2, H6 2, H7 1, H8 1
- **Evidence:** H4/H1: a four-sentence roadmap naming 'the projector onto coadjoint orbits', 'the substrate's radial coordinate', 'the fibre-functor atlas' without saying what any is or why the section needs it.
- **Suggested rewrite:** 'For $\mathrm{SU}(2)$, the projective line $\mathbb{CP}^1$ is the sphere $S^2\subset\mathfrak{su}(2)^*$ of rank-one projectors. This section makes that identification categorical.'

#### `fibre-functor-atlas` — proposition `prop:fibre-functor-atlas` — T = 12/16 (warn)

- **Scores:** H1 2, H2 1, H3 1, H4 2, H5 2, H6 2, H7 1, H8 1
- **Evidence:** H7/H8: L1 concludes that fibre functors form 'a $G$-gerbe', a heavy notion for the primary reader, with no framing of why it is the right tool and no reference; 'functorial composition enforces the cocycle condition' hand-waves the step. The torsor statement holds fpqc-locally, not for 'any two' fibre functors over an arbitrary $R$.
- **Suggested rewrite:** Add the classical case: 'For $\mathrm{Rep}(\mathrm{SU}(2))$ over $\mathbb C$ any two fibre functors are isomorphic and the isomorphisms form a copy of $G$ acted on by translation.' Cite Deligne 1990 §1.12 for the torsor and say 'locally' where needed.

#### `fibre-functor-atlas-affine-charts` — remark `rem:fibre-functor-atlas-affine-charts` — T = 12/16 (warn)

- **Scores:** H1 2, H2 1, H3 2, H4 1, H5 2, H6 2, H7 1, H8 1
- **Evidence:** H8: L1 'the $G$-gerbe of fibre functors is precisely the affine atlas of the quantum universe' turns an analogy into an identity. H4: 'affine chart' already names $U_\xi\subset\mathbb P(V)$ (def:contact-affine-chart); here it is reused for a fibre functor.
- **Suggested rewrite:** 'Each fibre functor can be read as a chart, and isomorphisms between fibre functors as transition functions; the analogy is with an atlas of a manifold.' Use 'chart' rather than 'affine chart'.

#### `substrate-radial-coordinate` — proposition `prop:substrate-radial-coordinate` — T = 7/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 0, H6 1, H7 1, H8 0
- **Evidence:** H8/H5: L1 'As $q\to\infty$ ... $Z\to0$; as $q\to1$ ... $Z\to\infty$' — $Z$ (def:contact-affine-chart) is defined with no dependence on $q$, and no argument or citation is given. H4: '$\hbar_q$ the quantum Planck constant' and the complex structure $J$ appear without definition.
- **Suggested rewrite:** State how $Z$ depends on $q$ (or what is meant by 'the radial coordinate governed by $q$') before the limits; give the proof location. Introduce $\hbar_q=1-q^{-1}$ as a parameter, with the physical name in a remark.

#### `fiber-adjoint-involution` — proposition `prop:fiber-adjoint-involution` — T = 7/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 0, H6 1, H7 1, H8 0
- **Evidence:** H4/H5: L1 calls $\sigma\colon\mathbb P(V)\hookrightarrow\mathrm{Ad}(A)$ 'an involution', but a map between two different objects cannot be one. H8: L1 'The non-degeneracy of the Frobenius pairing then forces the observability condition $\mathrm{Hom}(\mathbf1,\mathrm{Ad}(A))=0$' — the step is not given, and observability is an axiom of def:quantum-observable-universe.
- **Suggested rewrite:** Call $\sigma$ an embedding. Remove the observability sentence or state precisely what is derived. Open with ex:fiber-adjoint-su2's picture: a line $\ell\subset\mathbb C^2$ goes to the projector onto $\ell$.

#### `fiber-adjoint-su2` — example `ex:fiber-adjoint-su2` — T = 14/16 (warn)

- **Scores:** H1 2, H2 2, H3 1, H4 2, H5 1, H6 2, H7 2, H8 2
- **Evidence:** H5: L5 $vv^\dagger/\|v\|^2-\tfrac12\mathrm{id}$ is Hermitian, but is placed in $\mathfrak{su}(2)$ (skew-Hermitian) and identified with the orbit of $\tfrac12\mathrm{diag}(i,-i)$; the sphere has radius $\tfrac12$, not 1.
- **Suggested rewrite:** '...$\sigma([\ell])=i\bigl(vv^\dagger/\|v\|^2-\tfrac12\mathrm{id}\bigr)\in\mathfrak{su}(2)$, which identifies $\mathbb{CP}^1$ with the sphere of radius $\tfrac12$ (in the trace norm), the orbit of $\tfrac12\mathrm{diag}(i,-i)$.'
- **Also:** needs_owner (content): Hermitian vs skew-Hermitian in L5/L10.

#### `connection-su2` — example `ex:connection-su2` — T = 13/16 (warn)

- **Scores:** H1 1, H2 2, H3 1, H4 2, H5 2, H6 2, H7 1, H8 2
- **Evidence:** H1: repeats the material of ex:categorical-connection-su2 (Chapter 1) in less detail. H7: L1 'the failure of bi-covariance controls the deformation of the exterior derivative' is an unframed technical claim.
- **Suggested rewrite:** Cite ex:categorical-connection-su2 for the classical case and keep only the $q$-deformed statement: 'At $q\neq1$ we use Woronowicz's left-covariant calculus [cite]; no bicovariant 3-dimensional calculus exists, which is why the exterior derivative deforms.'

#### `substrate-parameter-intro` — prose `sec:substrate-parameter-preamble` — T = 11/16 (fail)

- **Scores:** H1 1, H2 1, H3 2, H4 1, H5 2, H6 2, H7 1, H8 1
- **Evidence:** H4/H8: L1 'This links the microscopic categorical data directly to the macroscopic fluid parameter' — no fluid parameter has been introduced; '$\mathbb G_m$-family of differentials' is undefined.
- **Suggested rewrite:** 'We read $q$ off the braiding: it is the eigenvalue of $c_{V,V}$ on $\mathrm{Sym}^2V$. For $\mathrm{Rep}(\mathrm{SU}_q(2))$ this is the deformation parameter of the quantum group. We then deform the differential and the gauge group with $q$.'

#### `braiding-eigenvalue-extraction` — proposition `prop:braiding-eigenvalue-extraction` — T = 12/16 (warn)

- **Scores:** H1 2, H2 2, H3 1, H4 1, H5 1, H6 2, H7 2, H8 1
- **Evidence:** H5/H8: L3-6 'We define ... $q:=\lambda_+$, $\lambda_-=-q^{-1}$' presents the second equation as part of a definition, though $\lambda_-$ was already determined; L9 then says '$\lambda_+\lambda_-=-1$ reflects the determinant constraint' without showing it. L9's last sentence about $d_q$ is unconnected. H4: $\lambda_\pm$ reuses $\lambda$, the Wedderburn block index.
- **Suggested rewrite:** 'Define $q:=$ the eigenvalue on $S^2V$. The eigenvalue on $\Lambda^2V$ is then $-q^{-1}$, because [reason: the volume constraint fixes $\det c_{V,V}$...].' Name the eigenvalues $\beta_\pm$. Move the $d_q$ sentence to the block that defines $d_q$.

#### `braiding-eigenvalue-extraction-novelty` — remark `rem:braiding-eigenvalue-extraction-novelty` — T = 14/16 (warn)

- **Scores:** H1 1, H2 2, H3 2, H4 1, H5 2, H6 2, H7 2, H8 2
- **Evidence:** H4: L3 'the CAL-2 calibration', L5 'archimedean level', L7 'the macroscopic fluid PDE' are project terms not explained to a reader meeting them here; L1 writes $\mathrm{End}^{\otimes}(\tau)$ where the rest of the paper uses $\mathrm{Aut}^{\otimes}(\tau)$. H1: L3 'in the words of that block' is internal cross-talk.
- **Suggested rewrite:** L3: 'The numerical value $q_0\approx1.10998$ is an input: it is chosen so that the model's muon-to-electron mass ratio matches experiment (rem:epistemic-status-of-calibrations).' Replace 'macroscopic fluid PDE' with a pointer to the chapter where it appears. Use $\mathrm{Aut}^{\otimes}$.

#### `spectral-chart-correspondence` — proposition `prop:spectral-chart-correspondence` — T = 10/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H8: L1 asserts that the transition coordinate $\kappa$ in $zw=\kappa$ 'equals $\lambda_+^{-1}=-\lambda_-=q^{-1}$' with no argument; classically $zw=1$ and the block does not say why the braiding should enter the gluing. H5: 'the two contact affine charts' — def:contact-affine-chart defines one.
- **Suggested rewrite:** Give the classical case ($\kappa=1$ on $\mathbb{CP}^1$), define the second chart, and cite or sketch why the gluing constant becomes $q^{-1}$ (e.g. the $q$-commutation $zw=q^{-1}wz$ in $\mathcal O_q(\mathbb P^1)$).

#### `substrate-parameter` — definition `def:substrate-parameter` — T = 6/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 0, H5 0, H6 1, H7 1, H8 0
- **Evidence:** H5/H8: L19 defines $q$ as 'the unique value for which $d_q$ acts as $q^{-1}d$ on horizontal forms and as $d$ on vertical forms' — but $d_q$ is defined at L4 for every $q$ by exactly that formula, so every $q$ satisfies it; the definition is circular. H4: prop:braiding-eigenvalue-extraction already defines $q:=\lambda_+$; this is a second, different definition of the same symbol. H6: the tikz diagram (L7-17) is decorated with phantom limit labels and carries no content.
- **Suggested rewrite:** Make this block a definition of $d_q$ for a given $q$ (the eigenvalue of prop:braiding-eigenvalue-extraction): '$d_q:=q^{-1}d+(1-q^{-1})\pi_Vd$; it scales horizontal derivatives by $q^{-1}$ and leaves vertical ones unchanged.' Delete L19 and the diagram.
- **Also:** needs_owner (content): two inconsistent definitions of q (here vs prop:braiding-eigenvalue-extraction); L19 is circular.

#### `substrate-parameter-limits-and-lusztig` — remark `rem:substrate-parameter-limits-and-lusztig` — T = 10/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H4/H7: '$q\colon M\to k^\times$' (L1) uses $M$ and $k$ undefined, and the Lusztig integral form $\mathcal U^{\mathbb Z}_q(\mathfrak{su}(2))$ is dropped in without saying what it is for (and is usually defined for $\mathfrak{sl}_2$).
- **Suggested rewrite:** 'At $q=1$, $d_q=d$; as $q\to\infty$, $d_q\to\pi_Vd$. To specialise $q$ to a number one needs a form of the quantum group defined over $\mathbb Z[q,q^{-1}]$; Lusztig's integral form $\mathcal U^{\mathbb Z}_q(\mathfrak{sl}_2)$ is that form [Lusztig 1990].'

#### `substrate-parameter-unique` — theorem `thm:substrate-parameter-unique` — T = 9/16 (fail)

- **Scores:** H1 1, H2 1, H3 2, H4 1, H5 1, H6 2, H7 1, H8 0
- **Evidence:** H8: L1 states a theorem about $q\in\mathrm{End}(\mathbf1)$ and then asserts, as part of the theorem, that 'the substrate parameter is a field $q\colon M\to\mathbb R_{>0}$ that varies ... with energy scale; high-energy processes see a different $q$' — physical claims with no definition of $M$ and no support. H5: 'uniquely determined as a parameter ... does not mean $q$ takes a single value' is confusing.
- **Suggested rewrite:** Theorem: 'In a QOU whose dagger is positive definite, exactly one of the two braiding eigenvalues $\{q,-q^{-1}\}$ is positive; we call it $q$.' Move the field-on-$M$ and energy-scale reading to a remark labelled as interpretation.

#### `substrate-parameter-su2` — example `ex:substrate-parameter-su2` — T = 11/16 (fail)

- **Scores:** H1 2, H2 2, H3 1, H4 0, H5 2, H6 2, H7 1, H8 1
- **Evidence:** H4: L1 uses $q_0$ for an arbitrary specialisation, including $q_0=e^{\pi i/\kappa}$, while the paper reserves $q_0$ for the calibrated value $\approx1.10998$; $\kappa$ is also the chart constant of prop:spectral-chart-correspondence. H8: L1 'leaving a finite semisimple category' at a root of unity needs semisimplification (tilting modules modulo negligibles), which is not mentioned.
- **Suggested rewrite:** Write $\zeta$ for the specialised value: '$q\mapsto\zeta$. At $\zeta=1$ ... At $\zeta=e^{\pi i/\ell}$, after quotienting by negligible morphisms, one gets a finite semisimple (modular) category with quantum dimensions $[2j+1]_\zeta$.'

#### `substrate-parameter-brings` — example `ex:substrate-parameter-brings` — T = 10/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H5: L1 'On Bring's surface, $V\otimes V\cong V_1\oplus V_0$' — a tensor decomposition is a statement about the category, not about a surface; $M$ and $p$ appear undefined. H8: L1 'the Euler characteristic $\chi(A)=-6$ constrains the quantum dimension $[2]_q$' is asserted with no indication how.
- **Suggested rewrite:** State what Bring's surface contributes here (or drop it): 'When the universe is realised over Bring's curve, $q$ may vary from point to point; the braiding at each point gives a positive $q(p)$.' Remove the $\chi(A)=-6$ clause or point to where it is derived.

#### `quantum-universe-explication` — prose `sec:quantum-universe-explication` — T = 11/16 (fail)

- **Scores:** H1 1, H2 1, H3 2, H4 1, H5 2, H6 2, H7 1, H8 1
- **Evidence:** H8: L1 'Every subsequent physical feature—commutators, Reeb derivations, and action traces—is governed strictly by this single categorical parameter' overclaims (the paper's own calibrations are three). H4: 'the $\mathbb G_m$-family of interpolations' is undefined.
- **Suggested rewrite:** 'Fixing $q$ deforms the dimension of $V$ from 2 to $[2]_q=q+q^{-1}$ and $\mathrm{SU}(2)$ to $\mathrm{SU}_q(2)$; the constructions that follow depend on $q$ through these.'

#### `q-hodge-star` — definition `def:q-hodge-star` — T = 10/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 1, H6 1, H7 2, H8 1
- **Evidence:** H4: $\wedge_q$ (L4) is not defined; '$n$' is undefined (as in def:categorical-hodge-star); $\star_q$ is called an involution though it maps $\Omega^k\to\Omega^{n-k}$. H6/H5: the diagram (L8-16) says $\star_q=q\star$, which agrees with the formula only if $\wedge_q=\wedge$.
- **Suggested rewrite:** 'Define $\star_q:=q\,\star$.' If $\wedge_q$ differs from $\wedge$, define it first. Drop 'involution'.

#### `q-deformed-commutator` — definition `def:q-deformed-commutator` — T = 8/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 0, H5 1, H6 2, H7 1, H8 0
- **Evidence:** H8: the definition sets $[\hat X,\hat P]_q:=J\hbar_q(p)$ without defining $\hat X$, $\hat P$ (as operators on what), the Levi distribution $H$, $M$ or $p$ — it assigns a value to a commutator of undefined objects. Physics names ('position and momentum observables', 'quantum Planck constant') are presumed.
- **Suggested rewrite:** Either define $\hat X,\hat P$ (e.g. as operators on sections over the affine chart) and prove the commutator, or rename the block: 'We call $\hbar_q:=1-q^{-1}$ the deformation constant; remark ... reads $J\hbar_q$ as the commutator of position and momentum.'

#### `heisenberg-commutator-prop` — proposition `prop:heisenberg-commutator` — T = 11/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 2, H6 2, H7 1, H8 1
- **Evidence:** H8: the proposition records the two limits of $1-q^{-1}$ (L3-4), immediate from def:q-deformed-commutator, under physics labels ('maximal uncertainty'); it inherits that block's undefined $\hat X,\hat P$.
- **Suggested rewrite:** Fold into the definition as one sentence: '$\hbar_q\to0$ as $q\to1$ and $\hbar_q\to1$ as $q\to\infty$.' Move the physical labels to rem:heisenberg-commutator.

#### `heisenberg-commutator` — remark `rem:heisenberg-commutator` — T = 9/16 (fail)

- **Scores:** H1 1, H2 1, H3 2, H4 1, H5 1, H6 2, H7 1, H8 0
- **Evidence:** H8: L3 'As $q\to1$, the observer sits at the base of the Reeb fibre ... as $q\to\infty$ ... at the tip' treats values of $q$ as positions in a fibre without any construction relating them; L5 '$[\hat X,\hat P]_q$ equals $\varTheta(\xi_q)$' introduces $\xi_q$ undefined. H1: L1 repeats the definition.
- **Suggested rewrite:** State plainly as interpretation: 'We read $\hbar_q$ as Planck's constant: it vanishes in the classical limit $q\to1$. The geometric reading below is heuristic.' Define $\xi_q$ or drop L5.

#### `algebraic-substrate-intro` — prose `sec:algebraic-substrate-intro` — T = 10/16 (fail)

- **Scores:** H1 1, H2 1, H3 2, H4 0, H5 2, H6 2, H7 1, H8 1
- **Evidence:** H4: a 119-word intro names the $q$-zeta function, the Chebyshev function of the Reeb flow, the Hasse–Weil bound, 'the obstruction to classicality' and 'the unit particle as a categorical invariant', none explained. H8: L1 'the differential operator forced by the categorical volume constraint' asserts a result without pointer.
- **Suggested rewrite:** 'This section studies $A$ as a ring with a distinguished derivation $\xi$ (the Reeb derivation). Its periodic orbits play the role primes play for $\mathbb Z$: we count them with a zeta function, bound them as Weil bounds point counts on a curve, and take the classical limit $q\to1$.'

#### `substrate-preamble` — prose `sec:algebraic-substrate-preamble` — T = 8/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 0, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H4: L3 names the Frobenius form $\lambda$ (elsewhere $\int_A$; $\lambda$ also indexes blocks), and introduces $\xi_q$, 'observer drift', the state bundle $\mathcal S$, Bring's curve $\mathcal B$, $\omega_A^\bullet$ and the 'observer trace $\Phi$' in a single preamble. H8: L1 'The quantum vacuum formalises as a self-dual Frobenius–Hopf algebra' presumes a physical identification.
- **Suggested rewrite:** Keep one notation for the Frobenius form ($\int_A$). Cut to: 'The substrate is the Frobenius–Hopf object $A$ with three extra structures: the Frobenius pairing, a derivation $\xi_q$ generating a circle action, and a duality making $A$ its own dualising complex. For $\mathrm{SU}(2)$ these are Haar integration, the Hopf circle field, and Poincaré duality of $S^3$.'

#### `frobenius-hopf-substrate` — definition `def:frobenius-hopf-substrate` — T = 5/16 (fail)

- **Scores:** H1 0, H2 0, H3 1, H4 0, H5 1, H6 2, H7 0, H8 1
- **Evidence:** H4/H5: the Frobenius form is $\lambda$ and the braiding $\beta$ (the rest of Chapters 1-2 use $\int_A$ and $c$); axiom 3 (L24) calls '$\mu\circ\Delta=(\Delta\otimes\mathrm{id})\circ\alpha\circ(\mathrm{id}\otimes\mu)$' a property of $\lambda$, though $\lambda$ does not occur in it and the two sides have different source and target, and it uses the Hopf $\Delta$ that ex:frobenius-relation-su2 says is *not* the Frobenius coproduct. H1/H7: L21-23 and L40-42 add ~250 words of commentary — including drafting history ('An earlier version of this definition...') and a Lean structure name. H2/H3: no example and no purpose.
- **Suggested rewrite:** Use $\int_A$ and $c$. Write axiom 3 with the Frobenius coproduct $\Delta_\mu$ and matching types, e.g. $(\mu\otimes\mathrm{id})(\mathrm{id}\otimes\Delta_\mu)=\Delta_\mu\mu$. Move L23 and L40 to a remark; delete L42. Open with the example: 'For a finite group $G$, $A=\mathbb C^G$ with pointwise product, group coproduct, $S(f)=f(\,\cdot^{-1})$ and counting measure is a Frobenius–Hopf object.'
- **Also:** proof-no-lean-mention-in-prose: L42 names `FrobeniusHopfData` and 'The formalization'; drafting-history leak ('An earlier version'). needs_owner (content): L23 says the antipode identity μ(S⊗id)Δ = ηε 'forces A to be trivial whenever the scalars form a field' — group algebras over a field are counterexamples as stated; L24 axiom 3 is mistyped.

#### `brings-coordinate-ring` — definition `def:brings-coordinate-ring` — T = 12/16 (warn)

- **Scores:** H1 2, H2 2, H3 1, H4 2, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H5: L29 says the $S_5$ permutation action descends to $\mathcal O_q(\mathcal B)$ by algebra automorphisms, but swapping $x_i,x_j$ turns $x_ix_j=qx_jx_i$ into $x_jx_i=qx_ix_j$, so permutations do not preserve the relations of L27 unless $q=\pm1$. H8: L29 'The $2g=8$ fundamental modes of the Reeb spectrum correspond to the 8 independent cycles' is asserted without construction. H3: why Bring's curve is the fibre is not said here.
- **Suggested rewrite:** State which action is meant (e.g. a twisted action, or only the subgroup preserving the order of indices). Replace the last sentence with a pointer to where the correspondence is constructed. Add one line of purpose: 'Bring's curve is the genus-4 curve with the largest symmetry group, $S_5$; we use it because ...'.
- **Also:** needs_owner (content): S_5 acting by permutations does not preserve the q-commutation relations x_i x_j = q x_j x_i (i<j) for q ≠ ±1.

#### `substrate-parameter-planck` — definition `def:substrate-parameter-planck` — T = 10/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H4/H5: this is the third definition of $q$ in the chapter — 'the deformation parameter of $A$', with $q\in\mathbb C^*$ (L1) — alongside $q:=\lambda_+$ (prop:braiding-eigenvalue-extraction) and $q\in\mathrm{End}(\mathbf1)$ (def:substrate-parameter). H8: L11 'The invertibility condition $q\ne0$ ensures $A$ is a genuine Hopf algebra with well-defined antipode' is asserted without reason.
- **Suggested rewrite:** Do not redefine $q$; cite the one definition and define only $\hbar_q:=1-q^{-1}$ here. Example: 'for $\mathcal O_q(\mathrm{SU}(2))$, $\alpha\beta=q\beta\alpha$, and $\hbar_q$ measures the failure of commutativity to first order.'

#### `categorical-reeb-derivation` — definition `def:categorical-reeb-derivation` — T = 7/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 0, H5 0, H6 2, H7 1, H8 0
- **Evidence:** H4: a second 'categorical Reeb derivation' ($\xi_q$) beside def:categorical-reeb ($\xi$), with different defining conditions. L3 '$\xi_q\circ\varTheta=\varTheta$' composes a map $A\to A$ after a 1-form. H5/H8: L1 'uniquely determined by' two conditions that do not determine it; L6 defines a period $\Omega_q$ with $\xi_q^{\Omega_q}=\mathrm{id}_A$, but a derivation kills the unit ($\xi_q(1)=0$), so no power of it is the identity.
- **Suggested rewrite:** Unify with def:categorical-reeb (one name, one definition). If the intended object is the time-$t$ flow $\exp(t\xi_q)$, define the period as the least $T>0$ with $\exp(T\xi_q)=\mathrm{id}$.
- **Also:** needs_owner (content): ξ_q^{Ω_q} = id_A is impossible for a derivation (ξ_q(1)=0); duplicate definition of the Reeb derivation.

#### `reeb-flow-bridge` — remark `rem:reeb-flow-bridge` — T = 9/16 (fail)

- **Scores:** H1 1, H2 2, H3 1, H4 1, H5 1, H6 2, H7 1, H8 0
- **Evidence:** H8: L6-8 assert correspondences — prime ideals of $\mathcal O_q(\mathcal B)$ ↔ closed Reeb orbits; $\sum_{p\le x}1$ ↔ a spectral trace; $\ln t$ ↔ $\ln_q t$ — with no construction; L10 'powers the quantum observable universe' is hype. H5: L7 equates the continuous flow with iterated powers $\xi_q^k$ of a derivation.
- **Suggested rewrite:** Present it as an analogy, marked as such, with one precise sentence: 'For a flow with closed orbits $\gamma$ of period $\ell(\gamma)$, counting orbits with $\ell\le x$ is the analogue of counting primes $p\le x$ (as in the Selberg trace formula).' Cite the analogy's source.

#### `reeb-contact-universal-computer` — remark `rem:reeb-contact-universal-computer` — T = 7/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 1, H5 1, H6 2, H7 0, H8 0
- **Evidence:** H7/H8: L3-5 invoke Cardona–Miranda–Peralta-Salas–Presas (existence of *some* Turing-complete Reeb flow on a contact 3-manifold) and conclude that 'every fibre $\mathcal S_p$ inherits the structural capacity to embed a Turing-complete Reeb flow' and that 'contact geometry ... generates universal computation natively' — the theorem is existential, the conclusion is not. L1 calls $\mathcal L_\xi\varTheta=0,\iota_\xi\varTheta=1$ 'the Cartan magic formula' (it is the definition of a Reeb field; Cartan's formula is $\mathcal L=d\iota+\iota d$).
- **Suggested rewrite:** 'Cardona, Miranda, Peralta-Salas and Presas showed that some Reeb flows on contact 3-manifolds are Turing complete [cite]. Since the state bundle carries a contact structure, such flows are available on it; whether $\xi_q$ is one is not addressed here.' Delete the last paragraph.

#### `rigid-dualizing-complex` — definition `def:rigid-dualizing-complex` — T = 7/16 (fail)

- **Scores:** H1 2, H2 0, H3 1, H4 0, H5 1, H6 2, H7 0, H8 1
- **Evidence:** H7: derived categories, injective dimension, $R\mathrm{Hom}_{A^e}$ and Van den Bergh duality arrive with no statement of what the dualizing complex is for and no simple case (for a smooth projective curve it is $K[1]$). H4: 'rigid' here collides with 'rigid monoidal'; $H^{d-i}(M)$ and $d$ are undefined. H5: L4 '$\omega\simeq R\mathrm{Hom}_{A^e}(A,A^e)$' is the inverse dualizing complex, not Van den Bergh's rigidity condition $R\cong R\mathrm{Hom}_{A^e}(A,R\otimes R)$.
- **Suggested rewrite:** Open: 'For a smooth projective curve $X$, Serre duality pairs $H^i(X,F)$ with $H^{1-i}(X,F^\vee\otimes K_X)$; the dualizing complex $K_X[1]$ is what makes this work. A rigid dualizing complex is the noncommutative replacement [Van den Bergh 1997, Yekutieli].' State the rigidity isomorphism correctly or cite it.
- **Also:** needs_owner (content): L4 states the inverse dualizing complex as the rigidity condition.

#### `rigid-dualizing-brings` — example `ex:rigid-dualizing-brings` — T = 8/16 (fail)

- **Scores:** H1 1, H2 2, H3 1, H4 1, H5 0, H6 2, H7 1, H8 0
- **Evidence:** H5: L1 promises the complex 'for Bring's coordinate ring' and L3 sets $A=\mathcal O_q(\mathrm{SU}(2))$. L5 gives $\omega_A^\bullet\cong A_\sigma[-3]$ while L19-22 compute $\mathrm{Ext}^3_{A^e}(A,A^e)=A_\sigma$, which is the inverse complex. H8: L28 'the dualizing complex encodes the Serre duality of the genus-4 curve' and '$q=q_{\mathrm{Bring}}$' are unexplained; 'Artin–Schelter regular' (L3) is asserted for a non-graded algebra.
- **Suggested rewrite:** Choose one algebra and title the example accordingly. For $\mathcal O_q(\mathrm{SU}(2))$ cite the source of the AS-Gorenstein property and the Nakayama automorphism (e.g. Brown–Zhang 2008). Delete L28 or move it to where Bring's curve is treated.
- **Also:** needs_owner (content): dualizing vs inverse dualizing complex (L5 vs L19-22); algebra mismatch with title.

#### `substrate-self-duality` — theorem `thm:substrate-self-duality` — T = 9/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 0, H6 2, H7 1, H8 1
- **Evidence:** H5: L1 states $A\simeq\omega_A^\bullet$ for the substrate, while ex:rigid-dualizing-brings computes $\omega_A^\bullet\cong A_\sigma[-3]$ (Nakayama-twisted and shifted) for the running $q$-deformed example — so the theorem, as stated, is contradicted by the chapter's own example unless $\sigma=\mathrm{id}$ and $d=0$. H8: L7 'whose cone is acyclic' restates quasi-isomorphism; L9 'the composition $\varepsilon\circ\mu$ factors through the Frobenius form' is unexplained.
- **Suggested rewrite:** State the hypotheses under which $\omega_A\simeq A$ (symmetric Frobenius, dimension 0), or state the twisted version $\omega_A\simeq A_\sigma[d]$. Give the finite-dimensional case first: 'For a symmetric Frobenius algebra, $A\cong A^*$ as bimodules; this is the case $d=0$.'
- **Also:** needs_owner (content): conflicts with ex:rigid-dualizing-brings (A_σ[-3]).

#### `substrate-self-duality-physical` — remark `rem:substrate-self-duality-physical` — T = 12/16 (warn)

- **Scores:** H1 2, H2 1, H3 2, H4 1, H5 1, H6 2, H7 2, H8 1
- **Evidence:** H5: L1 'The Frobenius form $\lambda$ is the unique trace that makes $A$ its own dualizing object' contradicts prop:frobenius-pairing-unique (unique up to scalar). H4: 'observer trace', 'observed state space' are metaphors given as identifications.
- **Suggested rewrite:** 'Self-duality pairs $A$ with itself, so elements of $A$ serve both as observables and as states: $a$ defines the state $b\mapsto\int_A ab$. The Frobenius form is unique up to scale.'

#### `archimedean-intro` — prose `sec:archimedean-qou` — T = 11/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 2, H6 2, H7 1, H8 1
- **Evidence:** H3/H7: L1 announces CR geometry, contact manifolds and pseudo-Hermitian structures — heavy tools for the primary reader — without saying why the archimedean realisation needs them. H2: no instance ($S^3=\mathrm{SU}(2)$ with its standard contact form).
- **Suggested rewrite:** 'Over $\mathbb R$ or $\mathbb C$ the categorical data become geometry on a manifold. The model case is $S^3=\mathrm{SU}(2)$: the Hopf circles give a contact structure, and the plane field orthogonal to them carries a complex structure (a CR structure). This section describes that dictionary.'

#### `c-quantum-universe` — example `ex:c-quantum-universe` — T = 10/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H5: L1 'A quantum universe over $K$ is realised by the 4-tuple $(\mathbf C,\varTheta,G,\mathcal S)$' — the relation between this 4-tuple and the triple $(\mathbf C,A,\tau)$ of def:quantum-universe is never stated; L9 sets $\mathbf C=\mathrm{Rep}(\mathrm{SU}_{q(p)}(2))$ with a point-dependent $q(p)$ and no explanation of a category varying with $p$. H7/H4: Levi form, Webster metric, signature $(r,s)$ all appear without use.
- **Suggested rewrite:** Open with the dictionary: 'The triple $(\mathbf C,A,\tau)$ is realised as follows: $A=\mathcal O_q(\mathrm{SU}(2))$, ... ; the extra geometric data $(\varTheta,\mathcal S)$ on a manifold $M$ is what the archimedean setting adds.' Keep only the CR data used later.

#### `c-quantum-observable-universe` — example `ex:c-quantum-observable-universe` — T = 9/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 0
- **Evidence:** H8: L6 '$\Gamma_c(M,\mathcal S)=0$' — sections of a $\mathbb P^1$-bundle do not form a vector space, so 'vanishing' has no meaning as stated; L9 'the irreducibility of the instanton connection' invokes an object not introduced. H5: L9 'force $H^0(M,\mathrm{Ad}(P))=0$' is stated without argument.
- **Suggested rewrite:** State the condition on a linear object (e.g. sections of the associated vector bundle $P\times_G\mathbb C^2$) and cite where the connection is introduced. 'Observability becomes: the adjoint bundle has no non-zero parallel sections.'
- **Also:** needs_owner (content): 'Γ_c(M, S) = 0' for a P^1-bundle is not well-defined.

#### `archimedean-realisations` — remark `rem:archimedean-realisations` — T = 7/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 0, H5 1, H6 2, H7 0, H8 0
- **Evidence:** H5/H8: L3 'the rank-4 distribution $H=\ker\varTheta$' — on the 3-manifold $\mathrm{SU}(2)$ a contact distribution has rank 2; 'The induced Hodge star forces the structure group to be $\mathrm{SU}(2)$' and L5 '$\mathrm{Ric}_{g_\varTheta}=T^{(q)}$', '$J\hbar_q\iota_{\xi_q}D_A\psi=\hat H_q\psi$' are asserted, with $T^{(q)}$, $\hat H_q$, $D_A$ undefined. H7: Einstein and Schrödinger equations dropped in unframed.
- **Suggested rewrite:** Keep items 1-2 with the rank fixed (or state $\dim M$). Replace item 3 with a pointer: 'The variational equations of §... become an Einstein-type equation and a Schrödinger-type equation (thm:...).' Define each symbol where it is used.
- **Also:** needs_owner (content): rank of H (4 vs 2) depends on dim M, which is not stated.

#### `categorical-dirac-operator-intro` — prose `sec:categorical-dirac-operator-intro` — T = 12/16 (warn)

- **Scores:** H1 2, H2 1, H3 2, H4 1, H5 2, H6 2, H7 1, H8 1
- **Evidence:** H8: L1 'This formula defines a unique morphism in $\mathbf C$ once $\nabla$, $q$, and $\xi$ are fixed' belabours the triviality that a formula defines a map; the name 'Dirac' (no Clifford action appears) is not justified. H4: 'gauge and matter terms of the categorical action' anticipates notation not yet introduced.
- **Suggested rewrite:** 'We combine $\nabla$, $q$ and $\xi$ into one first-order operator $\mathcal D_\nabla$, interpolating between $\nabla$ ($q=1$) and its Reeb component $\iota_\xi\nabla$ ($q\to\infty$). We call it a Dirac operator because ...'.

#### `categorical-dirac-operator` — definition `def:categorical-dirac-operator` — T = 8/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 0, H5 0, H6 2, H7 1, H8 1
- **Evidence:** H4/H5: L6 adds $q^{-1}\nabla$, a map $A\to A\otimes\Omega^1(A)$, to $(1-q^{-1})\iota_\xi\nabla$, a map $A\to A$, and declares the sum $A\to\Omega^1(A)$ — three different targets. H3/H2: no example (for $\mathrm{SU}(2)$ at $q=1$, $\mathcal D=d$).
- **Suggested rewrite:** Make the target explicit: e.g. '$\mathcal D_\nabla=q^{-1}\nabla+(1-q^{-1})\,\varTheta\otimes\iota_\xi\nabla$', so both terms land in $A\otimes\Omega^1(A)$ — or whichever typing is intended. Add the $\mathrm{SU}(2)$ instance.
- **Also:** needs_owner (content): type mismatch of the two summands.

#### `categorical-dirac-operator-unique` — proposition `prop:categorical-dirac-operator-unique` — T = 10/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 2, H5 2, H6 2, H7 1, H8 0
- **Evidence:** H8: the proposition says the operator 'is uniquely determined by the formula' and that anything equal to the formula equals it — a tautology stated as a result.
- **Suggested rewrite:** Delete, or replace with a statement that has content (e.g. characterise $\mathcal D_\nabla$ as the unique operator with given limits and linear dependence on $q^{-1}$).

#### `categorical-lagrangian-intro` — prose `sec:categorical-lagrangian-intro` — T = 10/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H4/H5: L1 places $\psi^*\otimes\mathcal D_\nabla\psi$ in $\mathrm{End}_{\mathbf C}(A)$, but $\psi^*\colon A\to\mathbf1$ tensored with $\mathcal D_\nabla\psi\colon\mathbf1\to\Omega^1(A)$ is a map $A\to\Omega^1(A)$. H8: 'This endomorphism exists uniquely once ... are chosen' is trivial; 'bosonic and fermionic sectors' presumes physics.
- **Suggested rewrite:** 'The Lagrangian is an endomorphism of $A$ built from $\mathcal D_\nabla$ and a state $\psi$; its trace will be the action. Physically the two summands are the field and the matter terms (rem:...).' Fix the typing in the definition.

#### `categorical-lagrangian` — definition `def:categorical-lagrangian` — T = 9/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 0, H6 2, H7 1, H8 1
- **Evidence:** H5: L6 squares $\mathcal D_\nabla$, whose source and target differ ($A\to\Omega^1(A)$), and L8 adds a map $A\to\Omega^1(A)$ to it, while L9 asserts the sum is in $\mathrm{End}_{\mathbf C}(A)$. H8: 'bosonic sector', 'fermionic coupling' presume physics.
- **Suggested rewrite:** State the maps that make $\mathcal D_\nabla^2$ and $\psi^*\otimes\mathcal D_\nabla\psi$ endomorphisms of $A$ (e.g. contraction with $\int_A$ or the extension to $\Omega^\bullet$). Move the bosonic/fermionic reading to a remark.
- **Also:** needs_owner (content): D_∇^2 and the sum are not typed as endomorphisms of A.

#### `categorical-action-intro` — prose `sec:categorical-action-intro` — T = 8/16 (fail)

- **Scores:** H1 1, H2 1, H3 2, H4 0, H5 1, H6 1, H7 1, H8 1
- **Evidence:** H4/H6: L3 displays the gravity, gauge and matter terms with $R_{\int}$, $\wedge_q$, $\star_q$, $\mathrm{tr}_A$ and a scalar named $\lambda$ (again the block index) — before any is defined (they are defined in sec:categorical-action-notation, after the definition). The guide asks that the action be motivated before it is displayed; here the display is the motivation.
- **Suggested rewrite:** Keep L1 (good: 'The rigid duality supplies the trace; no spacetime measure is invoked'). Replace L3 with: 'Its trace splits into three terms — curvature of the Frobenius form, the curvature of $\nabla$, and the coupling to $\psi$ — which we read as gravity, gauge field and matter (thm:...).'

#### `categorical-action` — definition `def:categorical-action` — T = 13/16 (warn)

- **Scores:** H1 2, H2 1, H3 2, H4 1, H5 1, H6 2, H7 2, H8 2
- **Evidence:** H4/H5: L6-13 use $\mathrm{ev}_A\colon A^\vee\otimes A\to\mathbf1$ and $\mathrm{coev}_A\colon\mathbf1\to A\otimes A^\vee$, the opposite conventions to def:snake-identity, and the composite $(\mathrm{id}_{A^\vee}\otimes\Phi)\circ\mathrm{coev}_A$ does not typecheck ($\mathrm{coev}_A$ lands in $A\otimes A^\vee$). H2: no instance of the categorical trace (for $\mathrm{Vect}$: the trace of a matrix).
- **Suggested rewrite:** Write $\mathfrak S=\mathrm{ev}_A\circ(\Phi\otimes\mathrm{id}_{A^\vee})\circ\widetilde{\mathrm{coev}}_A$ with the conventions of def:snake-identity stated once; add 'In $\mathrm{Vect}_{\mathbb C}$ this is $\mathrm{tr}(\Phi)=\sum_i e^i(\Phi e_i)$.'

#### `categorical-action-notation` — prose `sec:categorical-action-notation` — T = 10/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 0, H5 2, H6 2, H7 1, H8 1
- **Evidence:** H4: L3 '$\nabla_{\int}(a)=\int_A(a_{(1)})\otimes a_{(2)}-a\otimes1$' subtracts an element of $A\otimes A$ from one of $\mathbf1\otimes A$; L6 introduces $D_\nabla$ although the same operator is $\mathcal D_\nabla$ in def:categorical-dirac-operator. H3: the list comes after the definitions that use it.
- **Suggested rewrite:** Use $\mathcal D_\nabla$ throughout. Fix the typing of $\nabla_{\int}$. Place this notation block before sec:categorical-action-intro.

#### `categorical-action-notation-su2` — example `ex:categorical-action-notation-su2` — T = 11/16 (fail)

- **Scores:** H1 2, H2 2, H3 1, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H8: L3 calls the categorical trace on $\mathrm{End}(\mathcal O(\mathrm{SU}(2)))$ 'the usual matrix trace' $\sum_m\langle j,m|T|j,m\rangle$ — $A$ is infinite-dimensional and a single $j$ is fixed with no explanation; L4 '$R_{\int}=0$ in the classical limit' is asserted. H4: bra-ket notation appears nowhere else in the chapter.
- **Suggested rewrite:** L3: 'On each isotypic block $V_j\otimes V_j^*\subset A$ the categorical trace is the matrix trace; on $A$ itself it needs a regularisation (§...).' Give the one-line reason $R_{\int}=0$ (Haar measure is bi-invariant).

#### `qou-canonical-action` — proposition `prop:qou-canonical-action` — T = 8/16 (fail)

- **Scores:** H1 1, H2 1, H3 2, H4 0, H5 1, H6 1, H7 1, H8 1
- **Evidence:** H4/H5: L10 equates an operator $\mathcal D_\nabla^2$ with a sum containing a partial trace $\mathrm{tr}_A(F\wedge_q\star_qF)$, and L17-19 then wrap $\int_A\mathrm{tr}_A$ around it again; $\lambda$ (L1) is reused for a normalisation scalar. H6: the 'gravity + gauge + matter' identification is carried by underbraces, not prose. Physical labels sit inside the proposition statement.
- **Suggested rewrite:** State the proposition as an algebraic identity with typed terms ('$\mathrm{tr}(\mathcal L_q)=a+b+c$ where ...'), and put the gravity/gauge/matter reading and the Hamilton analogy (L22, which is good) in a following remark. Rename $\lambda$.

#### `canonical-action-obstruction` — remark `rem:canonical-action-obstruction` — T = 8/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 0, H5 1, H6 2, H7 0, H8 1
- **Evidence:** H5: L1 'The observability axiom ... ensures that the trace ... is faithful' — the step from no invariant vectors in $\mathrm{Ad}(A)$ to faithfulness of the trace is not given. H4/H7: L1 '$\kappa\in H^2(\mathcal S,\mathcal B)$ ... in the quantum-lifting sense' introduces a class and a pair of spaces with no definition or pointer.
- **Suggested rewrite:** Give the argument or a pointer for faithfulness. Replace the last sentence with a cross-reference: 'The obstruction to defining the action without observability is the lifting class of Chapter 3 (def:...).'

#### `variational-equations-intro` — prose `sec:variational-equations-intro` — T = 12/16 (warn)

- **Scores:** H1 2, H2 1, H3 2, H4 1, H5 2, H6 2, H7 1, H8 1
- **Evidence:** H8: L1 'to predict a material-dependent torsion phase shift' presents a physical prediction in a section intro without flagging it as the comparison point. H4: 'Reeb diffraction' is undefined.
- **Suggested rewrite:** 'Varying the three inputs gives three equations, analogues of the Einstein, Yang–Mills and Dirac equations. As an illustration we follow the matter equation through a double-slit geometry (ex:photon-wavefront); that example is where a comparison with experiment would be made.'

#### `variational-equations` — proposition `prop:variational-equations` — T = 9/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 1, H6 1, H7 1, H8 1
- **Evidence:** H8/H6: three field equations are stated with no indication of how they follow (e.g. what 'vary $\int_A$' means for a Frobenius form, or why a $q[F,\star_qF]$ term appears); $T_q$ is 'constructed from the gauge and matter terms' without formula. H4: $D_\nabla$ here, $\mathcal D_\nabla$ elsewhere; $J_\psi$ is built from $\psi^*\otimes D_\nabla\psi$, whose type is not stated.
- **Suggested rewrite:** Add one sentence per equation saying which variation produces which term, and point to the proof block. Use $\mathcal D_\nabla$. Give $T_q$ explicitly or cite it.

#### `wavefront-propagation` — remark `rem:wavefront-propagation` — T = 9/16 (fail)

- **Scores:** H1 1, H2 1, H3 2, H4 1, H5 1, H6 2, H7 1, H8 0
- **Evidence:** H8: L5 'transported along geodesics of the connection $\nabla$', L8 'the Gaussian beam waist $w_0$ is fixed by $q$', 'At a material boundary, $F_\nabla\ne0$' and 'The on-shell condition eliminates the matter term ... leaving only the topological gauge sector' are physical assertions with no derivation; the instanton background is not defined. H1: L1 restates the transport equation.
- **Suggested rewrite:** Mark the remark as heuristic: 'We read the two terms of $\mathcal D_\nabla$ physically: ... This reading is not derived here.' Remove claims about beam waist and material boundaries unless a derivation is cited.

#### `photon-wavefront-example` — example `ex:photon-wavefront` — T = 5/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 0, H5 1, H6 1, H7 0, H8 0
- **Evidence:** H4: the torsion phase is called $\tau(y)$ (L8), the paper's symbol for the fibre functor; $\lambda$ (L11) is a wavelength; $\varphi_i\sigma_i$, 'colour content', 'the exceptional divisor', $K_{\mathrm{mat}}$ are undefined. H8/H7: the phase formula $\tau(y)=\hbar_q\mathrm{Vol}(K_{\mathrm{mat}})\eta^2kw$ (L8) and its colour correction (L24) are posited, not derived from $\mathcal D_\nabla\psi=0$; L27 claims 'a measurable signature distinct from classical birefringence'.
- **Suggested rewrite:** Rename the phase ($\phi(y)$) and the wavelength ($\lambda_{\rm opt}$ or use $k$ only). Either derive the phase formula from the transport equation or label it an ansatz and move the measurability claim to an explicitly marked comparison remark with its experimental status.
- **Also:** needs_owner (content/anti-fit): the torsion-phase formula is posited, not derived; L27 asserts a measurable prediction.

#### `categorical-q-ext-deriv` — definition `def:categorical-q-ext-deriv` — T = 11/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 2, H5 2, H6 2, H7 1, H8 1
- **Evidence:** H1: the same operator $d_q$ is defined in def:substrate-parameter (same formula). H8: L7 'These operators exist and are unique' inside a definition; $\delta_q$ is 'the formal adjoint ... with respect to the dagger structure' with no inner product on forms specified.
- **Suggested rewrite:** Keep one definition of $d_q$ and cite it. Define the inner product on $\Omega^\bullet(A)$ (via $\star_q$ and $\int_A$) before $\delta_q$. Delete 'These operators exist and are unique.'

#### `categorical-q-ext-deriv-exists` — proposition `prop:categorical-q-ext-deriv-exists` — T = 10/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 2, H5 2, H6 2, H7 1, H8 0
- **Evidence:** H8: the proposition asserts that an explicit composite of morphisms of $\mathbf C$ 'exists as a morphism in $\mathbf C$' — true by construction, stated as a result.
- **Suggested rewrite:** Remove the proposition, or replace it with the non-trivial property it should carry (e.g. $d_q^2=0$, or $d_q$ is a graded derivation), if that is intended.

#### `categorical-q-ext-deriv-unique` — proposition `prop:categorical-q-ext-deriv-unique` — T = 8/16 (fail)

- **Scores:** H1 0, H2 1, H3 1, H4 2, H5 1, H6 2, H7 0, H8 1
- **Evidence:** H1/H7: L14 is a generic 'Archimedean specialisation' paragraph ('real-valued physical observables, real-analytic bounds, transcendental constants ...') appended to a purely algebraic uniqueness statement it does not describe. H5: condition 3 'R-linear in the components' is vague.
- **Suggested rewrite:** Delete L14. State: 'Since $\Omega^k=\Omega^k_H\oplus\Omega^k_V$, an $R$-linear map is determined by its restrictions; conditions 1–2 therefore determine $d_q$.'
- **Also:** boilerplate: L14 generic 'Archimedean specialisation' stamp that does not match the block.

#### `fermion-boson-decomposition` — definition `def:fermion-boson-decomposition` — T = 10/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H4: $\Delta_q$ (L1) is used without definition; 'the space of particles' names $\ker\Delta_q$ by a physics word. H5: L7 calls $\mathcal H^k_{q,H}$ 'the kernel' (it is the subobject), and defines a fermion as 'a particle with $\alpha_V\ne0$', which is not the same set as $\mathcal H^k_{q,V}$ in the splitting.
- **Suggested rewrite:** 'Let $\Delta_q=d_q\delta_q+\delta_qd_q$ and $\mathcal H^k_q=\ker\Delta_q$ (harmonic forms). We call the horizontal harmonic forms bosonic and the summand $\mathcal H^k_{q,V}$ fermionic; remark ... explains the names.'

#### `categorical-point` — definition `def:categorical-point` — T = 12/16 (warn)

- **Scores:** H1 2, H2 2, H3 1, H4 1, H5 1, H6 2, H7 2, H8 1
- **Evidence:** H5: L1 defines a point as a morphism $p\colon\mathbf1\to A$ (an element of $A$) and then says it 'corresponds to evaluation at $p\in M$', which is a map $A\to\mathbf1$; L1 then writes $p^*\colon A\to\mathbf1$ without saying how $p$ determines it.
- **Suggested rewrite:** 'A categorical point is a morphism of algebras $\mathrm{ev}_p\colon A\to\mathbf1$; for $A=C^\infty(M)$ these are evaluations at points of $M$.' Or keep $p\colon\mathbf1\to A$ and explain $p^*$ via the Frobenius pairing.

#### `categorical-point-explication` — prose `sec:categorical-point-explication` — T = 11/16 (fail)

- **Scores:** H1 1, H2 2, H3 1, H4 1, H5 1, H6 2, H7 2, H8 1
- **Evidence:** H1: restates def:categorical-point (point, augmentation ideal, germ). H5: L2 says a point $p\colon\mathbf1\to A$ 'is a character $\mathrm{ev}_g\colon f\mapsto f(g)$' — a character is a map $A\to\mathbf1$; L23 then defines $p^*$ through the Frobenius pairing, a different recipe from the definition's.
- **Suggested rewrite:** Merge with def:categorical-point and give one consistent account: 'a point is an algebra map $A\to\mathbf1$; via the Frobenius pairing it corresponds to an element $p\colon\mathbf1\to A$ (a delta function).' Keep the $\mathcal O(G)$ and $C^\infty(M)$ instances, which are good.

#### `observation` — definition `def:observation` — T = 7/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 0, H5 1, H6 2, H7 0, H8 1
- **Evidence:** H4/H7: the definition requires a state bundle $\mathcal S\to M$, an 'open causal neighbourhood', $\mathrm{Ad}(J^1\mathcal S)$, 'the colour fibre', and a Hopf-coaction formula for $\delta q$, none defined in Chapters 1-2 at this point. H5: L5 shifts $q\in\mathrm{End}(\mathbf1)$ (a fixed scalar of the universe) by a point-dependent $\delta q(p)$ without saying in what sense $q$ varies. H3: the purpose is given only at L7, after the axioms.
- **Suggested rewrite:** Lead with L7's picture ('An observation reads a field and its derivative at a point, and acts back on it'). Define or cite each ingredient before use, and state the model in which $q$ is a function on $M$ before writing $q+\delta q$.

#### `observation-physical-roles` — remark `rem:observation-physical-roles` — T = 12/16 (warn)

- **Scores:** H1 1, H2 2, H3 2, H4 1, H5 2, H6 2, H7 1, H8 1
- **Evidence:** H1: repeats L7 of def:observation almost verbatim. H8: 'the observation perturbs $q$, which shifts the Reeb flow, which changes what the next observation reads' is a causal story with no construction behind it; 'the affine chart (fibre functor atlas)' conflates two notions of chart (see rem:fibre-functor-atlas-affine-charts).
- **Suggested rewrite:** Merge into def:observation as its motivating sentence, or keep as an explicitly heuristic remark: 'Heuristically, ...'.

#### `observation-energy` — proposition `prop:observation-energy` — T = 8/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 0
- **Evidence:** H8: the computation $\hbar_{q+\delta q}-\hbar_q=\delta q/(q(q+\delta q))>0$ (L4) is the monotonicity of $1-1/q$; L7 calls $\hbar_q$ 'the quantum energy of the system' and L15 asserts 'only the quantum energy monotonically increases' — physical conclusions not supported by the algebra. L12 is a first-order Taylor expansion presented as a result.
- **Suggested rewrite:** State the content: '$\hbar_q$ is increasing in $q$.' Move the reading of $\hbar_q$ as energy, and the 'observation cost', to a remark marked as interpretation, or derive them.

#### `two-observer-parallelogram` — remark `rem:two-observer-parallelogram` — T = 7/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 1, H5 0, H6 2, H7 1, H8 0
- **Evidence:** H5/H8: L4 forms the commutator $[q_1'(p),q_2'(p)]$ of two values of the substrate parameter, which lives in $\mathrm{End}(\mathbf1)\cong R$, a commutative ring, so the commutator is zero; L7 'The non-cocommutativity of the Hopf structure ensures $[q_1',q_2']\ne0$' is therefore unsupported. L9 identifies the commutator with a curvature $F_q$ not yet defined.
- **Suggested rewrite:** State in which non-commutative algebra the increments $\delta q_i$ live (e.g. as elements of the germ algebra $A/\mathfrak m_p^2$ acting by multiplication) before forming their commutator.
- **Also:** needs_owner (content): commutator of elements of the commutative ring End(1) ≅ R.

#### `germ-commutator-q-curvature` — proposition `prop:germ-commutator-q-curvature` — T = 8/16 (fail)

- **Scores:** H1 1, H2 1, H3 2, H4 1, H5 0, H6 2, H7 1, H8 0
- **Evidence:** H5/H8: L9 '$[\delta q_1,\delta q_2]=F_q$' — increments in $A/\mathfrak m_p^2$, which for the archimedean model $A=C^\infty(M)$ is commutative, so the left side vanishes identically; L28 concedes this ('over a commutative ring the parallelogram would close'). L31-37 'is unconditional (structural); the identification ... is the narrative bridge' is editorial and does not say which part is proved.
- **Suggested rewrite:** Separate the claim from its interpretation: state in which (non-commutative) $A$ the identity holds and what is proved; remove 'narrative bridge' and say plainly 'The identification with ... is not proved here.'
- **Also:** needs_owner (content): the commutator vanishes for commutative A, which includes the archimedean realisation.

#### `q-harmonic-flow` — conjecture `conj:q-harmonic-flow` — T = 11/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 2, H6 2, H7 1, H8 1
- **Evidence:** H4: $\Delta_q$ here (L6, an operator on the scalar function $q$) is a different object from $\Delta_q=d_q\delta_q+\delta_qd_q$ on forms (def:fermion-boson-decomposition, rem:q-laplacian-interpretation); $\mathfrak C$ and $\Delta_\xi$ are named but not defined. H3: why $q$ should evolve by a heat flow is not motivated.
- **Suggested rewrite:** Rename (e.g. $\Box_q$), define $\mathfrak C$ and $\Delta_\xi$ or cite them, and open with the motivation: 'If $q$ varies over $M$, the simplest evolution compatible with ... is a heat flow.'

#### `observation-fermion-action` — remark `rem:observation-fermion-action` — T = 9/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 0
- **Evidence:** H8: L9 'the Ad action conjugates the antisymmetric component by $G$, mixing the fermionic state with the bosonic eigenspace' — $\mathrm{Sym}^2V$ and $\Lambda^2V$ are $G$-subrepresentations, so the $G$ action does not mix them; 'depositing $q+q^{-1}$ per crossing in the colour fibre' is unexplained. H4: 'bosonic'/'fermionic' label the symmetric/antisymmetric two-particle spaces without saying so.
- **Suggested rewrite:** State which operator mixes the summands (it cannot be the $G$-action), or delete the mixing claim. 'Call $\mathrm{Sym}^2V$ the bosonic and $\Lambda^2V$ the fermionic two-particle space.'
- **Also:** needs_owner (content): G-equivariance contradicts the claimed mixing of Sym^2 V and Λ^2 V.

#### `geometric-interpretations-intro` — prose `sec:geometric-interpretations-intro` — T = 10/16 (fail)

- **Scores:** H1 1, H2 1, H3 2, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H8/H4: L1 'identifies equilibrium between the spatial environment and internal quantum spin' and 'Coriolis cross-coupling' are metaphors offered as identifications; L3 'A particle is simultaneously $q$-closed and $q$-coclosed' defines 'particle' in passing; L3's last sentence about $q$ acquiring a phase is unrelated to the section.
- **Suggested rewrite:** 'We translate $d_q$, $\delta_q$ and $\Delta_q$ into vector calculus (rem:vector-calculus-bridge). $\Delta_q$ splits into a base Laplacian, a cross term and a fibre Laplacian (prop:...). We call harmonic forms particles.' Delete the phase sentence.

#### `vector-calculus-bridge` — remark `rem:vector-calculus-bridge` — T = 15/16 (warn)

- **Scores:** H1 2, H2 2, H3 2, H4 1, H5 2, H6 2, H7 2, H8 2
- **Evidence:** H4 (minor): L5 'the curl $d\alpha$ on a 1-form' and 'gradient $df$' identify forms with vector fields without the $\sharp$/$\star$ that does it (the curl is $\star d\alpha$ in dimension 3); $n$ is used before it is introduced. Otherwise a model reminder-remark for the primary reader.
- **Suggested rewrite:** '... gives the gradient $(df)^\sharp$ and, in dimension $n=3$, the curl $(\star d\alpha)^\sharp$.'

#### `q-laplacian-interpretation` — remark `rem:q-laplacian-interpretation` — T = 13/16 (warn)

- **Scores:** H1 1, H2 2, H3 2, H4 2, H5 2, H6 2, H7 1, H8 1
- **Evidence:** H8: L3 'the field $\alpha$ is in equilibrium between its spatial environment and its internal quantum spin' and L7 'A $q$-harmonic form ... is a particle' are interpretive statements presented as identifications. H1: L7 repeats L3.
- **Suggested rewrite:** Mark the reading as interpretation once ('We read $\Delta_q\alpha=0$ as a balance between ...'), keep the two limits (good), and drop L7's repetition.

#### `q-codifferential-formula-prop` — proposition `prop:q-codifferential-formula` — T = 10/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H4/H5: L1 writes $d_q=q^{-1}d+(1-q^{-1})\varTheta\wedge\mathcal L_\xi$, a third formula for $d_q$ beside $q^{-1}d+(1-q^{-1})\pi_Vd$ (def:categorical-q-ext-deriv); the equivalence is not stated. The Webster inner product and $\mathcal L_\xi^*$ are undefined here.
- **Suggested rewrite:** 'Using $\pi_V d=\varTheta\wedge\mathcal L_\xi$ (lemma ...), $d_q=\dots$.' Define $\langle\cdot,\cdot\rangle_\varTheta$ (the $L^2$ product of the Webster metric) before the formula.

#### `q-codifferential-formula` — remark `rem:q-codifferential-formula` — T = 15/16 (warn)

- **Scores:** H1 2, H2 2, H3 2, H4 2, H5 2, H6 2, H7 2, H8 1
- **Evidence:** H8 (minor): L2-4 'each operation is replaced by its geometric mirror' presents the adjoint rule as a recipe; it is correct only because $\varTheta\wedge$ and $\iota_\xi$ are adjoint for the Webster metric with $|\varTheta|=1$, which is the step that needs saying. Otherwise a clear remark.
- **Suggested rewrite:** Add: 'Since $\varTheta(\xi)=1$ and $\xi$ is unit-length for the Webster metric, $\iota_\xi$ is the adjoint of $\varTheta\wedge$; adjoints of composites reverse order, so ...'.

#### `q-laplacian-expansion` — remark `rem:q-laplacian-expansion` — T = 14/16 (warn)

- **Scores:** H1 2, H2 1, H3 2, H4 2, H5 2, H6 2, H7 2, H8 1
- **Evidence:** H8: the three labels 'classical core', 'quantum spin core', 'interference between macroscopic spatial motion and internal spin' (L3-5) name terms of an operator expansion with physical words that the block does not justify. H2: no instance (e.g. on functions on $S^3$, where $\Delta_\xi$ is $-\xi^2$).
- **Suggested rewrite:** Keep the expansion; describe the terms by what they are ('the base Laplacian', 'the fibre Laplacian $\Delta_\xi$', 'mixed terms'), and add: 'On functions on $\mathrm{SU}(2)$, $\Delta_\xi=-\xi^2$, the Laplacian along the Hopf circles.'

#### `q-laplacian-spectral-tower` — proposition `prop:q-laplacian-spectral-tower` — T = 9/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 2, H5 1, H6 2, H7 0, H8 0
- **Evidence:** H8: L1 asserts that $\Delta_q$ 'has eigenvalues given by the $q$-integer tower $[k]_q^2$' with no space (forms on which manifold?), no multiplicities, and no argument. H7: L13 invokes 'Verlinde / ADE quantum-dimension data' unframed. H5: L13 places $[k]_q$ at $q=e^{i\pi/r}$ in $\mathbb Q(\zeta_r)$, though it lies in $\mathbb Q(\zeta_{2r})$ (real subfield).
- **Suggested rewrite:** State the space and cite or prove the spectrum ('On $\Omega^0$ of $\mathcal O_q(\mathrm{SU}(2))$, the isotypic block $V_j$ is an eigenspace with eigenvalue ... (thm:...)'). Replace 'Verlinde / ADE data' with one sentence on what truncation at a root of unity means.
- **Also:** needs_owner (content): eigenvalue claim is unsupported as stated.

#### `q-laplacian-consumers` — remark `rem:q-laplacian-consumers` — T = 9/16 (fail)

- **Scores:** H1 1, H2 1, H3 2, H4 0, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H4/H5: a remark listing uses of the tower in later chapters — '$q$-Navier–Stokes dissipation', 'Markov trace / Gram blocks', 'the lifting obstruction tower caps at $r-1$' — none introduced, with '$[k]_q^2\sim q^{2k}$' (it is $\sim q^{2k-2}$).
- **Suggested rewrite:** Either delete (the forward pointers belong in the later chapters) or reduce to one sentence: 'The same numbers $[k]_q^2$ reappear as heat-decay rates (§...) and as block dimensions of the Markov trace (§...).'

#### `hodge-laplacian-relation` — remark `rem:hodge-laplacian-relation` — T = 12/16 (warn)

- **Scores:** H1 2, H2 1, H3 1, H4 2, H5 2, H6 2, H7 1, H8 1
- **Evidence:** H8: L1 asserts that $\Delta_q$ is formally self-adjoint and L3 that $\ker\Delta_q$ 'is a well-defined subspace with a canonical complement' — the complement needs Hodge theory (elliptic operator, compactness), not formal self-adjointness alone. H1: L1 restates def:q-hodge-star.
- **Suggested rewrite:** '$\Delta_q$ is formally self-adjoint (prop:q-codifferential-formula), so its eigenvalues are real. On a compact manifold elliptic theory gives $\Omega=\ker\Delta_q\oplus\mathrm{im}\,\Delta_q$ [cite]; whether $\Delta_q$ is elliptic is ...'.

#### `categorical-lichnerowicz` — proposition `prop:categorical-lichnerowicz` — T = 8/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 0, H5 1, H6 2, H7 1, H8 0
- **Evidence:** H4: the Dirac operator is written $\mathfrak D_\nabla$ here, $\mathcal D_\nabla$ in its definition and $D_\nabla$ in the notation block — three glyphs, one operator; $\Delta^q_\nabla$ and $\mathrm{Sc}_q$ are new and undefined. H8: L7 'On the Bring background, the Reeb generator $\xi=e_3$ is parallel, forcing $\mathrm{Sc}_q=0$' and 'the $q$-anomaly contribution from $d_q^2\neq0$' are asserted; the classical Lichnerowicz formula needs a spin structure and Clifford multiplication, neither present.
- **Suggested rewrite:** Use $\mathcal D_\nabla$. Define $\Delta^q_\nabla$ and $\mathrm{Sc}_q$ before the identity; recall the classical Lichnerowicz formula $D^2=\nabla^*\nabla+\tfrac14\mathrm{Sc}$ and say which ingredient replaces Clifford multiplication. Give the argument for $\mathrm{Sc}_q=0$ or cite it.

#### `q-harmonic-particle` — remark `rem:q-harmonic-particle` — T = 12/16 (warn)

- **Scores:** H1 1, H2 1, H3 2, H4 2, H5 1, H6 2, H7 2, H8 1
- **Evidence:** H5: L1 cites 'positive-definiteness of $\Delta_q$' — a positive-definite operator has zero kernel, so there would be no $q$-harmonic forms; positive semi-definiteness is meant. H1: L7 restates def:fermion-boson-decomposition; L9's arrow chain is ceremony.
- **Suggested rewrite:** 'Since $\langle\Delta_q\alpha,\alpha\rangle=\|d_q\alpha\|^2+\|\delta_q\alpha\|^2\ge0$, $\Delta_q\alpha=0$ iff $d_q\alpha=0$ and $\delta_q\alpha=0$.' Delete L9.

#### `brings-geometric-connection` — remark `rem:brings-geometric-connection` — T = 9/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 2, H5 1, H6 2, H7 1, H8 0
- **Evidence:** H8: L1 promises that the contact structure, Reeb field and $q$ 'reduce to explicit formulas' and 'computable eigenvalue problems' on Bring's surface but gives none. H5: a contact form needs odd dimension; on the genus-4 Riemann surface (real dimension 2) there is no contact structure, so the structure must live on a circle bundle over it, which is not said.
- **Suggested rewrite:** Either give one explicit formula, or replace with a pointer: 'On the unit circle bundle of Bring's curve these structures are explicit; see §...'.
- **Also:** needs_owner (content): contact structure on a 2-dimensional surface.

#### `complex-substrate-interpretation` — remark `rem:complex-substrate-interpretation` — T = 10/16 (fail)

- **Scores:** H1 1, H2 1, H3 2, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H4: L9 writes the root-of-unity specialisation as $q_0=e^{\pi i/\kappa}$, reusing $q_0$ (the calibrated real value) and $\kappa$. H8: L3 '$d_q^\dagger$ is the formal adjoint of $d_q$ ... if and only if $q\in\mathbb R_{>0}$' and the three consequences (L5-7) are asserted without argument.
- **Suggested rewrite:** Write $\zeta=e^{\pi i/\ell}$. Mark L5-7 as heuristic or give the computation for one of them.

#### `categorical-self-duality` — proposition `prop:categorical-self-duality` — T = 10/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 2, H5 2, H6 2, H7 1, H8 0
- **Evidence:** H8: L1-7 'Every connection that is a critical point of the categorical Yang–Mills functional is an instanton' — classically false (non-self-dual Yang–Mills critical points exist on $S^4$, Sibner–Sibner–Uhlenbeck 1989), and no hypothesis restricting the claim is stated. H1/H7: L9-14 discuss what the Lean declaration does not carry.
- **Suggested rewrite:** Add the hypothesis under which the implication holds (e.g. minimisers in a fixed topological class, via the Bogomolny bound) and say 'absolute minimiser' rather than 'critical point'. Move L9-14 to an author note.
- **Also:** proof-no-lean-mention-in-prose: L10-14 discuss `QOU.categorical_self_duality` and `CategoricalInstanton`. needs_owner (content): 'critical point ⟹ instanton' needs a minimising hypothesis.

#### `instanton-on-shell` — remark `rem:instanton-on-shell` — T = 9/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 0
- **Evidence:** H4/H5: L4 writes $c_2(A)$ (a Chern class of the algebra object?) where the bundle is $\mathrm{Ad}(A)$, and L7 sets the operator $\mathcal D_\nabla^2$ equal to the number $c_2(A)$. H8: L13 'There are no dynamical gauge degrees of freedom beyond topology. All physics lies in the matter equation' is a strong physical conclusion stated without argument.
- **Suggested rewrite:** 'For a self-dual connection, $\|F\|^2=8\pi^2c_2$ (Bogomolny), so the gauge term of the action is topological.' Keep the operator/number distinction. Mark the last paragraph as interpretation.

#### `self-dual-ses` — remark `rem:self-dual-ses` — T = 9/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 0, H6 2, H7 1, H8 1
- **Evidence:** H5: L1 'The $q$-Hodge star $\star_q$ is an involution on $\Omega^2(A)$' — $\star_q$ maps $\Omega^2\to\Omega^{n-2}$, so this needs $n=4$, while the running $\mathrm{SU}(2)$ calculus has $n=3$ (ex:hodge-su2 says the self-dual split is then trivial); and with $\star_q=q\star$ (def:q-hodge-star), $\star_q^2=q^2\star^2\neq\mathrm{id}$ unless $q=\pm1$.
- **Suggested rewrite:** State the dimension: 'When the calculus has top degree 4, $\star$ preserves $\Omega^2$ ...' and use $\star$ (or $q^{-1}\star_q$) for the involution.
- **Also:** needs_owner (content): ⋆_q^2 = q^2 ⋆^2 is not an involution; dimension 4 vs 3.

#### `hopf-non-cocommutativity` — remark `rem:hopf-non-cocommutativity` — T = 11/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 2, H6 2, H7 1, H8 1
- **Evidence:** H4: L1 writes the flip as $\sigma$, the paper's symbol for the Hecke/braid generator $\sigma_i$ (AGENTS §7a); $\mathrm{Ad}_{R_q}$ is used without saying in what algebra $R_q$ lives. H8: 'the algebraic origin of quantum uncertainty, preventing independent observations from commuting' is an interpretive claim with no supporting construction.
- **Suggested rewrite:** 'Writing $\mathrm{flip}$ for $a\otimes b\mapsto b\otimes a$, the coproduct satisfies $\mathrm{flip}\circ\Delta=R\,\Delta(\cdot)\,R^{-1}$ with $R$ the universal $R$-matrix [Kassel VIII]; at $q=1$, $R=1$ and $\Delta$ is cocommutative.' Move the uncertainty reading to a remark.

#### `categorical-dq-squared` — proposition `prop:categorical-dq-squared` — T = 10/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H4: $\omega_V$ 'the curvature of the weight decomposition' and $\wedge_q$ (L4) are undefined; $[\xi,\alpha]$ is used for the Lie derivative. H5/H8: L9 'vanishes if and only if $q=1$ or $[\xi,\alpha]=0$' ignores the possibility that $\omega_V\wedge_q[\xi,\alpha]=0$ with both factors non-zero (e.g. in top degree).
- **Suggested rewrite:** Define $\omega_V$ (e.g. $d\varTheta$) and write $\mathcal L_\xi\alpha$. 'In particular $d_q^2=0$ when $q=1$ or when $\alpha$ is $\xi$-invariant; otherwise $d_q^2\alpha=\dots$ need not vanish.' Add the $\mathrm{SU}(2)$ instance.

#### `q-torsion-existence` — remark `rem:q-torsion-existence` — T = 8/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 0, H5 1, H6 2, H7 0, H8 1
- **Evidence:** H4/H7: in 52 words the remark invokes Legendrian submanifolds, KAM-type persistence, and 'the failure of the Frobenius structure on $H$' — 'Frobenius' here is the integrability theorem, colliding with the paper's Frobenius algebra; '$q$-torsion leaf' is defined in passing.
- **Suggested rewrite:** 'A contact distribution $H$ is maximally non-integrable (Frobenius' integrability theorem fails for it), so its integral submanifolds have at most half the dimension of $H$: these are Legendrian. We call a Legendrian submanifold invariant under the $q$-Reeb flow a $q$-torsion leaf.' Drop the KAM sentence or cite it.

#### `quantum-torsion-motivation` — remark `rem:quantum-torsion-motivation` — T = 12/16 (warn)

- **Scores:** H1 2, H2 2, H3 2, H4 2, H5 1, H6 2, H7 1, H8 0
- **Evidence:** H8: L5 'The spinor sign rule follows. The first $360^\circ$ rotation addresses the physical state in space; the second ... completes the quantum torsion reset' asserts a derivation of the $720^\circ$ property from a metaphor; the standard reason ($\mathrm{SU}(2)\to\mathrm{SO}(3)$ is a double cover) is not mentioned.
- **Suggested rewrite:** 'The sign rule for spinors is the fact that $\mathrm{SU}(2)\to\mathrm{SO}(3)$ is a double cover: a $2\pi$ rotation lifts to $-1$ and a $4\pi$ rotation to $+1$. We read the $q$-twist as a deformation of this cover.' (or drop L5).

#### `q-heat-equation` — definition `def:q-heat-equation` — T = 10/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H4/H5: L1 takes the archimedean 4-tuple $(\mathbf C,\varTheta,G,\mathcal S)$ as 'a quantum observable universe' (def:quantum-observable-universe is a triple $(\mathbf C,A,\tau)$); L7 'a section $u\colon\mathbb R_{\ge0}\times\mathcal S\to\mathbf 1_{\mathbf C}$' maps into an object of a category; '$t_P(q)=q/(q-1)$' introduces a time unit equal to $1/\hbar_q$ without saying so.
- **Suggested rewrite:** 'Let $u(t)$ be a time-dependent form on the archimedean realisation. The $q$-heat equation is $\partial_tu=-\Delta_qu$.' Note $t_P=1/\hbar_q$ if that unit is needed later.

#### `q-heat-equation-elaboration` — remark `rem:q-heat-equation-elaboration` — T = 7/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 1, H5 1, H6 1, H7 1, H8 0
- **Evidence:** H8: L1 'The Reeb time $t$ evolves at fixed cosmological time $q$' treats the substrate parameter as a time without construction. H6: L4 contains a placeholder '[Coriolis]' in place of an operator. H5: L7 'holds over any commutative ring in which $q-1$ is invertible' — $\partial_t$ has no meaning over an arbitrary ring.
- **Suggested rewrite:** Replace the display by the expansion of rem:q-laplacian-expansion (or cite it) with the cross term written out. Delete the 'cosmological time' sentence; replace L7 with 'The operator $\Delta_q$ is defined over $\mathbb Z[q,q^{-1}]$; the time derivative is archimedean.'

#### `categorical-laplace-transform` — definition `def:categorical-laplace` — T = 6/16 (fail)

- **Scores:** H1 2, H2 0, H3 1, H4 0, H5 1, H6 1, H7 0, H8 1
- **Evidence:** H4: $\mathcal L$ collides with the Lagrangian $\mathcal L_q$ of def:categorical-lagrangian; $\ast_q$, $\mathcal H_q$, $G(\mathcal H_q)$, $\exp_q(-s\cdot)$ and $\mathrm{tr}_M$ are used without definition. H7/H8: 'monoidal functor' between monoids, 'uniquely characterising it as the mate of the comultiplication' — heavy terms, no framing. H2: no classical anchor ($\int_0^\infty e^{-st}f(t)\,dt$ turns convolution into product).
- **Suggested rewrite:** Open with the classical Laplace transform and its convolution property; define $\exp_q$ and $\mathcal H_q$ before use; rename the transform (e.g. $\mathscr L$ or $\mathrm{Lap}_q$).

#### `q-resolvent-properties` — remark `rem:q-resolvent-properties` — T = 8/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 0, H5 0, H6 2, H7 1, H8 1
- **Evidence:** H5: L13 gives the eigenvalues of $\Delta_q$ on the $j$-isotypic part as $[j]_q[j+1]_q(1-q^{-1})^2$, while prop:q-laplacian-spectral-tower gives $[k]_q^2$; the two spectra disagree. H4: $R_q(s)$ and $\widehat{\Delta_q}$ are undefined; $\lambda_j$ reuses $\lambda$; $[j]_q$ for half-integer $j$ is not defined by the balanced formula.
- **Suggested rewrite:** Define $R_q(s)=(s+\Delta_q)^{-1}$ first. Reconcile the eigenvalue formula with prop:q-laplacian-spectral-tower (or state the different operator/space). Rename $\lambda_j$ to $\mu_j$.
- **Also:** needs_owner (content): spectrum disagrees with prop:q-laplacian-spectral-tower.

#### `laplace-fourier-wick-rotation` — remark `rem:laplace-fourier-wick-rotation` — T = 9/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 0, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H4: L7 '$\tau=t+i\varTheta$' reuses $\tau$ (the fibre functor) and $\varTheta$ (the contact form) as complex time and its imaginary part; $\xi$ (L4) is a frequency variable here but the Reeb field elsewhere. H8: 'securing base-ring independence where a primitive fourth root of unity exists' is unexplained.
- **Suggested rewrite:** '$\mathcal F[f](\omega)=\mathrm{Lap}[f](i\omega)$: the Fourier transform is the Laplace transform on the imaginary axis, which turns the heat equation into the Schrödinger equation ($t\mapsto it$).' Use $\omega$ and $t$ only.

#### `q-exp-entire` — proposition `prop:q-exp-entire` — T = 14/16 (warn)

- **Scores:** H1 2, H2 1, H3 1, H4 2, H5 2, H6 2, H7 2, H8 2
- **Evidence:** H3/H2: the proposition does not say why entireness matters (e.g. so that $\exp_q(-s\Delta)$ is defined for every $s$) and gives no small instance. H4 (minor): $\|x\|$ for the modulus of a complex number.
- **Suggested rewrite:** Open: 'We need $\exp_q$ to be defined on all of $\mathbb C$ for the Laplace transform below.' Use $|x|$.

#### `beta-eq-ln-q-dictionary` — proposition `prop:beta-eq-ln-q-dictionary` — T = 13/16 (warn)

- **Scores:** H1 1, H2 2, H3 2, H4 1, H5 2, H6 2, H7 2, H8 1
- **Evidence:** H8: L7-19 state as a proposition that $E=-\ln y/\ln q$ solves $e^{-\beta E}=y$, that it reverses order, and that $\sum d_\lambda e^{-\beta E_\lambda}=\sum d_\lambda y_\lambda$ — each true by definition. H4: $d_\lambda$ 'degeneracies' is new notation.
- **Suggested rewrite:** Make it a definition plus remark: 'Setting $\beta=\ln q$ and $E_\lambda=-\ln y_\lambda/\beta$ writes the Markov trace as a Boltzmann sum; the dominant block is the ground state.' Say $d_\lambda=\dim V_\lambda$ if that is meant.

#### `q-exponential-realisations` — remark `rem:q-exponential-realisations` — T = 8/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 0, H5 1, H6 2, H7 0, H8 1
- **Evidence:** H4/H7: 'the free grouplike on the primitive generator of the Reeb flow', 'the Habiro ring $\widehat{\mathbb Z[q]}[[x]]$', 'cyclotomic-projection' — heavy, undefined, unframed. H8: L1 places the Taylor coefficients $1/[n]_q!$ in the Habiro ring, which contains no inverses of $[n]_q$.
- **Suggested rewrite:** '$\exp_q$ is the function whose $q$-derivative is itself; its coefficients $1/[n]_q!$ are rational functions of $q$.' Remove the Habiro claim or state the integral variant meant.
- **Also:** needs_owner (content): 1/[n]_q! is not in the Habiro ring.

#### `q-exponential-unique` — proposition `prop:q-exponential-unique` — T = 9/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H1/H8: L8-15 discuss 'the accompanying proof' and which of its steps the hypotheses encode — commentary on a proof inside a proposition; once 'rigidity' is assumed the conclusion is a one-line difference argument, which the block then gives anyway. H4: $H$ (an abelian group) and $\mathcal H_q$ (the shuffle Hopf algebra) are both used, with the grouplikes said to be 'of $\mathcal H_q$' but the hypotheses placed on $H$. H3: no purpose.
- **Suggested rewrite:** State: 'If the only element with $D_qx=x$ and $\epsilon(x)=0$ is $0$, then a grouplike solution of $D_qe=e$, $\epsilon(e)=1$ is unique.' Put the one-line argument in the proof block; delete the commentary. Say why uniqueness of $\exp_q$ matters.

#### `q-exp-finite-field-obstruction` — remark `rem:q-exp-finite-field-obstruction` — T = 11/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 2, H6 2, H7 1, H8 1
- **Evidence:** H8: L1 '$\exp_q$ nonetheless exists as a symbol in the formal Hopf algebra $\mathcal H_q\otimes\mathbb F_p$' is not explained. H3/H2: why characteristic $p$ is considered is not said; the classical anchor ($e^x$ fails mod $p$ because $p!$ vanishes; the truncated exponential is the Artin–Hasse starting point) is missing.
- **Suggested rewrite:** 'Over $\mathbb F_p$ the series breaks at $n=p$, exactly as $e^x=\sum x^n/n!$ does. Truncating at $p-1$ gives a polynomial that is grouplike modulo $x^p$.' Drop or explain the 'symbol' sentence.

#### `q-exp-p-adic` — remark `rem:q-exp-p-adic` — T = 14/16 (warn)

- **Scores:** H1 2, H2 2, H3 1, H4 1, H5 2, H6 2, H7 2, H8 2
- **Evidence:** H3: no reason given for the $p$-adic case. H4 (minor): '$[n]_q!$' here is the Jackson factorial of the unbalanced $q$-integers, while prop:q-exp-entire uses balanced ones; the valuation statement is insensitive to this but the switch is silent.
- **Suggested rewrite:** Open with: 'For comparison with the classical $p$-adic exponential:' and say 'with either normalisation of $[n]_q$, since they differ by a unit'.

#### `q-logarithm-unique` — proposition `prop:q-logarithm-unique` — T = 9/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H1/H7: L7-16 are commentary on 'the accompanying proof' and on why rigidity 'is not available here', invoking Milnor–Moore unframed. H5: 'two $q$-logarithm primitives sharing $\Delta_q$ and $\epsilon$' — the structure maps belong to the ambient algebra, so 'sharing' them is vacuous.
- **Suggested rewrite:** 'If the only primitive element with zero counit is $0$, the $q$-logarithm is unique.' Keep L13-16's honest caveat as a single sentence: 'In general primitives form a Lie algebra and need not be unique; it is the grading of $\mathcal H_q$ that makes the hypothesis plausible.'

#### `q-dilogarithm` — definition `def:q-dilogarithm` — T = 10/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H5: the definition asserts 'the unique level-2 primitive ... normalised by the pentagon relation', while prop:q-dilogarithm-unique proves uniqueness only under a rigidity hypothesis and prop:q-dilogarithm-exists exhibits the zero solution. 'Level-$k$ primitive' (L1) names elements satisfying a non-primitive coproduct. H2: the classical case ($q\to1$: the Rogers dilogarithm satisfies this five-term relation) is not given.
- **Suggested rewrite:** 'A $q$-dilogarithm is a level-2 element $\mathrm{Li}^q_2$ satisfying the five-term relation ... At $q=1$ the Rogers dilogarithm $L(x)$ is the classical solution.' Drop 'unique' or cite the conditional result.

#### `q-dilogarithm-pentagon-associator` — remark `rem:q-dilogarithm-pentagon-associator` — T = 8/16 (fail)

- **Scores:** H1 0, H2 1, H3 2, H4 1, H5 1, H6 2, H7 0, H8 1
- **Evidence:** H1/H7: 478 words covering the pentagon, Faddeev–Kashaev, the modular double, the 'bar-even face that drives mass and binding', the 'bar-odd face carrying the decay observable', a Hopf–Drinfeld pairing and resurgence — far beyond what the block needs. H5: L7 'By def:q-dilogarithm there is exactly one level-2 primitive' relies on the definition's unproved uniqueness. L15 is a formalisation-status paragraph.
- **Suggested rewrite:** Keep paragraph 1 (the pentagon is why the dilogarithm appears) and one sentence of the Faddeev–Kashaev operator form with citation. Move 'two faces' and 'pairing, not a product' to the chapters on mass and decay. Replace L15 with one line: 'The step from the categorical pentagon to the scalar five-term relation is the Faddeev–Kashaev identification [cite]; we use it without proof.'

#### `q-dilogarithm-exists` — proposition `prop:q-dilogarithm-exists` — T = 9/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 1, H5 2, H6 2, H7 1, H8 0
- **Evidence:** H8: the proposition states that the structure 'is inhabited' and L6-9 concede the witness is the zero map, which 'satisfies the five-term relation without being the intended solution' — a vacuous existence statement presented as a result. H4: 'carrier', 'inhabited', 'pentagon data' are proof-assistant vocabulary.
- **Suggested rewrite:** Either delete, or replace with the existence statement that has content (construction of a non-zero solution) marked as open. Use mathematical vocabulary ('a set $H$ with ...').
- **Also:** proof-no-lean-mention-in-prose (vocabulary): 'carrier', 'inhabitation', 'witness' — Lean idiom in prose.

#### `q-dilogarithm-unique` — proposition `prop:q-dilogarithm-unique` — T = 10/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 1, H5 2, H6 2, H7 1, H8 1
- **Evidence:** H8: the hypothesis 'the only $f$ satisfying the relation is $f=0$' (L4-11) is the conclusion for differences, so the proposition is a restatement; L3 '(mul, compl, div)' and L13 '$\mathrm{Li}_2^q$-eval' are formal field names. H3: why uniqueness of the evaluation map matters is not said.
- **Suggested rewrite:** 'The five-term relation is linear in $f$, so two solutions differ by a solution of the homogeneous relation; if that relation has only the zero solution on $H$, the $q$-dilogarithm's values are unique.' Drop the field-name notation.

#### `dilog-pentagon-is-associator` — proposition `prop:dilog-pentagon-is-associator` — T = 5/16 (fail)

- **Scores:** H1 0, H2 1, H3 1, H4 1, H5 0, H6 2, H7 0, H8 0
- **Evidence:** H5/H8: the 'if and only if' (L1-7) holds because a '$q$-dilogarithm datum' is defined as something satisfying the five-term relation (L20 'the reverse reads the datum's five-term field') — a tautology presented as 'the precise sense in which the $q$-dilogarithm is forced by the rigid-monoidal axioms' (L9), which L24 then says is not proved. The five-term functional equation is called 'the Mac Lane pentagon' (L1). L9 cites prop:q-dilogarithm-exists for uniqueness. L18-20 is a Lean section in prose.
- **Suggested rewrite:** Restate as what it is: 'By definition, a $q$-dilogarithm is a solution of the five-term relation. That this relation is the image of the Mac Lane pentagon is the Faddeev–Kashaev identification [cite], not proved here.' Remove the Lean section; fix the uniqueness citation.
- **Also:** proof-no-lean-mention-in-prose: L15, L18-20 name `QOU.BringsSurface.PentagonTwist.assoc_pentagon`, `pentagon_iff_isDilog`, `#print axioms`, Mathlib, `QRogersAnalyticContinuation`.

#### `generating-functions-solve-reeb-flow` — remark `rem:generating-functions-solve-reeb-flow` — T = 9/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 0
- **Evidence:** H8: L7 'These three functions are the unique algebraic objects in the Habiro completion satisfying the categorical evolution equations' — no uniqueness result is cited, and prop:q-dilogarithm-unique is conditional. H4: $\tau_\infty$ reuses $\tau$; 'volumetric expansion of the Reeb-heat flow' is undefined.
- **Suggested rewrite:** '$\exp_q$ solves the Reeb-flow equation, the Fourier transform diagonalises the $q$-heat equation, and $\mathrm{Li}^q_2$ appears in the volume (§...). At $q\to1$ the last becomes the Bloch–Wigner function.' Drop 'unique' unless cited.

#### `archimedean-realisation-volume-compatibility` — conjecture `conj:archimedean-realisation-volume-compatibility` — T = 7/16 (fail)

- **Scores:** H1 2, H2 0, H3 1, H4 0, H5 1, H6 2, H7 0, H8 1
- **Evidence:** H4/H7: the conjecture uses the Habiro ring, a 'motivic volume class' $\mu(\beta)$ in an undefined $\widehat{\mathcal M}$, a realisation $\mathcal R_{\mathrm{top}}$, $V_0(\beta)$ and $\tau_\infty$ (reusing $\tau$), none defined. H2/H3: no classical anchor — the statement is a version of the volume conjecture, which is not named.
- **Suggested rewrite:** 'The volume conjecture [Kashaev; Murakami–Murakami] says the hyperbolic volume of a knot is the growth rate of its coloured Jones polynomials. We conjecture the following version for QOU braids: ...' Define $V_0(\beta)$ and $\mu(\beta)$ or point to their definitions.

#### `braiding-unit-circle-convention` — remark `rem:braiding-unit-circle-convention` — T = 10/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H5: L1 calls it 'the inside-unit-circle convention' while assigning $q:=\lambda_+$, which L1 then says 'lies outside the unit circle'. H8: 'aligns with the standard orientation of the Kauffman bracket' is unexplained (and the paper does not use the bracket variable).
- **Suggested rewrite:** 'We take $q$ to be the eigenvalue on $S^2V$; for $q>1$ it lies outside the unit circle and $-q^{-1}$ inside. This makes $q$ positive (prop:substrate-parameter-unique).' Drop the Kauffman sentence or say what it means.

#### `i-as-braiding-orientation` — remark `rem:i-as-braiding-orientation` — T = 9/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 0
- **Evidence:** H8: L1 'The imaginary unit $i$ serves as the orientation of the braiding' and L5 'Negating $i$ equates to flipping the crossing orientation' are identifications with no construction; the three items list places where a sign choice occurs, which does not show they are one choice.
- **Suggested rewrite:** 'Three sign conventions in this chapter are tied together: the direction of Wick rotation, the complex structure $J$ on $H$, and the choice of $c_{V,V}$ over $c_{V,V}^{-1}$. Changing $i\mapsto -i$ reverses all three (prop:...).' — or mark the remark as heuristic.

#### `affine-chart-origin-of-i-and-q` — remark `rem:affine-chart-origin-of-i-and-q` — T = 8/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 0, H6 2, H7 1, H8 0
- **Evidence:** H5: L5 '$\rho_{\pi/2}=i\,\mathrm{id}_V$ operates as the square root of $\iota$' — $i\,\mathrm{id}_V$ acts on $V$ while $\iota(z)=z^{-1}$ acts on a chart of $\mathbb P(V)$, and on $\mathbb P(V)$ a scalar acts trivially. L1 calls $i$ and $q$ 'categorical coordinates' of $\mathbb P(V)$. H8: 'The Galois action exchanging $\pm i$ encapsulates the braiding orientation choice' is unsupported.
- **Suggested rewrite:** Use a map that does square to the chart swap (e.g. $z\mapsto iz$ squares to $z\mapsto -z$, which is the antipodal map in the chart; $z\mapsto 1/z$ is the swap). State precisely which relation is meant before the interpretation.

#### `reeb-u1-chart-swap` — proposition `prop:reeb-u1-chart-swap` — T = 10/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H5: L7 'The chart-swap one-parameter subgroup' — the chart swap $z\mapsto z^{-1}$ is an involution, not a one-parameter subgroup; $\rho_{\theta_q}$ and $\phi_t$ are not defined in this block, and $\theta_q\in U(1)$ mixes an angle with a group element. H2: no $\mathrm{SU}(2)$ instance (rotations of $\mathbb{CP}^1$ about the axis through $0$ and $\infty$).
- **Suggested rewrite:** 'On $\mathbb{CP}^1$, the rotations $z\mapsto e^{i\theta}z$ (fixing $0$ and $\infty$) form the image of the maximal torus; we show the Reeb flow generates the same subgroup.' Define $\rho_\theta$, $\phi_t$.

#### `reeb-u1-five-roles` — remark `rem:reeb-u1-five-roles` — T = 7/16 (fail)

- **Scores:** H1 1, H2 1, H3 1, H4 1, H5 1, H6 2, H7 0, H8 0
- **Evidence:** H5: item 4 gives the Reeb flow as $Z\mapsto e^{-t}Z$, a real scaling, while prop:substrate-radial-coordinate gives $\mathcal L_\xi Z=J\hbar_qZ$, a rotation. H7/H8: L8 'Knot operators function as Reeb-$U(1)$ Wilson loops' and 'The Osterwalder–Schrader reflection embodies the antipodal $\mathbb Z_2$' import physics machinery as identifications.
- **Suggested rewrite:** Reconcile item 4 with the rotation formula. Reduce L8 to what is shown, or mark it as interpretation with references.

#### `categorical-coordinate-ring` — proposition `prop:categorical-coordinate-ring` — T = 10/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 1, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H5: L1 takes $q\in R^\times$ (the family is indexed by $q\in R^\times$) and then forms $R[q,q^{-1}]$, which equals $R$ if $q\in R$; whether $q$ is a variable or a scalar is unclear. H4: 'the tangent representation $\rho_p(\iota)=-1$' is undefined. H3: why one wants this ring is not said.
- **Suggested rewrite:** 'Treat $q$ as a variable. The smallest ring over which the charts glue ($zw=q^{-1}$ with $q$ invertible) and the chart swap has a square root is $R[q^{\pm1},i]=R[q^{\pm1}][i]/(i^2+1)$.'

#### `tqft-context` — remark `rem:tqft-context` — T = 12/16 (warn)

- **Scores:** H1 1, H2 1, H3 2, H4 1, H5 2, H6 2, H7 2, H8 1
- **Evidence:** H8: L3 'The condition $\mathrm{Hom}(\mathbf1,\mathrm{Ad}(A))=0$ acts as the categorical contact condition. It ensures irreducibility of the associated 3d TQFT, non-degeneracy ..., and full dualisability' — no 3d TQFT has been associated to a QOU, and the claims are unsupported. H1: L1 is a 170-word paragraph. (Credit: L1's scoping of the Li theorem — what it gives and what it does not — is exemplary H7.)
- **Suggested rewrite:** Split L1 into: the 2d cobordism statement; the scope caveat. Replace L3 with what is actually used, or mark it as heuristic: 'We expect observability to play the role of irreducibility for an associated 3d TQFT; this is not proved here.'

#### `levi-generalisation` — remark `rem:levi-generalisation` — T = 7/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 0, H5 1, H6 2, H7 0, H8 0
- **Evidence:** H8/H4: L3 '$q(p)=1+|\langle L_\varTheta,F_A^+\rangle|\ge1$' defines the substrate parameter by a curvature pairing — a fourth definition of $q$, unexplained, with $F_A^+$ undefined; L1 'relies on Levi non-degeneracy over strict pseudoconvexity' is unclear. H7: Kohn–Rossi cohomology invoked unframed; $\Gamma_c(M,\mathcal S)=0$ inherits the issue noted at ex:c-quantum-observable-universe.
- **Suggested rewrite:** Delete the formula for $q(p)$ or derive it. 'We need only that the Levi form is non-degenerate (not that it is definite). Under that hypothesis Kohn–Rossi cohomology is finite-dimensional [Folland–Kohn], which is what controls $q$-harmonic forms.'
- **Also:** needs_owner (content): a fourth, curvature-based formula for q(p) with no derivation.

#### `schrodinger-jet-coaction` — remark `rem:schrodinger-jet-coaction` — T = 9/16 (fail)

- **Scores:** H1 2, H2 1, H3 1, H4 0, H5 1, H6 2, H7 1, H8 1
- **Evidence:** H4: $\mathcal S_{\mathrm{lin}}$, $D_A$, $V_q$ (also the letter of the fundamental object) and $\hat H_q$ are undefined; the title promises a 'jet coaction' that the text never mentions. H8: L7 'uncertainty vanishes and the wave trajectory freezes classically' is a physical gloss on $\hbar_q\to0$.
- **Suggested rewrite:** Define $\mathcal S_{\mathrm{lin}}$ (the associated vector bundle) and $D_A$; call the potential $U_q$. Either connect to the jet coaction or retitle.

## 8. Blocks recorded `n/a`

**Ch 1 — Quantum Universes.** Kind outside `applies_to` (10): `quantum-universe-exists-proof`, `frobenius-pairing-exists-proof`, `frobenius-pairing-unique-proof`, `quantum-universe-su2-table1-data`, `frobenius-relation-proof`, `positive-definite-dagger-proof`, `categorical-connection-exists-proof`, `categorical-connection-unique-proof`, `categorical-hodge-star-exists-proof`, `categorical-hodge-star-unique-proof`.

Under ~50 words (5): `quantum-universe-exists` (17), `fundamental-object-explication` (41), `categorical-connection-unique` (48), `categorical-hodge-star-exists` (46), `categorical-hodge-star-unique` (42).

**Ch 2 — Quantum Observable Universes.** Kind outside `applies_to` (62): `qou-exists-axiom-1-proof`, `qou-exists-axiom-2-proof`, `qou-exists-axiom-3-proof`, `qou-exists-axiom-4-proof`, `quantum-observable-universe-exists-proof`, `braiding-induced-ordering-proof`, `volume-from-rigidity-proof`, `su2-emergence-volume-determinant-proof`, `su2-emergence-dagger-unitarity-proof`, `su2-emergence-proof`, `spin-labels-proof`, `g-action-on-substrate-table1-data`, `g-action-on-substrate-table2-data`, `g-action-on-substrate-table3-data`, `weight-decomposition-exists-proof`, `categorical-reeb-exists-proof`, `categorical-reeb-unique-proof`, `fibre-functor-atlas-proof`, `substrate-radial-coordinate-proof`, `fai-projector-coadjoint-orbit-proof`, `fiber-adjoint-involution-proof`, `substrate-parameter-exists-proof`, `substrate-parameter-unique-proof`, `u1-equivariant-reduction-proof`, `categorical-dirac-operator-exists-proof`, `categorical-dirac-operator-unique-proof`, `categorical-lagrangian-exists-proof`, `categorical-lagrangian-unique-proof`, `categorical-action-exists-proof`, `categorical-action-unique-proof`, `variational-equations-proof`, `categorical-q-ext-deriv-exists-proof`, `categorical-q-ext-deriv-unique-proof`, `observation-energy-proof`, `categorical-lichnerowicz-proof`, `categorical-instanton-exists-proof`, `categorical-instanton-unique-proof`, `categorical-irreducible-proof`, `categorical-self-duality-proof`, `categorical-dq-squared-proof`, `categorical-q-connection-exists-proof`, `categorical-q-connection-unique-proof`, `q-heat-equation-exists-proof`, `q-heat-equation-unique-proof`, `categorical-laplace-transform-exists-proof`, `categorical-laplace-transform-unique-proof`, `categorical-fourier-transform-exists-proof`, `categorical-fourier-transform-unique-proof`, `q-resolvent-exists-proof`, `q-resolvent-unique-proof`, `q-exponential-exists-proof`, `q-exponential-unique-proof`, `q-exp-p-adic-table-data`, `q-logarithm-exists-proof`, `q-logarithm-unique-proof`, `q-dilogarithm-exists-proof`, `q-dilogarithm-unique-proof`, `reeb-u1-chart-swap-proof`, `categorical-coordinate-ring-proof`, `emergence-to-quantum-flat-proof`, `dq-squared-proof`, `q-jacobiator-proof`.

Under ~50 words (107): `quantum-observable-universe-exists` (41), `qou-exists-axiom-1` (9), `qou-exists-axiom-2` (13), `qou-exists-axiom-4` (11), `frobenius-integration` (17), `yekutieli-stokes-remark` (23), `qou-su2` (8), `base-field-independence` (22), `su2-emergence-volume-determinant` (23), `su2-emergence-dagger-unitarity` (17), `weight-decomposition-exists` (32), `reeb-physical` (37), `pawlowski-leitner-basis-construction` (41), `categorical-reeb-unique` (42), `projective-line-object` (48), `projective-line-su2` (41), `fai-projector-coadjoint-orbit` (49), `tannaka-krein-reconstruction` (49), `substrate-parameter-exists` (34), `quantum-gauge-group` (37), `quantum-planck-constant` (12), `planck-limits` (18), `exceptional-divisor` (42), `commutative-qou` (49), `u1-equivariant-reduction` (42), `intro-heisenberg-commutator` (43), `notation-special-cases` (46), `categorical-dirac-operator-exists` (43), `categorical-lagrangian-exists` (41), `categorical-lagrangian-unique` (31), `categorical-action-exists` (40), `categorical-action-unique` (33), `particles-intro` (46), `q-harmonic-form` (39), `lichnerowicz-wkb-corollary` (44), `lichnerowicz-q-correction` (45), `instanton-intro` (31), `categorical-instanton` (42), `categorical-instanton-exists` (24), `categorical-instanton-unique` (47), `categorical-irreducible` (18), `dq-squared-intro` (37), `categorical-q-lie-bracket` (45), `categorical-q-connection` (34), `categorical-q-connection-exists` (24), `categorical-q-connection-unique` (27), `q-deformed-operators-intro` (32), `q-ext-deriv` (41), `q-lie-bracket` (35), `q-connection` (40), `q-reeb-vector-field` (40), `q-reeb-flow` (32), `q-torsion-leaf` (44), `q-harmonic-analysis-intro` (29), `q-heat-equation-exists` (37), `q-heat-equation-unique` (21), `categorical-laplace-transform-properties` (28), `categorical-laplace-three-contexts` (33), `categorical-laplace-q-heat-resolvent` (31), `categorical-laplace-transform-exists` (14), `categorical-laplace-transform-unique` (20), `categorical-fourier-transform` (33), `categorical-fourier-transform-properties` (46), `categorical-fourier-brings-dft` (38), `categorical-fourier-transform-exists` (44), `categorical-fourier-transform-exists-harmonic` (41), `categorical-fourier-transform-unique` (46), `categorical-fourier-transform-unique-invariance` (38), `intro-q-resolvent-wick` (42), `q-resolvent` (45), `q-resolvent-exists` (24), `q-resolvent-unique` (15), `intro-q-special-functions` (34), `q-exponential` (48), `q-exponential-exists` (37), `q-logarithm` (49), `q-logarithm-properties` (36), `q-logarithm-exists` (19), `q-special-functions-dilog-intro` (19), `q-dilogarithm-properties` (25), `q-dilog-habiro-ring` (32), `q-dilog-three-contexts` (31), `q-dilog-archimedean` (20), `q-dilog-heat-partition` (29), `q-dilog-physical-meaning` (13), `braiding-conventions-intro` (23), `sqrt-q-ribbon-structure` (48), `sign-as-spin-structure` (24), `quantum-observable-universes-intro` (40), `vanishing-explication` (27), `quantum-gauge-group-category` (32), `hopf-structure-diagrams` (18), `quantum-flatness` (31), `self-dual-2group` (43), `emergence-to-quantum-flat` (43), `simplicity-from-category` (40), `frobenius-simplification` (39), `j1e-local-states` (29), `dq-squared-elaboration-intro` (26), `dq-squared` (34), `q-jacobiator` (40), `classical-recovery` (24), `physical-elaborations-intro` (28), `q-torsion-leaf-minimum` (32), `q-harmonic-physical` (23), `linearisation-convention` (40), `outro-quantum-observable-universes` (44).

The ~50-word cut is the spec's, applied mechanically by whitespace word count; it counts math tokens as words, so a few of these are real definitions with short prose. If the owner wants those scored too, they are the obvious next pass.

## 9. Reproduce

- Reader check: `readWitnessDoc("block", <block>.md, <repo>)` from `cat-harness/content/pipeline/qa-witness.ts`, after `configureLeanPackages(LEAN_PACKAGES)`; the `expo-milnor-clarity` view's first witness is `local/expo-milnor-rater` with `freshness: fresh`.
- Guards: `bun run folio/pipeline/qa-flag-preservation-audit.ts <chapter-dir> --check`; `python3 scripts/qa-duplicate-verdict-check.py`.
