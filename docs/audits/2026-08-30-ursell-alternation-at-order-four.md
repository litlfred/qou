# The Ursell alternation at n = 4 — already answered on main, and the reconciliation

**Date:** 2026-08-30 · **Branch:** `claude/ursell-alternation-a4-2026-08-30`
**Beans:** `qou-1zjd` (**stale — its task was already done**), `qou-6wil` (the work that did it)
**Scope:** (a). Nothing wired; no fit; no new H₁₂ evaluation.

## 0 · BLUF

Asked to extend #6152's `(−1)^{n−1}` alternation to A = 4. **The corpus-grep
found it already done**, and the answer is on `main`:

> `measured μ₄/μ₃ = −1.0206 against target −9.7522; alternation REPRODUCED,
> |ratio| off by 9.56×` — `helium4-mu4-cluster-moment.witness.json`

**The sign alternation continues to 4-body. The magnitude misses by ~9.6×.**

What this pass adds is not a re-derivation but a **reconciliation**, because two
committed results read as contradictory and nobody had squared them:

- #6152: the identity `b₃ = −φᵀ₃` holds 400/400 and **fails at n = 4**
  (`b₄` matches neither `±φᵀ₄`, 200/200 each).
- `helium4-mu4-cluster-moment`: at n = 4 the **alternation is reproduced**.

They are both right, and the reason splits cleanly in two.

## 1 · The corpus-grep result — `qou-1zjd` is stale

`qou-1zjd` (status `todo`) reads: *"the ONLY real mu4 test is A=4 / H12 — 4
particles, C(4,2)=6 bonds, 64 subset traces … compare sign+magnitude against the
derived mu4 = −4.591. Expensive: 64 H12 character evaluations."*

That is precisely
[`helium4_mu4_cluster_moment_probe.py`](../../computations/deltalambda/helium4_mu4_cluster_moment_probe.py),
which landed under **`qou-6wil`** and does exactly it — 6 bonds (3 adjacent + 3
BKL band), 64 subset traces at H₁₂ over 77 partitions, full per-bond and
per-triangle Möbius assembly, guarded by re-deriving each `μ₃` two ways against
the Lean identity `triangle_moment_decomp`. `qou-1zjd` is a duplicate that was
never closed. **Corrected here**; the expensive re-run was not done.

## 2 · Why the two results are compatible

Two independent conditions must hold for a corpus cumulant to equal `±φᵀ_n`:

**(M1) full Möbius inversion**, bonds and triangles summed *individually*.
**(M2) a multiplicative weight** `g(S) = g(∅)·∏_{b∈S} f_b` — what makes
`w(G) = ∏_{E(G)} f` a Mayer weight in the first place.

### (M1) holds — measured

[`ursell_alternation_order_four_probe.py`](../../computations/probes/ursell_alternation_order_four_probe.py),
exact `Fraction`, no tolerance: `φᵀ_n` by direct enumeration of connected
spanning subgraphs of `K_n`, `κ_n` by Möbius inversion over set partitions,
neither assuming a closed form, on **non-uniform** bonds `f ∈ (0,1)`:

| n | edges | `φᵀ_n == κ_n` | `(−1)^{n−1}φᵀ_n ≥ 0` |
|--:|--:|---|---|
| 2 | 1 | 200/200 | 200/200 |
| 3 | 3 | 200/200 | 200/200 |
| **4** | **6** | **200/200** | **200/200** |
| 5 | 10 | 200/200 | 200/200 |

So **the alternation and the identity both hold at n = 4** for the full cumulant.
This **replicates** #6152's sign-law measurement (n = 2…5) by a different route —
they enumerated connected graphs; this adds the Möbius-partition side and shows
the two agree exactly. Independent confirmation, not a new result.

**Therefore a `b₄` that differs from `±φᵀ₄` is not the full Möbius cumulant.**
That points at the corpus recursion `mu4 = M[4] − 6·mu2 − 4·mu3`, whose uniform
multiplicities `6` and `4` are correct only when all six bonds and all four
triangles are equivalent. At ⁴He they are not — the committed witness carries
three distinct adjacent flavour templates (`p–p` d = 0, `p–n` d = −0.10446,
`n–n` d = −0.20906) and four visibly different `μ₃`.

### (M2) fails — measured

[`h12_trace_multiplicativity_probe.py`](../../computations/probes/h12_trace_multiplicativity_probe.py)
tests the other half from committed data alone. If `g` were multiplicative, each
⁴He triangle gives a quadratic in one unknown `g₀`, and multiplicativity requires
**one** `g₀` to solve all four:

| triangle | upper root | lower root |
|---|---|---|
| (0,1,2) | 0.9518763229 | 0.2249114312 |
| (0,1,3) | 0.9424870830 | 0.2254420970 |
| (0,2,3) | 0.9380714213 | 0.2619423044 |
| (1,2,3) | 0.9569267307 | 0.2605089705 |

Relative spread **1.99 %** (upper) and **15.2 %** (lower). No common `g₀`:
**the H₁₂ subset-trace is not a multiplicative Mayer weight.**

The consequence is worth stating carefully, because it inverts which fact needs
explaining. A Mayer/Ursell identity should **not** be expected to hold of this
trace at *any* order. So #6152's n = 4 miss is the expected case, and its
**n = 3 match at 400/400 is the coincidence** — 3 bodies is where a
non-multiplicative deviation has too few degrees of freedom to show up.

## 3 · What this does and does not change

**Unchanged:** the alternation is real and reproduced at 4-body (committed
witness); #6152's sign law stands, now independently replicated; the ⁴He
magnitude gap of 9.56× stands.

**Changed:** "the identity fails at n = 4" should no longer be read as evidence
against the alternation programme. It is evidence that the corpus's 4-body
assembly is either not the full Möbius cumulant, or not multiplicative, or both —
and both halves are now measured, with the second refuted outright.

**Not claimed.** That the corpus's `μ₄` is wrong. That a multiplicative weight
*should* be sought. That `f_corpus = e^{−v}` holds — #6152's stated load-bearing
gap is untouched here, and (M2)'s failure arguably makes it harder, since a
non-multiplicative trace is not a Boltzmann weight of any pair potential. That
the 9.56× magnitude gap is explained: it is not.

## 4 · Verification

- Alternation probe: exact `fractions.Fraction` end to end, **no float anywhere**
  in the arithmetic and none in the witness; `φᵀ` and `κ` computed by two
  structurally different algorithms and required to agree.
- Multiplicativity probe: mpmath 40 dps, inputs are the committed witness's own
  values — which are serialized there as **raw float64**, so this probe's
  precision is bounded by its input and claims nothing beyond it. The verdict is
  a spread of 10⁻² to 10⁻¹, some 14 orders above float64 resolution, so it does
  not rest on the arithmetic.
- **No new H₁₂ evaluation.** The expensive path (`pyhecke_native`, 64 character
  evaluations) was deliberately not re-run: its result is committed and the
  corpus-grep found it.
- Exit codes captured directly, never through a pipe.
