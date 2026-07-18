# α_EM correspondence attack, brick 1 — the conjugation-doubling dictionary, corrected

**Date:** 2026-07-18 · **Axis:** the single remaining `1/π` wall (the correspondence
statement, per the merged conjecture-statement PR) · **Tier:** symbolic-exact structural
facts + one scope-(a) exclusion · **Derives no clause; no fit; nothing wired; `1/(8π)`
stays phase-4 (R1 canonical).**

Probe [`alpha_em_conjugation_doubling_dictionary_probe.py`](../../computations/alpha_em/alpha_em_conjugation_doubling_dictionary_probe.py)
→ [witness](../../computations/alpha_em/alpha-em-conjugation-doubling-dictionary.witness.json) (4/4).

## Context

The merged conjecture-statement PR collapsed the `1/π` wall to one correspondence
statement and named the **unification hypothesis**: the Hecke channel pair `e₊/e₋` and
the Hodge pair `H^{1,0}/H^{0,1}` (#3920's doubling) are the *same* conjugation doubling,
with the naive dictionary *{bar involution ↔ complex conjugation}*. This brick tests that
dictionary exactly — and corrects it.

## Findings (all exact, mod the Hecke relation)

- **(D1) Naive dictionary REFUTED.** The bar involution (`q→q⁻¹`, `σ→σ⁻¹`) **fixes** each
  channel individually: `bar(e₊)=e₊`, `bar(e₋)=e₋`. Complex conjugation *swaps*
  `H^{1,0}↔H^{0,1}`; a channel-fixing involution cannot correspond to a channel-swapping
  one. *{bar ↔ conjugation}* is excluded (scope-(a)).
- **(D2) The genuine channel-swapper is the TRANSPOSE duality** `φ: q → −q⁻¹` (σ fixed):
  it preserves the Hecke relation and swaps `e₊ ↔ e₋` exactly — the eigenvalue swap
  `q ↔ −q⁻¹`, i.e. the symmetric/antisymmetric (partition-transpose) duality. **Corrected
  dictionary: {transpose ↔ complex conjugation}.**
- **(D3) Fixed-locus coincidence (exact).** The transpose-fixed locus is `q² = −1` —
  *identical* to the equal-channel-weight locus of the resummed tower (`w₊=w₋=½` iff
  `q²=−1`, the merged F2). Channel democracy occurs precisely at the transpose-symmetric
  point; the classical limit `q=1` is bar-fixed. The two involutions organize the two
  special loci of the tower.
- **(D4) The sharp remaining sub-question (equivariance).** On the Hodge side conjugation
  is **S₅-equivariant** (`χ_std` is real, so `H^{0,1} ≅ H^{1,0} = std`); on the partition
  side the transpose maps `std=(4,1)` to `(2,1,1,1)=std⊗sign` — a *different* irrep
  (`χ((12))`: 2 vs −2). The corrected dictionary matches the two 2-element channel sets
  with involution, but its S₅-equivariant content — whether the τ-identification carries
  the *2-strand channel* transpose or the *5-letter partition* transpose to conjugation —
  is the precise next question.

## What this changes

The correspondence statement ("the `q→1` one-loop equals `a₀·α`") stands as the wall; its
unification route now has a **corrected, sharper target**: identify the transpose duality
`q→−q⁻¹` with complex conjugation on `H¹(Bring)` under τ, resolving the D4 equivariance
tension. The bar involution instead pairs with a structure *respecting* the Hodge
splitting (consistent with its fixing of the channels and of the classical point `q=1`).

## Brick 2 (same PR): D4 ADJUDICATED — the τ target is unique

Probe [`alpha_em_d4_equivariance_adjudication_probe.py`](../../computations/alpha_em/alpha_em_d4_equivariance_adjudication_probe.py)
→ [witness](../../computations/alpha_em/alpha-em-d4-equivariance-adjudication.witness.json) (4/4):

- **(E1) The 5-letter partition transpose is EXCLUDED.** Conjugation preserves the
  S₅-isotype (`χ_std` real over all 7 conjugacy classes ⇒ `H^{0,1} ≅ std`); the partition
  transpose is isotype-*changing* (`std → std⊗sign`, `χ((12))`: 2 vs −2). An
  isotype-changing involution cannot be an isotype-preserving one (scope-(a)).
- **(E2) The 2-strand channel transpose survives** — it acts on the loop-parameter/channel
  index only, S₅-neutral, isotype-preserving like conjugation. **The τ target is unique.**
- **(E3) Fibre-circle geometry (exact).** On `|q|=1`: bar = reflection across `ℝ` (fixed
  `q=±1`, the classical points, channels fixed); transpose = reflection across `iℝ` (fixed
  `q=±i`, the democratic points, channels swapped); composition = the antipode `q→−q`. The
  two involutions are the two reflection axes of the fibre circle.
- **(E4) The spec(J) coincidence (exact).** At `q=±i` the Hecke relation degenerates to
  `(σ∓i)² = 0` — the channel pair *merges* with common eigenvalue `±i`. And `{+i,−i} =
  spec(J)`: the complex-structure eigenvalues whose eigenspaces are `H^{1,0}/H^{0,1}` and
  whose eigenspace-swap **is** conjugation. The channel doubling collapses exactly at the
  eigenvalues of the operator whose doubling it is conjectured to match.

**Net.** The unification route's target is now unique: *τ carries the 2-strand channel
transpose `q→−q⁻¹` to complex conjugation on `H¹(Bring)`.* The partition transpose is not
lost — it is the *flavor*-side fermion–boson/spin-flip doubling (cf. the merged
SU(4)/Schur–Weyl work), a different doubling from the photon channel pair. The full
τ-functor derivation (the correspondence wall) remains open; every necessary condition now
points at one object.

## Scope guard (STRICT)

Exact structural facts + one exclusion; derives **no** clause of the per-loop conjecture;
no fit; nothing wired. Coordinates with (not duplicating): the merged conjecture-statement
PR (F1–F3), #3920 (Hodge doubling), `ba606720e` (GB form), `dd55a5748` (R1 ruling).

## Cross-references

- The wall + unification hypothesis: `2026-07-18-alpha-em-perloop-conjecture-statement.md` (merged)
- Hodge doubling: `2026-07-18-alpha-em-multiplicity2-realcomplex-count.md` (#3920)
- GB adjudication: `2026-07-18-alpha-em-gauss-bonnet-measure.md`
