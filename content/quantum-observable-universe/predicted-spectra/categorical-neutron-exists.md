The [categorical neutron](#def:categorical-neutron) $\mathfrak{n} = \mathcal{B}_3(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})$ exists as a well-defined, LP-stable element of $H_3(q)$.

#### Strategy

The $(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})$ partition assembles the constituent braids in the Hecke algebra $H_3(q)$. Two Hopf-link gluons minimize the stabilizer trace. Gröbner--Shirshov reduction reaches the normal form. The linear-programming dual verifies non-negativity $G x[\gamma] \ge 0$ at each step.

#### Formalization

The Lean formalization provides a `sorry`-free weak proxy proof (`CategoricalNeutron.exists`). It instantiates a structure without stability or positivity field constraints using free real fields. Full constraint satisfaction requires Hecke normal form and linear programming infrastructure. The underlying construction remains mathematically consistent. Missing computational algebra libraries cause the gap. Explicit instantiation validates the structural consistency of the categorical-neutron model.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. The categorical identities hold over an abstract coefficient ring. Only the archimedean realization requires specialization.
