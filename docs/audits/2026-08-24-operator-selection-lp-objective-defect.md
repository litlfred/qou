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


# What is derivable, and what the blast radius is

Added after the above, answering the two questions it left open. Probe:
[`computations/meson/operator_selection_what_selects_b3.py`](../../computations/meson/operator_selection_what_selects_b3.py).

## Derivable: **no linear objective can select `𝓑₃`** — the LP form itself cannot do it

At `NF(𝓑₃)` **all six** Frobenius positivity constraints are strictly slack:

| constraint | slack |
|---|---|
| `(Gx)₀` | `+0.998562164` |
| `(Gx)₁` | `+0.605509828` |
| `(Gx)₂` | `+0.619565652` |
| `(Gx)₃` | `+0.342488875` |
| `(Gx)₄` | `+0.409722223` |
| `(Gx)₅` | `+0.691166478` |

Zero of six active, and the boundedness constraints are slack for any sane `M`.
So with only `Σx = n_target` active, `𝓑₃` lies in the **relative interior** of
the feasible polyhedron inside that hyperplane.

A linear functional on a polyhedron attains its extrema on a **face**. If a
relative-interior point is a minimiser, the functional is constant on the whole
polyhedron — i.e. the objective vector is parallel to the equality normal, and
then *every* feasible point is equally optimal. Therefore

> **no linear objective selects `𝓑₃` as a unique minimiser** — not this
> objective, any objective.

**This refutes the hypothesis floated above.** Replacing `Σx = n_target` by
`t·x = n_target` swaps which hyperplane is the equality and leaves every
Frobenius slack untouched, so `𝓑₃` remains relative-interior. The `≈ 1`
coincidence was a red herring, as flagged.

### Two natural non-linear principles also fail

- **Minimum norm.** `argmin ‖x‖₂` on the hyperplane is the uniform point
  `(n/6)·𝟙`, which is feasible (min slack `0.610975`) and is not `𝓑₃`.
- **Maximum minimum-slack** (most robustly feasible). `𝓑₃` scores `0.342489`;
  the uniform point scores `0.610975` and beats it. So `𝓑₃` is not that either.

`𝓑₃` is not distinguished by the feasible geometry **at all**. Whatever selects
it is topological or physical — it is not an optimum of this constraint set.

## `rem:b3-local-minimum` — both of its claims are false

The block says: *"The confinement LP … admits a global minimum at
`tr_M = 0`. The Borromean solution `𝓑₃` is a local minimum at a vertex of the
LP feasible polytope."* The first sentence is **right**, and is a fourth
independent place the corpus already recorded defect 1 without drawing the
consequence. The second is wrong twice:

- **"at a vertex"** — zero of six Frobenius constraints are active. A vertex in
  `ℝ⁶` needs six active constraints; `𝓑₃` has one, the equality.
