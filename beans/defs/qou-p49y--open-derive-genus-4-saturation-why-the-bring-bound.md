---
# qou-p49y
title: 'OPEN: derive genus-4 saturation (why the Bring bound picks genus exactly 4)'
status: todo
type: task
created_at: 2026-11-22T18:27:46Z
updated_at: 2026-11-22T18:27:46Z
---

Owner 2026-11-22 (issue #8979, thread "Settle which α_em form is canonical"): leave saturation open as a bean for exploration.

Question: why does the genus bound g ≤ 4 on Bring's surface select the member with genus EXACTLY 4 (T(3,5) in the electron family T(3,3m+2) = e^(2m+1)σ₁; T(2,9) in the backup family)? The bound itself is fine; "saturation" is adopted, not derived.

Ruled out so far (all scope (a), on main):
- As curves: the compactified Milnor fibres y³=x⁵+1, y²=x⁹+1 have automorphisms of order 15, 9; S₅ has neither (QOU/AlphaEM/SaturationNotBringFibre.lean, audit 2026-11-21-alpha-em-which-form-is-canonical.md §19).
- As an S₅-invariant subsurface: would force S₅ cyclic (perm5_not_isCyclic, §20).
- Through the monodromy (order 15/18) in a finite mapping-class group with S₅: no_overgroup_of_perm5 (§20).
- S₅-equivariance tests for T(2,n): both stated (§21).

Related: qou-15sj (the [10]_q linchpin also rests on genus-4 saturation).

Leads not yet tried: a counting/extremal argument (why the maximal admissible member), a Reeb-degree or brane-tower level argument, or a non-equivariant geometric reason. Do not close while the rule is undeclared as derived.
