import QOU.Machinery.MarkovTraceH4Gram7

/-!
# QOU.Machinery.H4 — Gram symmetry and trace cyclicity

Closes `gram_symm` from the 576 computed Gram entries, hence `trM_cyclic`.
-/

namespace QOU.Machinery.H4

variable {R : Type*} [CommRing R]

/-! ## Gram symmetry — design note

`gram_symm` is `G_{i,j} = G_{j,i}`, i.e. `tr_M(b_i·b_j) = tr_M(b_j·b_i)` for the
24 NF basis elements — the residual finite (24² = 576, 276 nontrivial) content of
trace cyclicity after the sorry-free reduction `trM_cyclic_of_gram_symm`.

Machine-validated in the compute infra (`hecke_regular_nf_table.py`,
`self_validate`: cyclicity on all sampled pairs).

**CLOSEABLE (not whnf-blocked — correction 2026-07-19).** Each `G_{i,j}` is
`tr_M` of a depth-≤6 `mulσ` composition applied to a **basis** vector, and the
generator action on a basis vector is sparse (`mulσ_k(e_i)` is `e_{π(i)}` or
`e_a + h·e_b`). Chaining single-generator steps with explicit intermediate
vectors — never unfolding the whole tower at once — each step is depth-1 and the
mostly-zero entries resolve fast, so the `whnf` wall is never hit.

**CLOSED — and committed (correction 2026-08-09).** The paragraph that stood
here said the closure was *not* committed and that `gram_symm` "stays a cited
`sorry`", on the grounds that ~6.3k generated lines were too heavy a permanent
build cost. That had stopped being true: the 576 entries were in the tree and
`gram_symm` was proved from them. Nobody noticed because the module was one of
the 785 outside the `lake build` import closure (bean qou-rc7b) — it had never
compiled, so the contradiction between this note and the code below it was
invisible.

The build cost the note worried about is real, and it is what the split
addresses. Held as one module the closure needs **~15 GB and over an hour** —
measured, not estimated; peak memory grows linearly in the number of entries at
roughly 28 MB each (bean qou-8hjy). The 576 entries now live in
`MarkovTraceH4Gram0…7`, 72 apiece, **each importing the previous** so the chain
is built serially and peak elaboration memory stays bounded no matter how many
cores Lake has. Pure refactor: same theorems, same proofs, same namespace.

The lighter permanent closure remains the abstract Ocneanu-induction lemma on
main's `MarkovStabilization` (bean `qou-0vsu`), which discharges cyclicity for
every `n` at once without the 24² brute force. When that lands, this whole
generated chain can be deleted.

Ref: [manuscript] §mass-theory (H₄ Markov trace); compute
`hecke_regular_nf_table.py` `self_validate`.
-/
/-! `fin_cases` produces `Fin` indices in `Fin.mk` form (`⟨3, ⋯⟩`) while the
generated `gramval_i_j` are stated with `OfNat` numerals (`(3 : Fin 24)`), so the
rewrites do not fire without this bridge. Each is `rfl` — `(3 : Fin 24)` *is*
`⟨3, _⟩` definitionally; the two differ only syntactically, and `simp` matches on
syntax. -/

