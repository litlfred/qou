#!/usr/bin/env python3
"""Keystone axiom guard — `#print axioms` as a QA gate, not a one-off check.

Motivation (2026-08-07). Two keystones were merged claiming a discharge that a
per-declaration axiom check refutes: `OVTopAssembly.sum_numSYT_sq_eq_factorial`
and everything reindexed from it depend on `sorryAx`. File-level `grep sorry` is
a *screen*; the proof term is the *verdict*. See
`docs/audits/2026-08-07-ov-cone-axiom-audit-overclaim-correction.md`.

This script pins the measured axiom status of named declarations so that:

  * a declaration recorded `clean` that starts depending on `sorryAx` FAILS the
    gate (regression — the usual direction of harm);
  * a declaration recorded `sorryAx` that becomes clean is reported as a
    PROMOTION (someone closed an upstream gap; update the registry and the
    claims that were scoped around it).

Usage
-----
    scripts/lean-axiom-guard.py                 # check every entry
    scripts/lean-axiom-guard.py --filter TAIL   # substring filter on decl name
    scripts/lean-axiom-guard.py --registry F    # alternate registry file
    scripts/lean-axiom-guard.py --print-modules # the modules that must be built

Exit codes: 0 = all as recorded; 1 = regression; 2 = environment/setup problem.
A promotion alone exits 0 (it is good news) but prints a LOUD notice.

Registry format (one entry per line, `#` comments allowed):

    <import-module> | <fully-qualified-decl> | clean|sorryAx

The Lean root is `content/quantum-observable-universe/lean`; `LEAN_PATH` must
already be set for lean-direct use (see `.claude/skills/local/lean-environment-setup.md`
— restore the olean cache first, and note that a declaration's own module olean
must exist).

STALENESS IS ALREADY GATED HERE — AND THE GATE ONLY COVERS THIS REGISTRY
------------------------------------------------------------------------
`check_freshness` below walks the transitive QOU import cone of every registry
module and refuses to report when an olean is missing or older than its source
(by `lean_freshness.effective_source_time`, which uses commit time rather than mtime
so a fresh clone does not read as universally stale). That gate predates 2026-08-26
and works. `scripts/lean_cone_build.py` imports the SAME function, so the rebuilder
below cannot call fresh what this gate calls stale -- it could until 2026-08-26, and
the compose deadlocked because of it (bean qou-5v24).

What it does NOT cover is an **ad-hoc `#print axioms` probe** written by hand
against some other module. Such a probe reads the same mixed-vintage olean set
with none of this protection, and mixed-vintage is the normal state of a restored
container: measured 2026-08-26, QOU olean build dates on one tree spanned
2026-06-09 .. 2026-08-26.

Measured cost of that gap, same day, twice, both outside this registry:

  * Two SDP declarations reported depending on
    `PosSemidefDiagZero.entry_sq_le_diag_mul_axiom`, which does not exist in the
    source — that module proves it as a THEOREM, and its olean was built
    2026-06-09 when it was an axiom.
  * A probe resolved `…SDPRealUniqueness.SDPSlaterUniqueness.ofSlater_proven`.
    After a rebuild that name does not exist; the source declares it one
    namespace higher. The reading was of a pre-move snapshot.

So the rule is not "the guard is unsound" — it is sound within its registry. The
rule is: **a hand-written `#print axioms` outside this registry has no gate, and
must rebuild what it measures first.** The remediation tool already exists --
`scripts/lean-direct-cone.sh` (driver: `scripts/lean_cone_build.py`) -- and this
gate detects staleness without fixing it, so the two compose:

    scripts/lean-direct-cone.sh $(scripts/lean-axiom-guard.py --print-modules)

It uses `lean`-direct rather than `lake build`, which would evict a restored
cache (bean `qou-r13s`), skips modules already up to date, and builds in
parallel. Related and worth knowing before hand-rolling anything:
`scripts/lean-verify-cone.sh` (bean `qou-fjcd`) verifies an edited file AND its
consumers against rebuilt oleans, which is the consumer-side form of this trap.

Full finding: docs/audits/2026-08-26-live-axiom-surface-recheck.md §4.

WHAT MUST BE BUILT FIRST — only the registry's own modules
----------------------------------------------------------
The probe file imports exactly the modules named in the registry and nothing
else, so this gate does **not** need the `QOU` root or a whole-tree build.
`--print-modules` emits that list, so a caller builds precisely the
prerequisites without duplicating the registry here:

    lake build $(scripts/lean-axiom-guard.py --print-modules)

This is recorded because the opposite was believed, and the belief is what kept
the gate unrun: bean `qou-agrd` asserted "the guard imports the **`QOU` root**,
which transitively needs the whole tree built". It does not, and never did.
Measured 2026-08-15: four of the five registry oleans were already present and
exactly one — `QOU.BraidsAndKnots.PlancherelNormalisation` — was missing.
Building that single module took 329 s and made the gate run clean on all seven
declarations. The diagnosis, not the difficulty, was the blocker.

RE-MEASURED 2026-08-25, because the registry has since grown from 5 modules / 7
declarations to 11 / 34 and the figures above no longer describe it:

  * 6 of 11 registry modules are fully verifiable from a restored olean cache
    plus a small lean-direct build — every entry #5761 added, and the
    law-of-sines module.  Their cone is 33 modules, of which 30 needed
    building: 260 s wall, all 30 exit 0.  One batch run then verified all 27 of
    those entries `clean`, with no regression and no promotion.
  * 5 remained unverifiable at that point — `OVTopAssembly`, `RSKBurnsideDischarge`,
    `SYTEncodingBridgeTwo`, `PlancherelNormalisation`,
    `YoungDiagramTailFirstInstance` — needing 70 module builds
    (21 absent oleans + 49 present-but-older-than-source).

SUPERSEDED THE SAME DAY: those 70 were built (753 s, 70/70 exit 0) and the whole
registry now runs.  **Every entry is verifiable, and the full gate is rc=0.**  The
four `sorryAx` rows turned out to be stale — see the RSK block below.  Note what the
cost estimate was worth: the build was quoted as the reason not to bother, and it
took under 13 minutes and overturned the registry.

Count both criteria.  An olean that merely EXISTS is not enough — 49 of the 70
above are present and stale, and a verdict read off a stale olean is the axiom
status of an old snapshot, which the staleness check exists to refuse.  Counting
only absent oleans undercounts this backlog by more than 3x (21 vs 70), an error
made while writing this very paragraph.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

LEAN_ROOT = Path("content/quantum-observable-universe/lean")

# Measured 2026-08-07 by `#print axioms`. Keep sorted by module for readability.
DEFAULT_REGISTRY = """
# --- the Lagrange node-sum family (Pieri corner identity, PR #6098) ---
# `sum_prod_qratio_corner` is the node-coordinate form of the one identity the
# Macdonald hook telescope's Pieri step (P) reduces to. It is proved FROM
# `sum_eval_div_prod_eq_coeff`, so the keystone is registered alongside it: a
# regression there would poison the corner identity silently, and `#print axioms`
# on the consumer alone would not say which of the two moved.
QOU.Mathlib.LagrangeCornerNodeSum | QOU.Mathlib.sum_prod_qratio_corner | clean
QOU.Mathlib.LagrangeCornerNodeSum | QOU.Mathlib.sum_eq_one_of_corner_ratio_scaling | clean
QOU.Mathlib.LagrangeCoeffSum | QOU.Mathlib.sum_eval_div_prod_eq_coeff | clean
# The q-FRT chain the corner identity consumes. `prodHooksF_one_sub_pow_pair` is pinned
# because a session read LagrangeCoeffSum's (stale) docstring as saying it was OPEN and
# nearly rebuilt the chain; a registry row is a claim a machine re-checks.
QOU.Mathlib.SYTBetaGapVandermonde | QOU.Mathlib.SYTBeta.prodHooksF_one_sub_pow_pair | clean
QOU.Mathlib.QHookVandermonde | QOU.Mathlib.SYTBeta.prodHooksF_one_sub_pow_vandermonde | clean
# The general-X Macdonald hook telescope -- the goal of bean qou-dsif -- and the
# general-r branching it rests on. Pinned because until 2026-08-30 this theorem was
# UNVERIFIABLE: its import cone was red on main. `QOU.Mass.QIntegerBarParity` opened
# `QOU.Mass.QHookDimension`, which 1646b5d6d3 removed (it had been declared nested,
# as `namespace QOU.Mass` then `namespace QHookDimension`); `QIntegerCanonical` named
# the same path and broke with it. So `grep -c sorry` returned 0 while `#print axioms`
# could not run at all. A registry row is a claim a machine re-checks; a sorry count
# is not.
#
# An earlier draft of this comment said the namespace "never existed". That was wrong,
# and it was wrong for an instructive reason: the grep behind it matched only the
# fully-qualified `namespace QOU.Mass.QHookDimension` and so could not see the nested
# spelling. One spelling of a two-spelling construct -- the blind-spot class in
# docs/audits/2026-08-15-detector-blindness-taxonomy.md. Caught in review by Copilot
# after the same error had already been corrected in the bean and the commit message
# but not here, which is the contamination-spread failure AGENTS.md warns about.
#
# Measured on origin/main bf08fd156f9, whole-corpus lean-direct with keep-going:
# up-to-date 1718, ok 379, blocked 210, error 1. All 210 blocked trace to the single
# error, and 179 of them carry ZERO sorry tokens -- sorry-free on the screen, no
# verdict available from the proof term.
QOU.MathlibExt.MacdonaldTelescopeGeneralX | QOU.MathlibExt.MacdonaldTelescopeGeneralX.telescope_generalX | clean
QOU.SchurWeyl.BranchingGenericity | QOU.SchurWeyl.sum_schurPrincipal_addCellOrSelf | clean
QOU.SchurWeyl.BranchingGenericity | QOU.SchurWeyl.sum_wenzlWeight_addCellOrSelf | clean
# --- the (TAIL) first-instance chain (covariance-kernel epic qou-x631) ---
# The SIGN is genuinely sorry-free and is the content of the (TAIL) instance.
QOU.BraidsAndKnots.YoungDiagramTailFirstInstance | QOU.BraidsAndKnots.YoungDiagramTailFirstInstance.nuV_top_nonneg | clean
# The SYT-encoding bridge is genuinely sorry-free.
QOU.BraidKnot.SYTEncodingBridgeTwo | QOU.BraidKnot.SYTEncodingBridge.numSYT_eq_numStandardYoungTableaux | sorryAx-free-expected-clean-alias
QOU.BraidKnot.SYTEncodingBridgeTwo | QOU.BraidKnot.SYTEncodingBridge.numStandardYoungTableaux_le_numSYT | clean

