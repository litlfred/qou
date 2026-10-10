---
# qou-0tjt
title: Lean LP model drops the box constraints, so its dual is an equality not an inequality
status: completed
type: bug
priority: normal
created_at: 2026-08-16T12:35:00Z
updated_at: 2026-08-16T12:35:00Z
---

Found while checking whether the substrate's `x*`/`y₀*` satisfy the hypotheses
added in `k4ul` (#5216). They may not, and the reason is a **model mismatch**
between the narrative and the formalisation.

## The two programs differ

`operator-selection-lp.md` states the primal with a box constraint `xᵢ ≥ -M`
("where `M > 0` is a constant large enough to ensure boundedness"), and derives
the dual constraint as an **inequality**:

```
y₀ + Σᵢ G_{ji} yᵢ  ≤  t_j
```

The Lean `IsFeasible` **drops the box**, keeping only

```
Σᵢ xᵢ = n_target        and        ∀i, (G x)ᵢ ≥ 0
```

— its own docstring says so: *"Boundedness `xᵢ ≥ -M` is absorbed into the
existence of a large `M`; we keep the two binding constraints."*

With the box gone, `x` is a **free** variable, and the dual constraint for a
free primal variable is an **equality**, not `≤`. That is why `k4ul`'s
`dual_feasible` field reads

```
∀ j, t j = y_0_star + Σᵢ sᵢ * G i j
```

and it is the correct hypothesis *for the Lean model*: weak duality needs the
equality here. With `≤` and `x` free the bound fails, because `Σⱼ tⱼxⱼ ≥ …`
requires `xⱼ ≥ 0`, which the Lean model does not assume.

(The index order `G i j` vs the narrative's `G_{ji}` is **not** a discrepancy:
`G` is a Gram matrix, `Gᵢⱼ = tr_M(bᵢbⱼ)`, hence symmetric.)

## Why this matters

Anyone instantiating the class from the narrative's dual certificate will
supply a `≤` witness and **fail to satisfy** `dual_feasible`. The proof in
#5216 is sound; the risk is that the substrate's actual certificate does not
meet its hypotheses, in which case the claimed optimum is unproved for the
program the paper states.

Three ways out, and they are not equivalent:

1. **Restore the box constraint in the Lean model** so the two programs agree,
   and weaken `dual_feasible` to `≤` plus the box multipliers. Most faithful;
   more work, and the box constant `M` has to enter the class.
2. **Keep the free-variable model** and state in the narrative that the
   formalised program drops the box, so its dual is an equality. Cheapest, but
   the paper then describes a different LP from the one verified.
3. **Show the box is non-binding at `x*`** — if `x*ᵢ > -M` strictly for all `i`,
   the two programs have the same optimum and the equality dual is the right
   one. This is probably true by construction and would reconcile them
   properly.

Option 3 is the one worth checking first, and it is a question about the
substrate values rather than about Lean.

## Not yet done

The concrete `x*`/`y₀*` were not located: `operator-selection-lp.md` states the
program generically in `n` and `d = n!` and does not pin numeric values in the
prose. Whether a witness carries them was not established.

- [ ] Locate the concrete `x*`, `y₀*`, `t`, `G` for the substrate instance
- [ ] Check `x*ᵢ > -M` (option 3), or pick between 1 and 2
- [ ] Verify the three `k4ul` hypotheses hold at those values

## 2026-08-16 — RESOLVED, and this bean overstated the problem

Option 3 is what the narrative already asserts. `operator-selection-lp.md`:

> "For large $M$, the slack variables $s_i$ are **driven to zero at
> optimality**. The effective dual simplifies to …"

Those `sᵢ` are the multipliers on the box constraints `xᵢ ≥ -M`. In the dual of
`min tᵀx  s.t.  Σxᵢ = n_target, (Gx)ᵢ ≥ 0, xⱼ ≥ -M`, the box multiplier `μⱼ ≥ 0`
enters as

```
y₀ + Σᵢ Gⱼᵢ yᵢ + μⱼ = tⱼ        hence        y₀ + Σᵢ Gⱼᵢ yᵢ ≤ tⱼ
```

so the narrative's `≤` **is** the equality with the box multiplier carried. The
paper then says those multipliers vanish at the optimum — which is the box being
non-binding, and which makes the `≤` **tight**:

```
tⱼ = y₀ + Σᵢ Gⱼᵢ yᵢ
```

That is exactly `k4ul`'s `dual_feasible`. There is no conflict: the equality is
the *optimality* condition the paper itself asserts, and dropping the box in the
Lean model is the faithful reduction rather than a divergence.

**What this bean got wrong.** It framed the `≤`/`=` difference as "two different
programs", implying the Lean theorem verifies something other than the paper's
claim. It does not — it verifies the paper's claim under the paper's own stated
condition. The three options are moot; option 3 was already in the text and I
did not read far enough before filing.

**What remains true and worth keeping.** "Driven to zero for large `M`" is an
*assertion*, not a derivation — the paper does not exhibit an `M`, prove the
polyhedron bounded, or show the multipliers vanish. `k4ul`'s `dual_feasible` is
the formal counterpart of that assertion, so the Lean layer now states the
assumption explicitly where the prose left it implicit. That is an improvement
in honesty, not a gap.

Still unlocated, and still worth knowing: no computation or witness pins the
concrete `x*`, `y₀*`, `t`, `G`, or `M` — the narrative is generic in `n` and
`d = n!`, and the only LP script in the repo (`computations/_deprecated/
symbolic-lp.py`) is deprecated. So the hypotheses cannot be *checked* against
substrate values, only assumed. That is the real open item, and it is smaller
than this bean originally claimed.

---

## 2026-08-22 — correction: the box IS active at the solver's optimum

Left `completed`; the conclusion stands, the stated reason does not.

This bean closed on "the paper says the multipliers vanish at the optimum,
which is the box being non-binding, and which makes the `≤` tight". Two things
are wrong with that, found while working `qou/8na1`.

**1. "The box is non-binding" is false at the optimum the corpus actually
committed.** This bean ended saying no computation or witness pins the concrete
`x*`, `y₀*`, `t`, `G`, `M`. One does, and did at the time:
`computations/a-K-via-lp-dual-hecke-basis.witness.json` reports, for both
atoms,

    x*₀ = -1000000.0 = -M   exactly.

The box at index 0 is **active** there. The claim is true of the radical
optimum `x* = c·v` this bean reasoned about; the LP has many optima and the
solver returned a different one.

**2. Non-binding and zero-multiplier are not the same condition, and it is the
second one that matters.** Complementary slackness lets a multiplier vanish on
an *active* constraint — that is primal degeneracy, and it is what happens
here. With `y = e₀` and `y₀ = 0`,

    μⱼ = tⱼ - y₀ - Σᵢ Gⱼᵢ yᵢ = tⱼ - Gⱼ₀ = 0    for every j,

because `t` is row 0 of `G` and `G` is symmetric. So the `≤` is tight, the
equality `dual_feasible` of `k4ul` is right, and this bean's conclusion holds —
via zero multipliers on an active constraint, not via an inactive one.

**3. The mechanism is not the paper's.** The narrative says the multipliers are
"driven to zero for large `M`". They are zero for the structural reason
`t = G₀·`, at any `M`. Same answer, different cause, and the paper's stated
cause is not the operative one.

`operator_selection_lp.lean`'s `IsFeasible` docstring cited this bean when
dropping the box. Re-worded 2026-08-22 to justify the drop by two facts
independent of where the optimum sits: dropping a constraint only *enlarges*
the feasible set (so every optimality/lower-bound theorem in the file is
strengthened, not weakened), and `dual_bound_le_objective` supplies the
boundedness the box was introduced for, using nothing but the net constraint,
Frobenius positivity and `s ≥ 0`.

No status change: the disposition was correct and remains so.
