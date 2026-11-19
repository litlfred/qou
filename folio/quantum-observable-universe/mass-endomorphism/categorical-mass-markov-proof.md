## Proof

The chain has three steps.

**Step 1 (Mass integrand = identity).**
By definition ([mass](#def:mass-identity)), $\mathfrak{m}(\varrho) = \lVert \int_A \circ \Psi \circ \varrho \rVert$ with $\Psi = (\int_A \otimes \mathrm{id}) \circ \Delta$. The unit law and the Frobenius relation give $\Psi = L_u$, left multiplication by $u = \Psi \circ \eta$. When the Frobenius form is the counit, $\int_A = \varepsilon$, the counit law $(\varepsilon \otimes \mathrm{id}) \circ \Delta = \mathrm{id}_A$ gives $\Psi = \mathrm{id}_A$, hence

$$
  \mathfrak{m}(\varrho) = \Bigl\lVert \textstyle\int_A \varrho \Bigr\rVert .
$$

The reason is the counit law. It is not the Nakayama automorphism or $S^2 = \mathrm{id}$: $\Psi$ is a left multiplication, and it is the identity exactly when $u = \eta$.

**Step 2 (Frobenius form = Markov trace = quantum trace of the multiplicative integral).**
Take $\int_A$ to be the normalised Jones–Markov trace. It is realised on $V^{\otimes n}$, $V = R^2$, through Jimbo's R-matrix $\check R$. A braid word $\ell_1 \cdots \ell_k$ has transports $T(\sigma_a) = \check R_a$ and $T(\sigma_a^{-1}) = \check R_a - (q - q^{-1})$, acting at strands $a, a+1$. Its multiplicative integral is the ordered product $\mathrm{Hol}(\beta) = T(\ell_1) \cdots T(\ell_k)$, and

$$
  \textstyle\int_A \rho(\beta)
  \;=\; (1 + q^2)^{-n} \, \mathrm{Tr}\bigl( K^{\otimes n} \cdot \mathrm{Hol}(\beta) \bigr),
  \qquad K = \mathrm{diag}(1, q^2).
$$

This functional is cyclic. It satisfies the positive and negative Markov moves with scalars $q^3/(q^2+1)$ (convention D) and $q^{-1}/(q^2+1)$, and $\int_A 1 = 1$. The weight $K$ is not chosen: the Markov move exists only for $K = \mathrm{diag}(1, q^2)$ up to scale. This is Turaev's enhanced Yang–Baxter operator $(\check R, K, \alpha = q^2, \beta = q)$.

The categorical trace of $A$ acting on itself is not this functional. It is the regular trace, which fails the Markov property: on $H_3(q)$ the normalised regular trace gives $\mathrm{tr}(\sigma_1 \sigma_2) = h^2/6$ against $\mathrm{tr}(\sigma_1)^2 = h^2/4$, with $h = q - q^{-1}$.

**Step 3 (Mass = trace of cycle).**
Combining Steps 1 and 2:

$$
  \mathfrak{m}_{q,\mathcal{K}}
  \;=\; \Bigl\lVert \textstyle\int_A \bigl(
    \underbrace{(\int_A \otimes \mathrm{id}) \circ \Delta}_{= \,\mathrm{id}_A}
    \circ\, \varrho \bigr) \Bigr\rVert
  \;=\; \Bigl|\!\int_A\! \rho(\beta_\mathcal{K})\Bigr|
  \;=\; (1 + q^2)^{-n} \, \bigl| \mathrm{Tr}\bigl( K^{\otimes n} \cdot \mathrm{Hol}(\beta_\mathcal{K}) \bigr) \bigr| .
$$

**Scope.** Steps 1 and 2 are proved over a generic commutative ring: Step 1 establishes the mass-integrand identity from the counit hypothesis, and Step 2 establishes the word-braid Markov trace identity on top of the cyclic quantum trace and positive/negative Markov peel identities. The descent to braid classes holds on the tower of Artin braid groups: the framing-corrected trace is invariant under conjugation and both stabilisations, every braid is spelled by a word, and the identity of Step 2 holds on braid classes. Three points are not proved here.

1. *Which algebra carries the Frobenius structure.* Under convention D the Ocneanu weights vanish on every three-row shape. So the pairing $(x, y) \mapsto \int_A xy$ is degenerate on $H_n(q)$ for $n \ge 3$, and $(H_n(q), \int_A)$ is not a Frobenius algebra. The Frobenius object is the quotient by the radical of this pairing, $H_n(q)/\mathrm{rad}$. On it the form is positive definite for $q > 1$, because the surviving two-row weights $y_{(n-k,k)} = [n-2k+1]_q/[2]_q^{\,n}$ are strictly positive. That this quotient is the Temperley–Lieb algebra $\mathrm{TL}_n(q)$ is not proved here.
2. *That the Frobenius form is the counit.* This is the hypothesis of Step 1. It holds when $\Delta$ is the coproduct induced by $\int_A$, and has to be checked for the Frobenius–Hopf data actually used.
3. *The continuous holonomy.* $\mathrm{Hol}$ is a finite ordered product. That the holonomy of the Knizhnik–Zamolodchikov connection along a braid equals such a product of R-matrices is the Drinfeld–Kohno theorem. For $\mathfrak{sl}_2$ the precise statement is Kohno's Theorems 1.2.8 and 2.2.4: the monodromy of $\omega=\lambda\sum\Omega_{\alpha\beta}\,d\log(z_\alpha-z_\beta)$ sends $\sigma_i$ to $q^{\nu}$ times the Hecke generator, with $q=e^{-\pi i\lambda}$, and only up to conjugation by an analytic $P(\lambda)$. The scalar $q^{\nu}$ is a writhe factor. The conjugation leaves the plain trace unchanged. For the weighted trace, Kohno's particular $P(\lambda)$ is not shown to preserve total weight, but a weight-preserving replacement exists, which is all the trace needs. Write $H_{\mathrm{tot}}$ for the total weight, so that $K^{\otimes n}=q^{n}q^{-H_{\mathrm{tot}}}$. (i) $\Omega$ is $\mathfrak{g}$-invariant, so the monodromy $\theta$ commutes with the diagonal $\mathfrak{g}$-action and $V^{\otimes n}=\bigoplus_j V_j\otimes M_j$ as $\mathfrak{g}\times B_n$-modules; on the R-matrix side $V^{\otimes n}=\bigoplus_j V^{q}_j\otimes M^{q}_j$ by $q$-Schur–Weyl duality \cite{jimbo1986}, with the $M^{q}_j$ irreducible and pairwise non-isomorphic for $q$ not a root of unity. (ii) The two $B_n$-images are conjugate, so their commutants have the same dimension, $\sum_j(2j+1)^2$. On the monodromy side the commutant contains the image of $U(\mathfrak{g})$, $\bigoplus_j\mathrm{End}(V_j)\otimes 1$, of exactly that dimension, so it equals it. By the double commutant theorem the $M_j$ are irreducible and pairwise non-isomorphic, each occurring $2j+1$ times. (iii) Since $P(\lambda)$ is a $B_n$-isomorphism, irreducibles with equal multiplicity correspond, and the multiplicities $2j+1$ are distinct, so $M_j\cong M^{q}_j$ via some $\varphi_j$. Choosing weight-preserving linear isomorphisms $\psi_j:V_j\to V^{q}_j$ (each weight space is one-dimensional), $P'=\bigoplus_j\psi_j\otimes\varphi_j$ intertwines the two $B_n$-actions and commutes with $H_{\mathrm{tot}}$. Hence, for generic $\lambda$, $\mathrm{Tr}\big(K^{\otimes n}\mathrm{Hol}(\beta)\big)=q^{-\nu\,w(\beta)}\,\mathrm{Tr}\big(q^{n}q^{-H_{\mathrm{tot}}}\,\theta(\beta)\big)=q^{-\nu\,w(\beta)}\sum_j \mathrm{Tr}_{V_j}\big(q^{n}q^{-H}\big)\,\chi_{M_j}\big(\theta(\beta)\big)$, with $w(\beta)$ the writhe. Check at $n=2$: $\mathrm{Tr}(K\otimes K\,\check R)=q+q^{2}(q-q^{-1})+q^{5}=q^{3}+q^{5}$, which equals the triplet-plus-singlet sum $q(1+q^{2}+q^{4})-q^{-1}q^{2}$. Two conventions are not fixed here: the orientation $q\leftrightarrow q^{-1}$ between $e^{-\pi i\lambda}$ and the Jimbo parameter, and the normalisation of $\Omega$, which moves the per-crossing scalar. Neither changes the argument. It needs $q$ not a root of unity and says nothing about real $q_0$. This is the Drinfeld–Kohno theorem \cite{kohno1987, drinfeld1990, kassel1995}, cited rather than proved. For a real level the monodromy eigenvalues lie on the unit circle, so they cannot equal the real aether value $q_0 > 1$. The real value is reached at the purely imaginary coupling $\lambda_0=\ln q_0/(i\pi)\approx -0.0332\,i$, and the theorem does hold there. Kohno's Remark 1.3.14 states that for any complex $\lambda$ the correspondence of Theorem 1.2.8 holds when the R-matrix images $\varphi(\gamma_k)$ of $\gamma_k=(\sigma_1\cdots\sigma_{k-1})^k$, $2\le k\le n$, are diagonalizable, and that this holds when $\varphi$ is completely reducible \cite{kohno1987}. At real $q_0>1$, $q_0$ is not a root of unity, so $V^{\otimes n}=\bigoplus_j V^{q}_j\otimes M^{q}_j$ is semisimple and $\varphi(\gamma_k)$ acts on each isotypic block of $V^{\otimes k}$ by a scalar (the ribbon twist), hence is diagonalizable. The intertwiner argument above uses only that $q$ is not a root of unity, so it applies at $\lambda_0$ too. A numerical check at $n=3$ agrees: for pure braids $\sigma_1^2,\sigma_2^2$ and the products $\sigma_1^2\sigma_2^2$, $\sigma_2^2\sigma_1^2$, $\sigma_1^2\sigma_2^{-2}$, the KZ monodromy at $\lambda_0$ and the Jimbo R-matrix at $q_0$ have equal traces in every total-weight sector, up to the scalar $q^{-1}$ per $\sigma_i^2$, to $10^{-15}$, with the residual falling as $h^4$ under step refinement, and the opposite orientation $q\mapsto q^{-1}$ fails by $0.70$. So, with $\mathrm{Hol}$ read as the Knizhnik–Zamolodchikov holonomy at $\lambda_0$, the identity holds at the real pin, resting on the cited Kohno theorem and remark. Two pieces are proved unconditionally: the two-strand case, where the Knizhnik–Zamolodchikov transport is solved, shown unique, and its exchange operator equals $q^{-1/2}$ times a weight-preserving conjugate of $\check R(q)$, so that $\mathrm{Tr}\big((K\otimes K)(P\,\mathrm{Hol})^k\big)=q^{-k/2}\,\mathrm{Tr}\big((K\otimes K)\check R^k\big)$ for all $k$; and the flatness of the $n$-point connection ([KZ connection](#def:kz-connection-sl2)). A second, algebraic route to the $\mathfrak{sl}_2$ statement at every $\lambda\notin\mathbb{Q}$ adapts Etingof–Motorin–Varchenko–Zhu. What stays open is different: whether the framework's own aether connection is this Knizhnik–Zamolodchikov connection.

## Explicit values

Evaluating at $q_0 \approx 1.110$ with Markov parameter $z = q^3/(q^2+1) \approx 0.613$ (**convention D**, SU(2)/Temperley–Lieb — see the [trace-convention registry](../../../docs/coordination/trace-convention-registry.md)) and $h = q - q^{-1} \approx 0.209$:

| Particle | Braid $\beta_\mathcal{K}$ | $\int_A \rho(\beta_\mathcal{K})$ | Symbolic |
|:---:|:---:|:---:|:---:|
| $\gamma$ (photon) | $\mathbf{1}$ | $1$ | $1$ |
| $\sigma_0$ (pol.) | $\sigma_0$ | $z \approx 0.613$ | $z$ |
| $L_+$ (gluon) | $\sigma_0\sigma_1$ | $z^2 \approx 0.375$ | $z^2$ |
| $e^-$ (electron) | $\sigma_0\sigma_1\sigma_0$ | $\approx 0.691$ | $hz^2 + z$ |
| $4_1$ (figure-eight) | $(\sigma_0\sigma_1^{-1})^2$ | $\approx 0.280$ | $\dfrac{q^8-q^6+q^4-q^2+1}{q^6+2q^4+q^2}$ |

These constitute **dimensionless ratios** relative to the photon ($\mathfrak{m}_{q,\gamma} = 1$). Physical masses in MeV require a calibration constant $E_0$, determined by anchoring to one experimental value (e.g., the free neutron $\beta$-decay $Q$-value).

## Role in the unified mass formula

This proposition supplies the $k = 0$ stratum of the curvature-rank decomposition ([unified mass formula](#prop:unified-curvature-rank-mass-formula)): $\mathfrak{m}^{(0)}_{q,\mathcal{K}}(1) = |\!\int_A\! \rho(\beta_\mathcal{K})|$ is the descended Frobenius integral, equal to $E_\infty^{0,*}$ of the GB spectral sequence.

The integral $\int_A \rho(\beta_\mathcal{K})$ is **vortex-specific**, distinguishing $\varrho_{\mathfrak{p}}$ from $\varrho_{\mathfrak{n}}$ and capturing fine isotope variations. The vortex-independent constant offset is the Frobenius co-Casimir $m_e \cdot \tau(C_{\dim_q})$ ([Frobenius universal](#thm:frobenius-codim-universal)). The full mass is:

$$
  \mathfrak{m}_{q,\mathcal{K}}
  \;=\; \sum_{k \geq 0} \alpha_k \cdot \mathfrak{m}^{(k)}_{q,\mathcal{K}}(1)
       \;+\; m_e \cdot \tau(C_{\dim_q}),
$$

with this proposition governing the $k = 0$ component.