# --- known-BAD: the RSK identity and everything reindexed from it ---
# The real gap is upstream (RegularRepBlockTrace's sorry on the specialised
# lemma, plus the Specht-core cone: 16 of 23 modules carry sorry).
QOU.BraidKnot.OVTopAssembly | QOU.BraidKnot.OVTopAssembly.sum_numSYT_sq_eq_factorial | sorryAx
QOU.BraidKnot.RSKBurnsideDischarge | QOU.BraidKnot.RSKBurnsideDischarge.rskBurnsideHolds | sorryAx
QOU.BraidsAndKnots.PlancherelNormalisation | QOU.BraidsAndKnots.PlancherelNormalisation.sum_sytDim_sq_eq_factorial | sorryAx
QOU.BraidsAndKnots.PlancherelNormalisation | QOU.BraidsAndKnots.PlancherelNormalisation.nuV_top_closed_form_unconditional | sorryAx

# --- fibration exactness (bean qou-de7r, item 2 of qou-pan0) ---
# Measured 2026-08-24. The topological half of the homotopy LES, and only the
# MIDDLE spot: exactness of pi_N(F) -> pi_N(E) -> pi_N(B) at pi_N(E), from a
# stationary-relative homotopy lifting hypothesis. There is no connecting map
# and no exactness at the other two spots, so `clean` here is NOT a claim about
# the long exact sequence.
QOU.Mathlib.FibrationExactness | QOU.Mathlib.FibrationExactness.homotopyGroupMap_eq_const_iff | clean
QOU.Mathlib.FibrationExactness | QOU.Mathlib.FibrationExactness.range_homotopyGroupHom_eq_ker | clean
# The witness that the lifting hypothesis above is satisfiable at all.
QOU.Mathlib.HomotopyLifting | QOU.Mathlib.HomotopyLifting.Prod.hasHomotopyLiftingPropertyRel_fst | clean
# --- the RSK identity: WAS known-BAD, MEASURED CLEAN 2026-08-25 ---
# These four were recorded `sorryAx` with the note "the real gap is upstream
# (RegularRepBlockTrace's sorry ... plus the Specht-core cone: 16 of 23 modules carry
# sorry)".  That is now STALE.  All four are sorry-free, and — measured, not assumed —
# so are their UNCONDITIONAL forms.
#
# What changed: the in-repo Robinson–Schensted development (40 `QOU.Mathlib.Schensted*`
# source files, 5 sorry tokens between them, landed via PR #5745) and the keystone
# instance below.  Nobody noticed because the gate could not run: verifying these needs
# a 70-module lean-direct build, so the registry kept asserting a gap that had closed.
#
# HOW THIS WAS MEASURED, because "clean" alone would NOT have been sufficient evidence.
# All four now carry an instance binder `[SnWedderburnPartitionBridge.SnIsotypicSpechtSplit ℚ]`,
# so each proves an IMPLICATION.  `#print axioms` cannot see an undischarged instance
# hypothesis — a declaration can go `sorryAx` -> `clean` with ZERO new mathematics purely
# by moving its obligation into a class binder, which is the §3b-cond pattern and is
# exactly what "conditional-proved ≠ premise-established" warns about.  So `clean` here
# was treated as a RED FLAG and checked three ways:
#   1. the instance `instSnIsotypicSpechtSplit` is itself sorry-free   -> yes;
#   2. each theorem COMPOSED with that ambient instance is sorry-free  -> yes, all four;
#   3. the composition elaborated with EXIT 0 — a declaration that fails to elaborate
#      reports `sorryAx` from error recovery, which is not a finding.  (One draft of this
#      check did exactly that and would have been misread as a defect.)
QOU.BraidKnot.OVTopAssembly | QOU.BraidKnot.OVTopAssembly.sum_numSYT_sq_eq_factorial | clean
QOU.BraidKnot.RSKBurnsideDischarge | QOU.BraidKnot.RSKBurnsideDischarge.rskBurnsideHolds | clean
QOU.BraidsAndKnots.PlancherelNormalisation | QOU.BraidsAndKnots.PlancherelNormalisation.sum_sytDim_sq_eq_factorial | clean
QOU.BraidsAndKnots.PlancherelNormalisation | QOU.BraidsAndKnots.PlancherelNormalisation.nuV_top_closed_form_unconditional | clean

# --- the keystone instance: THE load-bearing entry for the four above ---
# Pinning the four theorems is NOT enough on its own.  They are conditional, so they stay
# `clean` even if this instance is weakened or acquires a `sorry` — the gate would keep
# reporting green while the mathematics silently reverted to assumed.  This entry is what
# makes the four above mean anything: it is the only place a regression can be caught.
QOU.BraidKnot.SnIsotypicSpechtSplitInstance | QOU.BraidKnot.SnIsotypicSpechtSplitInstance.instSnIsotypicSpechtSplit | clean

# --- the Catalan bridge: two definitions of one constant, now provably equal ---
# `catalan_G` (alternating series, HyperbolicVolumeTranscendence) and `Cl_2 (π/2)`
# (Clausen value, ClausenFunctionMathlibFiller) are defined in files that do not import
# each other, and nothing connected them: the filler's own
# `catalan_constant_eq_cl_2_pi_over_2` is `rfl` over a DEFINITION and carries no content.
# Two unbridged definitions of one constant is a live hazard — a result proved about one
# is not a result about the other. Pinned because that is the kind of theorem a later
# refactor silently breaks.
QOU.Archimedean.CatalanClausenBridge | QOU.Archimedean.catalan_G_eq_Cl_2_pi_div_two | clean
QOU.Archimedean.CatalanClausenBridge | QOU.Archimedean.summable_catalan_summand | clean
# --- the Lobachevsky-Catalan identity: an AXIOM until 2026-08-26, now a theorem ---
# `lobachevsky (pi/4) = catalan_G / 2` was recorded as an `axiom` citing Lewin 1981, on
# the stated ground that a proof needs "Mathlib's full polylogarithm machinery ... none of
# which is currently upstream".  That was wrong twice over: Mathlib has
# `integral_log_sin_zero_pi_div_two` and `Analysis.Complex.AbelLimit`, and THIS REPO
# already had the whole series-integral bridge in `QOU.Knot.clausen_eq_series`, sorry-free.
# The proof is three steps over those.
#
# This is the highest-value pin in the file: a declaration that moved from `axiom` to
# `theorem` is exactly what a careless revert turns back into an axiom while every name
# and every downstream `rw` still typechecks.  `#print axioms` is the only thing that can
# tell the difference, so it is pinned here.  The Whitehead entry is pinned alongside it
# because it is the downstream consumer that was CONDITIONAL on the axiom and is now not;
# if the identity regresses, this row is where the inherited `sorryAx` reappears.
QOU.Archimedean.BorromeanVolumeCatalan | QOU.Archimedean.lobachevsky_pi_div_four_eq_half_catalan | clean
QOU.Archimedean.WhiteheadVolumeCatalan | QOU.Archimedean.WhiteheadVolume.vol_L5a1_eq_eight_lobachevsky | clean

# --- the coset-sum lift: the step MarkovInductiveCyclicity's header says is NOT mechanised ---
# That header states "The **only** step not mechanised in Lean is the linear lift of the two
# single-coset grounding lemmas to the general E on an arbitrary w = a + sum b_i f c_i".
# These five are that lift. Pinned because the module is CONDITIONAL: its value is entirely
# in the hypotheses being genuine tower relations rather than the conclusion in disguise, and
# that property is exactly what a careless edit destroys while leaving the file compiling.
QOU.Machinery.MarkovCosetLift | QOU.Machinery.MarkovInductive.tr_finset_sum | clean
QOU.Machinery.MarkovCosetLift | QOU.Machinery.MarkovInductive.gwg_trace_lower_shape | clean
QOU.Machinery.MarkovCosetLift | QOU.Machinery.MarkovInductive.gwg_trace_mid_shape | clean
QOU.Machinery.MarkovCosetLift | QOU.Machinery.MarkovInductive.gwg_trace_cosetSum | clean
QOU.Machinery.MarkovCosetLift | QOU.Machinery.MarkovInductive.ce_trace_cosetSum | clean

