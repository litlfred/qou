---
id: q-clt-jsj-mass-scaling
title: "Remark: Exact q-CLT Scaling for Heavy Isotopes"
---
# Exact q-CLT Scaling for Heavy Isotopes

When modeling the macroscopic atomic mass of heavy isotopes up to Oganesson ($A=294$), evaluating the absolute topological Hecke trace of the $A$-nucleon knot becomes computationally intractable. However, physical mass scaling is fundamentally anchored by the Jaco-Shalen-Johannson (JSJ) additivity of the atomic braid volumes. 

Because the mathematical structure guarantees modular volume sums for the proton ($m_p$) and neutron ($m_n$) blocks (see the Braids & Knots discussion on JSJ Additivity), the q-CLT (quantum Central Limit Theorem) approximation is not merely a statistical heuristic. It is the exact topological asymptotic limit of the physical model.

As a result, we partition the absolute mass prediction into two computational channels:
1. **`m_symbolic`**: The exact closed-form evaluation of the Hecke matrix traces, computationally constrained to light isotopes (e.g., $A \le 8$).
2. **`m_qCLT_approx`**: The asymptotic mass limit, driven by the geometric JSJ volume additivity. 

This strict physical and mathematical separation ensures that the theoretical integrity of the predictions remains intact, correctly bridging the exact low-nucleon geometry with the exact macroscopic limits, without relying on truncated algorithmic triangulations.
