# Pilot review: braids-and-knots (2026-11-15, main `b2b349f36`)

Scope: 19 Lean-backed statement blocks and 16 `prf:` blocks in
`folio/quantum-observable-universe/braids-and-knots/`. For each one I read the
statement `.md`, the proof `.md` and the referenced Lean declaration side by side.
Algebra was re-checked by hand, and with sympy where noted. **No verdict has been
written to a sidecar yet.** The verdicts below are proposed; they go in only with
the owner's go.

Columns:
- **S↔L** = `proof-narrative-lean-equiv` (statement vs the Lean the `.ts` refers to).
- **S↔P** = whether the narrative proof proves the statement (stand-in: `da-non-sequitur` on the `prf:` block).

## Verdict table

| block | S↔L | S↔P | one-line reason |
|---|---|---|---|
| prop:chi-sym-alt-closed-form | warn | n/a (no prf; argued inline) | Lean closed form matches; the χ values are a hard-coded table, not derived from Hecke characters; the atomic-word specialisation (n_ud = 2A, one pn letter) is only existential in Lean |
| prop:figure-eight-reeb-rotation | **fail** | **fail** | Lean ref is a generic lemma (any root of λ²−tλ+1 with t²<4 has |λ|=1) that never mentions M₄₁; statement claims unit modulus with no q-range, but the proof (correctly) shows it only for φ⁻¹<q<φ, and for q>φ the eigenvalues are real and not unit |
| prop:hoefsmit-binding-amplitude | **fail** | **fail** | Lean *defines* b by b²=[3]/[2]² and proves [3]/[2]² = 1−1/[2]² (circular w.r.t. the claim); statement also asserts a pion-decay energy release E = m_π/[2]² that no proof addresses. The b² algebra itself checks (sympy) |
| prop:alpha-em-habiro-bar-involution | pass (warn) | missing proof | items 1–2 encoded exactly; tail claims (H(ζ₄)=0 "dual of the Q_β pole", α/(4π) leading term) unencoded and unproved |
| thm:jones-markov-trace | **fail** | missing proof (cited) | Lean `z` field docstring still says convention C `1/(q^½+q^−½)` while the statement fixes D; `z` is unconstrained; existence is an axiom; uniqueness, the ℓ(λ)≥3 vanishing, the TL quotient and Catalan count are not encoded; `nondeg` is index-independent (vacuous) and its docstring says "nonzero on every S_λ", contradicting the D vanishing claim |
| prop:r-matrix-braiding-structure | **fail** | missing proof (cited) | Lean ref is a `def … : Prop` stated "not asserted"; the statement asserts YBE |
| prop:three-strand-color-winding-rigidity | pass | warn | Lean faithful (generic CommRing, constrained a, β). Statement says "1−q² invertible"; the proof's a₊₂ needs q⁴≠1 |
| prop:braid-action-tensor | **fail** | pass | statement: Bₙ action for every n≥2; Lean: only a B₃ representation. (Statement also reads "there is a group ρₙ", missing "homomorphism") |
| prop:q-casimir-exists | **fail (critical)** | pass | `QCasimir.exists_axiom : ∀ qs, Nonempty (QCasimirData qs)` is unconditional, while the statement needs q−q⁻¹ invertible. `QuantumSu2` carries no U_q relations at all. **Suspected inconsistent:** take `Algebra := ℤ`; any ring hom R_q→ℤ sends q to ±1, so ι(q−q⁻¹)=0 and `invQm_left` reads 0=1. Not yet run in Lean. Centrality and the eigenvalue are not encoded |
| prop:q-casimir-unique | **fail (critical)** | warn | `unique_up_to_scalar_axiom` says *every* central C equals C_q + ι(r), with no eigenvalue or form hypothesis. False even in true U_q(sl₂) (C_q² is central). **Suspected inconsistent independently:** Algebra = ℚ[X], q↦2, E=F=0, K=1, C=X. Proof text says centre = R[C_q], which contradicts "unique up to scalar" without the degree-1 restriction the Lean drops |
| prop:meson-qcg-fusion-identity | pass | warn | identity exact in Lean and proof; statement adds a physics reading (m_K²/m_π²) the proof does not touch |
| prop:lagrange-resolvent-transform | **fail** | missing proof | sibling `.lean` genuinely proves n=5 (w₀=0, diagonal action), but the `.ts` ref points at the library version for general n, which is `ax.claim_equivariance` (self-assuming class). The quadric/cubic constraints are unencoded (I checked them by hand: correct) |
| prop:hoefsmit-toroidal-ladder-locus | pass | pass | Lean over `IsDomain`, conclusion 2α=−1, 2β∈{1,−3}: equivalent in char 0. "q-layer verified by direct computation" is an unformalised side claim |
| thm:pontryagin-dual-coxeter-character | warn | pass | Lean class encodes two auxiliary facts (characters of ℤ/2 fixed by value at 1; sign(swap 0 1) = −1), not the abelianisation isomorphism or ℂ^× characters |
| prop:frobenius-lepton-meson-bridge | **fail** | **fail** | Lean is `branchingH3H2 1 0 = 1 ∧ … := by rfl` on a lookup table; statement carries physical claims (mass ratios "measure" transitions; C vs bar alignment) that the proof (branching rule only) does not address |
| prop:meson-em-sinh-closed-form | pass | **fail** | the identity is exact in Lean and proof; but the statement block also carries the m_K²/m_π² formula, ppb comparisons with data, and says the stopping order "was chosen against the data" and the pair (3,4) "was found by scanning". Empirical and fitted content inside a proposition |
| prop:knot-eigenbasis-complete | **fail** | **fail** | Lean: `KnotEigenbasisData` carries `complete` and `summands_detected` as fields; the theorem projects them (self-assuming). Narrative: "H_n = End_{B_n}(V^⊗n)" is not right (Hₙ maps onto the TL quotient; End_{B_n} is the commutant of the braid action); "inclusions induced by the unit η: 1→V" is zero for the fundamental of SU_q(2) (Hom(1,V)=0) |
| prop:q-casimir-classical-limit | pass | missing proof | Lean genuine (Tendsto). Lean takes j : ℤ, so half-integer spins are not covered |
| prop:pion-half-figure-eight | **fail** | warn | Lean takes the trace and det as hypotheses and proves a tautology. Narrative traces are right (sympy: both −(q⁴−q²+1)/q²); proof says "complex conjugates on the unit circle" unconditionally, true only for h²<1 (q<φ). The statement (equal phases) still holds |

