# The `net → mass` exclusion generalises to every readout — and positivity is what closes it

**Date:** 2026-08-07
**Branch:** `claude/agent-pr-4690-stall-s9f5rt` (stacked on PR #4690)
**Bean:** `qou-lsp9` (second pass)
**Status:** scope-(b) for every *positive* `H₂(q)`-linear readout, on a
proved invariant. Sorry-free Lean, `lean`-direct exit 0.

## Why a second pass

The first pass ([`2026-08-07-lepton-net-to-mass-bridge-exclusion.md`](2026-08-07-lepton-net-to-mass-bridge-exclusion.md),
PR #4690) excluded the multiplicative class `m_n = C gⁿ net(n)^p` on the
proved Binet asymptotics of the Morgan–Voyce continuant. That result is
correct, but it is stated for **one** readout — the unweighted net
`a_n + b_n` — and it invites the obvious reply:

> *So don't use the net. Use the Markov trace.*

That reply is not idle. `tr_M` is the readout the canonical mass route
actually uses (`F_Bor` in the nucleon formula is a `tr_M`), so a referee
would be right to say the first pass excluded the *wrong* object. This
pass answers it.

## The generalisation: there are only two readouts' worth of freedom

`H₂(q)` has dimension `2! = 2`, basis `{1, σ₀}`, and the Gröbner–Shirshov
normal form is `NF(σ₀^w) = a_w · 1 + b_w · σ₀` with `a_w = b_{w-1}`.
So **every** linear functional `φ` on `H₂(q)` — every possible way of
reading a number off the lepton's own braid — is

```
  φ(σ₀^w) = α · b_{w-1} + β · b_w,      α = φ(1),  β = φ(σ₀).
```

`net` is `(1, 1)`. The canonical Markov trace is `(1, z)` with
`z = 1/(q^{1/2} + q^{-1/2})`. Both are single points of one
two-parameter family, and the family is rigid:

| result | statement | Lean |
|---|---|---|
| master identity | `φ(n)(q + q⁻¹) = A qⁿ − (−1)ⁿ B q⁻ⁿ`, `A = α + βq`, `B = α − βq⁻¹` | `linFunctionalK_binet` |
| two-step law | `φ(n+2) = q² φ(n) + (−1)ⁿ (q − q⁻¹) B q⁻ⁿ` | `linFunctionalK_two_step` |
| degenerate direction | `B = 0` ⟹ **exactly** geometric, `φ(n+2) = q² φ(n)` | `linFunctionalK_exactly_geometric` |

Every readout advances by the **same** factor `q²` per generation step.
The choice `(α, β)` survives only inside the single constant `B`, so it
can rescale the vanishing correction but never the `q²`. There is no
third basis element for a third scale to hide in.

Numerically (65 dps, proton pin), the direction that could have behaved
differently is the most rigid of all: `degenerate_B_zero` has both
log-increments equal to `0.208860…` = `2 ln q` to every digit carried.

## The escape I nearly missed, and the invariant that closes it

The two-step law bounds the *increment*, not the *ratio*. If `φ` has a
zero — a **node** — just below the window `n = 2, 4, 6` (windings 3, 5,
7), then `φ(2) ≈ 0` and `φ(4)/φ(2)` is arbitrarily large. Such a readout
**can** produce the observed 206.8. So the blanket claim *"no linear
readout works"* is **false**, and the first draft of this pass asserted
it. It is stated here because the failure mode is instructive: the
rigidity theorem is about increments and does not, by itself, exclude
anything with a near-zero denominator.

Solving the escape exactly (it is a quadratic in `u = A/B`, not a
root-find — an unbracketed `findroot` silently returned nothing and would
have hidden it):

| root | `u = A/B` | implied `β/α` | vs canonical `z` |
|---|---|---|---|
| 1 | 0.280860… | **−0.527611…** | −1.0567 |
| 2 | 0.670619… | **−0.192154…** | −0.3848 |

**Both roots need `β/α < 0`** — `φ(1)` and `φ(σ₀)` of opposite sign.

That is exactly what positivity forbids. For `q > 1` the Hecke parameter
`h = q − q⁻¹` is positive, so the continuant — starting `0, 1` and built
by `b_{n+2} = h b_{n+1} + b_n` — is positive from `b₁` on. Hence any
readout with `α ≥ 0` and `β > 0` is strictly positive at **every** index:
its node does not lie outside the window, it *does not exist*.

The canonical Markov trace is such a readout: `tr_M(1) = 1 > 0` and
`tr_M(σ₀) = z > 0`. The escape is unavailable to the only derived
candidate. Lean (companion file `lepton_continuant_positivity.lean`, split out per
the §7c wall — the algebra file is bare `[Field K]`, this one needs an
order): `hecke_h_pos`, `morganVoyceBK_pos`, `linFunctionalK_pos`,
`markovReadout_pos` — all sorry-free, all over a generic ordered field
(§7c: ordering only, no `Real.sqrt` / `Real.log` / CODATA constant, so no
archimedean specialisation is needed).

## The derived readout, measured

| readout | `(α, β)` | bend `r₁/r₂` | log-increments |
|---|---|---|---|
| observed leptons | — | **12.295** | 5.332, 2.822 |
| net | (1, 1) | 1.00377 | 0.2195, 0.2158 |
| **canonical `tr_M`** | **(1, z)** | **1.03939** | 0.3074, 0.2688 |
| σ₀ only | (0, 1) | 0.96708 | 0.0821, 0.1156 |
| 1 only | (1, 0) | 1.31479 | 0.7148, 0.4411 |
| degenerate `B = 0` | (q⁻¹, 1) | **1.00000** | 0.2087, 0.2087 |

The canonical readout's bend is 1.039 against an observed 12.295. Inside
the class `m = C g^w φ^p`, matching that needs `p = 64.94` — the same
exponential fine-tuning to a vanishing remainder that killed the net,
now measured for the object that actually matters.

## Honest scope

- **Scope-(b)** — for every **positive** `H₂(q)`-linear readout, including
  the canonical Markov trace. Rests on a proved invariant (positivity of
  the continuant for `q > 1`), not on a failed search, per the
  refuted/ruled-out discipline.
- **Scope-(a)** — sign-indefinite readouts are *not* structurally
  excluded. No trace supplies one, and the class `(A/B, g, p)` is three
  free parameters against two observed ratios — underdetermined, so it
  would predict nothing at winding 9 regardless. But it is not proved
  impossible, and it is not called so here.
- **Untouched** — the `T(2,9)` divisibility result
  ([`2026-08-02-generation-count-t29-continuant-divisibility.md`](2026-08-02-generation-count-t29-continuant-divisibility.md))
  and non-`H₂`-linear bridges: an additive interface term, or a route
  where the generation index enters through **linking with the hyperbolic
  Higgs knot `4₁`** rather than through the lepton's own torus braid
  (bean `qou-htk4`). The structural reason the latter is the live
  direction is unchanged: `T(2,n)` are Seifert-fibred with `Vol = 0`,
  while the corpus's working muon mass is `m_e · Vol(4₁)/ℏ_q²`.

## A correction to the bean's premise

`qou-lsp9` states: *"Until wired, the ladder has no predictive content at
n=9 to test against the LEP no-4th-lepton bound. Prerequisite to any
numerical falsification."* The second sentence does not hold, and the
gate should be re-routed rather than left where it is:

- The LEP constraint has two legs. `N_ν = 2.984 ± 0.008` is a
  **count**, and the corpus's generation-count derivation (`b₃ ∣ b₉`,
  `three_generation_windings_are_the_nonharmonic_ones`, sorry-free) is a
  count prediction. Comparing 3 against 2.984 ± 0.008 needs **no mass
  map at all**.
- The no-4th-charged-lepton-below-45 GeV leg likewise needs no mass if
  the count is 3 — there is no fourth state to weigh.
- What the count prediction *is* gated on is the **physical bridge**
  "normal-form-independent winding ⟹ physical generation", the residual
  gap of `qou-x4qm` — not the mass map of `qou-lsp9`.

So the mass map is required for **quantitative lepton-mass predictions**,
which is a real and open goal, but it is not the load-bearing gate on the
generation falsification. `qou-lsp9` is updated accordingly.

## Artifacts

- **Lean (sorry-free, `lean`-direct exit 0 on both):**
  [`lepton_continuant_binet.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/lepton_continuant_binet.lean)
  — `linFunctionalK_binet`, `linFunctionalK_two_step`,
  `linFunctionalK_exactly_geometric`, `netK_eq_linFunctionalK` (pure
  `[Field K]` algebra); and the new
  [`lepton_continuant_positivity.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/lepton_continuant_positivity.lean)
  — `hecke_h_pos`, `morganVoyceBK_nonneg_and_pos`, `morganVoyceBK_pos`,
  `linFunctionalK_pos`, `markovReadout_pos`, `linFunctionalK_ne_zero`
  (ordered field; split per the §7c base-ring wall, which the
  `check-sidecars` preflight flagged).
- **Probe:** [`lepton_linear_readout_rigidity.py`](../../computations/lepton_linear_readout_rigidity.py)
  → `lepton-linear-readout-rigidity.witness.json`. 65 dps, experimental
  (proton) `q₀` per the 2026-08-07 owner directive; no ideal-layer cache
  is read, so no layer straddling. Master identity verified to 4.3e-70
  and the two-step law to 7.2e-71 across six readouts, windings 1–14.
