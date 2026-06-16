**Remark.**
*The parity-blindness of the classical Murnaghan–Nakayama character
([MN parity-blind](#rem:mn-classical-parity-blind)) is closed by
the $q$-deformed Hecke character $\chi^\lambda_q(\sigma_w)$.  Computed
symbolically via the Hoefsmit seminormal form, the $q$-character
distinguishes $\sigma$ from $\sigma^{-1}$ through the Hecke
eigenvalue gap $(q, -q^{-1})$ and therefore distinguishes proton
from neutron at every $q$.*

**Hoefsmit seminormal form (symbolic).**
*For a partition $\lambda \vdash n$ with standard Young tableaux
$T_1, \ldots, T_{f^\lambda}$ (indexing the Specht-module basis;
distinct from the Hecke generator $\sigma_i$), the Hecke generator
$\sigma_i$ acts on the Specht module $S^\lambda$ by:*

- *If $i$ and $i+1$ are in the same row of $T$ (axial distance
  $\rho = 1$): $\rho_\lambda(\sigma_i)\,T = q \cdot T$.*
- *If in the same column ($\rho = -1$): $\rho_\lambda(\sigma_i)\,T =
  -q^{-1}\,T$.*
- *Otherwise: $2 \times 2$ block on $\{T, T'\}$ with $T'$ the
  tableau obtained by swapping $i, i+1$, matrix
  $\begin{pmatrix} a & b \\ b & a' \end{pmatrix}$ where
  $a = (q - q^{-1})/(1 - q^{-2\rho})$,
  $a' = (q - q^{-1})/(1 - q^{2\rho})$,
  $b^2 = a a' + 1$, $\rho = \mathrm{content}(c_{i+1}) -
  \mathrm{content}(c_i)$.*

*Keeping $q$ as a sympy symbol,
$\chi^\lambda_q(\sigma_w) =
\operatorname{Tr}\bigl(\prod_{i \in w} \rho_\lambda(\sigma_i^{\,\varepsilon_i})\bigr)$,
where $\varepsilon_i = \pm 1$ is the sign of the $i$-th letter in $w$,
is an exact rational function of $q$.*

**Numerical witness at $A = 1$ ($q_0 \approx 1.11$).**

| $\lambda \vdash 3$ | $\chi^\lambda_q(\sigma_w^{\mathfrak{p}})$ @ $q_0$ | $\chi^\lambda_q(\sigma_w^{\mathfrak{n}})$ @ $q_0$ | difference |
|---|---|---|---|
| $(3)$ | $+1.3825$ | $+1.1221$ | $+0.2604$ |
| $(2,1)$ | $+3.1902$ | $+2.3874$ | $+0.8028$ |
| $(1,1,1)$ | $+4.2587$ | $+2.7419$ | $+1.5167$ |

*All three partitions differ nontrivially between proton and
neutron — in sharp contrast to the classical MN case where all
characters were identical.*

**Schur–Weyl trace at $A = 1$:**

$$
  |\mathrm{tr}_M(\mathfrak{p})|_{q_0} = 3.036, \qquad
  |\mathrm{tr}_M(\mathfrak{n})|_{q_0} = 2.331, \qquad
  Q_{\mathrm{cat}} = -0.7052.
$$

*$\beta$-decay calibration now succeeds:
$E_0 = 0.782\,\mathrm{MeV} / |Q_{\mathrm{cat}}| = 1.109\,\mathrm{MeV}$/cat.unit.
The q-deformation restores the structural information lost in
the classical limit.*

**Why the $q$-character sees the sign.**
*A positive crossing $\sigma_i$ and a negative crossing $\sigma_i^{-1}$
project to the same $S_n$ transposition (parity-blind at $q = 1$),
but as elements of $H_n(R, q)$ they are distinct: $\sigma_i$ has
eigenvalue $+q$ on the symmetric channel and $-q^{-1}$ on the
antisymmetric channel, while $\sigma_i^{-1}$ has $q^{-1}$ and $-q$.
The seminormal matrix for $\sigma_i$ and $\sigma_i^{-1}$ differ:*

$$
  \rho_\lambda(\sigma_i)
  \;=\;
  \begin{pmatrix} a & b \\ b & a' \end{pmatrix},
  \qquad
  \rho_\lambda(\sigma_i^{-1})
  \;=\;
  \begin{pmatrix} a' & b \\ b & a \end{pmatrix}
  \;=\;
  \rho_\lambda(\sigma_i) - (q - q^{-1}) \cdot I.
$$

*(The Hecke inverse identity
$\sigma_i^{-1} = \sigma_i - (q - q^{-1}) \cdot I$ gives the clean form
on the right.)  Tracing through a braid word with mixed
$\sigma^{\pm 1}$ crossings accumulates a net $q$-dependence that
distinguishes the proton word (majority $\sigma$) from the
neutron word (majority $\sigma^{-1}$).*

**Computational cost and scope.**
*Symbolic Hoefsmit matrix products are $O(d^3)$ per generator in
sympy, where $d = \dim S^\lambda = f^\lambda$:*

- *$A = 1$: $f^\lambda \in \{1, 2, 1\}$, fast; the values above
  are exact.*
- *$A \geq 2$: $f^\lambda$ up to $16$ (for $\lambda = (3,2,1)$
  at $A=2$) and up to $132$ at $A=4$; symbolic cost becomes
  prohibitive.  For $A \geq 2$ use the **numerical**
  Hoefsmit pipeline in
  `computations/hecke/hecke_characters.py`
  (well-tested, handles 2$\times$2 block $b^2$ sign with
  `sqrt(abs(b^2))` where the symbolic expression can turn
  negative off the unitary locus).*

**Correction to an earlier claim.**
*An earlier draft asserted that the classical Murnaghan–Nakayama
character's support equals the Hecke $q$-character's support
(i.e., MN-support pruning is valid).  This is **false** for
general braid words.  It holds only when $\sigma_w$ is a pure
standard-basis element $T_v$ for some $v \in S_n$: then
$\chi^\lambda_q(T_v)$ is a $q$-deformation of $\chi^\lambda(v)$
and shares its support.  For a braid word $T_{i_1}T_{i_2}\cdots
T_{i_k}$ with mixed $\sigma^{\pm 1}$, the Hecke relations
$\sigma_i^2 = (q-q^{-1})\sigma_i + I$ expand the product into a linear
combination $\sum_v c_v(q)\,T_v$ over many $v$ with different
cycle types.  The $q$-character pulls in all of them, so the
effective support can be strictly larger than the
MN-support on any single $v$.  Pruning to the MN-support at
$A \geq 2$ produces a **biased** result and is not used.*

**Reference implementation.**
*Script: `computations/hecke/hecke_character_symbolic.py`.
Builds Hoefsmit matrices with `q` as sympy symbol, multiplies
through atomic braid word, traces to extract $\chi^\lambda_q(\sigma_w)$.
Witness: `hecke-character-symbolic.witness.json`.*

**Next step.**
*Apply the numerical pipeline in
`computations/hecke/hecke_characters.py` (full $H_{3A}$
Wedderburn sum) to $A = 2$ (deuteron) with all $11$ partitions of
$6$, weighted by the exact symbolic $w_\lambda(q_0)$.  The
numerical Hoefsmit handles the 2$\times$2 block $b^2$ sign robustly.
This is the final piece needed for deuteron binding energy from
first principles — the only inputs are $E_0$ ($\beta$-decay) and
$q_0$ (substrate).*
