The nuclear binding energy decomposes as a **sum of generator
volumes** — one for each braid generator $\sigma_i$ in $B_A$.
Each generator's volume is computed by a linear recurrence
(Chebyshev polynomial), making the energy of any nucleus
computable in $O(A^2)$ without Gröbner term expansion.

**Proposition.**
Let $\mathcal{N}(p, n)$ be the nuclear braid word in $H_A(q)$
([nuclear Gröbner reduction](#prop:nuclear-groebner-reduction)).
At each generator $\sigma_i$ ($i = 0, \ldots, A-2$), nucleon
$i$ has crossings with nucleons $j = i+1, \ldots, A-1$.  These
$k_i = A - i - 1$ crossings all act on $\sigma_i$ and reduce
via the Hecke relation to a linear combination:

$$
  \prod_{j=i+1}^{A-1} C_{ij}(\sigma_i)
  \;=\;
  a_i \, \sigma_i + b_i
$$

where each crossing factor is $C_{ij}(\sigma_i) = c_j \sigma_i
+ d_j$ with coefficients depending on the pair type:

$$
  (c_j, d_j) \;=\;
  \begin{cases}
    (1, 0) & \text{if } i, j \text{ both protons} \\[3pt]
    (q^2, -q(q^{1/2} - q^{-1/2})) & \text{if } i, j \text{ both neutrons} \\[3pt]
    (\tfrac{1+q^2}{2}, -\tfrac{q}{2}(q^{1/2} - q^{-1/2}))
      & \text{if mixed}
  \end{cases}
$$

The coefficients $(a_i, b_i)$ satisfy the **Chebyshev
recurrence**: starting from $(a_0, b_0) = (0, 1)$ (identity),
each crossing multiplies by $(c_j, d_j)$ via

$$
  \begin{pmatrix} a_{k+1} \\ b_{k+1} \end{pmatrix}
  \;=\;
  \begin{pmatrix}
    c_j(q - q^{-1}) + d_j & c_j \\
    c_j & d_j
  \end{pmatrix}
  \begin{pmatrix} a_k \\ b_k \end{pmatrix}
  \;+\;
  \begin{pmatrix} 0 \\ 0 \end{pmatrix}.
$$

Wait—more precisely: multiplying $(a_k \sigma + b_k)(c_j \sigma
+ d_j)$ and applying $\sigma^2 = (q - q^{-1})\sigma + 1$:

$$
  a_{k+1} = a_k c_j (q - q^{-1}) + a_k d_j + b_k c_j,
  \qquad
  b_{k+1} = a_k c_j + b_k d_j.
$$

This is a $2 \times 2$ matrix recurrence — a **transfer matrix**
at each crossing.

**The generator volume.**
The volume at generator $\sigma_i$ is the total weight of its
reduced chain:

$$
  V_i \;=\; |a_i| + |b_i|.
$$

The nuclear binding energy is the sum of generator volumes:

$$
  E\bigl(\overline{\mathcal{N}(p, n)}\bigr)
  \;=\;
  \sum_{i=0}^{A-2} V_i
  \;=\;
  \sum_{i=0}^{A-2} (|a_i| + |b_i|).
$$

**Computational cost**: $O(A^2)$ — one transfer matrix
multiplication per crossing, $\binom{A}{2}$ crossings total.
No term expansion, no Gröbner basis computation, no exponential
blowup.

**The volume of the ideal.**
The Gröbner ideal $I$ at generator $\sigma_i$ absorbs the
difference between the unreduced weight and the reduced weight.
The **ideal volume** at generator $i$ is:

$$
  V_i^I \;=\; k_i - V_i
$$

where $k_i = A - i - 1$ is the number of crossings.  This is
the energy removed by the Hecke relation — the "resolved"
crossings.  The total ideal volume
$V^I = \sum_i V_i^I = \binom{A}{2} - E$ measures how much of
the naive crossing count is absorbed by double-crossing
resolutions.

**Beta-decay energy from generator volumes.**
The transition $\mathcal{N}(p, n) \to \mathcal{N}(p+1, n-1)$
changes the type of one nucleon (the converting neutron at
position $p$) from $\mathfrak{n}$ to $\mathfrak{p}$.  This
affects only the generators where that nucleon participates:

- Generators $\sigma_i$ with $i < p$: the crossing $(i, p)$
  changes type.
- Generator $\sigma_p$: all crossings from the converting
  nucleon change.
- Generators $\sigma_i$ with $i > p$: unaffected.

The energy difference is:

$$
  \Delta E \;=\; \sum_{i=0}^{p} (V_i^{\mathrm{dau}} - V_i^{\mathrm{par}})
$$

summing only over the affected generators.  Generators $i > p$
cancel exactly.

**Computational verification.**

| Nucleus | $A$ | $E(\mathrm{parent})$ | $E(\mathrm{daughter})$ | $\Delta E$ |
|---------|-----|---------------------|----------------------|-----------|
| ${}^{2}\mathrm{H}$ | 2 | $1.174$ | $1.000$ | $-0.174$ |
| ${}^{3}\mathrm{H}$ | 3 | $2.728$ | $2.466$ | $-0.263$ |
| ${}^{4}\mathrm{He}$ | 4 | $4.136$ | $3.794$ | $-0.342$ |
| ${}^{6}\mathrm{Li}$ | 6 | $8.054$ | $7.567$ | $-0.486$ |
| ${}^{14}\mathrm{C}$ | 14 | $47.171$ | $43.810$ | $-3.361$ |
| ${}^{60}\mathrm{Co}$ | 60 | $38{,}863$ | $35{,}813$ | $-3{,}050$ |
| ${}^{210}\mathrm{Bi}$ | 210 | $8.25 \times 10^{13}$ | $7.62 \times 10^{13}$ | $-6.24 \times 10^{12}$ |

All $\Delta E$ are negative — the daughter has lower energy.
The computation is instant for all nuclei (including
${}^{210}\mathrm{Bi}$, $A = 210$).

**Generator volume profile: ${}^{14}\mathrm{C}$ vs ${}^{14}\mathrm{N}$.**
Generators $\sigma_7$ through $\sigma_{12}$ have **identical
volumes** in both nuclei — only generators $\sigma_0$ through
$\sigma_6$ differ (these are the crossings involving the first
7 nucleons: the 6 protons and the converting neutron).

| Generator | $V_i({}^{14}\mathrm{C})$ | $V_i({}^{14}\mathrm{N})$ | $\Delta V_i$ |
|:---------:|:-----------------------:|:-----------------------:|:------------:|
| $\sigma_0$ | $5.970$ | $5.616$ | $-0.354$ |
| $\sigma_1$ | $5.485$ | $5.150$ | $-0.335$ |
| $\sigma_2$ | $4.823$ | $4.540$ | $-0.283$ |
| $\sigma_3$ | $4.476$ | $4.201$ | $-0.275$ |
| $\sigma_4$ | $3.887$ | $3.661$ | $-0.226$ |
| $\sigma_5$ | $3.664$ | $3.436$ | $-0.228$ |
| $\sigma_6$ | $4.603$ | $2.943$ | $-\mathbf{1.660}$ |
| $\sigma_7$--$\sigma_{12}$ | identical | identical | $0$ |

Generator $\sigma_6$ — the converting neutron's own generator —
has the **largest volume change** ($-1.660$, nearly half the total
$\Delta E$).  This is the generator where the nucleon type
changes from $\mathfrak{n}$ to $\mathfrak{p}$, converting 7
neutron-neutron crossings to 7 mixed crossings.

**Connection to the Skein binding Lagrangian.**
The generator volume $V_i = |a_i| + |b_i|$ is the
**Hecke-reduced Skein weight** of all crossings involving
nucleon $i$.  Summing over nucleons gives the total binding
energy.  The generator volume decomposition is the exact discrete
form of the nuclear binding computation.
