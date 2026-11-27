The model takes three measured inputs: the electron mass, the proton-to-electron mass ratio (which fixes $q_0$), and the charged-pion mass. Every other entry below is computed from those three and compared with experiment. The full scorecard, with every observable, its uncertainty and its source, is [ACCURACY.md](https://github.com/litlfred/qou/blob/main/ACCURACY.md) in the repository; this table is generated from the same computations and changes when they do.

| Quantity | Model | Experiment | Difference | Status |
|---|---|---|---|---|
| Muon mass (MeV) | $105.6583978$ | $105.6583755$ | $+211$ ppb ($9.7\sigma$) | Derived |
| Tau-to-electron mass ratio | $3477.44$ | $3477.23$ | $+61$ ppm ($0.9\sigma$) | Conditional |
| Kaon-to-pion mass ratio | $3.5371186$ | $3.5371184$ | $+51$ ppb | Selected |
| Inverse fine-structure constant | $137.035999127$ | $137.035999177$ | $-0.37$ ppb ($2.4\sigma$) | Conditional |
| Electroweak scale (GeV) | $246.21964$ | $246.21965$ | $-29$ ppb ($0.1\sigma$) | Conditional |
| Neutron mass (MeV) | $939.1085$ | $939.5654$ | $-486$ ppm | Conditional |
| Neutron–proton mass difference (MeV) | $0.8364$ | $1.2933$ | $-35.3\%$ | Conditional |
| Neutron $\beta$-decay $Q$-value (MeV) | $0.3254$ | $0.7823$ | $-58.4\%$ | Conditional |
| $\beta^-$ decays of nuclei, exothermic | $0$ of $1009$ | $1009$ of $1009$ | median $142\%$ in $Q$ | Open |
| Deuteron binding (MeV) | $2.265$ | $2.225$ | $+1.8\%$ | Selected |
| Deuteron binding, ruled trace pipeline (MeV) | $0.00636$ | $2.22457$ | $-99.7\%$ | Conditional |
| Helium-4 binding (MeV) | $29.33$ | $28.30$ | $+3.7\%$ | Selected |
| Iron-56 binding (MeV) | $135.1$ | $492.3$ | $-72.6\%$ | Open |
| Binding, all $2542$ nuclides with $A \ge 2$ | chain proxy | AME2020 | median $69\%$ low | Open |

*Derived* means computed from the three inputs with no unproved hypothesis; *selected* means an object (a pair, a grid cell, a chart) was chosen because it lands near the measured value, which counts as a fit; *conditional* means the value rests on a stated conjecture or an unproved step; *open* means the model does not yet reproduce the quantity. Two of the close agreements carry further qualifications: the fine-structure value is conditional on an open step in the Lean formalisation, and the kaon-to-pion ratio rests on a fusion pair chosen from a scan and includes a truncated correction series. The deuteron and helium-4 binding energies are the grid cell nearest the measured deuteron out of several few-body models and energy charts compared in the full scorecard. The ruled trace pipeline (a γγ-selected bond between the two nucleons, the tower energy scale and the logarithmic binding law) is shown beside them: it binds the deuteron by about $6\;\mathrm{keV}$, $99.7\%$ short. Beyond the lightest nuclei the binding energies come from a chain proxy whose saturation is open, and they fall short by a median of $69\%$. The $\beta$-decay values and the binding energies are the clearest places where the model, as it stands, does not yet work.
