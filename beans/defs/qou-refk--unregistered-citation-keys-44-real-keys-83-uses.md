---
# qou-refk
title: 'UNREGISTERED CITATION KEYS: 46 real bibliography keys cited with no references.ts entry'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T09:00:00Z
updated_at: 2026-10-04T15:25:18Z
parent: qou-mub3
---

AGENTS.md §1: *"The `[key]` must match an entry in `content/schema/references.ts`
exactly (case-sensitive)."* These do not.

## How it surfaced

Chasing a DOI I had typed from memory into `CompleteStructureExclusion.lean`
(wrong: `...90050-3`; the registry had the correct `...90004-7` all along). While
verifying, `murakami2004` and `garoufalidis2012` — both cited by my own new
files — turned out to have NO registry entry at all. Swept the corpus for the
class.

## Measurement, classified honestly

Raw sweep of `-- Ref: [key]` across `content/` and `computations/` found 68
distinct unregistered keys. **Most are not defects**, and the raw number should
not be quoted:

    sanctioned `[manuscript]`          1 distinct,  3634 uses   <- AGENTS.md-sanctioned
    internal content-block labels     11 distinct,    18 uses   <- thm:/prop:/conj:/def:, cross-refs
    doc placeholders                   9 distinct,    13 uses   <- [key], [prNNNN], [probe], [audit]
    REAL unregistered bibliography    47 distinct,    83 uses   <- THE DEFECT

