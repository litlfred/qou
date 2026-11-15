/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MathlibExt.HeckeToTemperleyLieb
import QOU.IwahoriHecke.CoxeterCarrierEquiv

/-!
# The TL-ideal carrier mismatch is one matrix-equality lemma, and it is closed here

Bean `qou-jb7k` records the obstruction to stating the ideal equality

    ⟨U_i U_j U_i − v²·U_i⟩  =  rad(tr_M)

as a **carrier mismatch**: `HeckeToTemperleyLieb.tlKernel` is a
`TwoSidedIdeal (HeckeAlgebra R (v ^ 2) M)`, while `wtrace`, `traceRadicalIdeal` and every
result of the `H_n(q)/rad(wtrace)` arc live on `QOU.SchurWeyl.Hecke K q q⁻¹ n`. Two
different types, so the two ideals could not even be compared.

**Measured 2026-09-27: the bridge was already built, and the residual gap is one lemma.**

`QOU.IwahoriHecke.CoxeterCarrier.skeinCoxeterEquiv` — sorry-free, needing only `[Field K]`
and `q ≠ 0` — is exactly

    QOU.SchurWeyl.Hecke K q q⁻¹ n  ≃ₐ[K]  HeckeAlgebra K (q ^ 2) (AMat n)

i.e. the `tlKernel` carrier with `v := q` and `M := AMat n`. Its own docstring says the
left algebra is *"the one carrying the proved-unique Ocneanu trace
(`QOU.SchurWeyl.MarkovTraceInstance.wtrace`)"* — it was built for this (bean `qou-0fmb`).

What was genuinely missing is that `HeckeToTemperleyLieb` states its results over
`IsTypeADiagram M Adj` and inhabits that hypothesis only at its **own** type-A matrix
`coxeterFin`, never at `CoxeterCarrierEquiv`'s `AMat`. The two are equal —

* `coxeterFin i j = if i = j then 1 else if adjFin i j then 3 else 2`
* `AMat n i j = if i = j then 1 else if (j:ℕ)+1 = i ∨ (i:ℕ)+1 = j then 3 else 2`

— the same disjunction with its disjuncts swapped, since
`adjFin i j := i.val + 1 = j.val ∨ j.val + 1 = i.val`. That is `coxeterFin_eq_AMat` below,
and transporting the existing witness along it gives `isTypeADiagram_AMat`.

## What this closes, and what it does NOT

**Closed:** the mismatch. `tlKernelPulled` below has type
`TwoSidedIdeal (QOU.SchurWeyl.Hecke K q q⁻¹ n)` — the *same* type as
`QOU.QBeta.MarkovTraceQuotient.traceRadicalIdeal (wtrace …)`. That this typechecks is the
whole content: the two ideals are now comparable, so the equality is **statable**.

🛑 **NOT closed: the mathematics.** Whether the two ideals are *equal* — whether the TL
relators generate the whole Markov-trace radical — is untouched here and is the live open
problem. Nothing below asserts it, and no vacuous theorem is offered in its place; the
deliverable is a type, not a proof.

Also not touched: `HeckeToTemperleyLieb`'s own remaining item (that `tlKernel` is generated
*by the relators*, which its docstring separates from `heckeTLEquiv`), and the tower
compatibility `CoxeterCarrierEquiv` explicitly disclaims — it is one equivalence per fixed
`n`, and nothing here makes it commute with the level inclusions.

## 🛑 The dimension result does NOT close the equality, and the reason is circularity

Now that the two ideals are comparable, the tempting next step is a counting argument:
`finrank_traceQuot_eq_catalan` gives `dim (H_n/rad(wtrace)) = catalan (n+1)`, and
`dim TL_n(δ) = catalan n`, so one inclusion plus equal codimension would force equality.
**That route does not work, for two independent reasons — measured 2026-09-27, before
attempting it.**

1. **`dim TL_n(δ) = catalan n` is not available at general `n` in this corpus.** It is proved
   as an algebra fact only at `n = 2` (`tl2Basis`, `= 2`) and `n = 3` (`tl3Basis`, `= 5`);
   `TemperleyLiebNormalForm`'s own docstring says the closure lemma that would give the
   general case "is not done". So there is no general-`n` dimension to compare against.
2. **Supplying it from this arc is circular.** `TraceRadicalNondegenerate`'s
   `traceRadical_eq_zero_of_algEquiv_pi_matrix` is the packaged route to the `⊇` half, and
   its own docstring reduces that half to *"(i) the Wedderburn decomposition [of `TL_n(δ)`],
   still open"*. The decomposition this arc has is `traceQuotEquiv`, which decomposes
   `H_n(q)/rad(wtrace)` — a **different algebra**. Feeding it in as `TL_n(δ)`'s decomposition
   assumes `H_n/rad(wtrace) ≅ TL_n(δ)`, which is the equality being proved.

So both halves remain open. The `⊆` half is the concrete one — the corpus has
`tlRelator_mem_ker` (a relator inside `tlKernel`) but **no** theorem placing the relators in
`rad(wtrace)`. The `⊇` half needs `TL_n(δ)`'s own structure, independently of this arc; the
`TemperleyLiebSpanning` docstring puts it as needing `TL_n(δ)` semisimple.

### The `⊆` half is SHARPER than "the concrete one" — it is exactly ONE statement

