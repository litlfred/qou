# O2 applied to the κ(A) contest — the winning kernel is not admissible

**Status:** FINDING (reproducible, nothing fitted beyond the single scale the
incumbent hypothesis already carries, nothing wired). Bean `qou-17mq`, opened
2026-08-01 and untouched since.

Probe: [`em_linking_o2_neutralised_kernel_probe.py`](../../computations/em_linking_o2_neutralised_kernel_probe.py)
(witness `em-linking-o2-neutralised-kernel.witness.json`, 4 assertions, all
passed).

## Why this exists

[`2026-08-01-em-linking-reads-round1.md`](2026-08-01-em-linking-reads-round1.md)
records two structural obstructions from its round-2 reading of the primary
sources. **O1** (total antisymmetry) is cited constantly downstream and has
shaped every subsequent route. **O2** has not been applied to anything:

> On a closed manifold `∫Δu = 0` forces total charge zero … the pp-pair energy
> must be defined relative to the neutralizing background (equivalently, only
> charge-neutral combinations are well-posed), and the Green's function
> acquires a `−1/vol(M)` offset.

Corpus-grepped 2026-08-25: `neutralis*` / `neutraliz*` / "compact-quotient
neutrality" appear at **four** sites, all inside that one audit, and at **zero**
sites in `computations/`. No probe, no witness, and no Lean file has ever
applied O2. Meanwhile the same front's headline result — the κ(A) hypothesis
contest of `em-linking-mirror-series.witness.json` — scores a kernel that O2
excludes.

## The argument

The surviving route is the metric Coulomb pairing `⟨A₁, J₂⟩` on the `H³` scalar
Green's function `φ₀(α) = −coth(α)/4π`, and the hypothesis scored against the
mirror series is

$$H_{\mathrm{coth}}:\quad \kappa = \coth(\alpha),\qquad \alpha = c\,A^{1/3}$$

a one-parameter law. It won the contest on scatter, and the qualitative feature
that separated it from its rivals is **saturation**: `coth α → 1`, so `κ → +1`
in heavy nuclei while the power laws send `κ → 0`.

**An unsubtracted `coth` is exactly what O2 forbids.** On a finite-volume `M`
the admissible pair kernel is the *zero-mean* Green's function. The robust
consequence needs no model of that kernel:

> A zero-mean function that is not identically zero **must take both signs**.
> `coth(α)` is strictly positive and monotone. So no admissible kernel is a
> positive saturating function of the separation.

Physically this is ordinary jellium: a like-charge pair against a neutralising
background is repulsive at short range and *attractive* beyond a critical
separation. The saturation that won the contest is a property of the
**excluded** member.

Two scoping notes, both in the direction that weakens the claim:

- **Finite volume suffices** — `∫Δu = 0` does not need compactness, so the
  argument covers the corpus's *cusped* finite-volume hyperbolic complements
  (`4₁`, `L6a4`) as well as a closed quotient. The audit asserts the QOU fibre
  is a compact hyperbolic quotient; this probe takes that premise as given and
  notes it is stronger than the argument needs.
- **The one-term model is a model.** Writing the admissible family as
  `coth(α) − c₀` with `c₀ = ⟨coth⟩_M > 1` (strictly, since `coth > 1`
  pointwise) is the simplest realisation of the zero-mean condition, not the
  exact Green's function of a quotient, which is a regularised Poincaré series.
  The sign-change conclusion above does **not** depend on it; the numbers below
  do.

## The numbers

Re-scoring the **same** committed κ series (29 bound mirror pairs, `A = 3…63`),
with the same statistic the contest used — form the implied scale constant per
pair, report its relative scatter:

| kernel | `c₀` | admissible? | scatter | residual `r` vs `A` |
|---|---:|---|---:|---:|
| `H_coth`, as scored | 0 | **no** | **3.505 %** | +0.049 |
| best admissible member | 1.0 | boundary | 11.15 % | **−0.904** |
| | 2.0 | yes | 15.27 % | |
| | 4.0 | yes | 19.30 % | |
| | 7.5 | yes | 22.32 % | |

An end-to-end assertion checks that the incumbent row reproduces the committed
bound-only `H_coth` scatter to `< 10⁻⁶`, so the admissible rows are being
compared against the same arithmetic rather than against a quoted number.

Three readings, in descending order of how much they rest on the model:

1. **Scatter is monotone in `c₀`.** Every step toward a genuinely neutralised
   kernel makes the description worse, and the best admissible member is the
   `c₀ = 1` infinite-volume *boundary* — the least-neutralised point of the
   family, and not an interior member for any finite `M`. There is no
   admissible optimum in the interior to appeal to.
