# Δ_λ Phase 5 — α-derivation research progress

**Date:** 2026-05-19 (evening)
**Branch:** `claude/update-deprecated-scripts-catalog-jvbyM` ([PR #819](https://github.com/litlfred/qou/pull/819))
**Context:** Phase 4 identified $\lvert\Delta_\lambda^*(K)\rvert \approx (\mathrm{Vol}_{\mathrm{hyp}}(K) / [8]_q) \cdot [3]_q^{2(Z-1)} \cdot (q^{1/2}+q^{-1/2})^{4N}$ with the per-Z factor $\alpha = [3]_q^2$ having a 2.17% residual. Phase 5 aims to *derive* $\alpha$ from first principles, eliminating the residual.

## Hypothesis tested

> The Z-step factor $\alpha$ in the Phase 4 closure equals the Markov trace of the proton's intra-nucleon braid in $H_3$, modulo a known categorical normalisation.

The natural test: compute $\mathrm{tr}_M(\beta_p)$ at $q_0$, where $\beta_p$ is the proton braid `[1, -2, 1, -2, 1, -2, 1, 1, 2, 1, 1]` (length 11, $H_3$).

## Numerical results (this session)

| Quantity | Value at $q_0$ |
|---|---|
| $\mathrm{tr}_M(\beta_p)$ (recursive Markov, full word) | 0.6358 |
| $\mathrm{tr}_M(\beta_n)$ (neutron, identical except $\sigma_2 \to \sigma_2^{-1}$ at one position) | 0.3741 |
| $\alpha_{\mathrm{empirical}}$ (Phase 4 fit) | 9.469 |
| $[3]_q^2$ (Phase 4 categorical candidate) | 9.264 |
| $(q^{1/2}+q^{-1/2})^4$ (per-N factor, for comparison) | 16.087 |

**Direct match** of $\alpha$ to any single $\mathrm{tr}_M$ candidate (raw, squared, with $z$-multiplier, etc.) **fails** — none come within 5% of $\alpha = 9.469$. The best $\mathrm{tr}_M$-based candidate is $\mathrm{tr}_M(p) \cdot [3]_q = 1.94$, off by 79%.

## Per-partition decomposition of proton braid

Computed via `hecke_characters.chi_lambda_braid` at $H_3$, $q_0$:

| $\lambda$ | $\dim_q V_\lambda$ | $\chi_\lambda(\beta_p)$ | sign / channel |
|---|---|---|---|
| $(3)$ — symmetric | 1.000 | **+1.685** | dominant positive |
| $(2,1)$ — standard | 2.011 | −0.180 | mixed |
| $(1,1,1)$ — sign | 1.000 | −0.594 | antisymmetric |

The proton's $(3)$-channel character is large and positive — consistent with the "spin-1 baryon" reading where the 3 quarks form a symmetric composite. The corresponding $V_3$ representation of $U_q(\mathfrak{sl}_2)$ has $\dim_q = [4]_q \approx 4.110$, and $[4]_q^2 \approx 16.89$ — closer to $(1/z)^4 = 16.087$ than to $\alpha = 9.469$.

Neutron's $(3)$-character is also positive (1.368) but smaller, and its $(2,1)$ and $(1,1,1)$ characters are more negative. The proton/neutron $\mathrm{tr}_M$ ratio at $q_0$ is **1.700** — close to but not exactly any standard quantum quantity ($[2]_q = 2.011$ is the nearest 18%).

## Negative findings

1. **$\alpha \ne \mathrm{tr}_M(\beta_p)$ directly.** $\mathrm{tr}_M(\beta_p) = 0.636 \ne 9.469$.
2. **$\alpha \ne \mathrm{tr}_M(\beta_p)^2$.** $\mathrm{tr}_M(\beta_p)^2 = 0.404$.
3. **$\alpha \ne $ classical Plancherel sum $\sum_\lambda (\dim V_\lambda)^2 / 3!$.** This sum is $(1+4+1)/6 = 1.000$.
4. **$\alpha \ne $ q-Wedderburn sum $\sum_\lambda \dim_q^2(V_\lambda) / [3]_q!$.** This equals $(1 + 4.04 + 1) / 6.12 = 0.987$.

## Computational limitations encountered

To test $\alpha$ rigorously via the **full atom** $\mathrm{tr}_M$ ratio (e.g. $\mathrm{tr}_M(^3\mathrm{He}) / \mathrm{tr}_M(D) \stackrel{?}{=} \alpha$), one would need:
- $\mathrm{tr}_M(D)$ in $H_6$ — computable (17 s via `markov_trace_recursive.py`); $\mathrm{tr}_M(D) = 0.579$ at $q_0$.
- $\mathrm{tr}_M(^3\mathrm{He})$ in $H_9$ — **times out at 180 s** with the recursive approach (9! = 362880 basis elements).
- Need either (a) the pyhecke Rust kernel `pyhecke_native` (not currently compiled in this environment), (b) a smarter Markov-trace reducer that exploits the canonical-braid block structure, or (c) accepting the indirect test via $|\Delta_\lambda^*|$ ratios (already done in Phase 4).

## Productive directions for Phase 5b

1. **Wenzl hook-content closed form**. The Jones-Markov coefficients $y_\lambda$ have a known closed form in terms of hook lengths and contents. Compute $y_\lambda$ for partitions of $n=6$ and $n=9$ at $q_0$, then check $\sum_\lambda y_\lambda \chi_\lambda(\beta_D) / \sum_\lambda y_\lambda \chi_\lambda(\beta_{^3\mathrm{He}})$ matches $\alpha$.
2. **Build pyhecke Rust kernel locally** (`pyhecke_native`). This unblocks all $H_n$ Markov traces for $n \le 18$ within seconds rather than minutes/hours. Requires a Rust toolchain and is a one-time build.
3. **Decompose $\alpha$ as a categorical normalisation ratio**. The Phase 4 closure has structure $\alpha \cdot \mathrm{Vol}_{\mathrm{hyp}}(\,) \cdot \dots / [8]_q$. Maybe $\alpha = [8]_q \cdot \mathrm{(something cleaner)}$? Testing $\alpha \cdot [8]_q^{-1} = 9.469 / 8.946 = 1.058$ — close to $q_0 = 1.110$ but not exact. Test $\alpha \cdot [8]_q^{-2}$ etc.
4. **Adjacent-rank q-Schur dimension**. The Z=1 → Z=2 step adds a "proton sub-braid" that lives in a sub-Hecke algebra $H_3 \subset H_9$. The corresponding restriction $V_{\lambda \downarrow H_3}$ for each $V_\lambda$ of $H_9$ has a known branching. Maybe $\alpha$ is the *total q-Schur dimension* of the difference.

## Practical recommendation

The Phase 4 closure is already at the 2.51% max rel.err. level (zero-parameter). For the immediate 1ppb thread, this is **good enough to be useful** — the 2.17% residual on $\alpha$ propagates to 2.5% on $^4\mathrm{He}$ which is the loosest atom. A full derivation of $\alpha$ would tighten this to a 1-leg precision win, but is not blocking.

**Action item**: the cleanest path forward is **build the pyhecke Rust kernel** (Phase 5b.2 above) so $H_9$ computations become tractable. Then directly test the $\mathrm{tr}_M$-ratio hypothesis and verify (or refute) the categorical reading of $\alpha = [3]_q^2$.

## Bibliography

- Wenzl, H. (1988). Hecke algebras of type $A_n$ and subfactors. *Inventiones mathematicae* 92, 349–383.
- Jones, V. F. R. (1987). Hecke algebra representations of braid groups and link polynomials. *Annals of Mathematics* 126, 335–388.
- Kassel, C., Turaev, V. (2008). *Braid Groups* (Graduate Texts in Mathematics 247), Springer.
