Continuing the
[substrate parameter for SU(2)](#ex:substrate-parameter-su2),
we execute the
[Tannaka--Krein reconstruction](#thm:tannaka-krein-isomorphism)
algorithm concretely — replacing "the reconstruction theorem
guarantees $\mathcal{H}_\xi$ is uniquely determined" with an explicit
computation.

**Step 1: the :refterm[monoidal category]{#monoidal-category}.** Start with
$\mathbf{C} = \mathrm{Rep}(\mathrm{SU}_q(2))$ and the forgetful
(fibre) functor $\tau \colon \mathbf{C} \to \mathrm{Vect}_\mathbb{C}$.
The simple objects are $V_0, V_{1/2}, V_1, V_{3/2}, \ldots$ with
$\dim V_j = 2j + 1$.

**Step 2: compute the coend.** The reconstructed Hopf algebra is
$H = \mathrm{coend}(\tau^\vee \otimes \tau)$, concretely:

$$
  H = \bigoplus_{j \in \frac{1}{2}\mathbb{Z}_{\geq 0}}
      V_j^* \otimes V_j
  \bigg/ \sim,
$$

where $\sim$ identifies $(\tau(f)^* \otimes \mathrm{id})$ with
$(\mathrm{id} \otimes \tau(f))$ for all morphisms $f$. The matrix
coefficients $t^j_{m,m'} \in V_j^* \otimes V_j$ form a basis.

**Step 3: reconstruct the algebra structure.** Multiplication
on $H$ comes from the tensor product in $\mathbf{C}$. For the
fundamental representation $V = V_{1/2}$, the four matrix
coefficients $\alpha, \beta, \bar\alpha, \bar\beta$ (entries of the
$2 \times 2$ matrix) generate $H$. The relations are read off from
the $R$-matrix:

$$
  \alpha\beta = q\,\beta\alpha, \quad
  \alpha\bar\alpha = q\,\bar\alpha\alpha, \quad
  \beta\bar\beta = \bar\beta\beta, \quad
  \alpha\bar\beta - \bar\beta\alpha = (q - q^{-1})\,\beta\bar\alpha,
$$

together with the quantum determinant
$\alpha\bar\beta - q\,\beta\bar\alpha = 1$.

**Step 4: reconstruct the coalgebra.** The comultiplication
comes from the monoidal structure:
$\Delta(t^j_{m,m'}) = \sum_{k} t^j_{m,k} \otimes t^j_{k,m'}$.
On the generators:

$$
  \Delta\begin{pmatrix} \alpha & \beta \\ \bar\alpha & \bar\beta \end{pmatrix}
  = \begin{pmatrix} \alpha & \beta \\ \bar\alpha & \bar\beta \end{pmatrix}
    \otimes
    \begin{pmatrix} \alpha & \beta \\ \bar\alpha & \bar\beta \end{pmatrix}.
$$

The counit is $\varepsilon(t^j_{m,m'}) = \delta_{mm'}$ and the
antipode is $S(\alpha) = \bar\beta$, $S(\beta) = -q^{-1}\beta$,
$S(\bar\alpha) = -q\bar\alpha$, $S(\bar\beta) = \alpha$.
(Equivalently, $S(u) = u^{-1}$ where
$u = \bigl(\begin{smallmatrix} \alpha & \beta \\
\bar\alpha & \bar\beta \end{smallmatrix}\bigr)$
and the inverse uses the quantum determinant.)

**Result.** The output of the algorithm is
$H \cong \mathcal{O}_q(\mathrm{SU}(2))$ — the quantum coordinate
ring, recovered entirely from the monoidal structure of its
representation category. Every step is a finite computation: form the
coend, read off generators from the fundamental representation, and
extract relations from the $R$-matrix.

**Bring's surface specialisation.** On Bring's QOU, $q$ takes the
value determined by the Descartes condition
([constructive extraction of $q$](#ex:substrate-parameter-brings)),
and the reconstruction yields
$\mathcal{O}_{q_{\mathrm{Bring}}}(\mathrm{SU}(2))$ equipped with
its $S_5$-equivariant structure. The Reeb spectrum
([constructive Reeb derivation](#ex:categorical-reeb-brings)) is
automatically encoded in the weight spaces of $H$.
