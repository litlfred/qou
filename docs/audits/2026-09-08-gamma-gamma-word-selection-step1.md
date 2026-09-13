# γγ word selection — step 1 (Lean predicates) and step 2 (net-row fix, re-run)

**Bean:** `qou-ales` (owner ruling 2026-09-08). **Branch:**
`claude/ales-gg-word-selection-2026-09-08`. **Scope:** steps 1 and 2 of the
bean's closing plan only. Step 3 — comparing the surviving word for p, n, ²H,
pp, nn against the template words, and the diproton sign (`qou-vbyi`) — is
**not** done here and the bean stays open (rule 13a).

Owner ruling, verbatim (chat, 2026-09-08):

> "All selection of great words should be done through gamma gamma production
> and the semi-definite product solutions at q_0. Shouldn't use census."

Read, as the bean reads it, as *braid* words: every canonical braid word is to
be **selected** by the γγ (Breit–Wheeler pair-production) construction with
the confinement SDP at q₀ picking the canonical `T_w`; census
volume-matching is excluded as a selection mechanism.

## 0. What the corpus already held (corpus-grep, six paths)

Nothing below was re-derived. Cited so a reader can see what step 1 built on.

| where | what exists | used here as |
|---|---|---|
| `computations/gamma_gamma_pair_production_decomposition.py` | `β_Bor = (σ₀σ₁⁻¹)³`; each `σ₀σ₁⁻¹` is a **γγ̄ pair-production element** (photon on strands (0,1), anti-photon on (1,2)) | the definition of the pair-production *vertex* |
| `content/…/predicted-spectra/breit-wheeler-pair-production-derivation.md` | bare pair `γγ = σ₀²`, `NF = (q−q⁻¹)σ₀ + 1`, 1.6 % short of `2m_e`; colored-photon admixture with parameters `φ₀, φ₁, φ₀₁` | the *other* γγ reading (bare `σ₀²`); the `φ` parameters are noted as not-yet-derived and are **not** used |
| `QOU/Archimedean/BreitWheelerPairProduction.lean` | structure carrying the bare-pair NF coefficients, de-axiomatised via `TransferMatrixOperator` (bean `h2yz`) | prior Lean; a data carrier, not a predicate on words |
| `predicted-spectra/breit-wheeler-pair-production.lean`, `gamma-gamma-generates-particles.lean` | colored-photon threshold non-negativity; the two-photon product reaches `L₋` | prior Lean; about coefficients, not about which *words* are γγ-produced |
| `QOU/BraidKnot/SymmetricCrystalPairProduction.lean` | Type-B folding conjecture class (bar-invariance) | unrelated to word selection |
| `QOU/QBeta/GluonVertexPsdParity.lean` | `vertex_psd_iff_even`: `σ₀^k` is PSD on `H₂` iff `k` even (sorry-free, generic ordered field) | reused: the `H₂` instantiation of the new predicate reduces to it |
| `QOU/Interactions/ConfinementSDP.lean` | `prop:confinement-sdp` primal–dual data as a typeclass (`HasConfinementSDPData`), strong duality supplied not derived | prior Lean; carries the *program*, not a selection predicate on words |
| `QOU/StandardModel/ChiralFermionBraidWords.lean` | `BraidWord := List ℤ`, `gluonUnit = [1,-2]`, `borromean`, writhe 0 for both | the new file's `toCorpus` ties to this encoding |
| `computations/sdp_gamma_gamma_to_qqbar.py` | STARTER SCAFFOLD: `H₂` γγ→e⁺e⁻ demo, `H₃` outline, "NO Vol_hyp. NO census." | the PSD-parity selector it names is what `SDPSelected` formalises |
| `computations/nucleus_operator_selection_sdp.py` | sweeps `n_target` **from the existing atom word** — circular for selection | not used |
| `computations/probes/frobenius_admissibility_diagnostic.py` + bean `qou-vd7j` | the 0/3558 is an over-determination artifact: net row `1ᵀx=A` vs `Gx=nf` on an **invertible (rank 6)** Gram | the "cheap next step" step 2 implements — and finds changed underneath it (§2) |
| beans `qou-1qsw`, `qou-u2jg` | gluon `σ₀²` term (crossing budget 11); "z_D is the unique Markov trace whose radical contains the three-strand antisymmetriser" | the radical identity step 2 rests on |
| `library/` | `INDEX.md`: 0 rows for *breit* / *pair production* / *gamma gamma*; `sections/` and `ocr/` tiers: 0 files for *breit-wheeler* | no held source to cite; not evidence the physics literature lacks one |

