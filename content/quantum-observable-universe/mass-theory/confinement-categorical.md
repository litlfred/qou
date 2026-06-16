**Proposition (confinement = spectral-sequence collapse).**
*The collapse of the GB-filtration spectral sequence
([spectral sequence collapse](#prop:spectral-sequence-collapse))
is the categorical statement of color confinement: only central
elements of $A = H_n(R, q)$ survive as physical observables, and
"colored" non-central elements are cohomologically trivial.*

**Statement.**
*Let $A = H_n(R, q)$ be semisimple at generic $q$, with Frobenius
integral $\int_A : A \to R$ (the Markov trace).  Then:*

1. *(Survival.)
   The only $E_\infty$-page contributions are
   $E_\infty^{0, 0} = Z(A) = \bigoplus_\lambda R \cdot e_\lambda$.
   Non-central elements vanish on the $E_\infty$-page.*

2. *(Trace factorization.)
   The Frobenius integral factors through the centre:*

   $$
     \int_A \;=\; \mu \,\circ\, \pi_Z, \qquad
     \pi_Z : A \twoheadrightarrow Z(A), \quad
     \mu : Z(A) \to R,
   $$

   *with $\pi_Z(a) = \sum_\lambda e_\lambda \cdot a \cdot e_\lambda$
   the Wedderburn projection and $\mu(e_\lambda) = w_\lambda$ the
   Plancherel weight.*

3. *(Observables are Wedderburn residues.)
   Every physical observable
   $\mathfrak{W}(\mathcal{K}, \mathcal{T}) = \int_A \rho(\beta_\mathcal{K}) \cdot \mathcal{T}$
   factors as a sum of Wedderburn residues
   ([universal residue](#prop:plancherel-term-7-formulation)):*

   $$
     \mathfrak{W}(\mathcal{K}, \mathcal{T})
     \;=\; \sum_\lambda \int_{A_\lambda}\!\!\rho(\beta_\mathcal{K}) \cdot \mathcal{T}.
   $$

*Proof.*

$(1)$ is [spectral sequence collapse](#prop:spectral-sequence-collapse):
$\mathrm{HH}^k(A) = 0$ for $k \geq 1$ (Whitehead's lemma for
semisimple algebras), so $E_\infty^{p, q} = 0$ for $p + q \geq 1$.
Only $E_\infty^{0, 0} = \mathrm{HH}^0 = Z(A)$ remains.

$(2)$ Cyclicity of the Markov trace ($\int_A ab = \int_A ba$) means
$\int_A$ vanishes on commutators $[A, A]$.  Since $A / [A, A] \cong
Z(A)$ at the $\mathrm{HH}^0$-level, $\int_A$ descends to
$Z(A)$.  The induced map
$\mu : Z(A) \to R$ sends $e_\lambda \mapsto \int_A e_\lambda =
w_\lambda$.

$(3)$ Wedderburn decomposition $A = \bigoplus_\lambda A_\lambda$ with
$A_\lambda = e_\lambda A e_\lambda$ gives
$\int_A a = \sum_\lambda \int_{A_\lambda} a$ for any $a \in A$.
Apply with $a = \rho(\beta_\mathcal{K}) \cdot \mathcal{T}$. $\square$

**Confinement reading.**

*Each clause is the categorical reflection of a confinement statement
in QCD:*

| Clause | Algebra | QCD analogue |
|---|---|---|
| (1) | Non-central elements die at $E_\infty$ | Free quarks not observed |
| (2) | $\int_A$ factors through $Z(A)$ | All observables are gauge-invariant |
| (3) | Observables = sum of Wedderburn residues | Hadrons = sum of color-singlet projections |

*The curvature 2-cocycle $F$ encoding the Hecke + Yang–Baxter
relations
([curvature-rank stratification](#prop:curvature-rank-gb-stratification))
plays the role of the **string tension** categorically: $F$ is the
obstruction to extracting a non-central element through the GB
filtration, just as the QCD string tension is the obstruction to
extracting an isolated quark.*

**Curvature-rank as confinement layer.**

*The strata $J^k / J^{k+1}$ index "confinement layers": deeper $k$ =
more commutator load = harder to extract.  At $k = 0$ (the centre)
elements are completely free; at $k \geq 1$ extraction requires
energy proportional to $F$.  The chirality channel $D_q^2 = 0$
([q-Dirac cell scanner witness](#)) supplies the persistent
gauge-invariant background analogous to the gluon condensate, with
$\mathrm{Vol}(B_3) = 8 G$ matching $\dim \mathfrak{su}(3) = 8$.*

**Predictive consequence.**

*The hadron mass formula
([unified mass formula](#prop:unified-curvature-rank-mass-formula))
$\mathfrak{m}_{q,\mathcal{K}} = \sum_k \alpha_k \cdot
\mathfrak{m}^{(k)}_{q,\mathcal{K}}(1)$
is — read through this proposition — literally a sum over confinement
layers.  Term $k$ of the formula is the contribution of the
curvature-rank-$k$ confinement stratum.  The rank-3 chirality residue
($\mathrm{Vol}(6_1) \cdot |(q;q)_3|$) and the rank-$\geq 4$ universal
Pochhammer tail in the structural $\mathfrak{Q}_\beta$ derivation
([Q-beta path A extended witness](#)) are confinement residues, not
independent ingredients.*