# --- the Markov-trace linearity chain: an AXIOM until 2026-08-26, now a theorem ---
# `markovTrace_linear` asserted that an `opaque` function on `HeckeElement n` is linear.
# `HeckeElement n` is not opaque -- it abbreviates `EuclideanSpace ℝ (Fin n!)` -- so by
# Riesz every linear functional on it is `⟪w, ·⟫`. Carrying the trace as its weight vector
# instead of as an opaque function makes linearity PROVABLE at no cost in content, and the
# opacity moves to a datum (`markovTraceWeight`), which asserts nothing, from a function
# plus an asserted property, which asserted something unprovable.
#
# Same reason to pin as the Lobachevsky row: axiom -> theorem is exactly what a revert turns
# back into an axiom while every downstream name still typechecks. The two consumers are
# pinned alongside because they are what the SDP-uniqueness arc actually calls.
QOU.HeckeAlgebra.Common | QOU.HeckeAlgebra.markovTrace_linear | clean
# The content-preservation claim itself. `markovTrace_linear` alone does NOT justify the
# axiom -> theorem move: it is the easy direction, and on its own the move could have
# NARROWED the admissible traces. `isLinearMap_iff_exists_weight` is the direction that
# rules that out (every linear functional IS some `⟪w, ·⟫`), so it is the one whose loss
# would silently invalidate the change. It was asserted in prose before it was proved.
QOU.HeckeAlgebra.Common | QOU.HeckeAlgebra.isLinearMap_iff_exists_weight | clean
QOU.HeckeAlgebra.Common | QOU.HeckeAlgebra.exists_weight_of_isLinearMap | clean
QOU.HeckeAlgebra.Common | QOU.HeckeAlgebra.weight_unique | clean
# The degeneracy is checked rather than asserted: both trace axioms hold under a zero
# weight, so neither excludes `tr_M ≡ 0`. Pinned so that a later change claiming to have
# pinned the trace away from zero has to confront this.
QOU.HeckeAlgebra.MarkovTrace | QOU.HeckeAlgebra.MarkovTrace.markov_axioms_vacuous_of_weight_zero | clean
QOU.HeckeAlgebra.MarkovTrace | QOU.HeckeAlgebra.MarkovTrace.markovTrace_add | clean
QOU.HeckeAlgebra.MarkovTrace | QOU.HeckeAlgebra.MarkovTrace.markovTrace_smul | clean

# --- the gluing/volume arc cited by the mass-theory exposition blocks (PR #4925) ---
# Three content blocks assert these are proved; the assertion is only as good as an
# axiom check, so the check is pinned here rather than left as a one-off.  Measured
# 2026-08-10: all six depend on [propext, Classical.choice, Quot.sound] and nothing
# else.  A `sorry` appearing anywhere upstream regresses this gate, which is the
# point — the blocks would then be claiming more than the Lean delivers.
QOU.Knot.RivinConcavity | QOU.Knot.Rivin.strictConcaveOn_tetVolLine | clean
QOU.Knot.RivinConcavity | QOU.Knot.Rivin.cot_quadratic_pos | clean
QOU.Knot.RivinConcavity | QOU.Knot.Rivin.deriv_deriv_Lob | clean
QOU.Knot.IdealTetLawOfSines | QOU.Knot.IdealTet.norm_eq_sin_div_sin | clean
QOU.Knot.IdealTetLawOfSines | QOU.Knot.IdealTet.log_sin_sub_log_sin | clean
QOU.Knot.KummerRadial | QOU.Knot.KummerRadial.kummer | clean
# The volume functor's definitional layer (same PR).  `volume_rotate` is the
# well-definedness that makes "the volume of an ideal tetrahedron" a property of
# the tetrahedron rather than of a chosen edge label.
QOU.MathlibExt.IdealTriangulation | QOU.MathlibExt.IdealTetrahedron.volume_rotate | clean
QOU.MathlibExt.IdealTriangulation | QOU.MathlibExt.IdealTetrahedron.rotate_angles | clean
QOU.MathlibExt.IdealTriangulation | QOU.MathlibExt.IdealTetrahedron.volume_eq_dilog | clean
QOU.MathlibExt.IdealTriangulation | QOU.MathlibExt.IdealTriangulation.volume_eq_dilog | clean
QOU.MathlibExt.IdealTriangulation | QOU.MathlibExt.IdealTetrahedron.param_prod | clean
# The birthday-axiom DEFECT REPORT (same PR).  These are proofs that a two-valued
# `flatBirthday` satisfies the six SurrealField birthday axioms — i.e. that the
# axioms admit a model that is not Conway's birthday.  A NEGATIVE result, so it is
# worth pinning for the opposite reason to the others: if one of these ever fails,
# the axioms were strengthened and the defect report needs re-checking, not
# quietly deleting.  The last two are the birthday-free analytic content.
QOU.AppendixSurreals.HyperrealLimitTransfer | QOU.AppendixSurreals.HyperrealTransfer.flatBirthday_avg_le | clean
QOU.AppendixSurreals.HyperrealLimitTransfer | QOU.AppendixSurreals.HyperrealTransfer.flatBirthday_add_le | clean
QOU.AppendixSurreals.HyperrealLimitTransfer | QOU.AppendixSurreals.HyperrealTransfer.flatBirthday_neg | clean
QOU.AppendixSurreals.HyperrealLimitTransfer | QOU.AppendixSurreals.HyperrealTransfer.flatBirthday_ofReal_le_omega | clean
QOU.AppendixSurreals.HyperrealLimitTransfer | QOU.AppendixSurreals.HyperrealTransfer.st_ofSeq_of_tendstoReal | clean
QOU.AppendixSurreals.HyperrealLimitTransfer | QOU.AppendixSurreals.HyperrealTransfer.tendstoReal_le_of_eventuallyLE' | clean
# The 5_2 saddle sum rule (same PR).  `fiveTwoSaddleSumRule_holds` INHABITS a
# conjecture class the corpus declared with no instance and "the statement is
# open" — so its axiom status is exactly what distinguishes a discharged
# conjecture from a relabelled one.  Pin it.
QOU.QBeta.FiveTwoComplexPentagon | QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule | clean
QOU.QBeta.FiveTwoComplexPentagon | QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_sum_V | clean
QOU.QBeta.FiveTwoComplexPentagon | QOU.QBeta.FiveTwoComplexPentagon.fiveTwoSaddleSumRule_holds | clean
# --- the REST of that law-of-sines module: support lemmas (bean qou-29hy) ---
# The two entries above (`norm_eq_sin_div_sin`, `log_sin_sub_log_sin`) are the
# ones the exposition blocks cite.  These seven are the rest of the module, and
# they are pinned for a DIFFERENT reason, so they are listed separately rather
# than folded into the block above.
#
# Disposition (owner call, 2026-08-25): `QOU.Knot.IdealTetLawOfSines` stays a
# SUPPORT module and does NOT get its own content block.  The law of sines
# already has paper presence -- a `## The law of sines` section in
# `mass-theory/ideal-tetrahedron-relabelling-invariance.md`, and the identity
# stated outright in `mass-theory/kummer-bloch-wigner-identity.md` -- so a block
# would duplicate live prose.  It is reached through `QOU.Knot.KummerRadial`,
# which imports it (`KummerRadial.lean:41`) and names
# `IdealTetLawOfSines.log_sin_sub_log_sin` as the step that makes the two sides'
# derivatives agree.
#
# Because no block will ever cite these seven, no `lean.ref` will ever point at
# them, and the module has no `.qa.json` sidecar, they are invisible to every
# per-block checker AND to the manifest.  A `sorry` reaching them would surface
# in the two cited declarations only if it happened to lie on their path; these
# seven close that gap.  `lean.ref` is singular and both neighbouring blocks
# correctly point at their own claims, so the manifest cannot be the mechanism.
#
# Measured 2026-08-25 by `#print axioms` (not by grep), against a lean-direct
# build of the 3-module cone (ClausenFunctionMathlibFiller ->
# BlochWignerLobachevsky -> IdealTetLawOfSines): all nine declarations in the
# module return [propext, Classical.choice, Quot.sound] -- zero sorryAx.
QOU.Knot.IdealTetLawOfSines | QOU.Knot.IdealTet.one_sub_ne_zero | clean
QOU.Knot.IdealTetLawOfSines | QOU.Knot.IdealTet.ne_zero_of_im_pos | clean
QOU.Knot.IdealTetLawOfSines | QOU.Knot.IdealTet.sin_tetAngle₂ | clean
QOU.Knot.IdealTetLawOfSines | QOU.Knot.IdealTet.sin_tetAngle₃ | clean
QOU.Knot.IdealTetLawOfSines | QOU.Knot.IdealTet.sin_tetAngle₂_pos | clean
QOU.Knot.IdealTetLawOfSines | QOU.Knot.IdealTet.sin_tetAngle₃_pos | clean
QOU.Knot.IdealTetLawOfSines | QOU.Knot.IdealTet.sin_tetAngle₂_eq | clean

