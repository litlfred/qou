import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Combinatorics.Enumerative.Partition
import Mathlib.Tactic
import QOU.HeckeAlgebra.Common
import QOU.HeckeAlgebra.QSubstrate
import QOU.MathlibExt.QIntegerCanonical

/-!
# QOU.HeckeAlgebra.JonesMarkovWenzl

The Wenzl 1988 §3 closed form for the Jones-Markov central
coefficients `y_λ(q)`:

    y_λ(q) = z^{n-1} · ∏_{(i,j) ∈ λ} [h_{(i,j)}^λ]_q^{-1} · q^{|λ| · c_{(i,j)}^λ}

where:
- `z = 1 / (q^{1/2} + q^{-1/2})` is the Markov parameter
- `[k]_q := (q^{k/2} - q^{-k/2}) / (q^{1/2} - q^{-1/2})` is the
  q-integer
- `h_{(i,j)}^λ` is the hook length of cell `(i,j)` in `λ`
- `c_{(i,j)}^λ = j - i` is the cell's content

## What this module provides

- `qInteger k q` — the q-integer `[k]_q`
- `partsList` / `rowLen` / `colLen` — row and column lengths of `λ`,
  computed from `Nat.Partition.parts`
- `cellContent` / `cellHookLength` — **definitions** (`c = j − i`;
  `h = arm + leg + 1`), with `cellContent_diag`, `cellContent_swap` and
  `cellHookLength_corner` as proved sanity lemmas
- `wenzlClosedForm λ q` — the closed-form expression for `y_λ`, written out
  as a product over the cells of `λ`
- `JonesMarkovCoefficient_eq_wenzl` — the one genuine external input
  (Wenzl 1988 Lemma 3.2), identifying the abstract `y_λ` with that product

Everything except the last item is now computed. Until 2026-08-08 the middle
three were opaque `axiom`s, which left the identification an equation between
two unconstrained functions — no content whatsoever, while the module header
advertised "the Wenzl 1988 §3 closed form".

## Base ring (AGENTS.md §7c) — `ℝ` here is required, not a gratuitous specialisation

Every `q` in this module carries a **half-integer exponent**: the q-integer is
`[k]_q = (q^{k/2} − q^{−k/2}) / (q^{1/2} − q^{−1/2})` and the Markov parameter is
`z = 1/(q^{1/2} + q^{−1/2})`.  A square root of `q` does not exist in a generic
`CommRing`, so these are `Real.rpow` applications (hence the
`Mathlib.Analysis.SpecialFunctions.Pow.Real` import) and the module is
archimedean by construction — it sits on the observation side of the
substrate→archimedean wall.

**The generic content is not missing; it lives elsewhere and this module is its
archimedean realisation.** The base-ring-generic q-integer is
`QOU.QInteger.qIntBal` in `QOU.MathlibExt.QIntegerCanonical`, and the bridge is
proved here as `qInteger_eq_canonical`:

    qInteger k q = QOU.QInteger.qIntBal (q ^ ((1 : ℝ) / 2)) k     (for 0 ≤ q)

i.e. this file is exactly `qIntBal` instantiated at the **real** square root of
the substrate parameter.  Rewriting it over `{R : Type*} [CommRing R]` would be
unfaithful — there is no `√q` to instantiate at, and the Wenzl closed form would
have to be restated in a variable meaning `q^{1/2}`, which is what `qIntBal`
already is.

Recorded so §7c sweeps stop re-flagging this file: a bare grep sees ~26 `ℝ`s in
a `HeckeAlgebra` module and scores it a base-ring candidate, which it is not.

## Categorical content

The Wenzl closed form is one half of the q-Hecke / q-Plancherel
duality; the other half (`χ^lam_q` from Hoefsmit) is in
`QOU.HeckeAlgebra.Hoefsmit`.  Together they implement the
manuscript's `prop:wenzl-jones-markov-closure`.

## Open Lean port

The combinatorial accessors on `Nat.Partition` (hook length,
content) require Mathlib's `YoungDiagram` ↔ `Partition` bridge,
which is partial as of Mathlib 2024.  This module captures the
type-level interface; concrete computation is deferred.

