## Intra-shell vs. inter-shell crossings

The inductive construction
([nuclear Gröbner--Shirshov reduction](#prop:nuclear-groebner-reduction))
builds the nucleus one nucleon at a time. Within a shell, each
new nucleon crosses existing nucleons via **bare transfer
matrices** $T(c, d)$ with crossing coefficients pp, nn, or mix
([transfer matrix operator](#def:transfer-matrix-operator)).

At a shell boundary, the situation changes. The closed shell's
nucleons form a tightly intertwined braid — its normal form
fills the Bruhat lattice symmetrically. A new nucleon crossing
this closed shell does not see individual nucleons; it sees the
**collective torus knot** $T_{2, n_s}$ where $n_s$ is the
shell occupancy.

**Definition (inter-shell operator).**
Let shell $\ell$ contain $n_s$ nucleons and be closed
(palindromic histogram). The crossing of a new nucleon
(starting shell $\ell + 1$) with the closed shell $\ell$ is
encoded by the torus knot transfer matrix:

$$
  \Phi_{\mathrm{shell}}^{(\ell)}
   : 
  H_A(q) \to H_{A+1}(q),
  \qquad
  \bar{\mathcal{N}}_A
  \mapsto
  r\!\bigl(
    \bar{\mathcal{N}}_A \cdot (c_{n_s}\sigma + d_{n_s}),
    G
  \bigr)
$$

where $(c_{n_s}, d_{n_s})$ are the **Chebyshev crossing
coefficients** of $T_{2, n_s}$ (see below), and $r(\cdot, G)$
is the Gröbner--Shirshov division algorithm.

## Chebyshev recurrence for torus knot coefficients

The torus knot $T_{2,n}$ is the closure of $\sigma^n$ in $H_2(q)$.
Its crossing coefficients $(c_n, d_n)$ in the $2 \times 2$
transfer matrix satisfy the **Chebyshev recurrence**:

$$
  \boxed{
    c_n = U_{n-1}(\tfrac{q - q^{-1}}{2}),
    \qquad
    d_n = -\frac{c_n \cdot qs_q}{1 + c_n}
  }
$$

where $U_k$ is the Chebyshev polynomial of the second kind and
$s_q = q^{1/2} - q^{-1/2}$.

Equivalently, from the matrix power
$T(1,0)^n = \bigl(\begin{smallmatrix} a_n & c_n \\ c_n & d_n \end{smallmatrix}\bigr)$:

$$
  c_1 = 1, \quad d_1 = 0
  \qquad\text{(bare crossing)}
$$

$$
  c_{n+1} = c_n(q - q^{-1}) + c_n + d_n, \qquad
  d_{n+1} = c_n
$$

The first few values at $q \approx 1.110$:

See [Table 1](#tbl:torus-knot-shell-binding-table1-data).

## Proposition: magic numbers from torus knot shell sizes

**Let $q > 1$ and let the nucleus be built by the inductive
construction with Gröbner--Shirshov reduction at each step.**

**(i) Shell closure triggers inter-shell operator.**
When the word-length histogram of $\bar{\mathcal{N}}(p, n)$ is
palindromic at nucleon count $A = A_{\mathrm{close}}$, the
next nucleon ($A_{\mathrm{close}} + 1$) crosses the closed
shell via $\Phi_{\mathrm{shell}}^{(\ell)}$ with the torus knot
$T_{2, n_s}$ where $n_s = A_{\mathrm{close}} - A_{\mathrm{prev}}$
is the size of the closing shell.

**(ii) Normalization is preserved across shell boundaries.**
The inter-shell operator $\Phi_{\mathrm{shell}}^{(\ell)}$
produces a Gröbner--Shirshov normal form, by the same argument as the
intra-shell step: the Chebyshev crossing element
$(c_{n_s}\sigma + d_{n_s})$ is linear in $\sigma$ (no
squares), and the division algorithm produces a unique normal
form remainder. The palindromic structure of the previous
shell is **not destroyed** — the new nucleon's generators
act on strands $A, A+1, \ldots$, which are disjoint from the
closed shell's generators $0, \ldots, A_{\mathrm{close}} - 1$.

**(iii) Magic numbers from the six embeddable torus knots.**
The embeddable torus knots on the Bring surface
([torus knot generators](#prop:torus-knot-generators)) assign
shell sizes via their $r \times s$ products. The six
nontrivial torus knots and their shell assignments:

See [Table 2](#tbl:torus-knot-shell-binding-table2-data).

The **shell capacity** is the number of nucleon pairs that
the torus knot can bind. Each torus knot $T_{r,s}$ mediates
a shell of size $r \times s$ nucleon crossings, but the actual
shell occupancy is the number of nucleon **pairs** (proton +
neutron) that fill the shell before palindromic closure.

The degree-$1$ knots ($T_{2,n}$, single-strand meridional
winding) give the **primary shell sequence**. The degree-$2$
knots ($T_{2,9}$, $T_{3,4}$) give **sub-shell splittings**
that refine the primary shells.

**(iv) The cumulative magic number sequence.**
The magic numbers are the cumulative sums of shell occupancies,
where each shell closes when same-type nucleons fill all
available crossings:

See [Table 3](#tbl:torus-knot-shell-binding-table3-data).

reproducing the experimental magic numbers
$\{2, 8, 20, 28, 50, 82, 126\}$.

**(v) Energy gap at shell boundaries.**
The Hecke energy $\Delta E$ jumps by a factor
$\sim |\lambda_+(T_{2,n_s})/\lambda_-(T_{2,n_s})|$ at each
shell boundary. For the first shell closure (He-4 $\to$
Li-5):

$$
  \frac{\Delta E_5}{\Delta E_4}
   \approx 
  \frac{1.409}{0.095}
  =  14.8
$$

This ratio is the **shell gap** — the algebraic signature of
the transition from intra-shell (bare crossings) to inter-shell
(torus knot crossings). The gap grows with shell size because
the torus knot eigenvalue ratio $|\lambda_+/\lambda_-| = q^{2n_s}$
increases exponentially.

## Gröbner--Shirshov preservation across all shells (inductive summary)

The full inductive argument for the construction of any nucleus
$\mathcal{A}(Z, N)$ proceeds:

1. **Base.** $\bar{\mathcal{N}}(1, 0) = \mathbf{1}$ — by definition
 in normal form.

2. **Intra-shell step.** Given $\bar{\mathcal{N}}_A$ in normal
 form within shell $\ell$, the next nucleon crosses via bare
 transfer matrix $(c_j\sigma_j + d_j)$. Apply Gröbner--Shirshov
 division: the result is in normal form
 ([main theorem](#unital-groebner-bases:thm:ugb-main-theorem)).

3. **Shell closure detection.** After each step, check the
 word-length histogram. If palindromic, the shell is closed.

4. **Inter-shell step.** The next nucleon after a shell closure
 crosses the closed shell via the Chebyshev crossing element
 $(c_{n_s}\sigma + d_{n_s})$ of $T_{2, n_s}$. This element
 is linear in $\sigma$ — no $\sigma^2$ terms — so it enters
 the Gröbner--Shirshov division on the same footing as any intra-shell
 crossing. The division algorithm produces a normal form.

5. **Repeat** until $A = Z + N$ nucleons are linked.

At every step — intra-shell or inter-shell — the Gröbner--Shirshov
division algorithm produces a unique normal form. The
inter-shell step differs only in the **magnitude** of the
crossing coefficients (Chebyshev-enhanced), not in the
algebraic structure. Normalization preservation follows from
the same main theorem used for intra-shell steps.
