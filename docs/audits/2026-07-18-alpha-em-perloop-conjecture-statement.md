# α_EM `1/π` wall — stated as a precise two-clause conjecture (+ literature map)

**Date:** 2026-07-18 · **Axis:** α_EM per-loop measure (the single load-bearing wall) ·
**Tier:** symbolic-exact skeleton + literature anchors; Clauses A/B **conjectural** ·
**No fit, nothing wired, `1/(8π)` stays a phase-4 identification (R1 canonical).**

Probe [`alpha_em_perloop_conjecture_statement_probe.py`](../../computations/alpha_em/alpha_em_perloop_conjecture_statement_probe.py)
→ [witness](../../computations/alpha_em/alpha-em-perloop-conjecture-statement.witness.json) (3/3).

## The conjecture (the answer to "is the wall a well-stated conjecture?" — yes, two clauses)

Post-Gauss–Bonnet form (follows main's `ba606720e` adjudication + sorry-free Lean `2b562bc7d`):

> **Conjecture (α_EM per-loop measure).** In the α_EM loop tower, the per-loop measure equals
> $$\tfrac12\cdot a_0,\qquad a_0 := \frac{1}{4\pi} = \frac{|\chi|}{2\,\mathrm{Area}},$$
> where
> **(A) — loop universality:** the per-mode weight is the universal 2d heat-kernel unit
> `a₀` (the leading Seeley–DeWitt coefficient), Gauss–Bonnet-geometrized
> (`Area = 2π|χ|` ⇒ `a₀ = |χ|/(2·Area)`); and
> **(B) — channel multiplicity:** the multiplicity is **exactly 2** — the two Hecke
> eigenvalue channels of `σᵢ` (`(σ−q)(σ+q⁻¹)=0`, the `e₊/e₋` braiding idempotents) —
> not `b₁`, not a quantum dimension.
>
> A + B ⇒ measure `= 1/(8π)` on **every** closed hyperbolic surface (genus-independent);
> the `1/(π·b₁)` form is a `g=4` coincidence.

**Honest split.** Proved: the GB identity + genus-independence (main, Lean sorry-free); the
skeleton here (GB identity ∀g with `b₁`-reading unique to `g=4`; McKean–Singer `a₁=χ/6=−1`
exactly on Bring; multiplicity discriminant `m=2`, with `m=b₁=8` giving `1/(32π)`, ~4×
excluded). **Conjectural: Clauses A and B themselves — they ARE the wall.** `m=2` is
*data-selected* (the merged `D*=8.003` forcedness); *deriving* it from the Hecke relation is
Clause B, and no computed route has done it (owner ruling `dd55a5748`: R1
convention/μ-sector stays the canonical status).

## Does closing the wall give `conj:dilogarithm-archimedean-limit`? — **No**

The implication runs the **other way**. R3's shape is: *dilog conjecture + `2πg` genus
identity ⟹ the `1/π`*. So the dilog conjecture is an **input** to one candidate route, not a
consequence of the wall. Closing the wall via A+B (the R2/GB side) would *de-load* the dilog
conjecture for α_EM — it stays open, just no longer load-bearing here. If *both* A+B and R3
were proven, their consistency would force a nontrivial identity relating the heat-kernel
unit to the Bloch–Suslin archimedean π — a valuable **cross-check**, not a proof of either.

## What the literature supplies (the "what's in lit?" map)

| piece | literature status | source |
|---|---|---|
| `a₀ = 1/(4π)` per mode (Clause A's object) | **textbook** — leading heat-kernel/Seeley–DeWitt coefficient on any surface; `Tr e^{tΔ} ~ Area/(4πt) + χ/6 + O(t)` | McKean–Singer 1967 |
| heat-trace constant term `= χ/6` | **theorem**; Bring (`χ=−6`) sits at the integer anchor `−1` exactly | McKean–Singer 1967 |
| spectral normalizations of hyperbolic surfaces are **χ-objects** | **theorem** — `det'Δ = e^{c·χ}·Z'(1)` (Selberg zeta); genus enters only via `χ`, corroborating the GB adjudication (not `b₁`) | [D'Hoker–Phong CMP 104 (1986)](https://link.springer.com/article/10.1007/BF01211063), Sarnak CMP 110 (1987); modern extension [arXiv:2512.16681](https://arxiv.org/abs/2512.16681) |
| polarized-Jacobian theta determinant (the deferred genus-4 Epstein piece of #3911) | **established framework** — Faltings' `δ`-invariant via theta integrals; `δ = −6·D_Ar + a(g)` with `D_Ar` the regularized `det'Δ`; Bost's formula | [Wilms, arXiv:1605.00847](https://arxiv.org/abs/1605.00847); [Faltings-δ degeneration](https://arxiv.org/pdf/2101.04024) |
| the archimedean π of R3 | **established math** for the regulator objects (Bloch–Wigner `D(z)`, Borel regulator); the **QOU identification** (`conj:dilogarithm-archimedean-limit`) is what's open | Zagier, dilogarithm surveys |
| Clause B (`m=2` from the Hecke relation) | **not in the literature** — QOU-specific; the channel-split structure is #3810's | — |

Net: the literature supplies every *object* the conjecture mentions and independently
corroborates the χ-scaling; what it cannot supply is the two QOU-specific identifications —
Clause A ("`a₀` **is** the per-loop weight of *this* tower") and Clause B ("the multiplicity
**is** the Hecke channel count") — which is exactly why the wall is a conjecture about the
framework, not about spectral geometry.

## Clause-B sharpening (same-day follow-on): the ½ reduces to ONE correspondence statement

Probe [`alpha_em_clauseB_channel_sharpening_probe.py`](../../computations/alpha_em/alpha_em_clauseB_channel_sharpening_probe.py)
→ [witness](../../computations/alpha_em/alpha-em-clauseB-channel-sharpening.witness.json) (3/3),
building on the lever-2 two-channel factorization (`3f4ebbc1f`, derived):

- **(F1) The channel COUNT 2 is derived, not conjectural.** The Hecke relation is
  *quadratic*, so `H₂(q)` splits into exactly the two idempotent channels
  `e₊ = (σ+q⁻¹)/[2]_q`, `e₋ = (q−σ)/[2]_q` (`e₊+e₋=1`, `e₊e₋=0`, `σ = q·e₊ − q⁻¹·e₋` —
  exact mod the relation).
- **(F2) The ½ is NOT an equal channel *weight* — excluded.** The resummed tower's
  partial-fraction weights are `w₊ = q²/(q²−1)`, `w₋ = −1/(q²−1)`: they sum to 1 but equal
  `(½,½)` **iff `q² = −1`** (never at real q); at the substrate `q₀` they are
  `(5.31, −4.31)`. Any route deriving the ½ as "equal weights at `q₀`" is dead (scope-(a)).
- **(F3) Where the ½ actually lives.** The tower's 1-loop coefficient is `−[2]_q·x`
  **exactly** — the q-dependence sits entirely in `[2]_q`, the measure `x` is
  q-independent, and matching the working `α[2]_q/(8π)` term forces `x = α/(8π)` with *no*
  `q→1` limit. The ½ is then the **classical-limit normalization**: at `q=1` the 1-loop
  total is `2x`, and `x = α/(8π)` **iff** the `q→1` one-loop equals the universal
  heat-kernel unit `α·a₀ = α/(4π)`.

**Net: all of Clause B collapses to the single correspondence statement — "the `q→1`
one-loop total of the tower equals `a₀·α`."** Channel count: derived. Weights reading:
excluded. That one normalization (which is Clause A evaluated at 1-loop) is the entire
remaining wall — the conjecture is effectively **one clause** now: the tower's classical
limit is normalized by the universal heat-kernel unit.

## §6 reconciliation with #3920 (landed on main during this PR): three readings of the "2"

#3920 (`484c86462`) adjudicated the real-vs-holomorphic count sub-question — the per-loop
count is the **real** `b₁ = 2g` (the photon is a real U(1) 1-form; real Hodge Laplacian),
with the `2` in `8π = 2·(4π)` read as the **real-vs-complex Hodge doubling**
`H¹(M,ℝ)⊗ℂ = H^{1,0}⊕H^{0,1}`. This does **not** conflict with F1–F3 (exact algebra,
reading-independent) but it does put **three readings of the "2"** on main simultaneously:

| reading | the "2" | genus scaling | source |
|---|---|---|---|
| GB | `|χ|/(4·Area)` — no `2` per se | **independent** | `ba606720e` + Lean |
| Hodge doubling | `b₁ = 2·g` (real vs holomorphic) | `π·b₁ = 2πg` — **dependent** | #3920 |
| Hecke channels | `e₊/e₋` (quadratic Hecke relation) | independent (with Clause A) | lever-2 + this PR |

The GB and Hodge readings **disagree at g≠4** (the GB audit explicitly adjudicated
genus-independence; `π·b₁` scales) — flagged, not resolved here. **Natural unification
hypothesis (named, not derived):** the Hecke `2` and the Hodge `2` are the *same*
conjugation doubling — the bar involution `q ↔ q⁻¹` swaps `e₊/e₋` exactly as complex
conjugation swaps `H^{1,0}/H^{0,1}`, so a τ-functor correspondence would identify the two
channel pairs and reduce all three readings to one object (with the GB form as its
genus-independent evaluation). Deriving that identification **is** (a form of) the
remaining correspondence statement above. What F2/F3 contribute to *any* reading: the "2"
cannot be resummation weights (excluded at real q), and the per-loop parameter is
q-independent (`−[2]_q·x` exact), so every reading must place its "2" in the
classical-limit normalization, not in q-dependent weights.

## Scope guard (STRICT)

States and machine-checks the skeleton; **derives neither clause**; no fit; nothing wired;
`1/(8π)` stays phase-4 with R1 as the canonical status. Coordinates with (does not duplicate):
main's GB probe/Lean (`ba606720e`/`2b562bc7d`), #3810 (owns the ½ channel split), the
reconciliation ruling (`dd55a5748`).

## Cross-references

- GB adjudication: `2026-07-18-alpha-em-gauss-bonnet-measure.md` (main)
- π-origin ruling: `2026-07-18-alpha-em-pi-origin-three-reading-reconciliation.md` (main)
- count leg (derived): `2026-07-18-alpha-em-nonD-index-route.md` (main)
- magnitude machinery (deferred genus-4): `2026-07-18-bring-polarized-epstein-determinant.md` (#3911, merged)
