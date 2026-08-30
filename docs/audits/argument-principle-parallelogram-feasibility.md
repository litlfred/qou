# Assessment: Closability of the Argument Principle Parallelogram Bridge

## 1. Can the parallelogram version be DERIVED from the disc version?
**No, it cannot be derived directly from the disc version.**

*   **Mismatched Sums:** The disc version (`argument_principle`) computes the sum of orders for all zeros and poles inside the *disc*. If we place the fundamental parallelogram inside a large disc, the disc will contain additional lattice points (and hence extra zeros/poles of the elliptic function) outside the fundamental parallelogram but inside the disc. The divisor sum will thus be over the wrong set.
*   **Mismatched Boundaries (Loss of Cancellation):** The Liouville degree-zero theorem fundamentally relies on the contour integral of `f'/f` vanishing over the parallelogram boundary `∂P`. This happens because `logDeriv f` is elliptic (proved in `isElliptic_logDeriv`) and opposite edges cancel. A circle `C(c, R)` does not have opposite edges separated by a period, so the circle integral will not naturally cancel out.
*   **Missing Deformation Engine:** To relate the circle integral to the parallelogram integral, one would need to deform the circle contour onto the parallelogram contour. Because the region between them contains zeros and poles, deforming the contour requires the general homology version of Cauchy's residue theorem (multiply-connected domains). This general homology/winding engine is exactly the Mathlib gap that `ArgumentPrinciple.lean` intentionally bypassed by using a global factorization route.

## 2. Does Mathlib have rectangle/parallelogram contour integrals?
*   **Rectangles:** Mathlib does have contour integrals for axis-aligned rectangles and the Cauchy-Goursat theorem for rectangles (`integral_boundary_rect_eq_zero_of_differentiable_on_off_countable`, as mentioned in `ArgumentPrinciple.lean`).
*   **Parallelograms:** Mathlib does **not** have an API for contour integrals over arbitrary parallelograms (which are not axis-aligned unless the periods $\omega_1, \omega_2$ happen to be orthogonal). 
*   **Bare Pole Integrals:** Even if we specialized to rectangular lattices, Mathlib lacks the Cauchy integral for a simple pole over a rectangle (`∮_{∂Rect} (z-w)⁻¹ = 2πi`), which is the equivalent of `circleIntegral.integral_sub_inv_of_mem_ball` used in the disc version.

## 3. Feasibility Report
**Feasibility: Very Low / Blocked by Mathlib API gaps.**

The global Weierstrass factorization route successfully used for the disc (writing $f = P \cdot g$ over the closed region) could theoretically be applied to a parallelogram to avoid crosscut deformations. **However**, executing this would require building two major missing Mathlib bricks from scratch:
1.  **Cauchy-Goursat for parallelograms:** `parallelogramIntegral_eq_zero_of_differentiable`
2.  **Bare pole Cauchy integral for parallelograms:** `parallelogramIntegral_sub_inv_of_mem_interior = 2πi`

Because the disc version evaluates over the wrong region and boundary, and the factorization route for parallelograms requires building a new contour integration API, closing this bridge directly is currently not feasible without significant upstream Mathlib work.
