import HeckeTemperleyLieb.QHeatKernelRate

/-!
# The mode set `Λ` of the q-heat kernel: rates are blind to conjugation

Bean `qou-8vt2` (define `ϑ_K`), fibre route, step after `QHeatKernelRate`.

`prop:q-beta-c-k-recursion-from-habiro-q-difference` writes the fibre Habiro element as the
heat-kernel trace over the Hecke modules,

    Z_q(t) = Σ_{λ ∈ Λ} d_λ(q) · exp_q(−μ_λ(q)·t),

and says its q-difference equation has depth `|Λ|`. Modes that share a rate merge into one
exponential, so the depth is the number of **distinct** rates, not the number of
irreducibles.

## What is proved here (sorry-free)

* `diagramBracketSqSum_transpose`: `g_{λᵀ}(q) = g_λ(q)` for every Young diagram. Transposing
  negates every content, and each bracket `(q^c − q^{−c})²` is even in `c`.
* `cellBracketSqSum_eq_of_shape_transpose`: so two partitions whose shapes are transposes of each other
  have the same rate `μ_λ`.

Hence, for `Λ = Irr H_n(q)` (all `λ ⊢ n`, the reading of "trace over the Hecke modules"),
the depth is at most the number of partitions of `n` up to conjugation.

## What the companion probe adds (exact combinatorics, not Lean)

`computations/probes/qbeta_thetak_mode_set_depth_probe.py`: since
`g_λ = Σ_c (q^{2c} + q^{−2c} − 2)`, the rate determines the multiset `{|c| : c ∈ λ}`. For `n ≤ 7`
that multiset separates conjugation classes exactly, so the bound is attained:
`|Λ| = 1, 1, 2, 3, 4, 6, 8` for `n = 1, …, 7`. The first coincidence of non-conjugate rates
is at `n = 8`, where three conjugation classes, `{(4,4), (2⁴)}`, `{(4,2,2), (3,3,1,1)}` and
`{(4,3,1), (3,2,2,1)}`, share one rate, so `|Λ| = 10 < 12`.

At `n = 3` that gives depth 2, the same depth as the corpus's depth-2 toy kernel
(recorded in `qou-8vt2` as "underdetermined from seeds alone"). That is a match of depth only,
not of coefficients.

## Not claimed

That `Λ` *is* all of `Irr H_n(q)` is the reading of the proposition's phrase. It is not
derived here. Nothing is evaluated at any anchor. `ϑ_K` is still undefined.
-/

namespace QOU.SchurWeyl.HeatKernelRate

open QOU.SchurWeyl

variable {K : Type*} [Field K]

/-- The per-mode bracket on a Young diagram, `g_μ(q) = Σ_{c∈μ} (q^c − q^{−c})²`. -/
noncomputable def diagramBracketSqSum (μ : YoungDiagram) (q : K) : K :=
  ∑ c ∈ μ.cells, (q ^ (cellContent c) - q ^ (-(cellContent c))) ^ 2

theorem cellBracketSqSum_eq_diagram {N : ℕ} (lam : Partition N) (q : K) :
    cellBracketSqSum lam q = diagramBracketSqSum (shape lam) q := rfl

/-- Transposing a cell negates its content. -/
theorem cellContent_swap (c : ℕ × ℕ) : cellContent c.swap = -cellContent c := by
  simp [cellContent]

/-- **The rate is blind to conjugation**: `g_{μᵀ}(q) = g_μ(q)`. -/
theorem diagramBracketSqSum_transpose (μ : YoungDiagram) (q : K) :
    diagramBracketSqSum μ.transpose q = diagramBracketSqSum μ q := by
  unfold diagramBracketSqSum
  rw [show μ.transpose.cells = μ.cells.map (Equiv.prodComm ℕ ℕ).toEmbedding from rfl,
    Finset.sum_map]
  refine Finset.sum_congr rfl (fun c _ => ?_)
  show (q ^ cellContent c.swap - q ^ (-cellContent c.swap)) ^ 2 = _
  rw [cellContent_swap, neg_neg]
  ring

/-- Two partitions with transposed shapes have the same bracket, hence the same rate. -/
theorem cellBracketSqSum_eq_of_shape_transpose {N : ℕ} (lam lam' : Partition N)
    (h : shape lam' = (shape lam).transpose) (q : K) :
    cellBracketSqSum lam' q = cellBracketSqSum lam q := by
  rw [cellBracketSqSum_eq_diagram, cellBracketSqSum_eq_diagram, h,
    diagramBracketSqSum_transpose]

theorem heatRate_eq_of_shape_transpose {N : ℕ} (lam lam' : Partition N)
    (h : shape lam' = (shape lam).transpose) (t : K) :
    heatRate t lam' = heatRate t lam := by
  unfold heatRate
  rw [cellBracketSqSum_eq_of_shape_transpose lam lam' h]

end QOU.SchurWeyl.HeatKernelRate
