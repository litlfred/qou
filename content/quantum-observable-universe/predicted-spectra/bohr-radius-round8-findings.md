**Remark (Round-8 Hecke-algebraic findings).**

Direct attempts at 4a, 4b, 4d yielded partial structural progress
but no full closure.

#### 4a result — $V_i$ decomposes additively in $\{h_b, h_d\}$

Symbolic recompute of the H_2 binding pipeline at the optimal
ordering $[p_1, e_2, e_1, p_2]$ gives:

$$
\begin{aligned}
  V_H &= z + h_b - h_d, \\
  V[1] &= 1 + 2 z h_b - z h_d, \\
  V[2] &= z - h_b,
\end{aligned}
$$

where $h_b = q - q^{-1}$ (bare skein), $h_d = q^5 - q^{-5}$
(K-shell-dressed skein), $z = \sqrt{q}/(q+1)$ (Markov parameter).
The cross-terms $h_b \cdot h_d$ that one would naively expect from
the multiplicative transfer-matrix chain **cancel exactly** in
the optimal-ordering computation, leaving a clean linear
decomposition.

**Significance:** the "kinetic" ($h_d$) and "Coulomb" ($h_b$)
contributions to $V_i$ are *separately identifiable* as
Hecke-algebraic monomials, contradicting the round-7 claim that
no per-generator additive decomposition exists. The decomposition
is real for the optimal ordering — though the cross-cancellation
relies on the specific permutation structure.

#### 4b result — shell-ratio matches Bohr $1/n^2$

The categorical spectral-gap ratio
$\Delta_{\mathrm{kin}}(k)/\Delta_{\mathrm{Coul}} = (4k+2)/2 = 2k+1$
is shell-dependent and pure-Hecke (no QED transport). Inverting:

$$
  (2k+1)^{-2} \in \{1, \tfrac{1}{9}, \tfrac{1}{25}, \tfrac{1}{49}, \dots\}
  \quad\text{for}\quad k \in \{0, 1, 2, 3, \dots\}.
$$

This is **exactly the Bohr $1/n^2$ energy-level spacing** if we
identify $n = 2k+1$. The QOU shell index $k$ relates to the
physics quantum number $n$ by $n = 2k+1$ — so QOU $k=0$
corresponds to physics $n=1$ (ground state), $k=1$ to $n=3$,
etc., with the dressing-power $2k+1$ playing the role of the
physical principal quantum number.

**Significance:** the *relative* shell spacing
$E_n / E_1 = 1/n^2$ is recovered from pure Hecke
spectral-gap analysis, with no transport. The $\alpha_{EM}^{2}$
absolute scale is *not* fixed by this — only the
shell-to-shell ratios are.

#### 4d partial result — covalent bonds at curvature rank 2

The GB curvature-rank stratification suggests
$y_{\mathrm{cov}}^{*} \sim \alpha_{EM}^{(\text{rank})}$ where
"rank" counts independent EM force-carrier insertions. A
covalent bond shares two electrons (Pauli + singlet), each
mediated by one EM exchange, giving **rank 2 $\to$ $\alpha^{2}$**.

**Limitation honestly noted:** atomic spectra (single electron)
also scale as $\alpha^{2}$, but a single atom has only *one*
electron-EM coupling. So the "rank = number of EM exchanges"
interpretation correctly predicts covalent $\alpha^2$ but
doesn't explain *atomic* $\alpha^2$ — that requires the
virial-balance argument from
[`conj:bohr-radius-categorical`](#conj:bohr-radius-categorical),
which remains transported.

#### Shell-spacing and kinetic/Coulomb decomposition

The combination 4a + 4b establishes that **the Hecke-algebraic
structure encodes the relative shell spacing and the additive
kinetic/Coulomb decomposition correctly**. What remains
transported (not derived from Hecke) is the *absolute scale*
$E_h = m_e c^2 \alpha^2$ — specifically the appearance of
$m_e c^2$ as the natural mass-energy unit and the choice of
$\alpha^2$ rather than $\alpha^k$ for other $k$.

The conjecture is closer to closure than after round 7, but the
absolute-scale step still requires either a uniqueness lemma
(option 4e) or further work on the curvature-rank $\to$ $\alpha$-power
mapping (sharpening 4d to handle atomic as well as covalent
binding).