2. **The admissible boundary member fails the corpus's own residual test.**
   `em-linking-residual-structure.witness.json` separated `H_coth` from
   `H_FH_Z` on exactly this criterion: structureless residuals (`r = 0.049`)
   for the winner against a strong systematic trend (`r = 0.799`) for the
   loser, and the drift was counted against the loser. The admissible kernel
   carries `r = −0.904` — *more* structure than the hypothesis that was
   rejected for carrying structure.
3. **48 of 140 scanned admissible members are contradicted without any appeal
   to scatter.** For `c₀ > 1` the predicted `κ` crosses zero at a finite
   `A_zero = (\mathrm{arccoth}(c₀)/c)³`; for 48 of them that crossing lands
   inside `A ∈ [3, 63]`, where every measured `κ` is strictly positive
   (min 1.4127).

At the heaviest pair (`A = 63`, `Z = 32`, `κ = 1.4127`) the inadmissible
incumbent predicts 1.4225 and the admissible boundary member 1.1593.

## Scope

Per the STRICT (a)/(b) discipline:

- **(b) structural exclusion, invariant cited.** Compact- (indeed
  finite-volume-) quotient neutrality, `∫Δu = 0`, excludes the *unsubtracted*
  kernel `coth(α)` from the admissible family, and with it the saturation
  prediction. This is an exclusion of **the kernel as written**, not of the
  hyperbolic Coulomb route.
- **(a) scope-limited negative.** The admissible family, scored on this series
  with this frozen `B_pp` unit, does not improve on the inadmissible incumbent
  and gets monotonically worse with neutralisation. That is a statement about
  this parameterisation on this data.

**Not claimed.** The metric Coulomb pairing `⟨A₁, J₂⟩` on the hyperbolic
Green's function remains the surviving route, exactly as round 3 left it.
Nothing here excludes it, nothing here proposes a replacement, and nothing is
wired.

## What this changes for the standard-model chain

The two-like-charge EM-linking invariant is object **4-B** of
[`sm-eightfold-derivation-cheat-sheet.md` §4](../sm-eightfold-derivation-cheat-sheet.md),
ranked **1** in that file's near-term-derivable table because it is the only
one of the three gating objects that needs no `SU(3)` and because it closes
`m_d − m_u` and 69 % of the ³He mirror residual together.

Its status is unchanged — still open, still the gate. What changes is the
evidential situation *inside* it. The contest that appeared to have selected a
kernel compared:

- an **inadmissible** kernel (this finding), against
- two hypotheses whose **warrant had already been withdrawn** as a
  misattribution of a single-torus bound to a link (round 5).

So no member of that contest carried a live structural warrant at the time it
was scored, and its ranking should not be cited as support for
hyperbolic-saturation. The honest position on 4-B is that the *route* is
identified and the *kernel* is not.

## Carried confound

Bean `qou-gcmn`: the per-pair Coulomb unit is held at its `A = 3` `H₆` value
across the whole series, so any `A`-dependence of the strong bond `B_pp` is
absorbed into `κ`. That bounds what **any** scatter comparison on this series
can establish, this probe included. It does not touch the structural argument,
which involves no data at all.

## Next

The question this sharpens is well-posed and does not need more literature:
what is the zero-mean Green's function of the actual fibre? The one-term model
is a stand-in; a real Poincaré-series computation on a specific finite-volume
quotient would either produce a kernel whose shape fits `κ(A)` or establish
that no admissible kernel does — and the second outcome is as valuable as the
first, since it would move 4-B from "route identified" to "route excluded" and
force the search elsewhere.

## Housekeeping — four audit witnesses deliberately NOT regenerated

`scripts/precision-gates.sh --changed` reports RED on the raw-float64 ratchet
and flags four stale committed audit witnesses. Both are inherited from `main`,
not introduced here:

- The 5 newly-dirty witnesses are `deltalambda/deuteron-interface-handle-curvature`,
  `qbeta/birkhoff-barodd-pythagoras-bridge`, `qbeta/a3-branching-asymmetry-vs-required`,
  `deltalambda/yekutieli-trefoil-surface2form-discretization` and
  `deltalambda/sigma1cubed-seifert-surface-term`. None is touched by this
  change. The witness added here carries **zero** raw-float64 fields.
- The four regenerations were **reverted rather than committed**. This
  container has no `numpy`, `scipy`, `sympy` or `clarabel`, carries
  `mpmath 1.4.1` against the corpus's `1.3.0`, and a different
  `pyhecke_native_build`. Committing them would have overwritten real
  provenance with a degraded environment record and moved counts
  (`Q0_OK 963 → 970`, `STALE 229 → 228`) that cannot be attributed to content
  from inside this container. Leaving a witness honestly stale beats
  committing one that measures the harness.
