---
# qou-foh0
title: 'GAP: A=4 (4He) >=4-body magnitude scalar m in (0,1/sqrt5) not fixed by a categorical driver'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T09:22:59Z
updated_at: 2026-10-04T15:12:48Z
parent: qou-v2om
---

Formalize-first session (branch claude/a4-interface-magnitude-2026-08-02) reduced the A=4 >=4-body magnitude to a SINGLE under-determined scalar m (per-pair bond magnitude) in (0,1/sqrt5).

DERIVED (sorry-free Lean, QOU/MassTheory/A4InterfaceMagnitude.lean):
- det(I+G)=(1-5m^2)(1-m^2) from the #3924 exchange spectrum {+-sqrt5,+-1}; b4=-ln det.
- b4 is SURJECTIVE onto (0,inf) in m (closed-form inverse m*(t)=sqrt((6-sqrt(16+20 e^-t))/10)) and strictly monotone => the AME target is reachable (NOT scope-(b)) but matching it is a FIT.
- naive uniform z~0.499 has 5z^2>1 => det<0, scope-(b) excluded (cited invariant = the spectrum). Same OVERSHOOT signature as the #4526 geometric W_geom.

WHAT IS OPEN: an independent categorical DRIVER that fixes m in (0,1/sqrt5) strictly below the naive z (equivalently a normalized color-tube weight W strictly below the geometric d_q^2/D^2). No driver identified. A tuned m is an anchor-inversion fit; do NOT wire.

NEXT HONEST STEP: derive m (or the intermediate W) from the s5-so3 fiber action / interface-operator spectral data WITHOUT inverting B(4He)/mu4/b4. Candidate: the interface operator I=c*sigma+d spectral eigenvalues on the (xi,nu) isotypic blocks (InterfaceOperatorBlockDiagonal.lean) may fix the per-pair coupling m from c,d (Hecke eigenvalues q,-q^-1) rather than a normalized character reweight. Coordinate with #4543 (BindingWeightMarkovPinning, distinct object).

## 2026-08-28 — interface-operator driver route MEASURED to a negative (PR #5916)

The 'NEXT HONEST STEP' (derive m from I=c*sigma+d, Hecke eigenvalues q,-1/q) is
measured: a4_interface_operator_driver_search_probe.py enumerates the natural
parameter-free functionals of {q,-1/q,h}.
- scale-like (overlap: 1/q^2, z_C, z_D, 1/[2]_q, 1/q^3, ...): ALL overshoot 1/sqrt5
  => scope-(b) unphysical. Whole-window both-convention Lean form: zD_unphysical.
- gap-like (channel split) + roots: REACHES the target band (sqrt(1-1/q^2)=0.434 is
  4.2% from m*(b4)=0.416) but 4 land in band, none <0.1% => no uniqueness => any
  match is a functional-choice fit. Confirms/extends qou-j16x.
VERDICT: interface operator does NOT categorically fix m. Magnitude stays scope-(a)
open. Nothing wired.

WHAT WOULD CHANGE IT: a categorical uniqueness argument singling out ONE functional
of {q,-1/q} BEFORE seeing the target (e.g. a Lean-proved identity forcing the per-pair
bond weight = a specific spectral invariant). None known.
Audit: docs/audits/2026-08-28-a4-interface-operator-driver-search.md



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-28 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

### Progress (Round 72 — PR litlfred/qou#8311)
- Formalized in PR `litlfred/qou#8311` (`feat/round72-su4gate-markovzd-interface-vassiliev-lever1-43c1`, Commit 1 `120f8595e20646e98de0e5ba129245b973aa1574`, Head `be2282b84c903a928b1e78fc59abcd496c8ceea5`, `scriptHash: 3cfc48bf2b24`).