3 of the 47 are already fixed (`garoufalidis2012`, `murakami2004`, `ghys2007` —
all cited by files from PRs #4513/#4725, i.e. mine). 46 remain:

    fulman2004stein                   8x   computations/deltalambda/wlambda_D_reduction_content_covariance.py
    sniady2006asymptotics             7x   computations/deltalambda/fl_kernel_sign_structure.py
    serre1977                         6x   content/quantum-observable-universe/lean/QOU/Archimedean/CanonicalTitsIso.lean
    ivanov-olshanski                  4x   computations/deltalambda/wlambda_covariance_epic_A2_even_moment_positivity_proved.py
    donagi-markman1996cubics          3x   content/quantum-observable-universe/lean/QOU/Brings/CategoricalLagrangianDMCubic.lean
    rsz2013                           3x   computations/qbeta/c3_w2_c1_parity_artifact.py
    moralespakpanova2016              3x   computations/deltalambda/fl_sniady_genus_biased_measure.py
    biane1998representations          3x   computations/deltalambda/fl_sniady_genus_biased_measure.py
    ramis-sauloy-zhang-2013           2x   content/quantum-observable-universe/lean/QOU/Mass/C1FormalSolutionGrowth.lean
    voisin2002                        2x   content/quantum-observable-universe/lean/QOU/Archimedean/HodgeGramLift.lean
    beasleywitten2005                 2x   content/quantum-observable-universe/lean/QOU/BraidKnot/KeystoneRTSurgeryConstruction.lean
    donagi1997swintegrable            2x   content/quantum-observable-universe/lean/QOU/Brings/CategoricalLagrangianDMCubic.lean
    faddeev-kashaev-volkov-2001       2x   content/quantum-observable-universe/lean/QOU/QBeta/FaddeevStripGrowthConstructor.lean
    lawrence-rozansky1999             2x   computations/habiro_interpolation_wlambda.py
    cherednik2006                     2x   computations/probes/casimir_macdonald_probe.py
    costin2020                        1x   content/quantum-observable-universe/lean/QOU/Mathlib/BorelSingularity.lean
    frenkel2020                       1x   content/quantum-observable-universe/lean/QOU/Mathlib/QOper.lean
    koroteev-zeitlin2022              1x   content/quantum-observable-universe/lean/QOU/Mathlib/QOper.lean
    kontsevich-soibelman2008          1x   content/quantum-observable-universe/lean/QOU/Mathlib/WallCrossing.lean
    bridgeland2007                    1x   content/quantum-observable-universe/lean/QOU/Mathlib/WallCrossing.lean
    sauzin2014                        1x   content/quantum-observable-universe/lean/QOU/Mathlib/AlienDerivation.lean
    murakami1996                      1x   content/quantum-observable-universe/lean/QOU/KnotTheory/JonesPolynomial.lean
    kauffman1987                      1x   content/quantum-observable-universe/lean/QOU/KnotTheory/JonesPolynomial.lean
    habeggermasbaum2000               1x   content/quantum-observable-universe/lean/QOU/MassTheory/MilnorExactCoefficient.lean
    wielenberg1978                    1x   content/quantum-observable-universe/lean/QOU/Archimedean/WhiteheadVolumeCatalan.lean
    grassi-gu-marino2019qsw           1x   content/quantum-observable-universe/lean/QOU/Brings/CategoricalLagrangianDMCubic.lean
    kashaev1995                       1x   content/quantum-observable-universe/lean/QOU/BraidsAndKnots/BorromeanTowerConvergence.lean
    macdonald1995symmetric            1x   content/quantum-observable-universe/lean/QOU/BraidsAndKnots/NStatConjugateGeneral.lean
    gavrilik2001                      1x   content/quantum-observable-universe/lean/QOU/BraidsAndKnots/QIntegerAlexanderTorus.lean
    mckay1980graphs                   1x   content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean
    fulton-harris                     1x   content/quantum-observable-universe/lean/QOU/Eightfold/Sym2GateParity.lean
    murakami2013                      1x   content/quantum-observable-universe/lean/QOU/QBeta/MeridianLinearBarOdd.lean
    ggmw2020                          1x   content/quantum-observable-universe/lean/QOU/QBeta/HabiroClassicalLimit.lean
    garoufalidis2020                  1x   content/quantum-observable-universe/lean/QOU/QBeta/FiveTwoSaddleSumRule.lean
    adams1985                         1x   computations/gamma_gamma_pair_production_decomposition.py
    dimofte-garoufalidis2013          1x   computations/one_loop_torsion.py
    garoufalidis-yoon                 1x   computations/one_loop_torsion.py
    borodin-okounkov-olshanski        1x   computations/deltalambda/wlambda_covariance_epic_A1b_dpp_maya_representation.py
    stanley1999ec2                    1x   computations/deltalambda/wlambda_wstd_superexp_lower_bound.py
    vershik-kerov1985                 1x   computations/deltalambda/wlambda_wstd_superexp_lower_bound.py
    carlitz1948                       1x   computations/probes/casimir_carlitz_q_bernoulli_probe.py
    kaneko-kurokawa-wakayama2002      1x   computations/probes/casimir_carlitz_q_bernoulli_probe.py
    murakami2022wrt                   1x   computations/probes/keystone_valuemap_target_is_compact_hecke.py
    kac-cheung2002                    1x   computations/probes/casimir_q_factorial_probe.py
    silverman-1986                    1x   computations/alpha_em/alpha_em_b2_cm_weierstrass_scale_probe.py
    mathas-1999                       1x   computations/alpha_em/alpha_em_b2_canonical_scale_ratio_probe.py

## Why this matters — it is the phantom-citation class, mechanised

Same shape as the `meridian_holonomy_boost` finding (#4513) and the detector gap
raised on #4712: **a citation that points at nothing looks exactly like a
citation that points at something.** A named key gets trusted and copied; a bare
"see the literature" gets challenged. `fulman2004stein` is cited 8 times and
`sniady2006asymptotics` 7 times, both entirely unbacked.

Note the DOI incident is a SECOND, distinct failure mode not covered by this
sweep: a key that IS registered but whose DOI is typed wrong at the use site.
That one is invisible to a registration check — it needs the use-site DOI
compared against the registry entry. Worth a second detector.

## Suggested approach

  1. Mechanical gate first: extend the reference validation to fail on an
     unregistered `-- Ref:` key, with the classification above baked in so
     `[manuscript]`, block labels, and doc placeholders do not trip it. That
     stops accumulation.
  2. Then backfill, highest-use first (`fulman2004stein` 8x,
     `sniady2006asymptotics` 7x, `serre1977` 6x, `ivanov-olshanski` 4x).
  3. Add the use-site-DOI-vs-registry check as a separate pass.

## GUARD

Do NOT bulk-register from memory. That is exactly how the wrong NZ DOI got in.
`doi.org` and `arxiv.org` are egress-blocked from the agent sandbox, so entries
written here cannot be verified in-session; the three already added carry
explicit "not independently verified" notes for that reason. Either verify
against a reachable source or carry the caveat.
