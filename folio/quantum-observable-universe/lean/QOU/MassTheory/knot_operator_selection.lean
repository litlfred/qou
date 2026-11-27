import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Real.Basic

/-!
# QOU.Archimedean.knot_operator_selection

**Proposition** ([`prop:knot-operator-selection`](../../../predicted-spectra/knot-operator-selection.md)):
*Knot operator selection via the Frobenius dual.*

Let `(C, A, τ)` be a QOU with archimedean realisation `Hᵣ(q)`. Then

(i) **Spectral decomposition.** The Lagrangian endomorphism `Φ`
    decomposes via Schur orthogonality as `tr(Φ) = Σ_λ d_λ(q)·tr(Φ_λ)`.
(ii) **Multi-channel pair production.** The categorical action of two
    photons equals the per-channel sum `Σ_λ d_λ·tr_λ(…)`.
(iii) **Frobenius demand–supply.** The Frobenius pairing is
    non-degenerate (kernel dimension `0`).
(iv) **Minimum-action selection.** Among all on-shell `Φ_alt`, the
    selected `Φ` minimises `|tr(Φ)|`.

## 2026-09-02 — the previous docstring described a repair that was never made

This file's own header used to say:

> *"The class carries only the **categorical / Hecke data** … It does **not**
> carry the four conclusions as fields (the previous version did, then
> projected them — the self-assuming projection forbidden by AGENTS.md
> §3b-cond item 5)."*
>
> *"`knot_operator_selection` states the genuine four-part conjunction over
> that data and **ends in `sorry`** (disposition B)."*

Neither sentence described the code beneath it. `KnotOperatorSelectionContext`
**did** carry the four conclusions, in a single field docstring'd *"Operator
selection conclusion."*, and the theorem ended not in `sorry` but in
`exact ctx.operator_selection` — the projection, under prose naming the rule
it violates. `git log` shows the file was created in **one** commit
(`eb0f267e905`) carrying both halves, so this was never a repair that
regressed; the description and the defect were written together.

## And "disposition B" would not have been sound either

The docstring's proposed fix — drop the field, state the conjunction over the
class data, end in `sorry` — puts a `sorry` on a statement that is **false**.
With the data as freely-chosen fields, `n_partitions := 0`, `tr_Phi := 1`,
`tr_Phi_lambda := fun _ => 0` refutes conjunct (i): `1 = 0`. Measured
`lean`-direct, exit 0, on exactly that instance. A `sorry` on a refutable
statement is worse than the projection it would replace, because it reads as
"true, not yet proved".

The four claims are about *the* `Φ` arising from a QOU with its archimedean
realisation, not about arbitrary reals — and this development has no such
construction to quantify over.

## Disposition: name it, assert nothing (AGENTS.md §1a, disposition 3)

`knot_operator_selection` is now a **`Prop`-valued definition over
caller-supplied data**. It states the four-part claim exactly, and asserts
none of it. There is no class, no projection, and no `sorry` on a refutable
statement.

A caller who has a genuine QOU realisation takes
`knot_operator_selection …` as an ordinary hypothesis, and it constrains their
data because the data are theirs.

**What is still open**, stated rather than implied: all four parts. The
Wedderburn / Schur-orthogonality decomposition (i)–(ii), the QUO-1
non-degeneracy of the Frobenius pairing (iii), and the minimum-action
variational selection (iv) each need semisimple-algebra representation theory
and the Markov-trace projection machinery, which the `QOU` library and Mathlib
do not yet carry. Nothing here constructs `Φ`, the isotypic decomposition, or
the Frobenius pairing.

Bean `qou-z9ws`. -/

namespace QOU.Archimedean

/-- **The claim of `prop:knot-operator-selection`**, as a proposition over
caller-supplied data.

* `trPhi = Σ_{λ < nPartitions} trPhiLambda λ` — (i) spectral decomposition;
* `actionPair = channelSum` — (ii) multi-channel pair production;
* `pairingKernelDim = 0` — (iii) Frobenius non-degeneracy;
* `actionPhi ≤ actionAlt Φ_alt` for every on-shell `Φ_alt` — (iv)
  minimum-action selection.

**Named, not asserted.** See the module docstring for why neither a projection
nor a `sorry` is the honest form here. -/
-- Ref: [wenzl1990] https://doi.org/10.1007/BF02097372 (Schur orthogonality / Markov-trace projection)
-- Ref: [leitner2026] quantum-observable-universe/predicted-spectra/knot-operator-selection.md
def knot_operator_selection {V : Type}
    (nPartitions : ℕ) (trPhi : ℝ) (trPhiLambda : ℕ → ℝ)
    (actionPair channelSum : ℝ) (pairingKernelDim : ℕ)
    (actionPhi : ℝ) (actionAlt : (V → V) → ℝ)
    (isOnShell : (V → V) → Prop) : Prop :=
  trPhi = (Finset.range nPartitions).sum (fun l => trPhiLambda l) ∧
  actionPair = channelSum ∧
  pairingKernelDim = 0 ∧
  (∀ altPhi : V → V, isOnShell altPhi → actionPhi ≤ actionAlt altPhi)

/-- **The claim is refutable at freely-chosen data**, which is why it is named
rather than carried as a `sorry`.

At `nPartitions = 0`, `trPhi = 1`, `trPhiLambda = fun _ => 0`, conjunct (i)
reads `1 = 0`. Recorded as a theorem so the module docstring's argument is
checked rather than asserted, and so a later attempt to "finish" this file by
adding a `sorry` over free data fails against a standing counterexample. -/
-- Ref: [leitner2026] quantum-observable-universe/predicted-spectra/knot-operator-selection.md
theorem not_knot_operator_selection_of_free_data :
    ¬ knot_operator_selection (V := ℕ) 0 1 (fun _ => 0) 0 0 0 0
        (fun _ => 0) (fun _ => True) := by
  rintro ⟨h, -, -, -⟩
  simp at h

end QOU.Archimedean
