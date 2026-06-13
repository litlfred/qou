**Conjecture (Shared-denominator cusp holonomy).**
*Let $T_w \in H_n(R, q)$ be a Hecke normal-form word at GB-depth
$k_\star(T_w) = n$, let $\Phi_n(x; q) = \prod_{k=0}^{n-1}(1 - x q^k)^{-1}$
be its $q$-Pochhammer partial product
([definition](#def:q-pochhammer-partial-product)),
and let $K_S$ be the $\Phi_q$-piece of the lifted braid
([Φ$_q$-piece](#def:phi-q-piece)). Then the roots of the
denominator polynomial*

$$
  (x; q)_n
  \;=\;
  \prod_{k=0}^{n-1}\bigl(1 - x q^k\bigr)
  \;\in\;
  \mathbb{Z}[q, x]
$$

*enforce the **cusp completeness conditions** of the Thurston
gluing equations on the ideal-tetrahedron triangulation of
$S^3 \setminus K_S$:*

$$
  (x; q_0)_n \;=\; 0
  \quad\Longleftrightarrow\quad
  \mathrm{Hol}_{\mu_k}(z_k) = 1
  \;\;\text{and}\;\;
  \mathrm{Hol}_{\lambda_k}(z_k) = 1
  \;\;\text{for some cusp}\;k,
$$

*where $z_k$ is the shape parameter of the ideal tetrahedron at
cusp $k$ and $\mu_k, \lambda_k$ are its meridian and longitude.*

## Algebraic poles as geometric addresses

The conjecture says the **algebraic denominator zeros are the
addresses of the geometric cusps**: a zero in the algebraic state
sum at $x = q_0^{-k}$ corresponds to the geometric requirement that
parallel transport around the meridian and longitude of the $k$-th
ideal-tetrahedron cusp yields a holonomy of exactly $1$. Algebraic
divergence and geometric completeness are the same event, viewed
from opposite sides of the Archimedean fibre functor $\tau$.

| Algebraic side ($R$) | Archimedean side ($\mathbb{C}$) | Geometric side ($\mathbf{Hyp}_3$) |
|---|---|---|
| zero of $(1 - x q_0^k)$ | logarithmic singularity of $\mathrm{Li}_2$ | meridian + longitude holonomy = $1$ |
| pole of $\Phi_n$ | branch point of $\log$ | complete cusp of $\Delta_{z_k}$ |
| algebraic Markov-trace divergence | $\tau_{\mathrm{arch}}$-evaluation diverges | shape parameter $z_k$ on Thurston variety |
| GB-depth $k_\star = n$ | thimble dimension $n$ | $n$ ideal tetrahedra in JSJ piece |

The bijection across rows is the **shared denominator**: the same
polynomial $(x; q_0)_n$ controls the algebraic singularities, the
classical $\mathrm{Li}_2$ branch structure, and the Thurston cusp
equations.

## Proof sketch (modulo the upstream conjectures)

Assume
([algebraic-geometric dilog equivalence](#conj:algebraic-geometric-dilog-equivalence))
and
([Archimedean limit](#conj:dilogarithm-archimedean-limit)).

1. **Algebraic side** ([q-Pochhammer partial product §interpretation](#def:q-pochhammer-partial-product)).
   The denominator $(x; q)_n$ has $n$ simple zeros at $x = q^{-k}$
   for $k = 0, \dots, n-1$. Each is a simple pole of $\Phi_n(x; q)$.

2. **Archimedean side** ([Archimedean limit](#conj:dilogarithm-archimedean-limit)).
   Under Faddeev's scaling, $(1 - q) \log \Phi_n(x; q) \to
   \mathrm{Li}_2(x)$. The poles of $\Phi_n$ map to the logarithmic
   branch point of $\mathrm{Li}_2$ at $t = 1$ in the integrand
   $-\log(1 - t)/t$.

3. **Geometric side** (Thurston [`thurston1978`], Neumann–Zagier
   [`neumann-zagier1985`]). For an ideal-tetrahedron triangulation of
   a hyperbolic 3-manifold, the **cusp completeness conditions** are
   $\mathrm{Hol}_\mu = \mathrm{Hol}_\lambda = 1$ on the meridian and
   longitude; equivalently, the Neumann–Zagier potential
   $\Phi_{\mathrm{NZ}}(z)$ has a critical point at $z = z_k$ matching
   the corresponding shape parameter.

4. **Bridge.** Under the
   [algebraic-geometric equivalence](#conj:algebraic-geometric-dilog-equivalence)'s
   pole-to-cusp bijection, the algebraic root $x = q_0^{-k}$ matches
   cusp $k$, and Step 2 identifies the singularity of the algebraic
   $\Phi_n$ with the singularity of $\mathrm{Li}_2$ at $z_k$ — which
   by Step 3 is the cusp-completeness condition. $\square$

## Implication for the Newton–Raphson solver

The conjecture has a **direct computational consequence**: the zeros
$\{q_0^{-k}\}$ of the algebraic denominator are the **exact initial
seed values** for the Newton–Raphson solver of the Thurston gluing
equations on the active JSJ piece. The pipeline is:

1. The algebraic engine computes $\Phi_n(x; q_0)$ as a rational
   function.
2. Extract the $n$ roots of its denominator $(x; q_0)_n$:
   $\{q_0^{-k} : k = 0, \dots, n-1\}$.
3. Pass the roots across the WASM boundary to the SnapPy kernel.
4. Use the roots not as a universal constant but as the **initial
   guesses** for the Newton–Raphson solver.

By Steps 1–4 of the proof sketch above, the algebraic seeds sit
**near** the cusp-completeness solution of the Thurston gluing
equations — only the gluing residuals from the active transient
crossings differ from zero. The solver converges in $O(1)$ Newton
steps per cusp (empirically $\approx 10$ steps to machine precision
across depths $n = 1, \dots, 3$, see witness below), instead of the
$O(\log\epsilon^{-1})$ steps needed when starting from a generic
universal $z_q$. The Newton step also avoids local-minimum traps,
because the algebraic poles are **isolated** in the cusp variety.

The witness
[q-pochhammer-seed.witness.json](../../../folio-assistant/computations/q-pochhammer-seed.witness.json)
drives Newton–Raphson on the color-tube discriminant $\Delta(z) = 0$
from each algebraic seed (perturbed by $0.1i$ to enter $\mathbb{C}$).
At depths $n = 1, 2, 3$, all seeds converge to a complex critical
point with residual $\lesssim 10^{-13}$ in 9–11 iterations,
empirically supporting the $O(1)$ claim.

## Relation to existing PL/JSJ infrastructure

This conjecture is the **shared-denominator** statement that the
existing
([Φ$_q$-tower JSJ bridge](#rem:phi-q-tower-jsj-bridge)) already
asserts implicitly: the JSJ piecewise sum
$\sum_S \mathrm{Vol}(K_S)$ is computed from the algebraic
$\sum_S \Phi_q(\lvert V_S\rvert)$ at exactly the cusps prescribed by
the algebraic denominators. Phrased motivically, the algebraic class
$[\Phi_n(x; q_0)] \in \mathfrak{B}(q)$ in the
([quantum Bloch group](#def:quantum-bloch-group))
regulates archimedeanly to the volume of the matched JSJ piece, with
the regulator's domain of definition pinned by the shared-denominator
locus.

## Discussion

Stated conditional on
([algebraic-geometric dilog equivalence](#conj:algebraic-geometric-dilog-equivalence))
and
([Archimedean limit](#conj:dilogarithm-archimedean-limit)). The Lean
formulation
`QOU.QPochhammer.shared_denominator_cusp_holonomy` is therefore a
class instance, not a closed theorem.

### Empirical scope of the seeding pipeline

Two computational witnesses bracket the conjecture's strong form:

- **Color-tube cubic** (succeeds):
  [q-pochhammer-seed.witness.json](../../../folio-assistant/computations/q-pochhammer-seed.witness.json)
  drives Newton–Raphson on $\Delta(z) = 0$ from the algebraic seeds
  $q_0^{-k} + 0.1i$. At depths $n \leq 3$, Newton converges to
  machine-precision residual ($\lesssim 10^{-13}$) in 9–11 iterations,
  empirically supporting the $O(1)$-steps-per-cusp prediction.

- **SnapPy Thurston gluing system** (bounds the strong form):
  [snappy-cusp-seeding.witness.json](../../../folio-assistant/computations/snappy-cusp-seeding.witness.json)
  measures the distance between the bare algebraic seeds and SnapPy's
  tetrahedral shape parameters for $\mathtt{m004}$, $\mathtt{m003}$,
  and the Borromean rings $\mathtt{L6a4}$. The bare seeds sit at
  distance $\sim 0.4$–$0.9$ from SnapPy's $z_k$, so the pole-to-cusp
  bijection cannot be a literal numerical identity
  $q_0^{-k} = z_k$. The conjecture must be interpreted as a bijection
  of **labels** (algebraic-pole index $\leftrightarrow$ cusp index)
  with the actual shape parameter being a non-trivial function
  $\tau_{\mathrm{arch}}(q_0^{-k})$ of the algebraic seed; the shape
  of that function is the subject of further work.

The two witnesses together support the conjecture's *structural*
content (algebraic poles label cusps) while bounding its *numerical*
form (the bare $q_0^{-k}$ are not literally the cusp shapes).
