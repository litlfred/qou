## Proof

By [Wenzl 1988] (cited in [Orellana, math/9806163, Theorem on
p.17]), the unique Markov trace on the type-A Iwahori-Hecke
algebra in $g$-convention with parameter $z_{\mathrm{GL}} = Q^r
(1 - Q)/(1 - Q^r)$ has weights $\omega_\lambda(Q) =
s_{\lambda, r}(Q)$ given by the principal-specialization Schur
function.  By [Chlouveraki HDR Theorem 6.20 (=Juyumaya Theorem 12,
$d=1$ case)], the type-A Markov-trace family is 1-dimensional,
parameterised by $z$.

The convention isomorphism $g = q\sigma$ transports $\mathrm{tr}_M$
on $\sigma$-Hecke (with the $\sigma$-convention $z$) to
$\mathrm{tr}_{\mathrm{GL}}$ on $g$-Hecke (with $z_{\mathrm{GL}} = q z$).  Both traces have the
same expansion $\mathrm{tr} = \sum_\lambda y_\lambda \chi_\lambda$
for any choice of irreducible character basis (which is intrinsic
to the algebra, hence convention-independent).  By uniqueness, the
weights agree:

$$
  y_\lambda^{(\sigma)} \;=\; y_\lambda^{(g)} \;=\;
  \omega_\lambda(Q) / Z, \qquad Z := \sum_\mu d_\mu \omega_\mu(Q),
$$

normalised so $\mathrm{tr}_M(1) = \sum_\lambda y_\lambda d_\lambda = 1$.
$\square$

## Specialisation at the production convention

Under convention D, $z = q^3/(q^2+1)$, so $z_{\mathrm{GL}} = qz = Q^2/(1+Q)$
with $Q = q^2$, and the defining equation
$z_{\mathrm{GL}} = Q^r(1-Q)/(1-Q^r)$ has the **exact** solution $r = 2$.
The specialisation is then $s_\lambda(1, Q)$ — a Schur polynomial in *two*
variables — which vanishes identically for $\ell(\lambda) \geq 3$ and, on the
two-row stratum $\lambda = (n-k,k)$, equals
$$
  s_{(n-k,k)}(1, Q) \;=\; Q^k \bigl(1 + Q + \cdots + Q^{\,n-2k}\bigr)
  \;=\; q^{\,n}\,[\,n-2k+1\,]_q .
$$
The $q^n$ cancels against the normaliser $Z$, leaving
$y_{(n-k,k)} = [n-2k+1]_q/[2]_q^n$ and $y_\lambda = 0$ for
$\ell(\lambda) \geq 3$. So the row cap is not an extra hypothesis: it is
$r = 2$, the dimension of the $\mathrm{SU}_q(2)$ fibre, read off the bridge
equation itself.

## Canonical structural verification

Per-partition agreement at $H_3$, $H_4$, $H_5$ (representative entries):

See [Table 2](#tbl:y-lambda-closed-form-wenzl-bridge-table2-data).

The two legs are the principal-specialisation route above and the $q$-integer
closed form; they agree **identically**, not to a numerical tolerance, and
$\sum_\lambda y_\lambda d_\lambda = 1$ holds exactly at each $n$.

No independent numerical cross-check of the bridge under convention D is recorded here.
