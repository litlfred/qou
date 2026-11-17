---
# qou-v7qj
title: 'GAP: is the radical quotient the right repair for the convention-D operator-selection LP?'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T21:23:19Z
updated_at: 2026-10-10T07:47:09Z
parent: qou-cdx1
---

## Where this comes from

`qou-pb1w` is closed. Its last result: the convention-D operator-selection LP,
run on the `H₃(q)/rad` quotient, selects a canonical parameter-free direction
`Φ*` — and **no element of the coset `Φ* + span(v)` is a nonzero scalar
multiple of a braid image.** Proved symbolically over `ℚ(q)`, not searched.
Probe: `computations/meson/operator_selection_lattice_symbolic.py`; audit:
`docs/audits/2026-08-24-meson-braid-obstruction-a-measured.md`.

The exclusion is scope (b) with the invariant named — every braid word of
exponent sum `e` sits at `χ_sym = qᵉ`, `det ρ_std = (−1)ᵉ`, `χ_alt = (−1/q)ᵉ`
in the Wedderburn decomposition `H₃(q) ≅ ℚ(q) ⊕ M₂(ℚ(q)) ⊕ ℚ(q)`, hence
satisfies `χ_sym·χ_alt = det ρ_std` identically, and `Φ*`'s coset does not.

## The open question, stated sharply

**The two facts are the same fact, and that is what needs explaining.**

- The radical `v` (`vᵢ = (−1/q)^{ℓ(wᵢ)}`, the q-antisymmetriser) is what makes
  the convention-D Gram singular. Quotienting by it is the repair that turns a
  degenerate LP — unbounded in a direction neither the constraints (`Gv = 0`)
  nor the objective (`t·v ≈ −4.4e-16`) can see — into a finite optimum with a
  non-degenerate active set.
- `χ_alt(x) = v·x` **exactly**. So the quotient condition `v·x = 0` **is** the
  vanishing of the alternating character.

So the repair for LP degeneracy is, verbatim, the condition that forbids the
answer from being a braid. That is not a coincidence to note and move past —
it is the whole content of Obstruction A under convention D.

## What would count as progress

Any one of these, in rough order of how cheap it is to settle:

1. **Is the quotient the right repair at all?** It is one way to fix an
   unbounded polyhedron. Alternatives that do not annihilate `χ_alt`: a
   different normalisation in place of `Σx = 1`; bounding via a norm rather
   than a linear condition; keeping the full space and regularising the
   objective. Each gives a different `Φ*` with, in general, `χ_alt ≠ 0`.
2. **Is the objective right?** `primal_obj = 0` and `y₀* = 0` at every target
   — the minimum-action operator is trace-free and the dual certificate is
   trivial, so `n_target` is a pure scale rather than a selector. A program
   whose dual carries no information is weak evidence that the program is the
   intended one.
3. **Should the LP select a braid at all?** Possibly the honest reading is
   that it selects an algebra element and the braid is recovered downstream by
   a different map. If so, say it explicitly in `prop:operator-selection-lp`,
   because the current framing invites the braid reading.
4. **Does convention C behave differently here?** Under C the Gram is
   non-singular (`det = −0.1892`, cond 34), so there is no radical, no
   quotient, and no forced `χ_alt = 0`. That does **not** reopen C — the owner
   ruling of 2026-08-15 is not up for renegotiation — but the contrast
   localises exactly what D's singularity costs, and is cheap to measure.

## What is NOT open

- **Integrality.** `Ψ = D·Φ* = (−q³, −q⁴, N, −q⁵, qN, −q⁶)` with
  `N = q⁶+q²+1` and `D(q) = (q+1)(q⁶−q⁵−q³+q²+1)`: every entry a polynomial
  with integer coefficients. `Φ*` **is** in the `ℤ[q,q⁻¹]`-lattice up to one
  scale, so no integrality argument forbids it. That candidate obstruction was
  tested and does not fire.
- **Whether `G⁻¹` blocks this.** It does not, twice over: the LP uses `G` only
  as `Gx ≥ 0`, and `G_PINV` exists and is owner-approved. Both of my earlier
  "blocked" claims were wrong and are retracted in the audit.

## Discipline note

The exclusion above is a **structural** (b) result, resting on a proved
invariant, not on a search coming back empty. Do not weaken it to "we could
not find a braid". Equally, do not read it as refuting the framework: it says
the convention-D LP on the quotient selects an algebra element that no braid
realises, which relocates Obstruction A rather than closing off the program.

## 2026-08-24 — ANSWERED, and the question was wrong

This bean asked whether the radical quotient is the right repair. That framing
put the blame on convention D and the radical. **Both are innocent.** Two
corrections, in order of importance.

### The obstruction is RANK, not `χ_alt`

