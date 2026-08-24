# The operator-selection LP's objective is vacuous, its argmin is not a point, and its claimed optimizer is not one

**Date:** 2026-08-24 · **Bean:** `qou-v7qj` · **Probe:**
[`computations/meson/operator_selection_lp_objective_audit.py`](../../computations/meson/operator_selection_lp_objective_audit.py)

Follow-up to [Obstruction A](2026-08-24-meson-braid-obstruction-a-measured.md).
That audit proved the LP's optimum cannot be a braid image. This one asks *why*,
and the answer is not about braids, convention D, or the radical. It is that the
program in [`prop:operator-selection-lp`](../../content/quantum-observable-universe/mass-theory/operator-selection-lp.md)
does not do what its own prose says it does.

Everything below is symbolic over `ℚ(q)` except where a pin is named.

## Defect 1 — the objective is bounded below by one of its own constraints

The NF basis begins with the empty word, `b₁ = 𝟏`. Therefore

$$G_{1j} \;=\; \mathrm{tr}_M(\mathbf{1}\cdot b_j) \;=\; \mathrm{tr}_M(b_j) \;=\; t_j,$$

i.e. **the first row of the Gram matrix is the objective vector.** Verified
symbolically, all six entries, `G[0,j] − t[j] = 0`.

So the Frobenius positivity constraint at `i = 1`,

$$\sum_j G_{1j} x_j \;\ge\; 0,$$

*is literally* `t·x ≥ 0` — the objective, bounded below by zero. The program
minimises `t·x` subject to `t·x ≥ 0`, so

> **the optimal value is exactly `0` whenever the program is feasible.**

This is general: it needs only that the basis contains the identity, which the
NF basis always does. It holds for every `n`, every `q`, and **every trace
convention** — it is not a convention-D artifact and is not caused by the
singular Gram.

Two consequences that were previously recorded as separate puzzles are just this
one fact:

- `primal_obj = 0` at every target — necessarily, not coincidentally.
- `y₀* = 0` — forced, since strong duality gives `n_target · y₀* = 0` with
  `n_target > 0` free. The dual's "shadow price of the net constraint" reading
  in the interpretation block therefore describes a quantity that is
  identically zero, and `n_target` cannot influence the objective at all.

## Defect 2 — the argmin is a positive-dimensional face, so "the solution" does not exist

The optimal set is `{x : Σx = n, (Gx)₁ = 0, (Gx)_i ≥ 0 (i ≥ 2)}` — six unknowns
under two equality constraints, so a 4-dimensional affine space cut by five
inequalities (3-dimensional once the convention-D quotient condition `v·x = 0`
is added). It is not a point.

Enumerated at the proton pin over all active sets: **six distinct optimal
vertices**, every one at objective `0`.

| tight set | `x*` |
|---|---|
| `(1,2,3)` | `−1.3148, −1.4594, −1.4594, +3.2482, −1.6199, +3.6054` |
| `(1,2,4)` | `−1.3148, −1.4594, −1.4594, −1.6199, +3.2482, +3.6054` |
| `(1,3,5)` | `−0.6174, −0.6853, +1.8520, +2.0557, −0.7607, −0.8443` |
| `(1,4,5)` | `−0.6174, −0.6853, +1.8520, −0.7607, +2.0557, −0.8443` |
| `(2,3,5)` | `−0.6174, +1.8520, −0.6853, +2.0557, −0.7607, −0.8443` |
| `(2,4,5)` | `−0.6174, +1.8520, −0.6853, −0.7607, +2.0557, −0.8443` |

They come in **mirror pairs** under `σ₀ ↔ σ₁`, which is the short proof that no
unique optimum can exist: `t` and `G` are mirror-invariant, so the optimal set
is mirror-closed, and none of these vertices is mirror-symmetric.

