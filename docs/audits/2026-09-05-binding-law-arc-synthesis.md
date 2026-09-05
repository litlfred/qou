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

1. **No surface, Coulomb, symmetry or pairing term.** Fitted **jointly** over
   the 2548 measured nuclides the three SEMF shapes span, in `B`: `(N−Z)²/A²`
   **361 %**, `A^{−1/3}` **154 %**, `Z²/A^{4/3}` **67 %** — a ranking of
   **3 : 1.8 : 1**, with `R² = 0.927` between them. The symmetry energy leads,
   but not by the margin the *marginal* correlations (−0.804, −0.178, −0.044)
   suggested: those three shapes are collinear across the chart, because heavy
   nuclei have large `Z`, large `N − Z` and large `A` together. **Reading the
   −0.044 as "Coulomb is essentially absent" was wrong and is retracted**
   (2026-09-05, `qbeta_chain_cannot_carry_coulomb_or_surface_probe.py`).
2. **The isospin contribution has the wrong sign.** Derived `κ = +2(q₀−1) =
   +0.2200`; the data optimum is `κ ≈ −0.15`. Layout-free bond counting
   (p5–p95 **1.181**) beats every isospin-resolved variant (1.225–1.232). What
   the law earns is *"the algebra produces an extensive quantity"* — not the
   specific bond energies. (`qou-q7ga`.) **The sign has since been reduced to a
   single inequality** — see the supersession note at the end of this section.
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

**Coulomb and surface are ONE defect, and it is the edge set.** Both follow from
a single structural fact about a path, proved by counting rather than measured:

- A chain has `Z−1` proton–proton edges against `Z(Z−1)/2` proton pairs, so it
  carries `2/Z` of the Coulomb interaction — **2.44 % at `Z = 82`**. Coulomb is
  quadratic in `Z`; a path's edge count is linear. No choice of letters and no
  scale produces a `Z²` term from `Z−1` edges. That is `qou-nial`'s *"the bond
  rule is a centred SUM of charges where Coulomb needs a PRODUCT"* restated as
  combinatorics.
- A path's interior degree is the constant `2`, so its endpoint deficit is
  `A`-independent: there is no `A^{2/3}` in it at any `A`. `qou-3wvl`'s
  α-cluster ratio law — holding to ~2 % for `n ≤ 2` and drifting **+13 %** by
  ¹⁶O — is the same defect seen from the cluster side.

A one-dimensional chain is standing in for a saturating three-dimensional
packing, and two of the three missing SEMF terms are exactly what that
substitution costs.

**Sharpened the same day — "one defect" is right about the chain, but the two
halves are fixed in opposite directions.** Both arguments turn only on the
chain's *degree*, so both generalise; and generalising them separates them.

- **The surface half is SUPPLIED by a degree bound.** A bounded-degree packing's
  boundary deficit gives exactly `B/A = εk/2 − (εc(k−k′)/2)·A^{−1/3}`, the SEMF
  volume-minus-surface shape, with `a_S/a_V = c(k−k′)/k` — ε and k both cancel.
  Proved in `QOU/Mass/CoordinationSurfaceDeficit.lean` (bean `qou-kqdn`,
  2026-09-05). Fix the edge set and the surface term appears.
- **The Coulomb half is FORBIDDEN by a degree bound.** By the degree-sum formula
  a graph with max degree `d` has at most `dn/2` edges, so its share of the
  `n(n−1)/2` pairs is at most `d/(n−1)` — and this holds for the induced proton
  subgraph *whatever the assignment*. At `Z = 82`: **2.47 %** for the chain,
  6.17 % for max-contact deltahedra, **14.8 % even for close packing**. Fixing
  the edge set does not help, because every candidate edge set is degree-bounded.
  `QOU/Hecke/BoundedDegreeCoulomb.lean` (bean `qou-556v`).

