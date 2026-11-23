# Round-trip blind audit, pass 3 (2026-11-22)

Bean epic `qou-ncxf` (children `qou-zqno` RT-1, `qou-wnm3` RT-2, `qou-da6d` RT-3).
Bean-drain wave 2, sibling "honesty-roundtrip". Pass 1:
[`2026-11-20-roundtrip-blind-audit-pass1.md`](2026-11-20-roundtrip-blind-audit-pass1.md);
pass 2: [`2026-11-21-roundtrip-blind-audit-pass2.md`](2026-11-21-roundtrip-blind-audit-pass2.md).

This pass **records findings and fixes no block.** Every restatement, honest
`sorry`, kind change or disclosure below is an owner decision (AGENTS.md "ask the
owner before changing things", 2026-09-07); the decisions are put to the owner
separately.

## 1. Method

Sampler: `scripts/roundtrip-blind-sample.py 20 --offset 40` (next cursor after
pass 2), with the two sampler fixes of §4 applied. Population **408** eligible
provable blocks on `main` `3c4c98fcc` (pass 2 counted 419 with the old pairing
rule; §4 explains the drop). Order: sha256(label). Five labels in the window
were skipped as `decl-not-found`:

- `prop:local-substrate-q`
- `prop:vertex-is-exceptional-divisor`
- `prop:plancherel-term-7-formulation`
- `prop:level-sufficiency`
- `prop:yekutieli-lifting`

These are `lean.ref` defects of the `qou-5d0x` class and are listed there, not
re-litigated here.

Four blind legs, each a separate agent that saw only its own packet file and
was told not to open anything else:

| leg | input | output |
|---|---|---|
| RT-1 A | Lean statement + in-scope defs, comments stripped, decl renamed `thm` | English statement + shape flags |
| RT-2 B | the same, plus the Lean proof | proof narrative + where the content lives |
| RT-3 A | `.md` proof only | inferred statement + gaps |
| RT-3 B | `.md` statement only | proof obligations + flags |

Adjudication against the real files is mine and is **not** blind. A finding
marked **verified** was checked by me against the file; the rest are agent
findings, recorded as such.

### Packet limitations

- **Empty context.** Where a decl's helpers live in another module (P01, P16,
  the `prop:skein-generation` helper `mem_adjoin_of_complexity_eq`), RT-1 A and
  RT-2 B saw no definitions and said so.
- **Three packets re-run.** The first sampler run paired three blocks with the
  wrong proof (§4). `lem:brings-riemann-hurwitz` and
  `lem:descent-cocycle-deviation` had RT-3 A re-run on their own proofs; the
  first-run RT-3 A outputs for them are discarded. `prop:self-dual-higgs-real-volume`
  has no proof block and left the population; `prop:skein-generation` entered
  the window and got all four legs.
- **P19 Lean legs not blind.** `prop:categorical-q-connection-exists` first
  resolved to a docstring (§4); its corrected Lean was read by me, not by a
  blind agent. The finding (Class T) is immediate from the proof term.

## 2. Results

Classes as in pass 2: **A** the Lean conclusion is assumed (a hypothesis or class
field is returned); **T** tautology / `rfl` / trivially inhabited; **B** the Lean
is weaker than the `.md` claim; **C** the narrative proof does not prove the
statement; **E** an empirical value inside a formal result; **I** the statement
is ill-posed as written.

