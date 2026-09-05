# The binding-law arc: what was refuted, what replaced it, and what is left

**Date:** 2026-09-05 · **Branch:** `claude/q407-self-assuming-projections-2026-08-21`
**PRs:** #6611, #6615, #6668, #6672, #6682, #6709, #6727 (+ this one)
**Beans:** `qou-gm4q`, `qou-n9qf`, `qou-q7ga`, `qou-ib3g` (closed), `qou-0c19`,
`qou-xf14`, `qou-qkbp`, `qou-2pnv`
**Status:** the arc is finished. What remains is a different and larger problem,
scoped in §6.

Supersedes `docs/audits/2026-09-04-binding-law-options-decision-frame.md`, which
predates §§2–5 below. That note's §7 corrections stand; its avenue table does not.

---

## 1. The refutation

The corpus stated `B = Q_β·Δtr`. It is refuted, and the reason is algebraic
rather than empirical: **`tr_M` is multiplicative along the chain and binding
energy is extensive.** A constant times a product is still a product.

Over the 2548 AME2020 nuclides with *measured* binding energies, at the law's own
**optimal** scale, the residual p5–p95 spread is **1592×**; ²³⁸U is over-bound
19.6-fold. Sharper still:

```
Δtr / tr_free  =  1 − exp(−S)      exactly, with S the additive bond sum
```

which is within `7.7e−4` of 1 by **A = 11**. Above that, **`Δtr` does not
mis-scale the binding energy — it does not contain it.** What is left is the free
factor `t_p^Z t_n^N`. That is why no scale works.

## 2. The closed form it rests on

Derived with **zero fitted constants**, agreeing with the direct Markov trace to
`1e-35`:

```
t_p  = (q²²+q²⁰+2q¹⁸+2q¹⁶+3q¹⁴+2q¹²+q¹⁰−q⁸−q⁴−q²−1)/(4q⁹(q²+1)²)
t_n  = (q¹⁸−q¹⁶+2q¹⁴−2q¹²+4q¹⁰−3q⁸+3q⁶−2q⁴+q²−1)/(4q⁹)
b_pp = q³/(q²+1) = z      b_pn = (…)/(12q⁵(q²+1))      b_nn = 1/(q³+q)
```

Three identities collapse exactly: `b_pp − z = 0`, `b_pp/b_nn − q⁴ = 0`,
`r_prev − t_p·z = 0`. **Nothing in this note touches the algebra.**

## 3. The replacement, and why it is forced

`log` is the unique map carrying multiplicative to additive, so the functional is
not chosen:

```
B = E₀ · log( tr_M(β_free) / tr_M(β_atom) )
  = E₀ · [ (Z−1)(−ln b_pp) + (−ln b_pn) + (N−1)(−ln b_nn) ]
```

p5–p95 **1.225×** against 1592× — a ~1300-fold gain from changing the
**functional**, not the constant; both laws consume the same derived bond
factors. It was already in the repo, unscanned (`binding_log_free_energy.py`,
bean `lkpl`).

**And it is the framework's own object.** The Markov relation
`tr_{n+1}(x·σ_n) = z·tr_n(x)` makes `ν(x) = log_z tr_M(x)` the tower's additive
counter; `b_pp = z` is a derived identity, so **a p-p bond is exactly one Markov
reduction**. Independently, `rem:energy-scale-planck` reads `E₀` as *the energy
of one Hecke reduction step*. So

> **B = E₀ × (number of reduction steps)**

is the framework's reading of its own law. Neither side showed this alone.

**Order 0 is `q → 1`.** All five factors equal exactly `z = 1/2` there (verified
symbolically), the Hecke algebra degenerates to `ℂ[S_n]`, and `ν` becomes an
integer bond count. Expanding in `e = q−1`, the p-n interface has **no
first-order term** and the like-species bonds split symmetrically (`+1, 0, −1`):

```
B = E₀·[ ln2·(A−1) + 2(q₀−1)·(N−Z) ] + O(e²)
```

