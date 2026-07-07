<!-- FILE_START: mass-formula-derivation-commutative-chirality-vanishes-intro.md -->
Continuation of the preceding sub-section.

This sub-section derives the mass formula on the commutative substrate.  The arc proceeds through the Frobenius-S classification (a two-table substrate-level catalogue), pins the commutative-chirality-vanishes result, and exhibits the derived mass formula for light isotopes with table data.  The closing blocks specialise to the deuteron binding energy in the Frobenius codimension framework — the chapter's lightest non-trivial benchmark.
<!-- FILE_END: mass-formula-derivation-commutative-chirality-vanishes-intro.md -->

<!-- FILE_START: commutative-chirality-vanishes.md -->
**Corollary** (of [Frobenius S-classification](#prop:frobenius-s-classification)
applied in the [commutative QOU](#def:commutative-qou) limit).
*In the commutative specialisation $q \to 1$, the chirality term
$H_A^2 \Phi_3$ in the Wedderburn mass formula
([Wedderburn mass formula](#thm:wedderburn-mass-formula)) vanishes
identically:*

$$
  \lim_{q \to 1} H_A^2 \cdot \Phi_3 = 0.
$$

*Consequently the commutative atomic mass formula reduces to the
two-term expression*

$$
  \mathcal{M}^{\mathrm{class}}(Z, N) = Z\,\mathfrak{m}_{\mathfrak{p}} + N\,\mathfrak{m}_{\mathfrak{n}} + Z\,m_e + \alpha \bigl(\Phi_1 - 6\,\Phi_2\bigr),
$$

*where $\alpha = m_e \cdot 8G$ and $\lim_{q \to 1} [3]_q = 3$.*

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: commutative-chirality-vanishes.md -->

<!-- FILE_START: commutative-chirality-vanishes-interpretation.md -->
**Remark (significance).**
The Frobenius--Hopf antipode is trivial in the commutative QOU
($S = \mathrm{id}$ when the multiplication is commutative), so any
$S$-anti-invariant degree of freedom must vanish. The chirality
$\Phi_3$ — the unique $S$-odd channel by
[Frobenius S-classification](#prop:frobenius-s-classification) —
is therefore identically zero in the classical limit, and the
mass formula degenerates to the two surviving $S$-even invariants
$\Phi_1$ (trace) and $\Phi_2$ (determinant).
<!-- FILE_END: commutative-chirality-vanishes-interpretation.md -->

<!-- FILE_START: derived-mass-formula-light-isotopes.md -->
**Proposition.**
*The strict derived mass formula*

$$
\begin{aligned}
\mathcal{M}(Z, N) &= Z \mathfrak{m}_{\mathfrak{p}} + N \mathfrak{m}_{\mathfrak{n}} + Z m_e \\
                  &\quad + \alpha \bigl(\Phi_1 - 2[3]_q \Phi_2 + H_A^2 \Phi_3\bigr) \\
                  &\quad + \Delta_{W}(Z, N) + \Delta_{T=1}(Z, N)
\end{aligned}
$$

*with each term derived (no fitting):*

- *$\alpha = m_e \cdot 8G$ (Borromean prefactor;
 [binding scale](#prop:binding-scale-catalan));*
- *$\Phi_1, \Phi_2, \Phi_3$ extracted from per-generator transfer-matrix
 chains using only the inter-nucleon generators (positions $3k+2$ for
 $k = 0, \ldots, A{-}2$);*
- *$\Delta_W = -m_e \cdot H_q((2,2)) \cdot \min(Z, N)/A$
 (Wigner $T=0$ pn pairing,
 [Wigner np pairing](#prop:wigner-np-pairing));*
- *$\Delta_{T=1} = -m_e \cdot H_q((2,2)) \cdot (n_{pp} + n_{nn})/A$
 (natural $T=1$ isovector extension using the same self-conjugate
 partition $(2,2) \vdash 4$ and the same $1/A$ normalisation, with
 $n_{pp} = Z(Z{-}1)/2$ and $n_{nn} = N(N{-}1)/2$);*

*reproduces the atomic masses of all isotopes from $\mathfrak{p}$
through $^7$Li to sub-percent accuracy.*

**categorical scorecard at $q_0 = 1.109978595554181\ldots$ (50 dps):**

See [Table 1](#tbl:derived-mass-formula-light-isotopes-table1-data).

**Proton-neutron mass splitting:**
$\Delta\mathfrak{m}_{\mathfrak{n}-\mathfrak{p}} = 1.293332$ MeV
matches CODATA exactly (preserved by inter-gen direct convention,
since free nucleons have $\Phi = 0$).

**Binding under-prediction.**
*The same formula systematically under-predicts nuclear binding
energies by $30\%$ to $76\%$ across light isotopes:*

See [Table 2](#tbl:derived-mass-formula-light-isotopes-table2-data).

*The under-binding pattern is structural: the formula misses an
intra-shell binding mechanism present in nature. Closing the gap
universally requires a new derived term (not phenomenological
patches), which remains an open research direction.*
<!-- FILE_END: derived-mass-formula-light-isotopes.md -->

<!-- FILE_START: hoefsmit-seminormal-form.md -->
**Proposition.**
*For each partition $\lambda \vdash n$ and substrate parameter $q > 1$,
the Hoefsmit seminormal form \cite{hoefsmit1974} gives an explicit
matrix representation $\rho_\lambda\colon H_n(R, q) \to M_{d_\lambda}(\mathbb{C})$
where $d_\lambda = |\mathrm{SYT}(\lambda)|$ is the number of standard
Young tableaux of shape $\lambda$.  The generator $\sigma_i$ acts on the
basis of standard tableaux by:*

$$
  \rho_\lambda(\sigma_i)_{ss'}
  =
  \begin{cases}
    a_\rho & s' = s, \\
    b & s' = s_i, \\
    0 & \text{otherwise},
  \end{cases}
$$

*where $s_i$ is the tableau obtained by swapping entries $i$ and $i+1$
in $s$ (if the result is a valid standard tableau), and the matrix
entries are:*

$$
  a_\rho = \frac{q - q^{-1}}{1 - q^{-2\rho}},
  \qquad
  b = \sqrt{a_\rho \cdot a_{-\rho} + 1},
$$

*with $\rho = c(s, i{+}1) - c(s, i)$ the axial distance (content
difference) between the cells containing $i{+}1$ and $i$ in
tableau $s$.*

*These matrices satisfy the Hecke relation
$\sigma_i^2 = (q - q^{-1})\,\sigma_i + 1$ and the braid relation
$\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$, and are the explicit
$R$-matrix evaluations that dictate topological crossings in braid
and knot diagrams.*
<!-- FILE_END: hoefsmit-seminormal-form.md -->

<!-- FILE_START: figure-eight-branching-rule.md -->
**Proposition.**
*For any partition $\lambda \vdash k$ and substrate parameter $q > 1$,
the Frobenius character of the figure-eight braid
$4_1 = \sigma_0\sigma_1^{-1}\sigma_0^{-1}\sigma_1$ in the irreducible
representation $\rho_\lambda$ of $H_k(R, q)$ is determined by three
branching multiplicities in Young's lattice:*

$$
  \chi(4_1, \lambda)
  = \bigl(f^{\lambda/[3]} + f^{\lambda/[1^3]} - f^{\lambda/[2{,}1]}\bigr)
  \;-\; f^{\lambda/[2{,}1]} \cdot h^2
$$

*where $f^{\lambda/\mu} = |\mathrm{SYT}(\lambda/\mu)|$ is the number of
standard Young tableaux of skew shape $\lambda/\mu$
(equivalently, the number of saturated chains from $\mu$ to $\lambda$
in Young's lattice), and $h = q - q^{-1}$.*

*The two components are:*

- *$a_\lambda = f^{\lambda/[3]} + f^{\lambda/[1^3]} - f^{\lambda/[2{,}1]}$:
  the classical part (the $S_k$ character of the 3-cycle $(123)$
  embedded in $S_k$).*
- *$b_\lambda = -f^{\lambda/[2{,}1]}$:
  the $q$-deformation correction, always $\leq 0$.*

*Verified to machine precision ($< 10^{-12}$) against explicit Hoefsmit
seminormal matrix computation for all 191 partitions at $k = 3$ through
$k = 11$.*

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: figure-eight-branching-rule.md -->