@[simp] theorem finMk0 (hh : 0 < 24) : (⟨0, hh⟩ : Fin 24) = 0 := rfl
@[simp] theorem finMk1 (hh : 1 < 24) : (⟨1, hh⟩ : Fin 24) = 1 := rfl
@[simp] theorem finMk2 (hh : 2 < 24) : (⟨2, hh⟩ : Fin 24) = 2 := rfl
@[simp] theorem finMk3 (hh : 3 < 24) : (⟨3, hh⟩ : Fin 24) = 3 := rfl
@[simp] theorem finMk4 (hh : 4 < 24) : (⟨4, hh⟩ : Fin 24) = 4 := rfl
@[simp] theorem finMk5 (hh : 5 < 24) : (⟨5, hh⟩ : Fin 24) = 5 := rfl
@[simp] theorem finMk6 (hh : 6 < 24) : (⟨6, hh⟩ : Fin 24) = 6 := rfl
@[simp] theorem finMk7 (hh : 7 < 24) : (⟨7, hh⟩ : Fin 24) = 7 := rfl
@[simp] theorem finMk8 (hh : 8 < 24) : (⟨8, hh⟩ : Fin 24) = 8 := rfl
@[simp] theorem finMk9 (hh : 9 < 24) : (⟨9, hh⟩ : Fin 24) = 9 := rfl
@[simp] theorem finMk10 (hh : 10 < 24) : (⟨10, hh⟩ : Fin 24) = 10 := rfl
@[simp] theorem finMk11 (hh : 11 < 24) : (⟨11, hh⟩ : Fin 24) = 11 := rfl
@[simp] theorem finMk12 (hh : 12 < 24) : (⟨12, hh⟩ : Fin 24) = 12 := rfl
@[simp] theorem finMk13 (hh : 13 < 24) : (⟨13, hh⟩ : Fin 24) = 13 := rfl
@[simp] theorem finMk14 (hh : 14 < 24) : (⟨14, hh⟩ : Fin 24) = 14 := rfl
@[simp] theorem finMk15 (hh : 15 < 24) : (⟨15, hh⟩ : Fin 24) = 15 := rfl
@[simp] theorem finMk16 (hh : 16 < 24) : (⟨16, hh⟩ : Fin 24) = 16 := rfl
@[simp] theorem finMk17 (hh : 17 < 24) : (⟨17, hh⟩ : Fin 24) = 17 := rfl
@[simp] theorem finMk18 (hh : 18 < 24) : (⟨18, hh⟩ : Fin 24) = 18 := rfl
@[simp] theorem finMk19 (hh : 19 < 24) : (⟨19, hh⟩ : Fin 24) = 19 := rfl
@[simp] theorem finMk20 (hh : 20 < 24) : (⟨20, hh⟩ : Fin 24) = 20 := rfl
@[simp] theorem finMk21 (hh : 21 < 24) : (⟨21, hh⟩ : Fin 24) = 21 := rfl
@[simp] theorem finMk22 (hh : 22 < 24) : (⟨22, hh⟩ : Fin 24) = 22 := rfl
@[simp] theorem finMk23 (hh : 23 < 24) : (⟨23, hh⟩ : Fin 24) = 23 := rfl
set_option maxHeartbeats 4000000 in
/-- **Gram symmetry** — discharged by the 576 computed entries.