# --- W3 tower bridge (PR #5827, bean qou-r765) -----------------------------
# These are CONDITIONAL on HeckeTower.HeckeConditionalExpectation, which has no
# instance. They are pinned for the same reason #5822's coset lift is: their
# whole value is that the hypotheses are genuine tower relations rather than the
# conclusion in disguise, and that is exactly what a careless edit destroys
# while leaving the file compiling.
#
# hCE_fails_without_conditional_expectation is the necessity direction -- it
# proves the identity is FALSE for a linear map that is not a conditional
# expectation. If it ever stops being clean, the "derivation" has become a
# decoration.
QOU.Machinery.MarkovTowerBridge | QOU.Machinery.MarkovTowerBridge.memB_mul | clean
QOU.Machinery.MarkovTowerBridge | QOU.Machinery.MarkovTowerBridge.memB_one | clean
QOU.Machinery.MarkovTowerBridge | QOU.Machinery.MarkovTowerBridge.memB_towerE | clean
QOU.Machinery.MarkovTowerBridge | QOU.Machinery.MarkovTowerBridge.epsilon_inclusion_mul | clean
QOU.Machinery.MarkovTowerBridge | QOU.Machinery.MarkovTowerBridge.towerTrace_mul_eq_of_memB | clean
QOU.Machinery.MarkovTowerBridge | QOU.Machinery.MarkovTowerBridge.cyclic_two_g_of_tower | clean
QOU.Machinery.MarkovTowerBridge | QOU.Machinery.MarkovTowerBridge.hCE_fails_without_conditional_expectation | clean
QOU.Machinery.MarkovTowerBridge | QOU.Machinery.MarkovTowerBridge.gwg_trace_of_spanning | clean
QOU.Machinery.MarkovTowerBridge | QOU.Machinery.MarkovTowerBridge.spanning_shape_holds_for_identity_inclusion | clean
QOU.Machinery.MarkovTowerBridge | QOU.Machinery.MarkovTowerBridge.towerE_eq_of_spanning | clean
QOU.Machinery.MarkovTowerBridge | QOU.Machinery.MarkovTowerBridge.gwg_trace_towerE_of_spanning | clean
QOU.Machinery.HeckeTowerBasicConstruction | QOU.Machinery.HeckeTower.constant_generator_presentation | clean
QOU.Machinery.HeckeTowerBasicConstruction | QOU.Machinery.HeckeTower.far_commute_zero | clean
# --- rank-bounded presentation + the first content-bearing instance (qou-zm8z)
# `heckePresentationOfRank_H3A` is the corpus's first presentation instance with
# real content. `s0_mul_s1_ne_s1_mul_s0` is what separates it from the constant
# family (`constant_generator_presentation`), where every relation is `rfl`
# because everything commutes -- pin it, or a later "simplification" can hollow
# the instance out while leaving the file compiling.
QOU.Machinery.HeckeTowerBasicConstruction | QOU.Machinery.HeckeTower.ofRank_of_unbounded | clean
QOU.Machinery.HeckeBraidedPresentationRank | QOU.Machinery.HeckeRank.s0_mul_s0 | clean
QOU.Machinery.HeckeBraidedPresentationRank | QOU.Machinery.HeckeRank.s1_mul_s1 | clean
QOU.Machinery.HeckeBraidedPresentationRank | QOU.Machinery.HeckeRank.braid_s0_s1 | clean
QOU.Machinery.HeckeBraidedPresentationRank | QOU.Machinery.HeckeRank.heckePresentationOfRank_H3A | clean
QOU.Machinery.HeckeBraidedPresentationRank | QOU.Machinery.HeckeRank.s0_ne_s1 | clean
QOU.Machinery.HeckeBraidedPresentationRank | QOU.Machinery.HeckeRank.s0_mul_s1_ne_s1_mul_s0 | clean
QOU.Machinery.HeckeBraidedPresentationRank | QOU.Machinery.HeckeRank.t0_mul_t0 | clean
QOU.Machinery.HeckeBraidedPresentationRank | QOU.Machinery.HeckeRank.heckePresentationOfRank_H2A | clean
QOU.Machinery.HeckeBraidedPresentationRank | QOU.Machinery.HeckeRank.heckeCosetSpanning_H2_H3 | clean
# The three CE/Markov class FIELDS, discharged concretely for H2 subset H3.
# They are theorems rather than instances only because the two classes still
# bind the UNBOUNDED presentation; the mathematics is not what is missing.
QOU.Machinery.HeckeBraidedPresentationRank | QOU.Machinery.HeckeRank.epsLin_retract | clean
QOU.Machinery.HeckeBraidedPresentationRank | QOU.Machinery.HeckeRank.epsLin_bimodule | clean
QOU.Machinery.HeckeBraidedPresentationRank | QOU.Machinery.HeckeRank.epsLin_markov | clean
QOU.Machinery.HeckeBraidedPresentationRank | QOU.Machinery.HeckeRank.heckeConditionalExpectation_H2_H3 | clean
QOU.Machinery.HeckeBraidedPresentationRank | QOU.Machinery.HeckeRank.heckeMarkovExpectation_H2_H3 | clean
QOU.Machinery.HeckeBraidedPresentationRank | QOU.Machinery.HeckeRank.tower_classes_inhabited_H2_H3 | clean
# TRIVIAL DISCHARGE, pinned so it stays visible. wenzlTowerStep_H2_H3_trivial
# discards BOTH hypotheses and cites isSemisimpleRing_H3A -- it is NOT Wenzl's
# ascent, and nothing downstream may cite it as evidence the ascent is formalized.
QOU.Machinery.HeckeBraidedPresentationRank | QOU.Machinery.HeckeRank.wenzlTowerStep_H2_H3_trivial | clean
# The prerequisite Mathlib lacks, supplied here (bean qou-kzjl). This is what a
# real WenzlTowerStep ascent would consume; pinned because a regression here
# silently re-opens the gap.
# GENERAL RANK, and it USES its hypothesis -- contrast wenzlTowerStep_H2_H3_trivial
# which discards both. Scope: trn1 = algTrace only; whether QOU's Markov trace is
# the algebra trace is NOT settled.
QOU.Machinery.HeckeBraidedPresentationRank | QOU.Machinery.HeckeRank.wenzlTowerStep_regTrace | clean
QOU.QBeta.MarkovTraceQuotient | QOU.QBeta.MarkovTraceQuotient.traceRadical_zero_mem | clean
QOU.QBeta.MarkovTraceQuotient | QOU.QBeta.MarkovTraceQuotient.traceRadical_add_mem | clean
QOU.QBeta.MarkovTraceQuotient | QOU.QBeta.MarkovTraceQuotient.traceRadical_neg_mem | clean
QOU.QBeta.MarkovTraceQuotient | QOU.QBeta.MarkovTraceQuotient.traceRadical_apply_eq_zero | clean
QOU.QBeta.MarkovTraceQuotient | QOU.QBeta.MarkovTraceQuotient.mem_traceRadicalIdeal | clean
QOU.QBeta.MarkovTraceQuotient | QOU.QBeta.MarkovTraceQuotient.quot_eq_zero_iff | clean
QOU.QBeta.MarkovTraceQuotient | QOU.QBeta.MarkovTraceQuotient.quot_pairing_nondegenerate | clean
QOU.QBeta.MarkovTraceQuotient | QOU.QBeta.MarkovTraceQuotient.one_not_mem_traceRadical | clean
QOU.QBeta.MarkovTraceQuotient | QOU.QBeta.MarkovTraceQuotient.quot_one_ne_zero | clean
QOU.QBeta.MarkovTraceQuotient | QOU.QBeta.MarkovTraceQuotient.quot_pairing_one | clean
QOU.QBeta.MarkovTraceQuotient | QOU.QBeta.MarkovTraceQuotient.instAlgebraTraceQuot | clean
QOU.QBeta.MarkovTraceQuotient | QOU.QBeta.MarkovTraceQuotient.quotMk | clean
QOU.QBeta.MarkovTraceQuotient | QOU.QBeta.MarkovTraceQuotient.quotMk_apply | clean
QOU.QBeta.MarkovTraceQuotient | QOU.QBeta.MarkovTraceQuotient.heckeBraidedPresentationOfRank_quot | clean
# Brick 3: the tower inclusion detects the radical EXACTLY (both directions),
# which is what makes the quotients a tower rather than a sequence. Conditional
# on HeckeConditionalExpectation, itself an open class with no instance.
QOU.QBeta.TLTowerRadicalDescent | QOU.QBeta.TLTowerRadicalDescent.map_mem_traceRadical | clean
QOU.QBeta.TLTowerRadicalDescent | QOU.QBeta.TLTowerRadicalDescent.mem_traceRadical_of_map | clean
QOU.QBeta.TLTowerRadicalDescent | QOU.QBeta.TLTowerRadicalDescent.map_mem_traceRadical_iff | clean
QOU.QBeta.TLTowerRadicalDescent | QOU.QBeta.TLTowerRadicalDescent.one_not_mem_either | clean
# Brick 4, a NEGATIVE result: a nondegenerate cyclic trace does NOT imply
# semisimplicity. Witness Q[eps]/(eps^2). Pinned because a regression here
# would silently re-license discharging WenzlTowerStep from its own hypothesis.
QOU.QBeta.TraceNondegeneracyInsufficient | QOU.QBeta.TraceNondegeneracyInsufficient.epsCoeff_cyclic | clean
QOU.QBeta.TraceNondegeneracyInsufficient | QOU.QBeta.TraceNondegeneracyInsufficient.epsCoeff_nondegenerate | clean
QOU.QBeta.TraceNondegeneracyInsufficient | QOU.QBeta.TraceNondegeneracyInsufficient.dualNumber_not_isSemisimpleRing | clean
QOU.QBeta.TraceNondegeneracyInsufficient | QOU.QBeta.TraceNondegeneracyInsufficient.nondegenerate_cyclic_trace_not_sufficient | clean
QOU.QBeta.TraceNondegeneracyInsufficient | QOU.QBeta.TraceNondegeneracyInsufficient.traceRadical_epsCoeff_eq_bot | clean
# n(lam) vs contentSum. schurElement's prefactor is n(lam); it read contentSum
# until 2026-08-26, which breaks the Macdonald telescope from n=2 up. These pin
# the separation so the confusion cannot recur silently.
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.nLambda_two | clean
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.nLambda_one_one | clean
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.nLambda_ne_contentSum | clean
# Box-addition infrastructure for the Pieri step. The hook-length update rule
# (+1 on the arm side, unchanged below) was verified over 111 cells across
# twelve shapes BEFORE being formalised.
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.drop_addBoxRow | clean
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.hookLength_addBoxRow_same_row | clean
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.hookLength_addBoxRow_row_below | clean
# Leg-growth half. countP_set_of_flip is proved by structural induction, not
# imported -- Mathlib has no countP-over-set lemma reachable from here.
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.countP_set_of_flip | clean
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.countP_drop_addBoxRow_at_threshold | clean
# Assembly. countP_set_of_same is the no-flip companion; the master rule
# hookLength_addBoxRow_of_ne_corner covers every cell except the new box
# itself, whose hook length needs the weakly-decreasing property that the
# bare `List ℕ` carrier does not have.
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.countP_set_of_same | clean
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.countP_drop_addBoxRow_off_threshold | clean
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.hookLength_addBoxRow_leg_growth | clean
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.hookLength_addBoxRow_row_above_ne | clean
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.hookLength_addBoxRow_of_ne_corner | clean
# Bookkeeping the row products need: a box does not change the number of rows,
# the receiving row is one longer, every other row is untouched.
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.length_addBoxRow | clean
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.getElem?_addBoxRow_self | clean
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.getElem?_addBoxRow_ne | clean
# The prefactor's share of the Pieri step: n(lambda) rises by the ROW INDEX,
# not the row length. The two decide-guards pin that direction; row 0 is the
# case an index slip would break.
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.nLambda_addBoxRow | clean
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.nLambda_addBoxRow_row_one | clean
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.nLambda_addBoxRow_row_zero | clean
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.nLambda_eq_sum | clean
# The corner addBoxRow cannot reach. addBoxRow is List.set, a NO-OP out of
# range, so addBoxRow lam lam.length = lam and NOT lam ++ [1] — recorded as
# addBoxRow_at_length so the trap cannot be re-discovered by accident. Every
# partition has exactly one new-bottom-row corner, so (P) needs this operation.
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.addBoxRow_at_length | clean
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.length_addBoxNewRow | clean
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.getElem?_addBoxNewRow_lt | clean
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.getElem?_addBoxNewRow_self | clean
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.drop_addBoxNewRow | clean
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.hookLength_addBoxNewRow_col_pos | clean
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.hookLength_addBoxNewRow_col_zero | clean
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.hookLength_addBoxNewRow_new_cell | clean
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.nLambda_addBoxNewRow | clean
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.nLambda_addBoxNewRow_example | clean
# Addable-corner enumeration. addableCorners_two_two is the NEGATIVE case: (2,2)
# has only two corners because row 1 is NOT shorter than row 0, so a box there
# would break weak decrease. A mis-stated condition gets that one wrong.
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.addableCorners_one | clean
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.addableCorners_two_one | clean
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.addableCorners_two_two | clean
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.addableCorners_three_two_one | clean
QOU.MathlibExt.QPartitionCombinatorics | QOU.MathlibExt.QPartitionCombinatorics.addBoxNewRow_mem_addableCorners | clean
# (P), the Pieri step. schurElement is a fold; nothing cell-by-cell can be said
# about a fold, so schurElement_eq_prod exhibits it as a product first. The two
# rowFactor lemmas are the box-addition response in the two cases where it is a
# clean equality.
QOU.MathlibExt.WenzlSchurElement | QOU.MathlibExt.WenzlSchurElement.schurElement_eq_prod | clean
QOU.MathlibExt.WenzlSchurElement | QOU.MathlibExt.WenzlSchurElement.rowFactor_addBoxRow_row_below | clean
QOU.MathlibExt.WenzlSchurElement | QOU.MathlibExt.WenzlSchurElement.rowFactor_addBoxRow_same_row | clean
# The third case: rows above, where the changed cell sits in the interior of
# the row's range. Stated division-free — cellFactor's denominator may vanish,
# so a ratio form would need a hypothesis the statement does not.
QOU.MathlibExt.WenzlSchurElement | QOU.MathlibExt.WenzlSchurElement.rowFactor_addBoxRow_row_above | clean
QOU.MathlibExt.WenzlSchurElement | QOU.MathlibExt.WenzlSchurElement.rowFactor_addBoxRow_row_above_short | clean
# The Macdonald hook telescope, proved at n=1 and n=2 from the CONCRETE
# schurElement. old_contentSum_prefactor_breaks_telescope is what makes the
# n(lam) fix a correction rather than a preference: revert the prefactor and
# it and telescope_two become unprovable together.
QOU.MathlibExt.MacdonaldTelescope | QOU.MathlibExt.MacdonaldTelescope.telescope_one | clean
QOU.MathlibExt.MacdonaldTelescope | QOU.MathlibExt.MacdonaldTelescope.telescope_two | clean
QOU.MathlibExt.MacdonaldTelescope | QOU.MathlibExt.MacdonaldTelescope.telescope_two_at_two_three | clean
QOU.MathlibExt.MacdonaldTelescope | QOU.MathlibExt.MacdonaldTelescope.old_contentSum_prefactor_breaks_telescope | clean
# n=3, the first case where the SYT multiplicity f_lam is not identically 1.
# telescope_three_needs_multiplicity pins that the WEIGHTING is part of the
# claim: unweighted the same sum is 46/7, not 8.
QOU.MathlibExt.MacdonaldTelescope | QOU.MathlibExt.MacdonaldTelescope.telescope_three | clean
QOU.MathlibExt.MacdonaldTelescope | QOU.MathlibExt.MacdonaldTelescope.telescope_three_at_two_three | clean
QOU.MathlibExt.MacdonaldTelescope | QOU.MathlibExt.MacdonaldTelescope.telescope_three_needs_multiplicity | clean
# The REDUCTION. pieri_one is (P) at mu=(1); telescope_two_via_pieri derives n=2
# from n=1 THROUGH it, so the induction step is executed rather than asserted.
# General n needs (P) + the SYT recursion -- elementary combinatorics, NOT the
# symmetric-function theory this file previously claimed.
QOU.MathlibExt.MacdonaldTelescope | QOU.MathlibExt.MacdonaldTelescope.pieri_one | clean
QOU.MathlibExt.MacdonaldTelescope | QOU.MathlibExt.MacdonaldTelescope.telescope_two_via_pieri | clean
# (P) at lambda=(2,1) — the first shape whose three corners exercise all three
# row cases AND the new-bottom-row operation at once. pieri_one's two corners
# are both trivial and cannot distinguish them.
QOU.MathlibExt.MacdonaldTelescope | QOU.MathlibExt.MacdonaldTelescope.pieri_two_one | clean
QOU.MathlibExt.MacdonaldTelescope | QOU.MathlibExt.MacdonaldTelescope.pieri_two_one_at_two_three | clean
QOU.MathlibExt.MacdonaldTelescope | QOU.MathlibExt.MacdonaldTelescope.pieri_two_one_summands_at_two_three | clean
# (P) stated in general, with both proved cases shown to be INSTANCES of it
# rather than statements that merely resemble it. The general induction is open.
QOU.MathlibExt.MacdonaldTelescope | QOU.MathlibExt.MacdonaldTelescope.pieriStep_one | clean
QOU.MathlibExt.MacdonaldTelescope | QOU.MathlibExt.MacdonaldTelescope.pieriStep_two_one | clean
# --- qou-8mtd: the triangulation-to-manifold volume bridge, stated CONDITIONALLY ---
# The class HyperbolicVolumeBridge has NO INSTANCE by design (the honest open state).
# These theorems are conditional on it; their axiom status is what shows the conditional
# layer itself is sorry-free, i.e. that the gap is carried in the TYPE and not in a proof.
QOU.MathlibExt.ManifoldVolumeBridge | QOU.MathlibExt.IdealTriangulation.volume_rotateAt | clean
QOU.MathlibExt.ManifoldVolumeBridge | QOU.MathlibExt.IdealTriangulation.rotateAt_tet_self | clean
QOU.MathlibExt.ManifoldVolumeBridge | QOU.MathlibExt.IdealTriangulation.rotateAt_tet_of_ne | clean
QOU.MathlibExt.ManifoldVolumeBridge | QOU.MathlibExt.HyperbolicVolumeBridge.vol_eq_of_two_realisations | clean
QOU.MathlibExt.ManifoldVolumeBridge | QOU.MathlibExt.HyperbolicVolumeBridge.vol_eq_rotateAt | clean
QOU.MathlibExt.ManifoldVolumeBridge | QOU.MathlibExt.HyperbolicVolumeBridge.vol_eq_sum_of_realises | clean
#
# MostowTriangulationBridge connects the corpus's TWO "volume of M" notions:
# Encounter.MostowRigidity.volume (a per-type real, entered as a literal and synced
# from a witness by codemod-leanval.ts) and MathlibExt.IdealTriangulation.volume
# (the computed Bloch-Wigner sum). Before it they were unrelated. The compatibility
# between them is an EXPLICIT hypothesis argument, deliberately not a class field.
QOU.Encounter.MostowTriangulationBridge | QOU.Encounter.MostowTriangulationBridge.mostow_volume_eq_triangulation_volume | clean
#
# MostowRigidity was UNPINNED until 2026-08-30 despite carrying the corpus's
# manifold-volume instances. Pinned now because figureEight was exactified
# (volume := VOL_4_1, no longer a truncated decimal) and its three consumers moved from
# `norm_num` on literals to real proofs: volume_nonneg and the unknot comparison from
# Cl_2_pi_div_three_pos, the 5_2 comparison from the certified bracket
# abs_Cl_2_pi_div_three_sub_le. Those are exactly the proofs a regression would silently
# revert to decimals.
QOU.Encounter.MostowRigidity | QOU.Encounter.MostowRigidity.figureEight | clean
QOU.Encounter.MostowRigidity | QOU.Encounter.MostowRigidity.volumeInvariant | clean
QOU.Encounter.MostowRigidity | QOU.Encounter.MostowRigidity.volumeInvariant_nonneg | clean
QOU.Encounter.MostowRigidity | QOU.Encounter.MostowRigidity.unknot_volume_lt_figureEight_volume | clean
QOU.Encounter.MostowRigidity | QOU.Encounter.MostowRigidity.figureEight_volume_lt_knot5_2_volume | clean
QOU.Encounter.MostowRigidity | QOU.Encounter.MostowRigidity.mass_rigidity_of_mostow | clean
QOU.Encounter.MostowRigidity | QOU.Encounter.MostowRigidity.mass_eigenvalue_isolated | clean
QOU.Encounter.MostowTriangulationBridge | QOU.Encounter.MostowTriangulationBridge.figureEight_volume_eq_triangulation_volume | clean
QOU.Encounter.MostowTriangulationBridge | QOU.Encounter.MostowTriangulationBridge.volumeInvariant_eq_of_two_realisations | clean
#
# HyperbolicQuotient supplies what H^3 was missing: a GROUP acting. The load-bearing
# entry is `vaddInvariantMeasure` -- it is PROVED from the corpus's own
# hypVolume_add_left, not assumed, which is what lets the quotient volume be derived
# rather than entered. `isAddFundamentalDomain_slab` exhibits an actual fundamental
# domain, so `hypVolume_eq_of_isAddFundamentalDomain` is applicable rather than
# conditional over a possibly-empty hypothesis (the ManifoldVolumeBridge trap).
QOU.Archimedean.HyperbolicQuotient | QOU.Archimedean.HyperbolicQuotient.horizontal | clean
QOU.Archimedean.HyperbolicQuotient | QOU.Archimedean.HyperbolicQuotient.height_eq_zero | clean
QOU.Archimedean.HyperbolicQuotient | QOU.Archimedean.HyperbolicQuotient.vadd_height | clean
QOU.Archimedean.HyperbolicQuotient | QOU.Archimedean.HyperbolicQuotient.vadd_mem_upperHalfSpace | clean
QOU.Archimedean.HyperbolicQuotient | QOU.Archimedean.HyperbolicQuotient.vaddInvariantMeasure | clean
QOU.Archimedean.HyperbolicQuotient | QOU.Archimedean.HyperbolicQuotient.vadd_right_injective | clean
QOU.Archimedean.HyperbolicQuotient | QOU.Archimedean.HyperbolicQuotient.eq_zero_of_vadd_eq | clean
QOU.Archimedean.HyperbolicQuotient | QOU.Archimedean.HyperbolicQuotient.vadd_ne_of_ne_zero | clean
QOU.Archimedean.HyperbolicQuotient | QOU.Archimedean.HyperbolicQuotient.hypVolume_eq_of_isAddFundamentalDomain | clean
QOU.Archimedean.HyperbolicQuotient | QOU.Archimedean.HyperbolicQuotient.e₀_ne_zero | clean
QOU.Archimedean.HyperbolicQuotient | QOU.Archimedean.HyperbolicQuotient.isHorizontal_closure | clean
QOU.Archimedean.HyperbolicQuotient | QOU.Archimedean.HyperbolicQuotient.isHorizontal_zmultiples | clean
QOU.Archimedean.HyperbolicQuotient | QOU.Archimedean.HyperbolicQuotient.latticeE₀_ne_bot | clean
QOU.Archimedean.HyperbolicQuotient | QOU.Archimedean.HyperbolicQuotient.zsmul_e₀_apply_zero | clean
QOU.Archimedean.HyperbolicQuotient | QOU.Archimedean.HyperbolicQuotient.exists_zsmul_of_mem_latticeE₀ | clean
QOU.Archimedean.HyperbolicQuotient | QOU.Archimedean.HyperbolicQuotient.ofInt_surjective | clean
QOU.Archimedean.HyperbolicQuotient | QOU.Archimedean.HyperbolicQuotient.measurableSet_slab | clean
QOU.Archimedean.HyperbolicQuotient | QOU.Archimedean.HyperbolicQuotient.isAddFundamentalDomain_slab | clean
QOU.Archimedean.HyperbolicQuotient | QOU.Archimedean.HyperbolicQuotient.hypVolume_eq_slab_of_isAddFundamentalDomain | clean
#
# FigureEightVolumeBridge keys the 4_1 statement on the EXACT VOL_4_1 = 2*Cl_2(pi/3),
# not on MostowRigidity.figureEight's 15-digit truncated literal -- the sibling
# MostowTriangulationBridge theorem keyed on that literal is sound but has jointly
# unsatisfiable hypotheses at the corpus's own figureEightTriangulation. vol_pos is
# DERIVED here from Cl_2_pi_div_three_pos, closing the positivity ManifoldVolumeBridge
# deliberately left open (for this shape only; the general case stays open).
QOU.Encounter.FigureEightVolumeBridge | QOU.Encounter.FigureEightVolumeBridge.vol_eq_VOL_4_1_of_realises | clean
QOU.Encounter.FigureEightVolumeBridge | QOU.Encounter.FigureEightVolumeBridge.vol_eq_two_clausen_of_realises | clean
QOU.Encounter.FigureEightVolumeBridge | QOU.Encounter.FigureEightVolumeBridge.vol_pos_of_realises | clean
QOU.Encounter.FigureEightVolumeBridge | QOU.Encounter.FigureEightVolumeBridge.vol_ne_zero_of_realises | clean
#
# FiveTwoVolumeBridge: the SAME truncation defect at the second knot --
# MostowRigidity.knot5_2.volume := 2.82812208833078 is a 15-digit truncation of
# VOL_5_2 = 3*BlochWigner_lob(fiveTwoShape) = 2.8281220883307831627... These are keyed
# on the exact constant. NOTE there is deliberately NO positivity here: the 4_1 proof
# went through Cl_2_pi_div_three_pos (its shape is on the unit circle), and the 5_2
# shape is not -- the corpus has no 0 < BlochWigner_lob z for 0 < z.im.
QOU.Encounter.FiveTwoVolumeBridge | QOU.Encounter.FiveTwoVolumeBridge.vol_eq_VOL_5_2_of_realises | clean
QOU.Encounter.FiveTwoVolumeBridge | QOU.Encounter.FiveTwoVolumeBridge.vol_eq_three_blochWigner_of_realises | clean
QOU.Encounter.FiveTwoVolumeBridge | QOU.Encounter.FiveTwoVolumeBridge.vol_lt_iff_of_realises | clean
#
# FiveTwoShapeBounds: the first numeric handle on fiveTwoShape, which was
# Classical.choose on an IVT statement and had NO bracket on re/im/modulus -- only
# fiveTwoShape_im_pos. Steps (i)-(ii) of the qou-f8lit route to VOL_4_1 < VOL_5_2.
# Step (iv) (certified Lambda at angles that are NOT rational multiples of pi) is NOT
# attempted here and needs interval arithmetic on sin the corpus does not have.
QOU.Knot.FiveTwoShapeBounds | QOU.Knot.FiveTwoShapeBounds.realRoot_gt | clean
QOU.Knot.FiveTwoShapeBounds | QOU.Knot.FiveTwoShapeBounds.realRoot_lt | clean
QOU.Knot.FiveTwoShapeBounds | QOU.Knot.FiveTwoShapeBounds.fiveTwoShape_re | clean
QOU.Knot.FiveTwoShapeBounds | QOU.Knot.FiveTwoShapeBounds.fiveTwoShape_im | clean
QOU.Knot.FiveTwoShapeBounds | QOU.Knot.FiveTwoShapeBounds.fiveTwoShape_re_bounds | clean
QOU.Knot.FiveTwoShapeBounds | QOU.Knot.FiveTwoShapeBounds.radicand_bounds | clean
QOU.Knot.FiveTwoShapeBounds | QOU.Knot.FiveTwoShapeBounds.fiveTwoShape_im_bounds | clean
QOU.Knot.FiveTwoShapeBounds | QOU.Knot.FiveTwoShapeBounds.fiveTwoShape_normSq_gt_one | clean

