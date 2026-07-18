import QOU.BraidKnot.StandardYoungTableau

/-!
# Entry monotonicity and consecutive-label geometry for standard Young tableaux

Public, sorry-free geometric facts about `QOU.BraidKnot.StandardYoungTableau`
used by the Okounkov–Vershik exchange argument (`JucysMurphy.lean`).  The two
entry-monotonicity lemmas mirror the `private` copies in `JucysMurphy.lean`
(`entry_lt_diag_succ`, `entry_lt_of_diag_row_lt`), lifted here as reusable
public lemmas; the payoff is:

* **`content_ne_of_succ`** — the cells of two *consecutive* labels never lie on
  the same diagonal (their contents differ).  This is the `d ≠ 0` half of the
  admissibility of an `AdjacentSwapStep`: for a genuine standard tableau,
  consecutive labels can never share a content, because a shared content would
  force a cell carrying a label strictly between them (impossible).

Scope: pure combinatorics on `ℕ`/`ℤ` cell coordinates; §7c-clean (no `ℝ`); no fit.
-/

namespace QOU.BraidKnot

open YoungDiagram

variable {μ : YoungDiagram}

/-- Entries strictly increase along the immediate diagonal step `(i,j) → (i+1,j+1)`. -/
theorem entryLtDiagSucc (T : StandardYoungTableau μ) {i j : ℕ}
    (hmem : (i + 1, j + 1) ∈ μ) : T.entry i j < T.entry (i + 1) (j + 1) :=
  lt_trans
    (T.row_strict i j (μ.up_left_mem (Nat.le_succ i) le_rfl hmem))
    (T.col_strict i (j + 1) hmem)

