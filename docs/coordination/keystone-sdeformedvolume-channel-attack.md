# Coordination — attack on the SDeformedVolumeChannel keystone (post-#3773)

**Goal.** Reduce the open surface of `conj:binding-qbeta-complex-volume`'s
S-channel, landed in #3773 as the abstract §3b class
`QOU.QBeta.PhiBSArgumentIdentification.SDeformedVolumeChannel S` (fields:
`u : ℝ → ℂ`, `V : ℂ → ℂ`, `S_eq : ∀ q₀>1, S q₀ = (V (u q₀)).im`). The
docstring flags `V` (the figure-eight deformed complex volume
`𝔙(u)=Vol(u)+i·CS(u)`) as *"a theorem for 4₁ (Ohtsuki; Murakami–Yokota),
explicitly computable via Neumann–Zagier"* — yet it is carried as an
**abstract field**. Making `V` **concrete** turns the conjecture's open
surface from three unknowns (`u`, `V`, `S_eq`) into two (`u(q₀)`, `S_eq`).

## Existing corpus infra to BUILD ON (do not reinvent — corpus-grep 2026-07-26)

| File | What it gives |
|---|---|
| `QOU/Knot/CuspShapeBarParity.lean` | the **exact `𝔙 = Vol + i·CS` split**: 4₁ cusp shape `ω=e^{iπ/3}` (root of `Φ₆=z²−z+1`), bar-even `ω+ω⁻¹=1` (Vol side), bar-odd `ω−ω⁻¹=2ω−1`, `(bar-odd)²=−3` (CS/Im axis, trace field ℚ(√−3)) |
| `QOU/Knot/NeumannZagierParity.lean` | **`CVol(u)` is EVEN in `u`** (`CVol(u)=Vol(0)−(τ/4)u²+…`, no odd/`u³` rung; class `NeumannZagierEvenPotential`, `no_odd_rung` proved) |
| `QOU/Knot/FigureEightDeformedMeridianWinding.lean` | the deformed **log meridian holonomy** `meridian(a,k)=a−2πk·i` |
| `QOU/Knot/{FigureEightVolume,Clausen,ClausenValueBounds}.lean`, `QOU/Archimedean/BlochWignerUnitCircle.lean` | `Vol(4₁)=2Cl₂(π/3)≈2.0299` value + Bloch–Wigner on the unit circle |

## The two targets

- **T1 (qou-6s8k, formalize-first).** Assemble the explicit
  `V₄₁ : ℂ → ℂ`, `V₄₁(u) = Vol(u)+i·CS(u)`, from the pieces above (the
  Neumann–Zagier deformed potential of the figure-eight; `V₄₁(0)` matches the
  complete-structure value `2Cl₂(π/3)` on the Vol axis). Prove its
  complete-structure value + the `NeumannZagierParity` even-ness. Deliverable:
  a concrete `def V₄₁` that can instantiate `SDeformedVolumeChannel.V`,
  reducing the class to `{u, S_eq}`. Sorry-free or honest named residual.

- **T2 (qou-fook, probe).** With `V₄₁` explicit, test the channel identity
  `S = Im 𝔙(u(q₀))` numerically: can it reproduce the **sign-flipping**
  bar-odd leak `S(muon)≈+0.00968 > 0 > S(proton)≈−0.03946` under #3773's
  surviving `u(q₀)` constraint (one component crosses 0 linearly at `q*`, the
  other anchor-constant)? **Structural caveat (from `NeumannZagierParity`):**
  the classical `𝔙(u)` is even in `u`; the sign-flip must come from the
  *complex* meridian `u=a−2πk·i` (varying real part `a`), NOT from an odd
  geometric coefficient (the `u³` route is scope-(b) excluded). Classify the
  outcome honestly: `derived` / `structural-partial` / `numerical-coincidence`
  / `no-match` (scope-(a) vs (b)).

## Discipline

Formalize-first; anti-fit (`V₄₁` is the *literature* Neumann–Zagier function,
never a fitted form); anti-laundering (no instance of the keystone classes is
fabricated — making `V` concrete is not the same as proving `S_eq` or `u(q₀)`;
those stay open). If T2 shows `S=Im 𝔙` cannot sign-flip under the constraint,
that is an honest **scope-(b) refutation of the channel identity as stated**
(cite the invariant), a real result — record it, do not bury it.

Beans: milestone `qou-o93x`; T1 `qou-6s8k`; T2 `qou-fook`.

## Outcome (2026-07-26)

