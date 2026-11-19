import Mathlib.Data.Real.Basic
import QOU.Shared.MarkovTraceClaim

/-!
# QOU.BraidsAndKnots.wenzl_qmn_synergy

**Canonical declaration** for content block Wenzl-qmn synergy.

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.

Note: the chapter-dir uses singular `QOU.BraidKnot` for most blocks;
this plural `QOU.BraidsAndKnots` namespace was inherited from existing
`.ts` lean.ref URIs (a pre-existing convention drift).
-/

namespace QOU.BraidsAndKnots


/-- Abstract context for the `wenzl_qmn_synergy` claim — manuscript-named
    typed fields below; the `holds` field carries the `Prop`-valued
    claim of the lemma. -/
class WenzlQmnSynergyContext extends QOU.Shared.MarkovTraceContext where
  /-- Speedup factor of Wenzl bridge vs linear-system solve.

      Kept at `ℝ` deliberately (§7c): the speedup fields are *measured*
      wall-clock ratios and their sub-claims are order comparisons
      (`10000 ≤ …`), which is archimedean content sitting after the
      substrate→archimedean wall.  Only the trace fields below move to the
      inherited generic ring. -/
  wenzl_speedup : ℝ
  /-- Speedup factor of q-MN vs Hoefsmit characters. -/
  qmn_speedup : ℝ
  /-- Combined speedup factor (`= wenzl_speedup · qmn_speedup`). -/
  combined_speedup : ℝ
  /-- Manuscript sub-claim (i) — Wenzl-bridge speedup `≥ 10⁴×`. -/
  claim_i_direct_verification_wenzl : 10000 ≤ wenzl_speedup
  /-- Manuscript sub-claim (ii) — q-MN speedup `≥ 10²×`. -/
  claim_ii_mass_formula_compute : 100 ≤ qmn_speedup
  -- 🛑 SUB-CLAIM (iii) REMOVED 2026-09-07, not encoded: it is a
  -- knot-selection route, and those are ruled out.
  --
  -- It read: "Atom-knot identification path for ⁶Li, ⁷Li via enumerating
  -- hyperbolic knots and comparing `tr_M(β_K)` against the AME binding ×
  -- hyperbolic-volume ratio", carried as
  --
  --     claim_iii_atom_knot_identification : Prop
  --     claim_iii_atom_knot_identification_holds : claim_iii_atom_knot_identification
  --
  -- a field typed with the *universe* `Prop` plus its own witness, so the
  -- instance chose the proposition and `⟨True, trivial⟩` discharged it.
  --
  -- The obvious repair — carry the census and the AME ratio as fields and
  -- state the match — is the wrong one here.  Owner ruling 2026-09-05, "NO
  -- knot-selection routes allowed"
  -- (docs/audits/2026-09-05-binding-route-consolidation-no-knot-selection.md):
  -- choosing a knot from a census so that its volume reproduces a measured
  -- binding is fitting by selection.  No continuous parameter is tuned and
  -- it is still a fit.  ⁶Li and ⁷Li are named in the sub-claim and are two
  -- of the three atoms the census route left as GAP rows precisely because
  -- "no census knot/link with Vol ≈ B_AME/m_e yet found" — the gap is the
  -- proof that the selection was made against the data.
  --
  -- Encoding it would formalise a retired route as a live class field, so
  -- it is dropped from the class and from the conclusion of
  -- `wenzl_qmn_synergy` below.  The five surviving sub-claims are the
  -- speedup bounds and the two trace identities, none of which selects
  -- anything.  Nothing else in this file changes and no number moves.
  /-- Manuscript boxed identity — Combined speedup is the product of
      orthogonal speedups, bounded below by `10⁶×`. -/
  claim_combined_speedup_bound :
    combined_speedup = wenzl_speedup * qmn_speedup ∧
    1000000 ≤ combined_speedup
  -- 🛑 SUB-CLAIMS (iv) AND (v) REMOVED 2026-11-15: they were false.
  --
  -- They read `trM_Tw = z ^ lengthW` and `wenzlSum = z ^ lengthW`, "on any
  -- canonical permutation braid", with `z` described in convention C.  The
  -- length rule `tr_M(T_w) = z^{ℓ(w)}` holds only when the reduced word uses
  -- each generator at most once.  It fails for `w = s₁s₂s₁`: under
  -- convention D, `tr_M(T_w) = h z² + z = q³(q⁴+1)/(q²+1)²`, while
  -- `z³ = q⁹/(q²+1)³`.  The corpus already records the rule as retracted
  -- (`prop:corrected-markov-trace`, `frobenius-gram-matrix.md`).  Carrying it
  -- as a class field made every instance assert a false identity, so the
  -- fields and the matching conjuncts of `wenzl_qmn_synergy` are dropped.
