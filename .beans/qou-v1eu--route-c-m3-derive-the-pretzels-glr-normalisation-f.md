---
# qou-v1eu
title: 'Route C M3: derive the pretzel''s GL(r) normalisation from the q-Wronskian pairing (GGM 92/93)'
status: in-progress
type: task
priority: normal
created_at: 2026-09-14T17:43:28Z
updated_at: 2026-09-14T17:44:03Z
---


## Claimed 2026-09-14 (issue #7376, branch `claude/binding-gap-categorical-research-cem5tp`)

Follow-on from `qou-x3iv` (#7152, merged) and `qou-lzzi` (#7333, merged). Both routes
closed on ONE gap: the per-knot `GL(r)` normalisation.

**The finding that makes it a derivation.** GGM (92)/(93) — read further than either
merged PR did — are orthogonality relations on the fundamental solution matrix:

    (1/2) W_m(q) J W_l(q^-1)^T  in  SL(3, Z[q^+-]),   J = [[0,0,1],[0,2,0],[1,0,0]]

So the constant matrices flanking `W^-1(x;q)^T` in (94a)-(94d) / (186a)-(186d) are
constrained by a bilinear pairing the q-difference operator ITSELF determines — a
q-Wronskian, computable from the operator's coefficients via its formal adjoint under
the q-shift. Not a free choice.

**And it is the same object Part 17 measured.** `h_1(q,X) h~_1(q^-1,X^-1)` is a
`W(q) (...) W(q^-1)^T` pairing one entry at a time; Part 17's `Z[s(x)]` integrality is a
(93)-type statement. The two routes point at the same EQUATION, not merely the same gap.

**Anti-fit, load-bearing.** `J` is computed FROM the operator, never solved for against
the index. If the computed `J` does not close the gap, that is the result.

**Gates, in order:** (1) `J` from the 5_2 operator reproduces GGM's
`[[0,0,1],[0,2,0],[1,0,0]]`; (2) same at rank 2 for 4_1; (3) only then rank 6.
GGM state (94)/(186) as Conjecture 12 / Conjecture 19, so a derived `J` reproducing
their two cases is strictly stronger than what is held.

## Part 1 (2026-09-14) — the Casoratian gauge; 5_2 recovers GGM (276), the pretzel has NO palindrome gauge

Producer `aomega_m3_wronskian_casoratian_gauge_probe.py`, 4/5 (T1 a recorded negative).

- **The rule, calibrated before use.** GGM Thm 16(c) names it: `det W_{m+1}/det W_m =
  (-1)^r a_0/a_r`, the operator's END coefficients alone. Applied to GGM's OWN printed
  4_1 operator (135) it returns their printed (136) ratio `x^3`. G1.
- **Each operator has a distinguished PALINDROME gauge** — the one making the ratio
  `(-1)^r`. For 5_2 it is `lambda = q^{1/2}`, and in it our derived `N(X)` is GGM's
  printed (276) `(1, s, s, 1)` EXACTLY (G2). That is why their 5_2 Wronskian is
  m-independent (`det W_{m+1} = det W_m`, their sec-015). 4_1's is
  `lambda = q^{1/2}/x^{1/2}`, giving `(1, sigma, 1)`.
- **The pretzel has NO palindrome gauge at all — and the obstruction is INTERIOR.**
  Casoratian ratio `q^4`. The END-pair equation does have a root, `lambda = q^{2/3}` —
  already outside the `q^{1/2}` ring the level-2 grading lives in — but index pairs
  **(1,5) and (2,4) both fail there**, i.e. the whole doubled sector. Only (0,6) and the
  centre (3,3) close. So this is not "no root"; it is "the root the ends force is
  refused by the interior".
- **The negative is not a search-range artifact** (G4): at even rank `j` and `r-j` share
  parity, so a negative gauge imposes identical conditions.

**Harness bug caught and fixed before it was reported as math.** G2 first FAILED because
the gauged coefficients were round-tripped through `str()`; `sympify("XR**2+1")` mints a
fresh `XR` WITHOUT `positive=True`, and the assumption mismatch defeats `simplify`. The
coefficients were correct all along. Compare sympy objects, never re-parsed strings.

**Open.** Whether the absent palindrome gauge is an obstruction to the GL(r)
normalisation or merely means the pretzel's Wronskian determinant is m-DEPENDENT (which
is allowed — 4_1's is `x^{3m+3}`, also m-dependent, and GGM still normalise it). Do NOT
read this as "the normalisation cannot exist"; scope (a).
