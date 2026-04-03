The vertex operator definition
([vertex operator](#def:vertex-operator)) establishes a precise
dictionary between the standard vertex operator algebra (VOA)
formalism \cite{frenkel2004} and QOU structures.

**Full translation table.**

| VOA concept | QOU realisation | Location |
|-------------|----------------|----------|
| Graded state space $V = \bigoplus V_n$ | Brane tower $\bigoplus A_n = \bigoplus J^n(A_0)$ | [brane tower](#def:recursive-brane-tower) |
| Conformal weight $n$ | Jet prolongation level $n$ | [jet prolongation](#prop:jet-prolongation) |
| Formal variable $z$ | Affine coordinate $z = v_1/v_2$ on the standard chart ($v_2 \neq 0$) of $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$; coordinate ring $\mathbb{C}[z]$ | [vertex operator](#def:vertex-operator) |
| Vertex operator $Y(a, z)$ | $R$-matrix insertion at $z \in \mathcal{S}_p$ | [R-matrix braiding](#rem:r-matrix-braiding) |
| Modes $a_m$ | Laurent coefficients of $\check{R}_{(a)}$ on $\mathcal{S}_p$ | [vertex operator](#def:vertex-operator) |
| $L_0$ (conformal weight operator) | Reeb charge: zero-mode of $\xi_q$ | [Reeb bundle](#def:reeb-bundle) |
| $L_{-1}$ (translation) | Jet prolongation $j\colon A_n \to A_{n+1}$ | [jet prolongation](#prop:jet-prolongation) |
| Vacuum $\lvert 0 \rangle$ | Unknot $1 \in A_0$ | identity of coordinate ring |
| OPE singularity $(z - w)^{-n}$ | Strand collision on $\mathcal{S}_p$; Skein resolution | [vertex operator](#def:vertex-operator) |
| OPE channels | Hecke eigenvalues $q$ (bosonic) and $-q^{-1}$ (fermionic) | [fermion action](#rem:observation-fermion-action) |
| Contour integral $\oint$ | Integration around Reeb fibre of $\mathcal{R}_p$ | [Reeb bundle](#def:reeb-bundle) |
| Correlation function $\langle Y(a_1, z_1) \cdots Y(a_k, z_k) \rangle$ | Markov trace of braid word with $k$ insertions on $\mathcal{S}_p$ | [Jones--Markov trace](#thm:jones-markov-trace) |
| Central charge $c$ | $c = 3k/(k+2)$ where $q = e^{2\pi i/(k+2)}$; relates to $\chi(\Sigma_4) = -6$ | [Bring's surface](#def:brings-surface) |
| KZ equation | Flatness of the Reeb connection on conformal blocks over $\mathrm{Conf}_n(\mathcal{S}_p)$ | — |

**Why the dictionary works.**

The connection between VOA and quantum groups is classical: the
Knizhnik--Zamolodchikov (KZ) equation for the WZW model at level $k$
has monodromy given by the $R$-matrix of
$\mathcal{U}_q(\mathfrak{su}(2))$ with $q = e^{2\pi i/(k+2)}$.
The QOU makes this correspondence geometric:

1. The "worldsheet" of the CFT **is** the exceptional divisor
   $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$.
2. The "target space" is the Reeb bundle $\mathcal{R}_p = S^3 \to \mathcal{S}_p$.
3. The "time direction" on the worldsheet is the Reeb flow $\xi_q$.
4. The "state space at fixed time" is the brane tower $\bigoplus A_n$.

The Reeb bundle thus plays a dual role: it is simultaneously the
arena for braiding
([vertex factors through $\mathcal{S}_p$](#prop:vertex-is-exceptional-divisor))
and the total space of the "string" whose quantisation produces the
vertex operator algebra.  The substrate parameter $q$ is the
exponential of the inverse level: $q = e^{2\pi i/(k+2)}$, linking
the algebraic deformation parameter to the geometric pitch of the
Reeb connection.
