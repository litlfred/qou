# Phase 5q closed-form tr_M — reconciliation audit

**Date:** 2026-05-25
**Branch:** `claude/track-c-phase5q-reconciliation-2026-05-25`
**Track:** C (VolDensity / Phase 5l closed-form wiring)
**Severity:** clarification — no correctness fix needed

## Question being reconciled

Earlier framing of Track C said the Phase 5q closed form
`closed_form_tau_M(Z, N, q, tau_p, tau_n)` (in
[`computations/closed_form_tau_M.py`](../../computations/closed_form_tau_M.py))
"disagrees with the production pipeline by ~21% relative for atoms
with at least one p-n interface" — phrasing inherited from the
script's own docstring on the `"strict_averaged"` pn_convention
bullet (now reframed per this PR).

Per
[`per-observable-100x-status.witness.json`](../../computations/per-observable-100x-status.witness.json),
the framework still misses 100× targets on m_p, m_n, Δ_pn by
~10⁹ — a 21% structural disagreement on tr_M would be a major
correctness concern if confirmed.

## Verdict — no correctness disagreement

The closed form is **machine-precision validated** against the full
slow-path empirical computation at all four anchor atoms
(D, T, ³He, ⁴He). Existing
[`closed-form-tau-M-verification-phase5q.witness.json`](../../computations/closed-form-tau-M-verification-phase5q.witness.json):

| atom | tau_M (empirical, 50 dps) | tau_M (closed form) | rel_err | speedup |
|---|---|---|---:|---:|
| D    | 0.7280918153466761555460… | 0.7280918153466761555460… | 5.0e-50 | 113× |
| T    | 0.2525173728357417721182… | 0.2525173728357417721182… | 7.4e-50 | 14,037× |
| ³He  | 0.4436642078120950382745… | 0.4436642078120950382745… | 9.9e-50 | 17,635× |
| ⁴He  | 0.1538719675410951817775… | 0.1538719675410951817775… | 1.1e-49 | **22,690,901×** |

`verdict: closed-form-verified-50dps`, `max_rel_err: 1.1e-49`.

## Resolution of the "21%" framing

The 21% number applies to a **different convention**, not to the
production default. `closed_form_tau_M.py` exposes three
`pn_convention` choices for the p-n interface factor:

| convention | p-n factor | matches production? |
|---|---|---:|
| `"chi_lambda_braid"` (DEFAULT) | z | ✓ machine-precision (1e-49) |
| `"strict_averaged"` (audit-only) | z − h/2 | ✗ disagrees by ~21% on atoms with p-n interface |
| `"bring_color_weighted"` (queued research) | z − h·(1/2 − δ/4) | not yet implemented |

Production uses `chi_lambda_braid`-marshalled words (per
[`canonical_braid_marshalling.marshal_to_chi_lambda_braid`](../../computations/canonical_braid_marshalling.py),
which maps `(c=1, d=-h/2)` to `(sign=+1, gen)` — collapsing the
averaged interface to positive σ). The closed form's default
`pn_convention="chi_lambda_braid"` mirrors this collapse exactly,
which is why the Phase 5q witness shows rel_err ≈ 1e-49.

The `strict_averaged` mode (using the literal `σ - (h/2)·I`
algebraic averaged generator) is the **mathematically-correct**
form per `prop:averaging-resonance-rule`, but production
marshalling silently drops the `-h/2` component. **The 21% number
is the gap between production and the mathematically-strict form
— a known marshalling-bug audit trail item, NOT a closed-form bug.**

## Implications for Track C

1. **Closed form is correct as wired.** `binding_canonical.py:196` already
   uses `closed_form_tau_M` for the canonical atom-binding evaluation;
   no migration is needed for the canonical binding chain.

2. **Migration opportunities (perf wins, not correctness fixes).**
   The slow-path tr_M evaluation (per-atom `atom_braid_word_3A` +
   `chi_lambda_braid` on H_{3A}) costs ~1645s wall at ⁴He. Scripts
   that compute tr_M for multi-nucleon atoms could be migrated to:

       tau_atom = closed_form_tau_M(Z, N, q, tau_p, tau_n)

   for a 22-million× speedup at ⁴He. Slow-path consumers
   identified by `grep -L closed_form_tau_M $(grep -l atom_braid_word_3A *.py)`:

   - [`canonical_tr_m_helium4_stub.py`](../../computations/canonical_tr_m_helium4_stub.py)
     (156 LOC; ⁴He-specific stub)
   - [`atomic_tr_m_helium4.py`](../../computations/atomic_tr_m_helium4.py)
     (390 LOC; full H_12 path)
   - [`build_atomic_braid_recipe_4he_chain.py`](../../computations/build_atomic_braid_recipe_4he_chain.py)
     (307 LOC; recipe builder)
   - others under
     `grep -L closed_form_tau_M $(grep -l atom_braid_word_3A *.py)`

   Each is a separate follow-up; this audit does not migrate them.

3. **Marshalling-bug audit trail.** The 21% gap between
   `strict_averaged` and production is a SEPARATE workplan item
   (`canonical_braid_marshalling.py` silently drops `-h/2`; see
   sibling probes `probe_pn_flavor_asymmetry.py` and
   `probe_per_sheet_flavor_nonin.py`). The Bring color-tube weighted
   convention (queued research) reconciles this through quark-mass
   inputs. Out of scope for this audit.

## Action taken in this PR

Updated the misleading docstring in `closed_form_tau_M.py` (the
"21%" sentence implied the closed form disagrees with production
when in fact only the alternative `strict_averaged` convention
does). The DEFAULT `"chi_lambda_braid"` convention entry now
explicitly notes Phase 5q validation at 1e-49; the
`"strict_averaged"` entry now frames the 21% as the
alternative-convention vs production gap, with a pointer back
to this audit doc.

## Cross-references

- `closed_form_tau_M.py` § "Open: Bring color-tube weighted averaging (Phase 5q audit)"
- `closed-form-tau-M-verification-phase5q.witness.json` — empirical evidence
- `canonical_braid_marshalling.py` — production marshalling that collapses averaged → σ
- `binding_canonical.py:196` — already-wired consumer
