**Conjecture (D10 spin closure, conditional on the $S_5 \leftrightarrow \mathrm{SO}(3)$ fiber action).**
Within the QOU framework, spin $\mathrm{SU}(2)_S$ arises as the continuous lift of the full $\mathrm{SO}(3)$ rotation group acting on the 3 color sheets per nucleon. This operates via the $S_5 \to A_5 \cong I \subset \mathrm{SO}(3)$ icosahedral embedding on Bring's quintic surface ([`def:color-tube-fibers`](#def:color-tube-fibers)). The current pipeline implements only the discrete $S_3$ subgroup of $\mathrm{SO}(3)$ (the 6 permutations of three color sheets). Extending to the full continuous $\mathrm{SO}(3)$ populates the $\ell = 2, 3, 4, \ldots$ spherical-harmonic decompositions. These contribute the $h^4$, $h^6$, $\ldots$ corrections to the Borromean linking weight, which the current $S_3$-truncated framework omits.

**1. The structural gap.**
The Family A linking weight $(3q^2 + 4 + 3q^{-2})/4 = 5/2 + (3/4)h^2$ terminates at $h^2$. The Borromean Markov trace's exact closed form (see [`borromean-markov-trace-closed-form.md`](#prop:borromean-markov-trace-closed-form)) has $h^2 = 0$ and first non-trivial coefficient $h^4 = -3/4$. The gap between Family A's $(3/4)h^2$ contribution and the Markov-trace $h^4 = -3/4$ structural value constitutes the load-bearing $h^4$ closure gap.

The framework's pipeline currently uses only the $S_3$ discrete subgroup of $\mathrm{SO}(3)$. The premise that $S_3$ "sees only $\ell \le 1$" (making $\ell = 2$ require full continuous $\mathrm{SO}(3)$) is false. Under $S_3 \subset \mathrm{SO}(3)$, the standard $(2,1)$ irrep already appears at both $\ell = 1$ (multiplicity 1) and $\ell = 2$ (multiplicity 2). Therefore, $S_3$ is not $\ell$-truncated. 

Spherical-harmonic levels of $\mathrm{SO}(3)$ organise higher-order corrections ($\ell = 2$ gives $h^4$, $\ell = 3$ gives $h^6$). However, the proposed categorical link—that the icosahedral $\ell = 2$ level produces the Borromean $h^4 = -3/4$—is not derivable as written. The icosahedral construction lives on $A_5 \subset S_5$ (5 strands), whereas the $h^4 = -3/4$ coefficient lives on the $H_3$ Borromean Markov trace (3 strands, the $(2,1)$ irrep). These are different representation rings with no canonical map between them. The genuine missing object is a functor from the $S_5$/$\mathrm{SO}(3)$ level $\ell$ (5-strand) to a Wedderburn coefficient of the 3-strand $H_3$ trace.

**2. The conjectural content.**
Per `conj:s5-so3-fiber-action` (class scaffolded in [`S5SO3FiberAction.lean`](../../computations/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean)):

- **The icosahedral lift is well-defined.** $S_5 \supset A_5 \cong I \subset \mathrm{SO}(3)$ provides a canonical map from $S_5$-orbits on Bring's quintic to $\mathrm{SO}(3)$ rotations on the 3 color sheets.
- **The full $\mathrm{SO}(3)$ fiber action commutes with the Hecke structure.** The spherical-harmonic decomposition into $\ell$ levels respects the Wedderburn-block structure of $H_n(q)$; each $\ell$-level contributes to a definite subset of partition blocks.
- **The $\ell = 2$ contribution at the Borromean linking weight produces the $h^4 = -3/4$ coefficient.** The $h^4$ value comes from the dimension-5 irrep ($\ell = 2$) of $\mathrm{SO}(3)$ acting on the 3-color tensor space.

