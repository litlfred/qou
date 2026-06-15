# `gb_filtration_jet_tracker.py` extension plan

## Background

`gb_filtration_jet_tracker.py` currently performs Gröbner-Shirshov
normal-form reduction in $H_n(q)$ for two atlas entries:

| Entry | $\sigma$-word | Closure | Status |
|---|---|---|---|
| Electron | $\sigma_1^3$ | trefoil $3_1$ (torus, no BW) | tested |
| Proton/neutron | $(\sigma_1\sigma_2^{-1})^3$ | Borromean $\mathcal{B}_3$ (hyperbolic) | tested |

The atlas's other four hyperbolic entries lack explicit
$\sigma$-words: $\{4_1, 6_2, 8_{11}, L_{6a4}\}$. The
[`bring-hyperbolic-knot-bloch-decomposition`](../../content/quantum-observable-universe/archimedean-universe/bring-hyperbolic-knot-bloch-decomposition.md)
block flags this as the irreducible computational gate.

## Concrete extension plan

For each missing entry, the steps are mechanical:

### (a) Figure-8 $4_1$ — closes in $H_3$

Standard braid representation: $4_1 = \widehat{(\sigma_1\sigma_2^{-1})^2}$
in $B_3$. The braid word is **already** $\sigma$-shortlex if we
order $\sigma_1 < \sigma_2$ — no GS reduction needed beyond Hecke
relation $\sigma_i^2 = (q-q^{-1})\sigma_i + 1$, which doesn't fire
on this word.

**Action:** add `test_figure_8` to the tracker:
```python
braid_word = [(1, 1), (2, -1), (1, 1), (2, -1)]  # σ₁ σ₂⁻¹ σ₁ σ₂⁻¹
hecke_n = 3
```

### (b) Deuteron $6_2$ — closes in $H_3$ (one of several minimal forms)

Standard braid representation: $6_2 = \widehat{\sigma_1^{-1}\sigma_2\sigma_1^{-1}\sigma_2^2}$
in $B_3$. Bridge number 2, so $H_3$ suffices.

**Action:** add `test_deuteron_62` with the appropriate signed
sequence. Apply Hecke relation to $\sigma_2^2$.

### (c) Tritium $8_{11}$ — closes in $H_3$

Standard: $8_{11} = \widehat{\sigma_1^{-1}\sigma_2\sigma_1^{-2}\sigma_2^3}$
in $B_3$ (bridge number 2). Apply Hecke to $\sigma_2^3$ and
$\sigma_1^{-2}$.

### (d) Helium-3 $L_{6a4}$ — link, closes in $H_3$ as 2-component

Already noted in atlas: $L_{6a4}$ is volume-equivalent to $\mathcal{B}_3$
(both $= 8G$), so it shares a Bloch class with Borromean.
**No new computation needed** — reuse the $\mathcal{B}_3$ tracker
output with a Markov-equivalence justification (link form,
identical hyperbolic structure).

## Out-of-band

For each (a)-(c) above, after GS reduction:
1. Read off the canonical $T_w$ in the GS-shortlex normal form.
2. Apply the Markov trace $\mathrm{tr}_M$ at $q_0$.
3. Numerical-cross-check against SnapPy's hyperbolic volume.
4. Emit a witness JSON with the canonical form + trace value.

## Why not implemented now

The actual Python work is straightforward but cumulatively
substantial (~150-300 lines per knot for the symbolic-q tracker
infrastructure). Splitting into a separate PR keeps the focus on
the §3b-cond scaffolding closure pass we're in the middle of.

## Acceptance criteria

After extension, the tracker produces canonical $T_w$ in
$H_3(q)$ for each of $\{4_1, \mathcal{B}_3, 6_2, 8_{11}, L_{6a4}\}$,
and the cross-checked SnapPy volumes agree to ≥ 50 digits.

## How this relates to the Tier-0 PSLQ result

The Tier-0 PSLQ check
([`tier-0-atlas-pslq-check.witness.json`](tier-0-atlas-pslq-check.witness.json))
**already** searched for an integer relation among the four
atlas BW values $\{2\,\mathrm{Cl}_2(\pi/3), 8G, \mathrm{Vol}(6_2),
\mathrm{Vol}(8_{11})\}$ vs $2/(3\pi)$ at 100 dps with max coeff
$10^8$, and returned **NO** relation. So the four named atlas
hyperbolic objects, as numerical BW values, do NOT span $2/(3\pi)$
via small integer combinations.

The extension above does NOT change this conclusion — the BW
*values* are already known to high precision (SnapPy / KnotInfo).
What the extension adds is the **GS-NF derivation**: each volume
becomes a structurally-derived Markov-trace output rather than a
black-box geometric constant. This is required for the §3b-cond
`BringHyperbolicDecomposition` instance to be a *theorem* (with
provable derivation chain) rather than an existential claim.

The next-tier numerical advance is **Tier-1**: enumerating all
hyperbolic 3-braid closures (~30 prime knots through 10 crossings
per Birman-Hilden) and re-running the PSLQ search over the wider
basis. If a relation appears at Tier-1, the
`BringHyperbolicDecomposition` instance can be produced; if not,
the search extends to higher-bridge-number knots in $H_n$ for
$n \leq 8$.
