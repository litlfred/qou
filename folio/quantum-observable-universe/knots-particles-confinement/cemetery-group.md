**Definition.**
*Let $H_n(R, q)$ be the Iwahori–Hecke algebra and let $\mathcal{K}_n$ denote the category of finitely generated graded projective modules over the Khovanov–Lauda–Rouquier algebra whose cyclotomic quotient is $H_n(R, q)$. The fibre functor $\tau \colon \mathcal{K}_n \to \mathrm{Vect}$ acts as decategorification by graded Euler characteristic. For a graded module $M = \bigoplus_{d \in \mathbb{Z}} M_d$,*

$$
  \tau(M) \;:=\; \sum_{d \in \mathbb{Z}} (-1)^d \dim_R M_d \;\in\; R.
$$

*The :defterm[cemetery group]{#cemetery-group} of $H_n(R, q)$ is the localising Serre subcategory*

$$
  \mathcal{Z}_n \;:=\; \ker \tau
  \;=\; \{\, M \in \mathcal{K}_n : \tau(M) = 0 \,\}.
$$

*Its objects are the homologically acyclic complexes. Physically, these are the decoupled or non-observable interaction channels.*

**Remark.**
*The cemetery group is emergent. It is defined as the kernel of $\tau$ rather than postulated. One uses $\mathcal{Z}_n$ computationally as a homological filter on crystal-graph traversals.*
