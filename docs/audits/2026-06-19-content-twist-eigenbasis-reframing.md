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

### 2.5 Chip tried — even a single content mode is not single-x q-Bessel
**Compute:** [`chi_content_single_mode_probe.py`](../../computations/probes/chi_content_single_mode_probe.py).
The natural follow-up to §2.4 is to *isolate* one content mode and ask whether it
alone is a clean single-x q-Bessel. The only H₃ block with internal tower structure
is the `c=0` mode `(2,1)` (dim 2); the dim-1 blocks `(3),(1,1,1)` give frozen
two-order monomials under the winding `β^k`. Its bar-odd coefficients are rational,
but its single-x over-determination residual does **not** shrink:

| k | #odd orders | single-x residual (max over ≥5) |
|---|---|---|
| 3 | 12 | 480% |
| 5 | 24 | 606% |
| 7 | 35 | 186% |
| 9 | 46 | 240% |

So the §4a single-x failure is **not merely multi-mode mixing**: even one isolated
content mode is not single-x q-Bessel under the winding tower. The discrete
strand / winding / framing tower variables tried so far are not the q-Bessel
contraction parameter (or the bar-odd object is not single-x q-Bessel at all).

## 3. Reading (TIERED)

1. **The eigenbasis rewrite makes the proved structure evident.** Content `c(λ)` is the
   single organizing label: it sets the closed-form denominator exponent
   (`3 − ⅔c`, proved), the twist eigenvalue (`q^{2c}`, proved), the conjugation action
   (`c → −c`), and the framing pole location (`t = q^{−2c}`). The bar-odd *shape* is
   content-blind (depends only on `|c|`); the content is pure grading.
2. **It reframes the §4a failure — and the failure is deeper than mode-mixing.** The
   eigenbasis first suggested "the single-x ansatz mixes content modes" (§2.4); but
   isolating one content mode (§2.5) shows it *too* fails single-x (480–606% residual).
   So across every tower direction now tried — strand and winding (PR #2496), framing
   (§2.2), and single-content-winding (§2.5) — the bar-odd object is **not a single-x
   q-Bessel**. The honest status: the n=3 6.84% near-match does not extend; the discrete
   tower variables are not the q-Bessel contraction parameter. A genuine identification,
   if one exists, must come from the *continuous* `E_q(2)` contraction limit, not these
   discrete braid towers.
3. **Nothing wired; nothing newly claimed.** Every relation here is an exact symbolic
   re-expression of an already-proved H₃ identity. `c₃`/Q_β stay cal-anchored.

## 4. Gaps the eigenbasis closes (owner question: "can we prove gaps with this?")

Yes — for the **structural** gaps that #2496 and §2 above established only *numerically*.
Because the organizing eigenvalue `θ_λ=q^{2c}` is **Lean-proved**, the eigenbasis
promotes three verified-only observations to rigorous, Lean-formalizable lemmas
(all verified exact-symbolic at n=3,6[,9]:
[`eigenbasis_structural_lemmas_probe.py`](../../computations/probes/eigenbasis_structural_lemmas_probe.py),
witness [`eigenbasis-structural-lemmas.witness.json`](../../computations/eigenbasis-structural-lemmas.witness.json)):

- **L1 — order-parity = word-length parity.** `χ_λ(β)` has all Laurent exponents
  `≡ L (mod 2)`, `L` = number of typed crossings. *Proof:* every Hoefsmit crossing
  factor (`σ_i`; `σ_i − h·I`, `h=q−q⁻¹`) has odd Laurent degree, so a product of `L`
  of them has degree `≡ L (mod 2)`, preserved by the trace. ∎ This makes the **#2496
  parity obstruction a theorem**: the nucleon word has odd length 11, so any
  integer-multiple tower (`11·index`) alternates parity.
- **L2 — bar-involution ↔ conjugation duality.** `χ_λ(𝓑_n−𝓑_p)(1/q) = (−1)^L·χ_{λ'}(q)`
  for every `λ ⊢ n` (verified: sign uniform `−1` at n=3, `+1` at n=6 = `(−1)^A=(−1)^L`,
  tying the sign to L1). *Proof skeleton:* the Hecke bar involution `q ↦ q⁻¹` swaps the
  seminormal eigenvalues `q ↔ −q⁻¹`, i.e. the `V_λ ≅ V_{λ'}` intertwiner — the bar
  involution **is** content reflection `c(λ') = −c(λ)`. ∎ Generalizes the H₃-only proved
  case `χ_(1,1,1)=χ_(3)/q⁴` and **proves the conjugation invariant** verified this session.
- **L3 — framing generating function.** `Σ_m t^m χ_λ(β·Δ^{2m}) = χ_λ(β)/(1−t·q^{2c(λ)})`,
  a one-line corollary of centrality + the proved `θ_λ=q^{2c}`.

**What it does NOT close — the per-isotope Δ_λ binding gate.** Content-statistic ansätze
for `Δ_λ` are already refuted (GAP-A-3 / Kashiwara `c(λ)`); a content-based `Δ_λ` would
be a *seventh fitted ansatz* and is out of scope. The eigenbasis **reorganizes proved
structure** — it does not manufacture a binding closure. Stating this boundary is part of
the answer.

**Lean follow-up:** formalize L1, L2 in `QOU/BraidKnot` and L3 as a corollary of
`RibbonTwistEigenvalue`. Blocked this session only by the firewalled Lean toolchain
(`release.lean-lang.org`); the proofs above are complete modulo transcription.

## 5. Discipline

- **Grounded in proof.** The organizing eigenvalue `θ_λ=q^{2c}` is Lean-proved
  (`ChiralityWritheRibbon.lean`); the closed forms it reorganizes are Lean-proved.
- **No fit, nothing wired, TIERED**; no content/`.ts`/`.lean` touched.
- **Open chip (carried forward):** with every *discrete* braid-tower direction now
  refuted for single-x q-Bessel (strand, winding, framing, single-content), the live
  lead is the **continuous `E_q(2)` contraction** the q-Bessel actually comes from —
  i.e. test whether the bar-odd matrix coefficient matches a Hahn–Exton q-Bessel
  `J_ν^{(HE)}(·;q)` (the genuine q-deformed object), rather than the ordinary `J_ν`
  of the Jacobi–Anger backbone, before attempting any `lim spectrum = q-Bessel zeros`
  Lean.
