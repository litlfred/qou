import QOU.MathlibExt.MacdonaldTelescopeGeneralX

/-!
# QOU.MathlibExt.WenzlCandidateNormalisation — the `X = 0` candidate weights sum to one

`computations/hecke/tau_weights_vs_wenzl_schur_probe.py` (merged in the
Geck–Pfeiffer arc) proposes

  `c_λ = (1 - Q)^n · schurElement(Q, 0, λ)`

as the canonical trace's Wedderburn weight, and checks two things: a **Tier 1**
normalisation `Σ_λ f^λ c_λ = 1`, symbolically for `n = 1 … 8`; and a **Tier 2**
per-block comparison, exact for `n ≤ 3`.

This file proves **Tier 1 for every `n`**, in Lean, so the probe's numeric range
stops being the limit on that half.

## It is a corollary, not new mathematics

`QOU.MathlibExt.MacdonaldTelescopeGeneralX.telescope_generalX` already proves the
hook telescope for **all** `X` (the polynomial-identity argument: both sides are
polynomials in `X` agreeing on the infinite set `{Q^{r+1}}`).  Evaluating it at
`X = 0` and clearing `(1 - Q)^n` is the whole content here.

That machinery was found by corpus-grep rather than rebuilt — the telescope, the
List/YoungDiagram carrier bridge, and the polynomial lift were all already in the
tree, sorry-free.

## What this does and does not settle

It settles that the candidate weight system satisfies the **same single linear
constraint** that `QOU.Hecke.TwBasis.sum_dim_mul_traceWeight` proves for `τ`'s
actual weights (`Σ_λ d_λ c_λ = 1`, from `τ(1) = 1`).

It does **not** identify the two systems.  One linear constraint cannot pin a
whole weight vector, which is exactly why the probe's Tier 2 is a separate and
strictly stronger check — and why that check, being per-block, still reaches only
`n ≤ 3`.  Do not read this theorem as the Wenzl identification.

## §7c note: the `ℝ` here is forced, not gratuitous

`check-sidecars.sh` flags this file `base-ring-minimal` — *"ℝ in type but no
archimedean construct"*.  That is a **false positive**, and the reason is worth
recording rather than silently ignoring.

The `ℝ` is not a choice: `telescope_generalX` is stated over `ℝ` and takes
`1 < Q`, and its proof runs through `StrictMono` and an infinite subset of `ℝ`.
Generalising this file would mean generalising that theorem, which is a
different piece of work.  The ordering hypothesis `1 < Q` *is* the §7c
archimedean tell, and it is present.

The checker misses it because its `WEAK` pattern is `(0\s*<|<\s*1|≤|≥)` — it
matches the idioms `0 < x` and `x < 1` but **not `1 < x`**, which is this
corpus's substrate-regime idiom (`schurElement_ne_zero (hQ : 1 < Q)`, and the
whole telescope development).  Measured over the library tree: **13 other files**
are flagged for exactly this reason.

Adding `1\s*<` to `WEAK` was considered and **rejected**: of those 13, four
(`MolienFakeDegreeGeneralN`, `HeckeGramFactorial`, `HeckeGenericSemisimple`,
`H2TraceForm`) also declare a generic ring, so they would flip from
`base-ring-minimal` to `MIXED` — *"split into two files per §7c"* — which is a
worse verdict and the wrong edit for them.  The script's own comments record
three separate rounds of exactly that over-firing (beans `qou-mr3q`,
`qou-akb4`, `qou-aemx`), and this would have been a fourth.

## References

- [wenzl1988] Wenzl, "Hecke algebras of type $A_n$ and subfactors," Invent. Math. 92.
- [macdonald1995] Macdonald, *Symmetric Functions and Hall Polynomials*, §I.3.
-/

namespace QOU.MathlibExt.WenzlCandidateNormalisation

open QOU.MathlibExt.WenzlSchurElement
open QOU.MathlibExt.MacdonaldTelescopeGeneralX

/-- **The candidate weights sum to one, for every `n`.**

    `Σ_{|ν| = n} f^ν · (1 - Q)^n · schurElement Q 0 ν.rowLens = 1`.

    The `X = 0` specialisation of `telescope_generalX`, with `(1 - Q)^n`
    cleared. -/
theorem sum_dim_candidateWeight_eq_one (n : ℕ) (Q : ℝ) (hQ : 1 < Q)
    (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) :
    (∑ ν : {ν : YoungDiagram // ν.cells.card = n},
        (QOU.Mathlib.numStandardYoungTableaux ν.1 : ℝ)
          * ((1 - Q) ^ n * schurElement Q 0 ν.1.rowLens))
      = 1 := by
  have hne : (1 : ℝ) - Q ≠ 0 := sub_ne_zero_of_ne (ne_of_lt hQ)
  have h := telescope_generalX n Q 0 hQ hgen
  calc (∑ ν : {ν : YoungDiagram // ν.cells.card = n},
          (QOU.Mathlib.numStandardYoungTableaux ν.1 : ℝ)
            * ((1 - Q) ^ n * schurElement Q 0 ν.1.rowLens))
      = (1 - Q) ^ n * ∑ ν : {ν : YoungDiagram // ν.cells.card = n},
          (QOU.Mathlib.numStandardYoungTableaux ν.1 : ℝ)
            * schurElement Q 0 ν.1.rowLens := by
        rw [Finset.mul_sum]
        exact Finset.sum_congr rfl fun ν _ => by ring
    _ = (1 - Q) ^ n * ((1 - (0 : ℝ)) / (1 - Q)) ^ n := by rw [h]
    _ = 1 := by
        rw [sub_zero, div_pow, one_pow]
        field_simp

end QOU.MathlibExt.WenzlCandidateNormalisation
