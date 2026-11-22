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
something other than the γγ chain of production blocks: all-pairs/transported bonds (A = 3: one
crossing q* ≈ 1.49–1.65, unbound at q₀, see §5), many-body vertices, different nucleon blocks, or
the energy map. For contrast only (not the ruling): with the bond entering the older nucleon,
`μ_p − 1 = −y³ (q⁴ + q² + 1)(4 + 21y + 47y² + …)/(…) < 0` for every q > 1, so that side binds
through protons; `μ_n − 1` there changes sign at a finite q.

## 5. All-pairs bonds at A = 3: one crossing per cell, not a fixed sign

Preregistration addendum (commit `b83d7b041`), which discloses one timing cell computed before
the addendum was written. Bonds go on (0,1), (1,2) and (0,2). The non-neighbour bond is
transported by `σ₂σ₃σ₄ · V³ · (σ₄σ₃σ₂)⁻¹` (over) or with reversed crossing signs (under).
The computation is exact ℚ(q) on 9 strands for every order and both variants: 12 cells.

**Structure (exact).** In every cell,
`tr_atom/tr_free − 1 = −(q−1)ᵏ(q+1)ᵏ(q⁴+q²+1)·P(q)/D(q)`.
- `k = 5` if all three bonds enter a neutron (³H pnn), else `k = 4`.
- `P` is irreducible over ℚ, even in q, of degree 30 to 46.
- `D = qᵃ(q²+1)ᵇ·Dpⁱ·Dnʲ`, which is positive for q > 1 (§1).

Written in `y = q² − 1`, each `P` has negative coefficients up to some degree m (10 to 13)
and nonnegative coefficients after, with negative constant and positive leading coefficient.
Lean `single_crossing` (sorry-free, generic ordered field, standard axioms) proves that such
a polynomial crosses zero at most once on y > 0, from below. With `P(0) < 0` and `P → +∞`,
each cell therefore has exactly one crossing `q*`:
**the all-pairs nucleus unbinds on (1, q*) and has `tr_atom < tr_free` for q > q*.**
The trace itself passes through 0 at a larger `q₀*`, so `B_log` is undefined above that,
while `B_diff` stays positive.

The ratio depends only on the sequence of nucleons the bonds enter: ³H nnp ≡ ³He pnp and
³H npn ≡ ³He ppn, identically in q (the closed forms are equal as strings).

| cell | leading term at q = 1 | q* (ratio = 1) | q₀* (tr_atom = 0) |
|---|---|---:|---:|
| ³H pnn over / under | (9/2) y⁵ | 1.49366 / 1.61678 | 1.59923 / 1.72759 |
| ³H npn ≡ ³He ppn, over / under | (3/8) y⁴ | 1.54374 / 1.64633 | 1.63744 / 1.74581 |
| ³H nnp ≡ ³He pnp, over / under | (3/4) y⁴ | 1.49321 / 1.60889 | 1.59797 / 1.70754 |
| ³He npp over / under | (9/8) y⁴ | 1.54338 / 1.63347 | 1.63365 / 1.72227 |

**Metallic means: none.** No root of any numerator factor, for either the ratio or the
trace, is a metallic mean `(m + √(m²+4))/2` (m = 1…5) or its square root. The only small
factors are `q ± 1` and the cyclotomic `q² ± q + 1`.

**At the proton pin** (q₀ ≈ 1.110, inside (1, q*) in every cell), all 12 rows unbind. In
keV, B_diff / B_log:

| | over | under |
|---|---|---|
| ³H pnn | −1.117 / −7.856 | −1.134 / −7.971 |
| ³H npn | −1.394 / −9.797 | −1.406 / −9.882 |
| ³H nnp | −1.651 / −11.60 | −1.667 / −11.72 |
| ³He ppn | −1.846 / −9.797 | −1.862 / −9.882 |
| ³He pnp | −2.187 / −11.60 | −2.208 / −11.72 |
| ³He npp | −2.553 / −13.54 | −2.568 / −13.63 |

**Controls.** P5: the production orders reproduce the mpmath witness of
`he4_gg_all_pairs` to below 1e−28. P7: appended and arranged placements give the same trace
exactly.

