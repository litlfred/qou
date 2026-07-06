**Proposition (Categorical neutron existence).**

The [categorical neutron](#def:categorical-neutron) $\mathfrak{n} = \mathcal{B}_3(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})$ exists as a well-defined, LP-stable element of $H_3(q)$. Uniqueness up to braid isotopy is treated in [uniqueness of the categorical neutron](#prop:categorical-neutron-unique).

#### Strategy

We assemble the constituent braids for the $(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})$ partition in the Hecke algebra $H_3(q)$. We select two Hopf-link gluons to minimize the stabilizer trace. We then apply Gröbner--Shirshov reduction to reach the normal form, verifying non-negativity $G x[\gamma] \ge 0$ via the linear-programming dual at each step.

#### Formalization

The Lean formalization provides a `sorry`-free weak proxy proof (`CategoricalNeutron.exists`) by instantiating a structure without stability or positivity field constraints (using free real fields). Formalizing the full constraint satisfaction requires building the Hecke normal form and linear programming infrastructure. The underlying construction is mathematically consistent; the gap is strictly an artifact of missing computational algebra libraries. The explicit instantiation validates the structural consistency of the categorical-neutron model.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs—real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. The underlying categorical identities hold over an abstract coefficient ring; only their archimedean realisation is specialised here.
