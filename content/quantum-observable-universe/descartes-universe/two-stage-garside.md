Let $\mathcal{A}(Z, N)$ be a nucleus with $A = Z + N$ nucleons.
Each nucleon is a Borromean triple of quarks
([Borromean baryon](#def:borromean-baryon)):
proton $\mathfrak{p} = (u, u, d)$, neutron $\mathfrak{n} = (u, d, d)$.
The nucleus has $3A$ quark strands.

The **two-stage Garside element** is the element
$\mathcal{G}_{3A} \in H_{3A}(q)$ constructed in two stages,
both within the same Garside staircase.

## Stage 1: Intra-nucleon confinement ($\mathcal{B}_3$)

For each nucleon $k = 0, \ldots, A-1$, the quarks at strand
positions $\{3k, 3k{+}1, 3k{+}2\}$ are confined by the
Borromean braid $\mathcal{B}_3$.  The Garside staircase within
each triple produces $\binom{3}{2} = 3$ typed crossings:

```tex
\begin{equation}\label{eq:stage1-confinement}
  \mathcal{B}_3^{(k)}
  \;=\;
  C(q_{3k{+}1}, q_{3k{+}2};\, \sigma_{3k{+}1})
  \;\cdot\;
  C(q_{3k}, q_{3k{+}2};\, \sigma_{3k})
  \;\cdot\;
  C(q_{3k}, q_{3k{+}1};\, \sigma_{3k})
\end{equation}
```

where $q_i \in \{u, d\}$ is the quark flavor at position $i$
and $C(f_i, f_j; \sigma_m)$ is the typed crossing operator
([typed crossing](#def:typed-crossing-operator)).

This stage is determined by the LP-optimal confinement
([confinement LP](#prop:confinement-lp)): $\mathcal{B}_3$ is the
unique vertex of the linear program minimizing the categorical action
$|\mathrm{tr}_M(\Phi)|$ subject to Frobenius positivity $Gx \geq 0$.
No choice enters.

Total Stage 1 crossings: $3A$.

## Stage 2: Inter-nucleon crossings

After confinement, the inter-nucleon crossings pair every quark
in nucleon $a$ with every quark in nucleon $b$ ($a < b$).
For each nucleon pair $(a, b)$, the $3 \times 3 = 9$ quark-quark
crossings are:

$$
  C(q_{3a+i},\, q_{3b+j};\, \sigma_{3a+i})
  \qquad
  i \in \{0,1,2\},\;\; j \in \{0,1,2\}
$$

ordered by the Garside staircase in $H_{3A}(q)$: level by level,
sweeping right to left at each level.

Total Stage 2 crossings: $9 \binom{A}{2}$.

## Combined construction

The two stages are NOT separate algebraic operations.  They are
consecutive portions of the **single Garside staircase** in
$H_{3A}(q)$.  The quark ordering
$[q_0, q_1, q_2, q_3, q_4, q_5, \ldots]$ places each nucleon's
quarks in adjacent positions:

$$
  [\underbrace{u, u, d}_{\mathfrak{p}},\;
   \underbrace{u, d, d}_{\mathfrak{n}},\;
   \underbrace{u, d, d}_{\mathfrak{n}},\; \ldots]
$$

The Garside staircase in $H_{3A}(q)$ then naturally processes
intra-nucleon crossings first (strands within each triple are
adjacent) before reaching inter-nucleon crossings (strands in
different triples).

```tex
\begin{equation}\label{eq:two-stage-garside}
  \mathcal{G}_{3A}
  \;=\;
  \prod_{\ell=0}^{3A-2}
  \;\prod_{s=\ell}^{0}
  C(q_s,\, q_{\ell+1};\, \sigma_s)
\end{equation}
```

with
$\binom{3A}{2} = 3A + 9\binom{A}{2}$
total crossings, reduced to Gröbner--Shirshov normal form under
the braiding-induced ordering
([braiding-induced ordering](#prop:braiding-induced-ordering)).

## Crossing count verification

$$
  \binom{3A}{2}
  = \frac{3A(3A-1)}{2}
  = \underbrace{A \cdot 3}_{\text{intra}}
  + \underbrace{9 \cdot \frac{A(A-1)}{2}}_{\text{inter}}
  = 3A + \frac{9A(A-1)}{2}
$$

Verification: $3A + 9A(A-1)/2 = A(3 + 9(A-1)/2) = A(6 + 9A - 9)/2
= A(9A - 3)/2 = 3A(3A-1)/2 = \binom{3A}{2}$.  $\checkmark$

## Typed crossing coefficients

All crossings use the quark-level typed coefficients
([typed crossing](#def:typed-crossing-operator)):

$$
  d(u, u) = 0, \qquad
  d(d, d) = -(q - q^{-1}), \qquad
  d(u, d) = d(d, u) = -\tfrac{1}{2}(q - q^{-1}).
$$

No averaging, no approximation.  The coefficients are
**symbolic in $q$** — exact elements of $\mathbb{Z}[q, q^{-1}]$.
Evaluation at $q = q_0$ occurs only at the final step.

## Examples

| Nucleus | $A$ | $3A$ | Intra | Inter | Total | NF terms |
|:-------:|:---:|:----:|:-----:|:-----:|:-----:|:--------:|
| $p$ (proton) | $1$ | $3$ | $3$ | $0$ | $3$ | — |
| ${}^2\mathrm{H}$ (deuteron) | $2$ | $6$ | $6$ | $9$ | $15$ | — |
| ${}^3\mathrm{H}$ (tritium) | $3$ | $9$ | $9$ | $27$ | $36$ | — |
| ${}^4\mathrm{He}$ | $4$ | $12$ | $12$ | $54$ | $66$ | — |
| ${}^6\mathrm{He}$ | $6$ | $18$ | $18$ | $135$ | $153$ | — |
