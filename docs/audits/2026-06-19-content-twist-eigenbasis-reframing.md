# The content/twist eigenbasis: the proved χ_λ(𝓑_n−𝓑_p) relations made evident (2026-06-19)

**Date:** 2026-06-19
**Compute:** [`chi_content_eigenbasis_probe.py`](../../computations/probes/chi_content_eigenbasis_probe.py)
(witness [`chi-content-eigenbasis.witness.json`](../../computations/chi-content-eigenbasis.witness.json))
**Status:** exact-symbolic re-expression of already-proved relations, TIERED. Nothing wired.
**Follows:** PR #2496 (both natural brane-tower embeddings refuted for the §4a single-x test).

Two owner asks — "keep chipping" and "review what we've proved; can we rewrite the
proved relations in a different eigenfunction basis to make them more evident?" — meet
in one object: the **Jucys–Murphy content / twist eigenbasis**.

## 1. Review — what is proved

| Relation | Status | Source |
|---|---|---|
| 3 H₃ closed forms `χ_λ(𝓑_n−𝓑_p)` | **Lean sorry-free** (`field_simp+ring`) | `chi-per-irrep-cyclotomic-closed-forms.lean` |
| conjugate symmetry `χ_(1,1,1)=χ_(3)/q⁴` | **Lean sorry-free** | same |
| vanishing at q=1 (isospin) | **Lean sorry-free** | same |
| Jacobi–Anger three-term recurrence; J/I rotation–growth split | **Lean sorry-free** | `ReebTowerJacobiAnger.lean` |
| q-Bessel contiguity ⟹ order-2 recurrence; C-finite degeneration | **Lean sorry-free** | `QBesselContiguityRecurrence.lean` |
| **ribbon / full-twist eigenvalue** `θ_λ = q^{2c(λ)}` | **Lean sorry-free** (axiom class + first-order) | `ChiralityWritheRibbon.lean` |
| bar-odd n=3 coefficients; 6.84% single-x residual | numerically validated | `qbeta-reeb-tower-jacobi-anger.witness.json` |
| single-x q-Bessel match at n=3 | **refuted** (6.84% residual) | same |
| tower extension via strand / winding embeddings | **refuted** (parity / non-convergence) | PR #2496 |

The load-bearing proved fact for the reframe is the **ribbon eigenvalue**: the full
twist `Δ² ∈ Z(H_n(q))` acts on the Wedderburn block `V_λ` as the scalar
`θ_λ = q^{2·c(λ)}`, where `c(λ) = Σ_cells content` is the Jucys–Murphy content sum.
For H₃ the three blocks carry `c ∈ {+3, 0, −3}`.

## 2. Reframe — the content/twist eigenbasis (verified exactly)

### 2.1 The eigenvalue
`θ_λ = χ_λ(Δ²)/dim_λ = q^{2c(λ)}` — verified symbolically against the proved ribbon
eigenvalue: `{q⁶, 1, q⁻⁶}` for `λ = (3), (2,1), (1,1,1)`. Centrality gives
`χ_λ(β·Δ^{2m}) = θ_λ^m · χ_λ(β)` (verified).

### 2.2 Evident form A — the framing generating function is a 3-pole rational
Summing the framing tower over twist level `m`:
$$
\sum_{m\ge 0} t^m\,\theta_\lambda^{\,m}\,\chi_\lambda \;=\; \frac{\chi_\lambda}{1 - t\,q^{2c(\lambda)}},
$$
**three simple poles at `t = q^{−2c(λ)} ∈ {q⁻⁶, 1, q⁶}` — exactly the twist
eigenvalues.** The content `c(λ)` labels the poles. (This is precisely why the
framing tower of PR #2496 *separates* the bar-odd orders by content into disjoint
clusters with a gap, rather than filling `{7,9,11}` contiguously — the three modes
sit at three different pole locations.)

### 2.3 Evident form B — the bar-odd shape depends only on |c(λ)|
In the q-integer basis (`sinh(kη) = [k]_q·sinh η`, the natural twist eigenfunctions),
the bar-odd part of each closed form is `(q−q⁻¹)·Σ_k a_k [k]_q` with

| block | content c | bar-odd q-integer shape `a_k` |
|---|---|---|
| (3) | +3 | `{3:−¼, 5:−¼}` ⟶ `−¼([3]_q+[5]_q)` |
| (1,1,1) | −3 | `{3:−¼, 5:−¼}` ⟶ `−¼([3]_q+[5]_q)` — **identical** |
| (2,1) | 0 | `{1:+½, 3:−½}` ⟶ `½([1]_q−[3]_q)` |

The two propagating modes `c = ±3` (a conjugate pair) carry the **same** bar-odd
q-integer shape; the content enters *only* as the overall `q^{2c}`-grading prefactor,
and **conjugation `λ ↔ λ'` is exactly content reflection `c → −c`**. The
self-conjugate central mode `(2,1)` (`c=0`) is the odd one out.

### 2.4 Evident form C — why the §4a single-x test was doomed
The bar-odd tower carries **two distinct `|content|` frequencies, `|c| ∈ {0, 3}`**. A
single-x Jacobi–Anger / q-Bessel fit assumes *one* mode `2 J_{2m+1}(x)`; it cannot
represent a `|content|`-graded superposition of two modes. The 6.84% single-x
over-determination residual is the residue of forcing a 2-mode object through a
1-mode template — not numerical noise, and not refutable by a better `x`.

## 3. Reading (TIERED)

1. **The eigenbasis rewrite makes the proved structure evident.** Content `c(λ)` is the
   single organizing label: it sets the closed-form denominator exponent
   (`3 − ⅔c`, proved), the twist eigenvalue (`q^{2c}`, proved), the conjugation action
   (`c → −c`), and the framing pole location (`t = q^{−2c}`). The bar-odd *shape* is
   content-blind (depends only on `|c|`); the content is pure grading.
2. **It explains the §4a failure constructively.** Not "the keystone is wrong" but "the
   single-x ansatz was the wrong template": the object is content-graded / multi-mode.
   The productive next chip is a **content-graded** special-function fit — e.g. one
   `x_{|c|}` per `|content|` class, or a theta/Macdonald object whose modes are indexed
   by content — rather than a single q-Bessel.
3. **Nothing wired; nothing newly claimed.** Every relation here is an exact symbolic
   re-expression of an already-proved H₃ identity. `c₃`/Q_β stay cal-anchored.

## 4. Discipline

- **Grounded in proof.** The organizing eigenvalue `θ_λ=q^{2c}` is Lean-proved
  (`ChiralityWritheRibbon.lean`); the closed forms it reorganizes are Lean-proved.
- **No fit, nothing wired, TIERED**; no content/`.ts`/`.lean` touched.
- **Open chip (carried forward):** a content-graded multi-mode fit at n=3 (two `x_{|c|}`),
  and whether the even-length-increment requirement from #2496 can be met by an
  embedding that keeps the *same* content-pole at each level (a same-`c` tower) rather
  than the content-separating full twist.
