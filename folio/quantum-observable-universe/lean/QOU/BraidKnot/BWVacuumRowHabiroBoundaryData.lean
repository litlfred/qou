/-
# The folded fibre boundary data of Σ(2,3,5) as a datum for `HabiroRigidity`

**Extends** [`BWVacuumRowHabiroRigidity.lean`](BWVacuumRowHabiroRigidity.lean) (#3681) — it does NOT
edit it, and it does NOT close the geometric `W_λ` gate or prove Habiro's injectivity (AGENTS.md
§"Axiomatization is NOT a Proof").

Context (audit `2026-07-17-habiro-interpolation-wlambda.md`; probe
`computations/habiro_interpolation_wlambda.py`). #3822 pinned the keystone `W_λ` boundary data at the
**single** order-5 fibre root `ζ = e^{iπ/5}`. Single-order data does not pin a Habiro-ring element;
strength comes from **multiple fibre orders**. This file carries the folded modulus boundary data at
the **rational** fibre roots — order 2 (`ζ = e^{iπ/2} = i`) and order 3 (`ζ = e^{iπ/3}`) — of the
candidate interpolant

  `F_λ(q) = [mark λ]²_q / D(q)²`,  `D(q)² = Σ_{9 McKay nodes} [mark μ]²_q`

(the q-Verlinde measure of the affine-Ê₈ McKay marks `1,2,3,4,5,6,4,2,3`). At the order-2 root the
characters `[mark]_i` are `1,0,−1,0,1,0` (`D² = 4`); at the order-3 root `[mark]_{e^{iπ/3}}` are
`1,1,0,−1,−1,0` (`D² = 6`). The order-5 root (`D² = 10 ± 2√5`, `ℚ(√5)`) is #3822's
`KeystoneLRModulusFold.lean` and is cited, not re-encoded here.

* `FoldedFibreBoundaryData` — a **content-bearing** datum: the per-node squared characters
  `[mark]²_ζ`, the normalizer `D²`, and the derived Verlinde weights `F i = [mark]²_ζ / D²`, with the
  **normalization** `Σ_i F i = 1` as a genuine (provable, non-vacuous) content field.
* `sigma235_p2`, `sigma235_p3` — the two exact rational instances (order-2, order-3 fibre roots),
  each with `Σ F = 1` discharged sorry-free by `norm_num`.
* `q0_determined_by_sigma235_fibre_data` — the **§3b-cond conditional**: IF Habiro rigidity holds
  over the (2,3,5) fibre-root index (the **hypothesis** that the colored-WRT boundary data at the
  orders-2,3,5 fibre roots **suffices** to determine the element), THEN two elements realizing that
  data share the archimedean `q₀` value — "the fibre data forces the observable; a fit is impossible."
  Derived sorry-free from `q0_value_unique`.

**Honest scope.** A **finite** root set does NOT in general satisfy Habiro's injectivity — the
`[HabiroRigidity H Sigma235FibreRoot]` hypothesis is a *strong, non-established* restriction (the open
input), carried as the class hypothesis and **never given an instance** here (an instance would launder
a false injectivity). The conditional theorem states what *would* follow; it does not establish the
premise. Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-07-17-habiro-interpolation-wlambda.md
-- Ref: [hikami2005brieskorn] https://doi.org/10.1063/1.1834694
-- Ref: [fintushelstern1990] https://doi.org/10.1112/plms/s3-61.1.109
-- Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
-/
import QOU.BraidKnot.BWVacuumRowHabiroRigidity

namespace QOU.BraidKnot.Keystone

/-- **The folded fibre boundary datum of the candidate `F_λ = [mark]²/D²` at one fibre root.**
Content-bearing: the nine per-node squared characters `[mark]²_ζ` (`charSq`), the normalizer
`D² = Σ [mark]²_ζ` (`D2`), and the Verlinde weights `F` with the two genuine content fields
`hF : F i = charSq i / D2` and the **normalization** `hnorm : (F.map id).sum = 1`. The normalization
is the real (provable, non-trivial) claim — a bare marker `: True` would be a review failure. -/
structure FoldedFibreBoundaryData where
  /-- The nine per-node squared characters `[mark μ]²_ζ` (marks `1,2,3,4,5,6,4,2,3`). -/
  charSq : List ℚ
  /-- Exactly nine McKay nodes. -/
  hlen : charSq.length = 9
  /-- The normalizer `D² = Σ_{9 nodes} [mark]²_ζ`. -/
  D2 : ℚ
  /-- `D²` is the node-sum of the squared characters. -/
  hD2 : charSq.sum = D2
  /-- `D² ≠ 0` (the Verlinde weights are well-defined). -/
  hD2ne : D2 ≠ 0
  /-- The Verlinde weights `F_λ = [mark λ]²_ζ / D²`. -/
  F : List ℚ
  /-- `F` is the per-node quotient of the squared characters by `D²`. -/
  hF : F = charSq.map (· / D2)
  /-- **CONTENT — normalization.** `Σ_λ F_λ = 1`. -/
  hnorm : F.sum = 1