## References

- [wenzl1988] Wenzl, *Hecke algebras of type A_n and subfactors*,
  Inventiones Math. 92 (1988), Lemma 3.2.
- [jones1985] Jones, *A polynomial invariant for knots via von
  Neumann algebras*, Bull. AMS 12 (1985).
- [stanley1999] Stanley, *Enumerative Combinatorics II*, §7.21
  (RSK and the hook-length formula).
- `computations/wedderburn_jones_markov.py` —
  Python implementation of the Wenzl closed form.
-/

namespace QOU.HeckeAlgebra.JonesMarkovWenzl

open QOU.HeckeAlgebra QOU.HeckeAlgebra.QSubstrate

/-- The q-integer `[k]_q := (q^{k/2} - q^{-k/2}) / (q^{1/2} - q^{-1/2})`.
    Equivalent to the standard `[k]_q = 1 + q + q² + ... + q^{k-1}`
    when `q ≠ 1`.  Defined for real `q > 0`. -/
noncomputable def qInteger (k : ℕ) (q : ℝ) : ℝ :=
  if k = 0 then 0
  else (q ^ ((k : ℝ) / 2) - q ^ (-(k : ℝ) / 2)) /
       (q ^ ((1 : ℝ) / 2) - q ^ (-(1 : ℝ) / 2))

/-- **Bridge to the canonical balanced bracket — this is not a third
convention.**

The half-powers make this site look like a separate `[k]` from both `qIntBal`
and `qIntGeo`, and an earlier census set it aside on exactly that reading.  It
is not: substituting `v = q^{1/2}` gives `v^k = q^{k/2}` and
`v⁻¹ = q^{-1/2}`, so the whole expression is the *balanced* bracket in the
half-power variable.

That makes it the mirror of `qIntegerRescaled`: one site is the canonical
bracket at `q²`, this one at `q^{1/2}`, and both are instances of the single
twist `qIntBal_eq_twist_canonical` rather than new conventions.  Here the `k = 0`
guard is again redundant — `qIntBal v 0 = 0` already.

`0 ≤ q` is the real content of the hypothesis: it is what lets `rpow` powers
compose (`(q^{1/2})^k = q^{k/2}`), and it is the file's own standing assumption
("Defined for real `q > 0`"). -/
theorem qInteger_eq_canonical (q : ℝ) (hq : 0 ≤ q) (k : ℕ) :
    qInteger k q = QOU.QInteger.qIntBal (q ^ ((1 : ℝ) / 2)) k := by
  have hv : ∀ m : ℕ, (q ^ ((1 : ℝ) / 2)) ^ m = q ^ ((m : ℝ) / 2) := by
    intro m
    rw [← Real.rpow_natCast (q ^ ((1 : ℝ) / 2)) m, ← Real.rpow_mul hq]
    ring_nf
  have hinv : ∀ m : ℕ, ((q ^ ((1 : ℝ) / 2))⁻¹) ^ m = q ^ (-(m : ℝ) / 2) := by
    intro m
    rw [← Real.rpow_neg hq, ← Real.rpow_natCast (q ^ (-((1 : ℝ) / 2))) m,
      ← Real.rpow_mul hq]
    ring_nf
  unfold qInteger
  rw [QOU.QInteger.qIntBal_def]
  split_ifs with h
  · subst h; simp
  · rw [hv k, hinv k, show (-1 : ℝ) / 2 = -((1 : ℝ) / 2) by ring, Real.rpow_neg hq]

/-- `[1]_q = 1` whenever the denominator `q^{1/2} - q^{-1/2}` is
    non-zero (i.e. for `q ≠ 1`).  At `q = 1` the formula gives
    `0/0 = 0` by Lean's division convention; the `[1]_q = 1`
    identity is the limit, which Mathlib does not transport
    automatically.  This is the "generic-q" form. -/
