**Conjecture.**
*For each mass number $A = Z + N$, the experimentally observed stable isotope $(Z_*, N_*)$ is the unique minimizer of the demand magnitude:*

$$
  (Z_*, N_*)
  =
  \arg\min_{Z + N = A}
  |\mathrm{dem}(\mathcal{A}(Z, N))|
$$

*where $\mathcal{A}(Z, N)$ is the derived atom ([derived atom](#def:derived-atom)) and $|\mathrm{dem}|$ is the demand magnitude ([demand stability](#prop:demand-stability)).*

## Formal statement

Let $\mathcal{V} \subset \mathbb{Z}_{\geq 0}^2$ be the set of pairs $(Z, N)$ such that $\mathcal{A}(Z, N)$ minimizes demand at fixed $A$:

$$
  \mathcal{V}
  =
  \left\{
    (Z, N) \in \mathbb{Z}_{\geq 0}^2
    :
    |\mathrm{dem}(\mathcal{A}(Z, N))|
    \leq
    |\mathrm{dem}(\mathcal{A}(Z', N'))|
    \text{ for all } Z' + N' = Z + N
  \right\}.
$$

**Conjecture.** *$\mathcal{V}$ coincides with the experimentally observed valley of stability for all $A \leq 238$.*

## Subsidiary conjectures

**(i) Magic numbers from demand closure.**
*The nuclear magic numbers $\{2, 8, 20, 28, 50, 82, 126\}$ are the values of $Z$ (or $N$) at which the nucleus $\mathcal{N}(Z, N)$ achieves demand closure $\mathrm{dem}(\mathcal{N}) = \varnothing$ for at least one value of the complementary quantum number.*

**(ii) Shell closure from electron demand.**
*The atomic noble gases ($Z = 2, 10, 18, 36, 54, 86$) are the values of $Z$ at which the atom $\mathcal{A}(Z, N_*)$ achieves $\mathrm{dem}(\mathcal{A}) = \varnothing$ for the most abundant stable isotope $N_*$.*

**(iii) Drip lines from demand divergence.**
*The proton (neutron) drip line is the locus in $(Z, N)$-space where $|\mathrm{dem}(\mathcal{N}(Z, N))| \to \infty$ under the addition of one proton (neutron): beyond this line, the Gröbner--Shirshov reduction fails to produce a finite-demand normal form.*

## Inductive verification

Inductive Gröbner--Shirshov reduction ([derived atom](#def:derived-atom)) tests this conjecture computationally. For each $A$:

1. Compute $\mathcal{A}(Z, A - Z)$ for all $0 \leq Z \leq A$.
2. Evaluate $|\mathrm{dem}|$ for each.
3. Check that the minimizer matches the known stable isotope(s).

The inductive reduction ensures polynomial scaling. Each new nucleon multiplies a bounded-size normal form element by a typed crossing and reduces. For $A \leq 12$, this is computationally tractable. For $A > 12$, the transfer matrix identities $C_{pp}^2 = h_{\mathrm{A}} C_{pp} + \mathbf{1}$ and $C_{nn}^2 = h_{\mathrm{A}} C_{nn} + \mathbf{1}$ compress the calculation.

## Predicted vs observed for $A \leq 4$

| $A$ | Predicted $(Z_*, N_*)$ | Observed | $|\mathrm{dem}_*|$ |
|:---:|:---|:---|---:|
| $1$ | $(1, 0)$ | ${}^1\mathrm{H}$ | $0.024$ |
| $2$ | $(1, 1)$ | ${}^2\mathrm{H}$ | $0.058$ |
| $3$ | $(2, 1)$ | ${}^3\mathrm{He}$ | $0.000$ |
| $4$ | $(2, 2)$ | ${}^4\mathrm{He}$ | $0.098$ |

He-3 achieves exact demand closure ($|\mathrm{dem}| = 0$). He-4 has nonzero demand but minimal Markov trace. The doubly magic stability of He-4 arises from action minimization, not demand closure.
