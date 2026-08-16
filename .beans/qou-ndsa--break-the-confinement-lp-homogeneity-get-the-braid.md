---
# qou-ndsa
title: 'Break the confinement-LP homogeneity: get the braid into t or G, not just n_target'
status: in-progress
type: task
priority: high
created_at: 2026-08-07T17:16:15Z
updated_at: 2026-08-16T13:39:35Z
---

THE ONLY SURVIVING FORM of the owner's SDP-offset proposal (2026-08-07).

Two readings have now been excluded, each for a DIFFERENT structural reason,
and both exclusions point at the same fix.

1. ANGLE-STRUCTURE LP (qbeta_sdp_angle_offset_theta_probe.py): the offset
   x_geom - x_LP vanishes identically (2.4e-16, 5.0e-16) because both anchors
   sit at the symmetric point — 4_1 is 2 regular ideal tetrahedra, B_3 is the
   regular ideal octahedron decomposition. PROVED in general:
   QOU/Knot/SymmetricOptimum.lean `optima_coincide` — two concave objectives
   INVARIANT under the symmetry share their optimum. An informative offset
   needs a SYMMETRY-BREAKING objective.

2. CONFINEMENT LP (qbeta_confinement_sdp_offset_homogeneity_probe.py): the
   canonical program `min t.x s.t. 1^T x = n_target, Gx >= 0` is HOMOGENEOUS —
   Gx >= 0 is a cone, so the feasible set at net n is n times the fixed
   polytope at 1. Measured: x*(n) = (n/n0)x*(n0) to 5.7e-14, offset angle drift
   EXACTLY 0, ||offset||/n constant. Because t and G come from pyhecke.gram and
   are KNOT-INDEPENDENT, with only n_target = |tr_M(K)| varying, two knots give
   PARALLEL offsets: the angle is the same number for every knot and the
   magnitude is a constant times tr_M(K). One knot-dependent number, not two —
   ratio-shaped, hence unfalsifiable by `ratio_attained`.

THE COMMON DIAGNOSIS: in both cases the braid's own content never reaches the
part of the program that could break the degeneracy. In (1) the objective is
symmetric; in (2) the knot enters only the scalar net constraint.

THE TASK: find or construct a confinement formulation in which the braid's
operator content enters the OBJECTIVE t or the GRAM G — not merely n_target.
Candidates to examine:
  - `solve_frobenius_dual_lp(t, G, n_target, u_demand)` — the u_demand vector
    is a per-channel demand PROFILE, not a scalar. If u_demand is knot-derived
    and not proportional to a fixed vector, homogeneity breaks and the offset
    direction becomes knot-dependent. CHECK THIS FIRST — it is the cheapest.
  - a Gram built from the braid word itself (G_ij = tr_M(beta_K b_i b_j))
    rather than from the bare NF basis.
  - the dense-PSD lift (`operator_selection_sdp.rs`), where off-diagonal
    correlations enter and the diagonal-lift equivalence fails.

ACCEPTANCE BAR (unchanged, and it is the whole point): the formulation must
yield BOTH theta values ABSOLUTELY, with the metric/normalization fixed IN
ADVANCE, and land on the A-free curve
(L - theta_mu^2)/(L - theta_p^2) = S_mu/S_p = -0.2453912076. A ratio does not
qualify — that is Lean-proved, not an opinion.

Cross-refs: PR #4513; qou-qnnq (the gap), qou-offl, qou-krvm.

---

## 2026-08-16 — candidates 1 and 2 are BOTH ruled out, exactly

