# Pre-registration, part 3: two-term traces, element-level γγ, and the B amendment

Written 2026-11-21, BEFORE any number of part 3 was computed, and before any number of part 2
was computed (part 2 is `PREREGISTRATION-exclusions.md`, commit `f816f993c8`; its definitions and
priors stand unchanged). Bean `qou-99qc`. The scope grew after part 2 was written: the owner asked
for every cross term in BOTH the one-term trace and the scored two-term form, and the task now also
asks whether `A·P_L` / `A·passage` are γγ-admissible and what amendment would admit B. Nothing is
selected; `Q_β` and CODATA are not read.

## 1. The two-term trace on four strands (definitions fixed now)

The scored form `two_term_covariant_all_pairs_qtrace` lives on the three-strand nucleon weight
spaces (`NucleonWeightSpaceQTrace`): insertion `Q₁₂ + Q₂₃ + Q₁₃`, weight `K^{⊗3}`, normalisation
`[2]_q³`, connected subtraction of the insertion's scalar value on the weight space. It is not
defined on four strands, so its extension is a choice, labelled here:

* `Q_quark = diag(2/3, −1/3)` on `V = span(u, d)`; `Q_lep = diag(0, −1)` **[L]** (ν = u, e⁻ = d).
* Insertion `Q_all = Σ_{i<j} Q_{s(i)} ⊗ Q_{s(j)}`, diagonal in the position basis, with `s(i)` the
  species of position `i`.
* `conn(X) = Σ_k [Tr_k(K^{⊗4} Q_all ρ(X)) − ⟨Q_all⟩_k · Tr_k(K^{⊗4} ρ(X))] / [2]_q⁴`, summed over
  the five weight spaces `k = #d`, with `⟨Q_all⟩_k = Tr_k(Q_all)/dim_k`. On a weight space where
  `Q_all` is a scalar this is exactly the scored connected subtraction.
* **T2cov** (the scored form extended verbatim, covariant): every position carries `Q_quark`.
* **T2lep** (labelled comparison, NOT covariant): positions 0–2 carry `Q_quark`, position 3 carries
  `Q_lep`. For a pure word, position = strand at the insertion, so T2lep is then also the
  strand-tracked value. For a non-pure word (B, C) it is position-labelled only.
* The one-term functional is `tr_D` (= `Σ_k Tr_k(K^{⊗4} ρ)/[2]⁴`, checked on all 24 `T_w`).
* Two-term functional `F_c = tr_D + c·conn`, `c` NOT chosen (the QED scale is a selection, #8524).
  Its cross term `F_c(Xβ) − F_c(β)F_c(X) = C₁ + c·C₂ + c²·C₂₂` with
  `C₂ := conn(Xβ) − conn(β)·tr_D(X) − tr_D(β)·conn(X)`, `C₂₂ := −conn(β)·conn(X)`.
  Reported: `C₁`, `C₂`, `C₂₂`, and `conn(Xβ)` itself, each exact.

Priors: **P-T1 (95 %)** under T2cov, `Q_all` is a scalar on every weight space for any number of
strands, so `conn ≡ 0` for every element and `C₂ = C₂₂ = 0` for every candidate (a structural
statement, provable; the covariant two-term form cannot distinguish candidates at all).
**P-T2 (80 %)** under T2lep, `conn(β) ≠ 0` already (the lepton charge breaks the scalar), and
`C₂(A) ≠ 0`. **P-T3 (50 %)** under T2lep, `C₂(σ₂) ≠ 0` (the Markov argument of part 2 P-C does
not cover a non-scalar insertion on strand 3).

## 2. Element-level γγ (definitions fixed now)

The ruled grammar `GammaGammaWord` is word-level. An element-level reading ("a product of photon
elements `γ(φ)` with free φ") is tested as a second, labelled reading.

**P-E1 (99 %)** the photon span on strands `i, i+1, i+2` contains `σᵢ`, `σᵢ₊₁` and both inverses,
so products of photons with free φ generate the whole `H₃` on those strands: element-level γγ
admits every element and is vacuous as a selection rule. **P-E2 (95 %)**
`[2]·P_L(σ₂) = q⁻¹·γ₁₂₃(0, q, 0)`, so `A·P_L(σ₂)` is a scalar times a product of three photons:
admissible element-level, not word-level. **P-E3 (100 %)** `A·passage` has writhe 3, so it is not
a γγ word (writhe invariant).

## 3. Chirality and reading 3 of the A-products (computed in part 3)

Elements `A·P_L(σ₂)`, `P_L(σ₂)·A`, `A·passage`, `passage·A`, each `·β`. **P-A3 (70 %)** at least one
of them is chiral (reverse block 0); **P-A4 (60 %)** none of the chiral ones passes reading 3.

## 4. B's reading-3 failure, beyond `q₀`

`χ_(3,1)(W_B)` exact; its real roots in `q > 1` computed exactly (sympy `real_roots`), so the sign
is known on every interval of `(1, ∞)`, not only at `q₀`. **P-B2 (50 %)** negative on all of
`(1, ∞)`. Amendments examined (no choice made): (i) reading 3 applied to the bound-state word only,
not the transition word; (ii) reading 3 on the bar image `P̄`; (iii) on `P_L`-projected passages.

## 5. Ring-coloured trace

The sibling branch `claude/borromean-ring-coloured-trace-np-2026-11-21` is not on the remote at the
time of writing (`git ls-remote` empty), so it is NOT evaluated; recorded as not available.
