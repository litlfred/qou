# ²H, ³H, ³He on the ruled γγ bond: every chain unbinds, at every q > 1

Issue #9039, branch `claude/project-thread-4ieh97`. Owner, 2026-11-22: push the light-isotope
mass formula to A = 2 and A = 3 under the current rulings. Pre-registered in
`computations/probes/light_nuclei_a2_a3/preregistration.md` (commit `a1f9c63ee`, before any
number of the probe).

## Rulings used

Vertex `σ_iσ_{i+1}⁻¹` at strands `(i, i+1)` (reading A), closure on the right, so a bond
enters the newer nucleon (`owner-rulings.md`, 2026-11-22). Production proton and neutron
blocks. Ocneanu trace at `z_D = q³/(q² + 1)`. `B_diff = E₀(tr_free − tr_atom)` and
`B_log = E₀ ln(tr_free/tr_atom)`, both reported, neither chosen.

## 1. Structure (exact ℚ(q), then Lean)

By the chain law `towerTr_ggChain` (proved),
`tr_atom / tr_free = ∏_{bonds} μ_x`, with `μ_x = tr(V³ · x↑¹)/tr(x)` for the nucleon `x` the
bond enters. The first nucleon cancels, so **only the multiset of entered nucleons matters**,
not the order otherwise (Lean: `chain_ratio`).

Exact sympy over ℚ(q), with `y = q² − 1`:

- `μ_p − 1 = y⁴ (q⁴ + q² + 1) Pp / (q² (q² + 1) Dp)`
- `μ_n − 1 = y⁵ (q⁴ + q² + 1)(q⁴ − q² + 1) / (q² (q² + 1) Dn)`

and `Pp`, `Dp`, `Dn`, written in `y`, have all coefficients positive
(`Dp = 4 + 21y + 49y² + … + y⁹`, `Pp = 1 + 7y + … + y⁵`, `Dn = 1 + 3y + … + y⁷`). So
`μ_p > 1` and `μ_n > 1` for every `q > 1`, and the block traces are positive.

Lean, `QOU/Mass/LightNucleiGGChainSign.lean` (sorry-free, axioms `propext`,
`Classical.choice`, `Quot.sound`; generic linearly ordered field, no `ℝ`):

- `chain_gt_free`, `chain_unbinds`: positive block traces and bond factors above them give
  `tr_atom > tr_free`, so `B_diff < 0` for every `E₀ > 0`, for any chain with at least one bond;
- `mu_p_sub_one_pos`, `mu_n_sub_one_pos`, `trace_closed_forms_positive`: the closed forms
  above are positive at every `q > 1`.

The link "these closed forms are the Ocneanu traces of the production blocks" is the exact
ℚ(q) computation of the probe, not a Lean theorem. With it:

**Result (structural, scope (b) within the chain).** Under the ruling, the γγ chain of
production blocks unbinds for every A ≥ 2, every nucleon order and every q > 1. It cannot be
rescued by a choice of order, by `E₀`, or by the value of `q₀`. Binding vanishes as `q → 1`,
at order `y⁴` per bond entering a proton and `y⁵` per bond entering a neutron. The invariant
cited is the positivity of `μ_x − 1`. It does not cover all-pairs (transported) bonds,
many-body γγ vertices, other blocks or a non-trace energy map.

## 2. Numbers at the proton pin (exact Fractions)

`μ_p − 1 = 1.0578e−3`, `μ_n − 1 = 6.1119e−4`. `E₀ = 4.2274833556 MeV`.

| nucleus | order | bonds enter | tr_atom/tr_free | B_diff (keV) | B_log (keV) | AME (keV, comparison) |
|---|---|---|---:|---:|---:|---:|
| ²H | pn | n | 1.000611191 | −0.773 | −2.583 | 2224.6 |
| ²H | np | p | 1.001057753 | −1.337 | −4.469 | 2224.6 |
| ³H | pnn | n n | 1.001222756 | −0.734 | −5.166 | 8481.8 |
| ³H | npn, nnp | p n | 1.001669590 | −1.003 | −7.052 | 8481.8 |
| ³He | ppn, pnp | p n | 1.001669590 | −1.328 | −7.052 | 7718.0 |
| ³He | npp | p p | 1.002116624 | −1.684 | −8.939 | 7718.0 |
| ⁴He | ppnn (control) | p n n | 1.002281802 | −0.862 | −9.635 | 28295.7 |

Controls: ²H pn, ³H pnn, ³He ppn and ⁴He ppnn reproduce §6c of
`2026-11-21-he4-binding-breakdown.md` and the sign table's −0.862 keV; the chain law matches
the full six-strand ²H word exactly. Pre-registered P1 and P2 hold; P3 every order reported.

## 3. Audit against experiment (comparison only)

- **Sign: wrong for all three nuclei, in every order.** Observed binding is positive.
- **Size: about 500× to 12 000× too small** even in absolute value (²H: 0.8–4.5 keV against
  2224.6 keV).
- **Mirror (P4, no prediction made).** In every order ³He is more unbound than ³H; observed,
  ³He is less bound than ³H. The direction agrees, but between two unbound values this is not
  evidence of anything.

## 4. What this changes, and what is left

Row C4 of `2026-11-22-sign-conventions-table.md` ("⁴He, ²H, ³H, ³He on the γγ bond: all
unbind") was a measurement at `q₀`; it is now a theorem in `q` for the chain, given the
exact trace closed forms. Within the ruled convention, binding for A ≤ 4 has to come from
something other than the γγ chain of production blocks: all-pairs/transported bonds (measured
unbound at `q₀`, §6c, not proved for all q), many-body vertices, different nucleon blocks, or
the energy map. For contrast only (not the ruling): with the bond entering the older nucleon,
`μ_p − 1 = −y³ (q⁴ + q² + 1)(4 + 21y + 47y² + …)/(…) < 0` for every q > 1, so that side binds
through protons; `μ_n − 1` there changes sign at a finite q.

## Reproduce

```
python3 -u computations/probes/light_nuclei_a2_a3/light_nuclei_a2_a3_probe.py
scripts/lean-verify.sh folio/quantum-observable-universe/lean/QOU/Mass/LightNucleiGGChainSign.lean
```