`rad(wtrace)` is not an opaque ideal: it is **characterised**, at general `n`, sorry-free, by
`QOU.SchurWeyl.WtraceRadicalTwoRow.mem_rad_iff_twoRow_blocks_vanish` —

    (∀ b, wtrace q hq0 hq2 n (x * b) = 0)
      ↔ ∀ (d : YoungDiagram) (hd : d.cells.card = n + 1), d.rowLen 2 = 0 →
          seminormalRep q hq0 hq2 n hd x = 0

i.e. **`rad(wtrace)` is exactly the three-row part**: membership is equivalent to being killed
by every at-most-two-row seminormal block. (Convention D is what makes this true — the Ocneanu
weight of a three-row shape vanishes at `z = q³/(q²+1)`, so those blocks are invisible to the
form and impose no condition.)

Substituting that characterisation, the `⊆` half of the ideal equality stops being "show the
relators lie in some radical" and becomes a single concrete representation-theoretic claim:

> **for every shape `d` with `d.rowLen 2 = 0`, the seminormal representation kills the
> Temperley–Lieb relator.**

That is the classical statement that the at-most-two-row irreducibles of `H_n(q)` factor through
the TL quotient — equivalently that the three-strand antisymmetriser acts as zero on a shape iff
that shape has at most two rows.

**It is not in the corpus, and the near-miss is worth naming so it is not mistaken for it.**
`QOU.QBeta.TemperleyLiebTower.conventionD_kills_antisymmetriser` is about the Markov **weights**
— it derives `y₁₃ = 0` from the convention-D pin — and says nothing about how the
antisymmetriser acts in a representation. Weight-level vanishing and representation-level
vanishing are different claims; only the first is proved.

This paragraph **sharpens** the one above it rather than replacing it: "no theorem places the
relators in `rad(wtrace)`" is still literally true. What changed is that the target is now a
named, self-contained statement about `seminormalRep` on two-row shapes, with no reference to
ideals or radicals at all.

Recorded here rather than in a bean because this is the file a reader reaches *after* the
carrier stops being the obstacle, and the counting argument is what they will reach for next.

-- Ref: [leitner2026] beans qou-jb7k, qou-0fmb, qou-0cyu.
-/

namespace QOU.IwahoriHecke.TLCarrierBridge

open QOU.MathlibExt.HeckeToTemperleyLieb QOU.MathlibExt.TemperleyLieb
open QOU.MathlibExt.IwahoriHecke QOU.IwahoriHecke.CoxeterCarrier

/-- **The two type-A Coxeter matrices agree.** `HeckeToTemperleyLieb.coxeterFin` and
`CoxeterCarrierEquiv.AMat` are the same function on `Fin n`; they differ only in the order
of the two disjuncts of the adjacency test. -/
theorem coxeterFin_eq_AMat (n : ℕ) : (coxeterFin (n := n)) = AMat n := by
  funext i j
  simp only [coxeterFin, AMat, adjFin, CoxeterMatrix.Aₙ, Matrix.of_apply]
  split_ifs <;> first | rfl | tauto

/-- **`IsTypeADiagram` at `AMat`**, transported from `isTypeADiagram_coxeterFin` along
`coxeterFin_eq_AMat`. This is the hypothesis `HeckeToTemperleyLieb` takes everywhere, and
the reason its results could not previously be read at `CoxeterCarrierEquiv`'s matrix. -/
theorem isTypeADiagram_AMat (n : ℕ) : IsTypeADiagram (AMat n) (adjFin (n := n)) :=
  coxeterFin_eq_AMat n ▸ isTypeADiagram_coxeterFin

/-- **The TL quotient map, read on the skein carrier.**

`heckeToTL` composed with `skeinCoxeterEquiv`, so its domain is the algebra carrying
`wtrace` rather than the Coxeter-presentation algebra. -/
noncomputable def skeinToTL {K : Type*} [Field K] {q δ : K} (hq : q ≠ 0) (n : ℕ)
    (hδ : q * δ = q ^ 2 + 1) :
    QOU.SchurWeyl.Hecke K q q⁻¹ n →ₐ[K] TemperleyLiebAlgebra K δ (adjFin (n := n)) :=
  (heckeToTL (v := q) (δ := δ) (M := AMat n) (Adj := adjFin) hδ
      (isTypeADiagram_AMat n)).comp
    (skeinCoxeterEquiv q hq n).toAlgHom

/-- **`tlKernel`, pulled back to the skein carrier — the point of this file.**

Its type is `TwoSidedIdeal (QOU.SchurWeyl.Hecke K q q⁻¹ n)`, which is *the same type as*
`traceRadicalIdeal (wtrace q hq0 hq2 n) (wtrace_cyclic …)`. That this typechecks is what
closes bean `qou-jb7k`'s carrier mismatch.

🛑 It does **not** say the two ideals are equal. That is the open problem. -/
noncomputable def tlKernelPulled {K : Type*} [Field K] {q δ : K} (hq : q ≠ 0) (n : ℕ)
    (hδ : q * δ = q ^ 2 + 1) :
    TwoSidedIdeal (QOU.SchurWeyl.Hecke K q q⁻¹ n) :=
  TwoSidedIdeal.ker (skeinToTL hq n hδ).toRingHom

end QOU.IwahoriHecke.TLCarrierBridge