**What this changes.** The chain theorem (§1) has a fixed sign at every q > 1. All-pairs
bonding does not: its sign is set by where q₀ sits relative to `q*`. Binding at some q > 1
exists (q > q* ≈ 1.49–1.65). That is a statement about the model, not a choice: nothing here
moves q₀, which is pinned by the proton ratio. At q₀ the all-pairs nuclei unbind, 0.1–0.3 %
heavier than free, in every order and variant. The gap from q₀ ≈ 1.110 to q* ≈ 1.49 is large,
so no small change of pin reaches the binding side.

**Not in Lean.** That these rational functions are the traces (exact sympy), the coefficient
lists of P (exact, recorded in the witness), and the root values (sympy isolating intervals).

Reproduce: `python3 -u computations/probes/light_nuclei_a2_a3/light_nuclei_a3_all_pairs_probe.py`
(about 20 min).

## 6. ⁴He all-pairs, exactly in q: the A = 3 pattern does not carry over

Probe `he4_all_pairs_exact_probe.py`, engine `hecke_flint.py`, witness
`he4-all-pairs-exact.witness.json`, preregistered as addendum 2 (P8–P10). The routes and
the order p p n n are those of `he4_gg_all_pairs`. By `towerTr_disjoint` (proved) the first
nucleon factors out, so each cell is a 10-strand trace, exact in ℚ(q).

**Controls.**

- P8: all 9 cells reproduce the mpmath rows of `he4-gg-all-pairs.witness.json` to below 1e−28.
  The chain gives −0.862 keV.
- P9: at A = 3, tr N₀ · tr(tail) equals the full trace exactly in all 12 cells.

The first run failed P8 on 6 of 8 cells. It placed each bond after its own block j, while
the reference places it after the running maximum of j along the route. The preregistration
records the fix, and the rows below are from the corrected run.

**Structure.** In every cell `ratio − 1 = tr_atom/tr_free − 1` has the factor (q − 1)⁴(q + 1)⁴,
so it vanishes to order y⁴ at q = 1 (y = q² − 1), with leading coefficient +3/8. All the
other small factors are positive for q > 1. The sign is carried by one big factor per cell.

| cell | big factor degree in q | sign changes in y | crossings q* > 1 | B_diff at the pin (keV) |
|---|---:|---:|---|---:|
| γγ chain (control) | 46 | 0 | none | −0.862 |
| D+D a, over | 88 | 4 | **1.5394, 1.6880** | −1.607 |
| D+D a, under | 84 | 3 | 1.9755 | −1.642 |
| D+D b, over | 90 | 2 | **none** | −1.607 |
| D+D b, under | 84 | 3 | 1.9271 | −1.642 |
| ³H+p, over | 84 | 3 | 1.5486 | −1.606 |
| ³H+p, under | 78 | 1 | 1.7474 | −1.643 |
| ³He+n, over | 90 | 1 | 1.6482 | −1.607 |
| ³He+n, under | 84 | 1 | 1.6275 | −1.642 |

Each crossing is isolated in an exact rational interval of width 1e−22, and each is a simple root.

**What this says.**

1. Every cell unbinds near q = 1, since ratio − 1 is positive there. Every cell also unbinds at
   the proton pin q₀ ≈ 1.110, by about 1.6 keV (B_log about −18 keV), against AME 28 296 keV
   (comparison only).
2. Six cells have exactly one crossing, as at A = 3, so they bind for q above q*.
3. D+D a over has two crossings. It binds only on the window 1.539 < q < 1.688 and unbinds
   again above it.
4. D+D b over never binds for q > 1. Its factor has two sign changes in y but no positive root
   (Sturm count 0).
5. So the A = 3 pattern of one crossing per cell is **not** structural at A = 4. The single
   crossing theorem (`single_crossing`, Lean) applies only where the y-coefficients change sign
   once. Here they change sign 1 to 4 times.
6. Every crossing lies at q ≥ 1.539, far above q₀. Within this model no cell binds at the pin.

Nothing here is adopted. It is a scope-(a) negative: the γγ all-pairs bond, alone, under the
four formation routes, does not bind ⁴He at q₀.

## 7. Where the y⁴ comes from: bonds into a proton (exploratory, not proved)