# LobMonotonicity supplies the sign of Lambda' where Rivin concavity needs it.
# qou-52ch's chord argument folds an obtuse angle with Lob_pi_sub, leaving
# (Lob a - Lob (a+c)) + Lob c; the first bracket is positive because Lambda
# DECREASES past pi/6, and no VALUE of Lambda is used -- which is the whole
# point of that reduction and would be lost if it were done numerically.
QOU.Archimedean.LobMonotonicity | QOU.Archimedean.LobMonotonicity.one_lt_two_mul_sin | clean
QOU.Archimedean.LobMonotonicity | QOU.Archimedean.LobMonotonicity.deriv_Lob_neg | clean
QOU.Archimedean.LobMonotonicity | QOU.Archimedean.LobMonotonicity.strictAntiOn_Lob | clean
QOU.Archimedean.LobMonotonicity | QOU.Archimedean.LobMonotonicity.Lob_sub_Lob_add_pos | clean

# FiveTwoAngleSum translates VOL_5_2 (a Bloch-Wigner value) into the ANGLE
# functional Rivin concavity is stated for. The corpus already had fiveTwoTet
# and volume_eq_lob_sum; only the composition was missing.
QOU.Knot.FiveTwoAngleSum | QOU.Knot.FiveTwoVolume.fiveTwoTet_angle_sum | clean
QOU.Knot.FiveTwoAngleSum | QOU.Knot.FiveTwoVolume.fiveTwoTet_angle₁_pos | clean
QOU.Knot.FiveTwoAngleSum | QOU.Knot.FiveTwoVolume.fiveTwoTet_angle₂_pos | clean
QOU.Knot.FiveTwoAngleSum | QOU.Knot.FiveTwoVolume.fiveTwoTet_angle₃_pos | clean
QOU.Knot.FiveTwoAngleSum | QOU.Knot.FiveTwoVolume.VOL_5_2_eq_three_mul_lob_sum | clean

