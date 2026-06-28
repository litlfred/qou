# Gröbner-Shirshov Energy Probe

## Computational verification

The instrumented division algorithm (`hecke_division.py`) confirms the Hecke step behavior during Gröbner reduction:

| Nucleus | Hecke steps | YB steps | Far-comm | Total $\Delta E$ |
|---------|:---:|:---:|:---:|---:|
| Deuteron $\mathcal{N}(1,1)$ | 0 | 0 | 0 | 0 |
| ${}^{3}\mathrm{H} \mathcal{N}(1,2)$ | 1 | 0 | 0 | $+0.260$ |
| ${}^{4}\mathrm{He} \mathcal{N}(2,2)$ | 4 | 0 | 0 | $+0.641$ |
| ${}^{6}\mathrm{Li} \mathcal{N}(3,3)$ | 26 | 0 | 0 | $+4.233$ |

All energy changes in this probe arise from Hecke steps. Yang--Baxter and far-commutativity steps contribute zero energy change, consistent with the theoretical derivation.

## Evaluated reduction paths

Evaluating the reduction path between states of fixed nucleon number confirms the step count differential:

| Transition | $\Delta E$ (Hecke steps) |
|------------|:---:|
| ${}^{3}\mathrm{H} \to {}^{3}\mathrm{He}$ | $-0.027$ |
| ${}^{4}\mathrm{He} \to {}^{5}\mathrm{Li}$ | $-0.073$ |
| ${}^{6}\mathrm{Li} \to {}^{6}\mathrm{Be}$ | $-0.828$ |

The differential Hecke step count between these states is consistently negative, with magnitude increasing with $A$.
