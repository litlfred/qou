---
# qou-k8fc
title: 'GAP: sigma_1^3 is a three-role symbol (electron / deuteron / nucleon binding factor in H_3) and the deuteron role is unsupported'
status: in-progress
pr: 8302
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-21T21:21:18Z
updated_at: 2026-10-04T15:20:23Z
parent: qou-v2om
---

Found reconciling the two deuteron adjudications of 2026-08-21 (PR #5413,
docs/audits/2026-08-21-deuteron-two-adjudications-reconciled.md §3).

THE COLLISION. `sigma_1^3` (closure: trefoil T(2,3)) carries three distinct
roles in the corpus:

  1. ELECTRON -- content layer, unanimous, 7 sites:
       recursive-atom-knot-atlas-registry.md:11  (the registry's OWN
         `principled-derivation` example: "electron sigma_1^3 -> 3_1")
       recursive-atom-knot-atlas-registry.md:49  ("Used for: the electron")
       recursive-atom-knot-atlas-registry.md:234 (table row)
       fundamental-knots-operator-basis.md:6
       confined-particle-examples.md:8
       atom-knot-mass-derivation-table3-data.md:6
       lepton-bring-surface-h3-3channel.md:17
  2. "the nucleon binding factor in H_3" -- registry:49, same sentence as (1).
  3. DEUTERON -- computations/deltalambda/ only, 8 sibling probes, every one
     citing "#4158":
       deuteron_octahedral_gluing_probe.py:7,68,152,191
       octahedral_e2_coloring_quadratic_probe.py:24
       geometric_qdilog_lifted_amplitude_probe.py:37,149
       octahedral_barsplit_convergence_probe.py:11
       deuteron_g2_frame_artifact_probe.py:32,115,140,184
     plus the Lean cone MassTheory/{TrefoilColoringBarEven,
     PinchedOctahedronDegenerate,RogersDilogInflection,
     TransverseSurfaceCurvature,GermRootVectorGaugeFixing}.

WHY ROLE 3 IS UNSUPPORTED. Corpus-grepped every in-tree reference to #4158
(12 hits): all are about the Magnus / bar-parity g_2 route
(octahedral_barsplit_convergence_probe.py:10,63-65;
deuteron_r_is_binding_residual_probe.py:7,123,142;
deuteron_binding_frame_independent_probe.py:161). NONE identifies a knot.
So deuteron_octahedral_gluing_probe.py:7 -- "The deuteron braid word is
sigma_1^3 (#4158)" -- cites a PR for a claim its other citations never make,
and the assertion propagated across the directory by copy.

SCOPE-(a), deliberately. This does NOT show the trefoil is not the
deuteron's. It shows (i) the corpus contains no derivation that it is, and
(ii) seven content-layer blocks assign the same word to a different particle
at the same `principled-derivation` tier. AGENTS.md
"attributes do not transfer across overloaded symbols".

BLAST RADIUS is (c) status-unknown, not (a) wrong. Every sigma_1^3 result --
Lean and probe -- is a true fact ABOUT sigma_1^3 and stands whoever the word
belongs to. Only the physical labelling moves. Nothing is retracted.

WHAT WOULD CLOSE IT. Cheapest first:
  1. Documentation act, zero compute: decide which particle owns sigma_1^3
     and say so once. If the deuteron role is meant as the "pn CHANNEL word"
     (which is how nastokes_transverse_curvature_seifert_probe.py:39 words
     it, and how audit B scoped it), then say "pn channel", not "the deuteron
     braid word" -- the probes currently say the latter.
  2. If role 3 is meant seriously as the ATOM's word, it needs a derivation,
     and it must be reconciled with the registry's electron assignment.
     Note it is separately arity-excluded: sigma_1^3 closes to 1 component,
     the deuteron mass word to 3 (PR #5413 sec 4).
  3. Also worth resolving while in here: registry:49's role (2) makes
     sigma_1^3 both a particle and a binding factor in one sentence.

BLOCKED ON: nothing. This is a naming/provenance audit, not new math.
Related: qou-e5jf (the adjudication), qou-985x (A's tracker), PR #4619 (an
OPEN sibling working the sigma_1^3 NA-Stokes sector).
