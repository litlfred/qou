# Flavor-split α via the bond-dilog — RULED OUT (2026-06-29)

**Branch:** `claude/flavor-split-alpha-bond-dilog-2026-06-29`
**Probe:** `computations/probes/flavor_split_alpha_bond_dilog_probe.py` (+ witness)
**Closes the dilog line of attack on** the open flavor-split coefficient α
(see `2026-06-29-flavor-split-alpha-dilog-expansion.md`,
`2026-06-29-flavor-split-partial-derivation.md`).

## Question

The flavor split is `split = leading·(1 + α·leading)` (2nd-order structure
proven; α = 0.92925 the open coefficient). The dilog at the *tiny* argument
`leading ≈ 0.00138` was already shown too weak (q-effect ~0.1% vs the 7.8%
gap). Natural next idea: the dilog at the **O(1) bond arguments** — the actual
archimedean bond energy `E = E₀·log(1/f_pn)` (+ `Li_2^q` spectral corrections),
where `f_pn = z − h·(½ − δ/4)` carries O(1) `z ≈ 0.5`, `h ≈ 0.21`.

## Result — RULED OUT

The O(1) bond argument makes α **worse**, not better (both anchors,
anchor-stable to 5.8e-8):

| functional | α | err vs α_true=0.929 |
|---|---:|---:|
| geometric `1/(1−lead)` (full resummation) | 1.0014 | **+7.8%** (closest) |
| single-log | 0.500 | −46% |
| `Li_2^q(lead)` | 0.249 | −73% |
| **bond-log (O(1) arg)** | 0.066 | **−93%** |
| **bond-`Li_2^q` (O(1) arg)** | 0.033 | **−96%** |

**Analytic reason.** Any single `−ln(1 − a·x)` has second-order Taylor ratio
`c₂/c₁² = 1/2`; normalized to the split this gives `α ∝ A` with bond
sensitivity `A = (h/4)/(z − h/2) ≈ 0.13`, so α ≈ 0.066. The `Li_2^q` is smaller
still. The O(1) argument only *rescales* — it cannot raise α toward 0.929.

## Conclusion

**Only the full geometric self-energy resummation `Σ leadingⁿ` (α = 1) lands
near α_true.** So α is a **resummed self-energy, not a single bond-dilog at
any argument**. This is consistent across all three probes: the correction is
the geometric self-energy (α = 1, 0.0098%), and the exact 0.929 (7.8% below
geometric) is the **mass-functor per-block normalization** — the same open
piece gating Δ_λ — **not** a dilog effect. Per anti-flip-flop discipline, 0.929
is *not* fitted to any dilog. The dilog line of attack on α is closed.

## Reproduce
```bash
python3 computations/probes/flavor_split_alpha_bond_dilog_probe.py
```