The bean (and the merged Obstruction A audit) lead with `χ_alt(Ψ) = 0` and the
observation that this *is* the quotient condition `v·x = 0`. True, but it is the
**gauge-dependent** half — it only kills the single point `s = 0` of the coset.

Measured: `rank ρ_std(Φ*) = 1`, not 2 — the optimum is **singular in the
standard 2-dimensional block**. A braid image has rank 2 (verified as a control
on `NF(σ₀σ₁)`), since braids are units in `H₃(q)` (`σ⁻¹ = σ − h`). And
`ρ_std(v) = 0`, so the whole gauge orbit shares that rank. That is what
`F(s) = −s³·(…)` was saying: the vanishing `s¹` coefficient **is**
`det ρ_std(Ψ) = 0`.

### The cause is the objective, and it has nothing to do with convention D

`b₁ = 𝟏`, so `G[1][j] = tr_M(𝟏·b_j) = t_j`: the first row of the Gram matrix
**is** the objective vector, and the Frobenius constraint at `i = 1` is
`t·x ≥ 0`. The LP minimises `t·x` subject to `t·x ≥ 0`, so **the optimum is
identically 0** — for every `n`, every `q`, every convention. `y₀* = 0` follows
by strong duality. The argmin is a positive-dimensional face (≥ 6 vertices at
`n = 3`, in mirror pairs), and `NF(𝓑₃)` — the corpus's claimed optimizer — is
feasible but **not** optimal, at objective `0.9986`.

So the trace-free optimum, the trivial dual and the rank-1 degeneracy are one
fact, not three: a linear program whose objective duplicates a constraint lands
on a degenerate face, and the returned vertex is the solver's pivoting rule.

**Retracted:** this bean's claim that the LP "selects a canonical parameter-free
direction". It does not; that direction is one vertex of six.

Full analysis:
`docs/audits/2026-08-24-operator-selection-lp-objective-defect.md`.
Probe: `computations/meson/operator_selection_lp_objective_audit.py`.

### What is still open, restated

Not "is the quotient the right repair" but: **what objective was intended?**
`prop:operator-selection-lp` has been corrected to state the degeneracy, and
deliberately does not propose a replacement — choosing one is a decision about
the physics. The one numerical hint, recorded as a hypothesis only because it
may be circular: `tr_M(𝓑₃) = 0.998562` and `Σ NF(𝓑₃) = 0.999601` are both ≈ 1
and `n_target ≈ 1.000` for the proton, which is consistent with the intended
constraint having been `t·x = n_target` rather than `Σx = n_target` with `t·x`
minimised — and equally consistent with `n_target` having been picked as ≈ 1.


## 2026-08-25 — ANSWERED from the literature: the selection principle exists

Birman–Menasco, *Studying links via closed braids III* (Pacific J. Math. **161**,
1993), ingested as `library/pjm-v161-n1-p02-p/` in #5707 and unread until now.

**Classification Theorem (Version I):** a link represented by a closed 3-braid
admits a **unique conjugacy class** of 3-braid representatives, except for
(i) the unknot (3 classes), (ii) `(2,k)` torus links with `k ≠ ±1` (2 classes),
(iii) links admitting braid-preserving flypes (≤ 2 classes). And the conjugacy
problem in `B₃` has algorithmic solutions *"each yielding unique normal forms
for conjugacy classes"*.

So: **link type → conjugacy class → canonical word**, all determined, none of it
optimization. That is the non-invariant data my class-function obstruction
showed no invariant could supply — and it comes from topological input, not from
a program.

`𝓑₃ = (σ₀σ₁⁻¹)³` checks clean against all three exceptions (Brunnian, not a
torus link, and every exponent is `±1` where the flype family needs `|·| ≥ 2`),
so **the Borromean link determines its conjugacy class uniquely**.

**Consequence for Obstruction A:** the corpus's meson braid `𝔐 = (σ₀σ₁)²σ₁σ₀`
closes to T(2,5), which is exception (ii). It therefore does **not** have a
unique 3-braid representative — two conjugacy classes. Any argument treating
"the meson braid" as determined by its closure is under-specified for this link
specifically, and that is a known ambiguity rather than a corpus defect.

Scope: braid index 3 only. Birman–Menasco are explicit that the pathologies of
papers III–V obstruct generalisation to higher index.

Full analysis: `docs/audits/2026-08-25-closed-3-braid-selection-principle-exists.md`.


## 2026-10-10 re-audit verdict: **LIVE** (bean `qou-am5t`)

Is the radical quotient the right repair for the convention-D operator-
selection LP? Open mathematics downstream of D, not a C site. Live.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.

## Round 77 Progress (2026-11-17T12:34:08Z)
- Advanced in PR `litlfred/qou#8342` (branch `feat/round77-uicgate-deuteron1st-ecatrad-polydom-magnusbound-43c1`, head `5cf054672f4eaf9dc177beab1666e1bca45dbc19`).
