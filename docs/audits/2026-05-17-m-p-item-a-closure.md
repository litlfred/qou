# Item A closure — m_p chain T2+T3 KeyError at A=1 resolved (2026-05-17)

> **Item A** (from PR #671 m_p chain closure gap audit):
> *T2+T3 at A=1: currently `KeyError`, structural vs witness-coverage
> question open (cheap to probe).*
>
> **Outcome:** witness-coverage gap. The KeyError was stale
> documentation; the underlying witness was extended earlier but
> consumers were not updated.

## Root cause

Three independent stale references compounded:

1. **`mass_formula_6term_mpfr_50dps.py:430`** — assertion key used
   the removed `term4_frob_per_vortex` field name (P1.C HARD BREAK
   on 2026-05-12 renamed it to `term4_frob_canonical_per_3A`).
   Result: the witness regeneration threw `KeyError: 'term4_frob_per_vortex'`
   when validating *any* atom, masking the actual T2/T3 status.

2. **`tr_m_wenzl_bridge_mpfr.py:261`** — used `mp.dps` instead of
   `mp.mp.dps`. `mp` is the module alias (`import mpmath as mp`),
   so the attribute is on `mp.mp` (the context object).  Result:
   `atomic_tr_m_mpfr_50dps.py` raised `AttributeError: module
   'mpmath' has no attribute 'dps'` when regenerating the upstream
   witness.

3. **`derive_m_p_hecke_path_a.py:135`** — quarantined T2+T3 with
   value `"0 (KeyError at A=1)"` and reason citing PR #533's claim
   that *"A=1 brane tower structurally empty under current
   level-selection rule"*.  This was outdated: `terms-2-3-atom-
   per-gen-mpfr-50dps.py:ATOMS` already includes proton (Z=1, N=0)
   and neutron (Z=0, N=1), and the loader
   `_load_mpfr_native_volumes(1, 0)` returns valid volumes.  The
   chain just never re-attempted the load after PR #533 was
   superseded.

## Verification

After the three fixes:

- `terms_2_3_atom_per_gen_mpfr_50dps.py` → all 5 atoms emit
  `wedderburn_vols` (proton/neutron have 2 entries each, deuteron 5,
  tritium/³He 8).
- `mass_formula_6term_mpfr_50dps.py` → 10 assertions pass; all 5
  atoms produce T1, T2, T3, T4 at 50 dps (proton T2 ~ 1.097M, T3 ~
  82K — both megaelectronvolt-divergent under the legacy Φ_q tower
  form, see PR #682 for the Li₂^q production replacement).
- `derive_m_p_hecke_path_a.py` → emits the new
  `m_p_hecke_T1_T2_T3_T4_50dps` partial alongside the historical
  `m_p_hecke_T1_plus_T4`.  No KeyError.

## What this DOES NOT close

The closure target from PR #671 is "¹H lifts from
`derivation_pending` to genuine `derived` with the
`M_P_DERIVED_MAX_REL_DIFF` threshold tightened from 1% to 1 ppm".
That requires the Φ_q → Li₂^q production swap from **PR #682** (open).

With Φ_q: `m_p_hecke_T1_T2_T3_T4_50dps = 1,178,996 MeV` (six orders
of magnitude divergent from CODATA 938.272 MeV).

Once #682 merges, re-running this branch's `derive_m_p_hecke_path_a.py`
against the Li₂^q-emitted T2+T3 (matches AME within 1% at tritium per
PR #682 table) should yield a physical m_p value within ~MeV of CODATA.
Tightening `M_P_DERIVED_MAX_REL_DIFF` then proceeds per the staged
plan in workplan v5 §6 Q2.

## Sibling-PR coordination

- **#671** (open, docs-only) — original Item A identification; this
  audit doc resolves it without modifying #671.
- **#682** (open) — Li₂^q production wiring; needed for the
  numerical closure (not just the structural unblock).
- **#663** (open) — ¹H tautology audit; once Li₂^q lands, the
  `M_P_DERIVED_MAX_REL_DIFF` threshold tightening (#663's `1%` →
  workplan v5's `1 ppm`) can proceed.

## Files changed

- `computations/tr_m_wenzl_bridge_mpfr.py:261` —
  `mp.dps` → `mp.mp.dps`.
- `computations/mass_formula_6term_mpfr_50dps.py:430` —
  assertion key update + per-rename comment.
- `computations/derive_m_p_hecke_path_a.py` — T2+T3
  now loaded (no KeyError); new `m_p_hecke_T1_T2_T3_T4_50dps` partial;
  T4 reads canonical `term4_frob_canonical_per_3A` field with legacy
  fallback; quarantine note rewritten.

## What's next (Item C + Item B)

- **Item C** (full Habiro residue at A=1) — separate probe; the T6
  values are still `None` for p/n in the current witness, suggesting
  another upstream-coverage gap analogous to Item A.
- **Item B** (T5 categorical attribution) — T5 = -18.42 for proton,
  sign-indefinite, no known categorical ansatz. Open R&D.
