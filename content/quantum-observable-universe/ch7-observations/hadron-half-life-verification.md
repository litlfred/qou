We verify the half-life framework
([hadron half-life](#prop:hadron-half-life)) against measured
beta-decay lifetimes for representative nuclei spanning the periodic
table.

The $Q$-value for each transition is determined by the terminal
resolution of the parent and daughter composite links at $q = 1.110$,
using the pair Skein mass formula
$\mathcal{S}_{ab}(q) = (q\,\mu_a + q^{-1}\mu_b)/(q^{1/2}+q^{-1/2})$
with dressed quark masses $\mu_u = 311.10$ MeV, $\mu_d = 312.39$ MeV
([terminal resolution](#prop:terminal-resolution)).

**What is computed from $q$ alone (no free parameters):**

1. The sensitivity $\partial \ln \Gamma / \partial \ln q \approx 48$
   — exact from $q$.
2. The ${}^3\mathrm{H}$ half-life to 1% via the self-deformation
   $\Delta q_{\mathrm{eff}}$
   ([self-correction](#prop:hadron-q-self-correction)).
3. The Markov trace factorization
   $\text{tr}(\overline{\mathcal{N}}) = \prod_i \hat{V}_i$
   — exact, verified to ratio $= 1.000000$
   ([factorization theorem](#thm:markov-trace-factorization)).
4. The Gröbner-reduced normal form $\overline{\mathcal{N}(p,n)}$
   — unique by the diamond lemma
   ([nuclear Gröbner reduction](#prop:nuclear-groebner-reduction)).
5. The deuteron binding $B_d = 1.29$ MeV from
   $\text{Vol}(\mathcal{B}_3 \bowtie_\text{Hopf} \mathcal{B}_3) / \hbar_q^2$.

**What is NOT yet computed from $q$ alone:**

The $Q$-value for nuclei beyond the deuteron.  The $Q$-value is
the mass difference between parent and daughter, which requires
the terminal resolution of the full composite link $L_{3A}$ — the
pair Skein mass formula applied to all crossings in the $3A$-strand
braid, with Hecke compounding at each generator.  This computation
has been set up (braid registry, SnapPy volumes, Singular/Hecke
engine) but not yet evaluated for $A > 2$.

**Observed half-lives (NNDC/ENSDF):**

| Nucleus | $A$ | $Q_\beta^{\mathrm{exp}}$ (MeV) | $t_{1/2}^{\mathrm{obs}}$ |
|---------|-----|------|------|
| ${}^{3}\mathrm{H}$ | 3 | 0.0186 | 12.3 yr |
| ${}^{14}\mathrm{C}$ | 14 | 0.156 | 5730 yr |
| ${}^{60}\mathrm{Co}$ | 60 | 0.318 | 5.27 yr |
| ${}^{90}\mathrm{Sr}$ | 90 | 0.546 | 28.8 yr |
| ${}^{137}\mathrm{Cs}$ | 137 | 0.514 | 30.2 yr |
| ${}^{210}\mathrm{Bi}$ | 210 | 1.163 | 5.01 d |

**Forbidden transitions.**
The table covers allowed Gamow--Teller and Fermi transitions.
For first-forbidden transitions (spin change $\Delta J = 0, 1, 2$
with parity flip), the matrix element acquires an additional
suppression factor $\sim (R/\lambdabar_C)^2$, where $R$ is the
nuclear radius, lengthening half-lives by $10^2$--$10^4$.  The
$q$-dependence of forbidden transitions is identical to the allowed
case — the suppression is purely geometric (nuclear radius vs
Compton wavelength) and does not involve the substrate parameter.
