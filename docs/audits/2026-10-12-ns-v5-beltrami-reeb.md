# NS vector 5: the Reeb field of `UT(Σ₄)` is an explicit regular NS flow (bean `qou-byzu`)

**Date:** 2026-10-12 (finished 2026-10-13). **Branch:** `ns-v5`.
**Lean:** [`QOU/FluidDynamics/BeltramiSteadyEuler.lean`](../../folio/quantum-observable-universe/lean/QOU/FluidDynamics/BeltramiSteadyEuler.lean). It is sorry-free and uses no `axiom` and no `native_decide`. The verification line is in §6.
**Parent audit:** [`2026-10-12-ns-rescue-reformulations.md`](2026-10-12-ns-rescue-reformulations.md) §5. **This audit corrects one constant there and adds a convention dependence (§3).**

Tags: **[L]** proved in Lean in this PR. **[S]** standard, not formalized here. **[D]** derived here by hand. **[NH]** literature that is not held in `library/`.

---

## 1. Verdict

1. **The finding.**
   - On the homogeneous model `M = Γ\PSL₂(ℝ) = UT(Σ₄)`, the fibre-rotation (Reeb) field `V` is a unit-speed Killing field and a Beltrami field.
   - So it gives an eternal steady Euler flow.
   - It also gives an explicit, globally smooth NS solution for every viscosity.
2. **The correction.** *Which* NS solution it gives depends on the viscous-operator convention.
   - Under the physically standard deformation-tensor convention, `V` is a **steady** NS solution with no decay.
   - The parent audit's `e^{−νt}V` is correct only for the Hodge convention with `s = 1`.
3. **Scope.**
   - **Shown:** one regular solution, and its rescalings, on one fixed Riemannian 3-manifold.
   - **Not shown:** anything about generic data. Global regularity on `M` stays exactly as open as on `T³`.
   - The result runs **against** the retracted NS-singular claim: the model's own flow is regular.

## 2. The model and the left-invariant data

- **[S]** Let `Σ₄ = Γ\ℍ` be Bring's surface with its hyperbolic metric (`K = −1`, genus 4, `χ = −6`), with `Γ` torsion-free Fuchsian. Then `UT(Σ₄) ≅ Γ\PSL₂(ℝ)`.
- **[S]** `Γ` acts on the left. Left-invariant vector fields, forms and metrics on `PSL₂(ℝ)` therefore descend to `M`, and every computation below on left-invariant data is a computation on `M`.

**Basis [L, `sl2_brackets`].** Take `X = H/2`, `Y = (E+F)/2`, `V = (E−F)/2` in `sl₂(ℝ)`. Then

  `[X,Y] = V`,  `[X,V] = Y`,  `[Y,V] = −X`.

- `X` generates the geodesic flow and `V` the unit-speed fibre rotation: `exp(θV)` rotates unit tangent vectors by angle `θ`.
- `toMat_br` [L] proves that the coefficient bracket `br` used in Part C is the matrix commutator.

**Metric.** `g_s = diag(1, 1, s²)` in `(X, Y, V)`, with `s > 0`.
- `s = 1` is the Sasaki metric of the hyperbolic surface.
- Every `Ad(SO(2))`-invariant left-invariant metric is of this form up to an overall scale.
- **The choice of `s` is a choice.** No quantity is compared to data, so no fitting is involved. But the corpus does not fix `s`.
- The contact form `θ^V` and its Reeb field `V` do not depend on `s`:
  - `θ^V ∧ dθ^V = −θ^V∧θ^X∧θ^Y ≠ 0`;
  - `θ^V(V) = 1`;
  - `i_V dθ^V = 0`.

**Identification with the corpus [A, inherited].** The parent audit identifies the model's Reeb field with `V` via the cone-link Boothby–Wang form. That identification is the parent's [D]/[A] step and is not re-derived here. Everything below is about `V` on `(M, g_s)`.

## 3. The computations

All values are for left-invariant fields under the Koszul connection of `g_s`. In Lean, `nab` is checked torsion-free (`nab_torsion_free`) and metric (`nab_metric`), so it is the Levi-Civita connection on left-invariant fields. Its closed form is `nab_eq`, in which the `/s²` cancels. Every value in this table was also re-derived independently in sympy before it was proved.

