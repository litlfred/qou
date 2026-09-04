# The link-invariant normalisation of the convention-D Ocneanu trace is forced — `μ = [2]_q`, `ν = q⁻²` — and it makes every single-crossing bond weigh `q/(q²+1)`: the additive law becomes pure bond counting, and the wrong-signed asymmetry was the writhe

**Date:** 2026-09-04 · **Beans:** `qou-hfjc` (this), `qou-q7ga` (the roast this answers one row of),
`qou-59j5` (the scale factor, untouched but re-measured), `qou-2pnv` · **Arc:** binding law /
carrier · **Scope:** formalize-first (Lean, sorry-free) + a probe with **no fitted constant**;
answers avenue 4 of #6611's decision frame (*"make the object a braid"*) by derivation.
**Nothing is wired. The scale `E₀` is not touched.**

## 1. The question, as #6611 left it

#6611's decision frame §3 asks whether a *knot-dependent* normalisation of `tr_M` could be
derived rather than fitted, names the HOMFLY form `X = μ^{n−1} ν^{e} tr` as "precisely a
per-closure factor that the Markov moves force on you", and then sets it aside on three
grounds: (a) the atom word is not a braid (`2A+1` averaged letters, no single writhe `e`);
(b) granting one, no *substrate constant* for `μ` has the right slope; (c) the scale that
would work is the algebra's own output inverted. Its §7.4 leaves avenue 4 "unchanged".

Two things were not done there, and they change the answer:

1. **`μ` and `ν` were scanned, not derived.** The two Markov moves are two equations in two
   unknowns. They have a unique solution; nothing is chosen from the substrate.
2. **The strand factor `μ^{n−1}` is irrelevant under the log law** — the free and the atom word
   both have `n = 3A` strands, so it cancels in `ln(tr_free/tr_atom)`. Only `ν^e` survives, and
   `ν` is the parameter §3 never solved for.

## 2. Lean — the forcing and its consequence

`content/quantum-observable-universe/lean/QOU/MathlibExt/ForcedLinkNormalisation.lean`
(namespace `QOU.MathlibExt.ForcedLinkNormalisation`); `lean`-direct exit 0, zero `sorry`,
`#print axioms` on all 11 declarations `= {propext, Classical.choice, Quot.sound}`.

| declaration | statement |
|---|---|
| `nu_sq_forced` | `μνz = 1 ∧ μν⁻¹z' = 1 ⟹ ν² = z'/z` — the writhe normalisation is forced |
| `mu_forced` | `μ = 1/(νz)` — so is the strand normalisation |
| **`normalised_weights_equal`** | **`νz = ν⁻¹z'`: a positive and a negative crossing have the same normalised weight** |
| **`normalised_mixture`** | any branch mixture `cp σ + cm σ⁻¹` has normalised weight `(cp+cm)·νz` — every production letter (`cp+cm = 1`) weighs the same |
| `branch_weights_sum` | the `(c, d)` form `cσ + d·1` is the branch form `(c+d/h)σ − (d/h)σ⁻¹`, weights summing to `c` |
| `convD_zinv` | `z' = z − h = 1/(q³+q)` at convention D |
| `convD_nu`, `convD_mu` | the forced solution at D: `ν = q⁻²`, `μ = (q²+1)/q = [2]_q` |
| **`convD_weight`** | **the common crossing weight at D is `q/(q²+1)`, for both signs** |
| `convD_bondEnergy` | `−ln(q/(q²+1)) = ln[2]_q` |
| `bondCounting_of_uniform` | uniform bond weights ⟹ `B = (A−1)·E₀·(−ln w)` |
| `tr_mul_branchMixture` | on the `MarkovTrace` structure: `tr(x·(cp•g + cm•ginv)) = (cp z + cm z')·tr x` |

**Objection (a) is answered by linearity.** The normalised functional is applied per
`σ^{±1}` branch; on a branch mixture it is `normalised_mixture`. No single writhe is needed
because the two branches of every letter receive the *same* weight once `ν² = z'/z` — which
is exactly the content of `normalised_weights_equal`. **Objection (b) is about `μ`**, which
cancels under the log law. **Objection (c) does not arise**: nothing here is inverted from the
data.

## 3. Consequence for the binding law

