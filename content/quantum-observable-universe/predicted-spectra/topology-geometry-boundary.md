The categorical action $\mathfrak{S}_q = \mathrm{tr}(\mathcal{L}_q)$
([canonical action](#prop:qou-canonical-action)) evaluated on a nuclear
link $\mathcal{N}(Z, N)$ produces observables at two levels.

**What $q$ alone determines.**

These are computed from the Iwahori--Hecke algebra $H_A(q)$ at the single
parameter the substrate $q$, the Descartes condition $\chi(A) = -6$,
and the categorical definitions:

See [Table](#tbl:topology-geometry-boundary-table-data).

**What is not yet computed from $q$ alone.**

The **$Q$-value** for nuclei beyond the deuteron.  The $Q$-value
is the mass difference $M(\text{parent}) - M(\text{daughter}) - m_e$.
Each nuclear mass requires the terminal resolution of the full
composite link $L_{3A}$ — the pair Skein mass formula applied to
all crossings with Hecke compounding.  This computation is set up
(braid registry, SnapPy, Singular/Hecke engine) but not yet
evaluated for $A > 2$.

The mass formula for individual hadrons:
$\mathfrak{m} = \mathrm{Vol}(K) / \hbar_q^2$ (hyperbolic volume normalised
by $\hbar_q^2 = (1 - q^{-1})^2$) gives sub-keV masses for the
electron, muon, proton, and neutron.  For multi-nucleon links
(satellite links with $\mathrm{Vol} = A \times \mathrm{Vol}(\mathcal{B}_3)$
exactly), the nuclear binding comes from the pair Skein mass
$\mathcal{S}_{ab}(q) = (q\mu_a + q^{-1}\mu_b)/(q^{1/2}+q^{-1/2})$
evaluated at the inter-nucleon crossings.

The $Q$-value is a $\sim 0.001\%$ mass difference ($\sim 0.1$--$1$ MeV
on $\sim 10{,}000$--$200{,}000$ MeV total mass).  Computing it
requires the composite pair Skein weights to high precision — the
terminal resolution applied to the full $3A$-strand link.

The framework gives the correct **structure** of the $Q$-value
(which nuclei decay, in which direction, with which shell
blocking and sensitivity) from $q$ alone.