**T1 landed.** [`QOU/Knot/FigureEightComplexVolume.lean`](../../folio/quantum-observable-universe/lean/QOU/Knot/FigureEightComplexVolume.lean)
— concrete `V₄₁(u) = Vol(4₁) + i·(√3/4)·u²` (NZ leading form), lean-verify exit 0
sorry-free. `V₄₁_zero_re` (= 2·Cl₂(π/3), exact), `V₄₁_even`, `imV₄₁`
(`Im 𝔙₄₁ = (√3/4)(Re²u−Im²u)`), and the T2 invariants. Class open surface reduced
`{u,V,S_eq}` → `{u,S_eq}`; no instance fabricated.

**T2 verdict: structural-partial.** Probe
[`sdeformed_channel_signflip_probe.py`](../../computations/probes/sdeformed_channel_signflip_probe.py)
exit 0. The rigorous A-polynomial cusp modulus `τ = −i√3` (purely imaginary) ⇒
`a₂` purely imaginary ⇒ `Im 𝔙₄₁ = κ(Re²u−Im²u)` vanishing on the **diagonals**
`|Re u|=|Im u|`, **not** the axes — correcting the heuristic `√3·Re·Im` form the
#3773 F3 survivor was built on. Against the corrected form **F3 is refuted**
(scope-(b): `S = κ((k·d)²−c₀²)` is even in `d`, same sign at both anchors). The
channel itself is **not** excluded but requires `u(q₀)` to **cross the diagonal**
between anchors (`Re²u−Im²u`: +ve muon, −ve proton). `u(q₀)` stays open. Full
record: [`docs/audits/2026-07-26-sdeformed-channel-signflip.md`](../audits/2026-07-26-sdeformed-channel-signflip.md).

## Geometric boost readout of u(q₀) (2026-07-26, branch `claude/udeform-geometric-boost-2026-07-26`, bean qou-zuk4)

Derive-then-check on the open `u(q₀)` (probe
[`qbeta_geometric_boost_udeform_probe.py`](../../computations/qbeta/qbeta_geometric_boost_udeform_probe.py),
50 dps, exit 0). **Derive** (not fitted): `braids-and-knots/meridian-holonomy-boost.md`
(proved sorry-free) — the cusp-torus meridian holonomy IS multiplication by q₀, a
hyperbolic **boost of rapidity `ln q₀`** at real q₀>1, a compact **spin** only at
`|q|=1`. So the geometric log meridian holonomy is `u = ln q₀` (real) + a spin part.
**Check** under the corrected `Im 𝔙₄₁ = (√3/4)(Re²u−Im²u)` (#4372):

- **[G1] muon sign + ballpark ✓.** Real boost `u=ln q₀` ⇒ `Im 𝔙₄₁ = (√3/4)(ln q₀)²
  = +0.004714`, same sign as `S(muon)=+0.009683` and within ~0.49× — a genuine
  (unfitted) geometry-side hit on the muon anchor. **This overturns the "real m ⇒
  Im 𝔙 = 0, silent" reading of the third wrong-form probe**
  (`qbeta_c3_geometry_derived_argument_probe.py`, which used `Im ∝ √3·Re·Im`; a real
  `u` is silent only under that WRONG form).
- **[G2] refuted as the FULL map (scope-(a)).** The two canonical anchor q₀'s differ
  by `Δ(ln q₀) ≈ 1.2e-8`, so `Im 𝔙₄₁` is nearly CONSTANT across anchors
  (`Δ Im 𝔙₄₁ ≈ 1e-9`) — it **cannot** produce `S(proton)=−0.0395` (opposite sign)
  or the `S(muon)/S(proton)` gap. A purely-real boost is not the map.
- **[G3] geometric meaning of the diagonal-crossing (the open piece).** To reach
  `S(proton)<0` needs `Im²u > Re²u` at the proton side — i.e. `u(q₀)` must cross the
  diagonal `|Re u|=|Im u|`. Geometrically that is the meridian holonomy's
  **boost→spin transition** (`meridian-holonomy-boost.md`: real q₀ boost vs `|q|=1`
  spin). So the #4372 diagonal-crossing constraint = the boost→spin transition; the
  open `u(q₀)` is the hypersensitive **spin/imaginary part** switching on toward the
  proton anchor (slope `k≈2.2e6`, the #3773 hypersensitivity witness). Its geometric
  derivation is the remaining open frontier — **not fitted here**.

Net: the *real-boost* part of `u(q₀)` is geometrically fixed (`= ln q₀`,
muon-consistent); the *spin* part (which supplies the sign flip via diagonal-crossing)
is open. Third wrong-form probe flagged for the same `(√3/4)(Re²−Im²)` correction as
#4372's two.
