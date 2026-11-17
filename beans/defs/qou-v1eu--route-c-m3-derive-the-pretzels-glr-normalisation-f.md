---
# qou-v1eu
title: 'Route C M3: derive the pretzel''s GL(r) normalisation from the q-Wronskian pairing (GGM 92/93)'
status: in-progress
pr: 8352
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-14T17:43:28Z
updated_at: 2026-10-04T15:13:52Z
parent: qou-v2om
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

## Part 3 (2026-09-14) — 🛑 RETRACTED PREMISE, and one surviving result

Producer `aomega_m3_pairing_matrix_from_companion_probe.py`, 2/4. The two FAILs are the
superseded gates, kept as measured rather than deleted.

**What I set out to do and why it is wrong.** Parts 1-2 left `c_pretzel` unknown because no
held source prints a rank-6 orthogonality relation. The obvious move is to stop depending on
a printed source: `W_{m+1} = A_m W_m` with `A_m` the companion matrix, so if the pairing
`W_m(q) J W_l(q^-1)^T` were constant in `m` it would hold iff

    A J Abar^T = J                      <-- WRONG, retracted

which is LINEAR in `J` and would have solved the whole problem. **The pairing is not
m-invariant.** GGM (92) reads

    (1/2) W_{m-1}(x;q) J W_{-m-1}(x;q^-1)^T = [[1,0,0],[0,0,1],[0,1,3-q^m]]

whose RIGHT-HAND SIDE CARRIES `q^m`, and whose two indices shift in OPPOSITE directions
(`m-1` against `-m-1`). So (93) is an **INTEGRALITY** statement — Laurent entries,
determinant 1 — not an invariance. There is no such equation to solve.

**A harness bug sat underneath the wrong premise and would have hidden it.** `linsolve` was
fed `Poly(..., *unknowns).coeffs()`, which contain none of the unknowns, so it returned
EmptySet and every solution dimension read `None`. Repairing THAT alone would have produced
a confidently wrong `J`. Deliberately NOT repaired — a probe on a retracted premise should
not be made to work. Two failures stacked and only the harness one was visible; the premise
error was found by re-reading GGM (92), not by debugging.

**What survives, and it is worth keeping (G1).** The determinant necessary condition
`det A * det Abar = 1` holds for **all three knots including the pretzel**
(`det A` = `q/x`, `-q^{3/2}`, `q^4`; each times its bar = 1). So **Part 1's rank-6
palindromy obstruction does NOT by itself forbid a pairing** — the two obstructions are
separate, and the pretzel is not excluded on determinant grounds.

**Where that leaves the gap.** Unchanged from Part 2: one function `det W_0(x;q)` and one
constant `c_pretzel`, tied by the bar-involution equation. The shortcut is closed; a real
route needs the integrality statement (93) worked out at rank 6, or the blocks-side reading
of Part 17's `Z[s]` bilinear — and that second one risks reading `c` off the target, which
is the fit this tranche exists to avoid.

## Part 4 (2026-09-14) — 🛑 CORRECTION to Part 2's attribution, and a characterised blocker

Producer `aomega_m3_pairing_propagation_blocker_probe.py`, 2/3 (T1 the blocker).

**The corrected law.** Part 3 retracted the invariance premise. The right one, since
`W_{m+1} = A_m W_m` (GGM (130)/(244) define `W` with ROWS = shifts, so this direction is
confirmed, not assumed) and GGM (92) moves its two indices in OPPOSITE directions:

    G_M := W_M J Wbar_{-M-2}^T     satisfies     G_{M+1} = A_M G_M (Abar^T)^{-1}

the inverse because the second index DECREASES.

### 🛑 CORRECTION to Part 2: (92)/(93) are the u=0 case, not 5_2's

Part 2 called `c = 4` "the 5_2 constant, from (92)". The arithmetic
`det(RHS)/(pref^r det J) = 4` is right; the **attribution is wrong**. (92)/(93) are NOT in
the 5_2 sections (013/015) — they sit in the earlier Conjecture-12 section, and their RHS
`[[1,0,0],[0,0,1],[0,1,3-q^m]]` contains **no x at all**, while 5_2's operator (254) does.
The `3` in that RHS is `s(x)` at `x = 1`. So they are the **u = 0 (x = 1) specialisation**,
and Part 2 paired a u=0 pairing with an x-dependent operator.