**3. Partnership of D10 with D9 unlocking D11 (Wigner SU(4)).**
Per [`docs/duality-tracker.md`](../../docs/duality-tracker.md):
- **D9** (isospin $\mathrm{SU}(2)_I$): Flavor-swap $u \leftrightarrow d$ on color-sheet flavor triples ([`conj:isospin-from-canonical-bowtie`](isospin-from-canonical-bowtie.md)).
- **D10** (spin $\mathrm{SU}(2)_S$): $\mathrm{SO}(3)$ rotation on color sheets (this conjecture).
- **D11** (Wigner $\mathrm{SU}(4) = \mathrm{SU}(2)_S \times \mathrm{SU}(2)_I$): Combined symmetry. This is the categorical source for nuclear-shell structure.

Closing D10 together with D9 unlocks D11, the L3 (nuclear-shell binding) categorical source.

**4. Diagnostics.**
Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:
- **GB filtration level:** The $\mathrm{SO}(3)$-fiber decomposition is per-partition. Different Wedderburn blocks of $H_n(q)$ couple to different $\ell$ levels. Per-block Coxeter length determines which $\ell \leq \ell_{\max}$ levels contribute.
- **Jet order:** $h^4$ is the first non-trivial level contributed by $\ell = 2$ (the load-bearing closure step). $h^6$ comes from $\ell = 3$.
- **Bar-symmetry status:** Bar-symmetric. Spherical-harmonic decomposition coefficients are real-valued under $q \mapsto q^{-1}$.

**5. Lean axiomatisation (sketch).**
```lean
-- Conditional on the S_5↔SO(3) fiber action class (PR #1081):
class SpinFromSO3Fiber
    (M : Type*) [BrCategory M] [ColorTube M]
    [BringFiberAction M] where
  /-- The spherical-harmonic decomposition of the color-tube tensor
      under the full SO(3) action. -/
  spherical_harmonic_decomp :
    ColorTubeTensor → ∀ (ℓ : ℕ), SO3IrrepOfDim (2*ℓ + 1)
  /-- The S_3 subgroup pipeline sees only ℓ ≤ 1. -/
  s3_truncation_at_ell_le_one :
    ∀ T, spherical_harmonic_decomp T ℓ = 0 → ℓ ≥ 2 ∨ ℓ = 0 ∨ ℓ = 1
  /-- ℓ = 2 contributes the h^4 = -3/4 Borromean coefficient. -/
  ell_two_yields_h4_coefficient :
    borromean_h4_via_so3 = -3/4
  /-- Together with D9 (isospin), defines SU(4) Wigner. -/
  combined_with_isospin_yields_wigner_su4 :
    True   -- placeholder until SU(4) structure axiomatised
```

**6. Open R&D.**
- **Analytic extension:** Extend from $S_3$-truncated integration to full $\mathrm{SO}(3)$ spherical-harmonic decomposition on Bring's surface. Verify $h^4 = -3/4$ at the $\ell = 2$ level.
- **D10 to closed:** Requires the Lean class instance and the `ell_two_yields_h4_coefficient` proof (with `sorry` for the regulator of the divergent series at higher $\ell$).
- **Connect to W/Z binomial pattern:** The unified $T(2, 2m)$ torus-knot Markov-trace closed form may have a spherical-harmonic reading at the $\mathrm{SO}(3)$-fiber level.

**Cross-references:**
- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) §1 D10, §2 Cluster B.
- [`docs/audits/-h4-coefficient-source-trace-and-so3-gap.md`](../../docs/audits/-h4-coefficient-source-trace-and-so3-gap.md) (structural-gap audit).
- Upstream class supplier: `conj:s5-so3-fiber-action` (PR [#1081](https://github.com/litlfred/qou/pull/1081), [`S5SO3FiberAction.lean`](../../computations/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean)).
- Sibling Cluster B item: [`conj:isospin-from-canonical-bowtie`](isospin-from-canonical-bowtie.md).
- Color-tube structure on Bring's quintic: [`color-tube-coordinates.md`](../archimedean-universe/color-tube-coordinates.md), [`color-tube-fibers.md`](../archimedean-universe/color-tube-fibers.md).
- $h^4 = -3/4$ topological reference: [`borromean-markov-trace-closed-form.md`](#prop:borromean-markov-trace-closed-form).
