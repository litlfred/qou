The three corollaries
([amphicheiral](#cor:knot-factor-amphicheiral),
[Borromean-$k$](#cor:knot-factor-borromean-composite),
[shell-closed](#cor:knot-factor-shell-closed)) replace the empirical
per-isotope $a_\mathcal{K}$ choices with derived expressions:

| Nucleus | Knot family | Empirical $a$ | Spectral derivation |
|---|---|---|---|
| ${}^3\mathrm{H},\ {}^3\mathrm{He}$ | $4_1$ figure-eight | $1 - h^2$ | Amphicheiral self-pairing on $e_{(1^n)}$ |
| ${}^4\mathrm{He}$ | Borromean-$2$ | $(1 - h^2)^2$ | Independent product of two figure-eight pairings |
| ${}^{12}\mathrm{C},\ {}^{40}\mathrm{Ca},\ {}^{56}\mathrm{Fe},\ {}^{208}\mathrm{Pb}$ | Shell-closed | $1$ | Markov-chain equilibrium $\Rightarrow$ projection onto $e_{(n)}$ alone |
| Odd-odd $Z = N$ (${}^6\mathrm{Li},\ {}^{14}\mathrm{N}$) | Asymmetric | $1 - \delta_{\mathrm{Wigner}}$ | Last-neutron breaking $\Rightarrow$ residual on standard irrep |

**Practical computation.**
The Hoefsmit pipeline
([Hoefsmit](#conj:hoefsmit-scattering-pipeline)) produces
$\chi_\lambda(\beta_\mathcal{K})$ for any braid word.  The knot
factor is then a single q-deformed Wedderburn-weighted sum,
bounded (though not unit-normalised) by Wedderburn completeness with
no truncation.  Implementation: replace per-isotope
hand-fits in `computations/atomic_mass_pipeline.py`
with direct evaluation of
([knot factor](#prop:knot-factor-spectral-form)).
