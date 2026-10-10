---
# qou-ulj0
title: 'slz5 S4: pn letter from a spin x isospin projector (S=1, T=0)'
status: todo
type: task
priority: normal
created_at: 2026-10-10T15:10:00Z
updated_at: 2026-10-10T18:40:00Z
parent: qou-slz5
---

Stepping stone 4. OPEN. Builds on qou-kj4v (T, not content, selects the channel) and qou-q8vl (escape needs d_pn outside [d_nn, d_pp] or a non-monotone law).

**Idea (judgement, untested).** Build the pn bond from the spin x isospin projector on a doubled strand: S=1, T=0 for the deuteron, S=0, T=1 for pp/nn/pn singlet. This leaves the one-letter H_2 family {sigma + d}, so neither the averaging bar nor the monotone bar applies, and it targets the Pauli-lock degeneracy directly. Required: letters valid on the faithful window 0 <= z <= h, derived, not chosen against AME.

Test: the two-nucleon ordering pn bound, pp and nn unbound (= the sign-mixed chain pattern that gives b3 > 0, qou-q8vl). No path in the six-path grep shows this attempted.

## 2026-10-10 — narrowed by a structural exclusion (PR #7612, bc7606cf6f4)

`QOU.Hecke.ChannelSwapSplitting.tr_swap_sub` (sorry-free, generic CommRing): for any trace and degree-one letters a + b·c on carriers c1 (isospin), c2 (spin),
tr(f(c1) g(c2)) - tr(g(c1) f(c2)) = (a1 b2 - a2 b1)(tr c2 - tr c1).
A Markov trace has tr sigma_i = z for every i, so the deuteron (S=1,T=0) and singlet (S=0,T=1) are EXACTLY degenerate when spin and isospin each ride on one generator, adjacent or far. Scope (b), invariant tr c1 = tr c2; converse over a domain. Exact H_4 check: (s1,s2) and (s1,s3) give 0; (s1, s2 s3 s2) gives h z^2 (a1 b2 - a2 b1).

Surviving door: carriers with UNEQUAL traces (e.g. a crossing over a third strand, tr(s2 s3 s2) = z + h z^2). Open: a derived (not chosen) reason spin and isospin ride on carriers of different length, or the 3S1-3D1 tensor/space index of qou-kj4v. Stays open.