## 4. The scale — derived, pinned, and ruled

Three separate freedoms were closed.

**The loop value is pinned by an identity.** `b_pp` is `σ` and `b_nn` is `σ⁻¹`,
and their product collapses:

```
b_pp · b_nn = q²/(q²+1)² = 1/[2]_q²   ⟹   √(b_pp·b_nn) = 1/[2]_q   exactly
b_pp = q²/[2]_q      b_nn = q⁻²/[2]_q      (L_pp + L_nn)/2 = ln[2]_q
```

This holds **identically in `q`**, and of the five-member normaliser family only
`[2]_q` satisfies it — the others agree only at `q = 1`. A fit would land at `q₀`
and nowhere else. `qou-59j5`'s 1.33× family span, *the same size as the deficit
it would explain*, collapses to one member. (`qou-xf14`.)

**`E₀` is derived, not calibrated.** `qou-59j5` closed with "E₀ is CAL-1, a
calibration, not a derivation" — a **mislabel**. `rem:energy-scale-planck` gives

```
c_q = 1/(q−1)      ℏ_q = (q−1)/q      E₀ = m_e·c_q²·ℏ_q = m_e/(q(q−1))
```

so `q(q−1)` is `c_q⁻²·ℏ_q⁻¹`, a product of constants that exist anyway. The
algebra is dimensionless, so **one** dimensionful anchor is unavoidable — a
necessity, not a defect — and the binding chain uses only CAL-1 (`m_e`) and
CAL-2 (`m_μ/m_e`, dimensionless). It never touches CAL-3. (`qou-qkbp`.)

**Owner ruling 2026-09-05: brane-tower axioms preferred**, so
`E₀ = E₀^(N=0)/(1−ℏ_q²) = 4.227483` MeV.

## 5. The ruling makes the law one-sided

| | violations of `B ≤ 3·E₀·S` |
|---|---:|
| `E₀^(N=0) = 4.185981` | **10** of 2548 |
| `E₀^full = 4.227483` (ruled) | **1** of 2548 |

Under the ruling the law is an **upper bound on nuclear binding energy for 2547
of 2548 measured nuclides**, saturated at the iron peak to 0.6 % (Fe-54 0.9941,
Ni-56 0.9938, Ni-58 0.9930, Co-55 0.9918).

**The sign is right for structural reasons.** Every SEMF correction *subtracts*
from the volume term, so a law omitting all of them belongs above the data, with
the missing physics bringing it down. `E₀^(N=0)` sits below the peak and lets ten
nuclides climb over it — the wrong position for this shape.

**The sole exception is ⁴He** at 1.0758 — the corpus's own most-worked anomaly,
with 19 open beans on the magic surplus (`qou-ooqh`, `qou-foh0`, `w5tg`,
`qou-3wvl`, `qou-guyb`). A law whose one exception is the nuclide everybody
already flags is better placed than one failing in ten unexplained places.

This is a **structural** argument, not a proximity one: boundedness is a property
of the whole table and cannot be tuned by moving a scale 0.99 % toward one point.

## 6. What is left — and it is shape, not scale

| | size |
|---|---:|
| total scale freedom, after the ruling | **0.99 %** |
| residual band, p5–p95 | **22.5 %** |

**The shape residual is 22.7× the entire remaining scale freedom.** Five rounds
went into the scale, and it was never the dominant term. The named gaps:

1. **No surface, Coulomb, symmetry or pairing term.** Residual correlations:
   `(N−Z)²/A²` **−0.804**, `A^{−1/3}` −0.178, `Z²/A^{4/3}` −0.044. The symmetry
   energy dominates.
2. **The isospin contribution has the wrong sign.** Derived `κ = +2(q₀−1) =
   +0.2200`; the data optimum is `κ ≈ −0.15`. Layout-free bond counting
   (p5–p95 **1.181**) beats every isospin-resolved variant (1.225–1.232). What
   the law earns is *"the algebra produces an extensive quantity"* — not the
   specific bond energies. (`qou-q7ga`.)
