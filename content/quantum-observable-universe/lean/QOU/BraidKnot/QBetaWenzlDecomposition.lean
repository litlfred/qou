import QOU.HeckeAlgebra.JonesMarkovWenzl
import Mathlib.Data.Real.Basic

-- Declarations here are nested one namespace deeper than the module's
-- parent so this module and QOU.BraidKnot.H3HeckeIdempotents
-- can be imported together: both declared the same fully-qualified
-- name(s), and Lean rejects the second import with "environment already
-- contains" (bean `qou-kfcl`). Nothing imports this module, so the
-- nesting costs no consumer.
namespace QOU.BraidKnot.QBetaWenzlDecomposition

open QOU.HeckeAlgebra.JonesMarkovWenzl

/--
The q-factorial `[n]_q!`.
-/
noncomputable def qFact (n : ℕ) (q : ℝ) : ℝ :=
  if n = 0 then 1
  else (List.range n).foldl (fun acc i => acc * qInteger (i + 1) q) 1

/--
The alternating Wenzl weight `W_n(q) = 1 / [n]_q!`.
-/
noncomputable def wenzlAltWeight (n : ℕ) (q : ℝ) : ℝ :=
  1 / qFact n q

/--
The `Q_beta` N=3 brane-tower truncation structural residual coefficient,
`-2 - (3/2) * W_4(q)`.

**Provenance, and a corrected precision claim (2026-09-04, bean `qou-floy`).**
This docstring asserted the identification was "exactly" this form, "yielding an
error of -0.0005 ppm, significantly below the 0.0094 ppm Kashiwara N=3 ceiling".
Both halves need scoping:

* The **-0.0005 ppm** figure is not reproducible. A 216-combination sweep over
  the q0 pin (retired / CODATA-2022 muon / proton), `m_e`, the `Q_AME` source,
  the Markov convention, the `hbar_q` definition and three coefficient variants
  puts the closest candidate at **+0.0046 ppm** — ten times the quoted figure's
  own magnitude away. The committed witness's **-0.0257 ppm** IS reproducible,
  uniquely and to 4.2e-9, at: retired pin A, `m_e = 0.51099895000`, a
  **hardcoded** `Q_AME = 0.78233341`, **convention C**, balanced brackets.
* That recipe names what has since changed. The producer now computes `Q_AME`
  from CODATA rather than hardcoding it, and **convention D has been canonical
  since 2026-08-09**. Re-measured under D at the canonical proton pin, the
  residual is **+600.97 ppm** — roughly 470x *worse* than the N=2 baseline
  (1.27 ppm) this claim was compared against, and ~1.2e6 times the quoted error.

The convention is the cause, not the pin: C to D moves the residual ~2760x,
while the pin moves it 0.03 ppm in either convention.

**Scope (a), not (b).** This is a scope-limited negative: the expression, at the
canonical convention, does not reproduce `Q_beta` to the claimed precision. It
does **not** exclude the Wenzl weight `1/[4]_q!` as an ingredient of a `c_3`
closure — no proved invariant forbids it — and the `F_3` truncation reading is
untouched. The definition is kept for that reason; only the precision claim
attached to it was wrong.
-/
noncomputable def q_beta_c3_wenzl_coefficient (q : ℝ) : ℝ :=
  -2 - (3/2 : ℝ) * wenzlAltWeight 4 q

/--
The Wenzl correction genuinely moves the coefficient off `-2`: whenever the
alternating Wenzl weight `W_4(q)` is nonzero, `c_3(q) ≠ -2`.

**This replaces a tautology (2026-09-04, bean `qou-floy`).** The previous
declaration here was

    theorem q_beta_c3_wenzl_decomposition_exact {q : ℝ} :
      q_beta_c3_wenzl_coefficient q = -2 - (3/2 : ℝ) * wenzlAltWeight 4 q := by
      rfl

i.e. `def X := E` followed by `theorem X = E := rfl`. It restates the definition
and says nothing falsifiable about `Q_beta` — banned by AGENTS.md §"Strict Lean
Discipline" rule 5, and doubly misleading because its docstring claimed the full
`Q_beta` ansatz was being formally asserted, which no part of this file models.

The statement below is small but has content: it can fail (at any `q` where
`W_4(q) = 0`), and it is the one structural fact the definition does support —
that `c_3` is displaced from the bare `-2` scalar exactly when the 4-strand
Wenzl weight does not vanish. Nothing here asserts the numerical precision
claim; see the corrected docstring above for the measurement.
-/
theorem q_beta_c3_wenzl_coefficient_ne_neg_two {q : ℝ}
    (hW : wenzlAltWeight 4 q ≠ 0) :
    q_beta_c3_wenzl_coefficient q ≠ -2 := by
  unfold q_beta_c3_wenzl_coefficient
  intro h
  apply hW
  linarith

end QOU.BraidKnot.QBetaWenzlDecomposition
