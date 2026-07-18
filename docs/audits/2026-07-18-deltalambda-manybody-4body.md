# Δ_λ many-body wall — the [1⁴] value leg: locality + exchange sign (derive-or-constrain)

**Date:** 2026-07-18 · **Branch:** `claude/deltalambda-manybody-4body-2026-07-18`
· **Type:** FORMALIZE-FIRST derive-or-constrain of the ⁴He-local 4-body term.
**No fit, no tuning, no wiring, no AME inversion.**
**Probe:** [`computations/deltalambda/b4_slater_antisymmetrizer_exchange_sign.py`](../../computations/deltalambda/b4_slater_antisymmetrizer_exchange_sign.py)
(witness `b4-slater-antisymmetrizer-exchange-sign.witness.json`, 7/7 assertions).

## 0. The wall

Single-trace `Δ_λ = (−1)^{n(λ)}·dim(λ)` (sign + magnitude both settled at the
~2-body level) undershoots the AME connected binding; the residual
`target/B(dim)` is `{²H 5.9, ³H 4.4, ³He 3.3, ⁴He 9.3}`, **max at doubly-magic
⁴He**, non-monotone, proved not a single `O(1)` constant. The ℓ¹-ceiling prune
shows no sign re-weighting closes it — a **magnitude-adding**, ≥4-body,
**⁴He-local** term is mandatory. The candidate closed form is the connected
[1⁴] cumulant `b₄ = −ln det(I+G)` with a sign-carrying (bar-odd) exchange
matrix `G`.

This step executes the two named-but-unbuilt pieces of the 2026-07-06
construction spec (§5 `su4_slater_antisymmetrizer.py`) and the explicit **NEXT
UNIT** of `b4_slater_dictionary_functional_form.py` ("build `G` from the
framework pair factors at the nucleon-flavor level `Λ^A(4)`, verify its dominant
eigenvalue is negative, read `b₄` from `−ln det` … never fitted"). It does the
*structural* half — locality, sign, ceiling — parameter-free, and reports the
magnitude honestly as still-gated.

## 1. Part 1 — ⁴He-locality is EXACT and parameter-free (DERIVED)

The nucleon-flavor projector `P_{[1^A]} = Λ^A(ℂ⁴)` is the `S_A` antisymmetrizer
over the 4 SU(4) single-particle states (p↑, p↓, n↑, n↓). Its rank is the
antisymmetrizer **trace** on `(ℂ⁴)^{⊗A}`, verified here by **exact enumeration
of `S_A`** (not read off the binomial):

```
rank Λ^A(ℂ⁴) = (1/A!) Σ_{σ∈S_A} sgn(σ)·4^{c(σ)} = falling(4,A)/A! = C(4,A)
```

| A | 0 | 1 | 2 | 3 | **4** | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| rank | 1 | 4 | 6 | 4 | **1** | 0 | 0 | 0 |

Consequences, all exact and **q-independent** (no fit is even possible — pure
combinatorics):

- **A = 5 is the first vanishing** ⇒ `b₄(A>4) = 0`. The 4-body [1⁴] term is
  **⁴He-local by construction**, matching the ⁶Li `super× ≤ 1` return-to-pairwise
  and re-deriving the Lean gate `su4_supermultiplet_dim_vanishes_iff`
  (`C(4,A)=0 ↔ A>4`) as an explicit rank computation.
- **A = 4 is the unique A whose fully-antisymmetric channel is the rank-1
  SINGLET** — all four SU(4) states filled, the Wigner-supermultiplet closed
  shell. So ⁴He is the **unique doubly-magic [1⁴] closure**, and the residual's
  being **maximal exactly at ⁴He** is structurally explained: ⁴He is the one
  nucleus that saturates the [1⁴] singlet.

## 2. Part 2 — the exchange spectrum, sign and ceiling (DERIVED, no fit)

Build the ⁴He [1⁴] complete-graph (6 crossings) exchange matrix `G = mag·S`,
`S` the writhe-sign pattern (pp = +1, nn = −1, pn = ±1; det-class value is
pn-sign-invariant under `diag(1,1,−1,−1)` conjugation, corpus-proved in
`ReebPnMagnitude.lean`). Its spectrum is **exactly**

```
eig(S) = {+√5, −√5, +1, −1}   ⇒   det(I + mag·S) = (1 − 5·mag²)(1 − mag²)   [closed form, checked to 30 dps]
```

Parameter-free readings:

1. **Attractive channel confirmed (sign half of the NEXT UNIT).** A negative
   eigenvalue `−√5·mag` is **always present**, for any magnitude — so the
   dictionary probe's unique all-positive-cumulant branch (`s = −1`,
   `B = −ln det(I+G)`, net-attractive `G`) is **structurally realized** by the
   nucleon-flavor `Λ^A(4)` exchange matrix. `det < 1` for all `0 < mag < 1` ⇒
   `−ln det > 0` (binding). This closes the sign question without any magnitude
   input.
