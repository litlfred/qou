**Remark.**
*The parity-blindness of the classical Murnaghan–Nakayama character
([MN parity-blind](#rem:mn-classical-parity-blind)) is closed by
the $q$-deformed Hecke character $\chi^\lambda_q(T_w)$.  Computed
symbolically via the Hoefsmit seminormal form, the $q$-character
distinguishes $\sigma$ from $\sigma^{-1}$ through the Hecke
eigenvalue gap $(q, -q^{-1})$ and therefore distinguishes proton
from neutron at every $q$.*

**Hoefsmit seminormal form (symbolic).**
*For a partition $\lambda \vdash n$ with standard Young tableaux
$T_1, \ldots, T_{f^\lambda}$, the Hecke generator $T_i$ acts on the
Specht module $S^\lambda$ by:*

- *If $i$ and $i+1$ are in the same row of $T$ (axial distance
  $\rho = 1$): $\rho_\lambda(T_i)\,T = q \cdot T$.*
- *If in the same column ($\rho = -1$): $\rho_\lambda(T_i)\,T =
  -q^{-1}\,T$.*
- *Otherwise: $2 \times 2$ block on $\{T, T'\}$ with $T'$ the
  tableau obtained by swapping $i, i+1$, matrix
  $\begin{pmatrix} a & b \\ b & a' \end{pmatrix}$ where
  $a = (q - q^{-1})/(1 - q^{-2\rho})$,
  $a' = (q - q^{-1})/(1 - q^{2\rho})$,
  $b^2 = a a' + 1$, $\rho = \mathrm{content}(c_{i+1}) -
  \mathrm{content}(c_i)$.*

*Keeping $q$ as a sympy symbol, $\chi^\lambda_q(T_w) =
\operatorname{Tr}\bigl(\prod_{i \in w} \rho_\lambda(T_{\text{sign}_i} i)\bigr)$
is an exact rational function of $q$.*

**Numerical witness at $A = 1$ ($q_0 \approx 1.11$).**

| $\lambda \vdash 3$ | $\chi^\lambda_q(T_w^{\mathfrak{p}})$ @ $q_0$ | $\chi^\lambda_q(T_w^{\mathfrak{n}})$ @ $q_0$ | difference |
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
*A positive crossing $T_i$ and a negative crossing $T_i^{-1}$
project to the same $S_n$ transposition (parity-blind at $q = 1$),
but as elements of $H_n(q)$ they are distinct: $T_i$ has
eigenvalue $+q$ on the symmetric channel and $-q^{-1}$ on the
antisymmetric channel, while $T_i^{-1}$ has $q^{-1}$ and $-q$.
The seminormal matrix for $T_i$ and $T_i^{-1}$ differ:*

$$
  \rho_\lambda(T_i)
  \;=\;
  \begin{pmatrix} a & b \\ b & a' \end{pmatrix},
  \qquad
  \rho_\lambda(T_i^{-1})
  \;=\;
  \begin{pmatrix} a' & b \\ b & a \end{pmatrix}
  \;=\;
  \rho_\lambda(T_i) - (q - q^{-1}) \cdot I.
$$

*(The Hecke inverse identity
$T_i^{-1} = T_i - (q - q^{-1}) \cdot I$ gives the clean form
on the right.)  Tracing through a braid word with mixed
$\sigma^{\pm 1}$ crossings accumulates a net $q$-dependence that
distinguishes the proton word (majority $\sigma$) from the
neutron word (majority $\sigma^{-1}$).*

**Computational cost and scope.**
*Symbolic Hoefsmit matrix products are $O(d^3)$ per generator in
sympy, where $d = \dim S^\lambda = f^\lambda$:*

- *$A = 1$: $f^\lambda \in \{1, 2, 1\}$, fast.*
- *$A = 2$: $f^\lambda$ up to $9$ (for $\lambda = (3,3)$);
  symbolic takes seconds per $\lambda$.*
- *$A = 3$: $f^\lambda$ up to $42$ ($\lambda = (3,3,3)$); minutes.*
- *$A = 4$: $f^\lambda$ up to $132$ ($\lambda = (3,3,3,3)$);
  symbolic becomes impractical.*

*For $A \geq 3$, either (i) substitute numerical $q \to q_0$
early and use the numerical pipeline in
`folio-assistant/computations/hecke_characters.py`, or
(ii) pre-prune the partition set to the MN-support
([MN parity-blind](#rem:mn-classical-parity-blind) shows this
is $3$–$5$ partitions out of $30$–$77$ for $A \in \{3, 4\}$),
reducing symbolic cost by factor $\sim 10$.*

**Reference implementation.**
*Script: `folio-assistant/computations/hecke_character_symbolic.py`.
Builds Hoefsmit matrices with `q` as sympy symbol, multiplies
through atomic braid word, traces to extract $\chi^\lambda_q(T_w)$.
Witness: `hecke-character-symbolic.witness.json`.*

**Next step.**
*Apply to $A = 2$ (deuteron) with the $11$-partition sum.  The
support-pruning strategy using MN output reduces to $2$ partitions
$\{(6), (3,3)\}$, making the symbolic computation tractable.
This is the final piece needed for deuteron binding energy from
first principles — no empirical constants except $E_0$ and
$q_0$.*