**Scope `c = 4` to "the u=0 rank-3 case of Conjecture 12", never to 5_2 generally.**
Contaminated: this bean's Part 2 entry, the Part 2 commit message, the Part 2 PR comment.
Part 2's `c = 1` for 4_1 is UNAFFECTED — (137) is in the 4_1 section and carries `x`
explicitly (`x^-2 + x^-1 - 1`), and it was cross-checked against 4_1's own printed (136).

**The reading is corroborated, not assumed** (G2): specialising the operator to `x = 1`
cuts the residue from THREE nonzero entries to TWO.

### The blocker

The law still does not close. Entries **(1,0) and (2,0)** — column 0, rows 1-2 — survive
every index variant tried (`inv-3`, `inv-2`; the un-inverted variant is far worse at 9/9,
which independently confirms the inverse belongs there).

Three causes remain UNSEPARATED, named rather than guessed between:
1. the `J` for the u=0 rank-3 case may not be `[[0,0,1],[0,2,0],[1,0,0]]` as read from OCR;
2. the operator whose Wronskian (244) defines may differ from (254) at u=0;
3. the `q^{2+m}` index attachment in the companion matrix may shift.

**Next honest step:** read the u=0 section's OWN operator and `J` from the source, instead
of importing (254) and an OCR'd `J` across sections. I stopped rather than try conventions
until one closes — that is fitting a convention to a target.

## Part 5 (2026-09-14) — the source read: 3 of 4 causes eliminated, Part 2 CONFIRMED, one cause left

Same producer, now 4/5. The targeted source read Part 4 named was done.

**Cause 2 and 3 eliminated — GGM (86), printed:**

    y_m - 3 y_{m+1} + (3 - q^{2+m}) y_{m+2} - y_{m+3} = 0

i.e. `a = (1, -3, 3 - q^{2+m}, -1)` — EXACTLY the operator Part 4 used at `x = 1`, with the
`q^{2+m}` attachment confirmed on the `y_{m+2}` coefficient. And the blocks are the three
`H^-_{k,m}(q)` with `(q;q)_n^3`, so rank 3 at u=0 is right.

**Cause 1 eliminated AND Part 2 independently CONFIRMED — GGM Theorem 11 (91)/(92):**
`det(W_m(q)) = 2`, constant; `J = [[0,0,1],[0,2,0],[1,0,0]]` exactly as read from OCR. So
`det W(q) det W(1/q) = 2 x 2 = 4` — **exactly the `c` Part 2 derived from
`det(RHS)/(pref^r det J)` without having seen (91)**. The whole (92) identity is
determinant-consistent (both sides -1). Part 2's arithmetic is now verified against the
source, not merely derived; only its ATTRIBUTION needed the Part 4 correction.

**The one remaining cause, now NAMED rather than vague.** GGM's own relation, printed just
above (91):

    H^+_{k,m}(q^-1) = (-1)^k H^-_{k,-m}(q)

The index **NEGATES** and a sign `(-1)^k` appears **per column**. So `W` at `q^-1` runs its
index the OPPOSITE way to what the propagation law assumes, and carries a column sign — which
is exactly the shape that produces a structured column-0 residue. The law's second factor must
be rebuilt through that printed relation instead of a bare `q -> 1/q` substitution on the
companion matrix.

**Next honest step:** rebuild the second factor through `H^+_{k,m}(q^-1) = (-1)^k H^-_{k,-m}(q)`.
That is one derivation, not a convention search — the relation is printed.

## Part 6 (2026-09-14) — GGM (87)/(88) found: the blocker's MECHANISM is resolved

**Correction to Part 5's characterisation first.** Part 5 said the remaining step was "one
derivation, not a convention search -- the relation is printed". That was **over-confident**.
The `H^+/H^-` relation is printed, but how `W_m` is ASSEMBLED from the blocks was not in
anything I had read: Theorem 11 only says "`W_m(q)` is a fundamental solution". So the missing
piece was not a free choice and not a printed relation either -- it was a **definition I had
not located**. Located now.

