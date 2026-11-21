*Proof.* Transport everything along the Wedderburn isomorphism
$\Phi : A \xrightarrow{\sim} \prod_\lambda \mathrm{Mat}_{f^\lambda}(K)$,
which holds because $q$ is not a root of unity. Write $x_\lambda$ for the
$\lambda$-block of $\Phi(x)$, so $\mathrm{tr}(\rho_\lambda x) =
\mathrm{tr}(x_\lambda)$, and $\pi_Z(x) = \Phi^{-1}\bigl((\mathrm{tr}(x_\lambda)/f^\lambda)\,
1_\lambda\bigr)_\lambda$ as in the statement. This uses $f^\lambda \neq 0$ in $K$.

$(1)$ Each block of $\Phi(\pi_Z(x))$ is a scalar matrix, and scalar
matrices commute with everything in their block, so $\Phi(\pi_Z(x))$ is
central in the product and $\pi_Z(x) \in Z(A)$. It equals
$\sum_\lambda (\mathrm{tr}(x_\lambda)/f^\lambda)\, e_\lambda$.

$(2)$ A trace on a matrix algebra $\mathrm{Mat}_f(K)$ is a scalar multiple
of $\mathrm{tr}$, because it vanishes on commutators and the commutators
together with one diagonal unit span. Hence $\tau \circ \Phi^{-1}$ is a sum
of block traces $\sum_\lambda c_\lambda\, \mathrm{tr}(x_\lambda)$, and
evaluating at $e_\lambda$ gives $c_\lambda f^\lambda = \tau(e_\lambda) =
\mu_\lambda$. So
$\tau(x) = \sum_\lambda \mu_\lambda\, \mathrm{tr}(x_\lambda)/f^\lambda$.
The same formula applied to $\pi_Z(x)$, whose $\lambda$-block has trace
$\mathrm{tr}(x_\lambda)$, gives $\tau(\pi_Z(x)) = \tau(x)$.

$(3)$ If $x$ is central, each $x_\lambda$ commutes with all of
$\mathrm{Mat}_{f^\lambda}(K)$ and is therefore a scalar $s_\lambda\, 1$.
Then $\mathrm{tr}(x_\lambda)/f^\lambda = s_\lambda$ and $\pi_Z(x) = x$. $\square$

The Lean `confinement_categorical` follows exactly this route
(`trace_unique`, `eq_scalar_of_commute`, `centreProj_central`,
`trace_eq_residue_sum`). Reading $Z(A)$ as the $E_\infty^{0,0}$ page of
the GB-filtration spectral sequence additionally uses
$\mathrm{HH}^k(A) = 0$ for $k \geq 1$
([spectral sequence collapse](#prop:spectral-sequence-collapse)); that
reading is not part of the proof.

**Confinement reading.**

*Each clause is the categorical reflection of a confinement statement
in QCD:*

| Clause | Algebra | QCD analogue |
|---|---|---|
| (1) | $\pi_Z$ sends every element into the centre $Z(A)$ | Free quarks not observed |
| (2) | every trace $\tau$ factors through $\pi_Z$ | All observables are gauge-invariant |
| (3) | Observables = sum of Wedderburn residues | Hadrons = sum of color-singlet projections |

*The curvature 2-cocycle $F$ encoding the Hecke + Yang–Baxter
relations
([curvature-rank stratification](#conj:curvature-rank-gb-stratification))
plays the role of the **string tension** categorically: $F$ is the
obstruction to extracting a non-central element through the GB
filtration, just as the QCD string tension is the obstruction to
extracting an isolated quark.*

**Curvature-rank as confinement layer.**

*The strata $J^k / J^{k+1}$ index "confinement layers": deeper $k$ =
more commutator load = harder to extract.  At $k = 0$ (the centre)
elements carry no commutator load; at $k \geq 1$ extraction requires
energy proportional to $F$.  The chirality channel $D_q^2 = 0$
(q-Dirac cell scanner witness) supplies the persistent
gauge-invariant background analogous to the gluon condensate, with
$\mathrm{Vol}(B_3) = 8 G$ matching $\dim \mathfrak{su}(3) = 8$.*

**Predictive consequence.**

*The hadron mass formula
([unified mass formula](#prop:unified-curvature-rank-mass-formula))
$\mathfrak{m}_{q,\mathcal{K}} = \sum_k \alpha_k \cdot
\mathfrak{m}^{(k)}_{q,\mathcal{K}}(1)$
is, read through this proposition, a sum over confinement
layers.  Term $k$ of the formula is the contribution of the
curvature-rank-$k$ confinement stratum.  The rank-3 chirality residue
($\mathrm{Vol}(6_1) \cdot |(q;q)_3|$) and the rank-$\geq 4$ universal
Pochhammer tail in the structural $\mathfrak{Q}_\beta$ derivation
(Q-beta path A extended witness) are confinement residues, not
independent ingredients.*
