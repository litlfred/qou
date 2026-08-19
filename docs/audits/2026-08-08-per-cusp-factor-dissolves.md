# The per-cusp factor `2^{(c−1)/2}` dissolves — and `c_σ = 2^{−3/4}` becomes a zero-parameter prediction

**Date:** 2026-08-08 · **Beans:** `qou-fl4t`, `qou-pn5j`
**Probe:** `computations/probes/one_loop_c_sigma_percusp_dissolution_probe.py`
**Witness:** `computations/one-loop-c-sigma-percusp-dissolution.witness.json`
**Follows:** PR #4691, #4697, #4707, #4708 and
`docs/audits/2026-08-07-one-loop-multicusp-derivation.md`

## Headline

With the corrected, triangulation-invariant 1-loop invariant, the per-cusp
factor is **not there**. The law is

```
c_σ = 2^{−1/2} · |τ_DG|^{−1/2}
```

with the **same constant at `c = 1` and `c = 2`, to 17 digits**. Calibrating it
on `4_1` alone predicts `c_σ(L5a1) = 2^{−3/4}` with nothing adjustable.

The impact analysis guessed this ("fixing the construction likely dissolves that
whole line rather than repairing it"). It does.

## What was claimed

`whitehead_c_sigma_torsion.py` reconciled the Jones-side constant with a
geometrically computed torsion through

```
c_σ = 2^{(c−1)/2} · |τ_old|^{−1/2}
```

called there *"the standard per-cusp Gaussian-integration factor in the
GGMW/Ohtsuki saddle asymptotic"*. PR #4691 showed `|τ_old|` is not a
topological invariant, so the factor was fitted against an ambiguity of its own
size — the three "confirmations" at `c = 1, 2, 3` constrained nothing.

## The test, and why it is not circular

The Jones-side constants come from colored Jones / Kashaev asymptotics with **no
determinant anywhere**:

| | value | source |
|---|---|---|
| `c_σ(4_1)` | `0.75983568565159255077` (17 digits vs `3^{−1/4}`) | `whitehead-c-sigma-fig8-calib.witness.json` |
| `c_σ(L5a1)` | `0.59460355750136053336` (20 digits vs `2^{−3/4}`) | `whitehead-c-sigma-hiprec.witness.json` |
| `c_σ(L6a4)` | `exp(c₀) = 0.25087248112923` (NMAX=56) | `probes/borromean-jones-1loop-torsion.witness.json` |

The first two use the **same `c_σ` definition** — the calibration witness says
so in as many words (*"same c_σ definition … as the Whitehead run"*). So

```
k_c := c_σ · |τ_DG|^{1/2}
```

can be read off at `c = 1` and `c = 2` independently and compared. **A per-cusp
factor requires `k` to move by `√2` between them.**

```
c=1  4_1    k = 0.7071067811865475276
c=2  L5a1   k = 0.7071067811865475244
c=3  L6a4   k = 0.70957453047829191877

|k_1 − k_2| / k_2 = 4.5e−18          (17 digits of agreement)
measured k_2 / k_1 = 0.999999999999999995     — required by the old law: 1.41421…
```

`k = 2^{−1/2}` at both. **The factor is gone.**

### Stated as a prediction

Calibrate `k` on `4_1` — the one case whose torsion is classically known — and
predict `L5a1` with nothing fitted:

```
predicted  c_σ(L5a1) = 0.5946035575013605360512
measured   c_σ(L5a1) = 0.5946035575013605333606     ~17 digits
```

## Why the old fit looked like it worked

On the **default triangulations** of `4_1`, `L5a1` and `L6a4` — and not in
general —

```
|τ_old| = 2^c · |τ_DG|
```

Substituting into the old law:

```
2^{(c−1)/2} · |τ_old|^{−1/2}  =  2^{(c−1)/2} · 2^{−c/2} · |τ_DG|^{−1/2}
                              =  2^{−1/2} · |τ_DG|^{−1/2}
```

**identically.** The "per-cusp Gaussian-integration factor" was precisely the
`c`-dependence needed to undo the `2^c` between the wrong determinant and the
right invariant. Not a physical factor — a reparametrization.

And the `2^c` relation is not an identity. Measured across 13 manifolds it holds
on 5 and fails on 8:

```
4_1   c=1  ratio 2.0                MATCH        5_2   c=1  1.737673923665419   no
L5a1  c=2  ratio 4.0                MATCH        6_2   c=1  7.596658991967814   no
m125  c=2  ratio 4.0                MATCH        7_4   c=1  1.62353574881121    no
L6a1  c=2  ratio 4.0                MATCH        L6a2  c=2  2.0                 no
L6a4  c=3  ratio 8.0                MATCH        s776  c=3  1.0                 no
                                                 L7a1  c=2  2.82842712474619    no
                                                 L8a1  c=2  3.632999868801943   no
                                                 L10n1 c=2  5.681586378017384   no
```

It holds on exactly the three manifolds the factor was fitted to. It fails at
`c = 1` on `5_2`, `6_2` and `7_4`, where there is no per-cusp factor to blame.

## The original template inference was right, and the "correction" was the error

Write the law as `c_σ = (2|τ_DG|)^{−1/2}`. So the bare template
`c_σ = |T|^{−1/2}` that the corpus has used all along refers to
`T := 2·|τ_DG|`. Computing that:

```
T(4_1)  = 1.732050807568877293527   =  √3        rel 0.0
T(L5a1) = 2.828427124746190097603   =  2√2       rel 0.0
T(L6a4) = 16.0                      =  16        rel 0.0
```

`T(4_1) = √3` is exactly the normalization the corpus calls the known
figure-eight adjoint torsion. And **`T(L5a1) = 2√2` is exactly what bean
`qou-k00d` inferred from the template** — the value `whitehead_c_sigma_torsion.py`
declared an error and "corrected" to `2^{5/2}`:

> *"the independent 1-loop computation gives `|τ(L5a1)| = 4√2 = 2^{5/2}` — i.e.
> a FACTOR OF 2 LARGER than the `|τ| = 2√2` that the bare knot template would
> infer … The resolution is a per-cusp normalization"*

There was nothing to resolve. The factor of 2 came from the wrong determinant,
and the per-cusp factor was invented to absorb it. **The original inference
stands, and is now independently derived** rather than read off the template:
`2·|τ_DG(L5a1)| = 2√2`, from a triangulation-invariant computation with the
normalization fixed on `4_1`.

That is bean `qou-pn5j`'s stated gap — *"derive `|τ(L5a1)| = 2√2` from
octahedron NZ data"* — closed in the direction the bean originally asked for.

## This also closes a caveat the derivation left open

The multi-cusp derivation could not pin the **overall constant** at `c ≥ 2`:
triangulation invariance and the change-of-curve law are both blind to a factor
depending only on `c`, and I flagged that as exactly the shape of
`2^{(c−1)/2}`.

The Jones side is not blind to it — it is an outside measurement. Under the
1-loop prefactor form `c_σ ∝ |τ|^{−1/2}`, `k_1 = k_2` says the DG normalization
carries **no extra `c`-dependence** between `c = 1` and `c = 2`, to 17 digits.

## Status, stated precisely

**`c_σ = 2^{−3/4}` is now obtained from a triangulation-invariant torsion plus
a single `c = 1` calibration, with no free parameter.** Both objections that
demoted it are answered: the quantity is well-defined, and nothing is fitted.

What it still rests on, and this is not proved here: the **prefactor form**
`c_σ ∝ |τ|^{−1/2}`. That form is validated on `4_1` to 17 digits by
`whitehead_c_sigma_fig8_calib.py`, whose own witness calls it "template
validated" — validation on one known case, not a derivation. Anyone moving
`qou-pn5j` to DERIVATION should say that the assumption being carried is the
prefactor form.

**`c = 3` is supporting evidence only.** `k_3/k_1 = 1.0035` (0.35%), consistent
— but that tower's own witness flags *"an unresolved normalization+cusp
offset"* against the one-cusped anchor, and its extraction returns `p = 1.4993`
against the exact `3/2`. It is not a third independent pin.

## The cancellation is a theorem, and is now proved as one

`QOU/OneLoopEdgeLattice.percusp_factor_absorbs` — sorry-free,
`[propext, Classical.choice, Quot.sound]`:

```lean
theorem percusp_factor_absorbs {t c : ℝ} (ht : 0 < t) :
    (2 : ℝ) ^ ((c - 1) / 2) * ((2 : ℝ) ^ c * t) ^ (-(1 : ℝ) / 2)
      = (2 : ℝ) ^ (-(1 : ℝ) / 2) * t ^ (-(1 : ℝ) / 2)
```

Everything else in this document is measurement; this one is not. It says the
two laws are the **same function** on any data satisfying `|τ_old| = 2^c|τ|`,
for every real `c` — so agreement at `c = 1, 2, 3` on such data confirms
nothing, and the "per-cusp Gaussian-integration factor" reading was never
distinguishable from its absence there. The content of §"The test" is that
`k_1 = k_2` holds against the *corrected* invariant, where that identity does
not apply.

## Reproduce

```sh
python3 computations/probes/one_loop_c_sigma_percusp_dissolution_probe.py
scripts/verify-lean-direct.sh \
  content/quantum-observable-universe/lean/QOU/OneLoopEdgeLattice.lean
```

---

## Addendum, 2026-08-08 — an independent PUBLISHED check at `c = 1`

**Probe:** `computations/probes/one_loop_ohtsuki_5_2_crosscheck_probe.py`
**Witness:** `computations/one-loop-ohtsuki-5-2-crosscheck.witness.json`

The weakest point of the law above was that `k = 2^{−1/2}` is calibrated at
`c = 1` on the **figure-eight alone**, in a quadratic trace field, from this
corpus's own extraction. That is now fixed.

Ohtsuki's asymptotic expansion of the Kashaev invariant of `5_2`
(`library/ki52/ki52.pdf`, Theorem 1.1) is a **rigorous theorem**, not a fit:

```
<5_2>_N = e^{N ζ} N^{3/2} ω (1 + Σ κ_i (2πi/N)^i + O(N^{-d-1}))
ω = e^{−iπ/4} ((1 − y₀)/(2y₀ + 1))^{1/2},   y₀ the root of (y−1)³ = y, Im > 0
```

(That `ω` reproduces the paper's printed `0.0901905774… − i·0.6499757866…` to
all 10 digits, so the formula is recovered, not guessed.) Then:

```
predicted from the law, k from 4_1 alone   c_σ(5_2) = 0.65620337051419987
Ohtsuki's |ω|                                       = 0.65620337047140662
                                    agreement: 10 digits — all the paper prints
```

**Nothing was fitted**: `k` comes from `4_1`, `|τ_DG(5_2)|` from the geometry,
`ω` from the paper. `5_2` is also two-bridge, so Garoufalidis–Yoon prove 1-loop
= adjoint torsion for it — both sides are theorem-backed.

### A closed form falls out

Since `|ω|² = 1/(2|τ_DG|)`:

```
|τ_DG(5_2)| = |2y₀ + 1| / (2 |y₀ − 1|)         exact to working precision
```

`y₀` has minimal polynomial `y³ − 3y² + 2y − 1`, of discriminant **−23** — the
same as `x³ − x − 1`. That is the `5_2` trace-field discriminant found
independently in PR #4658, and the field of the ambiguity generator `√ρ` from
PR #4697. A **cubic** field, so the match is not a quadratic coincidence.

### Scope — what this does not do

It strengthens the `c = 1` leg only. `5_2` is one-cusped, so it says nothing new
about `c`-dependence: the only `c = 2` test remains the Whitehead link, and
`c = 3` remains supporting-only. And it confirms the constant on an independent
point; it does not prove the law.
