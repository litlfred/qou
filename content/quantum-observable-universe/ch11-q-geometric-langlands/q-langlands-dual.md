Let $G_q$ be the quantum gauge group of a QOU
(Definition \ref{def:quantum-gauge-group}).  The **$q$-Langlands dual
group** $\check{G}_q$ is the quantum group whose representation
category is related to $G_q$ by root system duality:

$$
  \check{G}_q = G_{q^{-1}}^{\vee},
$$

where $(-)^\vee$ denotes the classical Langlands dual (interchange of
roots and coroots) and the substrate parameter is inverted $q \mapsto
q^{-1}$.

Concretely, for the QOU gauge group $G_q = \mathrm{SU}_q(2)$
(Definition \ref{def:quantum-su2}):

$$
  \check{G}_q = \mathrm{SU}_{q^{-1}}(2) \cong \mathrm{SO}_{q^{-1}}(3),
$$

since $\mathrm{SU}(2)$ is self-dual at the level of root systems and
the Langlands involution acts by $q \mapsto q^{-1}$ on the quantum
parameter.

The inversion $q \mapsto q^{-1}$ interchanges the two eigenvalues of
the braiding: $q \leftrightarrow -q^{-1}$.  This exchanges the
symmetric and antisymmetric channels of the Hecke algebra, which is
the categorical manifestation of the exchange of roots and coroots.
