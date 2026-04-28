**Remark.**
*Each term of the empirical Bethe–Weizsäcker mass formula
corresponds to a specific stratum of the Schur–Weyl decomposition
([Schur–Weyl mass decomposition](#prop:schur-weyl-mass-decomposition)).
The empirical coefficients that nuclear physicists fit to data in
the 20th century are not free parameters in the categorical
picture: they are determined by the $q$-hook product
$H_q(\lambda)$ evaluated on specific partition shapes.*

**Dictionary.**

| BW empirical term | Schur–Weyl stratum $\lambda$ | Algebraic origin |
|---|---|---|
| Volume $a_V \cdot A$ | $(3A)$ (fully symmetric) | Extensivity of the trace on $\mathrm{Sym}^{3A}$; forced by tensor structure of the Markov trace. |
| Surface $a_S \cdot A^{2/3}$ | $(3A-1, 1)$ (standard defect) | Weyl dimension formula for boundary Specht modules gives the $A^{2/3}$ scaling. |
| Coulomb $a_C \cdot Z(Z-1)/A^{1/3}$ | Same-flavour $(3A-2, 2)$ with $uu$-dominant support | Same-object self-braiding $\beta_{u,u}$ contributes with coefficient $\binom{Z}{2}/A^{1/3}$. |
| Asymmetry $a_{\mathrm{sym}} \cdot (N-Z)^2/A$ | $(3A-2, 1, 1)$ (isospin-defect) | Quadratic Casimir on the isospin representation. |
| Pairing $\pm a_P/\sqrt{A}$ | Parity of $\lambda$ | Hecke eigenvalues $(q, -q^{-1})$ contribute a $\pm$ sign per generator; $\sqrt{A}$ is the fluctuation size of the $\mathbb{Z}_2$-graded trace. |
| Wigner $a_W \cdot T(T{+}1)/A$ | Specht-module Casimir | Second Casimir of the Specht $S^{\lambda}$; see [Wigner 2-coefficient](#prop:wigner-2-coefficient). |
| Shell $\delta_{\mathrm{shell}}(A)$ | Rectangular $\lambda$ | Hook product $H_q(\lambda)$ factorises at rectangular diagrams; ([shell–Schur–Weyl self-duality](#prop:shell-schur-weyl-self-duality)). |

**What this means operationally.**
*In the categorical picture, the coefficient
$a_V \approx 15.67\,\mathrm{MeV}$ (BW volume) is forced to equal
$2[2]_q[7]_q \cdot m_e$ at $q = q_0$, not fit.  The
$A^{2/3}$ scaling of the surface term is forced by Weyl's
dimension formula, not empirical.  The sign alternation of the
pairing term is forced by the two Hecke eigenvalues, not
measured.  The categorical derivation therefore predicts these
coefficients without any nuclear-physics input — only the
substrate parameter $q_0$ and the reference mass $m_e$.*

**What this does **not** say.**
*The dictionary identifies each BW term with an algebraic stratum.
It does **not** claim that nuclei are well-described by summing
only these strata: the Schur–Weyl sum includes far more
partitions than BW's seven terms, and
([GB residue spectral sum](#prop:gb-residue-spectral-sum)) adds
root-of-unity residues that BW has no analogue for.  The
dictionary explains why BW works as well as it does (it captures
the dominant low-partition strata); it does not validate BW as
exact.*
