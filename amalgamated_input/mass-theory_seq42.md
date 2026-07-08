<!-- FILE_START: intro-parity-classification-discrepancy.md -->
The classical evaluation is parity-blind. It cannot distinguish a knot from its mirror image. This causes a systematic discrepancy between the predicted and empirical mass spectra.

We trace the discrepancy to the chirality pairing. We resolve it using the augmented parity classification. Finally, we map the atomic atlas to track which elements resolve unambiguously.
<!-- FILE_END: intro-parity-classification-discrepancy.md -->

<!-- FILE_START: mn-classical-parity-blind.md -->
**Remark (Murnaghan–Nakayama parity blindness).**
*The classical Murnaghan–Nakayama recursion computes $S_n$ characters. When applied to the $S_{3A}$ atomic braid projection, it cannot distinguish a proton from a neutron. Both possess identical permutation cycle types.*

Positive and negative crossings project to the identical $S_n$ transposition. The q-deformed Hecke algebra distinguishes them through eigenvalue signs. The classical limit $q \to 1$ crushes this distinction.

The classical computation fails to predict mass splitting but succeeds as a structural diagnostic. It identifies the exact sparse partition support of the atomic braid. The full calculation uses the $q$-character evaluated strictly on this pre-computed support.
<!-- FILE_END: mn-classical-parity-blind.md -->

<!-- FILE_START: q-character-closes-parity-gap.md -->
**Remark (closing the parity gap).**
*The $q$-deformed Hecke character $\chi^\lambda_q(\sigma_w)$ explicitly breaks the parity blindness. Computed via the Hoefsmit seminormal form, it distinguishes $\sigma$ from $\sigma^{-1}$ using the Hecke eigenvalue gap $(q, -q^{-1})$. This strictly separates proton from neutron.*

The symbolic matrix evaluation preserves $q$ exactness. A positive crossing contributes differently to the partition sum than a negative crossing. The mixed $\sigma^{\pm 1}$ braid words accumulate a net $q$-dependence. The proton (majority $\sigma$) trace diverges from the neutron (majority $\sigma^{-1}$) trace.

This separation restores the beta-decay calibration constraint. The structural information lost in the classical limit returns.
<!-- FILE_END: q-character-closes-parity-gap.md -->

<!-- FILE_START: frobenius-codim-universal.md -->
*Let $A = H_n(R, q)$ be a self-dual Frobenius algebra with Markov trace $\tau$. The quantum-co-dimension element*

$$
  C_{\dim_q}
  \;:=\;
  \sum_{\lambda \in \widehat{A}}
    \frac{1}{\dim_q(\lambda) \cdot \tau(p_\lambda)}
    \cdot p_\lambda
  \;\in\; Z(A)
$$

*lies in the centre of $A$ and satisfies*

$$
  \boxed{
    \tau\bigl(C_{\dim_q}\bigr)
    \;=\;
    \sum_{\lambda \in \widehat{A}} \frac{1}{\dim_q(\lambda)}.
  }
$$
<!-- FILE_END: frobenius-codim-universal.md -->

<!-- FILE_START: frobenius-codim-universal-interpretation.md -->
**Physical content.**
*Any vortex on the self-dual Frobenius algebra inherits a tower residual. The residual equals the trace of the quantum-co-dimension element scaled by the electron mass $m_e$:*

$$
  \Delta m_{\text{vortex}}
  \;=\;
  m_e \cdot \tau\bigl(C_{\dim_q}^{(A)}\bigr).
$$

*This trace provides the universal derivation of the $(5/2) m_e$ proton residual.*
<!-- FILE_END: frobenius-codim-universal-interpretation.md -->

<!-- FILE_START: frobenius-limits-substrate-cost.md -->
**Remark (limits of the substrate cost).**
*The Frobenius co-Casimir trace $\tau(C_{\dim_q}) = \sum_\lambda 1/\dim_q(\lambda)$ exhibits a regular limit structure.*

As $q \to 1$, it reaches the classical sum $\sum 1/d_\lambda$. At $q \to 0$ or $q \to \infty$, it freezes to exactly $2$ (the sum of the two 1-dimensional endpoints). At the observed substrate $q_0 \approx 1.11$, the trace is slightly reduced from the classical peak.

