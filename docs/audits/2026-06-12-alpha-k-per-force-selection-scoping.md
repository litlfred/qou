# α_K per-force selection — scoping audit (the "other 5" question)

**Date:** 2026-06-12. **Branch:** `claude/wizardly-ride-zml15z`.
**Owner ask:** continue the α_{basis-knot} program step 3 — per-force
coupling values for the basis knots beyond α_EM ("the FSC was related
to the trivial/unknot via the 6-knot-operator cohomological basis;
what are the other 5?").

## 1. What is already established (corpus, do not re-derive)

| piece | where | status |
|---|---|---|
| The 7 force operators: identity (**unknot**, free propagation) + 6 cohomological basis knots | [`cohomological-embedding.md`](../../content/quantum-observable-universe/brings-surface/cohomological-embedding.md) consequence 3 | established |
| Per-operator interaction roles: T_{2,3} mass/EM (trefoil), T_{2,5} 2nd gen, T_{2,7} 3rd gen, T_{2,9} strong, T_{3,4} Hopf-squared/top, T_{3,5} weak | same block + [`force-knot-identification.md`](../../content/quantum-observable-universe/predicted-spectra/force-knot-identification.md) | established |
| EM is **not a knot** — it is the involutive structure; its coupling slot is the unique 2-strand singlet V₋ ≅ **1** (the unknot channel) | [`em-spectral-completeness.md`](../../content/quantum-observable-universe/mass-theory/em-spectral-completeness.md), [`gauge-coupling-uniqueness.md`](../../content/quantum-observable-universe/predicted-spectra/gauge-coupling-uniqueness.md) | theorem |
| α_EM value: 1/α_EM = q[9]_q[10]_q from the genus-4 carrier pair (T_{2,9}, T_{3,5}) | `prop:alpha-em-categorical-trace-ratio`; assembled end-to-end in [`alpha_k_per_force_assembly.py`](../../folio-assistant/computations/alpha_k_per_force_assembly.py) (PR #2107) | established |
| δ_q(T_{m,k}) = h[(m−1)k]_q (writhe rule) | `prop:torus-knot-delta-q-writhe` (PR #2107), sorry-free Lean | proved |
| Intertwining channel λ(T_{m,k}) = (m, 1^{n−m}) | [`force-carrier-intertwining-correspondence.md`](../../content/quantum-observable-universe/mass-theory/force-carrier-intertwining-correspondence.md) | conditional on `conj:e-hartree-categorical-derivation` |

## 2. Structural stratification of the 6 basis knots (derived, exact)

Seifert genus g = (m−1)(k−1)/2 stratifies the basis:

| g | saturating set (m−1)(k−1) = 2g | reading |
|---|---|---|
| 1 | {T_{2,3}} (unique) | EM particle (trefoil) |
| 2 | {T_{2,5}} (unique) | 2nd generation |
| 3 | {T_{2,7}, T_{3,4}} (pair) | 3rd generation + Hopf-squared/top |
| 4 | {T_{2,9}, T_{3,5}} (pair) | **the force-carrier pair** (strong, weak) |

The basis = all coprime torus knots with g ≤ 4 = g(Σ₄); each stratum's
membership is forced by the diophantine equation (integer arithmetic,
trivially Lean-able). The two pairs (g = 3, 4) are transpose-partition
pairs under the intertwining map (m = 2 ↔ (2,1^{n−2}); m = 3 ↔
(3,1^{n−3})).

## 3. The selection question and the even-strand singlet ladder (new)

The per-force coupling **values** need a selection rule: which categorical
slot carries each force's coupling. The established EM case: the 2-strand
sector has **exactly one** braid-invariant scalar coupling A⊗A → **1**
(`thm:em-spectral-completeness`, rank-2 e₊/e₋ split; V₋ ≅ **1**).

New probe [`alpha_k_four_strand_singlet_selection.py`](../../folio-assistant/computations/alpha_k_four_strand_singlet_selection.py)
(witness 5/5) derives the full ladder, exact and pre-archimedean:

$$\dim\operatorname{Hom}(\mathbf{1}, A^{\otimes n}) = \begin{cases} 0 & n \text{ odd}\\ \mathrm{Catalan}(n/2) & n \text{ even}\end{cases} = 1, 2, 5, 14 \text{ at } n = 2, 4, 6, 8.$$

- **n = 2 → 1 slot**: the EM coupling (theorem; the trivial/unknot channel).
- **n = 4 → 2 slots**: exactly as many independent scalar couplings as
  remaining knot-mediated short-range forces (strong T_{2,9}, weak
  T_{3,5}). The slot space carries the forced TL Gram matrix
  [[δ², δ], [δ, δ²]] (δ = [2]_q), eigenvalues δ(δ±1) on the
  symmetric / antisymmetric (bar-odd) combinations — the 4-strand
  analogue of the e₊/e₋ split.
- **n = 6 → 5 slots**: fiber degree ≥ 3 does not embed on Σ₄
  (`prop:cohomological-embedding` (ii)), consistent with no further
  fundamental forces.

**Tier: structural observation / selection-rule candidate.** The count
match (2 slots ↔ 2 forces) is forced, not fitted; the **identification**
(which slot = which force, and the resulting α_s/α_W values via the
archimedean trace-ratio on the slot space) is open and gated.

## 3b. The conditional selection rule (owner-directed continuation, same day)

Probe [`alpha_k_selection_rule_conditional.py`](../../folio-assistant/computations/alpha_k_selection_rule_conditional.py)
(witness 6/6) derives the rule exactly, conditional on
`conj:e-hartree-categorical-derivation`:

| force | block | mediator | decoration | coupling |
|---|---|---|---|---|
| EM (universal) | **(2,2)** — the unique self-transpose (scalar, antipode-closed) partition of 4; Schur–Weyl dual of the 2-dim slot space; dim_q = [4]_q/[2]_q = q²+q⁻² | the transpose **pair** (T_{2,9}, T_{3,5}) — the minimal insertion reaching the self-dual block | h[9]_q · h[10]_q | 1/α_EM = q[9]_q[10]_q (established) |
| strong (short-range) | (2,1,1) | T_{2,9} alone | h[9]_q | q^{1/2}[9]_q (split = convention) |
| weak (short-range) | (3,1) | T_{3,5} alone | h[10]_q | q^{1/2}[10]_q (split = convention) |

Exact spine (all symbolic, witness-asserted): (2,2) is the **unique**
self-transpose partition of 4; ((3,1), (2,1,1)) is the **unique**
transpose-dual pair among intertwining channels; both carrier channels
have equal dim_q = [3]_q (Frobenius self-duality of the pair);
single-carrier insertions cannot reach the self-dual block (the
round-17 exact (2,2)-zero is the computational shadow). Short-range =
non-self-dual channel (structural reading of confinement/massive
mediation, conditional).

**Invariant product identity (exact in R, derived not fitted):**

$$\bigl(q^{1/2}[9]_q\bigr)\bigl(q^{1/2}[10]_q\bigr) = q\,[9]_q\,[10]_q \quad\Longrightarrow\quad \alpha_s \cdot \alpha_W = \alpha_{EM}.$$

The product is the invariant; the symmetric q^{1/2} split per channel is
**convention** pending the pole-order derivation
(`prop:alpha-em-shift-multiplicative-chain` primitive). Critical-distance
note: the identity is the established α_EM formula re-bracketed — its new
falsifiable content arrives only with an independent archimedean
derivation for non-scalar channels; until then no comparison to measured
running couplings (scheme dependence makes any match-claim fishing).

## 4. Anti-fishing boundary (what was deliberately NOT done)

- No per-knot or per-pair coupling formulas were enumerated against
  measured α_s/α_W (multiple-comparison fishing; forbidden per
  `local/production-vs-exploratory-discipline` and the step-3 scope
  note in `alpha_k_per_force_assembly.py`).
- The g = 3 pair (T_{2,7}, T_{3,4}) admits the same h²/(q·δ_q·δ_q)
  template as the g = 4 pair purely formally; evaluating it and
  comparing to any measured coupling would be fishing — recorded here
  only as a *formal degree of freedom the selection rule must either
  force or exclude*.

## 5. Closure path (next steps, in order)

1. **Formalize the n = 4 spectral completeness** (the gating lemma):
   End(A⊗⁴) Wedderburn structure + the 2-dim singlet multiplicity
   space, generic ring, Lean (`§7c` generic-R discipline; integer
   CG walk is exact).
2. **The archimedean trace-ratio on the slot space** — the analogue of
   tr_τ(e₋) — conditional on `conj:e-hartree-categorical-derivation`
   (round-18 state: the χ_{(3,1)}·χ_{(2,1,1)} symbolic-q identity is
   the outstanding check; see the conjecture block's round log).
3. Only then: per-force values α_s, α_W with tiered reporting.

## Cross-refs

- `docs/workplans/2026-06-10-alpha-basis-knot-couplings.md` (the program;
  status table refreshed in PR #2205)
- `docs/coordination/alpha-em.md` (master ledger)
- PRs #2100 / #2107 / #2114 (merged program steps), #1495 (open n=2 RT
  track), #1523 (open J₂(unknot) categorical ID)
