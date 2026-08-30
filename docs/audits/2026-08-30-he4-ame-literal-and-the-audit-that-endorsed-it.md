# The ⁴He AME literal: settled, and the audit that was endorsing the wrong one

**Date:** 2026-08-30
**Beans:** `qou-edt7` (the question), `qou-tknj` (adjacent — the same audit's self-reference defect)
**Trigger:** PR #6088 flagged a 1.1e-5 MeV disagreement in the ⁴He AME literal and
deliberately left it unresolved rather than silently picking a side. That was the right
call, and the answer turns out to be already in the corpus — plus one thing that was not.

## 1. The question

`computations/probes/he4_body_order_shortfall_location_probe.py:90` carries

```python
"4He": mpf("28.295673"),
```

against `28.2956624` used in the #6101 writeup. 1.06e-5 MeV apart.

## 2. The answer: `28.2956624` is correct

Three independent confirmations.

**Mass-excess route, by hand.** `B(⁴He) = 2·Δ(¹H) + 2·Δ(n) − Δ(⁴He)`, with AME2020
`Δ(¹H) = 7288.971064`, `Δ(n) = 8071.31806`, `Δ(⁴He) = 2424.91587` keV:

```
2(7288.971064) + 2(8071.31806) − 2424.91587 = 28295.662378 keV = 28.295662378 MeV
```

**The live witness.** `computations/ame-2020-binding-energies.witness.json` carries
`B_he4_MeV = 28.2956624` and `B_he4_MeV_mass_excess_route = 28.295662378`, and its
producer asserts the per-A and mass-excess columns agree for every nuclide.

**The live accessor.** `codata_constants.ame_binding_mev(2, 4)` and
`codata_constants.AME_B_HE4_MEV_VALIDATION` both evaluate to `28.2956624` at 50 dps.

## 3. The corpus already knew — the producer names this exact pair

`computations/ame_2020_binding_energies.py` exists *because* of this defect. Its docstring
(lines 14–24) lists six entries where a hand-typed witness disagreed with the vendored
AME2020 publication table:

```
B_li6   31.99405    vs  31.9939872   (+62.8 eV)
B_be8   56.49950    vs  56.4994848   (+15.2 eV)
B_he4   28.295673   vs  28.2956624   (+10.6 eV)
B_c12   92.16173    vs  92.1617352   (-5.2 eV)
B_o16  127.61931    vs 127.6193152   (-5.2 eV)
B_he3    7.718043   vs   7.71804132  (+1.7 eV)
```

and records that AME's own uncertainty on `B(⁴He)` is **0.8 eV**, so a 10.6 eV gap is
**~13σ — not a rounding artifact**. The producer routes the witness through
`codata_constants.ame_binding_mev(Z, A)` so it is derived from the publication table
rather than hand-maintained.

So the *source* was fixed. The **consumers were never migrated**: 82 live
(non-`_deprecated/`) files still hardcode `28.295673` or `28.295674`, including 11 under
`computations/deltalambda/` and 20 under `computations/probes/`.

## 4. The thing that was NOT already known: the audit was endorsing the stale literal

`computations/audits/hardcoded_literal_audit.py` is the detector for exactly this class —
it imports `codata_constants` at runtime and flags any `computations/` literal that matches
a registered constant. Its **committed witness is stale**, and the staleness inverts its
verdicts for the whole ⁴He family:

| | committed witness | fresh run (2026-08-30) |
|---|---|---|
| `registry_value` for `AME_B_HE4_MEV_VALIDATION` | **`28.295673`** | **`28.2956624`** |
| hits against that constant | 82 | 112 |
| rows | 263 | 364 |
| `i9_violation` / `ok_acknowledged_anchor` | 248 / 15 | 351 / 13 |
| total hits across violations | — | 778 |

Because the recorded reference was the stale value, **12 files hardcoding `28.295673` were
reported at `rel_err 0.0`** — i.e. the audit certified them as matching the registry
*exactly*. Against the live registry they are wrong by 10.6 eV. The remaining 31 sites
spelling `28.295674` were scored `3.534e-8` against the wrong reference too.

This is the generic hazard, not a one-off: an audit that captures its reference values into
a committed witness will keep certifying the old reference after the source of truth moves.
The audit script is fine; the artifact went stale under it.

**Fixed here** by re-running the producer and committing the refreshed witness. The
raw-float64 ratchet is green after the refresh (exit 0, no NEW dirty entries); the three
raw-float64 fields the producer warns about in its own `assertions` block are pre-existing
in both the old and new witness and are not introduced by this refresh.

## 5. What this does NOT change

**Nothing in the binding-magnitude arc.** 1.06e-5 MeV is 3.7e-7 relative. The assembly
defect that `qou-edt7` is about is 30 %+, and the trilemma (multiplicative forces `b₃ < 0`;
pairwise-additive forces `b₃ = 0`; nature gives `b₃ > 0`) holds identically under either
literal. No conclusion, in #6088 or #6101, moves.

## 6. What is left open

The **82-file consumer migration** to `codata_constants.AME_B_HE4_MEV_VALIDATION`. Not
swept here, deliberately: it touches long-compute producers, and a sweep launched off a
grep count is the failure mode AGENTS.md warns about directly. The refreshed audit witness
is now an accurate list of the 351 violating scripts, which is the right input to scoping
that work — the point of this change is to make that list *true*, not to drain it.