This sum measures the substrate's fundamental processing overhead. The brane tower evaluates the cost of the specific knot computation. The substrate imposes the Frobenius bound independently of the braid.
<!-- FILE_END: frobenius-limits-substrate-cost.md -->

<!-- FILE_START: knot-mass-formula-unified.md -->
*The categorical mass of the vortex $\varrho$ is exactly:*

$$
  \boxed{
    \mathfrak{m}(\varrho)
    \;=\;
    \underbrace{\bigl|\mathrm{tr}_M(T_w)\bigr|}_{\text{descended}}
    \;-\;
    \underbrace{\sum_{i=0}^{n-2} \mathrm{Li}_2^q\bigl(-|\hat V_i^{\mathrm{full}}|\bigr)
               - z^2 \sum_{0 \leq i < j \leq n-2}
                  \mathrm{Li}_2^q\bigl(-|\hat V_i^{\mathrm{full}} \hat V_j^{\mathrm{full}}|\bigr)}_{\text{brane tower}}
    \;+\;
    \underbrace{m_e \cdot \mathrm{tr}_M\bigl(C_{\dim_q}^{H_n(R, q)}\bigr)}_{\text{Frobenius co-Casimir}}
  }
$$

*where $\mathrm{Li}_2^q(z)$ is the symmetric q-dilogarithm. This integrates the Briggs–Klein expansion over each resolved defect.*

The descended piece evaluates the basic topological trace. The brane tower resolves the computational cost of the braid diagram. The Frobenius co-Casimir accounts for the substrate's universal algebra representation overhead.

The archimedean specialisation $\Phi_q(|\hat V_i|)$ breaks the exact Markov invariance of the algebraic trace. Replacing it with the rigorous Habiro-coefficient cyclotomic sum eliminates the isospin pathology at $q_0$.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real-analytic constructs. Any generic categorical identities remain valid over an abstract coefficient ring.
<!-- FILE_END: knot-mass-formula-unified.md -->

<!-- FILE_START: nuclear-knot-classification.md -->
*The closure of the nuclear braid $\mathcal{N}(Z,N)$ in $H_3(R, q)$
determines a bulk modification factor $a(\mathcal{N})$ for the
BW binding energy.  This factor is a single product over
independent nucleon pairs:*

$$
  a(\mathcal{N})
  \;=\;
  \prod_{i=1}^{n_{\mathrm{pairs}}}
    (1 - \varepsilon_i)
$$

*where $\varepsilon_i$ is the Frobenius norm deviation of the
$i$-th nucleon pair from the identity braid:*

- *Amphicheiral pair (pp or nn in $\mathcal{B}_3$):
  $\varepsilon = h^2 = (q - q^{-1})^2$*
- *Chiral pair (pn):
  $\varepsilon = -h = -(q - q^{-1})$*

*The sign convention: amphicheiral pairs ($K = \bar{K}$) deviate
quadratically ($h^2 > 0$, reducing binding); chiral pairs deviate
linearly ($-h < 0$, increasing binding).*

| $A$ | Pairs | Deviations $\varepsilon_i$ | $a(\mathcal{N})$ |
|-----|-------|---------------------------|-------------------|
| $1$ | $0$ | — | free nucleon |
| $2$ | $1$ pn (chiral) | $-h$ | $1 + h \approx 1.209$ |
| $3$ | $1$ pp or nn (amphicheiral) | $h^2$ | $1 - h^2 \approx 0.956$ |
| $4$ | $2$ (pp + nn, amphicheiral) | $h^2, h^2$ | $(1 - h^2)^2 \approx 0.914$ |
| $\geq 5$ | many | $(1 - h^2)^n \to 1$ | $1$ |

*In the large-$A$ limit, $(1 - h^2)^n \to 1$ since
$h^2 \approx 0.044 \ll 1$, recovering the standard
BW formula for heavy nuclei.*

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: nuclear-knot-classification.md -->

