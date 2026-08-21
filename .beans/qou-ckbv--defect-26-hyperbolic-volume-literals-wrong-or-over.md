---
# qou-ckbv
title: 'DEFECT: 26 hyperbolic-volume literals wrong or over-claiming precision (corpus-wide)'
status: todo
type: task
priority: normal
created_at: 2026-08-21T21:33:05Z
updated_at: 2026-08-21T21:33:46Z
---

## Measured, not estimated

`computations/hyperbolic_volume_literal_audit.py` (added in PR #5407) checks
every hand-typed hyperbolic volume against SnapPy. First run, 2026-08-21, on
114 literals:

    WRONG          2   disagree within the digits they print
    OVER_CLAIMED  24   print materially more digits than are correct
    OK            50
    UNRECOGNISED  38   not matched to a census manifold -- NOT a pass

### WRONG (2) -- fix first

`VOL_6_2 = 4.40083298054544839393`, annotated "SnapPy census", in

  - computations/vol_density_deuteron_perknot_probe.py:39
  - computations/per_knot_density_deuteron_perknot_probe.py:39

True value `4.40083251612304610144`. Wrong at digit 9 (1.06e-7 relative),
while printing 21. The corpus already holds the CORRECT 6_2 value at
`probes/gap_a4_T2_per_knot_vol_probe.py:72`, so this is a transcription, not
a disagreement about the manifold. Both are deuteron per-knot density probes,
so the wrong value is upstream of a per-knot density number.

### OVER_CLAIMED (24) -- one bad string, copy-pasted

Eight files carry the SAME Vol(4_1) literal, printing 53 digits and correct
to 20:

    lit    2.0298832128193072500 115978049904475264466050157561096
    exact  2.0298832128193072500 42405108549040571883378615060599584

33 fabricated digits. Sites: canonical_lepton_braid_words.py:201,
q_beta_complex_q_test1_phaseA{,_v2}.py, t6_lepton_h3_3channel_convention.py:46,
xi_ell_phi_q_probe.py:158, f_ell_derivation_via_per_braid_mass_tower.py:64,
lepton_tower_probe_1_cinquefoil_muon.py:54, t6_three_halves_factor_probes.py:43,
per_generator_V_hat_general.py:162 (+ truncations of the same string in
whitehead_kashaev_volume.py:72, figure_eight_kashaev_volume.py:38,
whitehead_c0_mpmath.py:38).

A second cluster of five in `computations/qbeta/qbeta_c3_*` prints 36, correct
to 17.

**Vol(4_1) needs no literal at all** -- it is `2*Cl_2(pi/3)`, i.e.
`2*mp.clsin(2, mp.pi/3)`, which `qou_substrate.constants.vol_4_1_at()` already
computes. The drain for this cluster is deletion, not re-transcription.

### Why SnapPy is the reference

Measured: `snappy.Manifold("4_1").volume(bits_prec=500)` agrees with
`2*mp.clsin(2, mp.pi/3)` to 55 digits, relative error exactly 0. So
"correct to N digits" above is a statement about the literal, not about
SnapPy's resolution.

## Scope note -- why this was NOT drained in PR #5407

That PR fixed the three files it was already touching (the qou-substrate
constant, the rd4 search table, the 6_1 kappa-series constant) and added the
audit. The remaining 26 sites are spread across probes whose CONCLUSIONS may
move when the constant changes -- e.g. the two 6_2 sites feed a per-knot
density. Each needs its producer re-run and its witness regenerated, and a
few are long-compute. That is a separate, careful pass, not an idle-drain.

## Suggested order

1. The 2 WRONG 6_2 sites (real error at 1e-7, feeds a density).
2. The 8-file Vol(4_1) cluster -- replace with the closed form, one commit.
3. The 5 qbeta_c3_* sites -- same closed form.
4. The remaining singletons.
5. Triage the 38 UNRECOGNISED (VOL_PHASE4_Z1/Z2 = 12.776/12.554,
   VOL_HYP_D, PRE_REGISTERED_VOL4 = 8.048, VOL_7_SQ_1, VOL_BRINGS): decide
   per name whether it is a census volume that the audit should learn, or a
   derived quantity that should be excluded by name.

Gate: `python3 computations/hyperbolic_volume_literal_audit.py --strict`
exits 1 while any WRONG or OVER_CLAIMED remains. Requires snappy
(`pip install snappy`); exits 77 without it, deliberately NOT 0.
