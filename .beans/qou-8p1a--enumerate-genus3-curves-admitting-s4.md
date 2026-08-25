---
# qou-8p1a
title: 'qou-8pl1/a: enumerate ALL genus-3 curves admitting S_4 (no heavy infra needed)'
status: completed
type: task
created_at: 2026-08-07T00:00:00Z
updated_at: 2026-08-07T09:20:00Z
---

Parent: `qou-8pl1`. **Do this one first** — it is pure finite group theory plus a
known classification, needs no algebraic-geometry stack, and it bounds the whole
problem.

## Why

`computations/s4_genus3_competitor_fermat.py` proved the S_4 bridge has no
separating power by exhibiting ONE competitor (the Fermat quartic, |Aut| = 96,
S_4 verified by element-order profile {1:1, 2:9, 3:8, 4:6} + V_4 normal + full
S_3 action on V_4\{1}). The natural next question is how bad it is: is the
competitor set {Klein, Fermat}, or is it large?

## Task

The automorphism groups of genus-3 curves are **completely classified** (Broughton;
Magaard–Shaska–Shpectorov–Völklein; Kuribayashi–Komiya for the hyperelliptic
cases). Enumerate the classification and select every entry whose group contains
a subgroup isomorphic to S_4.

Known so far, to be confirmed and extended:
* Klein quartic `x^3 y + y^3 z + z^3 x`, Aut = PSL(2,7), order 168 — S_4 is the
  point stabilizer on the 7 Fano points.
* Fermat quartic `x^4 + y^4 + z^4`, Aut = (Z/4)^2 : S_3, order 96 — S_4 = V_4 : S_3,
  machine-verified.
* Candidates to check: the order-48 family, the hyperelliptic genus-3 curves,
  `y^3 = x^4 - 1`, and any curve with Aut of order divisible by 24.

## Deliverable

A table (curve / defining equation / |Aut| / structure / contains S_4?) with the
S_4 embedding exhibited concretely where it exists, following the matrix-group
style already used for the Fermat case. Exact arithmetic; no floats.

## Why it matters

* If the S_4-admitting set is exactly {Klein, Fermat}, then ONE extra invariant
  separating those two settles `qou-8pl1`, and the problem is small.
* If the set is large, the S_4 bridge is not merely non-selective but nearly
  vacuous, and the colour route needs a different organising datum entirely.

Either outcome is publishable content for the chapter's §5.


---

## RESULT (2026-08-07) — the second branch is the true one

**The S_4-admitting genus-3 curves are an INFINITE one-parameter family, not a
short list.**  `computations/s4_genus3_pencil_infinite_family.py`, exact
arithmetic, all checks pass; witness
`computations/s4-genus3-pencil-infinite-family.witness.json`.

The S_4-invariant ternary quartics form a **2-dimensional space**, i.e. a
**pencil**

    C_L : x^4 + y^4 + z^4 + L*(x^2 y^2 + y^2 z^2 + z^2 x^2) = 0

and `C_L` is smooth -- hence genus 3 -- for every `L` outside `{2, -2, -1}`.
The Fermat quartic is just the member `L = 0`.  So the bean's table came out
as: not `{Klein, Fermat}`, but a `P^1`.

Machine-verified: order-24 group faithful in `PGL_3` with element-order profile
`{1:1, 2:9, 3:8, 4:6}` (pins `S_4`; `SL(2,3)` is excluded by its single
involution and eight order-6 elements); `V_4` normal with full `S_3` action;
commutant in `M_3(Q)` is 1-dimensional (absolutely irreducible); invariant
quartics 2-dimensional; singular parameters exactly `{2, -2, -1}` via exact
polynomial identities `4 - L^2` and `(2-L)^2(2+2L)` plus an explicit verified
singular point at each; genus `(4-1)(4-2)/2 = 3`.

Infinitely many `L` give infinitely many **isomorphism** classes because the
fibres of `L -> [C_L]` are finite: `Aut` of a genus-3 curve is finite and
`N_{PGL_3}(S_4)` is finite (its centralizer is trivial by the scalar commutant).
Only *finiteness* of `Aut` is used -- the sharp Hurwitz bound is deliberately
avoided, an earlier step of this arc having been withdrawn for misusing it.

**Consequence:** the S_4 bridge is not merely non-selective between two
candidates, it is **nearly vacuous** -- it fails to cut a `P^1` down at all.
See the re-scope notes now appended to `qou-8p1b` and `qou-8p1c`.

Scope-(a): the bridge ARGUMENT is refuted; the Bring -> Klein degeneration
itself remains open.

Not verified here: the `L` at which Klein sits in the pencil (needs
`Q(sqrt(-7))`), and the hyperelliptic genus-3 curves admitting `S_4`, which lie
outside the pencil and only enlarge the competitor set.
