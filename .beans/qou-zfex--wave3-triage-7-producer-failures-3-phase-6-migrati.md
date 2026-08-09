---
# qou-zfex
title: 'wave3 triage: 7 producer failures — 3 Phase-6 migration stragglers + 4 timeouts'
status: in-progress
type: task
created_at: 2026-08-08T23:31:03Z
updated_at: 2026-08-08T23:31:03Z
---


Branch: claude/anchor-followups-2026-08-08. Wave 3 report:
scratchpad/f64regen3.json (76 of 101 producers run, 1.47 h wall).

## The 7 failures, triaged

THREE were Phase-6 migration stragglers — same root cause class, all now fixed
and verified exit 0:

1. `multiterm_cost_deuteron_psd_gate_probe.py` — `ModuleNotFoundError:
   _precision`. It does `sys.path.insert(HERE)` but `_precision` moved to
   `computations/substrate/`; the file was missing the `import _path_bridge`
   line that every working consumer has (cf. `binding_link_volumes.py:39`).
   FIX: added the bridge import.

2. `phase5/phase2_proton_m_e_hecke_diagnostic.py` — "missing input:
   .../phase5/mass-formula-6term-mpfr-50dps.witness.json", on a file that
   EXISTS at `computations/mass-formula-6term-mpfr-50dps.witness.json`. It used
   the pre-refactor `ASSEMBLY_DIR / "<name>"` join, which looks only beside the
   script. `_path_bridge.witness_path()` exists precisely to replace that idiom
   (its own docstring says so) and `derive_m_p_hecke_path_a.py:95` already uses
   it for the same witness. FIX: switched to `witness_path`.

3. `binding_per_block_magnitude_a3_probe.py` — `ValueError: invalid literal for
   int() with base 10: "'15513064682004775733400041715565838634937585726284'"`
   — note the nested quotes. Line 57 did `mp.mpf(repr(e["chi_lambda"]))`.
   `repr()` is correct on a FLOAT (round-trips all 17 digits) but the witness
   now stores a 50-dps STRING, and `repr("155…")` yields `'155…'`, quotes
   included, which mpmath rejects. FIX: a `_mpf()` helper that reads a string
   directly (also strictly more precise — 50 digits vs 17) and keeps `repr` for
   floats.

   SCOPE, measured not guessed: `mpf(repr(` appears at 155 sites, and 152
   witnesses now carry string-valued `chi`/`y_lambda`/`value` fields. Only sites
   reading a migrated field actually break, so this is NOT a blanket 155-site
   edit — but it is a live class, and more will surface as the wave reaches
   them. Worth a dedicated sweep that pairs each call site with the field it
   reads. Follow-up bean warranted.

FOUR were timeouts at the 900 s cap, none of them bugs:

  `_habiro_coefficient_extract.py`          900 s, 17 witnesses touched
  `extend_even_a_mirror_pair_test.py`       900 s,  2 touched
  `he3_tritium_cosh_asymmetry_diagnosis.py` 900 s,  0 touched
  `mass_at_3A_proper.py`                    900 s,  0 touched

`_habiro` has timed out in ALL THREE waves (f64regen, f64regen2, f64regen3) —
chronic and pre-existing. The other three appear only in wave 3's larger
selection, so they have no baseline.

RULED OUT as the cause of the `mass_at_3A_proper` timeout: my exact-h/δ change
inside the `workdps(max(dps,60))` guard. Measured `atom_braid_word_3A` at
0.000 s per call (20-call loop, sub-millisecond), and `flavor_split_leading` at
0.000 s. The cost is the script's `__main__` sweep — the p(3A) character sum
over ATOMS up to ¹²C, whose own comment says "p(3A) cost grows fast". It runs at
100 % CPU throughout, so it is computing, not hung.

## Why only 76 of 101

Not a global budget — `witness_regen_wave.py` has none. The last four records are
alphabetical in `computations/probes/` ending at `graded_hecke_energy_probe.py`,
so the run was cut mid-list around `probes/h*` and `finishedAt` was written by a
cleanup path. Cause not established; the four 900 s timeouts consumed 60 of the
88 minutes, which is what left so much of the list unreached.

## Next

- [x] fix the three migration stragglers, verify exit 0 each
- [ ] re-run the wave for the ~25 unreached producers plus the 3 fixed
- [ ] run the 4 slow producers separately with a large `--timeout`
- [ ] follow-up bean: audit the `mpf(repr(` sites against string-valued fields
