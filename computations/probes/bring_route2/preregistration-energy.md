# Pre-registration: an energy for closed geodesics on Bring's surface

Written 2026-10-10. No energy of any candidate had been computed when this was written. The owner asked for this on 2026-10-10: *"1 / 2 keep both as options"*. That means: fix an energy and a no-loop rule before computing (option 1), and keep the q-deformed matrix recipe open as an option (option 2).

Lengths from `preregistration.md` / `results.md` were already known when this was written, and they are listed in §0. Anything added after this file's first commit is marked **POST-HOC**. No Q_β, CODATA or mass number enters any computation, ordering or table.

## 0. Known before writing

| word | Bring loop | length |
|---|---|---|
| nuc9 | none (order-2 cone point) | — |
| class B: gluon_s0_s1, gluon_s0_s0 (= nuc11_interleaved) | none (order-5 cone point) | — |
| class A: gluon_s1_s0, gluon_s1_s1 | yes, same loop | 4.6031833095… |
| nuc11_gen_grouped | yes | 6.3676503714… |

So at most **two distinct loops** can be ranked: the class-A loop and the gen_grouped loop.

## 1. The energy (primary)

Let γ : [0, L) → X be the closed geodesic on X = Bring's surface. It is parametrised by arc length, with L the Bring length.

The energy is the surface analogue of the Möbius (O'Hara j = 2, p = 1) energy used in route 1:

  E(γ) = ∫₀ᴸ ∫₀ᴸ [ 1/d_X(γ(s), γ(t))² − 1/δ(s, t)² ] ds dt

- d_X is the intrinsic hyperbolic distance on X.
- δ(s, t) = min(|s − t|, L − |s − t|) is the distance along the loop.

Consequences fixed now:

- **The integrand is ≥ 0, so E ≥ 0.** Since d_X ≤ δ, each term is non-negative. It is exactly 0 wherever the shortest path between the two points runs along the loop itself.
- **A self-intersecting or non-primitive loop has E = +∞.** At a transverse crossing the integrand behaves like 1/(u² + v²), whose integral diverges. A loop that retraces itself has d_X = 0 at distinct parameters. In either case the loop is reported as **E = +∞**, and no number is quoted for it.
- **Computing d_X.** d_X(x, y) = min over h ∈ Γ_B of d_H(x̃, h ỹ), where x̃ and ỹ are lifts to the hyperbolic plane and Γ_B is the kernel of Δ(2,4,5) → S₅ (π₁ of Bring). The minimum is taken over all h with d_H(m, h m) ≤ 1.5·L + slack, where m is the midpoint of the lifted segment. This bound is proved in the probe's docstring.

## 2. Secondary kernel (robustness only, never used to rank)

The secondary energy, E_sinh, uses the same formula with 1/d² replaced by 1/(2 sinh(d/2))², for both d_X and δ. It is the hyperbolic chord kernel. **The ranking is read from E alone.** E_sinh is reported only to show whether the order survives a change of kernel. If the two kernels give opposite orders, the result is reported as **kernel-dependent, no ranking**.

## 3. Rule for words with no loop (fixed now)

Words whose image is a rotation (nuc9 and class B) get **no energy**: E is undefined, not 0 and not +∞. Route 2 ranks only the words that have a loop.

Consequence, stated before computing: **route 2 cannot rank the currently scored word** (gluon_s0_s0 = nuc11_interleaved), nor nuc9. The most it can say is how class A compares with gen_grouped.

Alternatives were considered and **not adopted**: cone point = 0 (the cone word wins automatically) and cone point = +∞ (the cone word loses automatically). Each decides the outcome by convention, not by computation. Adopting either is the owner's call and would be POST-HOC.

## 4. Matrix recipes (both kept as options, as the owner asked)

- **(R-classical), computed here.** B₃ → SL(2,ℤ) at Burau t = −1, as in `preregistration.md`.
- **(R-q), registered, not computed.** The reduced Burau representation at t = q₀ (the proton pin). Its image has determinant ≠ 1 and is not a discrete group, so it does not fold onto Bring's surface, and §1 cannot be applied as written. Using it requires a further definition (for example, translation length in PSL(2,ℝ) after normalising the determinant), which must itself be pre-registered before it is computed. Not done here.

## 5. Checks (pre-registered)

1. **Conjugate pair.** gluon_s1_s0 and gluon_s1_s1 must give the same E (it is the same loop), computed independently from each word.
2. **Kernel set.** The lifted group must contain the loop's own translation g^r, with displacement L. Any element preserving the axis must translate by a multiple of L/k; if k > 1 occurs, the loop is non-primitive (§1).
3. **Quadrature.** E is evaluated by the periodic trapezoid rule on N × N grids with N = 120, 240, 480. The figure reported is the N = 480 value. **Digits are quoted only where the N = 240 and N = 480 values agree.**
4. **Arithmetic.** mpmath mpf throughout (no float64). Enumeration and the grid run at 30 dps. The quadrature error dominates, and its estimate is reported.

## 6. Not claimed

- **This is not the 3D Möbius energy of route 1.** A route-1 link has 2 components, while the Bring loop is a single curve (the γγ core collapses and the closure's components are not tracked). No numerical comparison with route 1 is made.
- **A lower E does not by itself select a word.** It ranks two loops. What the ranking means for the scored element is stated in §3 and remains the owner's call.
