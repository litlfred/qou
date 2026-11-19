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
(q-Dirac cell scanner witness) supplies the persistent
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
(Q-beta path A extended witness) are confinement residues rather than
independent ingredients.*
