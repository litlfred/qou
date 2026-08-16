---
# qou-0tjt
title: Lean LP model drops the box constraints, so its dual is an equality not an inequality
status: todo
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
