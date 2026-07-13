*Proof.*

Each $\{\lambda : \mathrm{depth}(\lambda) = k\}$ is finite, so each
$\Phi_k$ is a finite $R$-valued sum.  By
[curvature-rank stratification](#prop:curvature-rank-gb-stratification),
the central idempotent $e_\lambda$ has GB-filtration depth
$\mathrm{depth}(\lambda)$, so binning
$\sum_\lambda \tilde w_\lambda \cdot
\log|\int_{A_\lambda} \rho(\beta_\mathcal{K}) \cdot \mathcal{T}|$ by
$\mathrm{depth}(\lambda)$ is the canonical curvature-rank
decomposition of the (logarithmic) Frobenius pairing.  The threshold
$k \geq 4$ is determined by which strata of $Z(H_n(R, q))$ still carry
a distinguished knot ideal — empirically $k_* = 4$.

The total sum is bounded: $\sum_{\lambda \vdash n} \tilde w_\lambda$
is finite for every $n$ and equals $1$ exactly at $q = 1$; at
$q_0 = 1.109978595554181\ldots$ (50 dps) it deviates from $1$ — categorically
$\sum \tilde w_\lambda \approx 1.51$ at $n = 12$
([prop:plancherel-weight-boundedness](#prop:plancherel-weight-boundedness)
remark on q-deformed alternative). Boundedness of $\Phi_k$ follows
from finiteness of the $\tilde w_\lambda$ together with finiteness
of the per-block log-Frobenius pairings; the absolute-convergence
constant is $\sup_\lambda \tilde w_\lambda \cdot \#\Lambda_k \cdot
\sup_\lambda |\log|\!\int||$, not $1$ as for the classical
Plancherel measure. $\square$

**Logarithmic control of scale.** *The bare Wedderburn-weighted
character sum $\sum_\lambda \tilde w_\lambda \cdot
\chi_\lambda(\beta) / \dim_q V_\lambda$ is bounded by a finite
constant (canonical $\lesssim 2$ at $q_0$ for $n \leq 12$), giving
a similarly small MeV-scale ceiling — too small for MeV-scale
binding gaps. Replacing $\chi_\lambda$ with
$\log|\!\int_{A_\lambda}\!\cdot|$ keeps the Wedderburn weighting
bounded but lets each block contribute $O(\log|\chi|)$, which can
be large.  This is how the formula reaches $\sim 30$ MeV
${}^4\mathrm{He}$ binding from a bounded measure: logarithmic
unbounding of bounded characters.*

**Comparison with the deprecated bare hook product.**
*An older form of "Term 7" used the Hopf hook polynomial
$H_q(\lambda) = \prod_{x \in \lambda}[h_x]_q$ summed naively across
deep partitions; that form diverges as $q^{n^2/2}$.  The Wedderburn-
weighted log functional above is the categorically correct
replacement — it descends from the Hochschild-cohomology spectral
sequence's collapse at $E_1$
([spectral sequence collapse](#prop:spectral-sequence-collapse)),
with $\mathrm{HH}^0 = Z(H_n(R, q))$ paired against the logarithmic
Frobenius integral.*

**Naming note.** *Earlier drafts (and the legacy formalism
the formal derivation) referred to $\tilde w_\lambda =
\dim_q^2/[n]_q!$ as the "q-Plancherel weight" and claimed
$\sum_\lambda \tilde w_\lambda = 1$ via a "q-Plancherel identity"
$\sum_\lambda \dim_q^2 V_\lambda = [n]_q!$. That identity does not
hold in $H_n(R, q)$ at generic $q$ — the Hecke algebra is a flat
deformation with $\dim_{\mathbb{Q}(q)} H_n = n!$ and Wedderburn–Artin
gives the classical Plancherel identity
$\sum_\lambda (\dim V_\lambda)^2 = n!$, whose Plancherel weight is
$w_\lambda := (\dim V_\lambda)^2/n!$
([prop:plancherel-weight-boundedness](#prop:plancherel-weight-boundedness)).
The current proposition uses $\tilde w_\lambda$ as the
q-deformed Wedderburn-block weight, not the Plancherel measure;
they coincide at $q = 1$.*

**canonical witness.**
the formal derivation computes
$\Phi_k$ for D, T, ${}^3\mathrm{He}$, ${}^4\mathrm{He}$, evaluating
$\chi_\lambda(\beta_\mathrm{atom})$ via Hoefsmit seminormal form
characters at $q_0$ and summing with the q-deformed Wedderburn weights
$\tilde w_\lambda$.  Compares $\alpha \cdot
\mathfrak{m}^{\geq 4}_{q,\mathcal{K}}$ to the Coulomb-corrected
nuclear binding $B_\mathrm{nucl}$ from
`coulomb-subtracted-binding.witness.json`.
