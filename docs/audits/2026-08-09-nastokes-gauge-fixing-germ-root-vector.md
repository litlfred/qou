# NA-Stokes transverse pairing: the gauge IS fixed, and the determined value is zero

**Date:** 2026-08-09
**Bean:** `qou-prjo` (deuteron Δ_λ magnitude)
**Branch:** `claude/nastokes-gauge-fixing-2026-08-09`
**Predecessors:** PR #4798 (discretization built, gauge-underdetermined),
PR #4818 (Lean wall + Betti-additivity scope-(b)), PR #4619, PR #4817, PR #4829/#4832/#4836.

**Status:** WORK IN PROGRESS — headline result recorded; Lean + probe follow.

---

## Headline

**Yes — there is a derived principle, it fixes both gauges, and the determined
value is `c₂ = 0`, not `c₂ ≈ 1`.**

PR #4798 reported `c₂ = ‖Ω₂^⊥‖/h² ∈ [0, 897]` across "natural" germ/handle choices
and concluded O(100×) gauge freedom. That spread is **not** a genuine
under-determination: it comes from admitting choices the corpus already excludes.
Once the corpus's own conventions are applied, every admissible choice gives the
same answer, and that answer is exactly zero.

