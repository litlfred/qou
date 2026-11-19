**Proposition (negative).**
*Let $Z$ protons and $N$ neutrons ($A = Z + N$) be arranged along the
transfer-matrix chain, and let*

$$
  \Phi_q = \sum_i \log|\hat{V}_i|
$$

*be the quantum dilogarithm volume of that chain.  Consider the
interleaved, tail-packed arrangement*

$$
  \mathrm{ordering}[k]
  =
  \begin{cases}
    1 \text{ (proton)} & k \text{ odd}, \; k < 2Z \\
    0 \text{ (neutron)} & \text{otherwise.}
  \end{cases}
$$

*This arrangement does **not** minimise $\Phi_q$.  Explicitly, at
$A = 5$, $Z = 1$, $N = 4$ it is the strict maximiser: the sorted
arrangement $p\,n\,n\,n\,n$ satisfies*

$$
  \Phi_q(p\,n\,n\,n\,n) < \Phi_q(n\,p\,n\,n\,n)
$$

*for every $q$ in an interval containing the aether anchor
$q_0 \approx 1.10998$ and for every Markov parameter lying strictly
between the two transfer-matrix eigenvalues, with equality only in the
undeformed limit $q \to 1$.*

The eigenvalue relation $\lambda_+\lambda_- = -1$ for the transfer
matrix survives; the ordering claim does not.

## Status of the three rules

The proposition previously asserted three rules.  An exhaustive sweep of
$\Phi_q$ over every $\binom{A}{Z}$ arrangement for $A \leq 16$, at the
experimental (proton) anchor, settles each of them.

**(i) Interleaving** — *refuted for $A \geq 4$.*  The interleaved
arrangement is the $\Phi_q$ minimiser in $17$ of $62$ swept cases on the
bare-nucleon readout ($10$ of $62$ with the electron tail), and is the
strict maximiser in $12$ (respectively $8$).  It is not the ground state.

**(ii) Tail packing** — *refuted.*  The minimising arrangement
head-packs rather than tail-packs.  At $Z = 1$ the minimising proton position is
$A - 5$ for every $6 \leq N \leq 15$, leaving exactly four neutrons after
it and all remaining neutrons before it.  For $Z \geq 2$ the minimiser is
an interleaved block at an interior offset with neutron runs on both
sides.

**(iii) Boundary correction ($A \leq 3$)** — *holds at $A = 3$, fails as
stated at $A = 2$.*  At $A = 3$ the sorted arrangement is the exhaustive
minimiser, on both readouts and on both sides of $Z \leq N$.  At $A = 2$
the two arrangements are *exactly degenerate* on the bare chain — a
consequence of the transfer factors commuting, so that the readout sees
the crossing coefficients only as a multiset — so sorted does not
*beat* interleaving; and with the electron tail appended, sorted is
strictly the worse of the two.

## Two readouts, not one

$\Phi_q$ is computed in two inequivalent ways in the corpus: over the
bare nucleon chain, and over the nucleon chain with an electron tail
appended.  The verdicts above are stated for both.  They differ only for
rule (iii) at $A = 2$, a case that the production path special-cases and
never routes through the ordering at all.

## The readout as a two-parameter object

Each transfer factor is $T(d) = S + d\,\mathbf{1}$ for a single fixed
matrix $S$ with $\mathrm{tr}\, S = q - q^{-1}$ and $\det S = -1$.
All such factors commute, so the chain product depends on the crossing
coefficients only as a multiset, and $S^2 = (q-q^{-1})S + \mathbf{1}$
collapses the product to $\alpha\mathbf{1} + \beta S$.  The vertex volume
is therefore

$$
  \hat{V}_i = c_+\mu_+ + c_-\mu_-,
  \qquad
  \mu_\pm = \prod_{j > i}(\lambda_\pm + d_{ij}),
$$

with $\lambda_+ = q$, $\lambda_- = -q^{-1}$ the roots of the
characteristic polynomial and, writing $z$ for the Markov parameter,

$$
  c_+ = \frac{z + q^{-1}}{q + q^{-1}},
  \qquad
  c_- = \frac{q - z}{q + q^{-1}},
  \qquad
  c_+ + c_- = 1 .
$$

The sum is $1$ identically in $z$, and $z$ enters the readout nowhere
else.

## Independence of the Markov-parameter convention

The two arrangements differ at positions $0$ and $1$ only, and that
comparison collapses to a single identity in which $z$ survives only
inside the product $c_+c_-$:

$$
  \hat{V}_0\hat{V}_1(n\,p\,n\,n\,n) - \hat{V}_0\hat{V}_1(p\,n\,n\,n\,n)
  = 2\,c_+c_-\left(\frac{q + q^{-1}}{2}\right)^{4}\frac{q^6 - 1}{q^3},
  \qquad
  4\,c_+c_- = \frac{4q\,(q - z)(qz + 1)}{(q^2 + 1)^2},
$$

the fourth power being the mixed proton–neutron eigenfactor, which carries
no $z$.  For $q > 1$ every other factor is positive, so the counterexample
holds exactly when $-q^{-1} < z < q$ — the Markov parameter strictly
between the two eigenvalues.  Both the canonical convention D,
$z = q^3/(q^2+1)$, and the excised convention C, $z = \sqrt{q}/(q+1)$,
lie in that window for every $q > 1$, so the refutation is a fact about the
readout rather than about a choice of $z$; it degenerates to equality only
at $q = 1$, where the deformation switches off, which is why it holds on a
whole interval rather than at a single anchor.

## Scope

The $A \geq 4$ refutation is a structural exclusion: an explicit
arrangement with strictly smaller $\Phi_q$, proved for an interval of $q$
containing the anchor and for every Markov parameter in the window above.
The description of the actual minimising family
is empirical, covering $A \leq 16$ only, and no claim is made beyond that
range.  Which ordering the mass and binding computations should use is a
separate question and is not settled here.
