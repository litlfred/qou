# Pre-registration — which word creates the e⁻ν̄ pair in β⁻ decay (task W)

Written 2026-11-21, BEFORE any number in this directory was computed. Bean `qou-99qc`.
Owner (Carl, 2026-11-21) asked for a **proposal, for his ruling**, of the word that creates the
lepton pair. Nothing here selects a word; every surviving candidate is reported, and none is
chosen by its `Q_β` or by any residual (AGENTS.md §NO FITTING). CODATA `Q_β` is not read at all.

## Fixed setting (stated choices, not derived)

* `H_4(q)`, generators `σ₀, σ₁, σ₂` (0-based), `σᵢ² = hσᵢ + 1`, `h = q − q⁻¹`; exact over `ℚ(q)`
  with the P1 engine (`hecke_exact.py`, `jimbo.py`, copied verbatim from branch
  `claude/beta-gs-reduction-n-gammagamma-2026-11-20`, #8681).
* Nucleon on strands 0–2 = `β_Bor = (σ₀σ₁⁻¹)³` — the element the γγ + reading-3 selection gives
  on three strands for BOTH n and p (`frobeniusSelected_ten_unique`, #8636). One lepton strand,
  position 3. Process word `W = β_Bor · X`; `X` is the candidate pair-creation word.
* Lepton labels: strand-colour reading **premise L** (#8673, owner left L UNDECIDED): the lepton
  strand is a second copy of `V = span(u, d)` with `ν = u`, `e⁻ = d`; the ν̄ is the incoming ν by
  crossing. Everything that uses L is labelled `[L]`. The knot reading (e⁻ = trefoil `σ³`,
  def:electron-knot, owner ruling #8677) is checked separately and only where it is a word property.

## Principles, as predicates on X (each reported separately; none combined by choice)

| id | principle | predicate |
|---|---|---|
| G | γγ rule (`qou-ales`), as ruled in Lean | `X` is a product of vertices `Vᵢ = σᵢσᵢ₊₁⁻¹` (`GammaGammaWord`) |
| Ḡ | γγ with mirrors (variant, NOT ruled) | product of `Vᵢ` and `V̄ᵢ = σᵢ⁻¹σᵢ₊₁` (as used in `GammaGammaFourStrandFlavour.lean`) |
| CC `[L]` | derived charged current (#8638) | the strand-tracked block `n⊗ν → p⊗e⁻` of `ρ_Jimbo(W)` is not identically 0 |
| wrap | P1/P4 (#8681) | the lepton strand crosses ≥ 2 distinct nucleon strands |
| X≠0 | nucleon sensitivity | `C(X) := tr_D(β X) − tr_D(β)·tr_D(X) ≢ 0` (convention D) |
| R3 | confinement SDP reading 3, whole word, every level | `χ_λ(W)|_{q₀} ≥ 0` on every `λ ⊢ 4` with `y_λ > 0` (convention D) |
| Q | charge / T³ / Y conservation | checked, expected to admit every word (Hecke elements commute with `U_q`, #7975) |

Blocks that are not words (reported as candidate ELEMENTS, evaluated by the same functionals):
the derived passage `P = σ₀σ₁σ₂` (#8638 leftward positive, `(hq)·T⁺`) and its bar image
`P̄ = σ₂⁻¹σ₁⁻¹σ₀⁻¹`; the weak knot `T(3,5) = (σ₁σ₂)⁵` placed on strands 1–3 (the only placement
touching the lepton); the left-handed vertex insertion `ιᵢ = −h·P_L(σᵢ)`, `P_L(σ) = (σ + q⁻¹)/[2]`
for `|q| > 1` (`weakVertex_sub_letter`).

## Enumeration (bounds fixed now)

1. Letter level: every freely reduced word in `σ₀^±, σ₁^±, σ₂^±` of length ≤ 4 (937 words incl. the
   empty one); predicates G, Ḡ, CC, wrap, X≠0, Q exact; R3 at `q₀` (proton pin, 70 dps).
2. γγ level: every `G` word of length ≤ 8 (vertices `V₀, V₁`; 30 words) and every `Ḡ` word of
   length ≤ 6 (4 + 16 + 64 = 84 words).
3. Block level: products of ≤ 2 blocks from {`V₀, V₁, V̄₀, V̄₁, P, P̄, T(3,5)`}.
Screening is exact in `ℚ(q)`; nothing is decided by a float.

## Priors (stated before computing)

* **PR1 (95 %)** — by `writhe_eq_zero` / `length_even` (Lean, already proved), `P`, `P̄`, the
  trefoil `σ³` and `T(3,5)` are NOT γγ words. Scope (b), invariant = writhe.
* **PR2 (60 %)** — some G word has CC ≠ 0 (a γγ word can still move the lepton strand across the
  nucleon). If PR2 FAILS, the γγ grammar and the derived charged current are disjoint, and the
  pair-creation word must lie outside the ruled grammar: that is an owner decision, not ours.
* **PR3 (85 %)** — CC ≠ 0 implies wrap (a one-strand join carries no `n → p` block).
* **PR4 (70 %)** — no single principle forces a unique word; the conjunction G ∧ CC ∧ wrap ∧ R3 with
  crossing-count minimality leaves a small family (≥ 2 words, related by the bar involution or by
  `V₀`-conjugation). Uniqueness, if it appears, comes from the cost, not from reading 3 (cf.
  `feasible_pair_delta_ne_zero`).
* **PR5 (80 %)** — every CC block is `O(h)` at `q → 1` (the W coupling vanishes classically).
* **PR6 (90 %)** — Q admits every word.

Decision rules: a principle "forces" a word iff exactly one word of the enumeration satisfies it
(with minimal crossing count where stated). Every survivor is reported with its normal form, wrap,
`C(X)`, and `q → 1` order of `C` and of the CC block. No ordering by value.