So Coulomb is not a missing *term* in the bond graph — it is outside the
bond-graph *form*, which is physically right: Coulomb is `1/r` long-range and a
contact graph is not. The one door left open is a `Z`-dependent per-bond energy,
and it is a wide one to walk through: reproducing the SEMF term needs
`ε(Z) ≥ 2a_C(Z−1)/(dA^{1/3})`, which runs **0.0732 → 1.588 MeV** from ⁴He to
²⁰⁸Pb, a factor of 21.7. The corpus's derived letters are numbers; that is a
function of the nucleus, so it is a different form of law rather than a
re-tuning. At ²⁰⁸Pb the omitted term is **47.7 %** of the total binding.

*(Aside worth knowing before quoting GAP-1: `3A−6` is only degree-5-admissible
up to `A = 12`. A triangulated sphere has average degree `6 − 12/A`, so max
degree exceeds 5 as soon as `A > 12`, and there are exactly eight convex
deltahedra, the largest the icosahedron. It is a small-`A` construction; past
that the honest bound is `d = 12`. This does not touch the theorem, which holds
for any `d` — it only fixes which `d` to quote, and the larger one still loses.)*

🛑 **This supersedes a claim made earlier in this arc.** An edge-set comparison
reported *"the bond GRAPH is not where the error lives"* on the strength of three
edge sets landing within 0.6 % of each other. The all-pairs member of that
comparison had been **renormalised to `A−1` bonds** — which divides out the
quadratic bond growth that is the only difference between a path and a complete
graph, making it a chain with reweighted letters. Raw, the medians are chain
`0.886414` against all-pairs `0.013558`, a factor of **65**. Neither graph is
right, but the graph is where the error lives. The **ordering** half of that
finding stands unchanged: segregated and alternating are both chains, they do
agree to 0.6 %, and layout-free `(A−1)` still beats every isospin-resolved
variant.

**The route the corpus has already closed:** the symmetry energy via an
isospin/SU(4) Casimir is **structurally forbidden** — the trace annihilates every
partition with `ℓ(λ) > 2` (`QOU/Hecke/RowCap.lean`), and SU(4) labels need four
rows; on the surviving two-row shapes `C₂^{GL(4)} − C₂^{GL(2)} = 2n`, a constant.
(`qou-ubsl`, completed.) 

🛑 **But "no obvious algebraic source" — which is what this paragraph used to
conclude — is superseded (same day).** There *is* a source, it is the p-n
interface count, and it is **sign-locked**. A bond sum is additive in
`L = −log b`, so its symmetry term compares `b_pn` against the **geometric** mean
of `b_pp` and `b_nn`; the construction delivers an **arithmetic** one
(`pn-bond-cannot-be-extremal.md`: `b_pn = w·b_pp + (1−w)·b_nn` with
`w = ½ + δ_flavour/4`). AM ≥ GM, so the sign is backwards structurally rather
than numerically. Three exact facts pin it:

```
GM      √(b_pp·b_nn) = 1/[2]_q                    0.497290545605
AM      (b_pp+b_nn)/2 = [2]_q/2 − 1/[2]_q         0.508155…
AM − GM = ([2]_q²−4)/(2[2]_q) = h²/(2[2]_q)       0.010867342144
```

with `h = q − 1/q` the Hecke parameter itself — **the AM–GM gap *is* the
deformation.** The crossing weight is `w = 1/(q²+1)`, which equals `½` only at
`q = 1` and is strictly below it for every `q > 1`: the deformation moves the
threshold down and the construction does not follow. At `q₀` the threshold is
`0.448018` against the corpus's `w = 0.500344` — **11.7 % above it**. And the
endpoints `δ(w=0) = +2 log q₀`, `δ(w=1) = −2 log q₀` are exactly `qou-y2np`'s bar
branch, so that "one bit" is two points of a continuum whose crossing is derived.

So the headline is stronger than "nothing found": a repair must move **one**
quantity — the convex weight `w` below `1/(q²+1)` — and nothing about the graph,
the layout, the scale or a re-derivation of `q` can substitute for it.
`QOU/Hecke/SymmetrySignAmGm.lean` (7 decls) and
`qbeta_symmetry_sign_is_am_gm_locked_probe.py`; bean `qou-i01a`. The *power*
(`(N−Z)²/A` rather than just a sign) still needs a well-mixed assignment, which
is a mean-field model and is labelled as one — the corpus's canonical layout is
segregated, with `E_pn = 1` and no symmetry term at all.