### Proof blocks whose statement is not in the 19

| prf block | S↔P | reason |
|---|---|---|
| prf:trm-hopf-sigma1-sq-closed-form | pass (warn) | closed form verified by hand; the statement's Q_β coefficient comparison is not covered by the proof |
| prf:hecke-satisfies-blitvic-hypothesis | **fail (critical)** | **The statement is false.** It claims odd joint moments of centred generators vanish. Counterexample: k=3, word σ̃₁σ̃₁σ̃₁ in H₂ under convention D. tr(σ̃³) = (h²+1)z + h − 3hz² − 3z + 2z³ = −3/4 at q=1 and −1.428 at q=2 (exact rationals). The proof's "unmatched factor → Markov kills it" step only holds for the top generator. The Lean (Observations) is honest: it derives odd vanishing from an assumed `HeckeBlitvicWickRecursion` class, which the real moments do not satisfy. Feeds the q-CLT |
| prf:trace-locality-meets-gs-nonlocality | **fail** | part (3): the "vertex volumes" V̂ᵢ are never defined, and the step "multiplicativity of the standard trace on products of matrix units" is not a valid argument (trace is not multiplicative). Cites "Wenzl 1988, Theorem 5.13.2 in the QOU manuscript" (mixed citation); still writes Wedderburn over ℚ(q^½), a convention-C remnant; "checked exactly for every λ ⊢ n ≤ 5" is a computation inside the proof |

## Update 21:23Z from "Make the Lean foundations real"

