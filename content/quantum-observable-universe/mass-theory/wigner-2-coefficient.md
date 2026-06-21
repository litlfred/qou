*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition.**
*For any self-conjugate partition $\lambda = \lambda'$ of $k$,
the per-generator trace in the Hoefsmit seminormal representation
satisfies*

$$
  \frac{\mathrm{tr}(\sigma_g^{(\lambda)})}{\dim(\lambda)}
  = \frac{h}{2}
  = \frac{q - q^{-1}}{2}
$$

*for every generator $g = 1, \ldots, k{-}1$.  Consequently, the
BW coefficient ([shadow price](#prop:mass-coefficient-shadow-price))
for $\lambda$ is*

$$
  C_\lambda = w_\lambda \cdot \frac{h}{2}
  = \frac{\dim_q(\lambda)^2}{[k]_q!} \cdot \frac{q - q^{-1}}{2}
$$

*In particular, for $\lambda = [3,2,1] \vdash 6$:*

$$
  C_{[3,2,1]}
  = \frac{[2]_q\,[4]_q\,[6]_q \cdot h}
         {2\,[3]_q^2\,[5]_q}
$$

*Proof.*
The argument has three steps: a pairing identity, a counting
argument, and an algebraic simplification.

**Step 1 (Paired sum identity).**
In the [seminormal form](#prop:hoefsmit-seminormal-form), the
diagonal entry for standard tableau $T$ at generator $\sigma_g$
is $a_\rho = h/(1 - q^{-2\rho})$ where
$\rho = c(T, g{+}1) - c(T, g)$ is the axial distance (difference
of contents of the cells containing entries $g{+}1$ and $g$).

For any $\rho \neq 0$:

$$
  a_\rho + a_{-\rho}
  = \frac{h}{1 - q^{-2\rho}} + \frac{h}{1 - q^{2\rho}}
  = h \cdot \frac{(1 - q^{2\rho}) + (1 - q^{-2\rho})}
              {(1 - q^{-2\rho})(1 - q^{2\rho})}
  = h \cdot \frac{2 - q^{2\rho} - q^{-2\rho}}
              {1 - q^{2\rho} - q^{-2\rho} + 1}
  = h
$$

since numerator and denominator are both $2 - (q^{2\rho} + q^{-2\rho})$.

**Step 2 (Conjugation pairing).**
Let $\lambda = \lambda'$ be self-conjugate.  The transposition of
the Young diagram (reflecting across the main diagonal) induces an
involution $T \mapsto T^\vee$ on the set of standard Young tableaux
of shape $\lambda$.  Under this involution:

- The cell of entry $m$ in $T^\vee$ has content $-c(T, m)$
  (reflection swaps row and column).
- Therefore $\rho(T^\vee, g) = -\rho(T, g)$ for every generator $g$.
- Since $\lambda$ is self-conjugate, $T^\vee$ is again a valid SYT
  of shape $\lambda$.
- The involution is fixed-point-free on axes: $\rho(T,g) \neq 0$
  implies $T^\vee \neq T$ in the relevant entry positions.

The $\dim(\lambda)$ tableaux pair into $\dim(\lambda)/2$ conjugate
pairs $\{T, T^\vee\}$.

**Step 3 (Trace computation).**
The trace of $\sigma_g$ in the seminormal basis is the sum of all
diagonal entries:

$$
  \mathrm{tr}(\sigma_g^{(\lambda)})
  = \sum_{T} a_{\rho(T,g)}
  = \sum_{\{T, T^\vee\}} \bigl(a_{\rho(T,g)} + a_{-\rho(T,g)}\bigr)
  = \sum_{\{T, T^\vee\}} h
  = \frac{\dim(\lambda)}{2} \cdot h
$$

Dividing by $\dim(\lambda)$:

$$
  \frac{\mathrm{tr}(\sigma_g^{(\lambda)})}{\dim(\lambda)}
  = \frac{h}{2}
$$

This is independent of $g$ (since all generators are conjugate in
$S_k$, and the trace is conjugation-invariant).

**Corollary (BW coefficient).**
By the [shadow price proposition](#prop:mass-coefficient-shadow-price),
$C_\lambda = w_\lambda \cdot \mathrm{tr}(\sigma_g)/\dim$.
Substituting $\mathrm{tr}/\dim = h/2$:

$$
  C_\lambda = \frac{\dim_q(\lambda)^2}{[k]_q!} \cdot \frac{h}{2}
$$

For $\lambda = [3,2,1] \vdash 6$, the hook lengths are
$\{5, 3, 1, 3, 1, 1\}$, giving $\dim_q = [6]_q!/([5]_q [3]_q^2)
= [2]_q [4]_q [6]_q / [3]_q$.  Therefore:

$$
  C_{[3,2,1]}
  = \frac{[2]_q^2 [4]_q^2 [6]_q^2}{[3]_q^2 \cdot [6]_q!}
    \cdot \frac{h}{2}
  = \frac{[2]_q [4]_q [6]_q \cdot h}{2\,[3]_q^3\,[5]_q}
$$

**Remark (isospin midpoint).**
The value $h/2 = (q - q^{-1})/2$ is the arithmetic mean of the
symmetric eigenvalue $q$ and the antisymmetric eigenvalue $-q^{-1}$
of the Hecke generators.  Self-conjugate partitions sit at the
exact isospin midpoint of the Hecke spectrum.

**Remark (pn invisibility).**
The per-crossing trace contribution in the $[3,2,1]$ representation
is:

| Crossing type | Coefficient $d$ | $\mathrm{tr}(\sigma + d \cdot I)/\dim$ |
|:---:|:---:|:---:|
| $pp$ | $0$ | $h/2$ |
| $nn$ | $-h$ | $-h/2$ |
| $pn$ | $-h/2$ | $0$ |

The proton-neutron crossing is **invisible** to $[3,2,1]$: its
trace contribution $h/2 - h/2 = 0$ vanishes exactly.  Only
$pp$ ($+h/2$) and $nn$ ($-h/2$) crossings contribute, with
opposite signs.

Consequently the $[3,2,1]$ BW scaling is

$$
  S_{[3,2,1]}(Z,N) = \frac{(Z - N)(A - 1)}{A^{4/3}}
$$

where $(Z{-}N)(A{-}1) = Z(Z{-}1) - N(N{-}1)$ counts the net
$pp$ minus $nn$ crossing asymmetry, NOT the isospin Casimir
$T(T{+}1)$.  This is why $\chi_{[3,2,1]}$ vanishes for deuterium
(pure $pn$) and ${}^3\mathrm{He}$ (where the single $pp$
crossing's contribution is cancelled by the full matrix
product structure at second order in $h$).

**Remark (character structure).**
The nuclear character $\chi_{[3,2,1]}$ has universal factor
$h^2 \cdot \Phi_6(q^2)$ where $\Phi_6(q^2) = q^4 - q^2 + 1
= (q^6 + 1)/(q^2 + 1)$ is the 6th cyclotomic polynomial evaluated
at $q^2$.  The $h^2$ factor encodes the isospin sensitivity (the
character vanishes at $q = 1$, i.e., in the classical limit).
$\square$
