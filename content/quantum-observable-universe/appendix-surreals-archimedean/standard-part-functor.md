The standard-part map realizes the quotient $\mathbf{No}_{\mathrm{fin}}
/ \mathbf{No}_{\mathrm{inf}} \cong \mathbb{R}$ and underlies the
classical limit at $q = 1 + \varepsilon$; its construction begins with
the finite and infinitesimal surreals.

An element $x \in \mathbf{No}$ is **finite** if there exists
$n \in \mathbb{N}$ with $|x| \leq n$. Write $\mathbf{No}_{\mathrm{fin}}
\subset \mathbf{No}$ for the subring of finite surreals, and
$\mathbf{No}_{\mathrm{inf}} \subset \mathbf{No}_{\mathrm{fin}}$ for the
ideal of infinitesimals (those $x$ with $|x| < 1/n$ for every $n \in
\mathbb{N}$).

## Definition

The **standard-part map**

$$
  \mathrm{st} : \mathbf{No}_{\mathrm{fin}} \to \mathbb{R}
$$

sends each finite surreal $x$ to the unique real $r \in \mathbb{R}$
with $x - r \in \mathbf{No}_{\mathrm{inf}}$. Classically
[@robinson1966; @alling1987]:

$$
  \mathrm{st}(x) =
  \sup\{q \in \mathbb{Q} : q \leq x\}
  = \inf\{q \in \mathbb{Q} : q \geq x\}.
$$

The map $\mathrm{st}$ is a surjective ring homomorphism with kernel
$\mathbf{No}_{\mathrm{inf}}$, inducing a ring isomorphism

$$
  \mathbf{No}_{\mathrm{fin}} / \mathbf{No}_{\mathrm{inf}}
  \xrightarrow{\sim} \mathbb{R}.
$$

## Functorial extension

For a $K$-linear category $\mathbf{C}$ equipped with a
[birthday grading](#def:birthday-grading), define the **standard-
part functor**

$$
  \mathrm{St} : \mathbf{C}_{\leq \omega + 1}^{\mathrm{fin}}
   \longrightarrow \mathbf{C}_{\mathbb{R}}
$$

from the finite-coefficient sub-category at birthday $\leq \omega + 1$
to the archimedean sub-category. On objects it is the identity; on
morphisms it applies $\mathrm{st}$ entrywise to the matrix
representation of $f$ in any Hoefsmit-type basis.

Concretely, if $f \in \mathrm{Hom}_{\mathbf{C}}(X, Y)$ has matrix
entries $f_{ij} = r_{ij} + \varepsilon \cdot s_{ij} + O(\varepsilon^2)$
with $r_{ij}, s_{ij} \in \mathbb{R}$, then $\mathrm{St}(f)_{ij} =
r_{ij}$.

### Key properties

1. **$K$-linear**: $\mathrm{St}(af + bg) = \mathrm{st}(a)\mathrm{St}(f)
   + \mathrm{st}(b)\mathrm{St}(g)$ for $a, b \in K_{\mathrm{fin}}$.
2. **Monoidal**: $\mathrm{St}(f \otimes g) = \mathrm{St}(f) \otimes
   \mathrm{St}(g)$ on finite-coefficient morphisms.
3. **Right inverse to inclusion**: $\mathrm{St} \circ \iota_{\mathbb{R}
   \hookrightarrow K} = \mathrm{id}_{\mathbf{C}_{\mathbb{R}}}$.
4. **Classical limit = $\mathrm{St} \circ$ evaluation at
   $q = 1 + \varepsilon$** (see
   [classical limit as standard-part](#conj:classical-limit-stpart)).