/-- Entries strictly increase along a diagonal: same content, strictly smaller row ⇒ strictly
smaller entry. -/
theorem entryLtOfDiagRowLt (T : StandardYoungTableau μ) :
    ∀ (r : ℕ) {x y : ℕ × ℕ}, x ∈ μ → y ∈ μ → y.1 = r →
      (x.2 : ℤ) - (x.1 : ℤ) = (y.2 : ℤ) - (y.1 : ℤ) → x.1 < y.1 →
      T.entry x.1 x.2 < T.entry y.1 y.2 := by
  intro r
  induction r with
  | zero => intro x y _ _ hy1 _ hlt; omega
  | succ r IH =>
    rintro ⟨x1, x2⟩ ⟨y1, y2⟩ hx hy hy1 hd hlt
    simp only at hy1 hd hlt ⊢
    subst hy1
    rcases eq_or_lt_of_le (Nat.lt_succ_iff.mp hlt) with heq | hlt'
    · subst heq
      have hy2 : y2 = x2 + 1 := by omega
      subst hy2
      exact entryLtDiagSucc T hy
    · have hzmem : (r, y2 - 1) ∈ μ :=
        μ.up_left_mem (Nat.le_succ r) (Nat.sub_le y2 1) hy
      have hstep : T.entry r (y2 - 1) < T.entry (r + 1) y2 := by
        have h1 : y2 - 1 + 1 = y2 := by omega
        have := entryLtDiagSucc T (i := r) (j := y2 - 1) (by rw [h1]; exact hy)
        rwa [h1] at this
      refine lt_trans (IH (x := (x1, x2)) (y := (r, y2 - 1)) hx hzmem rfl ?_ hlt') hstep
      have : ((y2 - 1 : ℕ) : ℤ) = (y2 : ℤ) - 1 := by omega
      simp only [this]
      omega

/-- **Consecutive labels never share a diagonal.** If cell `q` carries the label one greater
than cell `p` (`entry q = entry p + 1`), then `p` and `q` have different content
`(col − row)`.  A shared content would place a cell carrying a label strictly between the two
consecutive labels — impossible. -/
theorem content_ne_of_succ (T : StandardYoungTableau μ) {p q : ℕ × ℕ}
    (hp : p ∈ μ) (hq : q ∈ μ)
    (hval : T.entry q.1 q.2 = T.entry p.1 p.2 + 1) :
    (p.2 : ℤ) - (p.1 : ℤ) ≠ (q.2 : ℤ) - (q.1 : ℤ) := by
  obtain ⟨p1, p2⟩ := p
  obtain ⟨q1, q2⟩ := q
  simp only at hval ⊢
  intro hc
  -- row trichotomy on p1 vs q1
  rcases lt_trichotomy p1 q1 with hlt | heq | hgt
  · -- p1 < q1: reduce to p being the diagonal predecessor of q, then a strictly-between cell
    -- m = (q1 - 1, q2 - 1) is on the diagonal, in μ, with entry < entry q = a+1
    have hq1 : 1 ≤ q1 := by omega
    have hmmem : (q1 - 1, q2 - 1) ∈ μ := μ.up_left_mem (Nat.sub_le q1 1) (Nat.sub_le q2 1) hq
    have e1 : q1 - 1 + 1 = q1 := by omega
    have e2 : q2 - 1 + 1 = q2 := by omega
    have hmlt : T.entry (q1 - 1) (q2 - 1) < T.entry q1 q2 := by
      have := entryLtDiagSucc T (i := q1 - 1) (j := q2 - 1) (by rw [e1, e2]; exact hq)
      rwa [e1, e2] at this
    -- entry p ≤ entry m
    have hcm : (p2 : ℤ) - (p1 : ℤ) = ((q2 - 1 : ℕ) : ℤ) - ((q1 - 1 : ℕ) : ℤ) := by
      have : ((q2 - 1 : ℕ) : ℤ) = (q2 : ℤ) - 1 := by omega
      have h2 : ((q1 - 1 : ℕ) : ℤ) = (q1 : ℤ) - 1 := by omega
      rw [this, h2]; omega
    have hple : T.entry p1 p2 ≤ T.entry (q1 - 1) (q2 - 1) := by
      rcases lt_or_eq_of_le (Nat.lt_succ_iff.mp (Nat.lt_succ_of_le (Nat.le_pred_of_lt hlt))) with h | h
      · -- p1 < q1 - 1
        exact le_of_lt (entryLtOfDiagRowLt T (q1 - 1) (x := (p1, p2)) (y := (q1 - 1, q2 - 1))
          hp hmmem rfl hcm h)
      · -- p1 = q1 - 1: same row, same content ⇒ same cell
        have hp1eq : p1 = q1 - 1 := h
        have hp2eq : p2 = q2 - 1 := by
          have : ((q2 - 1 : ℕ) : ℤ) = (q2 : ℤ) - 1 := by omega
          have h2 : ((q1 - 1 : ℕ) : ℤ) = (q1 : ℤ) - 1 := by omega
          omega
        rw [hp1eq, hp2eq]
    -- so entry m = a, hence m = p; then a strictly-between cell exists
    have hmentry : T.entry (q1 - 1) (q2 - 1) = T.entry p1 p2 := by omega
    have hmp := T.inj_on (q1 - 1) (q2 - 1) p1 p2 hmmem hp hmentry
    -- p = (q1-1, q2-1), so q = (p1+1, p2+1); (p1, p2+1) carries a label strictly between
    have hp1' : p1 = q1 - 1 := hmp.1.symm
    have hp2' : p2 = q2 - 1 := hmp.2.symm
    have f1 : p1 + 1 = q1 := by omega
    have f2 : p2 + 1 = q2 := by omega
    have hbetween : (p1, p2 + 1) ∈ μ := by
      rw [hp1', f2]
      exact μ.up_left_mem (Nat.sub_le q1 1) (le_refl q2) hq
    have hlt1 : T.entry p1 p2 < T.entry p1 (p2 + 1) := T.row_strict p1 p2 hbetween
    have hqcell2 : T.entry (p1 + 1) (p2 + 1) = T.entry q1 q2 := by rw [f1, f2]
    have hlt2 : T.entry p1 (p2 + 1) < T.entry q1 q2 := by
      have hcol := T.col_strict p1 (p2 + 1) (by rw [f1, f2]; exact hq)
      rw [hqcell2] at hcol; exact hcol
    have hval' : T.entry q1 q2 = T.entry p1 p2 + 1 := hval
    have hchain : T.entry p1 p2 + 1 < T.entry q1 q2 :=
      lt_of_le_of_lt (Nat.succ_le_of_lt hlt1) hlt2
    rw [hval'] at hchain
    exact absurd hchain (lt_irrefl _)
  · -- p1 = q1: same content forces p2 = q2, so p = q, contradicting entries differ
    have : p2 = q2 := by omega
    rw [heq, this] at hval
    omega
  · -- q1 < p1: diagonal monotonicity gives entry q < entry p, i.e. a+1 < a
    have hmono : T.entry q1 q2 < T.entry p1 p2 :=
      entryLtOfDiagRowLt T p1 (x := (q1, q2)) (y := (p1, p2)) hq hp rfl (by omega) hgt
    omega

end QOU.BraidKnot
