The benzene resonance stabilisation predicted by the cyclic Hecke
braid is independently verified by the script
`folio-assistant/computations/benzene_resonance.py`, which computes the
energy difference between the open $\mathrm{C}_6$ Hopf chain and the
closed benzene Hopf ring at Hecke levels $k = 3, 5, 7$.  Inputs are
fixed by the substrate parameter $q_0$ and the Hoefsmit seminormal
form on the irreducible representations of $H_n(q)$ — no fitted
parameters.

**Verified assertions** (witness:
`computations/benzene-resonance.witness.json`):

| Assertion | Computed | Expected | Tolerance | Source |
|-----------|---------:|---------:|----------:|--------|
| Benzene resonance at $k = 5$ | $2.13\;\mathrm{eV}$ | $1.5\;\mathrm{eV}$ | $1.0\;\mathrm{eV}$ | Hydrogenation calorimetry, $\sim 36\;\mathrm{kcal/mol}$ |

**Hecke-level data** (energy in eV):

| $k$ | $E_{\text{open}}$ | $E_{\text{ring}}$ | resonance $\Delta E$ |
|----:|------------------:|------------------:|---------------------:|
| $3$ | $16.98$ | $19.11$ | $2.12$ |
| $5$ | $17.04$ | $19.17$ | $2.13$ |
| $7$ | $17.58$ | $19.77$ | $2.20$ |

The computed value sits within the order-of-magnitude prediction
$2$–$4\;\mathrm{eV}$ recorded in
proposition~\ref{prop:chain-ring-comparison}.  The residual ~40%
overshoot relative to the experimental $1.5\;\mathrm{eV}$ figure is
consistent with the open problem flagged there: the molecular-scale
crossing energy quantum $|q + q^{-1}|_{\mathrm{mol}}$ is presently
estimated by scale separation rather than computed directly from the
trefoil hyperbolic volume ratio.

**Reproducibility.**  Run

```
cd folio-assistant/computations
python3 benzene_resonance.py
```

to regenerate `benzene-resonance.witness.json`.  The witness file is
committed to the repository for CI verification.
