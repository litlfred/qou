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
  \min_{T_w \in H_{n_0}(q_0)^{\mathrm{GB\text{-}NF}},\,\rho \in \mathbb{Z}_{>0}}
  \Bigl\|
    \rho \cdot \bigl[|\mathrm{tr}_M(T_w)| + \mathrm{tower}(T_w)
    + \mathrm{tr}_M(C_{\dim_q})\bigr] \cdot \mathbf{E}_0
    \;-\; B_{\mathrm{AME}}(\mathfrak{H})
  \Bigr\|^2
$$

*subject to: $\|T_w\|_{\mathrm{Frob}} \leq \Delta_{\max}$
([prop:delta-max-uniform-bound](#prop:delta-max-uniform-bound)),*

*has a unique global minimizer $T_w^*$, achieved at:*

| Nucleus | Knot type | $n_0$ | $\rho$ | $B_\mathrm{AME}$ (MeV) |
|---------|-----------|-------|--------|------------------------|
| $^2\mathrm{H}$ | $6_2$ (Miller's knot) | $6$ | $1$ | $2.2246$ |
| $^3\mathrm{H}$ | $8_{11}$ | $6$ | $2$ | $8.4820$ |
| $^3\mathrm{He}$ | $L_{6a4}$ | $6$ | $2$ | $7.7181$ |

*with residual $< 0.5\%$ of $B_{\mathrm{AME}}(\mathfrak{H})$.*

## Historical evidence (volume matching)

The knot assignments above were originally found by matching
hyperbolic volumes to AME binding energies:

| Nucleus | Knot/link | Vol (SnapPy) | Vol $/ \mathbf{E}_0$ (approx) | Match quality |
|---------|-----------|-------------|-------------------------------|---------------|
| $^2$H | $6_2$ | $3.16396$ | $\approx 0.762$ | $< 1\%$ after multiplicity |
| $^3$H | $8_{11}$ | $3.42721$ | $\approx 0.826$ | $< 0.5\%$ after $\rho = 2$ |
| $^3$He | $L_{6a4}$ | $5.33349$ | $\approx 1.285$ | $< 2\%$ after correction |

The volume-matching identification is empirically strong, but it does not
constitute a categorical derivation.  The conjecture asserts that the SDP
ground truth agrees with the historical assignment.

## SDP witness evidence

Numerical SDP witnesses (stored in
`folio-assistant/computations/probe-sdp-canonical-paper-formula.witness.json`)
show that the multi-term mass formula reproduces the AME binding
energies of $^2$H, $^3$H, $^3$He to within the claimed error bound
when $T_w$ is set to these knot types.  The conjecture asserts that
no other $T_w$ within the $\Delta_{\max}$ ball achieves a smaller
residual.

## Proof obligations

1. **Finitude of candidate set.**  The Plancherel-weight boundedness
   ([prop:plancherel-weight-boundedness](#prop:plancherel-weight-boundedness))
   gives a finite bound on the number of GB-normal-form elements of
   $H_6(q_0)$ with $\|T_w\|_{\mathrm{Frob}} \leq \Delta_{\max}$.
   Make this bound explicit and computable.

2. **Exhaustive or branch-and-bound search.**  Over the finite
   candidate set (or via a certified branch-and-bound), confirm that
   no $T_w \neq T_{6_2}$ (resp.\ $T_{8_{11}}$, $T_{L_{6a4}}$) achieves
   a smaller residual.

3. **Uniqueness of $\rho$.**  Show that $\rho = 1$ for $^2$H and
   $\rho = 2$ for $^3$H/$^3$He are the unique positive-integer
   multiplicities in the feasible SDP region.

## Relationship to GAP-A-1

This conjecture directly addresses GAP-A-1 of the
[derivation audit report](#prose:derivation-audit-report).
A proof would replace the historical volume-matching identification
with a purely categorical derivation.

