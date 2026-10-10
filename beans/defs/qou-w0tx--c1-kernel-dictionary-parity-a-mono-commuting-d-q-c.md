---
# qou-w0tx
title: 'C1 kernel dictionary parity: a mono-commuting D_q carries no (−1)^m residual — does Door-v force σ = unit shift?'
status: completed
type: task
priority: normal
created_at: 2026-09-04T08:31:31Z
updated_at: 2026-09-04T10:42:55Z
---

Follow-on to `qou-33hb` (#6582). The two σ ↔ t-shift dictionaries for the C1 kernel disagree on parity: (a) unit shift has an odd component, (b) double cover commutes with the covering monodromy. Question: does the Door-v `(−1)^m` residual (the target property #6474 demanded of D_q's tower) decide between them?

PLAN
1. Lean `QOU.Mass.C1KernelDictionaryParity`: (i) generic — a monodromy-commuting homogeneous operator whose tower alternates from level n₀ on has ZERO tower from n₀+1 (two consecutive levels suffice, no seed hypothesis); (ii) apply to `c1KernelOpCover`; (iii) dictionary (a) via `residual_from_level_tower_is_odd_part`: E Y = 0 and E(O Y) = 0 are two q-recurrences differing by q^{e+2} vs q^{e+1} in the shift-2 weight — jointly they force Y = 0 (needs q ≠ 0, q ≠ 1).
2. Exact probe (sympy, symbolic q/u).
3. Audit doc; scope sentence on the conjecture block and/or `c1-ggm-bar-parity-faces`.

Expected shape (to be verified, not assumed): the residual kills BOTH dictionaries — so it does not discriminate; if D_q's symbol is L_K, the Door-v twist is not carried by D_q's own tower. Scope-(b) with invariants named; scoped as "the kernel itself as the operator" (lower-order corrections not excluded).


## RESULT (2026-09-04, PR #6610)

**The Door-v residual does not decide the dictionary — it kills both.** A tower whose level-n jet carries the monodromy character (−1)^n ε from level n₀ on is zero from that level on under either reading. (b) double cover: monodromy commutation transports the character unchanged, two consecutive alternating levels force 2(−1)^n ε T^{n+1}X = 0, no seed hypothesis (`comm_mono_flip_kills`, `c1KernelOpCover_residual_kills_tower`, zero from n₀+1). (a) unit shift: E Y = 0 and E(O Y) = 0 are (q^{e+2}−1)Y(e+2) = (q−1)Y(e) and (q^{e+1}−1)Y(e+2) = (q−1)Y(e); difference q^{e+1}(q−1)Y(e+2) = 0 (`c1E_zero_c1E_O_zero_imp`, q ≠ 0,1; `c1KernelOp_residual_kills_jet`, zero AT n₀). `QOU.Mass.C1KernelDictionaryParity`, sorry-free, axioms propext/choice/Quot.sound.

Probe-only facts: the window is minimal (E Y = 0 alone has the q-cosh family Y(2k) = Y(0)/([2]_q⋯[2k]_q), odd part forced zero by the e = −1 slot; the second alternating level kills); the kernel annihilates its own C1 carrier (L b = 0 incl. residue slots) so its tower on the carrier is (b,0,0,…).

Consequence: if symbol = L_K and D_q is its symbol, the (−1)^m twist is not made by D_q's iteration — it sits in the seed or the pairing. W2 NOT settled by the residual. My #6582 suggestion that the residual would pick (a) was wrong; retracted in the audit doc. Scope-(b), invariants named; lower-order corrections to the symbol not excluded; D_q not constructed.

Artifacts: `lean/QOU/Mass/C1KernelDictionaryParity.lean`, `computations/probes/c1_kernel_door_v_residual_probe.py`, `docs/audits/2026-09-04-c1-kernel-cannot-carry-door-v-residual.md`, scope paragraph on `mass-theory/qdifference-kernel-prolongation-symbol.md` (sidecar re-swept).

Waiting on: owner merge permission for #6610.



## Merged as #6610 (rebase, 2026-09-04). CORRECTION pending in the level-reading bean: the σ ↔ t-shift dictionaries were the wrong axis — σ is the level step (see that bean).
