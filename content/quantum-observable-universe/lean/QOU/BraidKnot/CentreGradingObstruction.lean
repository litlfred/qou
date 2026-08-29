import QOU.BraidKnot.TwoFiltrationBridge

/-!
# QOU.BraidKnot.CentreGradingObstruction — why no *shift* rescues the bridge

Bean `wpdb` / `qou-wjbd`. Six sites read

    Z^(k)(A) = span{ e_λ : gbDepth λ = k }

off `prop:curvature-rank-gb-stratification`, which stratifies **words**. The
audits
[`2026-08-16-word-depth-vs-partition-depth-bridge-is-unstated`](../../../../../docs/audits/2026-08-16-word-depth-vs-partition-depth-bridge-is-unstated.md)
and
[`2026-08-16-three-gb-filtrations-one-name`](../../../../../docs/audits/2026-08-16-three-gb-filtrations-one-name.md)
established that `J^•` names three inequivalent objects, and excluded two of
them. The third — the **Coxeter-length** filtration
`F_ℓ = span{T_w : ℓ(w) ≤ ℓ}` of `alg:mba-step07-gb-filtration` — survived, with
a dimension count that failed only at `n ≤ 3`.

This file supplies the two pieces that close it **for every `n`**, and it does
so in a form no re-indexing can dodge. The obvious repair to an off-by-one
index mismatch is a shift; §2 shows a shift cannot help, because the obstruction
is a *gap*, and a shift is an order isomorphism.

## What is and is not claimed

**Not claimed:** that the identification is false in the abstract. A filtration
inducing the `gbDepth` grading on the centre trivially exists — filter by the
Wedderburn blocks themselves. What is excluded is that any of the three things
the corpus calls `J^•` is such a filtration.

**Not claimed:** that any mass or binding result is wrong. `J^•` enters the
downstream chain as an *indexing*, not as a magnitude.

The algebra-side inputs to §3 (`dim(Z ∩ F_0) = 1`, `dim(Z ∩ F_1) = 1` for
`n ≥ 3`, and the full graded sequence at `n = 4`) are **hypotheses** here, not
Lean-proved: `H_n(q)` and its centre are not Lean objects in this tree. They are
established by exact computation in
[`docs/audits/scripts/centre_length_filtration_vs_gbdepth.py`](../../../../../docs/audits/scripts/centre_length_filtration_vs_gbdepth.py)
(`Fraction` over `ℚ`, `𝔽_p`, and symbolic `ℚ(q)` — three independent exact
backends agreeing), and `dim(Z ∩ F_1) = 1` additionally has a two-line proof
recorded in that script's docstring. Carrying them as hypotheses rather than
asserting them is the §3b-cond discipline: the theorem below *derives* the
exclusion from them.
-/

namespace QOU.BraidKnot

open QOU.MathlibExt.YoungDiagramCells (rowLen0_pos colLen0_pos)

/-! ### 1. The partition grading never occupies degree `0` -/

/-- **`gbDepth` is positive on every nonempty diagram.**

The corner hook `λ₁ + λ'₁ - 1` is at least `1 + 1 - 1`. Small, but it is the
whole of the degree-`0` obstruction: whatever filtration `J^•` turns out to be,
its induced grading on `Z(H_n(q))` has `Z^(0) ∋ 1 ≠ 0`, because the unit is
central and lies in filtration degree `0` in *any* algebra filtration. The
partition side's degree-`0` stratum, by contrast, is empty — so the two cannot
agree at `k = 0`, for any `n ≥ 1` and any candidate `J^•`.

This is why the repair has to be a shift, and §2 is why a shift does not work. -/
theorem gbDepth_pos (μ : YoungDiagram) (h : μ.cells.Nonempty) : 0 < gbDepth μ := by
  rw [gbDepth_eq_corner μ h]
  have hr := rowLen0_pos (μ := μ) h
  have hc := colLen0_pos (μ := μ) h
  omega

/-- The degree-`0` partition stratum is empty: no nonempty diagram has depth `0`. -/
theorem gbDepth_ne_zero (μ : YoungDiagram) (h : μ.cells.Nonempty) : gbDepth μ ≠ 0 :=
  (gbDepth_pos μ h).ne'

/-! ### 2. A shift cannot create or remove an interior gap

The two sides are compared as **multiplicity functions** `ℕ → ℕ`: `N k` is the
number of partitions of depth `k`, and `W k` is `dim Z^(k)`. The identification
asserts `W = N`; the natural repair asserts `W k = N (k + c)` for some shift `c`.