**GGM (87)/(88):**

    W_m(q) = W^+_m(q)                                  |q| < 1
           = R . W^-_{-m-2}(q^-1) . diag(1,-1,1)       |q| > 1        (87)

    W^eps_m(q) = [ H^eps_{k, m+j} ]_{j,k}              rows = SHIFTS, cols = the 3 blocks  (88)

Two things fall out.

1. **My matrix convention was right** -- (88) has rows = shifts, so `W_{m+1} = A_m W_m` is
   confirmed, as Part 4 already inferred from (130)/(244).
2. **The mechanism of the residue.** In (92), with `l = -m-1` so `-l-2 = m-1`:

       second factor = W_{-m-1}(q^-1) = R . W^-_{m-1}(q) . S
       first  factor = W^+_{m-1}(q)

   so **(92) pairs TWO DIFFERENT block families**, `W^+` against `W^-`:

       (1/2) W^+_{m-1} (J S) (W^-_{m-1})^T R  =  RHS

   My propagation test treated `W(q^-1)` as "the same `W`, bar-substituted". It is not. That
   is a deeper error than the index direction Part 4 chased, and it explains the structured
   column-0 residue: a column sign `S` and a row reversal `R` sit in the identity, and the two
   factors obey DIFFERENT recursions.

**The Part-6 derivation was sound, applied to the wrong object.** Deriving from the printed
`H^+_{k,m}(q^-1) = (-1)^k H^-_{k,-m}(q)` gave `W_l(q^-1) = R W_{-l-2}(q) S`, which is
structurally (87) itself. The reasoning reproduced their definition; the mistake was assuming
ONE family throughout rather than the +/- pair (87) prescribes.

**What remains.** `W^+` solves (86) (Theorem 11). Whether `W^-` solves (86) or a different
recursion is NOT yet established -- the `H^-` series (90a-c) carry `(-1)^n q^{n(n+1)/2 + nm}`
against `H^+`'s `q^{n(n+1)+nm}`, so they are different objects and may well satisfy different
operators. That is the next thing to read or derive, and it is the last piece before the
rank-3 calibration closes.

## Part 7 (2026-09-14) — 🟢 GATE 1 DONE: the propagation law CLOSES, and the blocker was mostly mine

Producer `aomega_m3_pairing_propagation_closes_probe.py`, **3/3**.