PR #7915 (open, not yet on main) already removes both Casimir axioms, each with a
Lean refutation, and builds a real U_q(sl₂) quotient with a proved-central Casimir.
It also fixes the jones-markov-trace docstrings (convention C wording on `z`,
`nondeg`). This pilot read main `b2b349f36`, so those rows describe main as it
stands. They will need re-review once #7915 merges. That thread has queued the
other Lean items.

## Tally

- S↔L, 19 statements: pass 5, warn 3, fail 11 (2 critical).
- S↔P, 16 proof blocks + inline: pass 4, warn 5, fail 7 (1 critical, a false statement); 6 statements have no proof block.

## Retraction inside this pilot

I first wrote that three statements (lagrange, pontryagin, knot-eigenbasis) were
cut off mid-sentence. That came from my own display truncation (`cut -c1-300`);
the files are complete. Removed before anything was recorded.

## Pace

About 50 minutes for 35 items, around 1.5 minutes each, including hand algebra
and four sympy checks. The corpus is about 905 items, so a single reviewer needs
about 22 hours. Four parallel reviewers need about 6 hours each.

## Re-review after the owner-ruled fixes (2026-11-15, later)

Six commits on main fixed pilot findings in nine blocks (93cc4bbea, 13f8f3506,
83d5ee4bf, bb77bb402, b606a8175, 9fb2b100f). I re-read each changed block. No
`.lean` file changed. The new verdicts are appended after the earlier ones,
because the earlier verdicts recorded the old text.

| block | S↔L | S↔P | what changed / what remains |
|---|---|---|---|
| figure-eight-reeb-rotation | fail | warn (was fail) | q-range added and proved. The Lean is still a generic lemma. The exterior claim is left implicit, and the "lepton channels" reading is still in the statement |
| pion-half-figure-eight | fail | pass (was warn) | The proof now splits h²<1 from h²≥1. The Lean is still a tautology |
| three-strand-color-winding-rigidity | pass | pass (was warn) | Hypothesis is now 1−q⁴ invertible. Note a₂ vs a₋₂ label mismatch between statement and proof |
| hoefsmit-binding-amplitude | fail | warn (was fail) | Physics moved out. The Lean still defines b by its value. The statement omits q⁴≠1 |
| frobenius-lepton-meson-bridge | fail | warn (was fail) | Physics moved out. The Lean is still `rfl` on a table. The coupling claims are unproved |
| meson-em-sinh-closed-form | fail, minor (was pass) | warn (was fail) | Empirical content moved out. **New:** the statement says "R a field" while the Lean needs `Invertible 2`; the identity fails to make sense in characteristic 2 |
| meson-qcg-fusion-identity | pass | pass (was warn) | Mass reading moved out |
| knot-eigenbasis-complete | fail | warn (was fail) | TL quotient and the inclusions are fixed. The Lean is still self-assuming. "Knot types label summands" is not shown |
| trace-locality-meets-gs-nonlocality | fail | warn (was fail) | Part (3) moved out. **New:** the Lean class still carries `productFactorisation` (false for the Markov trace) and a convention-C docstring on z |

## Second re-review, after PR #8075 (2026-11-15, 23:30Z)

PR #8075 fixed the items left from the first re-review and moved two more readings into remarks. These are the new verdicts.

**Statement vs proof (`da-non-sequitur`):** all six blocks now pass:
- figure-eight-reeb-rotation
- hoefsmit-binding-amplitude
- meson-em-sinh-closed-form
- knot-eigenbasis-complete
- trace-locality-meets-gs-nonlocality
- three-strand-color-winding-rigidity. This one was already a pass; only its statement's a₋₂ label was fixed.

**Statement vs Lean (`proof-narrative-lean-equiv`):**
- **Pass:** meson-em-sinh-closed-form and three-strand-color-winding-rigidity.
- **Fail, because the Lean is unchanged on main:**
  - figure-eight-reeb-rotation
  - hoefsmit-binding-amplitude
  - knot-eigenbasis-complete
  - trace-locality-meets-gs-nonlocality. Its fix is on #7915 and has not landed.
- **n/a:** composite-crossing-parity and boltzmann-constant. Owner rulings made them a conjecture and a definition, and the criterion only applies to theorems, lemmas, propositions and corollaries.
