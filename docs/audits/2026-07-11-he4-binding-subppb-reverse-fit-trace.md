# Why the binding energies are no longer "sub-ppb": a reverse-fit trace + the derived-weight refutations

**Date:** 2026-07-11 · **Axis:** A≥3 binding closure (Δ_λ / strong sector) ·
**Tier:** audit (no new compute wired) · **Discipline:** no fit, no c_k / Δ_λ
value, no wiring, no tier change.

This doc answers the owner's question: *"in the discussion we get much better
[binding]. why not any more? the LaTeX was computing sub-ppb values."* It traces
what produced those sub-ppb numbers, why the framework's own discipline removed
them, and records the two derived-weight families tested since (heat-kernel,
q-hyperbolic) — both refuted zero-fit.

## 1. The sub-ppb binding was a reverse-fit, not a derivation

The uploaded discussion's sub-ppb binding energies came from commit
`e987c1f5a1` *("feat(mass-theory): integrate unified binding architecture and
strong sector closures")*. That session **reverse-evaluated** the per-block
binding weights `w_λ` so that the unified binding sum

```
B(K) = E · Σ_λ w_λ · |Δθ_λ|,   Δθ_λ = arccos(χ^λ/d_λ)_atom − arccos(χ^λ/d_λ)_free
```

reproduced `B_AME` to machine precision **by construction** — the weights were
solved from the answer. That is the forbidden "7th Δ_λ ansatz" pattern (the six
prior closure ansätze — Frobenius co-Casimir, Demazure-fibre, LP-Plancherel,
LP-Frobenius, crystal-graph, augmented Markov — had all failed on the deuteron;
see [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md)).
A sum that is *solved to hit* the target is not a prediction; its "sub-ppb"
accuracy is a tautology, exactly the m_p fitted-Habiro-tower failure mode
recorded in [`docs/audits/2026-07-04-c4-mu-p-tension-pin-dependence.md`](2026-07-04-c4-mu-p-tension-pin-dependence.md).

## 2. The framework discipline de-laundered it

The reverse-fit did not survive review. The de-lamination happened in two moves:

- **PR #3511 / commit `242bd2515e`** re-scoped the L4 `A>40` atlas band from
  status `canonical-recursive` to **`asymptotic-approximation`** — an honest
  scope-(a) label ("this construction, alone, approximates; it does not derive").
- The per-isotope status labels on the canonical-isotope witnesses became
  **`canonical-with-empirical-assignment`** / **`borromean-tower-via-fitted-lambda`**
  (see `computations/canonical_isotope_witness.py`, `atlas_render_per_z.py`) —
  each label naming the empirical input rather than presenting it as derived.

Net effect: the sub-ppb numbers were correctly demoted to fitted/approximate.
The honest current deuteron figure (canonical, no per-block fit) is ~1% off AME,
**not** sub-ppb. **Nothing regressed** — the accuracy was never derivational; the
discipline simply stopped the corpus from *claiming* it was.

## 3. ⁴He `canonical-recursive` still carries a residual anchor over-claim

`canonical_isotope_witness.py` computes ⁴He at `layer = L3-α-cluster` with
`n_α = 1, pairs = 0`, so `B_pred(⁴He) = B(⁴He)_anchor = AME` — i.e. ⁴He's
binding is the AME value fed in as the α-cluster anchor, not a zero-parameter
prediction. (The zero-parameter magic-A route,
`alpha_cluster_recursion.py::B_4He = 29.9557 MeV`, is 5.9% off AME.) This is the
same class of over-claim PR #3511 fixed for `A>40`, still live for the ⁴He
α-anchor cell. **Recommended follow-up:** re-scope the ⁴He `canonical-recursive`
cell to `asymptotic-approximation` / `anchored-to-AME`, matching #3511. (Queued;
not done in this doc's PR — flagged for owner pick.)

## 4. The honest question that stays open: a *derived* per-block weight

With the fit removed, the real open problem is a **parameter-free** `w_λ` (or
`Δ_λ`) with a categorical pedigree that reproduces the A-growth of binding. The
cleanest single target is the AME ratio

```
S(⁴He)/S(D) = B(⁴He)/B(D) ≈ 28.30/2.224 ≈ 12.72
```

Two derived-weight families were tested against it this session, both zero-fit,
both refuted (scope-(a)):

### 4a. Compact q-heat-kernel weight — refuted (over-grows)

[`binding_heat_kernel_weight_probe.py`] tested the Peter–Weyl / SU_q(2)
heat-kernel eigenvalue `C_λ(q) = Σ_□ [c]_q[c+1]_q` (content Casimir) as `w_λ`.
At `q₀ > 1` the compact q-integer `[c]_q ~ sinh(c·ln q₀)` grows exponentially,
so `C_λ` **over**-grows: `S(⁴He)/S(D) = 34.15` vs target 12.72. Heat-kernel
damping `e^{−C_λ·τ}` at every substrate τ collapses (growth 0.0–0.21). Refuted.

### 4b. Non-compact / q-hyperbolic (Faddeev) weight — refuted, one near-miss

[`binding_qhyperbolic_weight_probe.py`] (this PR) tested slower-growing derived
weights seeking the moderate 12.72 regime:

| weight (parameter-free, fixed by q₀) | S(⁴He)/S(D) | worst \|err\| | verdict |
|---|---|---|---|
| C_λ(q₀) compact baseline | 34.15 | 61.3% | over-grows |
| C_λ(√q₀) half-monodromy (pion scale) | 30.96 | 57.4% | over-grows |
| **√C_λ amplitude** | **11.14** | **14.2%** | **closest — not ≤5%** |
| C_λ/dim_q intensive | 0.00 | 100% | collapses |

The one signal worth recording: **√C_λ** (halving the compact exponent) lands at
growth 11.14, ~12% below 12.72 — far closer than anything else, but not a
zero-fit closure.

**Structural reason (formalize-first, held):** the binding sum runs over
Young-diagram partitions — compact SU_q(2)/S_n objects with **no non-compact rep
labelling**. A genuine Faddeev weight has no partition index, and the modular
dual q̃ of q₀≈1.11 is non-perturbative (`e^{±O(400)}`) — it explodes or
collapses, never the moderate 12.72 regime. So the "q-hyperbolic weight" is a
category error at the level of the *index set*, not merely a magnitude miss.

## 5. Net

The sub-ppb binding was a reverse-fit; the framework correctly demoted it; the
honest accuracy is ~1% (deuteron) with the α-anchor cells still labelled
empirical. The derived-weight search has now excluded both the compact
heat-kernel (over-grows) and the non-compact/Faddeev family (no partition index)
zero-fit. The **Δ_λ / A≥3 binding closure stays OPEN**; the productive directions
remain GAP-A-3 / GAP-A-4 (categorical brane-tower level selection / ρ general
rule) and Option E via the A=4 interface operator — **not** a seventh fit-based
ansatz. No production compute touched; no value wired; no tier changed.

## Cross-references

- Reverse-fit source: commit `e987c1f5a1` (unified binding architecture)
- De-lamination: PR #3511 / commit `242bd2515e` (A>40 → asymptotic-approximation)
- Δ_λ gate + prior six ansätze: [`2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md)
- Fit-tautology precedent (m_p Habiro tower): [`2026-07-04-c4-mu-p-tension-pin-dependence.md`](2026-07-04-c4-mu-p-tension-pin-dependence.md)
- Compact heat-kernel probe: [`computations/binding_heat_kernel_weight_probe.py`](../../computations/binding_heat_kernel_weight_probe.py)
- q-hyperbolic probe (this PR): [`computations/binding_qhyperbolic_weight_probe.py`](../../computations/binding_qhyperbolic_weight_probe.py)
