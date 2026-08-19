---
# qou-btvl
title: 'D3: cross-knot DT data — 6_1 + harden 5_2 (import tier; parent qou-rtec)'
status: completed
type: task
priority: normal
created_at: 2026-08-15T02:49:30Z
updated_at: 2026-08-15T10:52:55Z
---


## Handoff note (2026-08-15, post-completion)

Slope hardening landed (SnapPy normal_boundary_slopes, exact). The OTHER
half of the cross-knot data — #boundary-parabolic connections (R1's
count; 5₂ = 4 literature-recalled, 6₁ = unknown third-knot test point
for dtMax = recursionOrder+1) — is NOT hardenable in this sandbox:
snappy.ptolemy_variety(2,'all').retrieve_solutions() needs
ptolemy.unhyperbolic.org, which 403s through the proxy, and local
Groebner (magma/sage) is unavailable. A network-open or sage-equipped
environment can close it in minutes with the same probe pattern.

## 2026-08-15 update — #connections CERTIFIED after all (egress workaround)

The ptolemy-DB-firewalled handoff above is RESOLVED for 4₁/5₂: per the
owner's egress hint, the snappy WHEEL itself ships the certified Magma
primary-decomposition outputs (ptolemy/testing_files). Probe
dt_crossknot_connection_count_certified_probe.py: 4₁ = 2 irreducible
(one degree-2 orbit, x²−x+1 = ℚ(√−3)) + 1 abelian = 3; 5₂ = 3 (one
degree-3 orbit, x³+2x²+3x+1, the trace-field cubic) + 1 = 4. R1's
counts are now locally computed, not literature-recalled. Residual:
6₁ has no bundled data — the dtMax=recursionOrder+1 third-knot test
still needs the DB or magma. Pattern documented in the new
.claude/skills/local/sandbox-egress.md skill.

## 2026-08-15 THIRD-KNOT A-POLY LEG CERTIFIED (owner upload 08c56228)

Culler census tarball (uploads/A_census.tgz): 6_1 = K4_1 (snappy
identify) has geometric L-degree 4, full 5; 4_1/5_2 re-certified (2/3
geom; the K2_1 support EQUALS the Lean a41Monomials). Probe:
apoly_census_ldegree_certification_probe.py, 3/3. The 6_1 prediction
chain (DT_max = #connections = 5) is recorded as PREDICTION — the
independent resurgence DT count for 6_1 is still the missing piece of
the third-knot test (full=geom+1 is by construction, not a test).

## 2026-08-19 — a sibling used this output and got r(6₁)=4 three independent ways

PR #5293 (`qou-gz37`, `claude/gz-third-knot-rank-grading-2026-08-19`, draft)
reads BOTH this bean's census A-polynomial output and `qou-6ort`'s ki6c
extraction, and credits them. Result: `r(6₁) = 4` by three independent routes —
DG §6's algebraic number field (`x⁴−2x³+x²+3x+1`, disc 257), this bean's Newton
polygon (geometric A-poly L-degree of K4_1), and ki6c's stationary-phase gluing
quartic — with an EXACT field-equality witness between the first and third
(`γ := −α³+3α²−4α−1` satisfies `γ⁴−γ³−4γ²+4γ+8 = 0`, `γ/2` a root of the ki6c
quartic; index-2 scaling, disc 16448 = 2⁶·257).

**They independently confirmed, and improved on, this bean's two caveats.**
The `full = geom + 1` leg being definitional (not evidence) is now the Lean
theorem `plus_one_leg_is_definitional`; and "these are saddles/critical points,
the DT invariants live on the rays BETWEEN them — so none of this is a DT
count" is stated in their artifacts. My prose caveats became theorems.

**This bean's open item is NOT closed and they say so**: an independent
resurgence DT count for 6₁ is their open item 1, naming this same gap. `r` is
the R1 *shadow*, not the count.

**Also from their sweep, worth carrying**: their M3 sweep keyed on the word
"Stokes" and missed three load-bearing papers — ki6c has ZERO "Stokes" hits.
The lesson generalises the corpus-grep discipline: *a sweep keyed on the
vocabulary of the answer you expect will miss the paper that answers in
different words.* Re-sweeping on structural vocabulary matched 94/371.

Coordination posted on #5293; `r`, the field identification, and the
9₁₂ / (−2,3,9) predictions are theirs. Do not re-derive.
