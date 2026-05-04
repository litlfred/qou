# P2.1 — Migration assessment for legacy `markov_trace_symbolic_eval` callers

**Workplan task**: P2.1 (full Wedderburn channels in `crt_markov.py`).
**Branch**: `claude/tier3-math-audit-B0wyO`.
**Pair**: `prop:phi-q-tower-algebraic-stratification` (algebraic
stratification provides the conceptual structure for the wiring);
P2.2a / P2.2b commits (the actual descended + tower SW wiring).

## Summary

After P2.2a + P2.2b wired Schur-Weyl into `tower_mass_symbolic_eval`,
the question for P2.1 is: which of the remaining callers of
`markov_trace_symbolic_eval` (the legacy std-only path) should be
migrated to the new path?

**Verdict**: most legacy callers are **legitimate** uses that cannot
be migrated until the SW path's `char_kind="mn-atom"` is extended to
accept the dressed-quark mass parameters `m_pp`, `m_pn`, `m_nn`.

| Caller | Category | Migration status |
|--------|----------|------------------|
| `crt_markov.py` | Defines the function + its own legacy fallback | ✅ Legacy fallback path inside `tower_mass_symbolic_eval` is intentional; the function itself is legitimate |
| `p2_2a_descended_wiring_witness.py` | Diagnostic — explicitly compares H_3-std-only vs SW | ✅ Legitimate diagnostic; keep |
| `tower_vs_descended_witness.py` | Diagnostic — descended vs full tower comparison | ✅ Keep |
| `per_braid_tower.py` | Uses legacy as comparison baseline alongside the per-braid path | ✅ Keep |
| `gb_residue_tower.py` | Calls with non-existent `channel=` kwarg (signature mismatch — likely broken or extension required) | ⚠ Out-of-scope; needs separate review |
| `canonical_isospin_pyhecke.py` | Uses **`pyhecke.trace.markov_trace_symbolic_eval`** (Rust binding, separate module) | ✅ Different code path; not a `crt_markov` issue |
| `derived_only_extended_A12.py` | Same — uses `pyhecke.trace` | ✅ Different code path |
| `paper_six_term_isotope_sweep.py` | Docstring-only mention of `pyhecke.trace.markov_trace_symbolic_eval` | ✅ No actual call |
| `deuteron_error.py` | Production caller — but **requires** the dressed-quark differentiation that SW path doesn't yet expose | ⚠ Cannot migrate until SW path accepts `m_pp/m_pn/m_nn`; documented in-source |

## Root cause of migration limitation

The Schur-Weyl path through `global_wedderburn_sum_symbolic` uses
the **q = 1 limit of the Hecke character** via Murnaghan-Nakayama
(per parent commit `8d289273e`'s caveat: "uses Murnaghan-Nakayama
(q=1 limit of the Hecke character). The full q-deformed Hecke
character is a refinement"). The legacy `markov_trace_symbolic_eval`
preserves the full q-deformation through transfer-matrix products
plus dressed-quark differentiation through the `m_pp`, `m_pn`, `m_nn`
parameters.

For analyses that need q-deformation refinement or dressed-quark
differentiation (deuteron error, gb-residue tower), the legacy
path remains the correct choice. P2.1 migration becomes possible
only when:

1. The SW path is extended to accept `m_pp`, `m_pn`, `m_nn` (wiring
   them into `specht_character_atomic`'s atomic-braid construction),
   OR
2. The Murnaghan-Nakayama character is refined to the full
   q-deformed Hecke character (q-ribbon-tableau weights — a
   separate module per the parent's caveat).

## Action

1. **Tag legitimate-legacy callers**: docstring updates explain
   why each remains on the legacy path.
2. **gb_residue_tower.py signature mismatch**: separate review
   needed (out of P2.1 scope).
3. **Document the SW-path extension requirement**: any future
   P2.1.b would extend `global_wedderburn_sum_symbolic` to take
   `m_pp/m_pn/m_nn`; track as a follow-up workplan item.

## Status

🟡 **Assessed; bulk of "callers" are legitimate-legacy.** The
wiring done in P2.2a/b is the substantive correctness fix; P2.1
migration of additional callers is blocked on either (a) extending
the SW path's char_kind to accept dressed-quark mass parameters,
or (b) implementing the full q-deformed Hecke character. Both are
substantial follow-up work, not audit-blocking.

The leading-order mass formula (`tower_mass_symbolic_eval`) now
uses proper SW; downstream analyses that need finer information
correctly stay on the legacy q-deformation path.