`computations/confinement_lp_braid_gram_probe.py` — exact in ℚ(q), stdlib only,
24/24 checks. Lean in `operator_selection_lp.lean`. Builds on `qou/k4f8`
(#5239), which found the structural fact this rests on: the `H₃` Frobenius
trace form is **singular**, `det G = 0` identically, radical
`v ∼ (−1/q)^len(wᵢ)` — the q-antisymmetriser — with `⟨𝟙,v⟩ = −(q−1)(q²−q+1)`.

### Candidate 1 (`u_demand`, "CHECK THIS FIRST — it is the cheapest") — dead

`solve_frobenius_dual_lp` (lp_dual_solver.py:114) constrains `Gx = u_demand` by
**equality**. Since `tⱼ = G₀ⱼ` (the basis contains `b₀ = 1`, so
`tⱼ = tr_M(b₀bⱼ)`), for *every* feasible `x`

```
t·x  =  Σⱼ G₀ⱼxⱼ  =  (Gx)₀  =  u₀
```

The objective is **constant on the whole feasible set**. This is worse than
homogeneity: there is nothing to optimise at all. A knot-derived `u_demand`
makes the answer knot-dependent only by reading one coordinate of its own
input back out. Lean: `objective_eq_demand_coord`,
`objective_constant_on_demand_fibre`. Exhibited concretely in the probe with
`x` and `x+v`.

And `u_demand` is not even free: `G` is singular, so `Gx = u` has a solution
only when `u ⊥ v`. Lean: `demand_perp_radical`.

### Candidate 2 (Gram from the braid word) — dead, and for a reason that generalises

Computed `G^w_{ij} = tr_M(w bᵢ bⱼ)` **and** `tr_M(bᵢ w bⱼ)` for nine braid
words — identity, both generators, `L₊`, `e⁻`, the trefoil `σ₀³`, two
alternating words, `σ₀²σ₁²σ₀`. In **every** case, both sides:

```
G^w v = 0      rank 5/6      det G^w = 0
```

The radical is untouched. The reason is not accidental: `V = Σⱼvⱼbⱼ` spans a
**two-sided ideal** (the sign block), so `(G^w v)ᵢ = tr_M(bᵢ w V) = 0` whatever
`w` is. And the other hypothesis is about the *cost* vector, not the Gram:
`⟨t,v⟩ = tr_M(V) = 0` says only that `V` lies in the radical of the trace form.

So all three hypotheses of `y_0_eq_zero_of_cost_perp_radical` survive and
`y₀ = 0` stays forced. **Decorating `G` cannot break the degeneracy.**

### The Lean was restated to make this the general statement

`y_0_eq_zero_of_cost_perp_radical` now takes `⟨t,v⟩ = 0` directly instead of
deriving it from "`t` is a row of `G`", so **nothing in its hypotheses
mentions where the Gram came from**. `y_0_eq_zero_of_radical` is now a
corollary. That is what makes it apply to every `G^w` at once rather than
one Gram at a time. Sorry-free.

### What this leaves — the search should be redirected

The degeneracy is the conjunction of

- **(a)** the cost vector is the Markov trace vector `tⱼ = tr_M(bⱼ)`, and
- **(b)** the Gram annihilates the trace form's radical.

**(b) is automatic** for anything of the form `tr_M(bᵢ w bⱼ)`. So the only
surviving move is to break **(a)** — change the *objective*, not the Gram.

That is the same conclusion this bean already reached for the angle-structure
LP by a completely different route ("an informative offset needs a
SYMMETRY-BREAKING objective"). Both halves of the diagnosis now point at the
objective, which is a stronger statement of the bean's own "the braid's
content never reaches the part of the program that could break the
degeneracy": for the confinement LP, the Gram is *not* such a part.

### Candidate 3 — the dense-PSD lift — also fails, for a third reason

Read the lift as actually written (`computations/sdp_moment_lift.py:194-208`).
The Lasserre moment relaxation **keeps every LP constraint** — `A_eq x = b_eq`,
`Gx ≥ 0`, the box — and *adds* `M = [[1,xᵀ],[x,X]] ⪰ 0`, `X ⪰ 0`,
`tr(GX) ≥ 0`. So its feasible `x`-set is a **subset** of the LP's, and
`min_SDP ≥ min_LP`.

That much says the SDP cannot do *worse*. What settles it is that the LP
optimum **survives the lift**: take the rank-one moment matrix `X = x*x*ᵀ`,
PSD by construction, and

```
tr(GX) = x*ᵀ(Gx*) = 0        because Gx* = 0
```

— every Frobenius constraint is already tight at the radical optimum, so
`tr(GX) ≥ 0` holds with equality and nothing is cut off. Hence
`min_SDP = min_LP = 0`, attained at the same `x*`.

Lean: `tightening_preserves_optimum`, stated for an **arbitrary** refinement
`Tighter` of `IsFeasible`. Only two hypotheses: it refines feasibility, and
`x*` still satisfies it. Neither mentions semidefiniteness. A tightening can
only help when it *cuts off* the incumbent optimum, and this one cannot,
because `x*` is exactly where all the constraints hold with equality.

Note the dual story is genuinely different here — worth recording so nobody
re-derives it. The moment block contributes `2Z₀ⱼ` to the `x`-block dual
equation, and `Σⱼ vⱼ·(∂M/∂xⱼ) ≠ 0`, so the moment lift **does** break the
`y₀ = 0` *forcing*. It just does not change the optimal *value*. Escaping the
dual argument is not the same as escaping the degeneracy.

### The criterion, for whatever is proposed next

`y_0_eq_zero_of_contribution_perp_radical` reduces all of this to one
question. Dual feasibility for the `x`-block of any conic program reads
`tⱼ = y₀ + cⱼ`, with `cⱼ = Σᵢ sᵢGᵢⱼ` for an LP, `cⱼ = ⟨Z,Mⱼ⟩` for an SDP with
lift `M₀ + Σₖ xₖMₖ`. Then:

> **`y₀ = 0` as soon as the constraint map annihilates the radical.**

So the one thing to check of any reformulation is whether `Σⱼ vⱼMⱼ = 0`. And
per candidate 3, even a formulation that passes that test still has to cut off
`x*` to change anything.

### Not claimed

That no confinement formulation can work — only that these two cannot, and
that Gram-decoration is the wrong axis. The acceptance bar (both θ values
absolutely, on the A-free curve) is untouched by this and remains the target.

## All three candidates are now closed

| candidate | why it fails |
|---|---|
| 1. `u_demand` profile | `t·x = u₀` for every feasible `x` — the objective is constant on the feasible set, so there is nothing to optimise |
| 2. braid-built Gram | `V` spans a two-sided ideal, so `G^w v = 0` for every `w`; `⟨t,v⟩ = tr_M(V) = 0` regardless of the Gram |
| 3. dense-PSD / moment lift | keeps `Gx ≥ 0` and only adds constraints, and `x*` lifts (rank-one `X = x*x*ᵀ`, `tr(GX) = 0`), so it cuts off nothing |

The common thread, which is the bean's own diagnosis sharpened: the braid's
content has to reach the **objective**. Candidates 1–3 all leave `t` alone.

## Next

- [ ] The only remaining axis is a genuinely different objective — one that
      breaks `⟨t,v⟩ = 0`, i.e. stops being the Markov trace vector on this
      basis. Whether such a thing is *motivated* rather than merely
      degeneracy-breaking is an owner question, not a mechanical one.
- [ ] Related: `qou/8na1` asks whether `prop:mass-coefficient-shadow-price`
      should read `y₀*` as a shadow price at all, given it is provably zero.
      That decision plausibly subsumes this bean's framing.
