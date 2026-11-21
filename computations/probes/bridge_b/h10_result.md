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
