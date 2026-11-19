An element $x \in \mathbf{No}$ is **finite** if there exists
$n \in \mathbb{N}$ with $|x| \leq n$, and **infinitesimal** if
$|x| < 1/n$ for every $n \in \mathbb{N}$. Write $\mathbf{No}_{\mathrm{fin}}$
for the subring of finite surreals and $\mathbf{No}_{\mathrm{inf}}$ for the
ideal of infinitesimals.

The **standard-part map**

$$
  \mathrm{st} : \mathbf{No}_{\mathrm{fin}} \to \mathbb{R}
$$

sends each finite surreal $x$ to the unique real $r \in \mathbb{R}$
with $x - r \in \mathbf{No}_{\mathrm{inf}}$.

For a $K$-linear category $\mathbf{C}$ equipped with a
[birthday grading](#def:birthday-grading), the **standard-part functor**

$$
  \mathrm{St} : \mathbf{C}_{\leq \omega + 1}^{\mathrm{fin}}
   \longrightarrow \mathbf{C}_{\mathbb{R}}
$$

from the finite-coefficient sub-category at birthday $\leq \omega + 1$
to the archimedean sub-category is the identity on objects and, on
morphisms, applies $\mathrm{st}$ entrywise to the matrix
representation of $f$ in any Hoefsmit-type basis.
