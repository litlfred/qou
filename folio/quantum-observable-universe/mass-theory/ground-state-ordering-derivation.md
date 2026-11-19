# Ground-state ordering: the eigenvalue heuristic and what the sweep found

This remark records the eigenvalue argument that originally motivated
the interleaving rule, and the exhaustive search that refuted it.

## Transfer matrix eigenvalues

The three transfer matrices
([transfer matrix](#prop:beta-decay-transfer-matrix)) have
eigenvalues determined by the typed crossing operators
([typed crossings](#def:typed-crossing-operator)):

See [Table 1](#tbl:ground-state-ordering-table1-data).

where $h = q - q^{-1}$.

**Key symmetry**: $T_{nn}$ is the $q \leftrightarrow q^{-1}$
mirror of $T_{pp}$.  Their eigenvalues are swapped:
$\lambda_\pm(T_{nn}) = \lambda_\mp(T_{pp})$.  The mixed matrix
$T_{pn}$ has **zero trace** and equal-magnitude eigenvalues
$\pm\sqrt{1 + h^2/4} \approx \pm 1.005$.

## The heuristic

Each $T_{pp}$ contributes dominant eigenvalue $+q \approx 1.110$
(growth).  Each $T_{nn}$ contributes $+q^{-1} \approx 0.901$
(decay).  The interleaved arrangement alternates growth and
decay factors, which suggests destructive interference driving
$|\hat{V}_i|$ below $1$ at most generators, whereas a sorted chain
front-loads pure growth.  Since $T_{pn}$ has zero trace, its
contributions were expected to average to zero over many chain
steps, making the mixed crossings neutral spacers between the
binding $T_{nn}$ and anti-binding $T_{pp}$ contributions.

**The exhaustive sweep below refutes this heuristic.**

## What the exhaustive sweep found

$\Phi_q$ was evaluated over **every** $\binom{A}{Z}$ arrangement for
each $(Z, N)$ with $Z \leq N$ and $A \leq 16$, at the experimental
substrate anchor, on both the bare-nucleon chain and the chain with the
electron tail appended.

The interleaved, tail-packed arrangement is the minimiser in a minority
of cases and the strict maximiser in a comparable number.  At $A = 5$,
$Z = 1$ it is the strict worst of all five arrangements on both
readouts, while the sorted arrangement — which the rule reserves for
$A \leq 3$ — is the minimiser.  The excess neutrons of the minimising
arrangement head-pack rather than tail-pack.  Full tallies and the
explicit counterexample are in
[the proposition](#prop:ground-state-ordering).

## Why the heuristic failed

The transfer factors are $T(d) = S + d\,\mathbf{1}$ for a single fixed
matrix $S$, so they all **commute**: the chain product at a position
depends on the crossing coefficients only as a multiset, and there is no
"alternation" for the readout to see.  What looks like a growth/decay
interference pattern at the level of individual matrices is, at the level
of the readout, a product of eigenfactors whose ordering is immaterial.
The only thing that varies between arrangements is *which multiset* sits
at *which position* — and the resulting $\Phi_q$ is not extremised by
alternation.

This also explains an exact degeneracy the heuristic cannot account for:
at $A = 3$, $Z = 2$ the arrangements $ppn$ and $pnp$ have *identical*
$\Phi_q$ on the bare chain.

## Connection to the Gram matrix

The transfer matrix eigenvalues are the Gram matrix entries
in disguise: $\lambda_+(T_{pp}) = q$ and $\lambda_+(T_{nn}) = q^{-1}$
are the braiding eigenvalues from the Hecke relation
$(T - q)(T + q^{-1}) = 0$.  That identification is unaffected by the
refutation; only the claim that a particular arrangement extremises
$\Phi_q$ does not apply.

## Scalability

For $A > 16$ exhaustive search over $\binom{A}{Z}$ arrangements was not
attempted, and no closed-form rule for the minimiser is available.  The
sweep's minimising family — an interleaved block at an interior offset,
with the excess neutrons split between a head run and a four-neutron
tail — is an empirical description over $A \leq 16$, not a derived
construction.
