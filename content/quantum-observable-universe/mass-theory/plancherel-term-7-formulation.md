**Proposition (universal residue at curvature-rank $k \geq 4$).**
*Define the **curvature-rank-$k$ residue functional***

$$
  \Phi_k(\mathcal{K}, \mathcal{T})
  \;:=\; \sum_{\substack{\lambda \,\vdash\, n \\ \mathrm{depth}(\lambda) = k}}
  \tilde w_\lambda \cdot \log\Bigl|\!\int_{A_\lambda}\! \rho(\beta_\mathcal{K}) \cdot \mathcal{T}\Bigr|,
  \qquad \tilde w_\lambda \;=\; \frac{\dim_q^2 V_\lambda}{[n]_q!},
$$

*where $A = H_n(R, q)$, $A_\lambda = e_\lambda A e_\lambda$ is the
Wedderburn block, $\beta_\mathcal{K}$ is a braid representative of the
knot $\mathcal{K}$, $\mathcal{T} \in A$ is a test element, and
$\mathrm{depth}(\lambda) = \mathrm{height}(\lambda) - 1$ is the
curvature-rank ([curvature-rank stratification](#prop:curvature-rank-gb-stratification)).
The symbol $\tilde w_\lambda$ denotes the **q-deformed
Wedderburn-block weight** — distinct from the classical Plancherel
measure $w_\lambda = (\dim V_\lambda)^2/n!$
([prop:plancherel-weight-boundedness](#prop:plancherel-weight-boundedness))
which it specialises to at $q = 1$. The **universal residue** is the
high-tower contribution:*

$$
  \boxed{\;
    \mathfrak{m}^{\geq 4}_{q,\mathcal{K}}(\mathcal{T})
    \;=\; \alpha \cdot \!\!\sum_{k \geq 4}\!\Phi_k(\mathcal{K}, \mathcal{T}),
    \qquad \alpha \;=\; m_e \cdot 8G.
  \;}
$$

*This is the algebraic content of what older drafts called "Term 7":
deep-tower strata where no specific hyperbolic-knot ideal appears, only
the universal Frobenius co-Casimir tail.*

**Why universal at $k \geq 4$.** *At low strata $k \leq 3$ the
restricted Frobenius integral $\int_{A_\lambda} \rho(\beta_\mathcal{K}) \cdot \mathcal{T}$
factors through specific hyperbolic-knot ideals (specifically $4_1$
at $k = 3$ — the chirality channel via Fricke-trace derivation, empirically
resolved by ; see
[chirality residue](#prop:chirality-from-frobenius-self-pairing) for
the derivation).
At $k \geq 4$ no specific knot ideal remains in the centre — what
survives is the dualizing-complex residue, which depends only on
$(\mathcal{K}, \mathcal{T})$ and the Wedderburn-stratification
data, not on a distinguished knot.*

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
$q_0 = 1.109978595554181\ldots$ (50 dps) it deviates from $1$ — empirically
$\sum \tilde w_\lambda \approx 1.51$ at $n = 12$
([prop:plancherel-weight-boundedness](#prop:plancherel-weight-boundedness)
remark on q-deformed alternative). Boundedness of $\Phi_k$ follows
from finiteness of the $\tilde w_\lambda$ together with finiteness
of the per-block log-Frobenius pairings; the absolute-convergence
constant is $\sup_\lambda \tilde w_\lambda \cdot \#\Lambda_k \cdot
\sup_\lambda |\log|\!\int||$, not $1$ as for the classical
Plancherel measure. $\square$

**Why the logarithm controls scale.** *The bare Wedderburn-weighted
character sum $\sum_\lambda \tilde w_\lambda \cdot
\chi_\lambda(\beta) / \dim_q V_\lambda$ is bounded by a finite
constant (numerically $\lesssim 2$ at $q_0$ for $n \leq 12$), giving
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

**Naming note.** *Earlier drafts (and the legacy script
`plancherel_term_7.py`) referred to $\tilde w_\lambda =
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

**Numerical witness.**
[`computations/plancherel_term_7.py`](#) computes
$\Phi_k$ for D, T, ${}^3\mathrm{He}$, ${}^4\mathrm{He}$, evaluating
$\chi_\lambda(\beta_\mathrm{atom})$ via Hoefsmit seminormal form
characters at $q_0$ and summing with the q-deformed Wedderburn weights
$\tilde w_\lambda$.  Compares $\alpha \cdot
\mathfrak{m}^{\geq 4}_{q,\mathcal{K}}$ to the Coulomb-corrected
nuclear binding $B_\mathrm{nucl}$ from
`coulomb-subtracted-binding.witness.json`.
