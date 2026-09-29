Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe. Every connection $\nabla$ that is a critical point of the categorical Yang--Mills functional

$$
  S[\nabla] =  \int_A\!\bigl(\star_q(F_\nabla) \cdot F_\nabla\bigr)
$$

is an instanton.

The argument is the Bogomolny decomposition, given in the proof below. The
Lean backing `QOU.categorical_self_duality` does **not** carry it: it is a
structural accessor for the `self_dual` field of `CategoricalInstanton`, so it
records that an object of that structure satisfies the condition the structure
imposes, not that a critical point of $S[\nabla]$ is such an object. The
implication above is established in narrative here and is not formalised.