| # | label | kind | Lean | statement / narrative |
|---|---|---|---|---|
| P01 | `lem:piece-a-corner-removal-obligation` | lemma | genuine (hook-sum identity, `linear_combination`) | genuine; all three text legs agree, RT-3 B checked small shapes |
| P02 | `prop:braiding-induced-ordering` | prop | genuine (deglex well-founded + admissible) | genuine; "braiding" is a name only, nothing braided is used |
| P03 | `prop:universal-braid-branching` | prop | **B, verified**: `χ` is an arbitrary function assumed to satisfy the branching recursion (`h_rec`); no Hecke character appears | **C/E (agent)**: the closure of the word used for 4₁ and the 4₁ table entry are disputed by two legs; the convergence bound uses CODATA δq and is heuristic |
| P04 | `prop:q-logarithm-unique` | prop | **A (hypothesis), verified**: uniqueness is the hypothesis `prim_rigid`; the `.md` says rigidity is not available | C (agent): with rigidity, any two primitives with ε = 0 are both 0, so the claim is vacuous as stated |
| P05 | `lem:genus-from-hecke-completeness` | lemma | arithmetic (`decide`), genuine | minor: the target "5 irreducibles" counts 3 for H₃, but the SU_q(2) image has 2; a modelling choice the narrative does not flag |
| P06 | `prop:torus-embeddable-complete` | prop | **B, verified**: the genus bound is a hypothesis `(m−1)(n−1) ≤ 8`; `torusKnotEmbeddable` is unused | **I/C (agent, both text legs)**: "T_{m,n} embeds in Σ₄ iff …" fails under the natural reading (every torus knot lies on a torus inside a genus-4 surface in S³); the list is exactly Seifert genus ≤ 4, a different notion |
| P07 | `thm:qou-obstruction-reduction` | **theorem** | **A, verified**: conjuncts come from class fields `vdb_duality`, `drinfeld_rigidity`, `kappa_vanishes_def`, `hattori_stallings` | **C (agent)**: step 1 "Ad^G = 0" is false for the adjoint action on a Hopf algebra (it fixes 1); the proof admits the Wigner axiom carries part (a) |
| P08 | `prop:parallel-fibre-noninteraction` | prop | **T, verified**: `rfl` on the definition of `parallel` | C (agent): the narrative calls the factorisation both derived and definitional; Jones/HOMFLY split-union normalisation ignored |
| P09 | `prop:hadron-exists` | prop | **T, verified**: `Nonempty Hadron` by two unknots at θ = φ = 0 | already disclosed (caveat 2026-08-08). C/E (agent): "crossing energy negative at q₀" asserted, LP-stability cited, no computation |
| P10 | `prop:descartes-elliptic-curve` | prop | genuine (two algebraic identities, `field_simp`/`ring`) | genuine algebra, both text legs re-checked it; minor: the discriminant (needed for "elliptic") is not checked |
| P11 | `lem:brings-riemann-hurwitz` | lemma | **A, verified**: `deg_is_four`, `branch_is_six` returned from class fields; R_tot = 14 by `norm_num` on field values | **C/I (agent, both text legs)**: the "canonical covering" of a genus-4 curve maps to ℙ³ with degree 6, not to ℙ¹ with degree 4; "distributed by S₅-symmetry over exactly 6 branch points" has no argument, and S₅ is not a finite subgroup of PGL₂(ℂ), so it cannot act compatibly on the target ℙ¹ |
| P12 | `cor:knot-factor-borromean-composite` | corollary | **A (hypothesis), verified**: the decoupling `composite = ∏ components` is a hypothesis | C (agent): "Brunnian-ness decouples" is unjustified (Brunnian links are not split); the Borromean components are unknots, not 4₁; the `.md` admits a conflict with another block |
| P13 | `lem:genus-ideal-characterisation` | lemma | **T, verified**: `Ideal.mk_ker` (ker(R → R/I) = I) | **C (agent)**: "rank H₁(F_p) = (p−1)/2" is wrong (it is p − 1) and rank H₁(Σ₄) = 8, not 4; the bound p ≤ 9 survives only because the two errors cancel |
| P14 | `lem:fai-projector-coadjoint-orbit` | lemma | **B, verified**: proves only (2ρ − 1)² = 1 for an idempotent ρ | **C (agent, both text legs)**: V simple ⇒ End(V) is scalars by Schur, so no rank-1 idempotent morphism exists in the category; and rank-1 idempotents on ℂ² form a 2-dimensional complex family, not ℙ(V), unless they are orthogonal |
| P15 | `lem:descent-cocycle-deviation` | lemma | **A, verified**: the body is `ctx.claim_cocycle_deviation n i j k`, the class field verbatim (`descent_cocycle_deviation.lean:42, 63`) | **I/C (agent, both text legs)**: "d(g_{ijk}) = a_{ij} g_{ijk} a_{jk}⁻¹" mixes degrees (d of a 2-cochain has four indices) and twisting is trivial in the abelian band 𝒪^× |
| P16 | `prop:confinement-topological` | prop | **B, verified**: proves only `lPlus² + lMinus² ≠ 2·lPlus·lMinus` (a Gram-indefiniteness witness) | **E/C (agent)**: items 1–3 (LP value 0, |x*| ≫ 1, uniqueness of (σ₀σ₁⁻¹)³ among words of length ≤ 6) are numerical reports at q₀; uniqueness is doubtful since cyclic rotations such as (σ₁⁻¹σ₀)³ have the same crossing counts |
| P17 | `prop:y-lambda-cyclotomic-factorization` | prop | **T, verified**: the two existentials take y = numerator / denominator over ℝ and say nothing about divisibility | **C (agent)**: X(q̌) carries the non-cyclotomic denominator 1 + q̌² + q̌³ − q̌⁴ − q̌⁶, and "closure under division" fails; possibly false as stated |
| P18 | `prop:isotope-knot-equivalence` | prop | **A, verified**: `⟨claim_reflexivity, claim_symmetry, claim_transitivity⟩` | the relation is the pullback of equality, so the claim is true but the Lean does not show it |
| P19 | `prop:categorical-q-connection-exists` | prop | **T, verified**: the structure is built from its own inputs and `nabla_q_formula := rfl` | **I (agent)**: existence with no defining axioms is vacuous (the zero morphism would do) |
| P20 | `prop:skein-generation` | prop | **A (inductive form), verified**: class fields `base` + `resolve` are the step-by-step form of the conclusion; `trivialSkeinGenerationContext` inhabits the class for every algebra | narrative genuine (HOMFLYPT skein of S³ free of rank 1 on [U], citing Lickorish); gap: q − q⁻¹ must be a unit; the empty link must be excluded or the rank is 2 |

