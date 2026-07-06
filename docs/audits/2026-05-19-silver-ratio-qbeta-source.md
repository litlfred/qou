# Q_β's silver-ratio source: $q^2 - 2q - 1$ from $h(h-2)/2$

**Date:** 2026-05-19
**Branch:** `claude/qbeta-fsc-categorical-ratio-2026-05-19`
**Context:** user inquiry "where does 1±√2 come in on Bring's? or in the gauge/symmetry groups floating about?" The silver-ratio polynomial $q^2 - 2q - 1$ (roots $1 \pm \sqrt 2$) appears in Q_β's Form A. This audit traces its categorical source and explores connections to gauge / symmetry structures.

## Source of the silver-ratio polynomial

From [`prop:neutron-qvalue-symbolic`](../../content/quantum-observable-universe/particle-interactions/neutron-qvalue-symbolic.md):

$$
\Delta(\mathrm{net}) \;=\; \mathrm{net}(n) - \mathrm{net}(p) \;=\; \frac{h^2}{2} - h \;=\; \frac{h(h-2)}{2}
$$

where $h = q - q^{-1}$ is the Hecke skein parameter.

Form A's polynomial factor $q^2 - 2q - 1$ equals $h(h-2) \cdot \text{(power of q)}$ (after clearing denominators).

**Roots of $h(h-2) = 0$**: $h = 0$ (trivial, $q = 1$) and $h = 2$.

Setting $q - q^{-1} = 2$ gives $q^2 - 2q - 1 = 0$, so $q = 1 \pm \sqrt 2$ (the silver-mean conjugates).

## Categorical interpretation of the silver ratio

At $q = 1 + \sqrt 2$ (silver ratio):

| Structure | At silver ratio |
|---|---|
| Hecke skein parameter $h$ | $h = 2$ (integer "branch number") |
| Hecke quadratic $\sigma^2 = h\sigma + 1$ | $\sigma^2 = 2\sigma + 1$, roots $\sigma = 1 \pm \sqrt 2$ |
| **Eigenvalues of $\sigma$ = the silver ratio itself** | **Self-referential fixed point** |
| $\Delta(\mathrm{net}) = h(h-2)/2$ | $= 0$ (proton/neutron degenerate) |
| Form A $|q^2 - 2q - 1|$ | $= 0$ (β-decay forbidden categorically) |

**Physical meaning**: $q = 1 + \sqrt 2$ is the "β-decay null" point — the substrate value at which proton and neutron become categorically indistinguishable. The actual substrate $q_0 \approx 1.110$ is far from this point, so β-decay is allowed with non-zero $Q_\beta$.

**Mathematical meaning**: $q = 1 + \sqrt 2$ is the FIXED POINT of the Hecke quadratic on V_(2,1): the generator's eigenvalue equals $q$ itself. The Hecke algebra "collapses" structurally at this point (loss of one Hecke degree of freedom).

## Where else does $1 \pm \sqrt 2$ live in the framework?

### Direct search

`grep -rln "silver ratio\|1[+-]√2\|2.4142"` across `content/` returns **only one hit** (a Lean witness file for Be-10). The silver ratio is NOT explicitly named anywhere else in the published framework.

### Implicit appearances — gauge / symmetry structures

The B_2 root system (rank-2, type B) has root-length ratio $\sqrt 2$ between long and short roots. B_2 is the Weyl-group root system of:

- **SO(5)** / **Spin(5)** / **Sp(2)** — all share the B_2 root system
- The 8-element B_2 Weyl group = dihedral group $D_4$ (8 reflections of the square)

Possible connection (speculative):

- **β-decay involves the SU(2)_L weak isospin doublet** $(u, d)$. The u→d transition is one Weyl group element. The doublet rep itself doesn't have B_2 structure.
- **Categorical level**: the Hecke algebra $H_n(q)$ acts on $V_{(2,1)} \subset \mathbb{C}^2$ via the seminormal basis. The "rotation" by $\sqrt 2$ between $T_1$ and $T_2$ basis elements via the off-diagonal $b$ coupling has $b^2 \to 3/4$ at $q=1$, which is the **same value as the off-diagonal Casimir for the SO(3)/SU(2) spin-1/2 rep** ($\frac{1}{2}(\frac{1}{2}+1) - (\frac{1}{2})^2 = 3/4$).

So **at $q=1$, $b^2 = 3/4$ matches the Casimir-off-diagonal value of spin-1/2**. At general $q$, $b(q)^2 = (q^4 + q^2 + 1) / (q^2+1)^2$ is the q-deformation of this $3/4$.

### Implicit appearances — Bring's surface

