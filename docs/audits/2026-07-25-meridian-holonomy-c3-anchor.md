# c₃ bar-odd: the meridian-holonomy q₀↦u deformation MAGNITUDE is anchor-smooth — an exact boost-hyperbola amplification bound (scope-(a))

**Date:** 2026-07-25 · **Axis:** Q_β c₃ (bar-odd `S`) · **Branch:**
`claude/qbeta-meridian-holonomy-c3-anchor-2026-07-25` (PR #4288) · **Tier:**
structural (Lean-exact) + measurement (scope-(a)). **No `c_k` wired; nothing
inverts `Q_β`/CODATA; registry untouched; no tier change.**

- **Lean:** [`QOU/QBeta/MeridianHolonomyAnchorCarrier.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/MeridianHolonomyAnchorCarrier.lean) (`lean`-direct exit 0, sorry-free).
- **Probe:** [`qbeta_meridian_holonomy_anchor_swing_probe.py`](../../computations/qbeta/qbeta_meridian_holonomy_anchor_swing_probe.py) (witness `qbeta-meridian-holonomy-anchor-swing.witness.json`, 4/4).

## The question (this branch's distinct angle)

C1 (#4282, sorry-free) proved the bar-odd datum is the ι-odd antisymmetric
off-diagonal `ω(β,p,q)=β·p−β⁻¹·q`, and its companion showed `ω` is **anchor-smooth**
(4.56 ppm swing across the muon↔proton `q₀` anchors) while `c₃` swings 3.47 %
(≈ 7.6×10³×). C1's audit relocated the missing anchor-dependence to the
**meridian-holonomy `q₀↦u` deformation** — the Neumann–Zagier
`CVol(u)=Vol−(τ/4)u²+…` off the complete point `u=0`, `CuspShapeBarParity`'s open
link. #4283 (active B-tranche) pursues the *in-block module-map* successors
(θ-tower + cyclotomic level), which C1 showed inherit the block basis'
anchor-smoothness. **This session attacks the orthogonal carrier: the `q₀↦u`
deformation itself.**

The precise question: does the deformation's **magnitude channel** supply the
percent-level anchor swing? Meridian holonomy is multiplication by `q`
(`meridian-holonomy-boost.md`), so the bar-odd deformation shape is
`barOdd q = q − q⁻¹` (`= 2 sinh(log q) = u + O(u³)`, substrate meridian
coordinate `u = 2 log q₀`), and the NZ observable enters as `S ∝ u²`.

## The formalize-first result — an exact amplification bound

The log-`q` sensitivity of the deformation magnitude is
`d log|barOdd q| / d log q = barEven q / barOdd q` (since
`d(barOdd q)/d(log q) = barEven q`). The **boost hyperbola**
`barEven² − barOdd² = 4` (`holonomy_hyperbola`) pins its square **exactly** — a
generic-field identity, no archimedean structure (§7c):

$$\Bigl(\frac{\mathrm{barEven}\,q}{\mathrm{barOdd}\,q}\Bigr)^{2} \;=\; 1 + \frac{4}{(\mathrm{barOdd}\,q)^{2}} \qquad(\texttt{sensitivity\_sq}).$$

Two `ℝ` corollaries make this the anchor-smoothness bound:

- `barOdd_sq_le_of_amplification` — amplification `ρ ≥ N` **forces**
  `(barOdd q)² ≤ 4/(N²−1)`: a large deformation-magnitude amplification requires
  `q` near the **compact / root-of-unity locus** `barOdd = 0` (`q = ±1`).
- `amplification_le_of_barOdd_sq_ge` — contrapositive: away from that locus
  (`barOdd² ≥ δ`), `ρ² ≤ 1 + 4/δ`.

## The true anchor comparison (measured)

The 2026-07-11 pole–cusp audit's "`(√3/2)|u|²` magnitude match ~4 %" matched
`|S(muon)|` with `|u| = barOdd(√q₀)` and `|S(proton)|` with `|u| = barOdd(q₀)` —
i.e. it substituted a **different coordinate at the same anchor** (`√q` vs `q`),
which is fit-adjacent and does **not** measure the anchor swing. This probe holds
the coordinate **fixed** (`u = 2 log q₀`) and evaluates at **both committed
anchors** (muon `q₀` from the `q-pinning` witness; proton `q₀` from the committed
`qou-substrate` constant), `|Δq₀|/q₀ = 1.15×10⁻⁸` (11.5 ppb):

| quantity | value |
|---|---|
| `barOdd q₀` (both anchors, to 6 sf) | `0.209064` |
| `ρ_u = barEven/barOdd` (magnitude sensitivity) | `9.6178 = O(10)` |
| `sensitivity_sq` residual (probe↔Lean tie) | `~1×10⁻⁵⁹` |
| **deformation-magnitude swing `Δ(u²)/u²`** | **`2.21×10⁻⁷` (0.221 ppm)** |
| cross-check: A1 `ω`-home swing (C1) | `4.56 ppm` (same order) |
| `(c₃ swing 3.47 %)/(deformation swing)` | **`1.57×10⁵`** |
| required amplification `ρ_req = c₃swing/Δq₀` | `3.01×10⁶` |
| compact-locus bound `2/√(ρ_req²−1)` | `6.65×10⁻⁷` |
| actual `barOdd q₀` vs that bound | **5.50 orders too far** |

## Verdict — scope-(a) NEGATIVE, unifying the bound with #4283

The meridian-holonomy `q₀↦u` deformation **magnitude** channel is provably
anchor-smooth at the substrate: its `q`-sensitivity `ρ_u ≈ 9.6 = O(10)` (exact,
`= √(1 + 4/barOdd²)`), so the `S ∝ u²` channel swings only `0.221 ppm` across the
11.5 ppb anchor spacing — `1.57×10⁵×` too smooth for the 3.47 % `c₃` swing. To
reach the required amplification `ρ_req ≈ 3×10⁶` a magnitude channel would need
`|barOdd q₀| ≲ 6.6×10⁻⁷`, i.e. `q₀` within `~3×10⁻⁷` of `1`; the substrate is
`≈ 0.11` away — **5.5 orders too far from the compact locus.**

This is a **scope-(a)** negative (per AGENTS.md §"Before declaring refuted"): it
constrains the *magnitude* the deformation channel can contribute; it does **not**
structurally exclude the meridian deformation (whose *phase* channel remains the
open `conj:algebraic-geometric-dilog-equivalence`).

**Two things this adds to the corpus:**

1. **An exact generic-field sharpening of the #3639 smooth-boost negative.**
   #3639 estimated `dζ/dq₀ = 1/q₀ = O(1)` numerically for the boost rapidity
   `ζ = ln q₀`; this replaces that with the closed form `ρ² = 1 + 4/barOdd²` for
   the deformation *shape* `barOdd q` and gives the **exact criterion** for where
   a magnitude amplification could live (only near `barOdd = 0`), quantifying
   precisely how far the substrate is from it (5.5 orders).

2. **A unified bound across this route and #4283.** Both the in-block module
   maps (anchor-smooth, C1) *and* the holonomy-deformation magnitude (this bound)
   are anchor-smooth objects. Under the single exact criterion
   "amplification ⇒ proximity to the compact locus `barOdd = 0`", **every
   smooth/magnitude object is excluded as the sole seat** of the `c₃` swing. The
   swing lives only in the near-singular / **non-perturbative phase** `arg(u)` —
   consistent with #3818's ξ-frame phase law (no perturbative odd phase at the
   meridian: any genuine odd-channel monodromy phase must be non-perturbative,
   unreadable from κ̃ rungs at any order).

**Does NOT close `c₃`.** The phase channel is the open keystone. This bounds the
magnitude routes and localizes the residual to the non-perturbative phase; it
composes with #4283 as a joint bound rather than refuting the module-map program
(a module map that carries a non-perturbative-phase factor is not touched by
this).

## Anti-laundering

No `c_k` value produced; the deformation magnitude is *measured* against the
committed `c₃` swing, never fitted to it; nothing inverts `Q_β`/CODATA; nothing
wired; `c₃` stays a q₀-dependent near-match (SETTLED #1580). Base ring:
`sensitivity_sq` generic `Field R` (§7c-clean); the ordering corollaries over `ℝ`
(genuinely archimedean — they order magnitudes).

## Cross-references

- C1 (bar-odd = ι-odd off-diagonal, anchor-smooth): [`2026-07-25-5two-gk-bridge-attack.md`](2026-07-25-5two-gk-bridge-attack.md).
- #3639 smooth-boost negative: [`2026-07-12-c3-meridian-boost-smooth-negative.md`](2026-07-12-c3-meridian-boost-smooth-negative.md).
- NZ deformation gap / pole–cusp phase: [`2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md`](2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md), [`2026-07-11-qbeta-c3-barodd-pole-cusp-phase-tractability.md`](2026-07-11-qbeta-c3-barodd-pole-cusp-phase-tractability.md).
- Cusp-shape coordinates: [`CuspShapeBarParity.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/CuspShapeBarParity.lean); boost: [`meridian-holonomy-boost.md`](../../content/quantum-observable-universe/braids-and-knots/meridian-holonomy-boost.md).
- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md).

-- Ref: [manuscript] docs/coordination/1ppq-qbeta.md