**The law, derived with NO free parameters** from four printed inputs — (86) the recursion,
(88) the block matrix, (87) the two-branch definition, and Theorem 11, which supplies the
`W^-` law without a further lookup by making BOTH branches of (87) solve (86):

    W^-_{n-1}(q) = R Abar_{-n-2} R W^-_n(q)          [from Thm 11 applied to (87)'s |q|>1 branch]
    P_{m+1} = A_{m-1} . P_m . R . ([R Abar_{-m-2} R]^T)^{-1} . R

with `P_m` GGM's printed (92) RHS. **It closes EXACTLY** — verified at eight explicit integer
`m` with `q` carrying NO assumptions (G1), and symbolically in `m` under positivity (G2).

**Gate 1 of issue #7376 is done.** The rank-3 calibration holds.

### 🛑 The Parts 3-5 blocker had three causes and only ONE was mathematics

1. Part 3's m-invariance premise — wrong, retracted there.
2. **(real)** GGM (87) makes `W` at `q^-1` a DIFFERENT block family,
   `R W^-_{-m-2}(q^-1) S`, not "the same `W` bar-substituted" — found by Part 6's source read.
3. A **sympy artifact**: with `q` unassumed, `(1/q)^m` does not fold to `q^-m`, so entry (1,0)
   displayed as `q**m - 1/(1/q)**m` — identically zero, shown as nonzero.

So **two of the three were my harness**, and I characterised the whole thing as a
mathematical blocker across three parts. That ratio is the durable lesson here, not the law.

**Caveat, recorded rather than smoothed over (G3).** The nonzero DISPLAY is **path-dependent**:
this probe's own code path simplifies the entry to `0` outright, so the literal
`q**m - 1/(1/q)**m` is NOT reproducible here — only the vanishing is. A residue that reads zero
or nonzero depending on how `simplify` is reached is a WORSE hazard than a stable one, because
no fixed guard catches it. Declare assumptions on `q` and `m` in any symbolic q-difference work.

**Next:** gate 2 (rank 2, 4_1) should now follow the same derivation; then rank 6, where the
same machinery applies and Part 1's `det W_m = q^{4m} det W_0` supplies the shape.

## Part 8 (2026-09-14) — 🟢 GATE 2 DONE, by a DIFFERENT route than gate 1

### 🛑 Correcting Part 7's forecast

Part 7 said gates 2 and 3 were "the same derivation applied twice, with no open questions in
between". **Wrong.** GGM sec-011 line 208: for 4_1, the `|q| > 1` case "can be obtained by
**analytic continuation**". There is **no** two-branch piecewise definition like (87). So:

| knot | how `W(q^-1)` is obtained |
|---|---|
| 5_2 (u=0) | **(87)**: a piecewise definition, `R . W^-_{-m-2}(q^-1) . diag(1,-1,1)` — a DIFFERENT block family |
| 4_1 | **analytic continuation** of the same function — genuinely `W` bar-substituted |

So Parts 3-5's bar-substitution assumption was **right for 4_1 and wrong for 5_2**. The two
knots have structurally different `W(q^-1)`, and that is not an artifact of how I read them.

### Gate 2, done

Propagating 4_1's printed (137) `G_{-1,-1} = [[x^-2+x^-1-1, 1],[1,0]]` by the companion matrix
of (135) gives, at every step, entries that are Laurent polynomials and determinants that are
unit monomials:

    G_{-1,-1}  det = -1
    G_{0,-1}   det = -x^3      Laurent: yes
    G_{1,-1}   det = -x^6      Laurent: yes
    G_{2,-1}   det = -x^9      Laurent: yes

which is exactly what (138)'s `GL(2, Z[q^+-, x^+-])` claims, verified rather than assumed.

**Third independent confirmation of Part 1.** That determinant ladder steps by `x^3` per index
— precisely the Casoratian ratio Part 1 derived for 4_1 and calibrated against GGM's printed
(136). Part 1's rule has now been confirmed three separate ways: against (136) directly, via
the Part 2 bar-involution constant against (91), and now via this propagation.

### What gate 3 actually needs

Not "the same machinery" but a prior question, now sharply posed: **does the pretzel's `W`
follow 5_2's (87)-style two-branch structure or 4_1's analytic continuation?** The pretzel is
level 2 with a `q^{1/2}` grading (#7333), which is exactly the kind of structure that forces a
branch definition — but that is a guess and is labelled one. It must be read or derived, not
assumed, and it is THE question gate 3 turns on.

## Part 9 (2026-09-14) — gate 3's prior question ANSWERED from the source; my guess was wrong

Part 8 posed the question gate 3 turns on — does the pretzel's `W` follow 5_2-at-u=0's
two-branch (87), or 4_1's analytic continuation? — and guessed, **labelled as a guess**, that
the level-2 `q^{1/2}` grading "would force a branch definition".

**It does not.** GGM **§7, Theorem 28** — "One-dimensional state integrals and their
descendants", which is exactly the pretzel's setting (#7152 Part 11 derived its state integral
as one-dimensional) — gives the GENERAL family:

    (331)  W_m(x,w;q) = [ B^{(k)}_{m+j} ]_{j,k}          rows = shifts, cols = the r blocks
    (332)  Bhat = prod_{k=1..r} (1 - x_k S_m)  -  (-q)^A w^-1 q^m S_m^A

and part (b) states the entries are **holomorphic functions of `|q| != 1`** — ONE definition on
both regions, no piecewise branch. So the pretzel follows **4_1's structure**, and its
propagation law's second factor is the bar-substitution form: the one Parts 3-5 originally
assumed, which was wrong only for 5_2 at u=0.

**Level-2-ness lives in `A` and the `x_k`, not in a branch structure.** Good thing the guess
was labelled.

### Bonus: (332) CONFIRMS #7333's derived operator against GGM's general theorem

#7333 derived `P(X) = q^{A/2} w prod_j (1 + a_j X/Q) - X^A` from the contour shift and
Faddeev's functional equation, having only GGM's 4_1 and 5_2 SPECIAL cases to check against.
(332) is the same shape — a product of `r` linear factors in the shift, minus a term carrying
`S^A` — and the degrees agree across all three:

| knot | r | A | max(r, A) | #7333's derived degree |
|---|---|---|---|---|
| 4_1 | 2 | 1 | 2 | 2 |
| 5_2 | 3 | 2 | 3 | 3 |
| pretzel | 6 | 2 | **6** | **6** |

The pretzel's `r = 6` (2 unit dilogarithms + 4 from the doubled `Phi_b(2v - c_b)`) is exactly
the degree #7333 derived independently. That is a cross-check #7333 could not run, because it
did not have Theorem 28.

**Gate 3 is now unblocked**: use the bar-substitution propagation law with (332)'s companion at
`r = 6, A = 2`, and Part 1's `det W_m = q^{4m} det W_0` for the determinant shape.

## Part 10 (2026-09-14) — GATE 3 DONE: the SL-vs-GL choice is FORCED by the Casoratian ratio

Probe: `computations/probes/aomega_m3_gate3_determinant_ladder_probe.py` (2/3; T1 is a
deliberate negative). The bean's title question — "derive the pretzel's GL(r) normalisation" —
has its **group** half answered, and it was never a per-knot choice.

**The derivation.** GGM's pairing has the shape `W_M(q) J W_L(q^-1)^T = G_{M,L}` (the (92) /
(137) family). Taking determinants and using Part 1's Casoratian ladder
`det W_{m+1} = ratio * det W_m` (ratio = `(-1)^r a_0/a_r`, GGM Thm 16(c)) on BOTH factors:

    det G_{M,L} = ratio^M * ratio_bar^L * det J * c ,      ratio_bar = ratio|_{q->1/q, x->1/x}