### Counts

- Lean: genuine 4 (P01, P02, P05, P10), **A 7** (P04, P07, P11, P12, P15,
  P18, P20), **T 5** (P08, P09, P13, P17, P19), **B 4** (P03, P06, P14, P16).
- Text: narrative or statement defects reported by at least one blind leg in
  13 of 20; by both text legs independently in 5 (P06, P11, P14, P15, P13 in
  substance).
- Empirical register flagged: P03 (CODATA δq in the convergence bound), P09,
  P16. All three are inside narrative proofs, not inside Lean.
- `sorry`, `axiom`, `native_decide`: none in the 20 Lean proofs.

One block is a **theorem** with a Class-A Lean: `thm:qou-obstruction-reduction`
(P07). That is the kind-change question this pass raises.

## 3. Not yet disclosed

The `.ts` of these Class-A/T/B blocks carries no caveat naming the defect
(searched for `caveat`, `authorNote`, "Assumed, not derived", "self-assuming",
"restated"): P08, P11, P13, P15, P16, P18, P19. P09 is already disclosed. The
others carry only the generic §7c archimedean note. Which of the three remedies
pass 1–2 used (caveat, restate to the Lean, honest `sorry`) applies to each is
the owner's decision.

## 4. Sampler fixes (this PR)

Both change which blocks are audited, so they also bear on passes 1–2.

1. **A docstring was taken for a declaration.** `locate` searched raw text, so
   the docstring line "theorem exists in this file …" in
   `lean/QOU/HeckeAlgebra/Wedderburn.lean` matched the ref
   `QOU.CategoricalQConnection.exists` (dotted-suffix `exists`). Fixed: the
   search runs on comment-blanked text (`blank_lean_comments`, offsets kept).
2. **A proof was paired with every block it cites.** A proof block was mapped
   to every label in its `uses`, first come first served. Measured on this
   window: `prop:self-dual-higgs-real-volume` (no proof block) got
   `prf:ew-triplet-charge-spin-from-involution`; `lem:brings-riemann-hurwitz`
   got `prf:brings-is-qou`; `lem:descent-cocycle-deviation` got
   `prf:descent-condition`. Fixed: a proof `prf:X` is paired only with the
   `uses` entry whose suffix is `X` (hyphens ignored). 6 of 415 proof blocks
   have no such entry and are now unpaired rather than guessed; one of them,
   `prf:topological-mass`, lists `prop:topological-mass-upper-bound` first
   while proving the conjecture.

   **Effect on passes 1–2.** Re-pairing the 30 labels of those passes, one
   changes: pass-1 B07 `prop:sl2-prolongation-recurrence` was paired with
   `prf:sl2-period-conserved-quantity`; its own proof is
   `prf:sl2-prolongation-recurrence`. B07's finding is a Lean-vs-statement one
   (Lean proves only the Cayley–Hamilton implication; bean `qou-vkm6`) and does
   not depend on the proof leg, but its RT-3 A column was read from the wrong
   proof.

## 5. Next

Next cursor: `--offset 60` (population 408). 348 blocks remain after this pass.
