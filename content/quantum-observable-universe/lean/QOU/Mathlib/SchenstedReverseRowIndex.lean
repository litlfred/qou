import QOU.Mathlib.SchenstedReverseRow

/-!
# QOU.Mathlib.SchenstedReverseRowIndex — where reverse row insertion writes (RSK inverse, brick 12a)

Brick 1 defined `rowUninsert` and proved it inverts `rowInsert` on the bumping branch. Everything
downstream that has to reason about **columns** — chiefly that the reverse cascade preserves
`ColStrict` — needs more than that: it needs to know *which index* `rowUninsert` writes to, and
that nothing to the right of that index was eligible.

`SchenstedInsertion` has the forward counterpart (`bump_findIdx_mono`, `getD_le_of_lt_findIdx`,
feeding `strictBelow_bump_step` and `insert_colStrict`). There is no reverse counterpart, so this
file supplies one.

**`rowUninsert_spec`** packages the whole story in a single existential: if reverse-inserting `y`
into `r` displaces `z`, then there is an index `k` with

* `k < r.length` and `r.getD k 0 = z` — `z` is the entry that was sitting at `k`;
* `(rowUninsert r y).1 = r.set k y` — the row changed at `k` and nowhere else;
* `z < y` — the replacement is strictly larger, which is what makes the column comparison move;
* `∀ m, k < m → m < r.length → y ≤ r.getD m 0` — **nothing to the right of `k` was eligible**.

That last clause is the one carrying the content. `rowUninsert` descends to the end of the row
before deciding, so it takes the *rightmost* entry strictly below `y`; the column argument needs
exactly that maximality, not merely "some entry was replaced".

Three consequences follow, and the last is the one the whole reverse programme was waiting on:

* `le_index_of_lt` — the write index dominates every eligible index (maximality, contrapositive);
* `reverse_bump_index_mono` — **reverse bump columns weakly increase going up**, the mirror of
  `bump_findIdx_mono`;
* **`strictBelow_reverse_bump_step`** — one adjacent-row step of column-strictness, the mirror of
  `strictBelow_bump_step`.

I had expected the monotonicity to be the hard step. It is three lines: `upper[kLow] < lower[kLow]`
makes `kLow` itself an eligible index in the upper row, and the write index dominates every
eligible index. The pair-of-rows step is then four column cases, of which monotonicity kills the
only bad one.

## Scope

Two adjacent rows. Lifting `strictBelow_reverse_bump_step` along the cascade — which also needs the
corner hypothesis located in `SchenstedUninsertInvariants`, for the `dropLast` at the target row —
is the next brick of epic `qou-nrex`. Nothing here claims it, and `RSKBurnsideHolds` for general
`n` stays open.

Pure combinatorics on `ℕ`; nothing archimedean.
-/

namespace QOU.Mathlib.Schensted

/-- Reading an in-range position with `getD` lands in the list. `getD` is used throughout the
column machinery to dodge dependent-index proofs, so this is the bridge back to membership. -/
theorem getD_mem {r : List ℕ} {m : ℕ} (h : m < r.length) : r.getD m 0 ∈ r := by
  rw [getD_eq_getElem_mem h]
  exact List.getElem_mem h