> **🛑 RETRACTION.** [Obstruction A](2026-08-24-meson-braid-obstruction-a-measured.md)
> and PR #5702 state that *"the LP does select a canonical, parameter-free
> direction in `H₃(q)`"* and give `x*(1) = (−0.61738763, …)`. **That is wrong.**
> It is row `(1,3,5)` of the table above — one arbitrary vertex among at least
> six, selected by the solver's pivoting rule, and its mirror `(2,3,5)` is
> equally optimal. Nothing canonical is being selected. The symbolic closed form
> for that vertex, the lattice-membership result, and the rank-deficiency result
> all stand as statements *about that vertex*; only the word "canonical" fails.

## Defect 3 — the optimizer the corpus claims is not a minimiser

[`prf:operator-selection-lp`](../../content/quantum-observable-universe/mass-theory/operator-selection-lp-proof.md)
tabulates the `n = 3` optimum as `x* ≈ (+0.998, −0.010, +0.009, +0.046, −0.044, 0)`
= `NF(𝓑₃)`, and the interpretation block says the LP *"selects the Borromean
link `𝓑₃` as the unique optimizer."*

Computing `NF(𝓑₃)` for `𝓑₃ = (σ₀σ₁^{-1})³` directly (using `σ^{-1} = σ − h`) and
evaluating at the proton pin reproduces that table **to every printed digit**:

```
NF(B_3) = +0.998090, -0.009537, +0.009137, +0.045616, -0.043706, +0.000000
net     = +0.999601
obj     = t.x = tr_M(Phi) = +0.998562
min (Gx)_i = +3.42e-01   -> strictly feasible
```

So `𝓑₃` is **feasible but not optimal**: its objective is `0.998562` against an
optimum of `0`. The stated program does not select it, and is not close to
selecting it — the gap is the entire range of the objective.

This is the substantive defect. The other two are about the program being
ill-posed; this one says that even taken at face value, it returns something
other than the physics it is cited for.

## How this survived: the number was already in the witness

`prop:operator-selection-lp` names its own producer,
[`computations/operator_selection_lp_symbolic_qq.py`](../../computations/operator_selection_lp_symbolic_qq.py),
and the committed witness
[`operator-selection-lp-symbolic-qq.witness.json`](../../computations/operator-selection-lp-symbolic-qq.witness.json)
records

```
/data/h3/optimal_value = 0
```

So defect 1 was **already measured and committed**. Nothing was hidden and no
new computation was needed to see it — the witness said the optimum is `0`
while the interpretation block said the program "selects the Borromean link
`𝓑₃` as the unique optimizer", and the two were never read against each other.

The lesson is narrow and worth stating: a witness field agreeing with a
degenerate answer is not the same as the prose being checked. `optimal_value: 0`
reads as unremarkable — a clean number — unless someone asks what it *implies*
about the objective, which is that the objective cannot be doing any selecting.

## Why this explains Obstruction A

The three degeneracies previously recorded of `Φ*` — trace-free, trivial dual,
and `rank ρ_std = 1` (singular in the standard block) — are what a linear
program returns when its objective duplicates a constraint: it lands on a
degenerate face and the "answer" is a vertex of that face rather than a selected
operator. Meanwhile `𝓑₃`, the intended answer, is invertible with
`tr_M ≈ 0.9986`. Every property the LP's optimum has, the intended answer lacks,
and vice versa.

So Obstruction A is not evidence against braid-valued operator selection. It is
evidence that this particular program is mis-specified.

## What is NOT concluded here

- **No replacement objective is proposed.** Choosing one is a decision about the
  physics, not a repair an audit can make.
- One numerical observation is recorded **as a hypothesis only**, because it is
  exactly the kind of coincidence this corpus punishes: `tr_M(𝓑₃) = 0.998562`
  and `Σ NF(𝓑₃) = 0.999601` are both `≈ 1`, and `n_target ≈ 1.000` for the
  proton. That is consistent with the intended constraint having been
  `t·x = n_target` (trace *matched* to the target) rather than `Σx = n_target`
  with `t·x` minimised — i.e. with the objective and the net constraint having
  been conflated. **It is equally consistent with `n_target` having been chosen
  as `≈ 1` in the first place**, which would make the agreement circular. It
  needs the author's intent, not more arithmetic.
- Convention D is untouched by all of this. Defect 1 holds in every convention.