| quantity | value | Lean |
|---|---|---|
| `ad_V` skew for `g_s` ⇒ `V` Killing ⇒ `div V = 0` | yes, for every `s` | `V_killing` |
| non-vacuity: `ad_X` never skew (defect `1 + s²`), so `X` is not Killing | yes | `X_not_killing` |
| `∇_V V` | `0` | `nab_VV` |
| `curl V`, with `(curl V)♭ = ⋆dV♭` | `−s V` | `curl_V` |
| `curl curl V` (= `Δ_H V`, since `div V = 0`) | `s² V` | `curl_curl_V` |
| `Ric V` | `(s²/2) V` | `ric_V` |
| `Ric X` (Milnor cross-check `2μ₂μ₃`) | `−(1 + s²/2) X` | `ric_X` |
| rough Laplacian `∇*∇ V` | `(s²/2) V` | `rough_V` |
| Weitzenböck on `V`: `∇*∇V + Ric V = Δ_H V` | holds | `weitzenbock_V` |
| deformation operator `(Δ_H − 2Ric) V` | `0` | `deformation_V` |

The Weitzenböck row is a consistency check between two independent computations: Hodge via `curl`, and rough plus Ricci via the connection. It would fail if either were mis-defined.

**Which Laplacian NS uses [S/NH].** On a Riemannian manifold, incompressible NS reads `∂ₜu + ∇_u u + ∇p = ν L u` with `div u = 0`. Three conventions for `L` circulate:

1. **Deformation (Ebin–Marsden 1970; Taylor, PDE III; Chan–Czubak–Disconzi, who argue it is the physically correct one) [NH].** `L u = 2 div Def u`. For divergence-free `u`, `L = −(Δ_H − 2Ric) = −∇*∇ + Ric`.
2. **Hodge.** `L = −Δ_H`.
3. **Bochner (rough).** `L = −∇*∇`.

They agree on flat `T³` (`Ric = 0`) and differ on `M`.

**Explicit solution [D, from the L rows].** Write `u(t) = a(t) V` with `p` constant.
- `∇_u u = a² ∇_V V = 0` and `div u = 0`. So NS reduces to `a′ V = ν a L V`.
- `L V = −κ V` with:

| convention | `κ` | solution |
|---|---|---|
| deformation | `0` | **`u ≡ V` steady**, for every `ν` |
| Hodge | `s²` | `u = e^{−ν s² t} V` |
| Bochner | `s²/2` | `u = e^{−ν s² t / 2} V` |

**Physical reading of the deformation row.**
- `V` is Killing, i.e. an infinitesimal rigid motion.
- A rigid motion has `Def V = 0`, so the dissipation `2ν∫|Def u|²` vanishes. This is the curved analogue of solid-body rotation.
- The kinetic energy `½∫|V|² = s² vol(M)/2` is conserved.
- The helicity `∫⟨V, curl V⟩ = −s³ vol(M) ≠ 0` is conserved too.

**Correction to the parent audit §5.**
- It wrote `Δ_H V = curl² V = V` and `e^{−νt}V`. That is right only for Hodge with `s = 1`.
- It said "only the decay rate changes" across conventions. That is true, and under the standard convention the rate is **zero**.
- The parent's `Ric = a(·) + bβ²` with `Ric(V) = bV` is confirmed, with `b = s²/2`.

## 4. The flat counterpart, fully checkable (Lean Parts A and B)

The manifold statements above rest on [S] steps: descent to `Γ\PSL₂`, and the identification of the manifold operators with the Lie-algebra formulas. On flat space nothing needs to be imported, so the same mechanism is proved end to end with Mathlib `deriv`:

- **`lamb₁₂₃` [L].** Lamb identity `(u·∇)u = ∇(|u|²/2) − u × curl u`, componentwise, for any field with differentiable coordinate slices.
- **`beltrami_steady_euler` [L].** If `curl u = λu` and `div u = 0`, then `u` solves steady Euler with `p = −|u|²/2`.
- **`beltrami_eigen_ns` [L].** If also `Δu = −μu`, then `U(t) = e^{−νμt}u` with `P(t) = −e^{−2νμt}|u|²/2` is an exact incompressible NS solution at every point of `ℝ⁴`.
  - The NS residual is stated through `deriv` in `t` and the explicit flat Laplacian.
  - It is not an assumed equation.
- **ABC [L].** `u = (A sin z + C cos y, B sin x + A cos z, C sin y + B cos x)` satisfies all of:
  - `curl u = u` (`abc_beltrami`, every derivative computed);
  - `div u = 0`;
  - `Δu = −u` (`abc_lap`);
  - `2π`-periodicity in each variable (`abc_periodic`);
  - non-vacuity: `u ≢ 0` (`abc_nonzero`).