/-- **Proposition statement** (from manuscript):

The Wenzl-bridge ([y-lambda-closed-form](#prop:y-lambda-closed-form-wenzl-bridge))
gives $y_\lambda(q)$ as a closed q-rational expression in $\sqrt q$
in $O(p(n) \cdot \max\text{hooks})$ time, while q-Murnaghan-Nakayama
([Halverson-Ram 1995, Wenzl q-MN as in `q_mn_canonical.py`]) gives
$\chi_\lambda(T_w; q)$ for canonical permutation braids $T_w$ in
$O(n^2)$ time.*

*Combining them gives the Markov trace*

$$
  \mathrm{tr}_M(T_w) \;=\; \sum_{\lambda \,\vdash\, n} y_\lambda(q) \cdot \chi_\lambda(T_w; q)
$$

*on canonical permutation braids in $O(p(n) \cdot (\max\text{hooks} + n^2))$
time — far faster than the Hoefsmit-seminormal path
($O(p(n) \cdot \dim_\lambda^2 \cdot \ell(w))$).*

## Why this is significant

Three orthogonal speedups combine:

| Quantity | Old path | New path | Speedup |
|---|---|---|---|
| $y_\lambda(q)$ | Linear-system solve, sympy 20-min timeout @ n=5 | Wenzl-bridge, ~0.3 s @ n=12 | $\sim 10^4 \times$ |
| $\chi_\lambda(T_w; q)$ canonical | Hoefsmit $O(\dim_\lambda^2 \cdot \ell(w))$ | q-MN $O(n^2)$ | $10^2 \times$ at $n = 12$ |
| $\mathrm{tr}_M$ on closed braid | Direct seminormal matrix-trace | $\sum y_\lambda \chi_\lambda$ via above | combined $10^6 \times$ |

For atom-knot identification at $n = 18$ ($p(n) = 385$, $\max\dim_\lambda \approx 1000$) or $n = 21$ ($p(n) = 792$, $\max\dim_\lambda \approx 5000$),
this drops the per-isotope compute time from

    The Lean encoding below states the manuscript claim over a context class and discharges it from the class's fields (§3b-conditional). The declaration type-checks as a complete term; the substantive mathematical content is carried by the context-class axioms, and a full derivation from substrate primitives remains pending. -/
-- Ref: [leitner2026] quantum-observable-universe/braids-and-knots/wenzl-qmn-synergy.ts
def wenzl_qmn_synergy [ctx : WenzlQmnSynergyContext] :
    10000 ≤ ctx.wenzl_speedup ∧
    100 ≤ ctx.qmn_speedup ∧
    (ctx.combined_speedup = ctx.wenzl_speedup * ctx.qmn_speedup ∧
     1000000 ≤ ctx.combined_speedup) := by
  refine ⟨ctx.claim_i_direct_verification_wenzl, ctx.claim_ii_mass_formula_compute,
    ctx.claim_combined_speedup_bound⟩

end QOU.BraidsAndKnots
