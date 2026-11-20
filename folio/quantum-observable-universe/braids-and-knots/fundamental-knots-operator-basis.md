The framework's particle catalogue and operator algebra share a single six-element basis. Fundamentally, each particle is a knot or link on Bring's surface. Interaction operators form the six-dimensional Iwahori--Hecke algebra $H_3(q)$.

| Particle | Knot / link | Type | Braid word | $q$-invariant |
|---|---|---|---|---|
| neutrino $\nu$ | unknot $0_1$ | trivial | $\mathbf{1}$ | $\mathrm{Vol}=0$, $J=1$ |
| electron $e^-$ | trefoil $3_1 = T(2,3)$ | torus | $\sigma_1^3$ | $\mathrm{Vol}=0$ |
| strong force | Hopf link $L2a1 = T(2,2)$ | torus | $\sigma_1^2$ | $\mathrm{Vol}=0$ |
| Higgs $h$ | figure-eight $4_1$ | hyperbolic | $(\sigma_1\sigma_2^{-1})^2$ | $\mathrm{Vol}\approx 2.0299$ |
| nucleon $\mathfrak{p},\mathfrak{n}$ | Borromean rings $L6a4$ | hyperbolic | $(\sigma_1\sigma_2^{-1})^3$ | $\mathrm{Vol}\approx 7.328 = 8G$ |
| photon $\gamma$ | — (not a knot) | Hecke element | $\mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1^{-1}$ | $J=1$ (bare) |

Torus knots carry zero hyperbolic volume, representing the massless, force-carrying sector. Hyperbolic knots carry positive volume, which translates to mass via $\mathrm{Vol}(K)/\hbar_q^{2}$. The photon is not a knot but a four-term element of $H_3(q)$ whose products generate the rest of the spectrum.

The six Gröbner--Shirshov normal-form words span $H_3(q)$:

| Operator | Braid word | Permutation | $\mathrm{tr}_M$ at $q_0$ |
|---|---|---|---|
| $\gamma$ (identity) | $\varnothing$ | $e$ | $1.000$ |
| $\sigma_0$ | $(0)$ | $(1\;2)$ | $0.613$ |
| $\sigma_1$ | $(1)$ | $(2\;3)$ | $0.613$ |
| $L_+$ | $(0,1)$ | $(1\;2\;3)$ | $0.375$ |
| $L_-$ | $(1,0)$ | $(1\;3\;2)$ | $0.375$ |
| $e^-$ | $(0,1,0)$ | $(1\;3)$ | $0.691$ |

These basis operators are algebraically distinct from the topological knots sharing their names. Their Markov traces at the substrate parameter $q_0$ provide the weights used for mass and binding computations. The column is evaluated in the canonical **convention D**, $z_D = q^3/(q^2+1)$ ([notation register](../notation/notation-register-table3-data.md)): $\mathrm{tr}_M(\sigma_i) = z$, $\mathrm{tr}_M(L_\pm) = z^2$, and $\mathrm{tr}_M(e^-) = z + (q - q^{-1})z^2$.