# FiveTwoNinthPower proves the 5_2 smallest dihedral angle exceeds 2*pi/9 --
# the angle condition qou-52ch's Rivin-concavity chord bound needs. Reached
# WITHOUT any value of a transcendental function: z^3 = z - 1 makes z^9 a
# quadratic in z, and Im(z^9) > 0 collapses to Re z < 2/3.
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.realRoot_gt_three_sevenths | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.branch_upper | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.branch_lower | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.ninth_power_im_pos_reduced | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.zz | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.fiveTwoShape_ne_zero | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.zz_cubic | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.zz_pow_nine | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.normSq_mul_realRoot | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.normSq_pos | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.zz_im_pos | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.zz_re_eq | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.zz_re_lt_two_thirds | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.zz_pow_nine_im_pos | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.zz_re_pos | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.disc_pos' | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.zz_im_eq | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.zz_im_lt_re | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.sqrt_three_mul_zz_im_gt_re | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.zz_arg_eq_arctan | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.zz_arg_lt_pi_div_four | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.pi_div_six_lt_zz_arg | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.zz_pow_nine_arg_pos | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.two_pi_div_nine_lt_zz_arg | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.zz_arg_eq_angle₃ | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.two_pi_div_nine_lt_angle₃ | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.fiveTwoShape_re_pos | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.fiveTwoShape_im_gt_re | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.pi_div_four_lt_angle₁ | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.angle₁_lt_pi_div_two | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.pi_div_four_lt_angle₂ | clean
QOU.Knot.FiveTwoNinthPower | QOU.Knot.FiveTwoNinthPower.all_angles_gt_two_pi_div_nine | clean

