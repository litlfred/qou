Every nucleus $\mathcal{N}(Z, N)$ corresponds to a braid word in $B_A$; Gröbner--Shirshov reduction in $H_A(q)$ produces a unique normal form representing the lowest-energy state.

**Proposition.**
Let $R = \mathbb{Z}[q, q^{-1}]$, with $q$ a categorical invariant rather than a free parameter. The Iwahori--Hecke algebra $H_A(q) = R[B_A] / I$ is presented by the three defining relation families

$$
  G_0 = \bigl\{\, \sigma_i^2 - (q - q^{-1})\sigma_i - 1, \;\;
  \sigma_{i+1}\sigma_i\sigma_{i+1} - \sigma_i\sigma_{i+1}\sigma_i, \;\;
  \sigma_i\sigma_j - \sigma_j\sigma_i \ (i \geq j + 2) \,\bigr\}
$$

(the Hecke relation, the Yang--Baxter braid relation, and far commutativity, oriented in the shortlex-decreasing direction). For $A \leq 3$, $G_0$ is already a complete Gröbner--Shirshov basis; for $A \geq 4$, completing $G_0$ with the $q$-free Bokut--Shiao braid family $\sigma_i\sigma_{i-1}\cdots\sigma_j\sigma_i \to \sigma_{i-1}\sigma_i\sigma_{i-1}\cdots\sigma_j$ ($j \leq i - 1$, subsuming the Yang--Baxter rule at $j = i - 1$; [Hecke normal form](#def:hecke-normal-form)) yields the confluent Gröbner--Shirshov basis $G$ for $I$. The division algorithm computes the remainder with respect to $G$, yielding the unique, path-independent normal form

$$
  \mathcal{N}(Z, N)
   := 
  r\bigl(\mathcal{N}_{\mathrm{raw}}(Z, N), G\bigr)
   \in  H_A(q).
$$

By convention, $\mathcal{N}(Z, N)$ denotes the reduced normal form unless explicitly stated.

**The nuclear braid word.**
The unreduced braid word is

$$
  \mathcal{N}(Z, N)
  = 
  \prod_{1 \leq i < j \leq A}
  \sigma_{i}^{\epsilon(i, j)}
$$

where the crossing sign $\epsilon(i, j)$ depends on nucleon types: $+1$ (protons), $-1$ (neutrons), $0$ (mixed, resolved as $\tfrac{1}{2}(\sigma_i + \sigma_i^{-1})$). Because the factors are grouped in increasing generator blocks $i = 1, \ldots, A - 1$, intra-block Hecke reductions alone collapse each block to a linear factor $a_i\,\sigma_i + b_i$, and the resulting subset expansion consists exclusively of strictly increasing generator chains $\sigma_S$ that are already irreducible under all of $G$ with zero braid, Bokut--Shiao, or far-commutativity steps ([Hecke-only reduction of the nucleus element](#prop:tm-gs-normal-form)).