## 6b. "Why only the leading order?" — because the tail is 323× too small

A fair objection to every truncated `q`-series in this arc, raised against the
flavour split `δ = Δm_pn/M_N`, which the corpus carries as

```
δ_leading = (q−1)²(1−q⁻⁴)/3        δ_canonical = δ_leading · (1 + ℏ_q³)
```

`(1 + ℏ_q³)` is the first two terms of `1/(1 − ℏ_q³)`. Mathematical accuracy says
take all of them. The answer has two halves, and **only the second is a defence
of the truncation**:

**It would not help.** The entire tail past two terms is `x²/(1−x)`, which at
`x = ℏ_q³ ≈ 9.727e−4` is **9.4707e−7**. The gap between the two-term form and
the measured `Δm_pn/M_N` is **3.0598e−4** — `K = 323.07` times larger. Summing
every remaining term to infinity closes one three-hundredth of what is missing.
`summing_cannot_close` in `QOU/Hecke/GeometricTailBound.lean` is that statement
in general form, over an ordered field, with the measurement entering only as
the hypothesis `K > 1`.

**And the series is not established as the right object.** `(1 + ℏ_q³)` is
*labelled* a 3-loop substrate-Planck correction, not derived as a geometric
series; reading two terms as the head of one and summing them is precisely the
clean-formula move the anti-fit discipline exists to catch. Nor does resumming
rescue it numerically: solving `δ_leading/(1 − ℏ_q^k) = δ_CODATA` needs
`k = 2.8822`, not `3` (4.09 % off); and `1 + c·ℏ_q^k` needs
`c = 0.012905, 0.130249, 1.314562, 13.26745` at `k = 1,2,3,4` — none of them `1`
or any simple rational. **The missing 0.03 % is not in this tower at any
order.** (`computations/qbeta/qbeta_flavour_split_series_probe.py`.)

So the truncation is not an approximation anyone should feel uneasy about. It is
exact to the precision the tower can reach, and the residue is somewhere else
entirely.

**Credit where it is due:** `computations/probes/flavor_split_geometric_closure_probe.py`
had already established the second half — the two forms differ only at `O(ℏ⁶)`,
neither reaches CODATA, `(1+ℏ_q³)` supplies 76.07 % of the demanded correction,
and the exact coefficient `1.31459` is the `c` at `k = 3` above. What is added
here is the ratio `K = 323` (a bound on what *any* resummation could be worth),
the sweep at `k = 1, 2, 4`, and the Lean statement.

## 7. Formalisation

| file | content |
|---|---|
| `QOU/Hecke/RowCap.lean` | the `ℓ(λ) > 2 ⇒ dim V_λ = 0` row cap, 10 thms |
| `QOU/Hecke/CrossingConvexity.lean` | two-crossing coordinates, the cone, central multipliers, 12 thms |
| `QOU/Hecke/BindingExtensivity.lean` | `exists_pow_gt_linear` (the refutation) and `linear_le_bondSum`/`bondSum_le_linear` (the replacement's extensivity), 6 decls |
| `QOU/Hecke/LayoutConflict.lean` | two disjoint intervals touch at one boundary ⇒ no contiguous layout carries a colour tube, 4 decls |
| `QOU/Hecke/GeometricTailBound.lean` | `(1−x)⁻¹ − (1+x) = x²/(1−x)`, and `summing_cannot_close`: if the gap is `K > 1` tails wide, the *whole* sum still undershoots, 5 decls |
| `QOU/Hecke/BoundedDegreeCoulomb.lean` | the degree-sum formula as a bond-count bound, the `d/(n−1)` pair share, and `exists_gt_bounded_degree_bond_sum`: no constant per-bond energy makes a degree-bounded bond sum quadratic, 4 decls |
| `QOU/Hecke/SymmetrySignAmGm.lean` | the symmetry sign is AM-vs-GM; an equal-weight p–n bond is always wrong-signed; the crossing weight is `1/(q²+1)`, below `½` for every `q > 1`; the gap is `h²/(2[2]_q)`, 7 decls |

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