- **Conclusion: `abc_ns_exact` [L].** `e^{−νt}u_ABC` solves NS on `T³` exactly, globally and smoothly, for every `ν, A, B, C`.

## 5. Draft proposition for the owner (NOT added as a content block)

> **Proposition (regular Reeb flow on the Descartes 3-manifold).** Let `Σ₄ = Γ\ℍ` be Bring's surface with its hyperbolic metric. Let `M = UT(Σ₄) = Γ\PSL₂(ℝ)`, carrying the left-invariant metric `g_s = diag(1,1,s²)` in the frame `(X, Y, V)` of §2, for any `s > 0`. Let `V` be the fibre-rotation field, i.e. the Reeb field of the connection form `θ^V`. Then:
>
> (i) `V` is a unit-speed (for `s = 1`) Killing field with `curl V = −sV` and `∇_V V = 0`. Hence `V` is a steady solution of the Euler equations with constant pressure.
>
> (ii) For every `ν > 0`, `u(t) = V` (deformation convention), `u(t) = e^{−νs²t}V` (Hodge), or `u(t) = e^{−νs²t/2}V` (Bochner) is a smooth solution of incompressible Navier–Stokes on `M × [0, ∞)` with constant pressure.
>
> **Hypotheses.**
> - The hyperbolic metric on `Σ₄`.
> - The chosen invariant metric `g_s`.
> - Unforced NS.
> - The identification of the model's Reeb field with `V`. This is inherited from the cone-link audit and is not proved.
>
> **What it does not say.**
> - Nothing about solutions with other initial data.
> - Nothing about global regularity on `M`, which is open on `M` exactly as on `T³ = UT(T²)`.
> - Nothing about forcing.
> - Topology (Euler number `−6`, Kummer class `−6 mod n`) is compatible with this regular solution. So no topological invariant of the bundle can force every solution on `M` to be singular. This is scope (b), and the invariant is this explicit solution.
> - It contradicts the retracted claim that the model's natural flow is NS-singular. It does not settle whether *some* data blows up.
>
> **Lean.** Parts A and B are the flat proof. Part C is the left-invariant algebra. The descent to `Γ\PSL₂(ℝ)` is [S] and not formalized.

Cost: one block plus a Lean link. Risk: the statement points in the regularity direction, against the chapter's earlier narrative. Default if the owner does nothing: nothing changes. This audit and the Lean file stand as records.

## 6. Verification

- **Method:** `lean --root=/ -DautoImplicit=false -s 65536` against the private olean tree `olean-v5`. **No `lake build`.**
- **Result:** exit 0 on the committed file. 0 `sorry`, 0 `axiom`, 0 `native_decide`, 0 `: True`.
- **Axioms.** `#print axioms` was run on a copy for 18 key declarations:
  - Part A: `beltrami_steady_euler`, `beltrami_eigen_ns`.
  - Part B: `abc_ns_exact`, `abc_periodic`, `abc_nonzero`.
  - Part C: `sl2_brackets`, `toMat_br`, `nab_torsion_free`, `nab_metric`, `V_killing`, `X_not_killing`, `nab_VV`, `curl_V`, `ric_V`, `ric_X`, `rough_V`, `weitzenbock_V`, `deformation_V`.
  - Every one depends only on `[propext, Classical.choice, Quot.sound]`.
- **Not done:** no content block was edited. The library sweep was not run. The file is new and has no consumers.
- **Base ring (§7c).** Parts A and B use `ℝ` because they are archimedean: `sin`, `exp`, `deriv`. Part C's algebra is over `ℝ` because `sl₂(ℝ)` and `g_s` are real objects. It could be generalised to a field, but that was not done here.

## 7. Literature (all [NH] unless noted)

- **Etnyre–Ghrist**, *Contact topology and hydrodynamics I*, Nonlinearity 13 (2000). Non-vanishing rotational Beltrami fields are reparametrised Reeb fields, and conversely. §3 is an instance.
- **Arnold–Khesin**, *Topological Methods in Hydrodynamics*. Steady Euler, Beltrami fields and helicity. `khesin2003` (a survey) is held. The book is not.
- **Ebin–Marsden** (Ann. Math. 1970), **M. Taylor** *PDE III*, **Chan–Czubak–Disconzi** (*The formulation of the Navier–Stokes equations on Riemannian manifolds*, J. Geom. Phys. 2017). All discuss the deformation-tensor convention. The three-convention table above is the hand derivation here and was **not** checked against these texts.
