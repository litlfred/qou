**The fundamental knots and the operator basis.**

The framework's particle catalogue and its algebra share a single
six-element backbone.  On the knot side, each fundamental particle is a
knot or link embedded on Bring's surface; on the operator side, the
interactions form the six-dimensional Iwahori--Hecke algebra $H_3(q)$,
the image of the three-strand braid group.  The two tables below collect
the cast of characters that the rest of the paper computes with.

**The fundamental knot--particle dictionary.**

| Particle | Knot / link | Type | Braid word | $q$-invariant |
|---|---|---|---|---|
| neutrino $\nu$ | unknot $0_1$ | trivial | $\mathbf{1}$ | $\mathrm{Vol}=0$, $J=1$ |
| electron $e^-$ | trefoil $3_1 = T(2,3)$ | torus | $\sigma_1^3$ | $\mathrm{Vol}=0$ |
| strong force | Hopf link $L2a1 = T(2,2)$ | torus | $\sigma_1^2$ | $\mathrm{Vol}=0$ |
| Higgs $h$ | figure-eight $4_1$ | hyperbolic | $(\sigma_1\sigma_2^{-1})^2$ | $\mathrm{Vol}\approx 2.0299$ |
| nucleon $\mathfrak{p},\mathfrak{n}$ | Borromean rings $L6a4$ | hyperbolic | $(\sigma_1\sigma_2^{-1})^3$ | $\mathrm{Vol}\approx 7.328 = 8G$ |
| photon $\gamma$ | — (not a knot) | Hecke element | $\mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1$ | $J=1$ (bare) |

The torus knots carry zero hyperbolic volume — the massless,
force-carrying sector — while the hyperbolic knots carry positive
volume, which becomes mass through $\mathrm{Vol}(K)/\hbar_q^{2}$ (here
$G$ is Catalan's constant).  The photon is not a knot at all but the
four-term element of $H_3(q)$ whose two-photon products generate the
rest of the spectrum.

**The six-dimensional operator basis $H_3(q)$.**

| Operator | Braid word | Permutation | $\mathrm{tr}_M$ at $q_0$ |
|---|---|---|---|
| $\gamma$ (identity) | $\varnothing$ | $e$ | $1.000$ |
| $\sigma_0$ | $(0)$ | $(1\;2)$ | $0.499$ |
| $\sigma_1$ | $(1)$ | $(2\;3)$ | $0.499$ |
| $L_+$ | $(0,1)$ | $(1\;2\;3)$ | $0.249$ |
| $L_-$ | $(1,0)$ | $(1\;3\;2)$ | $0.249$ |
| $e^-$ | $(0,1,0)$ | $(1\;3)$ | $0.551$ |

These six Gröbner--Shirshov normal-form words span $H_3(q)$
($\dim = 3! = 6$), with the identity $\gamma$ among them — so the
catalogue of interactions is six-dimensional, not seven.  Their Markov
traces $\mathrm{tr}_M$ at the substrate value $q_0$ are the weights that
every mass and binding computation reads off.  These are the basis
*operators*; the particle assignments of the first table are a separate,
geometric identification (the basis operator $e^- = \sigma_0\sigma_1\sigma_0$
is the longest word, not the trefoil-electron of the dictionary above).
