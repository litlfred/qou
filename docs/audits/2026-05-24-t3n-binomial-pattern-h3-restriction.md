# T(3, n) binomial pattern — restriction to H_2(q)

**Date:** 2026-05-24
**Trigger:** Deferred item #3 from PR #1193's pending list — "Generalization to T(p,q) for p>2 (H_3(q) analog of binomial pattern)"
**Status:** Structural finding — negative-for-extension, positive-for-mechanism.

## §1. The question

PR [#1165](https://github.com/litlfred/qou/pull/1165) PROVED the bar-symmetric Markov trace of the T(2, 2m) torus link family has the closed form

$$P_m(h) \;=\; \frac{\cosh((2m+1)\eta)}{2\cosh\eta} \;=\; \sum_{j=0}^m \binom{m+j}{2j}\frac{h^{2j}}{2}$$

via the Fibonacci-polynomial / Chebyshev-of-second-kind identity (Graham–Knuth–Patashnik *Concrete Mathematics* §6.6; Riordan; Vajda).  PR [#1185](https://github.com/litlfred/qou/pull/1185) Lean-encoded the four hyperbolic identities (P_m² − Q_m² = 1/[2]_q², Q_m/P_m = tanh, etc.).

The obvious next question: **does the binomial pattern $c_{2j}(T(2,2m)) = \binom{m+j}{2j}/2$ extend to the T(3, n) torus knot family?**  This matters because T(3, 5) is a strong-force particle in the framework's particle map (per [`2026-05-24-sm-particle-categorical-map-rt-route.md`](2026-05-24-sm-particle-categorical-map-rt-route.md)).

## §2. The probe

[`computations/probes/t3n_binomial_pattern_probe.py`](../../computations/probes/t3n_binomial_pattern_probe.py) builds the Hoefsmit (2,1) standard rep of H_3(q) symbolically:

$$\sigma_0 = \begin{pmatrix} q & 1 \\ 0 & -q^{-1}\end{pmatrix}, \quad \sigma_1 = \begin{pmatrix} -q^{-1} & 0 \\ 1 & q\end{pmatrix}$$

(matching [`HeckeH3.lean §1`](../../content/quantum-observable-universe/lean/QOU/Archimedean/HeckeH3.lean)), verifies Hecke + braid relations, and computes

$$\chi^{(2,1)}\bigl((\sigma_0\sigma_1)^n\bigr) \;=\; \operatorname{tr}\bigl(M^n\bigr) \quad\text{where}\quad M := \sigma_0\sigma_1.$$

## §3. The finding

**Sympy-verified, sigma-symbolic:** $M^3 = I$ exactly in (2,1) of H_3(q), for all q.

The eigenvalues of $M = \sigma_0\sigma_1$ in the (2,1) rep are

$$\lambda_\pm \;=\; -\tfrac{1}{2} \pm \tfrac{i\sqrt{3}}{2} \;=\; e^{\pm 2\pi i / 3}$$

— the primitive cube roots of unity, **independent of q**.  Consequently

$$\chi^{(2,1)}\bigl((\sigma_0\sigma_1)^n\bigr) \;=\; \lambda_+^n + \lambda_-^n \;=\; 2\cos(2\pi n / 3) \;\in\; \{-1, -1, +2\}$$

cyclically with $n \bmod 3$.

| n | gcd(3,n) | χ^{(2,1)}((σ_0σ_1)^n) | knot/link |
|--:|--:|--:|---|
| 1 | 1 | −1 | knot |
| 2 | 1 | −1 | knot |
| 3 | 3 | +2 | 3-component link |
| 4 | 1 | −1 | knot |
| 5 | 1 | −1 | knot (**T(3,5) = strong-force**) |
| 6 | 3 | +2 | 3-component link |
| 7 | 1 | −1 | knot |
| 8 | 1 | −1 | knot |
| 9 | 3 | +2 | 3-component link |
| 10 | 1 | −1 | knot |

## §4. Interpretation

**Negative-for-extension.**  The Fibonacci/Chebyshev binomial pattern $c_{2j} = \binom{m+j}{2j}/2$ does NOT generalize to T(3, n) via the (2,1) channel of H_3(q) — there is no non-trivial h-polynomial in that channel to find.  Each $\chi^{(2,1)}$ is a degree-0 polynomial in h.

**Positive-for-mechanism.**  The reason is categorical: $\sigma_0\sigma_1$ is the 3-cycle generator of B_3, and its (2,1)-character is the character of the 3-cycle in the standard rep of S_3 — a purely combinatorial invariant (cube roots of unity).  **The H_3(q) Hecke deformation acts as identity on this character.**

This is consistent with — and orthogonal to — the H_2(q) finding: in H_2(q), $\sigma_1$ has eigenvalues $q$ and $-q^{-1}$ in its 2D standard rep (trivial + sign decomposition), and the trace $\sigma_1^k \mapsto q^k + (-q^{-1})^k$ deforms non-trivially.  In H_3(q), the element $\sigma_0\sigma_1$ has roots-of-unity eigenvalues in (2,1) — the q-deformation collapses out.

**Where the q-dependence of $J_{T(3,n)}(q)$ lives.**  The trivial and sign channels:

$$\chi^{(3)}\bigl((\sigma_0\sigma_1)^n\bigr) = q^{2n}, \qquad \chi^{(1,1,1)}\bigl((\sigma_0\sigma_1)^n\bigr) = q^{-2n}$$

Both are pure q-powers — no Fibonacci/Chebyshev richness.  So $J_{T(3,n)}(q)$ decomposes as

$$J_{T(3,n)}(q) \;=\; y_{(3)}\, q^{2n} \;+\; y_{(2,1)}\, \cdot 2\cos(2\pi n/3) \;+\; y_{(1,1,1)}\, q^{-2n},$$

where the (2,1) coefficient is the only $n$-dependent piece in the middle term and it's purely combinatorial.

## §5. Lean encoding

The structural identity is now type-level in [`HeckeH3.lean §3a`](../../content/quantum-observable-universe/lean/QOU/Archimedean/HeckeH3.lean) as

```lean
theorem stdRep3_M_cubed_eq_one :
    (stdRep3_gen0 * stdRep3_gen1) ^ 3 = (1 : TMatrix)
```

with the same `ext` + `fin_cases` + `simp [Matrix.mul_apply, …]` + `ring` proof pattern as `stdRep3_braid` (Jones 1987 reference).

## §6. Implications for the framework's RT-chain

1. **For T(3, 5) (strong-force particle)**: the Jones polynomial is fully determined by the trivial/sign q-powers and the Markov weights y_λ at H_3(q), which are computed in [`alpha_k_jones_markov_h3.py`](../../computations/alpha/alpha_k_jones_markov_h3.py).  No new h-polynomial structure to discover at the (2,1) channel.

2. **For higher-p T(p, q) generalization**: the same phenomenon will recur at H_p(q).  Each higher-dimensional irrep contributes roots-of-unity eigenvalue contributions to the trace of $(\sigma_0\cdots\sigma_{p-1})^n$, and the Hecke deformation acts as identity on those roots.  **The Fibonacci/Chebyshev richness is H_2(q)-specific.**

3. **For closed-form $J_{T(p,n)}(q)$**: the canonical route is the Jones 1987 formula via Burau-rep or HOMFLY/Skein recurrence — not via H_p(q) Wedderburn decomposition.

## §7. Cross-references

- PR [#1125](https://github.com/litlfred/qou/pull/1125) — sympy-verified the T(2, 2m) binomial pattern for 54 cells
- PR [#1165](https://github.com/litlfred/qou/pull/1165) — PROVED the binomial pattern in general via Fibonacci-polynomial / Chebyshev-of-second-kind identity
- PR [#1185](https://github.com/litlfred/qou/pull/1185) — Lean encoding of P_m, Q_m + Pythagorean identity
- PR [#1193](https://github.com/litlfred/qou/pull/1193) — Borromean H_3(q) (2,1) irrep derivation probe (Q_Borromean = 0)
- [`2026-05-24-sm-particle-categorical-map-rt-route.md`](2026-05-24-sm-particle-categorical-map-rt-route.md) — SM particle map (T(3, 5) = strong-force)
- [`alpha_k_jones_markov_h3.py`](../../computations/alpha/alpha_k_jones_markov_h3.py) — H_3 Jones-Markov weights
- [`HeckeH3.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/HeckeH3.lean) — Lean (2,1) standard rep + `stdRep3_M_cubed_eq_one`