theorem qInteger_one (q : ℝ)
    (h_denom : q ^ ((1 : ℝ) / 2) - q ^ (-(1 : ℝ) / 2) ≠ 0) :
    qInteger 1 q = 1 := by
  unfold qInteger
  rw [if_neg Nat.one_ne_zero]
  -- (1 : ℕ) cast to ℝ is 1, so numerator = denominator = q^{1/2} - q^{-1/2}.
  simp only [Nat.cast_one]
  exact div_self h_denom

/-- The q-integer `[0]_q = 0` (by convention; consistent with
    `[k]_q = (q^{k/2} - q^{-k/2}) / (q^{1/2} - q^{-1/2})` having
    a zero numerator at `k = 0`). -/
theorem qInteger_zero (q : ℝ) : qInteger 0 q = 0 := by
  unfold qInteger
  simp

/-! ## Partition combinatorics — computed, not axiomatised

`cellContent`, `cellHookLength` and `wenzlClosedForm` were previously three
opaque `axiom`s, which made the fourth axiom (`JonesMarkovCoefficient_eq_wenzl`,
`y_λ = wenzlClosedForm`) an equation between two *unconstrained* opaque
functions — satisfiable by anything, hence no content at all. The module
advertised "the Wenzl 1988 §3 closed form" and supplied none of it.

The two combinatorial accessors were also redundant: `cellContent i j = j − i`
is already defined for real in three other places in this corpus
(`MathlibExt/QPartitionCombinatorics`, `MathlibExt/WenzlSchurElement`,
`BraidKnot/JucysMurphy`). Re-declaring them opaque here was strictly weaker
than what the corpus already had.

All three are now definitions, so `JonesMarkovCoefficient_eq_wenzl` states
something falsifiable. Bean `qou-t7zg`. -/

/-- The parts of `λ` as a descending list — the row lengths `λ₀ ≥ λ₁ ≥ …`. -/
def partsList {n : ℕ} (lam : Nat.Partition n) : List ℕ :=
  lam.parts.sort (· ≥ ·)

/-- Row length `λ_i` (`0` past the last row). -/
def rowLen {n : ℕ} (lam : Nat.Partition n) (i : ℕ) : ℕ :=
  ((partsList lam)[i]?).getD 0

/-- Column length `λ'_j = #{ i : λ_i > j }` — the conjugate partition's `j`-th
    part, computed by counting the rows long enough to reach column `j`. -/
def colLen {n : ℕ} (lam : Nat.Partition n) (j : ℕ) : ℕ :=
  ((partsList lam).filter (fun r => j < r)).length

/-- **Cell content** `c_{(i,j)} = j − i` (column index minus row index).
    Independent of `λ`; the partition argument is kept for call-site symmetry
    with `cellHookLength`. -/
-- Ref: [fulton1997] https://doi.org/10.1017/CBO9780511626241 §1 (cell content c=j−i on Young diagrams)
def cellContent {n : ℕ} (_lam : Nat.Partition n) (i j : ℕ) : ℤ :=
  (j : ℤ) - (i : ℤ)

/-- **Hook length** `h_{(i,j)} = (λ_i − j) + (λ'_j − i) − 1`: the arm to the
    right of `(i,j)`, plus the leg below it, plus the cell itself. -/
-- Ref: [fulton1997] https://doi.org/10.1017/CBO9780511626241 §4 (hook length formula on Young diagrams)
def cellHookLength {n : ℕ} (lam : Nat.Partition n) (i j : ℕ) : ℕ :=
  (rowLen lam i - j) + (colLen lam j - i) - 1

@[simp] theorem cellContent_apply {n : ℕ} (lam : Nat.Partition n) (i j : ℕ) :
    cellContent lam i j = (j : ℤ) - (i : ℤ) := rfl

/-- A cell on the diagonal has content `0`. -/
@[simp] theorem cellContent_diag {n : ℕ} (lam : Nat.Partition n) (i : ℕ) :
    cellContent lam i i = 0 := by simp

/-- **Content is antisymmetric under transposing the cell** — the chirality
    atom (cf. `BraidsAndKnots.KeystoneChiralityInvolution`). -/
theorem cellContent_swap {n : ℕ} (lam : Nat.Partition n) (i j : ℕ) :
    cellContent lam j i = - cellContent lam i j := by simp

