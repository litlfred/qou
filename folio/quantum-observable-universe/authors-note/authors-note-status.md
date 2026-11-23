**This monograph is a work in progress.** Many of its results are proved, some are conditional on stated conjectures, and several of its comparisons with experiment are far from closed. It is released so that others can check it, correct it and build on it. Meaningful contributions are welcome. The contribution policy is in [Contributions and authorship](#sec:authors-note-contributions).

**Where the gaps are.** The open problems are collected where they arise. The two main collections are the [open problems of the mass theory](#sec:mass-open-problems) and the [open problems of the Standard Model appendix](#sec:sm-open-problems). Each chapter also marks its conjectures as conjectures, and a theorem that depends on one states that dependence in its first line.

**How close the numbers are.** The framework takes three measured inputs: the electron mass, the substrate parameter $q_0$ (pinned on the proton-to-electron mass ratio), and the pion mass. Everything below is computed from those three and compared with experiment. The figures come from the project's live dashboards (`computations/per-observable-100x-status.witness.json` and `computations/mass_binding_dashboard.py`, regenerated November 2026). They will change as the work continues.

| Quantity | Model | Experiment | Agreement |
|---|---|---|---|
| Muon-to-electron mass ratio (mass) | 211 ppb off | CODATA 2022 | about $9.5\sigma$ |
| Neutron mass (mass) | $939.11$ MeV | $939.57$ MeV | $0.05\%$ low |
| Neutron–proton mass difference (mass) | $0.84$ MeV | $1.29$ MeV | $35\%$ low |
| Inverse fine-structure constant (charge) | $137.035999127$ | $137.035999177$ | $0.4$ ppb, conditional on an open Lean step |
| Neutron β-decay $Q$-value | $0.33$ MeV | $0.78$ MeV | $58\%$ low |
| Kaon-to-pion mass ratio | $3.537119$ | $3.537118$ | $51$ ppb |
| Deuteron binding | $2.86$ MeV | $2.22$ MeV | $29\%$ high |
| Triton binding | $6.20$ MeV | $8.48$ MeV | $27\%$ low |
| Helium-4 binding | $8.77$ MeV | $28.30$ MeV | $69\%$ low |
| Lithium-7 binding | $18.0$ MeV | $39.3$ MeV | $54\%$ low |

Two readings of this table matter. First, the close agreements are not all unconditional: the fine-structure result rests on an unproved step, and the kaon–pion result includes a truncated correction series. Second, the binding energies use a functional form that is asserted rather than derived, and they miss badly beyond the lightest nuclei. The β-decay value and the binding energies are the clearest places where the model, as it stands, does not yet work.