/-- **Order-2 fibre root `ζ = e^{iπ/2} = i`.** Characters `[mark]_i` for marks `1,2,3,4,5,6,4,2,3`
are `1,0,−1,0,1,0,0,0,−1`, squared `1,0,1,0,1,0,0,0,1`; `D² = 4`; `F = [1/4,0,1/4,0,1/4,0,0,0,1/4]`,
`Σ F = 1`. -/
def sigma235_p2 : FoldedFibreBoundaryData where
  charSq := [1, 0, 1, 0, 1, 0, 0, 0, 1]
  hlen := by rfl
  D2 := 4
  hD2 := by norm_num
  hD2ne := by norm_num
  F := [1, 0, 1, 0, 1, 0, 0, 0, 1].map (· / 4)
  hF := rfl
  hnorm := by norm_num

/-- **Order-3 fibre root `ζ = e^{iπ/3}`.** Characters `[mark]_{e^{iπ/3}}` for marks `1,2,3,4,5,6,4,2,3`
are `1,1,0,−1,−1,0,−1,1,0`, squared `1,1,0,1,1,0,1,1,0`; `D² = 6`;
`F = [1/6,1/6,0,1/6,1/6,0,1/6,1/6,0]`, `Σ F = 1`. -/
def sigma235_p3 : FoldedFibreBoundaryData where
  charSq := [1, 1, 0, 1, 1, 0, 1, 1, 0]
  hlen := by rfl
  D2 := 6
  hD2 := by norm_num
  hD2ne := by norm_num
  F := [1, 1, 0, 1, 1, 0, 1, 1, 0].map (· / 6)
  hF := rfl
  hnorm := by norm_num

/-- **The (2,3,5) fibre-root index.** The five roots at which the candidate `F_λ` is evaluated: the
order-2 root `i`, the order-3 root `e^{iπ/3}`, the two order-5 Galois roots `e^{iπ/5}, e^{2iπ/5}`, and
the trivial `q = 1`. A **finite** index — the idealization at the heart of the honest-scope caveat. -/
inductive Sigma235FibreRoot
  | p2        -- e^{iπ/2} = i
  | p3        -- e^{iπ/3}
  | p5m1      -- e^{iπ/5}
  | p5m2      -- e^{2iπ/5}
  | q1        -- q = 1
  deriving DecidableEq, Fintype

/-- **§3b-cond conditional — the (2,3,5) fibre data forces the `q₀` observable.**

IF Habiro rigidity holds over the (2,3,5) fibre-root index — the **hypothesis**
`[HabiroRigidity H Sigma235FibreRoot]`, i.e. that agreement on the colored-WRT boundary data at the
orders-2,3,5 fibre roots is **sufficient** to determine the Habiro element — THEN two elements `w w'`
realizing the same `(2,3,5)` fibre boundary data have the **same archimedean `q₀` value**: the fibre
data forces the observable `W_λ(q₀)`, it cannot be tuned. Derived sorry-free from
`q0_value_unique` (#3681).

**Not established:** a **finite** root set does not in general satisfy Habiro injectivity; the class
hypothesis is a strong, open restriction (carried, never instantiated). This states what *would*
follow — it is not a proof that the four computed roots pin `F_λ`. -/
theorem q0_determined_by_sigma235_fibre_data
    {H : Type*} [HabiroRigidity H Sigma235FibreRoot] (w w' : H)
    (hmatch : ∀ ζ : Sigma235FibreRoot,
        HabiroRigidity.evalRoot ζ w = HabiroRigidity.evalRoot ζ w') :
    HabiroRigidity.evalQ0 (RootIndex := Sigma235FibreRoot) w
      = HabiroRigidity.evalQ0 (RootIndex := Sigma235FibreRoot) w' :=
  q0_value_unique w w' hmatch

end QOU.BraidKnot.Keystone
