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

## Part 2 (2026-09-14) — the bar-involution constraint, and a CORRECTION to Part 1

Producer `aomega_m3_wronskian_bar_involution_constraint_probe.py`, 5/6 (T1 a recorded
negative).

**The constraint.** Taking determinants of the orthogonality relation
`pref * W_m(q) J W_l(q^-1)^T = RHS` gives, since det is multiplicative,

    det W_m(q) * det W_l(q^-1)  =  det(RHS) / (pref^r * det J)  =:  c

a BAR-INVOLUTION equation with `c` a constant fixed per knot. From GGM's printed pairings:
**c = 1** for 4_1 ((137), `J = diag(1,-1)`) and **c = 4** for 5_2 ((92), `J` antidiagonal
with a 2, prefactor 1/2). `c` is NOT universal.

**Cross-checked against GGM's own data** (G2): their printed (136) `det W_m = x^{3m+3}`
gives `det W_-1 = x^0 = 1`, carrying no `q` at all, so the product is 1 — matching the
derived `c = 1` exactly. The derivation is calibrated, not assumed.

**Why a theta.** GGM (109) extended to `|q| != 1` gives `theta(y;q^-1) = theta(y;q)^-1`,
so a theta solves such an equation for free. That is why GGM's 5_2 answer IS a theta.

### 🛑 CORRECTION to Part 1, found by this probe (G5)

Part 1's G3 said the palindrome gauge is "what makes GGM's Wronskian m-INDEPENDENT".
**Wrong for this knot.** A palindromic operator has ratio `(-1)^r`, which is
m-independence only at **EVEN** rank; at odd rank it ALTERNATES. Measured: GGM's (254)
has end coefficients `(1, -1)` and ratio **+1** — that is where their m-independence
statement lives — while the palindromic (276) has `(1, 1)` and ratio **-1**. The two
differ by the sign gauge `lambda = -1`, which flips the ratio by `lambda^-r = -1`.

Contaminated and now corrected: this bean's Part 1 entry, the Part 1 commit message, and
the Part 1 comment on PR #7377. Part 1's G2 (our 5_2 `N(X)` in its palindrome gauge IS
GGM (276)) is UNAFFECTED and still holds; only the claim about what the gauge explains
was wrong. The pretzel is rank 6, EVEN, so palindromy there would have given genuine
m-independence — which is part of why its absence matters.

### The gap, stated more sharply than "the GL(r) normalisation"

At rank 6 what is missing is **one function `det W_0(x;q)` and one constant
`c_pretzel`**, tied by that bar-involution equation, with `det W_m = q^{4m} det W_0` from
Part 1. `c_pretzel` is unknown because **no held source prints a rank-6 orthogonality
relation** — searched: GGM `arxiv-2012.00062v3` secs 011/015, whose only printed pairings
are (137) at rank 2 and (92)/(93) at rank 3. T1, a recorded negative.
