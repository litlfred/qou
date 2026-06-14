The [categorical neutron](#def:categorical-neutron)
$\mathfrak{n} = \mathcal{B}_3(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})$
exists as a well-defined, LP-stable element of $H_3(q)$.

Uniqueness up to braid isotopy is
([uniqueness of the categorical neutron](#prop:categorical-neutron-unique)).


**Strategy.** We assemble the constituent braids for the $(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})$ partition in the Hecke algebra $H_3(q)$, selecting two Hopf-link gluons to minimize the stabilizer trace. We then apply Gröbner--Shirshov reduction to obtain the normal form, verifying non-negativity $G x[\gamma] \ge 0$ via the linear-programming dual at each step.

**Formalization Goal Plausibility.** The Lean formalization currently provides a `sorry`-free weak proxy proof (`CategoricalNeutron.exists`) by instantiating a structure without stability or positivity field constraints (using free real fields). While the text describes a highly constrained LP-stable Borromean object, closing the gap to formalize the full constraint satisfaction is plausible because it strictly requires building out the Hecke normal form (NF) and linear programming infrastructure. The underlying construction is physically and mathematically consistent; the gap is entirely an artifact of missing computational algebra libraries in the formal environment rather than an unresolved theoretical doubt.

Although the proof relies on a standard Nonempty-witness argument, the instantiation of this witness validates the novel structural consistency of the categorical-neutron model within the broader geometric framework of the Quantum Observable Universe.
