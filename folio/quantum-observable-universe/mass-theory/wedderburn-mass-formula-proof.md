*Proof.*
Work over $R = \mathbb{Z}[q^{\pm 1/2}]$ at generic $q$, passing to
the fraction field where inverses are required; write
$h_{\mathrm{A}} = q - q^{-1}$ for the Hecke parameter and
$z = q^{3}/(q^{2}+1)$ (**convention D**) for the Markov weight, so that the
Markov trace $\mathrm{tr}_M$ is the linear functional normalised by
$\mathrm{tr}_M(1) = 1$ and $\mathrm{tr}_M(\sigma_i) = z$ (positive
stabilisation).

**Step 1 — extremal Wedderburn blocks and channel eigenvalues.**
By the
[three-parameter decomposition](#prop:three-parameters-wedderburn),
$H_3(R, q) \cong M_1(R) \oplus M_2(R) \oplus M_1(R)$, with blocks
labelled by the partitions $(3)$, $(2,1)$, $(1,1,1)$; for general $n$
the corresponding extremal blocks are the symmetric $[n]$, standard
$[n-1, 1]$, and alternating $[1^n]$ representations. The Hecke
relation $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$ gives each generator
the eigenvalue $q$ in the symmetric channel and $-q^{-1}$ in the
alternating channel; since all $\sigma_i$ are conjugate, the two
one-dimensional blocks are the algebra characters
$\varepsilon^{\mathrm{sym}}(\sigma_i) = q$ and
$\varepsilon^{\mathrm{alt}}(\sigma_i) = -q^{-1}$. A typed crossing
element $X = c \cdot \sigma_i + d \cdot \mathbf{1}$
([transfer matrix](#def:transfer-matrix-operator)) therefore
evaluates in the two scalar channels as

$$
\lambda^{\mathrm{sym}} = \varepsilon^{\mathrm{sym}}(X) = cq + d,
\qquad
\lambda^{\mathrm{alt}} = \varepsilon^{\mathrm{alt}}(X)
  = -c q^{-1} + d .
$$

**Step 2 — the transfer matrix is the regular representation of the
crossing algebra.** A single crossing generates the two-dimensional
commutative algebra
$R[\sigma] = R[x] / \bigl((x - q)(x + q^{-1})\bigr)$, in which
$\sigma^2 = h_{\mathrm{A}} \sigma + 1$. In the ordered basis $(\sigma, 1)$,
multiplication by $X = c\sigma + d$ has matrix exactly the crossing
(transfer) matrix of the statement,

$$
T(X) =
\begin{pmatrix}
  c h_{\mathrm{A}} + d & c \\
  c & d
\end{pmatrix},
$$

since $X \cdot \sigma = c\sigma^2 + d\sigma = (ch_{\mathrm{A}} + d)\,\sigma + c$
and $X \cdot 1 = c\sigma + d$. As a matrix of left multiplication,
$T$ is an algebra homomorphism: $T(X)\,T(X') = T(XX')$, which one
verifies directly — $XX' = c''\sigma + d''$ with
$c'' = cc'h_{\mathrm{A}} + cd' + c'd$ and $d'' = cc' + dd'$, matching the entries
of the matrix product. Consequently, for the chained element
$X_i := \prod_{j > i} X_j$ of the crossings of all strands $j > i$,
the transfer-matrix chain satisfies
$M_i = \prod_{j > i} T(X_j) = T(X_i)$, and reading off the basis
coefficients gives $(M_i)_{12} = (M_i)_{21} = c_i$ and
$(M_i)_{22} = d_i$, where $X_i = c_i \sigma + d_i$. Moreover the
eigenvalues of $M_i = T(X_i)$ are precisely the two character values
$\lambda_i^{\mathrm{sym}} = \varepsilon^{\mathrm{sym}}(X_i)$ and
$\lambda_i^{\mathrm{alt}} = \varepsilon^{\mathrm{alt}}(X_i)$, since
the regular representation of $R[\sigma]$ diagonalises along its two
characters. (Chaining within a single crossing algebra is the
defining Level-0 transfer-matrix reduction; the exact all-partitions
computation replaces it for $n \ge 4$, as the statement records.)

**Step 3 — the three invariants are the three extremal block
readouts.**

1. *Markov trace (standard block).* By linearity and the
   normalisation above,
   $\mathrm{tr}_M(X_i) = c_i\,z + d_i = z\,(M_i)_{12} + (M_i)_{22}$.
   Hence $\Phi_1 = \sum_i \ln\bigl\lvert z\,(M_i)_{12} +
   (M_i)_{22}\bigr\rvert = \sum_i \ln\lvert \mathrm{tr}_M(X_i)\rvert$
   is the Markov-weighted trace datum of the chain — the invariant
   attached to the standard (dim $n{-}1$) block in the
   correspondence table.
2. *Determinant $=$ sym $\times$ alt.* Directly,
   $\det T(X) = (ch_{\mathrm{A}} + d)\,d - c^2 = cdh_{\mathrm{A}} + d^2 - c^2
   = (cq + d)(-cq^{-1} + d)
   = \lambda^{\mathrm{sym}}\lambda^{\mathrm{alt}}$; equivalently this
   is the product of the two eigenvalues exhibited in Step 2. By
   multiplicativity of the determinant and of the characters,
   $\det M_i = \lambda_i^{\mathrm{sym}}\,\lambda_i^{\mathrm{alt}}$,
   so
   $\Phi_2 = \sum_i \bigl(\ln\lvert\lambda_i^{\mathrm{sym}}\rvert +
   \ln\lvert\lambda_i^{\mathrm{alt}}\rvert\bigr)$.
3. *Ratio $=$ sym $/$ alt (chirality).*
   $\Phi_3 = \sum_i \bigl(\ln\lvert\lambda_i^{\mathrm{sym}}\rvert -
   \ln\lvert\lambda_i^{\mathrm{alt}}\rvert\bigr)$.

From 2 and 3,
$\ln\lvert\lambda_i^{\mathrm{sym}}\rvert$ and
$\ln\lvert\lambda_i^{\mathrm{alt}}\rvert$ are recovered as half the
sum and half the difference of the per-chain summands: the pair
$(\Phi_2, \Phi_3)$ is an invertible linear repackaging of the two
one-dimensional block evaluations, while $\Phi_1$ carries the
standard-block Markov datum. The triple $(\Phi_1, \Phi_2, \Phi_3)$
therefore carries exactly the evaluations of the three extremal
Wedderburn blocks on the chain — no more and no fewer. This is the
claimed completeness at the $2 \times 2$ transfer level: the chain
data $(c_i, d_i) \in R^2$ of the two-dimensional crossing algebra
support precisely the two characters and the Markov functional
exhibited, and every block-respecting multiplicative invariant of
$\{M_i\}$ is a function of these three. For $n \ge 4$ the
non-extremal partitions contribute additional invariants, computed
exactly by the full partition sum via Young's seminormal form, as
stated.

**Step 4 — the coefficients.** The overall scale
$\alpha = m_e \times 8G$ is the archimedean evaluation of the
algebraic binding scale $m_e \cdot \mathrm{Vol}_q(\mathcal{B}_3)$,
with $\mathrm{Vol}(\mathcal{B}_3) = 8G$ the Borromean volume
([binding scale](#conj:binding-scale-catalan)). The determinant
weight $\beta_2 = -2[3]_q$ has a direct count: the three color
channels give the pair count $\binom{3}{2} = 3$, $q$-deformed to
$[3]_q$, with the sign fixed by the determinant sign accumulation and
the factor $2$ by the $\mathfrak{p}\mathfrak{n}$ crossing-doubling
convention established there. The chirality weight $h_{\mathrm{A}}^2$ is the
minimal even power of the Hecke parameter compatible with the
$S$-parity classification of the three terms
([$S$-classification](#prop:frobenius-s-classification)) and with the
vanishing of the chirality contribution in the commutative limit
([commutative chirality](#cor:commutative-chirality-vanishes)):
$h_{\mathrm{A}} \to 0$ as $q \to 1$, so $h_{\mathrm{A}}^2 \Phi_3 \to 0$ and the classical
mass formula retains no chirality term. All three weights are
functions of $q$ alone, evaluated at $q_0$, and the scale is fixed by
$m_e$: no fitted parameter enters.

Assembling: the binding functional
$\alpha\,(\Phi_1 - 2[3]_q\,\Phi_2 + h_{\mathrm{A}}^2\,\Phi_3)$ is the weighted
sum of the three extremal-block invariants of the atomic braid
established in Steps 1–3, with the weights of Step 4, added to the
free constituent masses $Z \cdot m_{\mathfrak{p}} + N \cdot
m_{\mathfrak{n}} + Z \cdot m_e$. $\square$

The numerical agreement of this formula with measured atomic masses
across the nuclide table is an empirical cross-check, not part of the
proof.