The obstruction is that `N` is *gap-free* — its support is an interval, proved
in the probe's Lemma 3 and verified to `n = 40` — while `W` has a hole at
degree `1`, between two nonzero values. A shift is an order isomorphism of `ℕ`,
so it transports gap-freeness; hence no `c` exists.
-/

/-- **A shift of a gap-free multiplicity function is gap-free, so it cannot be
a function with an interior hole.**

`hgapfree` says `N`'s support is order-convex: nothing vanishes strictly between
two nonzero values. `hshift` is the candidate re-indexing. The remaining three
hypotheses describe the word side: nonzero at degree `0` (the unit is central
and has filtration degree `0`), **zero at degree `1`**, and nonzero somewhere
above (the centre has dimension `p(n) ≥ 2`, so it is not exhausted by the unit).

No such `c` exists. The proof is three lines and uses every hypothesis. -/
theorem shift_cannot_fill_a_gap
    (N W : ℕ → ℕ) (c : ℕ)
    (hgapfree : ∀ a b k : ℕ, N a ≠ 0 → N b ≠ 0 → a ≤ k → k ≤ b → N k ≠ 0)
    (hshift : ∀ k : ℕ, W k = N (k + c))
    (hzero : W 0 ≠ 0) (hone : W 1 = 0)
    (hhigh : ∃ m : ℕ, 1 < m ∧ W m ≠ 0) : False := by
  obtain ⟨m, hm, hWm⟩ := hhigh
  have hNc : N (0 + c) ≠ 0 := by rw [← hshift 0]; exact hzero
  have hNm : N (m + c) ≠ 0 := by rw [← hshift m]; exact hWm
  have h1 : N (1 + c) ≠ 0 := hgapfree (0 + c) (m + c) (1 + c) hNc hNm (by omega) (by omega)
  exact h1 (by rw [← hshift 1]; exact hone)

/-! ### 3. The Coxeter-length reading, excluded at `n = 4`

The measured word side at `n = 4` (exact, three backends, `q` symbolic and
specialised):

    dim(Z ∩ F_k) = [1, 1, 1, 1, 2, 4, 5]     k = 0 … 6 = ℓ(w₀)
    dim Z^(k)    = [1, 0, 0, 0, 1, 2, 1]

against the partition side `gbDepth [2,2] = 3`, `gbDepth λ = 4` for the four
hooks, i.e. `N 3 = 1`, `N 4 = 4`, `N k = 0` otherwise — which is gap-free.

`p4` and `p22` are the diagrams already in `TwoFiltrationBridge`; `gbDepth_p4`
and `gbDepth_p22` are what makes `N` the function below rather than a guess. -/

/-- The `n = 4` partition-depth multiplicity function, read off `gbDepth_p22`
(`[2,2] ↦ 3`) and `gbDepth_p4` (`[4] ↦ 4`, shared by all four hooks). -/
def N4 : ℕ → ℕ := fun k => if k = 3 then 1 else if k = 4 then 4 else 0

/-- `N4` is gap-free: its support `{3, 4}` is an interval. -/
theorem N4_gapfree : ∀ a b k : ℕ, N4 a ≠ 0 → N4 b ≠ 0 → a ≤ k → k ≤ b → N4 k ≠ 0 := by
  intro a b k ha hb hak hkb
  unfold N4 at *
  split_ifs at ha hb ⊢ with h1 h2 <;> omega

/-- **No shift of the `n = 4` partition grading is the centre's Coxeter-length
grading.**

The word side enters as hypotheses — the exact computed sequence
`[1, 0, 0, 0, 1, 2, 1]`, stated pointwise for the three degrees the argument
uses. Everything else is derived.

**Not vacuous.** Concluding `False` from a hypothesis set is a refutation, not a
tautology, precisely because each part is separately satisfiable: `W = ![1,0,0,0,1,2,1]`
is realised (it is the measured graded sequence), and `hshift` is realised by
`W = fun k => N4 (k + c)` for any `c`. What is impossible is their conjunction —
which is the statement that the measured centre grading is a re-indexing of the
partition grading. All three `W`-hypotheses are used in the proof term. -/
theorem coxeter_reading_excluded_at_four
    (W : ℕ → ℕ) (c : ℕ)
    (hW0 : W 0 = 1) (hW1 : W 1 = 0) (hW5 : W 5 = 2)
    (hshift : ∀ k : ℕ, W k = N4 (k + c)) : False :=
  shift_cannot_fill_a_gap N4 W c N4_gapfree hshift
    (by rw [hW0]; exact one_ne_zero) hW1 ⟨5, by omega, by rw [hW5]; exact two_ne_zero⟩

end QOU.BraidKnot
