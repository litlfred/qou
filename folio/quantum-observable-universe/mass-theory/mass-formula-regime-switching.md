*There is a single evaluation of the binding energy $B(Z,N)$ that does not branch on $A$, whose dominant contribution changes character exactly at the boundaries of the pair-graph regimes $r(A)$ of [pair-graph regime trichotomy](#prop:pair-graph-regime-trichotomy): regime I ($A=2$), regime II ($A\in\{3,4\}$) and regime III ($A\ge5$). The piecewise evaluation*

$$
  B(Z, N)
  \;=\;
  \begin{cases}
    B_{\mathrm{SW}}(Z, N) + m_e\,\tau(C_{\dim_q}^{H_3})
      & \text{if } A = 2, \\[4pt]
    B_{\mathrm{BW}+\chi}(Z, N)
      & \text{if } 3 \leq A \leq 4, \\[4pt]
    B_{\mathrm{BW}}(Z, N) + B_{\mathrm{shell}}(A)
      & \text{if } A \geq 5
  \end{cases}
$$

*is then a description of that change, not a definition of $B$.*

What is proved is only where the boundaries fall: by [pair-graph regime trichotomy](#prop:pair-graph-regime-trichotomy), $2\bigl(\binom A2-(3A-6)\bigr)=(A-3)(A-4)$, so the cut-offs $2\mid3$ and $4\mid5$ depend on $A$ alone. That criterion was identified after the cut-offs below had been selected. No result derives which evaluation belongs to which regime, and no $A$-uniform evaluation with this property has been established.

The earlier description of the regimes as "non-additive", because the Schur–Weyl and Bethe–Weizsäcker evaluations would count overlapping Wedderburn content, is not a well-posed statement: $B_{\mathrm{BW}+\chi}$ is a polynomial in $A$ and $Z$ with $q$-integer coefficients, not a sum over Wedderburn blocks, so there is no common index set on which an overlap could be shown or refuted.

**Comparison (selection against the measured target; not a prediction).** Table 2 lists, per isotope, the error of each evaluation against AME. The column marked regime-selected is chosen per isotope by the smaller AME deviation. This is selection against the target, one free choice per branch, and AGENTS.md counts it as fitting. The statement that the selected regime agrees with AME to within $5\%$ for $A\le4$ uses a tolerance sized to its own largest miss ($^4$He, $-4.07\%$). The chirality factors in $B_{\mathrm{BW}+\chi}$ are assigned per isotope by hand. The readings "the Schur–Weyl evaluation applies to the light satellite topology of the deuteron" and "collective Wedderburn states dominate for the Borromean topologies at $A\ge3$" are physical glosses without a definition of "dominate".