3. **Unbound systems are outside it by construction** — strictly positive bond
   energies cannot produce `B ≈ 0` (⁵Be, the hydrogen drip line).
4. **The factor of 3 has no realisable mechanism.** It is the strand count, and
   the colour tube that would supply it needs three colour-matched
   single-generator couplings per interface. `tr_M` cooperates exactly
   (factorisation over disjoint non-adjacent blocks, rel. diff 0.0 at 40 dps),
   but **no strand ordering carries it**: exhaustively zero at `A = 2, 3`, and
   for general `A` two disjoint intervals touch at one boundary
   (`QOU/Hecke/LayoutConflict.lean`). Under contiguity the maximum is `A−1`
   couplings against `3(A−1)` needed — exactly one third, the same 3.
   (`qou-0c19`, `qou-ib3g`.)

**Two of these already have diagnosed root causes in the corpus**, which is where
a successor should start rather than from scratch: `qou-nial` — *"the bond rule
is a centred SUM of charges where Coulomb needs a PRODUCT"*, which explains the
−0.044 Coulomb correlation directly; and `qou-3wvl` — the α-cluster ratio law
holding to ~2 % for `n ≤ 2` and drifting +13 % by ¹⁶O, *which is the surface
correction*.

**The route the corpus has already closed:** the symmetry energy via an
isospin/SU(4) Casimir is **structurally forbidden** — the trace annihilates every
partition with `ℓ(λ) > 2` (`QOU/Hecke/RowCap.lean`), and SU(4) labels need four
rows; on the surviving two-row shapes `C₂^{GL(4)} − C₂^{GL(2)} = 2n`, a constant.
(`qou-ubsl`, completed.) So the dominant missing term has no obvious algebraic
source, and that is the honest headline of what remains.

## 7. Formalisation

| file | content |
|---|---|
| `QOU/Hecke/RowCap.lean` | the `ℓ(λ) > 2 ⇒ dim V_λ = 0` row cap, 10 thms |
| `QOU/Hecke/CrossingConvexity.lean` | two-crossing coordinates, the cone, central multipliers, 12 thms |
| `QOU/Hecke/BindingExtensivity.lean` | `exists_pow_gt_linear` (the refutation) and `linear_le_bondSum`/`bondSum_le_linear` (the replacement's extensivity), 6 decls |
| `QOU/Hecke/LayoutConflict.lean` | two disjoint intervals touch at one boundary ⇒ no contiguous layout carries a colour tube, 4 decls |

All sorry-free on `[propext, Classical.choice, Quot.sound]`, `lean`-direct exit 0.
Everything in `BindingExtensivity` and `LayoutConflict` is proved for arbitrary
bases and bond energies, so no substrate constant enters; `t_p > 1` and bond
positivity are stated there as **measurement, not proved**.

## 8. Reproducing

```sh
python3 computations/qbeta/qbeta_binding_law_options_probe.py          # 10/10
python3 computations/qbeta/qbeta_tower_log_z_and_roast_probe.py        #  9/9
python3 computations/qbeta/qbeta_strand_multiplicity_probe.py          #  7/7
python3 computations/qbeta/qbeta_disjoint_support_factorisation_probe.py #  7/7
python3 computations/qbeta/qbeta_layout_conflict_probe.py              #  5/5
python3 computations/qbeta/qbeta_loop_value_pinned_probe.py            #  8/8
python3 computations/qbeta/qbeta_e0_is_derived_probe.py                #  6/6
python3 computations/qbeta/qbeta_tower_ruling_bound_probe.py           #  6/6
python3 computations/qbeta/qbeta_no_regime_of_validity_probe.py        #  5/5
python3 scripts/probe-float64-guard.py --diff <files>                  # clean
```

**No CI run exists** for any of this — every workflow in this repo is
`workflow_dispatch`-only by the 2026-06-30 owner directive, so nothing fires on
push or PR. The above are the local equivalents the workflow headers name.