`fin_cases i <;> fin_cases j` opens 24² = 576 goals and each is matched against
the full 576-lemma `simp only` set, so this one dispatch costs far more than the
default 200 000 heartbeats. It is a finite, terminating computation — the budget
is raised, not removed. The limit was never hit before the split because the
enclosing module never compiled this far. -/
theorem gram_symm (z h : R) :
    ∀ i j, trM z h (mulNF h (e i) (e j)) = trM z h (mulNF h (e j) (e i)) := by
  intro i j
  fin_cases i <;> fin_cases j <;>
    simp only [finMk0, finMk1, finMk2, finMk3, finMk4, finMk5, finMk6, finMk7, finMk8, finMk9, finMk10, finMk11, finMk12, finMk13, finMk14, finMk15, finMk16, finMk17, finMk18, finMk19, finMk20, finMk21, finMk22, finMk23, gramval_0_0, gramval_0_1, gramval_0_2, gramval_0_3, gramval_0_4, gramval_0_5, gramval_0_6, gramval_0_7, gramval_0_8, gramval_0_9, gramval_0_10, gramval_0_11, gramval_0_12, gramval_0_13, gramval_0_14, gramval_0_15, gramval_0_16, gramval_0_17, gramval_0_18, gramval_0_19, gramval_0_20, gramval_0_21, gramval_0_22, gramval_0_23, gramval_1_0, gramval_1_1, gramval_1_2, gramval_1_3, gramval_1_4, gramval_1_5, gramval_1_6, gramval_1_7, gramval_1_8, gramval_1_9, gramval_1_10, gramval_1_11, gramval_1_12, gramval_1_13, gramval_1_14, gramval_1_15, gramval_1_16, gramval_1_17, gramval_1_18, gramval_1_19, gramval_1_20, gramval_1_21, gramval_1_22, gramval_1_23, gramval_2_0, gramval_2_1, gramval_2_2, gramval_2_3, gramval_2_4, gramval_2_5, gramval_2_6, gramval_2_7, gramval_2_8, gramval_2_9, gramval_2_10, gramval_2_11, gramval_2_12, gramval_2_13, gramval_2_14, gramval_2_15, gramval_2_16, gramval_2_17, gramval_2_18, gramval_2_19, gramval_2_20, gramval_2_21, gramval_2_22, gramval_2_23, gramval_3_0, gramval_3_1, gramval_3_2, gramval_3_3, gramval_3_4, gramval_3_5, gramval_3_6, gramval_3_7, gramval_3_8, gramval_3_9, gramval_3_10, gramval_3_11, gramval_3_12, gramval_3_13, gramval_3_14, gramval_3_15, gramval_3_16, gramval_3_17, gramval_3_18, gramval_3_19, gramval_3_20, gramval_3_21, gramval_3_22, gramval_3_23, gramval_4_0, gramval_4_1, gramval_4_2, gramval_4_3, gramval_4_4, gramval_4_5, gramval_4_6, gramval_4_7, gramval_4_8, gramval_4_9, gramval_4_10, gramval_4_11, gramval_4_12, gramval_4_13, gramval_4_14, gramval_4_15, gramval_4_16, gramval_4_17, gramval_4_18, gramval_4_19, gramval_4_20, gramval_4_21, gramval_4_22, gramval_4_23, gramval_5_0, gramval_5_1, gramval_5_2, gramval_5_3, gramval_5_4, gramval_5_5, gramval_5_6, gramval_5_7, gramval_5_8, gramval_5_9, gramval_5_10, gramval_5_11, gramval_5_12, gramval_5_13, gramval_5_14, gramval_5_15, gramval_5_16, gramval_5_17, gramval_5_18, gramval_5_19, gramval_5_20, gramval_5_21, gramval_5_22, gramval_5_23, gramval_6_0, gramval_6_1, gramval_6_2, gramval_6_3, gramval_6_4, gramval_6_5, gramval_6_6, gramval_6_7, gramval_6_8, gramval_6_9, gramval_6_10, gramval_6_11, gramval_6_12, gramval_6_13, gramval_6_14, gramval_6_15, gramval_6_16, gramval_6_17, gramval_6_18, gramval_6_19, gramval_6_20, gramval_6_21, gramval_6_22, gramval_6_23, gramval_7_0, gramval_7_1, gramval_7_2, gramval_7_3, gramval_7_4, gramval_7_5, gramval_7_6, gramval_7_7, gramval_7_8, gramval_7_9, gramval_7_10, gramval_7_11, gramval_7_12, gramval_7_13, gramval_7_14, gramval_7_15, gramval_7_16, gramval_7_17, gramval_7_18, gramval_7_19, gramval_7_20, gramval_7_21, gramval_7_22, gramval_7_23, gramval_8_0, gramval_8_1, gramval_8_2, gramval_8_3, gramval_8_4, gramval_8_5, gramval_8_6, gramval_8_7, gramval_8_8, gramval_8_9, gramval_8_10, gramval_8_11, gramval_8_12, gramval_8_13, gramval_8_14, gramval_8_15, gramval_8_16, gramval_8_17, gramval_8_18, gramval_8_19, gramval_8_20, gramval_8_21, gramval_8_22, gramval_8_23, gramval_9_0, gramval_9_1, gramval_9_2, gramval_9_3, gramval_9_4, gramval_9_5, gramval_9_6, gramval_9_7, gramval_9_8, gramval_9_9, gramval_9_10, gramval_9_11, gramval_9_12, gramval_9_13, gramval_9_14, gramval_9_15, gramval_9_16, gramval_9_17, gramval_9_18, gramval_9_19, gramval_9_20, gramval_9_21, gramval_9_22, gramval_9_23, gramval_10_0, gramval_10_1, gramval_10_2, gramval_10_3, gramval_10_4, gramval_10_5, gramval_10_6, gramval_10_7, gramval_10_8, gramval_10_9, gramval_10_10, gramval_10_11, gramval_10_12, gramval_10_13, gramval_10_14, gramval_10_15, gramval_10_16, gramval_10_17, gramval_10_18, gramval_10_19, gramval_10_20, gramval_10_21, gramval_10_22, gramval_10_23, gramval_11_0, gramval_11_1, gramval_11_2, gramval_11_3, gramval_11_4, gramval_11_5, gramval_11_6, gramval_11_7, gramval_11_8, gramval_11_9, gramval_11_10, gramval_11_11, gramval_11_12, gramval_11_13, gramval_11_14, gramval_11_15, gramval_11_16, gramval_11_17, gramval_11_18, gramval_11_19, gramval_11_20, gramval_11_21, gramval_11_22, gramval_11_23, gramval_12_0, gramval_12_1, gramval_12_2, gramval_12_3, gramval_12_4, gramval_12_5, gramval_12_6, gramval_12_7, gramval_12_8, gramval_12_9, gramval_12_10, gramval_12_11, gramval_12_12, gramval_12_13, gramval_12_14, gramval_12_15, gramval_12_16, gramval_12_17, gramval_12_18, gramval_12_19, gramval_12_20, gramval_12_21, gramval_12_22, gramval_12_23, gramval_13_0, gramval_13_1, gramval_13_2, gramval_13_3, gramval_13_4, gramval_13_5, gramval_13_6, gramval_13_7, gramval_13_8, gramval_13_9, gramval_13_10, gramval_13_11, gramval_13_12, gramval_13_13, gramval_13_14, gramval_13_15, gramval_13_16, gramval_13_17, gramval_13_18, gramval_13_19, gramval_13_20, gramval_13_21, gramval_13_22, gramval_13_23, gramval_14_0, gramval_14_1, gramval_14_2, gramval_14_3, gramval_14_4, gramval_14_5, gramval_14_6, gramval_14_7, gramval_14_8, gramval_14_9, gramval_14_10, gramval_14_11, gramval_14_12, gramval_14_13, gramval_14_14, gramval_14_15, gramval_14_16, gramval_14_17, gramval_14_18, gramval_14_19, gramval_14_20, gramval_14_21, gramval_14_22, gramval_14_23, gramval_15_0, gramval_15_1, gramval_15_2, gramval_15_3, gramval_15_4, gramval_15_5, gramval_15_6, gramval_15_7, gramval_15_8, gramval_15_9, gramval_15_10, gramval_15_11, gramval_15_12, gramval_15_13, gramval_15_14, gramval_15_15, gramval_15_16, gramval_15_17, gramval_15_18, gramval_15_19, gramval_15_20, gramval_15_21, gramval_15_22, gramval_15_23, gramval_16_0, gramval_16_1, gramval_16_2, gramval_16_3, gramval_16_4, gramval_16_5, gramval_16_6, gramval_16_7, gramval_16_8, gramval_16_9, gramval_16_10, gramval_16_11, gramval_16_12, gramval_16_13, gramval_16_14, gramval_16_15, gramval_16_16, gramval_16_17, gramval_16_18, gramval_16_19, gramval_16_20, gramval_16_21, gramval_16_22, gramval_16_23, gramval_17_0, gramval_17_1, gramval_17_2, gramval_17_3, gramval_17_4, gramval_17_5, gramval_17_6, gramval_17_7, gramval_17_8, gramval_17_9, gramval_17_10, gramval_17_11, gramval_17_12, gramval_17_13, gramval_17_14, gramval_17_15, gramval_17_16, gramval_17_17, gramval_17_18, gramval_17_19, gramval_17_20, gramval_17_21, gramval_17_22, gramval_17_23, gramval_18_0, gramval_18_1, gramval_18_2, gramval_18_3, gramval_18_4, gramval_18_5, gramval_18_6, gramval_18_7, gramval_18_8, gramval_18_9, gramval_18_10, gramval_18_11, gramval_18_12, gramval_18_13, gramval_18_14, gramval_18_15, gramval_18_16, gramval_18_17, gramval_18_18, gramval_18_19, gramval_18_20, gramval_18_21, gramval_18_22, gramval_18_23, gramval_19_0, gramval_19_1, gramval_19_2, gramval_19_3, gramval_19_4, gramval_19_5, gramval_19_6, gramval_19_7, gramval_19_8, gramval_19_9, gramval_19_10, gramval_19_11, gramval_19_12, gramval_19_13, gramval_19_14, gramval_19_15, gramval_19_16, gramval_19_17, gramval_19_18, gramval_19_19, gramval_19_20, gramval_19_21, gramval_19_22, gramval_19_23, gramval_20_0, gramval_20_1, gramval_20_2, gramval_20_3, gramval_20_4, gramval_20_5, gramval_20_6, gramval_20_7, gramval_20_8, gramval_20_9, gramval_20_10, gramval_20_11, gramval_20_12, gramval_20_13, gramval_20_14, gramval_20_15, gramval_20_16, gramval_20_17, gramval_20_18, gramval_20_19, gramval_20_20, gramval_20_21, gramval_20_22, gramval_20_23, gramval_21_0, gramval_21_1, gramval_21_2, gramval_21_3, gramval_21_4, gramval_21_5, gramval_21_6, gramval_21_7, gramval_21_8, gramval_21_9, gramval_21_10, gramval_21_11, gramval_21_12, gramval_21_13, gramval_21_14, gramval_21_15, gramval_21_16, gramval_21_17, gramval_21_18, gramval_21_19, gramval_21_20, gramval_21_21, gramval_21_22, gramval_21_23, gramval_22_0, gramval_22_1, gramval_22_2, gramval_22_3, gramval_22_4, gramval_22_5, gramval_22_6, gramval_22_7, gramval_22_8, gramval_22_9, gramval_22_10, gramval_22_11, gramval_22_12, gramval_22_13, gramval_22_14, gramval_22_15, gramval_22_16, gramval_22_17, gramval_22_18, gramval_22_19, gramval_22_20, gramval_22_21, gramval_22_22, gramval_22_23, gramval_23_0, gramval_23_1, gramval_23_2, gramval_23_3, gramval_23_4, gramval_23_5, gramval_23_6, gramval_23_7, gramval_23_8, gramval_23_9, gramval_23_10, gramval_23_11, gramval_23_12, gramval_23_13, gramval_23_14, gramval_23_15, gramval_23_16, gramval_23_17, gramval_23_18, gramval_23_19, gramval_23_20, gramval_23_21, gramval_23_22, gramval_23_23]



/-- **(M2) Trace cyclicity** `tr_M(u·v) = tr_M(v·u)` — the defining trace property,
**sorry-free**.

Both halves are proved: the Fin-24-free reduction `trM_cyclic_of_gram_symm`, and
the finite Gram-symmetry base `gram_symm` above, discharged by
`fin_cases i <;> fin_cases j` against the 576 generated entries of the
`MarkovTraceH4Gram0..7` chain. An earlier revision of this docstring said
`gram_symm` "remains a cited `sorry` (closeable on demand)" — that was written
before the closure was committed and is no longer true, the same staleness the
module header records. Verified:
`#print axioms QOU.Machinery.H4.trM_cyclic` →
`[propext, Classical.choice, Quot.sound]`. -/
theorem trM_cyclic (z h : R) (u v : Fin 24 → R) :
    trM z h (mulNF h u v) = trM z h (mulNF h v u) :=
  trM_cyclic_of_gram_symm z h (gram_symm z h) u v

end QOU.Machinery.H4
