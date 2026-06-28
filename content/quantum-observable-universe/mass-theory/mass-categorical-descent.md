The QOU mass formula is the :refterm[descent]{#descent}
decomposition of the mass endomorphism
$\mathfrak{m} \colon A \to A$ under the brane tower blow-up.
The empirical Bethe–Weizsäcker liquid-drop ansatz is recovered
as one phenomenology of this descent decomposition; see
[`conj:q-integer-mass-formula`](#conj:q-integer-mass-formula)
for the recovered coefficients.

**Proposition.**
\*Let $\mathcal{A}(Z,N)$ be the atomic braid in $H_{A+Z}(q)$,
and let $\hat{\tau}$ denote the :refterm[descent]{#descent} involution acting on
$\operatorname{End}(A)$.  Then the mass identity
\$\mathfrak{m}(\mathcal{A}) = Z m\_{\mathfrak{p}} + N m\_{\mathfrak{n}}

* Z m\_e - B(Z,N)\$ decomposes as\*

$$
  B(Z,N) = \underbrace{B^{\mathrm{desc}}(Z,N)}_{\text{descended}}
          + \underbrace{B^{\mathrm{trans}}(Z,N)}_{\text{transient}}
$$

*where the descended component lies in the centre of $H_n(q)$
and the transient component localises to the exceptional divisors
of the brane blow-up.*

**Descended (central) terms.**

The descended component consists of Casimir operators — elements
of the centre $Z(H_n(q))$ that commute with all generators.  By
the Wedderburn-Artin decomposition, these are indexed by partitions
$\lambda \vdash n$:

| BW term                              | Casimir level | Partition family                | Scaling    |
| ------------------------------------ | ------------- | ------------------------------- | ---------- |
| Volume ($\lambda_V \cdot A$)         | $k = 3$       | $[n], [1^n]$ (sym $\oplus$ alt) | $A$        |
| Pairing ($\pm \lambda_P / \sqrt{A}$) | $k = 3$       | $[n-1,1]$ (standard)            | $A^{-1/2}$ |
| Wigner ($\lambda_W \cdot T(T+1)/A$)  | $k = 5$       | $[n-2,2] + [n-2,1^2]$           | $T(T+1)/A$ |

Their coefficients are quantum factorials $[n]_q!$ by the
[Wedderburn trace identity](#prop\:wedderburn-trace-identity):
the sum $\sum_\lambda \dim_q(\lambda)^2 = [n]_q!$ partitions the
total Markov weight among the irreducible representations.

**Transient (exceptional divisor) terms.**

The transient component localises to the exceptional divisors
$E_i \subset \widetilde{X}$ of the blow-up
$\pi \colon \widetilde{X} \to X$ at codimension-$\geq 2$ loci
where crossings degenerate.  Each blow-up centre contributes a
quantum dilogarithm correction:

| BW term                                       | Divisor type            | Content $c$              | Coefficient                  |                              |    |
| --------------------------------------------- | ----------------------- | ------------------------ | ---------------------------- | ---------------------------- | -- |
| Surface ($-\lambda_S \cdot A^{2/3}$)          | Boundary $\partial A_n$ | $c = 0$                  | $\Phi_q(1)$                  |                              |    |
| Coulomb ($-\lambda_C \cdot Z(Z{-}1)/A^{1/3}$) | Charge locus            | $c = \pm 1$              | $\Phi_q(q^{\pm 1})$          |                              |    |
| Exchange ($\pm \lambda_{\mathrm{ex}} / A$)    | Parity locus            | $c = \pm 1$              | $\Phi_q(-q^{\pm 1})$         |                              |    |
| Shell ($\delta_{\mathrm{sh}}$)                | Magic number loci       | $c = c_{\mathrm{shell}}$ | $\Phi_q(z_{\mathrm{magic}})$ |                              |    |
| Hook ($\delta_{\mathrm{hook}} / A$)           | Hook locus              | $c = \pm 2$              | \$                           | \ln \lambda\_{\mathrm{hook}} | \$ |

The content $c$ of each blow-up centre is the magnetic quantum
number $m_j$ under the Schur-Weyl correspondence: the Young
diagram content $c(i,j) = j - i$ equals the $m_j$ eigenvalue of
the angular momentum projection.

**Parallel with coupling.**

The same :refterm[descent]{#descent} structure applies to the electromagnetic coupling
endomorphism $\Phi = P_{\mathrm{anti}}$
([CS-corrected coupling](#prop\:em-coupling-projection)):

| Component              | Mass (BW)                            | Coupling ($1/\alpha$)                                            |
| ---------------------- | ------------------------------------ | ---------------------------------------------------------------- |
| **Base holonomy**      | $\lambda_V \cdot A$ (volume)         | $q \cdot [9]_q \cdot [10]_q$ (bare coupling)                     |
| **Divisor correction** | $-\lambda_S \cdot A^{2/3}$ (surface) | $(\mathrm{CS}_1 + \mathrm{CS}_2) \cdot \hbar_q^2$ (Chern-Simons) |
| **Physical origin**    | Nuclear boundary nucleons            | Force-carrier crossing degeneracies                              |
| **Sign**               | Negative (reduces binding)           | Positive (increases $1/\alpha$)                                  |

The universality of the :refterm[descent]{#descent} decomposition — base holonomy plus
exceptional divisor corrections — reflects the categorical origin
of both mass and coupling as endomorphisms in $\mathbf{C}$,
decomposed by the same involution $\hat{\tau}$.