- **"a local minimum"** — exhibited constructively. Take `d` = the component of
  `−t` orthogonal to `𝟙`, so `Σd = 0` and the net constraint is preserved. Then
  `t·d = −0.268780394 < 0`, and stepping `s = 0.5`:

  | | |
  |---|---|
  | feasible | yes, min slack `+0.447890` (better than `𝓑₃`'s) |
  | `Σx` | `+0.999600646`, unchanged |
  | `tr_M(𝓑₃)` | `+0.998562164` |
  | `tr_M(new)` | `+0.864171967` |

  Strictly lower, strictly feasible, same net. Not a local minimum.

## Blast radius, in real terms

25 content blocks reference `prop:operator-selection-lp` or `prop:confinement-lp`.
The line that matters is whether a block depends on the **optimum / dual
variables** or only on the **Gram-and-trace data or feasibility**.

**Affected — these read the optimum or its duals:**

- **`prop:mass-coefficient-shadow-price`** — the most serious, because it reaches
  the mass formula. It asserts that *each coefficient of the six-term mass
  formula is the shadow price of the corresponding partition's Frobenius
  positivity constraint*. At `𝓑₃` every constraint is slack, so complementary
  slackness forces **every `yᵢ* = 0`**; at the actual optimum the active set is
  solver-dependent. Either way the coefficients are not well-defined by this
  route. *Scope note: measured at `n = 3`. The vacuous-objective defect is
  general-`n`, but whether the nuclear instance's solution is also
  relative-interior is **not** measured here.*
- **`prop:he4-channel-active-set`** — "active demand channels" are the tight
  constraints. Nothing is tight at `𝓑₃`.
- **`prop:knot-operator-lp-selection`** — selection by LP.
- **`rem:b3-local-minimum`** — falsified above.

**Unaffected — these use the data, not the optimum:**

- the Gram matrix and the Markov traces themselves, which are correct and were
  re-derived from the structure constants in the sibling probe;
- **`alg:lp-sdp-dual-emission`** and **`alg:witness-json-pipeline`** — an
  infrastructure contract about *emitting* dual fields, orthogonal to whether a
  particular program's duals mean anything;
- any claim that `𝓑₃` **satisfies** the Frobenius structure, which is true and
  now quantified: strictly, with min slack `0.342489`.

## The constructive residue

The LP is not worthless; it is mis-cast. `𝓑₃` being *strictly* feasible with
room to spare is a genuine certificate — it says `𝓑₃` is robustly compatible
with the Frobenius structure rather than marginally so. That is a
**verification** result and it stands. What does not stand is reading it as a
**selection principle**, and nothing in the LP form can be repaired into one.


# CORRECTION to my own blast radius: the mass formula does not depend on this

I wrote above that `prop:mass-coefficient-shadow-price` is *"the most serious,
because it reaches the mass formula"*. **Measured, that is wrong in the way that
matters**, and the correction is worth more than the original claim.

## The six-term formula does not cite it

`thm:six-term-mass-formula-complete` declares

```
uses: ["prop:terms-2-6-higher-operations",
       "prop:chirality-writhe-ribbon-derivation"]
```

The coefficients come from the **chirality / writhe / ribbon** route —
`a_K(β) = 1 + w(β)·h + O(h²)` from the Kauffman ribbon-twist evaluation — and
that route touches nothing in this audit. The shadow-price proposition is a
**parallel interpretive claim about the same numbers**, not the derivation the
formula runs on.

## The coefficients are computed in closed form, never by solving an LP

`prop:wigner-2-coefficient` gives, for self-conjugate `λ`, `C_λ = w_λ · h/2`,
and [`shadow_price_c_321_q0.py`](../../computations/shadow_price_c_321_q0.py)
evaluates the `k = 6` case algebraically:

$$C_{[3,2,1]} \;=\; \frac{[2]_q\,[4]_q\,[6]_q\,h}{2\,[3]_q^{3}\,[5]_q} \;=\; 0.03748823722039044429504997$$

at the proton pin, 50 dps. **No LP is solved anywhere in that derivation.**

## So the identification fails and the numbers survive

| | |
|---|---|
| closed-form coefficient | `0.0374882372204` — derived, fixed |
| LP dual at `𝓑₃` | `0` — forced, since every constraint is strictly slack |
| LP dual at the LP's optimum | solver-dependent (six vertices, mirror pairs) |

A nonzero derived constant cannot equal a dual variable that complementary
slackness pins to zero. **The identification is false; the coefficient is
untouched.** "Shadow price" is an interpretation attached to a number obtained
another way, and it is the interpretation that fails.

## Revised blast radius

**Interpretive claims that fail** — `prop:mass-coefficient-shadow-price` and its
proof block, plus the five blocks citing it in `uses[]`
(`prop:wigner-2-coefficient`, `prop:unified-iterative-correction`,
`rem:sdp-regime-switch-interpretation`,
`rem:markov-trace-axiomatic-closed-form-interpretation`,
`rem:confinement-frobenius-reciprocity-interpretation`). What they lose is the
*reading* of their constants as LP duals. `prop:wigner-2-coefficient`'s closed
form stands on its own derivation.

**Untouched** — the six-term mass formula and its actual derivation chain, every
numerical coefficient, and the chirality/writhe/ribbon route.

**An undeclared-dependency defect, separately.** `mass-coefficient-shadow-price.ts`
names `operator-selection-lp` only in a **comment**
(`operator-selection-lp → shadow prices → mass coefficients`) and not in
`uses[]`, so the manifest never recorded the dependency its prose asserts. That
is why the block did not surface in a `uses[]`-based sweep, and it is a defect
independent of everything else here.

## And the promised measurement is moot

I said the open item was whether the **nuclear** LP instance is also
relative-interior. It does not arise: the mass coefficients are not read off any
LP solution, so there is no nuclear-instance optimum whose geometry could matter
to them. The question was well-posed only under the assumption this correction
removes.