Probe `bond_leading_order_probe.py`, witness `bond-leading-order.witness.json`. It is
exploratory and was not preregistered. It measures the leading order of ratio − 1 at q = 1,
exactly, for single bonds and bond sets at A = 2, 3, 4.

- **Rule A** (written first): a like-proton bond gives (3/8)y⁴, and any other bond gives
  (3/2)y⁵. It fits 24 of 28 cases and fails at np, (0,1).
- **Rule B** (read off those 28 cases, so they cannot test it): to leading order the bonds
  add. A bond (i, j) whose receiving block j is a **proton** gives (3/8)y⁴. A bond into a
  **neutron** gives (3/2)y⁵. So

  ratio − 1 = (3/8)·n_into_p·y⁴ + O(y⁵) when n_into_p > 0, and otherwise
  (3/2)·n_bonds·y⁵ + O(y⁶).

- Rule B was then tested on 16 holdout cells, fixed before they were run (A = 3 and A = 4,
  orders npp, nnp, npn, nnn, pnpn, nnpp, npnp, pnnp). It holds on **16 of 16**. Rule A holds on
  2 of 16.

This explains §6: in the order p p n n, every route has exactly one bond into a proton,
(0, 1). The other five bonds all go into a neutron. Hence the same +3/8 in every cell.
Over and under transport never change the leading term.

**Status: conjecture.** It is measured exactly on 44 cells. It is not proved, and there is no
Lean for it. A proof would need the h-expansion of the Ocneanu trace of a word with V³
inserted, where V³ = 1 at q = 1: first-order additivity over bonds, plus the vanishing of
orders y¹ to y³ (y¹ to y⁴ into a neutron).

## 8. Why "into a proton": exact at A = 2 for every Markov parameter z

Probe `bond_generic_z_probe.py`, witness `bond-generic-z.witness.json` (exploratory). The
first nucleon factors out by `towerTr_disjoint`, so one bond (0, 1) acts on a 4-strand tail:
the receiving block's word on σ₁, σ₂, followed by V³ on σ₀, σ₁. The tail shares σ₁ with
the bond. The computation is exact over ℤ[h, z], with the trace parameter z left **free**:

- **into a proton:** tr_atom − tr_free = h⁴ (z² − hz − 1) P_p(h, z) / 4, with
  P_p = −h⁷ + h⁶z − 4h⁵ + 3h⁴z − 6h³ + 2h²z − 3h − 2z;
- **into a neutron:** tr_atom − tr_free = h⁵ (h² + 1)(h² + 4)(hz − h² − 1)(z² − hz − 1) / 4.

Since y = q h, these give the orders y⁴ and y⁵ of §7. The leading coefficients of
ratio − 1 are (1 − z²)/2 into a proton and (1 − z²)/z into a neutron. At z_D(1) = 1/2 these
are 3/8 and 3/2. So the per-bond rule at A = 2 holds for **every** z, not only z_D, and the
extra power of h into a neutron is a fact about the two block words, not about the trace
parameter. Both effects vanish exactly where z² − hz − 1 = 0, that is at z = q or z = −1/q.

Lean status:

- **Proved, sorry-free (pilot, kept in a scratch file, not committed):** σ₁²·V³ is
  trace-neutral, tr(σ₁² V³) = tr(σ₁²) for every z and h. The proof runs the repo's verified
  evaluator `trWord` (`markov-trace-recursive-reducer`) with simp and ring.
- **Proved in Lean, sorry-free:** the two identities above, and the two free traces, over any
  field with 2 ≠ 0 (content block `prop:light-nuclei-a2-bond-tail`, namespace
  `QOU.LightNucleiBond`). The naive expansion (256 and 512 positive words) ran out of memory, so
  the proof uses a merging evaluator `ME` that collects like basis terms after each letter;
  `ME_eq_P` proves it equals the plain expansion, and `tail_eq_trWord` writes that as a sum of
  `trWord` over subwords. `bond_into_proton_vanishes` and `bond_into_neutron_vanishes` give the
  zero at z² − hz − 1 = 0. The full file takes about 10 minutes with lean-direct.
