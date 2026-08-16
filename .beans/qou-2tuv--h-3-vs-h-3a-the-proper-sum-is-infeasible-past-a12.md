---
# qou-2tuv
title: 'H_3 vs H_{3A}: the proper sum is infeasible past A~12, so substitution cannot fix the heavy-atom rows'
status: todo
type: task
priority: normal
created_at: 2026-08-16T11:25:45Z
updated_at: 2026-08-16T11:43:16Z
---

## What the audit recommends, and why its Path A is not available

`docs/audits/2026-05-25-h3-vs-h3a-legacy-bug-audit.md` recommends **Path A**:
"Fix `pyhecke/atom.py` to compute Wedderburn weights dynamically from
`partitions_of(3A)` → 15+ callers fixed automatically. Path A is much cleaner."

Path A is not reachable. The H_{3A} Wedderburn sum runs over p(3A):

     A     3A          p(3A)
     1      3               3
     2      6              11
     4     12              77
    12     36          17,977
    20     60         966,467
    40    120   1,844,349,560
   418   1254   3.2e35

`mass_at_3A_proper.py` says so in its own header: *"Heavy atoms: full p(3A)
enumeration fails for 3A ≳ 35 (p(36) ≈ 17 000, dim-sum ≈ 3 × 10⁷). Any
truncation is an audit option, never the default."*

So the correct weights are computable to **A ≈ 12** and no further. Any producer
scanning beyond that — `mass_table_comprehensive` goes to **A = 418** — cannot
be fixed by substitution at all. That is a property of the mathematics, not of
the implementation.

## Where per_generator_V_hat_3A SHOULD be used

Callers whose atom range stays within A ≲ 12 can migrate; callers that scan
heavy nuclei cannot. Of the 31 files calling `atom_per_generator_volumes`, the
audit already names the A-bounded ones:

    mass_formula_6term.py            tower_isotope_absolute.py
    mass_formula_6term_mpfr_50dps.py paper_six_term_isotope_sweep.py
    catalan_binding.py               brane_tower_isospin_diagnosis.py
    multi_level_jet_sum.py           entanglement_orders.py
    adjacent_vs_full_probe.py

Those are the migration candidates. `mass_table_comprehensive.py` is NOT one —
it must instead DECLARE the approximation, which it now does (added caveat).

## Measured: how wrong are the H_3 weights?

Deuteron (A=2, 3A=6, 11 partitions — the one case cheap enough to compute both
ways in this container):

    legacy (H_3)   V_hat = [1.08022, 0.94694, 0.34000, 0.94109, 0.94310]
    proper (H_3A)  V_hat = [0.67139, 1.05511, 0.00007, 0.55166, 1.08837]

    sum ln|V|   legacy  -1.1755
                proper -10.3951      ratio 8.84

Since `B = -alpha * sum ln|V|`, the proper weights give **8.84x more binding**
at A=2. The third generator is the striking one: H_3 says 0.34, H_{3A} says
7e-05 — four orders of magnitude, and it is the dominant term in the log sum.

### What this does NOT establish

One data point is not an A-dependence. The heavy-A deficit is a ~3.5x
UNDER-prediction (B_pred/B_AME plateaus at ~0.28 for A >= 12, qou-53p1), so a
correction of this sign and order is what those rows need — but at A=2 the
model is already ~2x OVER (q-CLT D: +97.9%), and multiplying by 8.84 would make
it far worse. So the H_3 fix is **not** a uniform rescale that repairs the
table; it is a large A-dependent correction that plausibly helps heavy and
hurts light.

Getting the actual A-dependence needs the same measurement at A = 3, 4, 6, 8,
12. That is the next step and it is bounded work — p(36) = 17,977 is the
ceiling, and each point is minutes not hours.

## Not done

- The A = 3..12 sweep above.
- Migrating the nine A-bounded callers.
- `atom_mass_derived.py` (audit §6, "DO NOT TRUST OUTPUT", production-wired).
