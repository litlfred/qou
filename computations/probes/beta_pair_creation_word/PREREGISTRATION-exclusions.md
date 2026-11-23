# Pre-registration, part 2: can candidates A–D be excluded by proved invariants?

Written 2026-11-21, BEFORE any number of part 2 was computed. Bean `qou-99qc`. Part 1:
`PREREGISTRATION.md` (commit `ee04d3c394`).

The owner (Carl, 2026-11-21) wrote about the four candidates: *"Keep these as options and explore
the implications of each. Can we rule out some of them?"* So this part tries to EXCLUDE, never to
select. No candidate is ruled in or out by `Q_β` or by any residual; CODATA is not read.

## Candidates (from part 1)

* **A** `X = V₁³ = (σ₁σ₂⁻¹)³`.
* **B** the derived W passage `X = σ₀σ₁σ₂` (#8638).
* **C** the single lepton crossing `X = σ₂`.
* **D** the grammar question: are the mirror vertices `V̄ᵢ = σᵢ⁻¹σᵢ₊₁` γγ? If yes, the eight
  length-6 Ḡ words that pass G-free CC ∧ R3 are candidates.

The process word is `W = X · β_Bor` with `β_Bor = (σ₀σ₁⁻¹)³` on strands 0–2, as in part 1.

## Scoping rule

An exclusion is written as scope (b) only if a proved invariant forbids the candidate. The
invariant is cited, and the tier of each cell is one of: proved-lean / symbolic-exact (exact in
`ℚ(q)`, numbers only for signs at the proton `q₀`, 70 dps) / conditional (on a named premise) /
empirical. Everything else is scope (a).

## Definitions fixed now

1. **Chirality.** A word is *chiral* iff its CC block `n⊗ν → p⊗e⁻` is non-zero and its reverse
   block `p⊗e⁻ → n⊗ν` is zero (part 1's `reverse_block_nonzero` field). The derived passage is the
   reference (`(q²−1)·T⁺`). Left projector `P_L(σᵢ) = (σᵢ + q⁻¹)/[2]` (idempotent for `|q| > 1`).
2. **Lepton knot type.** Closure of `W` as a braid. The lepton component is the cycle of the
   permutation of `W` that contains strand 3. A one-strand component is an unknot (a one-strand
   closed braid). For a two-strand component, the restricted braid is `σ^k`, with `k` the signed
   number of crossings between the two strands, and the closure is `T(2,k)`. It is a trefoil iff
   `k = ±3`. Components on three or more strands are reported as such and not identified.
   Two readings, because premise L is undecided:
   * **knot reading** (#8677: electron = trefoil, up quark = unknot strand): the electron is the
     lepton component, and it must close to `T(2,±3)`;
   * **strand-colour reading** (premise L): the electron is the `d` label on strand 3; the knot type
     of the component is not constrained.
3. **Nucleon sensitivity.** Cross term `C(X) = tr_D(βX) − tr_D(β)·tr_D(X)`, as in part 1.
4. **Reading 3 under normalisation.** A candidate fails reading 3 for every normalisation iff its
   vector `(χ_λ(W))_{y_λ > 0}` at `q₀` has entries of both strict signs. That pattern is unchanged
   by any non-zero scalar (up to a global sign flip, which keeps it mixed) and by conjugation
   (characters are class functions).
5. **Mirror closure (D).** Three ways the grammar could already contain `V̄ᵢ`:
   (i) at the element level, `1 + c·V̄₀` lies in the photon family `γ(φ)` for some `φ`;
   (ii) `V̄ᵢ` equals `1 + c·Vᵢ` or another photon-scaled vertex;
   (iii) the bar involution `σ ↦ σ⁻¹, q ↦ q⁻¹` maps `V₀ ↦ V̄₀` and maps the photon family to itself.
   Plus at the word level: `V̄ᵢ` is not a `GammaGammaWord`.
6. **Five strands (item 6).** Strands 0–2 are the nucleon, strand 3 is e⁻, and strand 4 is ν̄.
   The pair is created from the vacuum as the `U_q`-singlet cup on strands 3, 4, which is
   `ud − q⁻¹·du` (the `−q⁻¹` eigenvector of `Ř`). Charge: `n + cup` carries two `u`, and
   `p ⊗ e⁻ ⊗ ν̄` must carry two `u`, so `e⁻ = d` and `ν̄ = d` (`ū ≅ d` under `V* ≅ V`).
   CC₅ block: `⟨p ⊗ d ⊗ d| ρ(W) |n ⊗ cup⟩`, strand-tracked. This is a stated choice, labelled
   **[L5]**. G words on five strands use `V₀, V₁, V₂`, enumerated to length 8 (121 words).
   Reading 3 on `H₅` uses `χ_(5), χ_(4,1), χ_(3,2)` with Markov weights solved and validated on all
   120 `T_w`.

## Priors (before computing)

* **P-A1 (90 %)** A's reverse block stays non-zero after inserting `P_L(σ₂)` before or after `V₁³`.
* **P-A2 (95 %)** In the knot reading, every pure `X` (A included) gives an unknot lepton
  component. This is a (b) exclusion conditional on the knot reading.
* **P-B (85 %)** B's character vector at `q₀` is mixed-sign (`χ_(4) > 0`, `χ_(3,1) < 0`), so B
  fails reading 3 under every non-zero normalisation and under conjugation.
* **P-C (95 %)** `C(a + b·σ_{n}) = 0` for every nucleon element `x ∈ H_n`, by the Markov property
  alone. This is a (b) exclusion of C as an *energy-carrying* (non-factorising) word, invariant =
  Markov property. It says nothing about C as a bare W vertex.
* **P-D (70 %)** `1 + c·V̄₀` is a photon (`φ = (hc, −hc, c)`), and the photon family is
  bar-closed, so the mirrors are already present at the element level but not at the word level.
  The minimal ruling is then "γγ selection acts on photon elements, not on words".
* **P-5 (60 %)** On five strands, `V₁³` is still the unique cheapest G ∧ CC₅ ∧ R3 word.