- **Proved in Lean, sorry-free (same block):** the step from the full A = 2 word to the
  four-strand tail. `a2_reduce` shows that for any first nucleon N₀ ∈ H₃ the γγ chain
  `ggChain N₀ [N]` and the free product `freeTail [N₀, N]` have traces tr N₀ · tail(N↑¹ V³)
  and tr N₀ · tail(N↑¹). `a2_bond_into_proton` and `a2_bond_into_neutron` then state the two
  identities on the full A = 2 words, times tr N₀. Axioms: propext, Classical.choice,
  Quot.sound.
- **Not in Lean:** the leading coefficients read off the identities, and additivity over
  several bonds at A ≥ 3 (§7, §9), which is checked exactly but not proved.

## 9. A = 3 and A = 4 with z free: additivity holds for every z (exploratory, not proved)

Probe `a3_bonds_generic_z_probe.py`, witness `a3-bonds-generic-z.witness.json`. The
prediction was written in the probe's docstring before it was run, from the A = 2 identities
of §8: bonds add at leading order in h, so

- ratio − 1 = n_into_p · (1 − z²)/2 · h⁴ + O(h⁵) when at least one bond goes into a proton;
- ratio − 1 = n_bonds · (1 − z²)/z · h⁵ + O(h⁶) otherwise.

It is tested as an identity in z, exact over ℚ[h, z]: all 8 orders, four bond sets
({01, 12}, {01, 12, 02}, {02, 12}, {02}), over and under transport. **64 of 64 cells match**,
and the free trace at h = 0 is z² in every cell. So Rule B of §7 is not a property of z_D:
the per-bond coefficients and their sum hold for every Markov parameter. At A = 4 the
same rule, also written down before the run (`a4_bonds_generic_z_probe.py`, witness
`a4-bonds-generic-z.witness.json`), holds in **224 of 224 cells**: all 16 orders, over and
under, for the γγ chain, the four all-pairs formation routes of §6 (bond placed after the
running maximum of j, as there), and the non-chain sets {02, 13} and {13}. The free trace at
h = 0 is z³ in every cell. At z = 1/2 the p p n n all-pairs cells give leading coefficient
3/8, matching §6: only the bond 01 goes into a proton.

So in every cell measured at A = 3 and A = 4, the leading order is the sum of the A = 2
per-bond terms, a bond (i, j) counting as a bond into nucleon j. The sign changes of §6 come
from higher orders, not from the leading one.

What this does not show: it is a check on finitely many words, not a proof of additivity,
and it says nothing about the orders beyond the leading one. For chain bonds the exact
product form already follows from `towerTr_ggChain`; the non-chain cells (bond 02) are the
new evidence.

**Lean: still open.** The A = 2 proof evaluates a 4-strand tail and takes about 10 minutes.
At A = 3 the tail has 7 strands and twice as many letters, so the same brute-force evaluation
will not fit. A structural proof needs an argument that is not yet available. V³ − 1 is only
O(h) as an algebra element, since (s₀s₁)³ = 1 in S₃, so the h⁴ comes from cancellation in the
trace. Cross terms between two bonds are therefore not obviously of higher order. Leading-order
additivity stays a conjecture, backed by the 288 exact cells above.

## Reproduce

```
python3 -u computations/probes/light_nuclei_a2_a3/light_nuclei_a2_a3_probe.py
python3 -u computations/probes/light_nuclei_a2_a3/light_nuclei_a3_all_pairs_probe.py
python3 -u computations/probes/light_nuclei_a2_a3/he4_all_pairs_exact_probe.py  # about 6 min, needs python-flint
python3 -u computations/probes/light_nuclei_a2_a3/bond_leading_order_probe.py  # about 70 s
python3 -u computations/probes/light_nuclei_a2_a3/bond_generic_z_probe.py  # about 1 s
python3 -u computations/probes/light_nuclei_a2_a3/a3_bonds_generic_z_probe.py  # about 1 s, needs python-flint
python3 -u computations/probes/light_nuclei_a2_a3/a4_bonds_generic_z_probe.py  # about 20 min on 4 cores
lean -DautoImplicit=false -s 65536 folio/quantum-observable-universe/mass-endomorphism/light-nuclei-a2-bond-tail.lean  # about 9 min; needs the reducer olean on LEAN_PATH
scripts/lean-verify.sh folio/quantum-observable-universe/lean/QOU/Mass/LightNucleiGGChainSign.lean
```
