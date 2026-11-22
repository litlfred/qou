# H10 result: deriving the wall's Hecke parameter (2026-11-21)

Pre-registration: `h10_preregistration.md`. Script: `h10_wall_parameter_probe.py`, output in `.out.txt`.

## Results

| candidate | Q | status | D(1) | D(q₀), V³ |
|---|---|---|---|---|
| **L Lusztig folding of lengths** | `q^{1/2}` | **conditional derivation**, no choice made here (see below) | 1 | **0.96807142877888556063** |
| E equal parameters | `q` | no corpus statement found | 1 | 0.93995737184425521828 |
| M type-B Markov | — | fixes a trace value `y = q²(Q−Q⁻¹)/(q²+1)`, not `Q`; any `y` is admissible | — | — |
| C coideal / Schur–Weyl | — | the corpus defines no coideal or symmetric pair (grep of `folio/`) | — | — |

## Why L is a derivation and not a choice

- In the folding `B(B_n) ⊂ B_{2n}`, the type-B bulk generator **is** the folded pair `σ_{n+i}σ_{n−i}`,
  which has Coxeter length 2. The wall is the middle crossing `σ_n`, which has length 1.
- For a quasi-split folding, the fixed-point group carries the weight function `L = ℓ` restricted to it
  (Lusztig, *Hecke algebras with unequal parameters*). So its Hecke algebra is `H(B_n)` with weights
  `L(σᵢ) = 2` and `L(τ) = 1`.
- In normalised form the eigenvalues are `{v^{L}, −v^{−L}}`. The bulk generator is ruled to have `{q, −q⁻¹}`,
  which forces `v² = q`, and then the wall has `{q^{1/2}, −q^{−1/2}}`.

So the wall's parameter is the **square root** of the bulk's.

This also fixes the level question from H9b. Lusztig's algebra is the Hecke-level object: abstract,
quadratic in each generator, with unequal parameters. It is neither H9's doubled-strand
representation, where the folded bulk generator satisfies a cubic, nor H8's equal-parameter guess.
Both arms stay recorded.

## Conditions and caveats

1. **Conditional on folding**, `conj:type-b-folding-cpt`, which is a conjecture in the corpus.
2. **The boundary shares the bulk λ** (H8 open trace).
3. **The Lusztig statement is cited, not read from a held source.** The monograph is cited in two corpus
   audits but is not in `library/`. The weight function `L = ℓ|_{W^σ}` for quasi-split folding is the
   standard example, recalled here rather than checked against the held text.
4. **Only `M_QCD`** was computed, **for the V³ special pair.** For a general photon pair `D` depends on φ at
   q₀ (H9b).

`D` is not a mass, since the trace-to-MeV map is not derived, so no CODATA comparison is made.

## Verdict

**Conditional hit for the parameter:** `Q = q^{1/2}` follows from folding plus a literature theorem,
with no number chosen. **Not a hit for a splitting.** `D` still needs a trace-to-mass map, the
photon parameters, and the folding conjecture.

## Source check (2026-11-21, after the owner chose "Get the Lusztig source")

**Not obtained.** Lusztig, *Hecke algebras with unequal parameters* (CRM Monograph Series 18; arXiv math/0208154) is not in `library/` (INDEX.md, `sections/` and `ocr/` grepped). Fetching it from arxiv.org and export.arxiv.org failed: the environment's network policy denied both hosts (CONNECT 403).

**What the held sources do confirm** (Geck, *Hecke algebras of finite type are cellular*, `library/arxiv-math-0611941v3`, §2):
- A weight function satisfies L(ww') = L(w) + L(w') whenever l(ww') = l(w) + l(w'), and L(s) = L(t) for conjugate s, t.
- The generic algebra H_A(W, L) has T_s T_w = T_{sw} + (v^{L(s)} − v^{−L(s)}) T_w when l(sw) < l(w).

So *given* L(bulk) = 2 and L(wall) = 1, the step "wall parameter = v = q^{1/2} when bulk q = v²" is confirmed from a held source.

**What remains unconfirmed:** the folding rule itself, that the weight function on the fixed-point group W^σ of a quasi-split folding is the restriction L = ℓ|_{W^σ} of the ambient length. That is Lusztig's monograph, Chapter 16 as recalled; no held source states it. The conditionality of Q = q^{1/2} is therefore unchanged on that point.

## Source check, second pass (2026-11-21): the monograph, now held

The owner uploaded the source as `uploads/0208154v2.pdf` (commit `f5d31c46b93` on `main`; not yet ingested into `library/`). Read directly:

- **§16.2 confirms the folding rule.** For a Coxeter group W̃ with diagram automorphism ι, the fixed group W is a Coxeter group on the generators w₀^I, one for each ι-orbit I with finite W̃_I, "and the restriction of l̃ to W is a weight function L" (Theorems A.8, A.9). This is the quasisplit case. For B(B_n) ⊂ B_{2n}, the middle generator is a one-element orbit with L = 1. A commuting mirror pair has w₀^I = s_{n−i}s_{n+i} with L = 2. Condition 3 above, "recalled rather than read", is **discharged**.
- **§16.7(b) fixes the normalisation, and H10 used the other one.** The quadratic relation is (b_{w₀^I} − v^{l̃(w₀^I)})(b_{w₀^I} + v^{−l̃(w₀^I)}) = 0, where v is the **ambient** indeterminate, the grading shift of the W̃ Soergel category. So the folded bulk has eigenvalues {v², −v⁻²} and the wall {v, −v⁻¹}. The ratio "wall = square root of bulk" is right. Which of the two equals the physical q is fixed by what is folded:
  - `conj:type-b-folding-cpt` folds **the canonical atomic-braid algebra H_n(q)** itself, so the ambient carries the physical q and v = q.
  - Then the folded bulk is at **q²** and the wall at **q**. H10 instead set the folded bulk equal to q (v = q^{1/2}), which is Lusztig's algebra for an ambient H_n(q^{1/2}), not for the H_n(q) the conjecture names.
- **§16.3–16.7: the folded algebra is not a subalgebra of H̃.** It is built from the ι-twisted Grothendieck group K♯ of Soergel bimodules. This is consistent with H9b, where braid-level folding gave a cubic.

| reading | bulk | wall | D(q₀), V³ | D(1) |
|---|---|---|---|---|
| A (H10 as written) | q | q^{1/2} | 0.96807142877888556063 | 1 |
| **B (Lusztig 16.7(b) with the conjecture's ambient H_n(q))** | **q²** | **q** | **0.94911520554914481986** | 1 |

Script: `h10b_lusztig_normalisation_probe.py` (exact sympy; check A(q₀²) − B(q₀) = 0).

**Caveat on B.** The H8 `D(s)` formula, the pivot K and the V³ pair were built in a bulk H₃ at parameter q. Reading B evaluates that same formula at bulk parameter q². That treats the photon words as living in the folded bulk. Whether they live there, or in the ambient H_n(q), is not fixed by the conjecture, and in the ambient there is no Hecke-level wall generator to pair them with. So B is the reading the source and conjecture support, but the photon placement is a new open input.

**Revised verdict.** The folding rule is now sourced. The wall-to-bulk ratio is derived. The absolute normalisation of H10 (A) is **not** supported. Reading B follows from the held source plus the conjecture's own wording, and gives D(q₀) = 0.949115. D is still a trace ratio, not a mass; no CODATA comparison.
