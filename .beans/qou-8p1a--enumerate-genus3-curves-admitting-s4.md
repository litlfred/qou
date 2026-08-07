---
# qou-8p1a
title: 'qou-8pl1/a: enumerate ALL genus-3 curves admitting S_4 (no heavy infra needed)'
status: todo
type: task
created_at: 2026-08-07T00:00:00Z
updated_at: 2026-08-07T00:00:00Z
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
