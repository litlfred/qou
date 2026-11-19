*Proof.*

*Step 1 (Schur--Weyl setup).*  Self-duality of $A$ and rigidity of
$\mathbf{C}$ give a braided monoidal action of the braid group $B_n$
on $V^{\otimes n}$.  Tannaka--Krein reconstruction realises
$\mathbf{C} \simeq \mathbf{Rep}(H)$, so the centraliser of the
diagonal $H$-action on $V^{\otimes n}$ is the Hecke algebra of type
$A_{n-1}$:

$$
  H_n(R, q) \;=\; \mathrm{End}_H(V^{\otimes n}),
$$

with multiplicity decomposition
$V^{\otimes n} \cong \bigoplus_{\lambda \,\vdash\, n}
V_\lambda^H \otimes V_\lambda^{H_n}$ where
$\dim_R V_\lambda^{H_n} = d_\lambda$ is the classical Hecke irrep
dimension.

*Step 2 (fibre-functor trace = Markov trace).*  The fibre-functor
trace on $\mathrm{End}_R(V^{\otimes n})$, restricted to the
$H_n(R, q)$-summand under the decomposition of Step 1, satisfies the
Markov property
$\mathrm{tr}(x \cdot \sigma_n) = z \cdot \mathrm{tr}(x)$ for
$x \in H_n$ — a direct consequence of the braided monoidal trace
identity for cabling.  The parameter $z$ is fixed by the categorical
$q$-dimension constraint
$z \cdot \dim_q V = 1$, equivalent to
$z = 1/(\sqrt q + 1/\sqrt q)$ when $\dim_q V = [2]_q^{\mathrm{symm}}$.

*Step 3 (uniqueness of the trace).*  By Chlouveraki HDR Theorem 6.20
(equivalently Juyumaya's Theorem 12 at $d = 1$), the type-$A$
Markov-trace family on $\{H_n(R, q)\}_{n \ge 1}$ is **one-dimensional**
in the trace functionals — the conditions
(a) trace property, (b) Markov property at parameter $z$,
(c) consistency across the tower
$H_n \hookrightarrow H_{n+1}$
together cut out a one-parameter family parameterised by $z$
([volume normalisation](#thm:jones-markov-trace)).  The
normalisation $\mathrm{tr}_M(1) = 1$ pins the scale.

*Step 4 (Wenzl bridge supplies the closed form).*  The
$g$-convention isomorphism $g_i := q \sigma_i$ transports
$\mathrm{tr}_M$ on $\sigma$-Hecke (with the present $z$) to
$\mathrm{tr}_{\mathrm{GL}}$ on $g$-Hecke (with
$z_{\mathrm{GL}} = q \cdot z$).  By Wenzl 1988, the Markov trace
on $g$-Hecke at $z_{\mathrm{GL}} = Q^r(1 - Q)/(1 - Q^r)$ has
weights $\omega_\lambda(Q) = s_{\lambda, r}(Q)$ given by the
principal Schur specialisation, where $Q = q^2$.  Combining Steps
1--3 with this formula yields the Wenzl-bridge closed form
([prop:y-lambda-closed-form-wenzl-bridge](#prop:y-lambda-closed-form-wenzl-bridge)):

$$
  y_\lambda \;=\;
  \frac{s_\lambda(1, Q, Q^2, \ldots, Q^{r - 1})}
       {\sum_{\mu \,\vdash\, n} d_\mu \cdot s_\mu(1, Q, Q^2, \ldots, Q^{r - 1})}.
$$

The trace is *forced*, not assumed: every step is dictated by the
QOU substrate axioms plus the Chlouveraki HDR uniqueness theorem.
$\square$

## Satisfaction of the hypotheses by the QOU substrate

| Hypothesis                                                            | QOU realisation                                                                                                                   |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Rigid :refterm[braided monoidal category]{#braided-monoidal-category} | $\mathbf{C}$ as the [rigid :refterm[braided monoidal category]{#braided-monoidal-category}](#def:rigid-monoidal-category) of QOU |
| Self-dual fundamental object                                          | $A$ as the [fundamental confined particle](#def:confined-particle), self-dual via $A^* \cong A$ from the antipode                |
| Fibre functor                                                         | [$\tau \colon \mathbf{C} \to R\text{-mod}$](#prop:fibre-functor-atlas) realising the state bundle                                |
| Tannaka--Krein Hopf algebra                                           | $H = U_q(\mathfrak{sl}_2)$ in the running QOU example                                                                             |
| $V = \tau(A)$ has $q$-dimension $[2]_q^{\mathrm{symm}}$               | direct from $A$ being the spin-$\tfrac{1}{2}$ representation                                                                      |
