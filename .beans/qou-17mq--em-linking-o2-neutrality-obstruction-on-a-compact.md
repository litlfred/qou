---
# qou-17mq
title: 'EM-linking O2 (neutrality obstruction): on a COMPACT quotient int(Laplacian u)=0 forces total charge zero — ''two like charges alone'' is NOT admissible as stated; the Green''s fn acquires a -1/vol(M) offset. Re-pose the two-like-charge invariant relative to a neutralizing background (only charge-neutral combinations well-posed; physically the nucleus IS neutral). Blocks/reshapes the STATEMENT of qou-o6ml, not just its solution'
status: in-progress
type: task
priority: normal
created_at: 2026-08-01T20:31:20Z
updated_at: 2026-08-25T16:35:35Z
---

## WORKED 2026-08-25 — O2 applied; it excludes the contest's winner

Probe: computations/em_linking_o2_neutralised_kernel_probe.py
Witness: em-linking-o2-neutralised-kernel.witness.json (4 assertions, pass)
Audit: docs/audits/2026-08-25-em-linking-o2-neutrality-applied-to-kappa-contest.md

O2 had never been applied to anything: neutralis*/neutraliz* appears at 4
sites corpus-wide, all in the round-1 audit, 0 in computations/.

STRUCTURAL (no data): a zero-mean kernel that is not identically zero must
take BOTH SIGNS. coth(alpha) is strictly positive and monotone. So no
admissible kernel saturates at kappa -> +1 — and saturation is exactly what
separated H_coth from its rivals in the mirror-series contest. The
unsubtracted coth is outside the admissible family. Finite volume suffices
(covers the cusped complements 4_1, L6a4), so this does not rest on the
compactness premise.

NUMERICAL (same 29-pair series, same statistic):
  c0 = 0 (inadmissible)  3.505%  r_vs_A +0.049   <- committed incumbent, reproduced to <1e-6
  c0 = 1 (boundary)     11.15%   r_vs_A -0.904
  c0 = 2               15.27%
  c0 = 7.5             22.32%
Monotone in c0 — every step toward genuine neutralisation is worse, and the
best member is the infinite-volume BOUNDARY, not an interior optimum.
48/140 scanned members predict a kappa zero-crossing inside A in [3,63],
contradicted outright by kappa > 1 throughout (min 1.4127).

The r = -0.904 is the sharpest part: em-linking-residual-structure rejected
H_FH_Z for r = +0.799. The admissible kernel carries MORE structure than the
hypothesis rejected for carrying structure.

SCOPE: (b) exclusion of the kernel AS WRITTEN, invariant cited (int(Laplacian
u) = 0). (a) scope-limited negative on the parameterisation. The metric
Coulomb route <A_1, J_2> SURVIVES — nothing here excludes it, nothing wired.

NET FOR qou-o6ml: round 5 withdrew the two H_FH warrants; this removes the
third from the admissible family. No member of that contest carried a live
structural warrant when scored. 4-B stays rank 1 and stays open.

NEXT (sharpened, needs no literature): compute the zero-mean Green's function
of an actual finite-volume quotient rather than the one-term stand-in
coth - c0. Either it fits kappa(A) or no admissible kernel does — and the
second outcome moves 4-B from 'route identified' to 'route excluded'.

CARRIED: qou-gcmn (B_pp frozen at A=3) bounds every scatter number here. The
structural half involves no data and is unaffected.
