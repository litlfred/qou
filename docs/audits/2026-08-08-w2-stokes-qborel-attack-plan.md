# W2 ∞-residual: staged attack plan for the q-Borel transform + the two Stokes multipliers

> **⚠ CONVENTION-C CONDITIONAL — scope note added 2026-09-06 (bean `qou-h6o3`).**
> This document's conclusions depend on the `c_k` precision ladder / `Q_β`, which
> AGENTS.md records as **convention-C-frame throughout and NOT re-derived** under
> the owner ruling of 2026-08-15 making convention D (`z = q³/(q²+1)`) canonical.
> Treat every `c_k`-dependent statement below as **C-conditional** until the
> ladder is re-derived (bean `qou-cds1`). The numbers here are correct *for C*
> and are kept as recorded — they need **scoping, not correction**. This note was
> applied mechanically to the 45 documents in this arc that reference the ladder;
> it asserts dependence on the ladder, not that any particular conclusion changes
> under D.


> **🛑 SUPERSEDED IN FRAMING (same day).** The RSZ route this plan is built on is
> **closed** — see [`2026-08-08-rsz-c1-infinity-route-closed.md`](2026-08-08-rsz-c1-infinity-route-closed.md).
> §3.3 is restricted to integral slopes; its level is `d := μ₂ − μ₁` (a slope
> *difference*, not a denominator); `dim F = 0` when `k = 1`; and C1 has one slope
> at `∞`. Bugeaud [14] lifts integrality but is **still two-slope**. Stages **S1,
> S2, S3 below are void as written** (they presuppose a level and an `A₁,A₂`
> that C1's `∞` does not have). **S0 stands** — the kernel formalization is
> correct for arbitrary `d` from the stated recurrence. The work moves to alien
> calculus; see the closure audit's final section.


**Date:** 2026-08-08 · **Axis:** C1 ∞-side (W2, `qou-xufp`; D-ladder `qou-dri7`,
`qou-b00b`) · **Tier:** plan + one formalize-first prune. No fit, nothing wired,
no `symbol=C1` claim, **no Stokes multiplier computed**.

Owner authorized overlap on this front. This plan is deliberately staged so each
stage has a *falsifiable* deliverable and the cheap structural checks run before
the expensive analytic ones — per the formalize-first probe discipline.

## The target

Per [`2026-08-01-c1-inf-slope-half-rsz-stokes.md`](2026-08-01-c1-inf-slope-half-rsz-stokes.md):
`L1 = (q²x−1)σ² − (q−1)σ − (q−1)` is Fuchsian at `0`, irregular at `∞` with
Newton slope **½** ⇒ RSZ level `d = 2`. Isoformal classes
`F(P₁,P₂) ≅ Matr_{1,1}(ℂ)² = ℂ²` ⇒ **two Stokes multipliers `U ∈ ℂ²`**.

Already in hand:
- `QBorelKernel` — the **level-1** kernel `tₙ = q^{C(n,2)}`, `t_{n+1} = qⁿ tₙ`.
- `QCharacter.ratio_qInvariant` — why the sector difference is theta/elliptic-valued.
- **`deg_q(cₙ) = n²`, proved for all `n`** over `Polynomial ℤ`
  ([`2026-08-08-c1-inf-degree-law-proved.md`](2026-08-08-c1-inf-degree-law-proved.md)),
  with the bridge to `c1FormalDeg`. This is the growth budget the transform must absorb.

## PRUNE (run first, and it already bites)

RSZ §3.3 resolves a level-`d` singularity with `B_{q,d}(Σ fₙzⁿ) = Σ (fₙ/tₙ)ξⁿ`,
kernel `tₙ = q^{n−d} t_{n−d}`, growth `q^{n²/2d}`. Iterating that recurrence on
degrees alone (no analysis needed) reproduces the stated growth:

| `d` | measured `deg tₙ / n²` at `n=400` | RSZ `1/2d` |
|---|---|---|
| 1 | 0.4988 | 0.5000 |
| 2 | 0.2487 | 0.2500 |
| 3 | 0.1654 | 0.1667 |
| 4 | 0.1237 | 0.1250 |

So the reading of the recurrence is right. Now compare against the proved
`deg_q(cₙ) = n²`:

| `d` | `deg(cₙ/tₙ) / n²` |
|---|---|
| 1 | **+0.50** |
| 2 | **+0.75** |
| 3 | +0.83 |
| 4 | +0.88 |

**No level `d` absorbs the `n²` growth, and larger `d` is strictly worse.** The
quotient stays divergent. Therefore the *unramified* `B_{q,d}` applied directly
to `Σ cₙ x^{−n}` cannot be the resolving transform, for any `d`.

**Reading (scope-(a), with an explicit caveat).** This is a consistency
computation on degrees, not a theorem about RSZ. Three ways it can be resolved,
and stage **S1** exists to decide which:

1. **Ramification is forced, not cosmetic.** A non-integral slope requires the
   pullback `z = ζ^d` *before* transforming (this is why RSZ needs the square
   roots `B₁,B₂` of the slope blocks). Re-indexing changes the effective growth,
   and the budget above is the quantitative reason the step cannot be skipped.
2. **Normalization mismatch.** `cₙ` may enter the transform after a gauge /
   shearing transformation, or in a different variable, so `deg = n²` is not the
   input growth.
3. **Slope→level convention.** If the correct level for slope `½` is not `d = 2`
   under RSZ's convention, the table is being read against the wrong `d`.

Until S1 settles this, **do not** invest in the analytic machinery of the
unramified transform — that is exactly the wasted-search the formalize-first
rule targets. Note the cost asymmetry: this prune took minutes; the analytic
route it guards is multi-session.

## S0 + S1 RESOLVED (2026-08-08, same day)

**S0 — done, sorry-free.** `QOU/MathlibExt/QBorelKernelLevel.lean`: closed form
`qBorelExp d n = (n/d)(n%d) + d·C(n/d,2)`, RSZ recurrence *proved* from it,
level 1 shown to reproduce the existing `qBorelKernel` on the nose, degree law
`qBorelExp d (d·m) = d·C(m,2)` (the `q^{n²/2d}` growth), and the concrete
`qBorelExp 2 (2m) = m(m−1)`. Axioms `[propext, Quot.sound]` — no `Classical.choice`.

**S1 — resolved to candidate (1): ramification is FORCED.** Extending the budget
table to the ramified variable settles it:

| input | `d=1` kernel | `d=2` kernel |
|---|---|---|
| unramified, `deg = n²` | +0.50 | +0.75 |
| **ramified** `z = ζ²`, `deg = N²/4` | −0.25 | **+0.0006 → 0** |

Under `z = ζ²` the coefficient `cₘ` sits at index `N = 2m`. Against the
**level-2** kernel the match is critical — and the leftover is not merely small
but **exactly linear**:

```
deg cₘ = m²,    qBorelExp 2 (2m) = m(m−1),    difference = m   exactly.
```

Sub-quadratic leftover is precisely the convergence condition, so the resolving
transform is **ramify, then level 2**. This is the quantitative reason RSZ's
square roots `B₁,B₂` are forced rather than cosmetic. The `d=1` ramified pairing
over-converges (−0.25) and is not canonical.

**Proved in Lean, sorry-free:** `QOU.QBeta.ramified_qBorel_budget` — `m² = m(m−1) + m`,
composing `cCoeff_natDegree` with `qBorelExp_two_even`.

*Caveat retained:* a degree-budget determination, not a theorem about RSZ's
analytic construction. It fixes which pairing *can* converge; it does not build
the transform. **S2 is unblocked and its target confirmed.**

## Stages

Each stage is a bean. Deliverables are stated so failure is visible.

### S0 — level-`d` kernel in Lean (`qou-qbk1`)
Generalize `qBorelKernel` from `d = 1` to general `d`: define `qBorelKernelLevel d`,
prove the recurrence `t_n = q^{n−d} t_{n−d}` and the **closed-form degree law**
(for `d = 2` the even/odd chains give `deg t_{2m} = m(m−1)`, i.e. `≈ n²/4`).
Cheap, purely algebraic, and it is the Lean statement of the table above.
*Deliverable:* sorry-free lemmas + `#print axioms` clean. *Falsifiable:* the
closed form either matches the recurrence or it does not.

### S1 — settle the growth budget (`qou-qbg2`) ← **do this before S2/S3**
Decide among (1)/(2)/(3) above by reading RSZ §3.3 against the C1 module: what
exactly is the input series to `B_{q,d}`, in which variable, after which gauge,
and what is its coefficient growth? *Deliverable:* a stated identity
`deg(input_n) = <expr>` plus the `d` for which `deg(input_n) − deg(t_n)` is
bounded. *Falsifiable:* if no `d` bounds it even after ramification, the RSZ
route as mapped is wrong and the mapping must be re-derived — a genuine negative
worth recording.

### S2 — ramification: the square roots `B₁,B₂` (`qou-qbr3`)
Compute the slope blocks `A₁,A₂` from `L1`'s Newton polygon at `∞`, then their
`d`-th (here square) roots. Concrete linear algebra over a suitable extension —
checkable exactly, no resummation yet. *Deliverable:* explicit `A_i`, explicit
`B_i`, with `B_i² = A_i` verified symbolically. *Gated on S1.*

### S3 — extract `U ∈ ℂ²` (`qou-qbs4`) — the RSZ-wild core
Sector-dependent q-Borel/Laplace summation and the cohomological / Birkhoff–
Guenther normal-form extraction of the two multipliers (RSZ §4–5, q-analog of
Birkhoff–Malgrange–Sibuya). *Deliverable:* the two multipliers with an
independent cross-check (e.g. the theta/elliptic ratio structure from
`QCharacter.ratio_qInvariant`). **Genuinely multi-session; not a session brick.**
*Gated on S1 + S2.*

## Discipline notes

- **Anti-fit.** `U` must be *derived*. A pair of constants tuned to make a
  downstream number land is a fit, must be labelled one, and may not be wired as
  canonical. The Q_β `Φ₂` precedent (the forbidden seventh ansatz) applies
  directly here.
- **Scope labels.** Any negative from S1/S2 is scope-(a) — "this construction as
  mapped does not resolve it" — unless a proved invariant excludes the ingredient
  outright, in which case cite the invariant.
- **Coordination.** `qou-xufp` (W2), `qou-dri7` (W9), `qou-b00b` (F1) are the
  owning beans; intent posted on PR #4721. S0/S1 are chosen to be disjoint from
  the analytic core so parallel work does not collide.

-- Ref: [ramis-sauloy-zhang-2013] https://arxiv.org/abs/0903.0853 (§3.3 q-Borel, §4–5 Stokes)
-- Ref: [manuscript] docs/audits/2026-08-01-c1-inf-slope-half-rsz-stokes.md
