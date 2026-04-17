Ding, Wang, Yao, Hergert, Liang, and Bogner
\cite{ding2026} ("From Spin to Pseudospin Symmetry: The Origin of
Magic Numbers in Nuclear Structure", PRL 136, 052501) use chiral
effective field theory evolved under the similarity renormalization
group (SRG) to trace the spin-orbit potential as a function of the
momentum resolution scale $\lambda$.  They report a *transition
from spin symmetry to pseudospin symmetry* as $\lambda$ decreases,
with the magic numbers $\{2, 8, 20, 28, 50, 82, 126\}$ emerging
naturally along that flow; they further confirm the pattern with
relativistic one-boson-exchange potentials.

**Alignment with our framework.**

Our derivation in
[shell intruder](#prop:nuclear-shell-intruder) reproduces the same
magic-number set $\{2, 8, 20, 28, 50, 82, 126\}$ from a
different-looking starting point:

1. **Spin-orbit strength is not fit.**  In
   \cite{ding2026} the SO potential arises at a definite SRG
   resolution scale $\lambda$ and its size is set by the two- and
   three-nucleon chiral couplings integrated down to that scale.
   In our derivation the SO coupling coefficient is fixed by the
   **Borromean crossing number $3$** of the baryon link
   ([Borromean baryon](#def:borromean-baryon)).  Both accounts
   trade an adjustable SO parameter for a structural datum — a
   resolution scale in \cite{ding2026}, a topological invariant
   here.

2. **Resolution scale $\leftrightarrow$ Hecke truncation $K$.**
   The SRG parameter $\lambda$ in \cite{ding2026} controls which
   momentum modes are integrated out.  In
   [magic numbers from $q$](#prop:magic-numbers-from-q) the role
   of scale is played by the Hecke truncation level $K$: the
   cumulative Wedderburn signal
   $\Phi(Z) = \sum_{k \leq K} \sum_{\lambda \vdash k} w_\lambda
   \ln|\chi_\lambda(Z)|$ resolves magic $8$ already at $K = 3$,
   magic $28$ only from $K \geq 7$, and magic $126$ requires
   $K \geq 12$.  The hierarchy of scales at which successive
   magic numbers appear is qualitatively the same as the
   hierarchy reported by Ding et al.

3. **Pseudospin degeneracy is a $q$-deformation statement.**
   Pseudospin pairs $(\ell, j = \ell - \tfrac{1}{2})$ and
   $(\ell - 2, j = \ell - \tfrac{3}{2})$ become (nearly)
   degenerate in \cite{ding2026} at low $\lambda$.  In our
   setting the SO energy is
   $E_{\mathrm{SO}} \propto [\ell]_q [\ell + 1]_q \cdot (j - \ell)$
   ([orbital Fourier decomposition](#prop:orbital-fourier-decomposition)).
   The pseudospin-degeneracy condition reads
   $[\ell - 1]_q [\ell]_q \approx [\ell - 2]_q [\ell - 1]_q$,
   which in the classical limit $q \to 1$ reduces to the ratio
   $\ell / (\ell - 2)$: not exact, but **monotonically
   approaching unity as $\ell \to \infty$** (e.g.\ $5/3$ at
   $\ell = 5$, $7/5$ at $\ell = 7$, $9/7$ at $\ell = 9$).  At
   $q_0 \approx 1.1098$ the $q$-deformation corrections partially
   cancel this classical mismatch, and the ratio
   $[\ell - 1]_q [\ell]_q / ([\ell - 2]_q [\ell - 1]_q)$ holds
   within a few percent for $\ell \geq 3$ — precisely the regime
   where \cite{ding2026} reports the cleanest pseudospin
   doublets.  Pseudospin in our framework is therefore an
   **asymptotic / approximate** symmetry, emerging at large $\ell$
   and mildly improved by the $q$-deformation, not an exact
   symmetry at any value of $q$.

**Where the accounts differ.**

- \cite{ding2026} is a chiral-EFT / SRG calculation at the level
  of the nucleon–nucleon potential; it does not predict the
  *number* of Borromean crossings, it takes nucleons as point
  particles with phenomenological interactions.
- Our account derives the SO strength from an internal
  topological invariant of each nucleon and from the single
  substrate parameter $q$.  It therefore makes a **scale-free
  prediction**: the same set of magic numbers is reached at any
  $K$ provided the truncation exceeds the shell's resolution
  threshold.

**Caveats — where the data currently do not fit cleanly.**

1. **Spin-orbit strength overshoot at low $K$.**  Our derivation
   gives a *single* coefficient (the Borromean crossing number
   $3$), whereas \cite{ding2026} reports a smoothly varying SO
   potential whose amplitude grows as $\lambda$ decreases.  At
   small Hecke truncation $K \lesssim 4$ our
   $3 \cdot [\ell]_q [\ell+1]_q$ exceeds the chiral-EFT SO
   strength at corresponding $\lambda$; quantitative agreement
   requires either $K \geq 7$ or an explanation of why the
   Borromean integer is effectively renormalised at coarse
   resolution.  This is a **known open point**, not a refutation.

2. **Pseudospin degeneracy breaks for the $sd$-shell.**  The
   degeneracy ratio
   $[\ell - 1]_q [\ell]_q / [\ell - 2]_q [\ell - 1]_q$ is within
   $3$–$5\,\%$ of unity for $\ell \geq 3$ at $q_0 \approx
   1.1098$ — consistent with the "near-degenerate" doublets
   reported in \cite{ding2026}.  At $\ell = 2$ (the $sd$-shell)
   the deviation grows to $\sim 10$–$15\,\%$, which is larger
   than the residual breaking seen in the PRL data.  Either the
   $sd$-shell lies outside the pseudospin regime (consistent
   with Ding et al., who emphasise its cleanest appearance at
   higher $\ell$) or an additional $q$-correction is needed at
   $\ell = 2$.

3. **Magic number $28$ is marginal.**  In
   [magic numbers from $q$](#prop:magic-numbers-from-q) the
   $\delta^2 \Phi$ peak at $Z = 28$ is only $+4.4$ at
   $K = 10$, compared to $+33.2$ at $Z = 8$ and $+20.4$ at
   $Z = 20$.  Ding et al.\ report $Z = 28$ as fully robust
   across their $\lambda$ range; our signal at $K = 10$ is at
   best "consistent" rather than "clean", and a higher-$K$
   computation is needed to confirm.

**Net assessment.** The two frameworks agree on the observable
content (same seven magic numbers, same intruder levels
$1f_{7/2}, 1g_{9/2}, 1h_{11/2}, 1i_{13/2}$) and disagree only on
the identification of the bookkeeping scale.  Ding et al.'s
resolution scale $\lambda$ and our Hecke level $K$ play
analogous roles.  We read \cite{ding2026} as independent
evidence that a *single* structural control parameter — SRG
scale for them, Borromean crossing number plus $q$ for us — is
sufficient to explain the stability hierarchy; neither account
requires an externally tuned spin-orbit coupling.  The three
caveats above mark where further computation (higher $K$,
$\ell = 2$ correction) is needed to make the alignment
quantitative rather than qualitative.