/-- **What `rowUninsert` does, as an index.** See the module docstring: the fourth conjunct — that
nothing right of `k` was eligible — is the maximality the column argument runs on. -/
theorem rowUninsert_spec : ∀ (r : List ℕ) (y z : ℕ), (rowUninsert r y).2 = some z →
    ∃ k, k < r.length ∧ r.getD k 0 = z ∧ (rowUninsert r y).1 = r.set k y ∧ z < y ∧
      ∀ m, k < m → m < r.length → y ≤ r.getD m 0
  | [], y, z, hz => by simp at hz
  | a :: r, y, z, hz => by
      obtain ⟨r', w, hr⟩ : ∃ r' w, rowUninsert r y = (r', w) := ⟨_, _, rfl⟩
      rw [rowUninsert_cons, hr] at hz ⊢
      cases w with
      | some w =>
          simp only at hz ⊢
          have hwz : w = z := Option.some.inj hz
          subst hwz
          obtain ⟨k, hk, hgk, hset, hzy, hright⟩ :=
            rowUninsert_spec r y w (by rw [hr])
          rw [hr] at hset
          simp only at hset
          refine ⟨k + 1, by simpa using hk, by simpa using hgk, ?_, hzy, ?_⟩
          · rw [List.set_cons_succ, ← hset]
          · intro m hm hmlt
            match m with
            | 0 => omega
            | m' + 1 =>
                simp only [List.getD_cons_succ]
                exact hright m' (by omega) (by simpa using hmlt)
      | none =>
          by_cases ha : a < y
          · rw [if_pos ha] at hz ⊢
            simp only at hz ⊢
            have hza : a = z := Option.some.inj hz
            subst hza
            refine ⟨0, by simp, by simp, by simp, ha, ?_⟩
            intro m hm hmlt
            match m with
            | 0 => omega
            | m' + 1 =>
                simp only [List.getD_cons_succ]
                have hall := forall_le_of_rowUninsert_none r y (by rw [hr])
                exact hall _ (getD_mem (by simpa using hmlt))
          · rw [if_neg ha] at hz
            simp at hz

/-! ### The consequence the cascade argument consumes

`getD_set_self`, `getD_set_ne` and `getD_eq_getElem_mem` are already in `SchenstedInsertion`
(lines 551-563) and are reused, not restated. -/

/-- **The displaced entry is strictly below everything to its right.**

Worth noting how cheap this is: it does *not* need the row to be sorted. The maximality clause of
`rowUninsert_spec` already says every entry right of `k` is `≥ y`, and the displaced `z` is `< y`,
so the two chain directly. I expected to need weak sortedness plus a rightmost argument here; the
spec hands it over. -/
theorem lt_of_index_lt {r : List ℕ} {y z k m : ℕ}
    (hright : ∀ m, k < m → m < r.length → y ≤ r.getD m 0) (hzy : z < y)
    (hm : k < m) (hmlt : m < r.length) : z < r.getD m 0 :=
  lt_of_lt_of_le hzy (hright m hm hmlt)

/-! ### Bump-column monotonicity, reversed

The forward cascade is column-strict because bump columns weakly **decrease** going down
(`bump_findIdx_mono`). Reversed, they weakly **increase** going up: the reverse cascade removes a
cell from a lower row and writes into the upper row at an index no further left.

That is the one fact I expected to be the hard step of the reverse bumping lemma. It is not: it is
the maximality clause of `rowUninsert_spec` read contrapositively, and needs no induction of its
own. Both lemmas below are three lines. -/

/-- **The write index dominates every eligible index.** If any in-range entry of `r` is strictly
below `y`, then `rowUninsert` writes at least that far right. Contrapositive of maximality. -/
theorem le_index_of_lt {r : List ℕ} {y k j : ℕ}
    (hright : ∀ m, k < m → m < r.length → y ≤ r.getD m 0)
    (hj : j < r.length) (hjy : r.getD j 0 < y) : j ≤ k := by
  by_contra hcon
  exact absurd (hright j (by omega) hj) (by omega)

/-- **Reverse bump columns weakly increase going up** — the mirror of `bump_findIdx_mono`.

If the lower row gave up its entry at `kLow`, and the upper row sits strictly above it
(`StrictBelow upper lower`), then reverse-inserting that entry into the upper row writes at an
index `kUp ≥ kLow`.

The proof is the whole reason column-strictness survives: `upper[kLow] < lower[kLow] = yLow`, so
`kLow` is itself an eligible index in the upper row, and the write index dominates every eligible
index. -/
theorem reverse_bump_index_mono {upper lower : List ℕ} {yLow kLow kUp : ℕ}
    (hsb : StrictBelow upper lower)
    (hkLow : kLow < lower.length) (hyLow : lower.getD kLow 0 = yLow)
    (hright : ∀ m, kUp < m → m < upper.length → yLow ≤ upper.getD m 0) : kLow ≤ kUp := by
  refine le_index_of_lt hright (lt_of_lt_of_le hkLow hsb.1) ?_
  rw [← hyLow]
  exact hsb.2 kLow hkLow

/-! ### One adjacent-row step of column-strictness, reversed

With monotonicity in hand the pair-of-rows step goes through directly — the mirror of
`strictBelow_bump_step`. -/

/-- **A reverse bump keeps the two rows column-strict.**

`lower` gives up its entry `yLow` (writing `yBelow` in its place), `yLow` is reverse-inserted into
`upper` (writing `yLow` in place of `yUp`), and the pair stays `StrictBelow`.

Four column cases, and monotonicity kills the only bad one:

* `j = kUp = kLow` — the upper row now reads `yLow`, the lower row now reads `yBelow`, and
  `yLow < yBelow` because a reverse insertion always writes something strictly larger.
* `j = kUp > kLow` — the lower row is unchanged at `j`, and `lt_of_index_lt` on the lower row's
  maximality gives `yLow < lower[j]`.
* `j = kLow < kUp` — the upper row is unchanged at `j`, and
  `upper[kLow] < lower[kLow] = yLow < yBelow`.
* neither — both rows unchanged at `j`.

`j = kUp < kLow` is the case that would break it, and `reverse_bump_index_mono` excludes it. -/
theorem strictBelow_reverse_bump_step {upper lower : List ℕ} {yBelow yLow yUp : ℕ}
    (hsb : StrictBelow upper lower)
    (hlow : (rowUninsert lower yBelow).2 = some yLow)
    (hup : (rowUninsert upper yLow).2 = some yUp) :
    StrictBelow (rowUninsert upper yLow).1 (rowUninsert lower yBelow).1 := by
  obtain ⟨kLow, hkLow, hgLow, hsetLow, hltLow, hrightLow⟩ :=
    rowUninsert_spec lower yBelow yLow hlow
  obtain ⟨kUp, hkUp, hgUp, hsetUp, hltUp, hrightUp⟩ :=
    rowUninsert_spec upper yLow yUp hup
  have hmono : kLow ≤ kUp := reverse_bump_index_mono hsb hkLow hgLow hrightUp
  rw [hsetLow, hsetUp]
  refine ⟨by simpa using hsb.1, ?_⟩
  intro j hj
  have hjl : j < lower.length := by simpa using hj
  have hju : j < upper.length := lt_of_lt_of_le hjl hsb.1
  by_cases hjU : j = kUp
  · subst hjU
    rw [getD_set_self hju]
    by_cases hjL : j = kLow
    · rw [hjL, getD_set_self hkLow]
      exact hltLow
    · rw [getD_set_ne (fun h => hjL h.symm)]
      exact lt_of_index_lt hrightLow hltLow (lt_of_le_of_ne hmono (fun h => hjL h.symm)) hjl
  · rw [getD_set_ne (fun h => hjU h.symm)]
    by_cases hjL : j = kLow
    · rw [hjL, getD_set_self hkLow]
      calc upper.getD kLow 0 < lower.getD kLow 0 := hsb.2 kLow hkLow
        _ = yLow := hgLow
        _ < yBelow := hltLow
    · rw [getD_set_ne (fun h => hjL h.symm)]
      exact hsb.2 j hjl

/-! ### The rightmost choice, machine-checked

`rowUninsert [1,2,4] 3` has **two** eligible entries (`1` and `2` are both `< 3`). It must take the
right-hand one. If it took the leftmost the result would be `([3,2,4], some 1)`, which is not even
weakly increasing — so this witness also shows why `rowUninsert_sorted` needs the rightmost
convention rather than merely some eligible entry. -/
theorem rowUninsert_rightmost_witness : rowUninsert [1, 2, 4] 3 = ([1, 3, 4], some 2) := by decide

/-- And the spec's index for that witness is `1`, not `0`: the row changed at index 1, the entry
there was `2`, and the one entry to its right is `≥ 3`. -/
theorem rowUninsert_rightmost_witness_index :
    ([1, 2, 4] : List ℕ).getD 1 0 = 2 ∧ ([1, 2, 4] : List ℕ).set 1 3 = [1, 3, 4] ∧
      (2 : ℕ) < 3 ∧ ∀ m, 1 < m → m < 3 → (3 : ℕ) ≤ ([1, 2, 4] : List ℕ).getD m 0 := by
  refine ⟨by decide, by decide, by decide, ?_⟩
  intro m hm hmlt
  match m with
  | 0 => omega
  | 1 => omega
  | 2 => decide
  | (n + 3) => omega

end QOU.Mathlib.Schensted
