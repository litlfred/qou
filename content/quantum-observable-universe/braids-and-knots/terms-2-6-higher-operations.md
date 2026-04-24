Terms 2 (single-generator brane tower $\sum \Phi_q(|\hat V_i|)$) and
6 (jet-level prefix corrections) of the unified knot mass formula
([unified knot mass](#thm:knot-mass-formula-unified)) are the two
remaining open identifications in the spectral-sequence framework
([$E_\infty$ page identifications](#prop:e-infinity-page-identifications)).
This proposition sketches concrete avenues to close both via
**higher operations** on the Hochschild cohomology of $H_n(q)$.

**Setup: Gerstenhaber structure on $HH^*(H_n(q))$.**

*The Hochschild cohomology $HH^*(A, A)$ of any associative algebra
$A$ carries a canonical **Gerstenhaber algebra** structure:*

- *Cup product $\cup \colon HH^p \otimes HH^q \to HH^{p+q}$
  (graded-commutative, associative).*
- *Gerstenhaber bracket $[-, -] \colon HH^p \otimes HH^q \to HH^{p+q-1}$
  (graded Lie bracket of degree $-1$).*

*For $A = H_n(q)$, the cup product gives a ring structure on
$\bigoplus_p HH^p$, and the Gerstenhaber bracket measures the
non-commutativity of the deformation.*

**Term 2 = Cauchy $\Phi_q$ kernel = cup-product tower.**

**Claim.**
*The single-generator brane tower
$\sum_i \Phi_q(|\hat V_i|)$ arises from the **cup-product tower**
of the class $[\sigma_i] \in HH^1(H_n(q))$ with itself:*

$$
  \sum_{k = 1}^{\infty} \frac{q^{-k}}{(q; q)_k}\bigl([\sigma_i]\bigr)^{\cup k}
  \;=\;
  \bigl\langle \Phi_q(|\hat V_i|) - 1\bigr\rangle
  \quad \text{in } HH^* \text{ pairing with } \mathrm{tr}_M.
$$

*Expansion: $\Phi_q(z) = \sum_k z^k / (q;q)_k$ (Cauchy's $q$-exponential),
with $(q;q)_k = \prod_{j=1}^k(1 - q^j)$.  The $z^k$ coefficient
$1/(q;q)_k$ is the $q$-binomial coefficient tracking partition
counts at the $k$-th level of the flag.*

**Derivation sketch.**
*Each generator $[\sigma_i] \in HH^1$ pairs with
$\mathrm{tr}_M$ via the Markov trace at degree $1$:
$\langle \mathrm{tr}_M, [\sigma_i]\rangle = z$.  The $k$-fold
cup product $[\sigma_i]^{\cup k}$ lives in $HH^k$ (higher
filtration stratum) and its Markov-trace pairing is
$z \cdot q^{-(k-1)} \cdot (\text{weight})$ by the recursive
Hecke relation.  Summing over $k$ with the $(q;q)_k$ normalisation
gives the full $\Phi_q$ kernel.*

**Status.**
*The **structure** (cup-product tower matches $\Phi_q$'s Cauchy
kernel) is rigorous in principle: both are generating functions
of the same partition-counting sequence.  The **explicit match**
of coefficients requires computing $[\sigma_i]^{\cup k}$ for each
$k$ and verifying the Markov-trace weights match the
$(q;q)_k$-normalised $\Phi_q$ series.  This is a finite-dimensional
computation in $HH^*(H_3(q))$ for $n = 3$ — **tractable but not
done**.*

---

**Term 6 = jet prefix = NOT a prefix-product formula.**

*Four candidate prefix conventions have been tested (three upstream
+ one GB-filtration in
[jet-prefix GB filtration](#prop:jet-prefix-gb-filtration));
**all fail**.  We propose that Term 6 is structurally **not** a
prefix-word product but is instead the **root-of-unity residue
contribution** already captured by
[GB residue spectral sum](#prop:gb-residue-spectral-sum).*

**Proposed identification.**

$$
  \text{Term 6}(K)
  \;=\;
  \sum_{\ell \geq 2}
    \frac{\mathrm{Res}_{q = \zeta_\ell}\bigl[\Phi_q \cdot \mathrm{tr}_{M, \ell}(T_w)\bigr]}
         {q_0 - \zeta_\ell},
$$

*i.e., the Mittag-Leffler residue sum at roots of unity $\zeta_\ell$
for $\ell \geq 2$ (the level-$\ell = 1$ residue is absorbed into
Terms 2, 3 as the dominant $\zeta_1 = 1$ pole).*

**Why this replaces the prefix formula.**

*The paper's prefix formula
$a_k(\beta) = \sum_\lambda w_\lambda \chi^\lambda(\beta_k) / \sum_\lambda w_\lambda \dim \mathrm{Res}^{H_k}_{H_3} V_\lambda$
has no algebraic match against the higher-strata $E_\infty^{\ell \geq 3}$
pages of the spectral sequence — consistent with the four failed
tests.  Meanwhile, the **Mittag-Leffler** formula DOES correspond
to higher $E_\infty$ strata (via the residue-spectral-sum
derivation in
[GB residue spectral sum](#prop:gb-residue-spectral-sum)).*

*So Term 6 may have been **mis-stated** in earlier blocks as a
prefix product; the correct identification is with root-of-unity
residues summed over all $\ell \geq 2$.*

**Status.**
*This is a **structural proposal**, not a proof.  It requires:*

1. *Confirming that the Mittag-Leffler sum for $\ell \geq 2$ reproduces
   the empirical Term 6 corrections needed to close the $A \geq 3$
   binding errors (currently $5\%$-$20\%$ from paper's BW+$\chi$
   + shell).*
2. *Rigorously identifying $E_\infty^{\ell, *}$ for $\ell \geq 3$
   with specific ribbon-residue combinations via the Cauchy
   kernel of Term 2.*

*If confirmed, the unified mass formula collapses from 6 terms to
**5 independent structural pieces**:*

1. *Descended $|\mathrm{tr}_M|$ (Term 1)*
2. *Brane tower $\sum \Phi_q(|\hat V_i|) + z^2 \sum \Phi_q(|\hat V_i \hat V_j|)$
   (Terms 2 + 3, combined as Cauchy kernel tower on $HH^{\geq 1}$)*
3. *Frobenius co-Casimir $m_e \cdot \tau(C_{\dim_q})$ (Term 4)*
4. *Chirality / ribbon twist $a_K$ (Term 5)*
5. *Higher-stratum residues (what was Term 6, now = ML sum at
   $\zeta_\ell$ for $\ell \geq 2$)*

*A much cleaner structural story.*

---

**Implications for the unified formula.**

*If the above identifications hold:*

$$
  \boxed{\;
  \mathfrak{m}(\varrho)
  \;=\;
  \underbrace{|\mathrm{tr}_M(T_w)|}_{E_\infty^{0, *}}
  \;+\;
  \underbrace{\bigl\langle \mathrm{tr}_M,\ \Phi_q \text{-tower} \bigr\rangle_{HH^{\geq 1}}}_{\text{Cauchy kernel (Terms 2, 3, 6)}}
  \;+\;
  \underbrace{m_e \cdot \tau(C_{\dim_q})}_{\text{Term 4}}
  \;+\;
  \underbrace{a_K(\varrho) \cdot \mathcal{C}}_{\text{Term 5 (ribbon)}}
  \;}
$$

*where $\mathcal{C}$ denotes the chirality-couplable piece (e.g.,
$B_{\mathrm{bulk}}$ in the BW+$\chi$ form).  Four structurally
distinct pieces, not six.*

**Caveat.**
*All of this is proposed, not proven.  The cup-product tower
derivation for Term 2 and the root-of-unity residue
identification for Term 6 are **concrete computational
targets** but have not been verified for any nontrivial case.
They are the natural next steps.*

**Computational tasks, prioritized.**

1. *Compute $[\sigma_0]^{\cup k}$ for $k = 1, 2, 3$ in $HH^*(H_3(q))$
   over $\mathbb{R}[q, q^{-1}]$; verify Markov-trace pairings
   match $\Phi_q$ Taylor coefficients.*
2. *Compute Mittag-Leffler residue at $\zeta_2 = -1$ for D's
   atomic braid; compare to residual $5$–$20\%$ binding errors
   at $A \geq 3$.*
3. *If Term 2 + Term 6 unification holds, the 6-term formula
   reduces to the 4-term boxed form above.*