2. **Physicality ceiling = the derived writhe cap.** `det(I+G) > 0` requires
   `mag < 1/√5 = 0.44721` — **exactly** the derived per-pair writhe cap
   `g < 1/√5`. This is now a *closed-form consequence* of the spectrum, not a
   separately-asserted bound.
3. **The naive Markov bond factor is excluded; the reeb magnitude is marginal.**
   `z = 1/[2]_v = 0.49932 > 1/√5` gives `det(I+G) = −0.185 < 0` (unphysical),
   re-deriving the corpus "z anywhere is unphysical at A=4" (reeb audit §3h).
   The derived reeb magnitude `g = 1/√(5 + (q₀−1)²/q₀) = 0.44673` sits just
   below the ceiling (headroom `≈ 1.1e−3`), physical, `−ln det = 6.353`
   (dimensionless).

## 3. Honest classification — DERIVED vs CONSTRAINED-not-closed

| item | verdict |
|---|---|
| ⁴He-locality: `C(4,A)=0` for A>4, A=5 first vanishing | **DERIVED** — exact, q-independent, no fit possible |
| A=4 unique rank-1 [1⁴] singlet (doubly-magic closure) | **DERIVED** — explains residual max at ⁴He |
| attractive sign / `B = −ln det(I+G)` branch | **DERIVED** — negative eigenvalue `−√5·mag` present for any magnitude |
| physicality ceiling = writhe cap `1/√5` | **DERIVED** — closed form `det=(1−5m²)(1−m²)`; z excluded, g marginal |
| the **b₄ MeV magnitude** | **CONSTRAINED-NOT-CLOSED** — needs the per-pair magnitude in `(0, 1/√5)` + the `E₀→MeV` dressing |

**The precise residual open scalar.** The one undetermined quantity is the
per-pair bond **magnitude** (equivalently the `E_unit` scale). Per the reeb
audit §2j, selecting the `A`-flattening normalization that fixes it **is** the
Δ_λ closure — the standing Track-A gate on which six parameter-free ansätze
(Frobenius co-Casimir, Demazure-fibre, LP-Plancherel, LP-Frobenius,
crystal-graph, augmented Markov) have failed and for which a seventh **fit-based**
ansatz is forbidden (AGENTS.md). Reading `b₄` in MeV by inverting the AME point
would be exactly such a fit, so it is **not** done here. The honest terminus:
the [1⁴] `−ln det` form's **locality, sign, and ceiling are derived
parameter-free**; its **magnitude is the Δ_λ gate**, unchanged by this step.

This is the expected honest-negative-adjacent outcome — the `b₄` form
**constrains** (locality exact, sign fixed, magnitude bounded by `1/√5`) but
**does not close** without the one gated magnitude scalar.

## 4. Cross-references

- Construction spec (Step A′, §5): [`docs/design/2026-07-06-gap-a4-b4-branching-projector-construction-spec.md`](../design/2026-07-06-gap-a4-b4-branching-projector-construction-spec.md).
- Sign branch (executed here): [`computations/probes/b4_slater_dictionary_functional_form.py`](../../computations/probes/b4_slater_dictionary_functional_form.py).
- Locality gate (Lean): `QOU/MassTheory/SU4SupermultipletGate.lean` (`C(4,A)=0 ↔ A>4`).
- Ceiling / pn-sign invariance (Lean): `QOU/MassTheory/ReebPnMagnitude.lean`.
- Reeb magnitude + z-exclusion + §2j Δ_λ-gate identification: [`docs/audits/2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md`](2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md).
- θ_λ magnitude derive-or-refute (scalar-𝒜 refuted, geometric-in-A constraint): [`docs/audits/2026-07-13-theta-lambda-magnitude-derive-or-refute.md`](2026-07-13-theta-lambda-magnitude-derive-or-refute.md).

EXPLORATORY — audit + witness only; no production wiring, no fit, no AME inversion.
