# λ-coloured WRT → `W_λ`: the Schur–Weyl / q-Plancherel 4-count refinement

**Date:** 2026-06-22
**Branch:** `claude/inspiring-albattani-ijfp7m` (PR #2608)
**Status:** Positive/structural — refines (and partly corrects) the #2603 counting obstruction; the
WRT→`W_λ` route via *fundamental* SU(2) Schur–Weyl is shown obstructed, the open object sharpened.
No fit; no `component = W_λ` match asserted.
**Bean:** [`s5bb`](../../.beans/s5bb--s5-so3-keystone.md)
**Follows:** [`2026-06-22-keystone-wrt-color-schurweyl.md`](2026-06-22-keystone-wrt-color-schurweyl.md) (#2603)
**Uses (corpus):** [`2026-06-16-keystone-plancherel-target-clarification.md`](2026-06-16-keystone-plancherel-target-clarification.md),
[`2026-06-16-s5so3-ingredient4-fibre-schur-weyl-constraint.md`](2026-06-16-s5so3-ingredient4-fibre-schur-weyl-constraint.md) (#2364)
**Script:** [`scripts/keystone_wrt_schurweyl_plancherel_4count_probe.py`](scripts/keystone_wrt_schurweyl_plancherel_4count_probe.py) (float64, exit 0)
**Witness:** [`computations/keystone-wrt-schurweyl-plancherel-4count.witness.json`](../../computations/keystone-wrt-schurweyl-plancherel-4count.witness.json)

## Context

PR #2603 computed the colour-resolution of the bare Σ(2,3,5) WRT invariant into its four false-theta
components `Ψ̃₃₀^(a)`, `a ∈ {1,11,19,29}` (the icosahedral/E₈ residues), and stated the handoff:

> WRT colour components: **4**; partitions λ⊢5: **7**; physical blocks: **3**. `4 ≠ 7` and `4 ≠ 3` ⇒
> no naïve component↔`W_λ` bijection, *impossible by counting*. The map SU(2)-colour → H₅(q)-block is
> **Schur–Weyl duality**, not the identity — push the SU(2)-coloured WRT data through Schur–Weyl and
> compare the H₅(q)-resolved weights to `W_λ`.

Before running that (wide) numerical comparison, a corpus-grep / formalize-first pass surfaces two
facts already on `main` that sharpen the handoff. They do not close the keystone; they prune the search.

## (A) `W_λ` is the conjugation-symmetric q-Plancherel measure ⇒ 4 distinct values

`W_λ = d_q(λ)²/[5]_q!` is the **q-Plancherel measure**
([target-clarification, 2026-06-16](2026-06-16-keystone-plancherel-target-clarification.md)). Because
the multiset of hook lengths is transpose-invariant, `d_q(λ) = d_q(λ')` and hence `W_λ = W_{λ'}` (the
Plancherel hallmark). On λ⊢5 the seven blocks therefore carry only **four distinct values**:

| distinct `W_λ` | block(s) | conjugation |
|---|---|---|
| **0.29467** (peak) | (3,1,1) | self-conjugate |
| 0.20754 | (3,2), (2,2,1) | (3,2)′ = (2,2,1) |
| 0.12862 | (4,1), (2,1,1,1) | (4,1)′ = (2,1,1,1) |
| 0.00762 | (5), (1⁵) | (5)′ = (1⁵) |

**Consequence — #2603's counting claim is too strong.** The relevant count is not "7 blocks" or "3
physical blocks" but the **4 distinct Plancherel values**. Against the **4** WRT components this is a
**count match**, so a *value-level* correspondence is **not** counting-forbidden. (This is the
component the #2603 framing missed; raised as a coordination note on #2603, not a silent override.)

## (B) No parameter-free numerical identity (honest negative)

The 4↔4 count match does **not** become a numerical identity. Ordered (descending) and sum-normalized:

| rank | `WRT_norm` | `Wλ_norm` | rel Δ |
|---|---|---|---|
| 1 | 0.42497 | 0.46154 | −7.9 % |
| 2 | 0.33852 | 0.32507 | +4.1 % |
| 3 | 0.21592 | 0.20146 | +7.2 % |
| 4 | 0.02059 | 0.01193 | **+72.6 %** |

The shapes are similar (monotone, same order of magnitude on the top three) but unequal — the smallest
component is off by 73 %. **Forcing equality would be numerology.** The 4↔4 is best read as both objects
inheriting the same icosahedral/E₈ structure, not as a derived identity. (Matches #2603's no-fit
verdict.)

## (C) The #2364 Schur–Weyl row-bound obstructs the peak block

Schur–Weyl duality on a 5-strand tensor space ([#2364](2026-06-16-s5so3-ingredient4-fibre-schur-weyl-constraint.md)):

$$(\mathbb{C}^d)^{\otimes 5} = \bigoplus_{\lambda\vdash 5,\ \mathrm{rows}(\lambda)\le d} S^\lambda \otimes W^{\mathrm{gl}_d}_\lambda,$$

so block λ is hosted **iff** `rows(λ) ≤ d`. On the **spinor ℂ²** (SU(2)) the Hecke algebra acts through
its Temperley–Lieb (sl₂) quotient, which hosts only the ≤2-row blocks `{(5),(4,1),(3,2)}` and
**annihilates every ≥3-row block** — in particular the electron block **(3,1,1)**, which is exactly
where the Plancherel `W_λ` **peaks** (0.29467). Therefore a **fundamental**-SU(2) Schur–Weyl map
cannot reproduce the peak of `W_λ`, regardless of weighting. (The on-main
[#2604 row-count split](2026-06-22-keystone-schurweyl-su2-rowcount.md) states the same ≤2-row rule as a
generation-level fact — muon (3,2) spin-reachable, electron (3,1,1) colour; this PR's `W_λ` weight
analysis is the complementary measure-side statement.)

## Net — the sharpened open object

- The WRT→`W_λ` route via **fundamental** SU(2) Schur–Weyl is **obstructed**: the (3,1,1) peak (and the
  other ≥3-row blocks (2,2,1),(2,1,1,1),(1⁵)) are unreachable on a 2-dim fibre.
- Reaching them needs **≥3-dimensional** colour data: either higher SU(2) Wilson lines (spin ≥ 1,
  dim ≥ 3) whose Schur–Weyl content reaches ≥3 rows, or the colour-ℂ³/SU(3) promotion (#2364's bridge),
  which reconnects to **"no finite colour-SU(3) arena"** ([#2406](2026-06-16-keystone-arena-is-full-hecke-not-su3.md))
  → the full-Hecke principal-specialization object.
- The genuine remaining step is to **derive** that higher-colour Schur–Weyl weighting from the WRT data
  and check whether it lands the 4 distinct `W_λ` values without a free parameter. If it requires a
  parameter, the route is **underdetermined** — the honest Stage-C-style outcome, recorded as such.

> **Update (same PR — resolved).** The higher-colour step is now **foreclosed for all colour `d`**: the
> colour-multiplicity weight is conjugation-asymmetric (`m₅(5)=126` vs `m₅(1⁵)=1`) while `W_λ = W_{λ'}`,
> and its support `{rows ≤ d}` misses `W_λ`'s 4-/5-row blocks for `d < 5`. So the WRT-colour functor lands
> the **production** weight, not the Plancherel `W_λ`; the latter needs the symmetric pairing (full-Hecke
> `d_q²`). See
> [`2026-06-22-keystone-wrt-schurweyl-higher-colour-foreclosure.md`](2026-06-22-keystone-wrt-schurweyl-higher-colour-foreclosure.md). The on-main
> [dual-sides capstone](2026-06-22-keystone-schurweyl-dual-sides.md) reaches the same terminus (WRT↔`W_λ`
> is Schur–Weyl *duality*, not equality); the 4↔4 count match recorded here is a **near-coincidence
> consistent with that** — structural, not a numerical identity (residuals up to 73 %).

This is a forward (formalize-first) prune complementing #2603, not a closure.

## Cross-checks (probe, no fit)

- `W_λ` recomputed from the q-hook formula vs the canonical table: max `|Δ| = 4.6×10⁻⁶`.
- Plancherel total **`Z = 0.98222`** — independently reproduces the #2517 sub-normalization
  (mass-defect `1 − Z = 0.0178`).
- conjugation symmetry `W_λ = W_{λ'}` holds to `< 10⁻¹²` → exactly 4 distinct values.
- WRT component sum `= 2.329577` (= bare `Ψ(1/q₀)`, `|Δ| = 0`).

## Cross-references

- [`2026-06-22-keystone-wrt-color-schurweyl.md`](2026-06-22-keystone-wrt-color-schurweyl.md) — #2603, the colour-resolution this refines.
- [`2026-06-16-keystone-plancherel-target-clarification.md`](2026-06-16-keystone-plancherel-target-clarification.md) — `W_λ` = q-Plancherel measure.
- [`2026-06-16-s5so3-ingredient4-fibre-schur-weyl-constraint.md`](2026-06-16-s5so3-ingredient4-fibre-schur-weyl-constraint.md) — #2364 row-bound.
- [`2026-06-22-keystone-schurweyl-dual-sides.md`](2026-06-22-keystone-schurweyl-dual-sides.md) — the on-main dual-sides capstone (WRT↔`W_λ` = Schur–Weyl duality); the 4↔4 here is a near-coincidence consistent with it.
- [`2026-06-22-keystone-schurweyl-su2-rowcount.md`](2026-06-22-keystone-schurweyl-su2-rowcount.md) — #2604, the on-main SU(2) row-count split.
- [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) — the keystone ledger.

## Possible Lean follow-up (not in this PR)

The conjugation symmetry `W_λ = W_{λ'}` for the q-Plancherel measure follows from transpose-invariance
of the hook-length multiset — a clean, sorry-free candidate lemma (`#distinct W_λ on λ⊢5 = 4`). Deferred
(sandbox Lean env cold); noted for a follow-up.
