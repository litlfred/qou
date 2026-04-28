**Definition.**
*Let $P_{\mathrm{bare}}$ be a [confined particle](#def:confined-particle)
at level $\ell$ (typically a bare nucleus, $\ell = 2$) and let
$S = (\{e_k\}, \iota, W_{\mathrm{bind}})$ be an
[electron shell](#def:electron-shell) of multiplicity $Z$ attached
to it.  The **dressing morphism** at $S$ is the arrow in the
[confinement category](#def:confinement-category):*

$$
  \mathrm{dress}_S\,:\;P_{\mathrm{bare}}\;\longrightarrow\;P_{\mathrm{dressed}}
$$

*sending $P_{\mathrm{bare}}$ to the **dressed particle**:*

$$
  P_{\mathrm{dressed}}
  \;=\;
  \bigl(
    \mathrm{name}(P_{\mathrm{bare}}) \oplus \mathrm{name}(S),\;
    \ell,\;
    [\iota(K_{\mathrm{bare}}) \cdot W_{\mathrm{bind}}]_M,\;
    n_0 + Z
  \bigr)
$$

*where $\mathrm{name}(S)$ is the shell label (e.g. `[He]`, `[Ne]`,
`[Ar]`, noble-gas core notation), $[\ \cdot\ ]_M$ is Markov
equivalence, and the composite braid lives in $H_{n_0 + Z}(q)$ via
the cabling embedding.*

**Examples.**

- *Bare proton $\xrightarrow{\mathrm{dress}_{[1s^1]}}$ neutral
  hydrogen ${}^1\mathrm{H}$.*
- *Bare $^4$He-nucleus $\xrightarrow{\mathrm{dress}_{[1s^2]}}$
  neutral helium (noble gas, $Z = 2$).*
- *Bare $^{20}$Ne-nucleus $\xrightarrow{\mathrm{dress}_{[1s^2 2s^2 2p^6]}}$
  neutral neon (noble gas, $Z = 10$).*

**Composition.**
*Dressing is not generally invertible: stripping electrons changes
the binding subword non-trivially via the SDP.  However, dressings
compose:*

$$
  \mathrm{dress}_{S_2} \circ \mathrm{dress}_{S_1}
  \;=\;
  \mathrm{dress}_{S_1 \oplus S_2}
$$

*where $\oplus$ concatenates shell data when the combined $Z$
remains SDP-feasible.  Partial dressing ($0 < Z' < Z_{\max}$) yields
**ions**.*

**Stability under dressing.**
*By [shell-closure stability](#prop:shell-closure-stability)
(forthcoming), the Frobenius-stability index of $P_{\mathrm{dressed}}$
is monotonically non-decreasing along the dressing chain toward
closed-shell noble-gas configurations
($Z \in \{2, 10, 18, 36, 54, 86\}$): each shell closure is a
$\mu \ge 2$ multi-operator fixed point of the SDP, and breaking the
bond requires simultaneously breaking every tight dual block.
Noble-gas objects are therefore **local terminal objects** of the
dressing sub-diagram of $\mathbf{Conf}$.*

**Functoriality of the Markov trace.**
*Under dressing, the Markov trace transforms as:*

$$
  \mathrm{tr}_M(P_{\mathrm{dressed}})
  \;=\;
  \mathrm{tr}_M(P_{\mathrm{bare}}) \cdot
  \prod_{\lambda \in \mathcal{S}^*(S, q)} w_\lambda^{\,\langle \pi_\lambda, \Phi^* \rangle}
$$

*where $\mathcal{S}^*(S, q)$ is the SDP active support and $w_\lambda$
are the block shadow prices.  For $\mu(S, q) = 1$ this collapses to
the scalar-LP product; for $\mu \ge 2$ the full matrix shadow
contributes, which is the content of the multi-operator binding
regime.*
