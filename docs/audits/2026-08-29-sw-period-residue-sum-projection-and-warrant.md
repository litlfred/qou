# `sw_period_eq_residue_sum` assumes its conclusion, and its warrant is the residue theorem read backwards

**Date:** 2026-08-29 · **Bean:** `qou-6v5l` · found working `qou-u8oy` input (2)
**Subject:** [`prop:sw-period-residue-sum`](../../content/quantum-observable-universe/brings-surface/sw-period-residue-sum.md)
**Not a discovery:** the vanishing conclusion is already held by
[`prop:sw-classical-jet-exactness`](../../content/quantum-observable-universe/brings-surface/sw-classical-jet-exactness.md).
Read §"What was already known" first.

## Why this was looked at

`qou-u8oy` leaves input (2), the non-abelian-Stokes keystone
`a_D^(n) = lw(n−1)`, as the one open input under
`conj:binding-manybody-eq-jet-filtration`. The keystone's residue-sum form is
`prop:sw-period-residue-sum`, so that block is the natural place to start.

## Two defects

### 1. The theorem is a conclusion-typed projection

```lean
structure SWPeriodResidue (k : ℕ) where
  ...
  period_eq : period = twoPiI * ∑ p, residues p

theorem sw_period_eq_residue_sum {k : ℕ} (S : SWPeriodResidue k) :
    S.period = S.twoPiI * ∑ p, S.residues p :=
  S.period_eq
```

The statement is literally the type of the `period_eq` field and the proof is
that field. This is the self-assuming projection AGENTS.md §3b-cond item 5
names: *"a class that carries the block's own conclusion as a field, with a
'theorem' that merely projects it."*

It is **not** newly noticed by a machine — it is entry
`content/quantum-observable-universe/brings-surface/sw-period-residue-sum.lean`
in [`lean-triviality.json`](lean-triviality.json), `"closed": false`, checked
`2026-08-07`. What was missing is the agent verdict the ledger discipline
requires; the machine can flag, only an agent can clear. It does not appear in
[`lean-vacuity-review-ledger.json`](lean-vacuity-review-ledger.json) at all.

### 2. The warrant is the residue theorem, backwards

Both the `.md` and the proof block justified the residue-sum identity as *"the
residue theorem on the compact Riemann surface `S_c`"*, summing over **all**
`p ∈ S_c`. Two independent problems:

- **The residue theorem says the opposite.** On a compact Riemann surface the
  residues of a meromorphic 1-form **sum to zero**. It does not say a period
  equals the total residue sum. Summing over every pole therefore forces
  `a_D^(n) = 0` at every jet level — the reverse of what the block wants.
- **`P¹(ℂ)` has no generating cycle.** The proof block asks for *"the period
  over the generating cycle of `S_c`"*, but `H₁(P¹) = 0`. Only a *bounding*
  cycle has a residue-sum value at all, and then the sum ranges over the
  **enclosed** poles — a proper subset, whose identity is precisely the content
  not supplied.

Worth separating from a nearby fact: the **colour cubic** curve
`X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1) = 0` is a *smooth plane cubic* — no
projective singular points — hence **genus 1**, with a genuine two-dimensional
`H₁`. So real periods do exist in this problem; they just do not live on the
genus-zero `S_c` where the block places them, and on a genus-1 curve a period
over a homology generator is not a residue sum in the first place.

## What was already known — and this is the part that matters

[`prop:sw-classical-jet-exactness`](../../content/quantum-observable-universe/brings-surface/sw-classical-jet-exactness.md)
(`QOU.Brings.classical_jet_period_zero`) **already reaches `period = 0`**, by a
better argument: under the classical-jet rule
`λ_SW^(n) = X^(n)(z)dz = d(X^(n−1))` is exact, so every residue vanishes
individually, and it is properly recorded as a **scope-(b)** exclusion of the
classical-jet reading with the q-difference prolongation left untouched.

The corpus-grep found this before anything here was written up as new, which is
what the checklist is for. The lemma added by this bean is therefore a **second
route, not a finding**:

| route | assumes | driven by | scope |
|---|---|---|---|
| `classical_jet_period_zero` (already on main) | each residue vanishes (exactness) | the **jet rule** | classical-jet reading |
| `period_eq_zero_of_total_residue_vanishes` (added here) | only the **total** vanishes | the **ambient surface** | any reading summing over all poles |

The second assumes strictly less, so it survives readings in which individual
residues are nonzero. They agree by different mechanisms.

## A counting bound on the "one residue per Wedderburn block" reading

The block characterises the residues as *"a per-block quantum-dimensional weight
on the Wedderburn decomposition restricted to that level"*, with *"the residue
family at level `n` indexed by the weight data of rank `n`"*.

Measured this session: the pole locus is the branch locus of the colour cubic,
and that is **exactly 6 points, independent of `n`** —

```
disc_X = −16z⁶ − 24z⁵ − 35z⁴ − 50z³ − 35z² − 24z − 16      (squarefree: gcd(D, D′) = 1)
```

three conjugate pairs at `|z| ≈ 0.943, 1.000, 1.061`, reproducing the three
pairs `lever1_sw_period_lw_rate_refine.py` reports.

A one-to-one indexing of the level-`n` residue family by the blocks `λ ⊢ n`
therefore requires `p(n) ≤ 6`, which **fails from `n = 5`** (`p(5) = 7`,
`p(6) = 11`, `p(n) → ∞`). The cardinality bound is a genuine invariant, so this
is a scope-(b) exclusion **of that indexing reading** — it says nothing against
the equality `a_D^(n) = lw(n−1)` itself, since 6 numbers can of course sum to
what 11 numbers sum to. What it excludes is the bijection, which is how the
block's prose reads.

Note also the block's *"the vertical (jet) degree `n` governs the number of
contributing poles"*: the pole **locus** cannot grow, being `n`-independent. What
grows with `n` is the pole **order** — `X^(n) ~ (z−z_k)^{1/2−n}` — so that
sentence is true only if "number of poles" is read as "order", which is not what
"indexed by the weight data of rank `n`" then licenses.

## What changed

- **Lean.** `period_eq_zero_of_total_residue_vanishes` and its contrapositive
  `total_residue_ne_zero_of_period_ne_zero` added — derived, sorry-free, axioms
  `[propext, Classical.choice, Quot.sound]`. Verified non-vacuous: `S.period = 0`
  is **not** provable without the hypothesis (it requires `sorry`).
  `sw_period_eq_residue_sum` is **kept**, because downstream prose cites the
  proposition by that name, but its docstring now states plainly that it is a
  projection.
- **Narrative.** Both `.md` files now range the sum over an **enclosed subset
  `E`** and say that identifying `E` is the open geometric content. The false
  warrant is replaced by the correction, not deleted.

Nothing about the keystone is weakened or strengthened by this: it remains a
§3b conjecture class with no instance. What changes is that the residue-sum
route to it no longer claims a proof it does not have.

## Reproduce

```bash
python3 -c "
import sympy as sp
X,z=sp.symbols('X z')
P=X**3+(z+1)*X**2+(z**2+z+1)*X+(z**3+z**2+z+1)
D=sp.expand(sp.discriminant(sp.Poly(P,X)))
print(sp.factor(D)); print('squarefree:', sp.gcd(D,sp.diff(D,z))==1)
print([abs(sp.N(r,12)) for r in sp.nroots(sp.Poly(D,z),n=30)])"
```