"""


def parse_registry(text: str) -> list[tuple[str, str, str]]:
    out: list[tuple[str, str, str]] = []
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 3:
            print(f"axiom-guard: malformed registry line: {raw!r}", file=sys.stderr)
            sys.exit(2)
        module, decl, expected = parts
        # Tolerate the alias marker used for entries whose module differs from
        # the declaration's own namespace.
        if expected.startswith("sorryAx-free"):
            expected = "clean"
        if expected not in {"clean", "sorryAx"}:
            print(f"axiom-guard: bad expectation {expected!r} in: {raw!r}", file=sys.stderr)
            sys.exit(2)
        out.append((module, decl, expected))
    return out


def _module_path(mod: str) -> Path:
    return LEAN_ROOT / (mod.replace(".", "/") + ".lean")


def _olean_path(mod: str) -> Path:
    return LEAN_ROOT / ".lake/build/lib/lean" / (mod.replace(".", "/") + ".olean")


def _qou_imports(src: Path) -> list[str]:
    out: list[str] = []
    try:
        for line in src.read_text().splitlines():
            m = re.match(r"^import\s+(QOU\.\S+)", line)
            if m:
                out.append(m.group(1))
            elif line.strip() and not line.startswith(("--", "/-", "import")):
                break
    except OSError:
        pass
    return out


# ---------------------------------------------------------------------------
# Freshness: ONE definition, shared with the cone builder.
#
# `_dirty_paths` / `_commit_time` / `_effective_source_time` used to be defined
# here, and `scripts/lean_cone_build.py` used a *different* (mtime) rule.  The
# compose this file's docstring recommends therefore deadlocked whenever you
# built before committing.  Both now import `scripts/lean_freshness.py`, so the
# two notions cannot drift apart again.  Bean `qou-5v24`; the rationale, and BOTH
# measured ways a timestamp answers this wrong, are in that module's docstring.
# ---------------------------------------------------------------------------
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lean_freshness import (  # noqa: E402
    dirty_paths as _dirty_paths,
    olean_is_current as _olean_is_current,
)


def check_freshness(entries: list[tuple[str, str, str]]) -> list[str]:
    """Return human-readable staleness complaints.

    The guard reads whatever `.olean`s are on disk. A *missing* olean already fails
    loudly, but a **stale** one passes silently and reports the axiom status of an old
    snapshot — which is worthless, and worse than worthless because it looks like
    assurance. (Found 2026-08-15: the guard reported all-match against 9-day-old oleans
    while five of the underlying sorries had been closed upstream and three declarations
    had moved files.) So walk the transitive QOU import cone of every registry module and
    flag any olean older than its own source.

    "Current" is `lean_freshness.olean_is_current`: the source-hash stamp the rebuilder
    leaves when a stamp exists, and commit time (never raw mtime -- see there) when it
    does not. The rebuilder asks the same function with a stricter fallback, so its
    stale set contains this one and a rebuild always clears this gate.
    """
    problems: list[str] = []
    seen: set[str] = set()
    dirty = _dirty_paths(LEAN_ROOT)
    stack = [m for m, _, _ in entries]
    while stack:
        mod = stack.pop()
        if mod in seen:
            continue
        seen.add(mod)
        src, ole = _module_path(mod), _olean_path(mod)
        if not src.exists():
            continue
        stack.extend(_qou_imports(src))
        if not ole.exists():
            problems.append(f"{mod}: olean MISSING")
            continue
        # conservative=False: commit time as the no-stamp fallback, so this gate
        # does not refuse to report on a fresh clone (2026-08-15: mtime flagged 15
        # modules stale that `lake build` replayed as up to date). The rebuilder
        # uses the stricter fallback, so its stale set CONTAINS this one and a
        # rebuild always satisfies this gate -- that containment is what keeps
        # qou-5v24 fixed. Where a hash stamp exists both consult it and agree
        # exactly.
        if not _olean_is_current(src, ole, dirty, conservative=False):
            problems.append(f"{mod}: olean STALE (source is newer)")
    return problems


def parse_axiom_output(out: str) -> dict[str, set[str]]:
    """Parse `#print axioms` output into {decl: set-of-axioms}.

    Factored out of `run_axiom_check` so `--selftest` can exercise it without Lean.
    """
    found: dict[str, set[str]] = {}
    for m in re.finditer(r"^'([^\n]+)' depends on axioms: \[([^\]]*)\]", out, re.M):
        found[m.group(1)] = {a.strip() for a in m.group(2).split(",") if a.strip()}
    # A declaration proved without any axiom prints a different sentence.
    for m in re.finditer(r"^'([^\n]+)' does not depend on any axioms", out, re.M):
        found[m.group(1)] = set()
    return found


# The shapes the parser must handle.  PRIMED is the regression case: it is what a
# Mathlib-style primed lemma actually prints, and the pre-2026-08-25 regex scored 0 on
# it while scoring 1 on every other row here — which is exactly why the gap survived.
_SELFTEST_CASES = [
    ("primed",
     "'QOU.AppendixSurreals.HyperrealTransfer.tendstoReal_le_of_eventuallyLE'' depends "
     "on axioms: [propext,\n Classical.choice,\n Quot.sound]\n",
     "QOU.AppendixSurreals.HyperrealTransfer.tendstoReal_le_of_eventuallyLE'",
     {"propext", "Classical.choice", "Quot.sound"}),
    ("plain",
     "'QOU.Knot.Rivin.cot_quadratic_pos' depends on axioms: [propext, Classical.choice]\n",
     "QOU.Knot.Rivin.cot_quadratic_pos", {"propext", "Classical.choice"}),
    ("wrapped",
     "'QOU.A.b' depends on axioms: [propext,\n Classical.choice,\n Quot.sound]\n",
     "QOU.A.b", {"propext", "Classical.choice", "Quot.sound"}),
    ("sorry",
     "'QOU.Bad.thing' depends on axioms: [propext, sorryAx]\n",
     "QOU.Bad.thing", {"propext", "sorryAx"}),
    ("axiom-free",
     "'QOU.Foo.bar' does not depend on any axioms\n",
     "QOU.Foo.bar", set()),
]


def selftest() -> int:
    """Fail loudly if the parser stops seeing any known output shape."""
    bad = 0
    for label, raw, decl, axs in _SELFTEST_CASES:
        got = parse_axiom_output(raw)
        if decl not in got:
            print(f"  [FAIL] {label}: parser did not see {decl!r}")
            bad += 1
        elif got[decl] != axs:
            print(f"  [FAIL] {label}: axioms {sorted(got[decl])} != {sorted(axs)}")
            bad += 1
        else:
            print(f"  [ok  ] {label}")
    # A run that parses nothing must never look like a pass.
    if parse_axiom_output("some unrelated lean output\n"):
        print("  [FAIL] parser invented a verdict from unrelated output")
        bad += 1
    else:
        print("  [ok  ] unrelated output yields no verdicts")
    print("axiom-guard selftest: " + ("PASS" if not bad else f"{bad} FAILURE(S)"))
    return 0 if not bad else 1


def run_axiom_check(entries: list[tuple[str, str, str]]) -> dict[str, set[str]]:
    """Return {decl: set-of-axioms}. One lean invocation for the whole batch."""
    modules = sorted({m for m, _, _ in entries})
    body = "".join(f"import {m}\n" for m in modules)
    body += "".join(f"#print axioms {d}\n" for _, d, _ in entries)

    # The file must live under the Lean root (lean rejects outside paths).
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".lean", prefix="AxiomGuard", dir=LEAN_ROOT, delete=False
    ) as fh:
        fh.write(body)
        tmp = Path(fh.name)
    try:
        proc = subprocess.run(
            ["lean", tmp.name],
            cwd=LEAN_ROOT,
            capture_output=True,
            text=True,
            timeout=3600,
        )
    except FileNotFoundError:
        print("axiom-guard: `lean` not on PATH — restore the toolchain first.", file=sys.stderr)
        sys.exit(2)
    finally:
        tmp.unlink(missing_ok=True)

    out = proc.stdout + proc.stderr
    if "object file" in out and "does not exist" in out:
        print("axiom-guard: a module olean is missing; build it lean-direct first:", file=sys.stderr)
        for line in out.splitlines():
            if "does not exist" in line:
                print("  " + line.strip(), file=sys.stderr)
        sys.exit(2)

    # `#print axioms X` prints: 'X' depends on axioms: [a, b,\n c]
    #
    # THE NAME MAY ITSELF CONTAIN A PRIME, and Lean does not escape it.  A Mathlib-style
    # primed lemma prints as
    #
    #     'QOU.AppendixSurreals.HyperrealTransfer.tendstoReal_le_of_eventuallyLE''
    #       depends on axioms: [...]
    #
    # i.e. TWO closing quotes.  The obvious `'([^']+)'` stops at the prime, then demands
    # a space where the second quote is, and matches nothing at all — so a primed
    # declaration is UNVERIFIABLE BY THIS GATE, which is the one thing the gate must not
    # be.  Worse, it fails quietly in the single-entry case: `found` ends up empty and
    # the exit-2 "no output parsed" path looks like an environment problem rather than a
    # declaration the gate cannot see.  (Caught 2026-08-25 verifying #5761's entries;
    # one of the eighteen is primed.)
    #
    # Fix: keep the name greedy but confine it to ONE LINE (`[^\n]+`, no re.S), so it
    # backtracks to the last quote that is actually followed by " depends on axioms:".
    # The axiom list keeps `[^\]]*`, which spans the newlines Lean wraps it across —
    # a character class matches "\n" regardless of re.S.
    found = parse_axiom_output(out)
    if not found:
        print("axiom-guard: no `#print axioms` output parsed. Raw:", file=sys.stderr)
        print(out[:2000], file=sys.stderr)
        sys.exit(2)
    return found


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", type=Path, default=None)
    ap.add_argument("--filter", default=None, help="substring filter on declaration name")
    ap.add_argument(
        "--print-modules",
        action="store_true",
        help="print the modules this gate needs built (space-separated) and exit; "
             "feed to `lake build` — the gate does NOT need the QOU root",
    )
    ap.add_argument(
        "--selftest",
        action="store_true",
        help="exercise the `#print axioms` parser on every known output shape and exit; "
             "needs no Lean, no oleans and no repo root",
    )
    args = ap.parse_args()

    # Before LEAN_ROOT, so the selftest runs from anywhere.
    if args.selftest:
        return selftest()

    if not LEAN_ROOT.is_dir():
        print(f"axiom-guard: run from the repo root (missing {LEAN_ROOT})", file=sys.stderr)
        return 2

    text = args.registry.read_text() if args.registry else DEFAULT_REGISTRY
    entries = parse_registry(text)
    if args.filter:
        entries = [e for e in entries if args.filter in e[1]]
    if not entries:
        print("axiom-guard: nothing to check")
        return 0

    # `--print-modules` answers BEFORE the freshness gate, deliberately: it is a pure
    # query over the registry that touches no olean, and its whole purpose is to tell a
    # caller what to build. Gating it on a fresh build would make the flag unusable in
    # exactly the situation it exists for — a cold or stale tree.
    if args.print_modules:
        # Deliberately bare stdout: this is consumed by `lake build $(...)`.
        print(" ".join(sorted({m for m, _, _ in entries})))
        return 0

    stale = check_freshness(entries)
    if stale:
        print("axiom-guard: refusing to report — the olean set does not match the source.",
              file=sys.stderr)
        for pr in sorted(stale):
            print("  " + pr, file=sys.stderr)
        print("\nRebuild the affected modules, then re-run. A verdict from a stale olean set\n"
              "is not assurance — it is the axiom status of an old snapshot.\n"
              "\n"
              "  scripts/lean-direct-cone.sh " + " ".join(sorted(
                  pr.split(":")[0] for pr in stale)) + "\n"
              "\n"
              "That rebuild is enough: since 2026-08-26 the rebuilder gates on the same\n"
              "`lean_freshness.effective_source_time` this gate does, so it can no longer\n"
              "consider fresh an olean this gate calls stale. Before that it compared\n"
              "MTIME while this gate compared COMMIT time, and building before committing\n"
              "— the natural order — deadlocked the pair. Bean qou-5v24. `--force` is\n"
              "still available as a manual override; you should not need it here.",
              file=sys.stderr)
        return 2

    found = run_axiom_check(entries)

    regressions: list[str] = []
    promotions: list[str] = []
    missing: list[str] = []
    for _, decl, expected in entries:
        if decl not in found:
            missing.append(decl)
            continue
        has_sorry = "sorryAx" in found[decl]
        status = "sorryAx" if has_sorry else "clean"
        mark = "ok  " if status == expected else "FAIL"
        print(f"  [{mark}] {decl}: {status} (recorded {expected})")
        if status == expected:
            continue
        if expected == "clean" and has_sorry:
            regressions.append(decl)
        else:
            promotions.append(decl)

    if missing:
        print("\naxiom-guard: declarations not found in the environment:", file=sys.stderr)
        for d in missing:
            print("  " + d, file=sys.stderr)
        return 2

    if promotions:
        print("\n*** PROMOTION — an upstream gap closed: " + ", ".join(promotions))
        print("    Update the registry AND the claims that were scoped around the sorryAx.")
    if regressions:
        print("\n*** REGRESSION — these were clean and now depend on sorryAx:")
        for d in regressions:
            print("      " + d)
        return 1
    # Print the registry size rather than leaving it to be hand-counted in a PR
    # body. A PR on this branch claimed "53 entries" against a measured 51 —
    # careless description of a careful measurement, the recurring error this
    # session kept correcting. The tool knows the number; let it say so.
    print(f"\naxiom-guard: all {len(entries)} registry declarations match their "
          "recorded axiom status.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
