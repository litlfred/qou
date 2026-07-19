**Proof.** Throughout, $h = q - q^{-1}$ denotes the Hecke amplitude and $[2]_q = q + q^{-1}$, $[3]_q = q^2 + 1 + q^{-2}$ the balanced quantum integers, with $q > 0$ real.

**Step 1: The seminormal matrices on $V_{(2,1)}$.** In the Hoefsmit seminormal basis of the two-dimensional representation $V_{(2,1)}$ of $H_3(q)$, the first generator is diagonal,

$$
\sigma_1 = \begin{pmatrix} q & 0 \\ 0 & -q^{-1} \end{pmatrix},
$$

and the second generator is the real symmetric matrix

$$
\sigma_2 = \begin{pmatrix} a & b \\ b & c \end{pmatrix},
\qquad
a = \frac{q - q^{-1}}{1 - q^{4}},
\qquad
c = \frac{q - q^{-1}}{1 - q^{-4}},
\qquad
b^2 = \frac{[3]_q}{[2]_q^2},
$$

with $b > 0$; the off-diagonal entry is the binding amplitude of [the Hoefsmit proposition](#prop:hoefsmit-binding-amplitude). These entries satisfy the two seminormal identities

$$
a + c
= h \cdot \frac{(1 - q^{-4}) + (1 - q^{4})}{(1-q^{4})(1-q^{-4})}
= h,
\qquad
a c
= \frac{h^2}{2 - q^{4} - q^{-4}}
= \frac{-h^2}{(q^{2} - q^{-2})^{2}}
= \frac{-1}{[2]_q^2},
$$

so that $\det \sigma_2 = ac - b^2 = -\bigl(1 + [3]_q\bigr)/[2]_q^2 = -[2]_q^2/[2]_q^2 = -1$ and $\mathrm{tr}\,\sigma_2 = h$: both generators have the Hecke eigenvalues $q$ and $-q^{-1}$. These are Hoefsmit's seminormal matrices for the standard representation, with diagonal entries indexed by the axial distances $± 2$ of the two standard tableaux of shape $(2,1)$; they satisfy the braid relation $\sigma_1\sigma_2\sigma_1 = \sigma_2\sigma_1\sigma_2$ by the seminormal construction \cite{hoefsmit1974,wenzl1988c}.
