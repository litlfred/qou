**Proposition (decomposition of the Hecke log-deformation factor).**

*Let $h := q - q^{-1}$ be the Hecke skein deformation and
$\hbar_q := (q - 1)/q$ the QOU quantum Planck constant
([`prop:boltzmann-constant`](#prop:boltzmann-constant)). Then for
every $q > 0$,*

$$
\boxed{\quad
  \log\!\frac{1}{h(q)}
  \;=\;
  \log\!\frac{1}{\hbar_q}
  \;-\;
  \log(1 + q).
\quad}
$$

## Proof

Compute directly. The skein deformation factors:
$$
  h
  \;=\;
  q - q^{-1}
  \;=\;
  \frac{q^2 - 1}{q}
  \;=\;
  \frac{(q-1)(q+1)}{q}
  \;=\;
  \hbar_q \cdot (q + 1).
$$
Taking the reciprocal and the natural logarithm,
$$
  \log\!\frac{1}{h}
  \;=\;
  \log\!\frac{1}{\hbar_q (q+1)}
  \;=\;
  \log\!\frac{1}{\hbar_q}
  \;-\;
  \log(1 + q).
$$
∎

## Numerical verification at $q_0$

At the substrate parameter $q_0 = 1.109978595554181\ldots$ (50 dps):

See [Table](#tbl:hecke-log-decomposition-table-data).

The decomposition is verified to $10^{-50}$ via
[`probe_delta_coupling_q_edgeworth.py`](computations/probe_delta_coupling_q_edgeworth.py)
and the substrate-derivation audit
[`2026-05-17-delta-coupling-substrate-derivation.md`](../../../docs/audits/2026-05-17-delta-coupling-substrate-derivation.md).

## Physical interpretation

The two pieces of the decomposition carry distinct QOU substrate
meanings:

- $\log(1/\hbar_q)$ is the **Shannon–Boltzmann free-energy log** at
  the QOU Hecke-thermal scale. Per
  [`prop:boltzmann-constant`](#prop:boltzmann-constant),
  $k_B T_q = \hbar_q$, so $\log(1/\hbar_q) = \log(1/(k_B T_q))$ is
  the standard thermodynamic free-energy log per excitation.
- $\log(1 + q)$ is a **skein-convention normalisation** that arises
  because the Iwahori–Hecke algebra is symmetric in $q \leftrightarrow q^{-1}$
  via the skein eigenvalue pair $\{q, -q^{-1}\}$, whereas the
  thermodynamic scale $\hbar_q$ is one-sided. The factor $(q + 1)$
  absorbs the eigenvalue-pair sum $q + 1 = q - (-1) = q - (-q^0)$.

Together these decompose the bare Hecke log into a thermodynamic
term and a substrate-specific normalisation. This decomposition was
used in the Δ_coupling closed-form claim (since refuted at
single-magic anchors; the substrate Δ_coupling derivation
remains open research).
