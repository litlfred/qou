**Proposition (Schur–Weyl justification of shell self-duality).**
*Let $\mathcal{U}_q(\mathfrak{gl}_k)$ denote the quantum enveloping
algebra and $H_n(R, q)$ the Iwahori–Hecke algebra.  Under Schur–Weyl
duality*

$$
  V^{\otimes n}
  \;=\;
  \bigoplus_{\lambda\,\vdash\,n}
    V_{\mathcal{U}_q(\mathfrak{gl}_k)}(\lambda)
    \;\otimes\;
    V_{H_n(R, q)}(\lambda),
$$

*the $S_n$-transpose involution $\lambda \leftrightarrow \lambda^*$
on Young diagrams is the image of the representation-duality
involution $V \leftrightarrow V^*$ on $\mathcal{U}_q(\mathfrak{gl}_k)$-
modules:*

$$
  V_{\mathcal{U}_q(\mathfrak{gl}_k)}(\lambda^*)
  \;\cong\;
  V_{\mathcal{U}_q(\mathfrak{gl}_k)}(\lambda)^*
$$

*(up to a twist by $\det^{n}$ when $\lambda$ has fewer than $k$ rows).
Equivalently, on the Hecke side:*

$$
  V_{H_n(R, q)}(\lambda) \,\otimes\, V_{H_n(R, q)}(1^n)
  \;\cong\;
  V_{H_n(R, q)}(\lambda^*),
$$

*where $V_{H_n(R, q)}(1^n)$ is the sign (alternating) representation.*

*Consequently, the **shell-operator self-duality constraint***

$$
  x_\lambda \;=\; x_{\lambda^*}
  \qquad\text{for all}\quad \lambda \vdash A_{\mathrm{magic}}
$$

*on the Wedderburn decomposition*

$$
  \sigma_{\mathrm{shell}}
  \;=\;
  \sum_{\lambda\,\vdash\, A_{\mathrm{magic}}}
    x_\lambda \cdot e_\lambda
  \;\in\; H_{A_{\mathrm{magic}}}(q)
$$

*is equivalent to $\mathrm{GL}_k$-charge-conjugate invariance of the
underlying quantum-group module structure under Schur–Weyl transport.*

**Physical interpretation.**
*Shell closures in nuclei (magic numbers $\{2, 8, 20, 28, 50, 82, 126\}$)
correspond to **charge-conjugate-invariant braid elements** in
$H_{A_{\mathrm{magic}}}(q)$.  This is the categorical origin of:*

- *Parity conservation in the nuclear strong interaction (shell
  closures respect charge conjugation);*
- *Proton-neutron interchange symmetry at closed shells (isospin
  SU(2) doubling);*
- *Absence of shell-level CP violation (parity-odd channels cancel
  between $\lambda$ and $\lambda^*$ contributions).*

*Parity-violating phenomena (β-decay) arise at **level 3**
(inter-nucleon pair) where the conjugate symmetry is broken by the
skein asymmetry
([skein crossing asymmetry](#prop:skein-crossing-asymmetry)), not
at level 4 (shell) where the Schur–Weyl self-duality is exact.*

**Consequence for the ILP at level 4.**
*The shell-operator ILP*

$$
  \text{minimize}\;
  \sum_\lambda x_\lambda \cdot w_\lambda
  \;\text{s.t.}\;
  \sum_\lambda x_\lambda \cdot y_\lambda
  \;=\; y_{\mathrm{target}},
  \;\;
  x_\lambda \in \mathbb{Z}_{\geq 0},
$$

*admits a **constrained** formulation imposing $x_\lambda =
x_{\lambda^*}$, reducing the search space to self-dual vectors.
The constrained ILP has at most $\lceil p(A_{\mathrm{magic}})/2 \rceil$
variables (one per conjugate-equivalence class), yielding a
significant computational saving for large $A_{\mathrm{magic}}$.*

**Relation to existing propositions.**
*This result refines
[mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price)
(which gives y_λ per partition) by asserting the self-dual
symmetry of the physical shell operator.  It complements
[skein-crossing-asymmetry](#prop:skein-crossing-asymmetry)
(which encodes the parity-violation mechanism at level 3) by
locating the parity-conserving regime at level 4.*
