---
# qou-rv6z
title: 'Orphan witness a4-interface-magnitude-one-scalar-gate: no provenance, no producer, carries stale z_C; needs a producer before its number can be regenerated'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T11:21:24Z
updated_at: 2026-10-04T15:13:25Z
parent: qou-5vkl
---

RESOLVED 2026-08-30. Producer written: computations/deltalambda/a4_interface_magnitude_one_scalar_gate.py.

CONFIRMED ORPHAN FIRST. engine, scriptFile, scriptHash, commitSha, computedAt,
q0Anchor, precisionMetadata, environment ALL absent, and no script in the tree
wrote it. Every number was unreproducible by construction -- which is why PR
#6193 could only RECORD the convention-C residue, not fix it.

THE WITNESS WAS ALSO STALE AGAINST ITS OWN CITED LEAN. A4InterfaceMagnitude.lean
carries 21 declarations; the witness listed 7 and omitted zD, zD_sq, zD_sq_mem,
zD_unphysical -- the convention-D replacements added when C was excised. The Lean
docstring says so explicitly. Found by a new check that greps the .lean and fails
if a cited declaration is absent; nothing previously verified that a witness's
lean.key_theorems named real declarations.

VERDICT UNCHANGED, now reproducible. Surjective onto (0,inf) still True,
free_parameters still 0, ceiling now at full precision. Both conventions
reported: z_C 0.4993203342 (det -0.1851204799) and z_D 0.6126880371
(det -0.5477441720) -- excluded under both, MORE STRONGLY under canonical D.

TWO PRECISION LIMITS MEASURED rather than avoided, and three of my own checks
failed correctly before I got them right:
 - t=1e6 gave +inf: exp(-t) underflows, m* lands ON the ceiling, det=0, b4=-ln 0.
 - Saturation threshold measured at t = 116.2664 at 50 dps, tracking
   dps*ln(10) = 115.1293. A PRECISION limit, not a limit of the mathematics.
 - Round-trip digit loss is TWO-SIDED: ~t*log10(e) at large t (1-5m^2 cancels as
   m* -> ceiling) and ~log10(1/t) at small t (log near 1), exact at t~1. My first
   law was one-sided and failed at t=1e-6 -- correctly. Now checked against the
   two-sided floor rather than a fixed tolerance that would hide the decay.
   This is the (C2) digit-count result from the other side: B(4He) at t=28.3
   already sits 1.44e-13 below the ceiling.

TWO BASELINES DRAINED (never widened): the witness left
q0-anchor-missing-baseline.json (now q0Anchor: proton) and
raw-float64-baseline.json (3 raw float64 fields -> 0, all fmt-serialized mpf).
Ratchet re-run: exit 0, NEW dirty witnesses 0.

BLAST RADIUS ZERO. The schema shape changed (top-level -> data-nested) but
grep shows all 7 references across the corpus are PROSE citations; no file
json.loads it. Checked before changing shape, not after.

NOT MINE: the ratchet reports regressed 0 -> 1, which is
he-nu-sdp-saturation-obstruction.witness.json (5 -> 11), untouched by this
branch and last modified on main by fcc65c1380 (qou-tekx muon-pin fix).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-30 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