No existing Lean predicate of the form "this word is pair-production-generated"
was found in the tree (grep for `PairProduction|GammaGamma|BreitWheeler` over
`content/**/*.lean`: the five files above, none of which quantifies over words).

## 1. Step 1 — what was defined and proved

File: [`QOU/Mass/GammaGammaWordSelection.lean`](https://github.com/litlfred/qou/blob/378dca11dc/content/quantum-observable-universe/lean/QOU/Mass/GammaGammaWordSelection.lean)

**Verification.** `lean -DautoImplicit=false -s 65536 <file>` with the restored
`LEAN_PATH` (Mathlib 3480 oleans, QOU 2713): **exit 0**. `#print axioms` on every
theorem: `[propext, Classical.choice, Quot.sound]` or none — **no `sorryAx`**.

### Definitions

* `Crossing` (`gen : ℕ`, `pos : Bool`), `Word := List Crossing`.
* `vertex i := [σᵢ, σᵢ₊₁⁻¹]` — the γγ̄ pair-production vertex.
* `GammaGammaWord : Word → Prop` — inductively, the (left-to-right) products of
  vertices; `[]` is the empty product. **This is the "product of
  pair-production vertices" reading of the ruling**, sourced to the `.py` above.
* `altChar q w := ∏ (if pos then −q⁻¹ else −q)` over a generic `[Field R]` —
  the one-dimensional alternating representation `σᵢ ↦ −q⁻¹` of the Hecke
  algebra, evaluated on a word.
* `WedderburnBlocks R W ι d` — for each block label `l`, the matrix image
  `proj w l : Matrix (Fin (d l)) (Fin (d l)) R` of each candidate.
* `WedderburnBlocks.PSDFeasible B w := ∀ l, (B.proj w l).PosSemidef` — the
  **actual** `Matrix.PosSemidef` cone, block by block (over any
  `[Ring R] [PartialOrder R] [StarRing R]`).
* `SDPSelected B cands cost w : Prop` — a structure with three fields:
  `w ∈ cands`, `PSDFeasible B w`, and `∀ w' ∈ cands, PSDFeasible B w' → cost w ≤ cost w'`.
  This is what "the SDP selects the canonical `T_w`" means: feasibility (1)+(2)
  of `prop:confinement-sdp` on a candidate, plus optimality.

### Theorems (all sorry-free; each was checked to hold before being stated)

| theorem | statement | why it is falsifiable |
|---|---|---|
| `writhe_eq_zero` | γγ-produced ⇒ writhe `0` | a vertex with two positive crossings would refute it |
| `length_even` | γγ-produced ⇒ even crossing count | |
| `altChar_eq_one` (`q ≠ 0`) | γγ-produced ⇒ `altChar q w = 1` | each vertex is `(−q⁻¹)(−q)`; a bare `σ₀²` vertex would give `q⁻²` |
| `altChar_ne_zero` | hence `≠ 0` | the lemma step 2 measures |
| `not_gammaGamma_single` | a lone `σᵢ` is **not** γγ-produced | writhe `1`; the template `pp` bond `σ₀` on its own |
| `borromean_gammaGamma`, `toCorpus_borromean` | `β_Bor` is γγ-produced and equals the corpus's `BraidWords.borromean` | ties the new encoding to the existing one by `decide` |
| `h2_psdFeasible_iff_even` (`0 < q`, over ℝ) | on `H₂` with the two `1×1` blocks `q^k`, `(−q⁻¹)^k`, `PSDFeasible k ↔ Even k` | recovers `GluonVertexPsdParity.vertex_psd_iff_even` through `Matrix.posSemidef_diagonal_iff` — the abstract predicate is not vacuous |
| `h2_two_feasible_one_not` | `σ₀²` feasible, `σ₀` not | |
| `SDPSelected.cost_eq` | two selected words have equal cost | |

Base ring: words/writhe/`altChar` are generic (§7c); only the `H₂`
instantiation is on `ℝ` (needs `StarOrderedRing` and an order).

What step 1 does **not** do: it does not construct the `H₃` (or `H_{3A}`)
Wedderburn projections in Lean, so `SDPSelected` at the nucleon level is a
predicate with no instance yet. That is the intended shape — the predicate is
stated before the search — and it is what step 3 would instantiate.

## 2. Step 2 — the vd7j net-row fix, re-run under convention D

Probe: [`computations/probes/frobenius_admissibility_net_row_probe.py`](https://github.com/litlfred/qou/blob/bec27adb1e/computations/probes/frobenius_admissibility_net_row_probe.py)
(mpmath 60 dps end to end, proton pin `Q_50_DIGIT_STR`, witness
`computations/probes/frobenius-admissibility-net-row-probe.witness.json`,
`q0Anchor = proton`, 6/6 assertions pass, 21.9 s wall).

**No AME / CODATA binding value is read.** The demand profile is each word's
own normal form; survival is decided by the algebra.

### 2.1 What changed underneath vd7j

`qou-vd7j`'s diagnostic (2026-08-02) was made on the **convention-C** Gram
(rank 6, invertible). Under **convention D** (canonical since 2026-08-15) the
`H₃(q)` trace form on the NF basis is singular. Measured at the proton pin:

| quantity | value | source |
|---|---|---|
| Gram eigenvalues | `−0.75270211, −2.44e−61, 0.75270211 (×3), 4.2303392` | `gram.gram_matrix_mp(60)`, `mp.eigsy` |
| rank / neg-norm / null | `5 / 1 / 1`; `‖G v‖ = 7.6e−62` | `gram.radical_mp` |
| radical `v_k` | `(−1/q)^{len b_k}` = the alternating character of the basis, `max|v_k − ε(b_k)| = 0.0` | proved exactly over ℚ in `gram_radical_exact_probe.py` |
| `1ᵀv` | `0.0902372332705995` (≠ 0) | this probe |

Consequences, all measured:

1. `G x = nf` is solvable iff `nf ∈ range(G) = v^⊥`, i.e. iff `⟨v, nf⟩ = 0`.
2. When solvable the solution is a line `x_min + t·v`; since `1ᵀv ≠ 0`, the net
   row `1ᵀx = A` is **always** satisfiable by choosing `t`. **The
   over-determination vd7j named is gone under D** — the net row is no longer
   the obstruction, whether dropped or kept.
3. `⟨v, nf(W)⟩ = ε(W)`, the alternating character of the word (a product over
   crossings of `c·(−1/q) + d`), because `v_k = ε(b_k)` and `ε` is a ring
   homomorphism. Measured: `max |⟨v,nf⟩ − ε(W)| / max(1,|ε|) = 7.78e−61` over
   all 4238 words (an L1-style cross-check, not a fit).
4. Every crossing type in play has a **nonzero** `ε`-factor: `σ₀ ↦ −1/q`,
   `σ₀⁻¹ ↦ −q`, colour-weighted p-n `↦ −1/q + D_PN`, γγ vertex `↦ 1`
   (`altChar_eq_one`). So `ε(W) ≠ 0` for every candidate, and **no** candidate's
   demand profile is in the range of the Gram.

### 2.2 Candidate words and the per-nucleus result

Each nucleus is built exactly as `pyhecke.atom.build_atom_nf` builds it
(Borromean `B₃` + quark crossings + gluon `σ₀²` per nucleon, then a crossing
with each previous nucleon; word builder cross-checked against the float64
`build_atom_nf` to `5.2e−16` on the eight template words), except that every
inter-nucleon **bond** is free over four types — `S` `σ₀`, `I` `σ₀⁻¹`, `C`
colour-weighted (R3), `G` the γγ vertex `σ₀σ₁⁻¹` — so a nucleus with
`B = A(A−1)/2` bonds has `4^B` candidates. Template = `pp→S`, `nn→I`, `pn→C`.
Bare nuclei (no electron crossings); the `--atoms` variant (Z electrons) gives
the same counts.

| nucleus | A | bonds | candidates | **survive** | `ε(template)` | min `|ε|` over candidates | net of `x_min` (template) | `1ᵀnf` (template) |
|---|---|---|---|---|---|---|---|---|
| p   | 1 | 0 | 1    | **0** | −0.73922357 | 0.739224 | 0.35275 | 1.20808 |
| n   | 1 | 0 | 1    | **0** | −0.91076221 | 0.910762 | 0.29514 | 0.98092 |
| ²H  | 2 | 1 | 4    | **0** | −0.67687668 | 0.606549 | 0.44545 | 1.40196 |
| pp  | 2 | 1 | 4    | **0** | −0.49230814 | 0.492308 | 0.55543 | 1.87742 |
| nn  | 2 | 1 | 4    | **0** | −0.92071371 | 0.747301 | 0.32856 | 1.01437 |
| ³H  | 3 | 3 | 64   | **0** | +0.68795163 | 0.448376 | 0.24972 | 1.29998 |
| ³He | 3 | 3 | 64   | **0** | +0.45321002 | 0.363926 | 0.38979 | 1.96947 |
| ⁴He | 4 | 6 | 4096 | **0** | +0.46310193 | 0.242367 | 0.73860 | 2.26908 |

Total: **4238 candidates, 0 survivors.** The `1ᵀnf` column is the quantity
`all_nuclides_sdp_admissibility.py` used as `n_target`; the `net of x_min`
column is vd7j's "consistent net `1ᵀG⁻¹nf`", now computed on the quotient
`H₃/rad` (`gram.gram_quotient_solve_mp`) since `G⁻¹` does not exist under D.
Both are O(1) and neither equals `A`, as vd7j found — but under D that is
moot, per 2.1(2).

### 2.3 Reading — scope-(a), and what it does *not* say

**Scope-(a) negative.** *The Frobenius-demand formulation `G x = nf(W)`, as
posed in `all_nuclides_sdp_admissibility.py` / `solve_frobenius_dual_lp`, admits
no word for any of the eight light systems under convention D, with or without
the net row.* The reason is structural to that formulation: the demand profile
carries a nonzero alternating-character component, and the D-frame trace form
kills exactly that component (its radical is the antisymmetriser). A word would
survive only if some factor had `ε = 0`, i.e. `d = 1/q` — the factor
`σᵢ + q⁻¹`, which is (up to scale) the q-symmetriser on that pair. None of the
template crossing types, and no γγ vertex, is of that form.

**What it does not say.**

* Nothing about the PSD **confinement SDP** (`prop:confinement-sdp`, the
  program `SDPSelected` formalises): that is a different program (PSD blocks +
  trace normalisation + cost), not `Gx = nf`. Step 2 was scoped to vd7j's
  formulation; the ruling's selector is the SDP, and it has not been run here.
* Nothing about which word is *the* nucleon word. Zero survivors is a fact about
  the demand-profile test, not a refutation of γγ-produced words (which, by
  `altChar_eq_one`, are the cleanest case: `ε = 1` exactly).
* The vd7j finding is **re-scoped, not contradicted**: on the C-frame Gram it
  was correct; on the D-frame Gram the net row is satisfiable and the radical
  is the obstruction. Bean `qou-vd7j` is updated with this.

## 3. Precision preflight

`scripts/precision-gates.sh --changed` (with `qou_substrate` supplied on
`PYTHONPATH`; the tree has no editable install): the new probe/witness are
not named in any red; the reds reported are tree-wide ratchets that
pre-exist on `main` (see
`docs/audits/2026-09-08-raw-float64-ratchet-is-regressed-on-pristine-main.md`).
The ten tree-measuring audit witnesses the gate regenerates were reverted and
not committed, per the gate's own instruction (bean `qou-v0t8`).

## 4. What stays open (step 3, not done here)

* Instantiate `SDPSelected` at `H₃` (the nucleon) — the Wedderburn projections
  `(3), (2,1), (1³)` on the six-element NF basis — and run the PSD selection
  over γγ-produced candidates at q₀. That is the ruling's selector; step 2 did
  not run it.
* Compare the selected word for p, n, ²H, pp, nn with the template words
  (`uu→σ`, `dd→σ⁻¹`, `ud→averaged`, `pn→colour-weighted`). The diproton sign
  (`qou-vbyi`) is the first falsifiable output. Observation recorded, not
  acted on: the template `pp` bond `σ₀` is not γγ-produced
  (`not_gammaGamma_single`), while the `G` bond `σ₀σ₁⁻¹` is.
* The `φ₀, φ₁, φ₀₁` colored-photon parameters of the Breit–Wheeler block
  remain underived; nothing here uses them.
* Default if nothing further is done: words stay template-assigned;
  `qou-ales` stays `in-progress` at step 2 of 3.