/-- The corner cell `(0,0)` of a nonempty partition has hook length
    `λ₀ + λ'₀ − 1`, the full first row plus the full first column. -/
theorem cellHookLength_corner {n : ℕ} (lam : Nat.Partition n) :
    cellHookLength lam 0 0 = rowLen lam 0 + colLen lam 0 - 1 := by
  simp [cellHookLength]

/-- **Wenzl closed form** for the Jones-Markov coefficient `y_λ(q)`
    (Wenzl 1988 Lemma 3.2):

        y_λ(q) = z^{n-1} · ∏_{(i,j) ∈ λ} [h_{(i,j)}^λ]_q⁻¹ · q^{|λ|·c_{(i,j)}^λ}

    with `z = QSubstrate.markovParameter` the Markov parameter and `[k]_q` the
    `qInteger` above. The product runs over the cells of `λ`: rows
    `i < (partsList λ).length`, and within each row columns `j < λ_i`.

    **Transcription note.** The formula is transcribed from this module's own
    header (the manuscript's statement of Wenzl §3) and has *not* been checked
    against Wenzl 1988 independently — in particular the `q^{|λ|·c}` exponent
    convention (rather than the more common `q^{c}`) is the manuscript's, not
    a correction of mine. Making it an explicit definition is what turns the
    identification below into a checkable claim; verifying the convention
    against the source is the remaining task in bean `qou-t7zg`. -/
-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457 Lemma 3.2 (closed form for y_λ(q))
noncomputable def wenzlClosedForm {n : ℕ} (lam : Nat.Partition n) (q : ℝ) : ℝ :=
  markovParameter ^ (n - 1) *
    (List.range (partsList lam).length).foldl
      (fun acc i =>
        acc * (List.range (rowLen lam i)).foldl
          (fun a j =>
            a * (qInteger (cellHookLength lam i j) q)⁻¹
              * q ^ ((n : ℝ) * (cellContent lam i j : ℝ)))
          1)
      1

/-- The empty partition contributes the bare Markov-parameter prefactor: the
    cell product is empty, so `y_∅(q) = z^{0-1} = z⁻¹`… but `n = 0` here, and
    `0 - 1 = 0` in `ℕ`, so the prefactor is `z^0 = 1`. A sanity check that the
    fold bottoms out rather than a statement about Wenzl's formula. -/
@[simp] theorem wenzlClosedForm_empty (lam : Nat.Partition 0) (q : ℝ) :
    wenzlClosedForm lam q = 1 := by
  -- `Nat.Partition 0` has no parts: each part is positive and they sum to `0`.
  have : partsList lam = [] := by simp [partsList]
  simp [wenzlClosedForm, this]

/-! ## Identification with the abstract Jones-Markov coefficient

`QOU.HeckeAlgebra.MarkovTrace.JonesMarkovCoefficient` is now **defined** to be
`wenzlClosedForm`, so the Wenzl 1988 Lemma 3.2 identification is definitional
rather than an axiom. It is recorded as a `rfl` theorem at the definition site
(`MarkovTrace.jonesMarkovCoefficient_eq_wenzlClosedForm`) rather than here,
because `MarkovTrace` imports this module and not the other way round.

History, because the shape is worth recognising: this used to be
`axiom JonesMarkovCoefficient_eq_wenzl`, and before `wenzlClosedForm` was
defined it was *vacuous* — both sides were opaque, so the equation constrained
nothing. Commit `fa0aa1c5c8` correctly deleted the axiom, but left this comment
attached to nothing, which is a PARSE ERROR: a `/-- -/` doc comment must be
followed by a declaration. The module has not compiled from source since.

It went unnoticed for the reason documented in
`docs/audits/2026-08-26-live-axiom-surface-recheck.md` §4 — a stale `.olean`
(this one dated 2026-07-02) kept satisfying every `import`, so nothing that
merely *used* the module ever noticed it could not be *built*. That is the
same class of defect one step worse: not a wrong axiom verdict, an unbuildable
module hidden behind a cache.
-/


end QOU.HeckeAlgebra.JonesMarkovWenzl
