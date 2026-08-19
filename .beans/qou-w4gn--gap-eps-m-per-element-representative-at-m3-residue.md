---
# qou-w4gn
title: 'GAP: eps_m per-ELEMENT representative at m>=3 — residue-level lattice model shown insufficient (Addendum 25)'
status: todo
type: task
created_at: 2026-08-11T11:21:33Z
updated_at: 2026-08-11T11:21:33Z
---


## Single-relation route: RULED OUT (2026-08-11, idle-window probe)

The cheapest route to a per-element representative is one five-term
relation seeded at the offending symbol. xi's symbols are the specific
elements z_1 (mult 2) and z_2 (mult 1), so per-element divisibility
m | n_j e(w_j) fails only where noted:

| m | z_2 needs fixing (m does not divide e(z_2)) | z_1 needs fixing (m does not divide 2 e(z_1)) |
|---|---|---|
| 2 | no | no |
| 3 | yes | no |
| 4, 8, 12, 24 | yes | yes |
| 6 | yes | no |

Fixing z_2 by subtracting a five-term relation seeded at (z_2, y)
cancels z_2 but introduces its other four arguments at multiplicity -1,
each then needing m | e(w). Swept over every admissible y in F_25
(alpha basis, alphabar^2 = 4 alphabar + 3):

    ZERO candidates at every m | 24.

So no single relation clears the obstruction. This does NOT close the
bean: multi-relation combinations (and relations seeded at other
positions, or acting on z_1 as well) are untested, and the search space
of coefficient vectors over the 506 relations is large. The negative is
scope-(a): one route, exhaustively excluded.

Convention note: this run measures e(z_1) = 15, e(z_2) = 22 against an
alpha-basis generator, where the merged probes report 9 and 2 against a
different generator. The dlogs differ by a unit rescaling; every
divisibility verdict agrees, as it must.

### 2026-08-19 (PR #5296, Addendum 32) — the target group, found

CGZ Remark 1.9 (arXiv:1712.04887v3 p. 8): the invariant is
`R_ζ ∈ (F_n^×/(F_n^×)^n)^{χ⁻¹}`, with `P_ζ ∈ H^×/H^{×n}` only its image
and the **lift** flagged unchecked in general. An eigenspace is proper
only when `μ_n ⊄ F`; every field in this programme was `Q₅(μ_{624m}) ⊇
μ_m`, so Lemma 2.4(e) was vacuous throughout.

Correct base is place-dependent: `K = Q(α)`, `α³−α²+1=0`, has two places
over 5. At the degree-1 one `K_v = Q₅ ⊉ μ₃`, `F₃ = Q₂₅`, and the
χ⁻¹-eigenspace of `B^×/(B^×)³` is the Teichmüller line — order 3 of 9,
with `5` outside it. Non-vacuous.

**Reverses half of Addendum 31.** `B = Q₂₅` *is* `F_n` there, and
`χ_B = teich(·)⁸` *is* the eigenspace projection. The root-dependence of
Addenda 27–29 belongs to the lift, not the field.

**Route closed:** Lemma 2.3 is an isomorphism `F^×/F^{×n} ≅ H¹(Φ,μ)`, so
the Kummer-cocycle reformulation computes the same object as Addendum 31.
Dead end; no probe spent on it.

**Still open:** the lift `P_ζ → R_ζ` at the degree-1 place (CGZ §3, via
Chern classes). No ε_m value claimed at m ≥ 3.
