Independent audit of the tritium $\beta$-decay Q-value derivation
${}^3\mathrm{H} \to {}^3\mathrm{He} + e^- + \bar\nu_e$, verifying
each step of [prop:tritium-qvalue-symbolic](#prop\:tritium-qvalue-symbolic)
for fitted parameters and hidden assumptions.  This block is
purely audit; the canonical statement and proof of the closed-form
Q-value formula live with the proposition.

## Derivation chain (verified against the proposition)

**Step 0: Substrate parameter** (1 measurement consumed).

$$
  \hbar_q = \sqrt{\mathrm{Vol}(4_1) / (m_\mu/m_e)},
  \quad
  q_0 = \frac{1}{1 - \hbar_q} \approx 1.10998
$$

Three inputs: $\mathrm{Vol}(4_1) = :val[Vol_4_1]{precision=6}$ (mathematical constant),
$m_\mu/m_e = 206.7683$ (CODATA), $m_e = 0.5110$ MeV (CODATA).
The first fixes $q_0$; the second sets the energy scale.

**Step 1: Typed crossing operator** (structural postulate).

| Pair | Hecke element                                       | Justification                                  |
| ---- | --------------------------------------------------- | ---------------------------------------------- |
| $uu$ | $\sigma$                                            | Positive crossing                              |
| $dd$ | $\sigma^{-1} = \sigma - h$                          | Negative crossing (Hecke relation)             |
| $ud$ | $\tfrac{1}{2}(\sigma + \sigma^{-1}) = \sigma - h/2$ | Arithmetic mean (**isospin-invariant choice**) |

The $\lambda = \tfrac{1}{2}$ coefficient is the unique value invariant
under $u \leftrightarrow d$ (isospin flip $\sigma \leftrightarrow \sigma^{-1}$).
The Hecke algebra does not determine $\lambda$ — it treats all generators
identically regardless of strand content.  The choice $\lambda = 1/2$ is
natural but not derived from representation theory.

**Step 2: Per-nucleon Garside factors** (verified analytically).

The trefoil operator $T_{2,3} = \sigma_0\sigma_1\sigma_0$ in $H_3(q)$
has four eigenspaces (trivial $q^3$, confining $q^{-1}$, unconfining
$-q$, sign $-q^{-3}$).  The typed Garside element is projected onto
each eigenspace via Young's seminormal form:

$$
  G_P(c) = \langle v_c | \Delta_3(uud) | v_c \rangle,
  \quad
  G_N(c) = \langle v_c | \Delta_3(udd) | v_c \rangle
$$

**Independently verified** using the repo's seminormal form implementation:

| Channel            |  $G_P$ (proton)  | $G_N$ (neutron) |
| ------------------ | :--------------: | :-------------: |
| sym ($q^3$)        |     $+1.122$     |     $+0.911$    |
| std$_1$ ($-q$)     |     $-1.174$     |     $-1.222$    |
| std$_2$ ($q^{-1}$) |     $+0.858$     |     $+0.800$    |
| alt ($-q^{-3}$)    |     $-0.911$     |     $-1.122$    |
| **Sum**            | $-0.1045 = -h/2$ |    $-0.6340$    |

The channel sums are:

$$
  a = -\frac{h}{2}, \quad
  b = -\frac{3(q^2-1)(q^2+1)^2}{4q^3}
$$

Both confirmed to machine precision.

**Step 3: Branching factorization** (algebraically exact).

$$
  \sum_{4^A \text{ configs}} \Delta m_e
  = a^Z \cdot b^{N-1} \cdot (a - b)
$$

For tritium $(Z=1, N=2)$: $Q/m_e = |a \cdot b \cdot (a-b)|$.

**Step 4: Closed form** (pure algebra, verified).

$$
  Q = \frac{3(q^2-1)^3(q^2+1)^2(3q^4+4q^2+3)}{32q^7} \times m_e
  \approx 0.01793 \text{ MeV}
$$

Experimental: $Q_{\mathrm{exp}} = 0.01861$ MeV.  Error: $-3.6\%$.

## Audit findings

### Verified (no issues)

1. **Channel sums $a$ and $b$**: confirmed from the full seminormal
   form of $H_3(q)$ using $T_{2,3}$ eigenspace projections.
2. **Branching factorization**: algebraically exact given $a$ and $b$.
3. **Closed-form algebra**: verified numerically to machine precision.
4. **Zero continuously-tunable fitted parameters**: the entire chain
   uses $q_0$ (from $m_\mu/m_e$) and $m_e$ (energy scale), nothing else.

### Structural postulates (not fitted, but not derived)

1. **$\lambda = 1/2$ mixing**: the unique isospin-invariant choice.
   Sensitivity analysis shows the Q-value is moderately sensitive
   to $\lambda$: a shift of $\pm 0.1$ changes $Q$ by $\sim 50\%$.
   The isospin symmetry argument is strong but not a derivation.

2. **Energy unit $m_e$**: consistent with the 2-input calibration
   scheme.  The categorical quantity map identifies $m_e$ as the
   natural unit via $Q = \sum_\lambda \chi_\lambda(\Delta) \times m_e$.

3. **$\mathrm{Vol}(4_1)$ in mass ratio**: consumed as calibration
   Input #1 to fix $q_0$.  The identification of $4_1$ with the
   Higgs field (mass mechanism) is a postulate from the knot-particle
   dictionary; the coupling $m_\mu \propto \mathrm{Vol}(4_1)$ is
   not derived from first principles.

### Resolved: two computation paths

The branching factorization ($-3.6\%$) and the Gröbner--Shirshov
$H_9$ verification ($-57\%$) are **not competing models**.  They
compute different quantities at different levels of description:

|                    | Branching               | Gröbner $H_9$                |           |    |                    |           |
| ------------------ | ----------------------- | ---------------------------- | --------- | -- | ------------------ | --------- |
| Algebra            | Per-nucleon $H_3(q)$    | Full quark-level $H_9(q)$    |           |    |                    |           |
| Dimensionless part | \$                      | ab(a-b)                      | = 0.035\$ | \$ | \Delta\mathrm{net} | = 0.449\$ |
| Energy scale       | $m_e \approx 0.511$ MeV | $\kappa_q \approx 0.018$ MeV |           |    |                    |           |
| Inputs consumed    | 2 ($q_0$, $m_e$)        | 2 ($q_0$, $\kappa_q$)        |           |    |                    |           |

The branching path uses the per-nucleon channel decomposition in
$H_3(q)$; the Gröbner path uses the full 9-strand braid with
Borromean confinement.  The Gröbner path's $-57\%$ error reflects
the cruder energy scale $\kappa_q = \ln(q) m_e/3$ rather than $m_e$.

### Formula is not a knot invariant

The expression $Q/m_e = 3(q^2-1)^3(q^2+1)^2(3q^4+4q^2+3)/(32q^7)$
is **not** the Jones polynomial (or any Skein polynomial) of a
specific knot.  In quantum-integer notation:

$$
  Q/m_e = \frac{3}{32} (q-q^{-1})^3 (q+q^{-1})^2 (3[2]_q^2 - 2)
$$

The irreducible factor $3q^4+4q^2+3$ (discriminant $-20$) has no
knot-theoretic interpretation.  The formula arises from algebraic
manipulation of the branching factorization, not from topology.