Bring's surface is the genus-4 quintic curve in $\mathbb{CP}^4$ cut by the symmetric polynomials. Its symmetry group is $S_5$ (alternating $A_5$ at the level of orientation-preserving). $S_5$ has order 120; its representations involve cyclotomic 5th roots of unity, NOT the silver ratio.

The Bring-curve fibre structure at $q \to 0$ and $q = 1/2$ (shown in figures of Ch 3) doesn't obviously feature silver-ratio coordinates. **Search of `content/quantum-observable-universe/descartes-universe/brings-*` for $\sqrt 2$ returns zero hits.**

So Bring's surface does NOT host the silver ratio explicitly. The silver ratio's source is specifically the **Hecke quadratic structure at h=2**, not Bring's quintic geometry.

## Does the silver-ratio insight unlock the $c_k$ derivation?

**Tested**: evaluate $c_k$ closed forms at $q = 1 + \sqrt 2$ (silver ratio):

| $c_k$ | Closed form | At $q = 1+\sqrt 2$ |
|:----:|:-----------:|:-----:|
| $c_3$ | $-2$ | $-2$ (constant; unaffected) |
| $c_4$ | $c_3 \cdot b^4$ | $\approx -1.53$ (b² ≈ 0.876 at silver ratio; b⁴ ≈ 0.766; c_4 = -2·0.766) |
| $c_5$ | $-(b^2 + 1/2)$ | $\approx -1.38$ |
| $c_6$ | $4 b^2$ | $\approx 3.50$ |
| $c_7$ | $-8$ | $-8$ |

**Not clean** — the c_k closed forms don't simplify at the silver ratio. The silver ratio is NOT a "natural simplification point" for the c_k.

This rules out "evaluate at the silver ratio to get clean c_k" as a derivation path.

## What the silver ratio actually contributes

The silver-ratio polynomial $q^2 - 2q - 1$ is the **categorical-degeneracy locus** — the q-value where β-decay vanishes. Form A's overall scale is set by HOW FAR $q_0$ is from this locus:

$$
|q_0^2 - 2q_0 - 1| \big/ |q_{\text{silver}}^2 - 2q_{\text{silver}} - 1| = |1.988 / 0| = \infty
$$

The actual $q_0 \approx 1.110$ gives $|q_0^2 - 2q_0 - 1| \approx 1.988$, so the categorical mass is "set by the distance from the silver-ratio degeneracy."

This is **NOT a shortcut to deriving $c_k$**, but it IS:

1. A clear physical meaning of Form A's polynomial structure (categorical-degeneracy locus).
2. An explanation of why FSC/G-style cyclotomic derivations DON'T apply to Q_β: the source polynomial has irrational roots, not roots of unity.
3. A hint that the c_4..c_7 corrections are "perturbations away from silver-ratio degeneracy" — but the explicit functional form of these perturbations is what we don't have.

## Open question: is the silver ratio fundamental to β-decay?

The framework currently uses $q_0 \approx 1.110$ (fixed by $m_\mu/m_e$ via CAL-2). The silver ratio $1 + \sqrt 2 \approx 2.414$ is a DIFFERENT q-value. The framework's chain is:

CAL-1 ($m_e$) + CAL-2 ($q_0 = 1.110$) → predict $Q_\beta$ at $q_0$.

If $q_0$ were the silver ratio instead, β-decay would be categorically forbidden. The fact that $q_0$ is NOT the silver ratio is what enables β-decay physically.

**Open**: is there a deeper reason $q_0 \neq$ silver ratio, beyond the empirical CAL-2 calibration? This connects to the **substrate-derivation of $q_0$** open problem (declined per coordination ledger 2026-05-08 as "Subgoal-2 research-grade").

## Cross-references

- [`prop:neutron-qvalue-symbolic`](../../content/quantum-observable-universe/particle-interactions/neutron-qvalue-symbolic.md) — Form A derivation (Δ(net) = h(h-2)/2)
- [`prop:q-beta-categorical-precision-ladder`](../../content/quantum-observable-universe/braids-and-knots/q-beta-categorical-precision-ladder.md) — c_k precision ladder
- [`computations/qbeta/qbeta_fsc_g_pattern_comparison.py`](../../computations/qbeta/qbeta_fsc_g_pattern_comparison.py) — FSC/G algebraic comparison
- [`prop:alpha-em-categorical-trace-ratio`](../../content/quantum-observable-universe/descartes-universe/alpha-em-categorical-trace-ratio.md) — FSC derivation (cyclotomic)
- [`rem:g-q-closed-form`](../../content/quantum-observable-universe/observations/g-q-closed-form.ts) — G(q) = q²/(q-1)⁴ derivation
