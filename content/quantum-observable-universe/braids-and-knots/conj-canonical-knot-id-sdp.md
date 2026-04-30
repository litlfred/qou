The canonical Hecke elements $T_w$ for the light nuclei
$^2\mathrm{H}$ (deuterium), $^3\mathrm{H}$ (tritium), and
$^3\mathrm{He}$ (helium-3) were historically identified by matching
their hyperbolic volumes to AME binding energies.  This conjecture
states that the joint mass-tower confinement SDP
([prop:confinement-sdp](#prop:confinement-sdp)) uniquely selects
the same Hecke elements from first principles.

## Statement

**Conjecture.**
*Let $\mathbf{E}_0$ be the hadronic energy scale fixed by $Q_\beta$
and let $q = q_0$ be the substrate parameter fixed by $m_\mu/m_e$.
For each light nucleus $\mathfrak{H} \in \{{}^2\mathrm{H}, {}^3\mathrm{H}, {}^3\mathrm{He}\}$,
the joint mass-tower confinement SDP*

$$
  \min_{T_w \in H_{n_0}(q_0)^{\mathrm{GB\text{-}NF}}}
  \Bigl\|
    \rho \cdot \bigl[|\mathrm{tr}_M(T_w)| + \mathrm{tower}(T_w)
    + \mathrm{tr}_M(C_{\dim_q})\bigr] \cdot \mathbf{E}_0
    \;-\; B_{\mathrm{AME}}(\mathfrak{H})
  \Bigr\|^2
$$

*subject to: $\|T_w\|_{\mathrm{Frob}} \leq \Delta_{\max}$,
$\rho \in \mathbb{Z}_{>0}$,*

*has a unique global minimizer $T_w^*$, achieved at:*

| Nucleus | Knot type | $n_0$ | $\rho$ |
|---------|-----------|-------|--------|
| $^2\mathrm{H}$ | $6_2$ | $6$ | $1$ |
| $^3\mathrm{H}$ | $8_{11}$ | $6$ | $2$ |
| $^3\mathrm{He}$ | $L_{6a4}$ | $6$ | $2$ |

*with residual $< 0.5\%$ of $B_{\mathrm{AME}}(\mathfrak{H})$.*

## Evidence

Numerical SDP witnesses (stored in
`folio-assistant/computations/probe-sdp-canonical-paper-formula.witness.json`)
show that the multi-term mass formula reproduces the AME binding
energies of $^2$H, $^3$H, $^3$He to within the claimed error bound
when $T_w$ is set to these knot types.  The conjecture asserts that
no other $T_w$ within the $\Delta_{\max}$ ball achieves a smaller residual.

The uniqueness claim requires:
1. A bound on the number of GB-normal-form elements of $H_6(q_0)$
   with $\|T_w\|_{\mathrm{Frob}} \leq \Delta_{\max}$ (finite, by
   [prop:plancherel-weight-boundedness](#prop:plancherel-weight-boundedness));
2. An exhaustive or branch-and-bound search over those elements
   confirming no other element achieves a smaller residual.

Both steps are computationally tractable but have not yet been executed
in a certified proof.

## Relationship to GAP-A-1

This conjecture directly addresses GAP-A-1 of the
[derivation audit report](#prose:derivation-audit-report).
A proof would replace the historical volume-matching identification
with a purely categorical derivation.
