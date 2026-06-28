## The open problem: $B/A$ from $q$

**Physics of $B/A$.** The binding energy per nucleon $B/A$ measures
how tightly nucleons are bound inside a nucleus. For free nucleons
(${}^1\mathrm{H}$), $B/A = 0$. For iron-56, $B/A \approx 8.79$ MeV
--- the most tightly bound nucleus. The total binding energy is
$B = Z m_\mathfrak{p} + N m_\mathfrak{n} - M_\mathrm{nucleus}$,
i.e. the mass deficit between free constituents and the actual
nucleus. $B/A$ varies smoothly from 0 (hydrogen) through a peak
near iron to $\sim$7.6 (uranium), encoding the entire nuclear
landscape.

**Significance.** Currently, $B/A$ enters our mass formula as an
external AME2020 input, making $M(Z,N)$ a tautology. If $B/A$ could
be derived from the certificate polynomial $P(q_0)$, then
$M(Z,N) = Z m_\mathfrak{p}(q) + N m_\mathfrak{n}(q) + Z m_e - A \cdot (B/A)(q)$
would be a genuine one-parameter prediction (with $m_e$ as ruler).
This is the single most important open computation in the QOU mass
programme.

**Current status.** Computing $B/A$ purely from $q$ requires deriving
the nuclear Skein polynomial volume integral from the transfer matrix
chain, without importing AME2020 values. The transfer matrix product
$\prod_i \hat{V}_i(q)$ gives the Skein polynomial $P(q)$ whose
logarithm $\ln|P(q_0)|$ grows monotonically with $A$, but the
mapping $\ln|P| \to B/A$ is not yet established.

**Approach 1: Volume integral (non-abelian Stokes).** For a single
knot $K$, mass is $\mathfrak{m}(K) = \mathrm{Vol}(K)/\hbar_q^2$.
For a multi-nucleon system with $A$ nucleons, the non-abelian Stokes
theorem expands the volume integral over the composite braid as a sum
of crossing contributions:

$$
\mathrm{Vol}(K_A) = \sum_{i < j}^A V_{ij}(q)
$$

where $V_{ij}$ is the crossing volume between nucleon strands $i$ and
$j$. Each $V_{ij}$ is computed from the $6 \times 6$ transfer matrix
at the $(i,j)$ crossing site. The binding energy is the difference
between the interacting and free volumes:

$$
B(Z,N) = \sum_\mathrm{free} \mathrm{Vol}(K_i) - \mathrm{Vol}(K_A)
$$

This is a simple sum (not a path-ordered integral) because each
crossing site contributes independently to the total volume after
Gröbner reduction.

**Approach 2: Spectral decomposition (eigenvalues of $6 \times 6$).**
The eigenvalues of the transfer matrix encode crossing energies in
each irrep channel. The binding energy may emerge as the difference
between eigenvalues of the interacting vs free Skein polynomials.
This is the same as tracking cross-channel traffic on the jet bundle
--- the $6 \times 6$ is the spectral decomposition, and each eigenvalue
corresponds to a definite irrep of $S_3$.

**Approach 3: Binding operator from NF receptivity.** The negative NF
coefficients of proton and neutron indicate which channels they are
receptive to. A binding operator $\hat{B}$ must supply what the
negative channels demand. Concretely:

- Both p and n have negative $\gamma$ and $e^-$ --- the binding
 operator must supply identity and trefoil content.
- The neutron has negative $L_+$ --- the binding operator must supply
 Hopf link content to the neutron.

**Open problem.** The outstanding computational goal is to identify a
torus knot $T(2,k)$ whose normal form, when applied to both proton
and neutron simultaneously, fills their negative channels and yields
$B/A$ matching the AME2020 curve. The candidate must have positive
$\gamma$, positive $e^-$, and positive $L_+$ coefficients. The
Borromean link $B_3 = (\sigma_0\sigma_1^{-1})^3$ already provides
exactly this pattern with $\mathrm{net}(B_3) = +1.000$,
$L_+ = +0.046$, $L_- = -0.044$, but operates at the single-nucleon
(gluon) level, not the inter-nucleon binding level.

**Approach 4:** Certificate polynomial roots --- the tr\_alt
polynomial's root structure at $q = q_0$ may encode binding through
level repulsion.