with `c` Part 2's pairing constant. **Every index dependence of the pairing determinant is the
Casoratian ratio, and nothing else.** So:

    ratio^M * ratio_bar^L identically 1   <=>   det G is index-independent   <=>   SL is available
    otherwise                                                                     GL, never SL

That is a statement about the operator's end coefficients alone — `a_0` and `a_r` — and it is
decided before any matrix is written down.

**Calibrated 2-for-2 against GGM's own printed choices**, which is what makes it a derivation
rather than an observation:

| knot | ratio | `ratio^M ratio_bar^L` | predicts | GGM prints |
|---|---|---|---|---|
| 4_1 | `q/x` | `(q/x)^{M-L}` | GL | **GL(2, Z[q^+-, x^+-])** (138) |
| 5_2 at u=0 | `1` | `1` | SL | **SL(3, Z[q^+-])** (93) |
| (-2,3,7) | `q^4` | `q^{4(M-L)}` | **GL, not SL** | — none printed |

**The pretzel prediction:** `det G_{M,L} = q^{4(M-L)} * det J * c`. A nonconstant unit monomial,
so **SL is impossible off the diagonal `M = L`** and the normalisation group is GL(6). The
q^4 is Part 1's measured pretzel ratio (end-pair root `q^{2/3}`, no palindrome gauge).

**A second independent grouping.** On index-dependence the pretzel groups with **4_1**, not with
5_2-at-u=0 — the same partition Part 9 found from the branch structure (Theorem 28's single
holomorphic definition vs (87)'s two branches). Two unrelated features, same split.

**What this does NOT close (T1, recorded as a failing assertion on purpose).** `det J` and `c`
individually. The ladder gives their PRODUCT's index dependence; pinning the constant needs the
explicit rank-6 pairing blocks, and no held source prints a rank-6 pairing. That is the same
missing input `qou-lzzi` names — a normalisation, not new q-series data — now reduced from
"the whole GL(r) normalisation" to "one constant".

### Arc meta-finding (Parts 1-10)

Five self-corrections in ten parts, and **every one was resolved by reading more of GGM, not by
computing more**: Part 1's G3 wording (fixed by Part 2's G5), Part 2's attribution of (92)/(93)
(fixed by Part 4 — they are the u=0 specialisation), Part 3's premise (retracted outright), Part
5's "no free choices" (Part 6: a definition not yet located), Part 8's guess (Part 9: Theorem 28).
Three of the five looked like compute bugs and were source-reading gaps. The one genuine compute
bug found in the tranche — Part 12b's `(-1)**(-k)` float — was found by reading a WITNESS, also
not by computing.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-14 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