Under `B = E₀ · ln(tr_free/tr_atom)` (#6611) and the monotone factorization (#6561), `B` is a
sum over the `A−1` bond letters alone (the nucleon runs cancel). With the forced normalisation:

    b_pp = z              → ν z          = q/(q²+1)
    b_nn = z' = z − h     → ν⁻¹ z'       = q/(q²+1)
    b_pn = cp z + cm z'   → cp νz + cm ν⁻¹z' = (cp + cm)·q/(q²+1) = q/(q²+1)

so **every bond has the same weight**, and

    B_norm = (A − 1) · E₀ · ln[2]_q,   ε = E₀ ln[2]_q = 2.9242463 MeV   (derived, no fit).

The un-normalised bond energies `−ln b_pp = 0.490`, `−ln b_pn = 0.677`, `−ln b_nn = 0.907` —
and with them #6611's derived asymmetry `κ_derived = +0.22`, measured there to have the **wrong
sign** against the data (`κ ≈ −0.15`) and **retracted** — are exactly the writhe factor `ν^e`
that the un-normalised trace leaves in. Under the forced normalisation `κ_derived = 0`
identically.

## 4. Probe

`computations/probes/forced_link_normalisation_bond_counting_probe.py` — **33/33**, mpmath
50 dps, the affine-letter algebra of #6561, the production bond letters read off
`atom_braid_word_3A`, #6611's AME selection and percentile function reproduced verbatim.

| check | result |
|---|---|
| `z' = z − h = 1/(q³+q)`; `ν = q⁻²`, `μ = [2]_q` satisfy both Markov-move equations | exact |
| every production bond letter (pp, pn colour-weighted, nn) in branch form: `cp + cm = 1`, raw trace reproduced, **normalised weight `= q/(q²+1)` to 50 dps** | 9/9 bonds |
| raw `b_pp = z`, `b_nn = z'` (#6611's closed forms) | exact |

| law (scale-free comparators, 2548 measured nuclides) | median AME/pred | p25–p75 | **p5–p95** | full |
|---|---:|---:|---:|---:|
| un-normalised segregated chain (#6611, at `E₀`) | 2.6856 | 1.0953 | **1.22497** | 10.18 |
| **normalised = bond counting, `ε` derived** | 2.8213 | 1.0843 | **1.18085** | 8.17 |

The normalised law's spread is #6611's "bond COUNT only (layout-free)" spread to five figures
— which that PR found *empirically* to beat every isospin-resolved variant and could not
explain. The forced normalisation **predicts** it. Both spread measures tighten; the full range
tightens from 10.2× to 8.2×.

Light nuclei, `B_norm = (A−1)·ε`:

| | `B_norm` | `B_AME` | AME/`B_norm` |
|---|---:|---:|---:|
| ²H | 2.924 | 2.225 | 0.761 |
| ³H | 5.848 | 8.482 | 1.450 |
| ³He | 5.848 | 7.718 | 1.320 |
| ⁴He | 8.773 | 28.296 | 3.225 |

## 5. What this does and does not establish

- **Established (derived, exact):** the normalisation is forced; under it every single-crossing
  bond has one weight; the additive law is pure bond counting with `ε = E₀ ln[2]_q`; the
  `(N−Z)` asymmetry of the un-normalised law is a writhe artifact and vanishes.
- **Consistent with the data's own verdict:** #6611 measured bond counting as the best shape;
  this is why.
- **Not established:** that the *normalised* trace is the right functional rather than the raw
  one. Both are Markov traces; the normalised one is the one that is a link invariant per
  branch. That is an argument for it, not a proof that the physics uses it. Recorded as the
  open decision below.
- **Untouched:** the scale. `median AME/B_norm = 2.82`, i.e. the data want `ε ≈ 8.25 MeV` per
  bond against the derived `2.92`. This is `qou-59j5`'s "2.656 factor" re-measured on the
  normalised law (2.82 here). A target, never a criterion.
- **Untouched:** the remaining shape. With the asymmetry artifact removed, the residual's shape
  against `(N−Z)²/A²`, `A^{−1/3}`, `Z²/A^{4/3}` should be re-measured on the *normalised* law;
  #6611's `−0.804` correlation with the symmetry term was measured on the un-normalised one and
  is presumably partly the artifact. Not done here — one probe, scoped in the bean.

## 6. Decision for the author (default first; recommendation is judgement)

**What is being decided:** whether the framework's binding functional is the *raw* Ocneanu
trace `tr_M` or its *branch-wise link-invariant normalisation* `X = μ^{n−1}ν^e tr_M`. Nothing
in the mass sector is affected (the muon-anchored `F_Bor` carries its own `[3]_q!/q³`
normalisation, which this note does not touch).

- **Default — nothing changes.** `binding_canonical` keeps the raw trace (and the linear law,
  which #6611 already refuted; wiring the log law is `qou-2pnv`'s separate question). The
  wrong-signed asymmetry stays in the stated law as a known artifact with a derived explanation.
  Cost 0, forecloses nothing.
- **Adopt the normalised functional in the *stated* law** (paper + `binding_log_free_energy`),
  not production. What it means: the stated binding law becomes `(A−1)·E₀·ln[2]_q`, one derived
  bond energy, no isospin structure at first order. Cost: one content-block edit and one
  producer edit, hours. Risk: it removes the only isospin-dependent term the law had, so the
  symmetry energy becomes wholly "missing" rather than "wrong-signed" — which is the honest
  state (#6611 §7.4 row 7 already says "named gap, NO route"). Commits to the branch-wise
  reading of a non-braid word.
- **Re-measure the residual shape on the normalised law first** (one probe, `qou-hfjc`
  follow-on) before either of the above. Cost: an hour. Risk: none. This is my recommendation
  (judgement): the decision above is cheaper to make once the normalised residual's correlation
  table exists.

## 7. Verification

- Lean: `lean`-direct exit 0; 11 declarations axiom-clean; zero `sorry`. The imported
  `MonotoneWordTraceFactorizes.olean` was built lean-direct from `main`.
- Probe 33/33; `scripts/precision-gates.sh --changed` (result in the PR body).
- Repo CI is `workflow_dispatch`-only; this agent verification is the gate.