<!-- FILE_START: geom-yekutieli-alignment.md -->
**Proposition (conditional on
[`conj:hyperbolic-volume-transcendence`](#conj:hyperbolic-volume-transcendence)
and
`rem:baryon-period-ratio`).**
*The piecewise geometric invariant
$\mathrm{Geom}(K)$
([topological mass formula](#prop:topological-mass-formula))
is the evaluation of the Yekutieli rigid dualizing complex
$\omega_A^\bullet$ on the algebraic stratification of the braid
$\beta$ with closure $K = \widehat\beta$ (per
[algebraic stratification](#prop:phi-q-tower-algebraic-stratification);
the τ-image of this evaluation is the geometric reading on
$S^3 \setminus K$, classified by Thurston's geometrization at the
τ-side):*

$$
  \mathrm{Geom}(K) =
  \langle \omega_A^\bullet, S^3 \setminus K \rangle_{\mathrm{Frob}}
  =
  \begin{cases}
    \mathrm{Vol}(K) / \hbar_q^2
      & K \text{ hyperbolic} \\[4pt]
    \mathrm{CS}(K) \cdot \hbar_q^2
      & K \text{ torus} \\[4pt]
    0 & K = \bigcirc
  \end{cases}
$$

*where $\langle -, - \rangle_{\mathrm{Frob}}$ is the Frobenius
pairing induced by the rigid dualizing complex, and
$\hbar_q = 1 - 1/q$ is the quantum Planck constant.*

*Proof.*
The argument has three parts.

**Part 1: the rigid dualizing complex mediates duality.**
The Frobenius--Hopf algebra $A$ at the substrate parameter $q$
carries a rigid dualizing complex $\omega_A^\bullet$
(Yekutieli \cite{yekutieli2015}), which satisfies the rigidifying
isomorphism

$$
  \omega_A^\bullet
  \;\simeq\;
  R\mathrm{Hom}_{A^e}(A, A^e)
$$

in the derived category $D(A^e)$.  The Frobenius form
$\lambda\colon A \to \mathbf{1}$ makes $A$ self-dual with respect
to $\omega_A^\bullet$, inducing the non-degenerate pairing

$$
  \langle -, - \rangle_{\mathrm{Frob}}
  \colon
  H^\bullet(S^3 \setminus K; \omega_A^\bullet)
  \otimes
  H^{3-\bullet}(S^3 \setminus K; A)
  \;\longrightarrow\;
  \mathbb{C}.
$$

This is the categorical substitute for the canonical sheaf in the
non-commutative setting.

**Part 2: Geometric type selects the evaluation mode (algebraic
side).** The proof works in $\mathbb{Z}[q^{\pm 1/2}]$ throughout;
the geometric / 3-manifold reading appears only as the τ-image
discussed in Part 3. Algebraically, the rigid dualizing evaluation
$\langle \omega_A^\bullet, S^3 \setminus K \rangle_{\mathrm{Frob}}$
admits a single closed-form expression in terms of the
[algebraic quantum volume](#def:algebraic-quantum-volume)
$\mathrm{Vol}_q(\beta) \in \mathbb{Z}[q^{\pm 1/2}]$ and the
[Chern-Simons phase](#rem:chern-simons-as-knot-invariant) $\mathrm{CS}_q(\beta)$:

$$
  \mathrm{Geom}(K)
  \;=\;
  \frac{\mathrm{Vol}_q(\beta)}{\hbar_q^2}
  \;+\;
  \mathrm{CS}_q(\beta) \cdot \hbar_q^2
$$

with the $\hbar_q$ factors normalising the Frobenius pairing. For
the algebraic-side derivation no Thurston-geometrization input is
required; the Wedderburn-Artin block decomposition of $H_n(R, q)$
selects which of the two summands dominates for a given braid:

- *Algebraic-hyperbolic regime* ($\mathrm{Vol}_q(\beta) \ne 0$
  in $\mathbb{Z}[q^{\pm 1/2}]$): the first summand carries the
  contribution. The fundamental class pairs against the algebraic
  quantum volume, and the Frobenius normalisation introduces
  $1/\hbar_q^2$ as the mass scale.

- *Algebraic-torus regime* ($\mathrm{Vol}_q(\beta) = 0$ in
  $\mathbb{Z}[q^{\pm 1/2}]$, e.g. $\beta = \beta_{T_{m,n}}$): the
  algebraic quantum volume vanishes identically and the second
  summand carries the contribution. The dualising normalisation
  flips to $\hbar_q^2$ (multiplicative rather than divisive),
  reflecting the Frobenius duality between bulk and boundary:

$$
  \frac{\mathrm{Vol}_q(\beta)}{\hbar_q^2}
  \quad\longleftrightarrow\quad
  \mathrm{CS}_q(\beta) \cdot \hbar_q^2.
$$

- *Algebraic-trivial regime* ($\beta = 1$, the identity / unknot
  closure): both algebraic summands vanish (vacuum normalisation),
  reflecting the empty cohomology of the trivial element of
  $H_n(R, q)$ against $\omega_A^\bullet$.

**Part 3: the Frobenius self-pairing is unitary (algebraic).**
For any braid $\beta$ and its mirror $\beta^*$ (obtained by
reversing each $\sigma_i \mapsto \sigma_i^{-1}$), the Frobenius
pairing satisfies

$$
  \langle \beta, \beta^* \rangle_{\mathrm{Frob}}
  = \mathrm{Geom}(\beta) \cdot \mathrm{Geom}(\beta^*)^{-1}
  = 1,
$$

since $\mathrm{Vol}_q(\beta^*) = \mathrm{Vol}_q(\beta)$ in
$\mathbb{Z}[q^{\pm 1/2}]$ (algebraic quantum volume is invariant
under mirror image, by inspection of the Markov-trace product
formula) and $\mathrm{CS}_q(\beta^*) = -\mathrm{CS}_q(\beta)$
(the Chern-Simons phase changes sign on mirror — direct
consequence of the $q \mapsto q^{-1}$ involution on the relevant
braid representation).

For **amphicheiral** knots ($K = K^*$, e.g.\ the figure-eight
$4_1$), the self-pairing is manifestly real.  This explains why
the figure-eight BW modification factors
([figure-eight BW coefficients](#thm:six-term-mass-formula-complete))
are both real algebraic expressions in $q$:
$1 - h^2 = 4 - [3]_q$ and $h[2]_q = q^2 - q^{-2}$.

**Connection to transcendence.**
The non-vanishing obstruction classes $\kappa_n \neq 0$
at every level of the brane tower — the content of
[motivic perpetual obstruction](#conj:motivic-perpetual-obstruction)
applied to the substrate's motivic Galois character at every
finite place — ensure that the evaluation $\mathrm{Geom}(K)$ for
distinct hyperbolic knots produces algebraically independent
values. A polynomial relation among the
$\mathrm{Vol}(K_i)/\hbar_q^2$ would force the tower to collapse
at finite height, contradicting place-by-place non-vanishing of
the motivic Galois character
([hyperbolic volume transcendence](#conj:hyperbolic-volume-transcendence)).
$\square$
<!-- FILE_END: geom-yekutieli-alignment.md -->

<!-- FILE_START: content-scaling-correspondence.md -->
*By $q$-Schur--Weyl duality $V^{\otimes n} \cong \bigoplus_\lambda V_\lambda \otimes S_\lambda$,
the content $c = j - i$ of a box at position $(i,j)$ in a Young diagram
equals the magnetic quantum number $m_j$ of the corresponding
$\mathrm{SU}_q(2)$ weight space.*

*The content determines the BW scaling function:*

| Content $c$ | Isospin meaning | Scaling $f_c(Z,N)$ |
|:-----------:|:---------------:|:-------------------:|
| $+1$ | proton nearest-neighbor | $Z(Z{-}1)/A^{1/3}$ |
| $-1$ | neutron nearest-neighbor | $N(N{-}1)/A^{1/3}$ |
| $0$ | balanced (pn mixed) | $A^{2/3}$ or $\pm 1/\sqrt{A}$ |
| $\pm 2$ | next-nearest same-type | $Z^{4/3}/A^{1/3}$ |
| $\lvert c\rvert \geq 3$ | long-range | $T^p(T{+}1)^p/A^p$ |

*Each scaling function counts the number of nucleon pairs at
spin projection $c$ in the nuclear ground state.* $\square$
<!-- FILE_END: content-scaling-correspondence.md -->

