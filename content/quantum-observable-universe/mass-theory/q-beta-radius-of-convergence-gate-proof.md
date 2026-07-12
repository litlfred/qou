## Proof

Write $c_k$ for the pinned ladder coefficients at the substrate
anchor (canonical SDP extraction,
`qbeta-decay-sdp-extended-ck.witness.json`),
$g(u) := \sum_{k \ge 2} c_k u^k$ for the log-correction generating
function, and $u_0 := u_{\text{substrate}} \approx 0.00852$.

**Step 1 — rationality of $g$.** By the
[$c_k$ recursion](q-beta-c-k-recursion-from-habiro-q-difference.md),
the ladder coefficients of any admissible candidate Habiro element
$F(q)$ satisfy a depth-$d$ linear recursion with constant
($q_0$-rational) coefficients,
$c_{k+1} = \sum_{j=1}^{d} a_j\,c_{k+1-j}$. A sequence satisfying such
a recursion has a rational generating function: multiplying the
recursion by $u^{k+1}$ and summing gives
$g(u) = P(u)/Q(u)$ with $Q(u) = 1 - \sum_{j=1}^{d} a_j u^j$ and
$\deg P \le d + 1$. The singularities of $g$ are therefore
exclusively poles, located at the reciprocals $1/r$ of the roots $r$
of the characteristic polynomial
$\chi(x) = x^d - \sum_{j=1}^{d} a_j x^{d-j}$ (with multiplicities, up
to cancellation against $P$). No branch points and no essential
singularities can occur, and the radius of convergence of the series
is $1/|r_{\max}|$ for $r_{\max}$ a characteristic root of maximal
modulus surviving cancellation.

**Step 2 — asymptotic signature of a simple dominant pole.** Suppose
the dominant root $r_{\max}$ is unique (no other root of equal
modulus) with multiplicity $\mu$, and set $\rho := 1/r_{\max}$.
Partial fractions give
$c_k = C\,k^{\mu-1} r_{\max}^{\,k}\,\bigl(1 + o(1)\bigr)$ for some
constant $C \ne 0$. Two consequences:

1. *Ratio test.* $c_{k+1}/c_k \to r_{\max} = 1/\rho$.
2. *Normalized magnitude.* $c_k\,\rho^k = C\,k^{\mu-1}(1 + o(1))$: a
   flat (constant) asymptote is the exact signature of $\mu = 1$, a
   simple pole. For $\mu \ge 2$ the sequence must grow by the factor
   $((k+1)/k)^{\mu-1}$, at least $12.5\,\%$ per step at $k = 8$; a
   dominant complex-conjugate pair would instead make $c_k \rho^k$
   oscillate with the argument of $r_{\max}$.

Within the rational class forced by Step 1, these finite-order
signatures are therefore *decisive*: flatness of $c_k \rho^k$
together with convergence of the ratio identifies a unique simple
dominant pole at $u = \rho$.

**Step 3 — locating the canonical pole.** The pinned
$c_2, \ldots, c_{10}$ exhibit exactly the simple-pole signature at
$\rho = u_0$ (table below): the ratio $c_{k+1}/c_k$ converges to
$1/u_0 \approx 117.4$ by $k = 10$; the normalized magnitudes
$c_k\,u_0^k$ for $k \in \{8, 9, 10\}$ agree at
$\approx 2.118 \times 10^{-13}$ with $0.02\,\%$ spread — flat to
$2 \times 10^{-4}$ per step, excluding $\mu \ge 2$ (which forces
$\ge 12\,\%$ growth) and a dominant complex pair (which forces
oscillation); and the log-slope fit of $\ln(c_k u_0^k)$ against
$\ln k$ gives exponent $\beta \approx 0.999$ against the calibration
$c_k \rho^k \sim k^{\beta-1}$, forcing the integer $\mu = \beta = 1$.
Hence the canonical generating function has a unique dominant simple
pole at $u = u_0$, within the resolution of the $k \le 10$ window.
The location is anchor-stable: re-pinning from the proton to the muon
anchor shifts $u_0$ by only $2.10 \times 10^{-7}$ relative (210 ppb,
table below).

**Step 4 — gate direction and tolerance.** Let $F$ be a candidate
generating coefficients $\tilde c_k$ by the same recursion mechanism,
with rational $\tilde g(u) = \sum_k \tilde c_k u^k$ (Step 1 applies
verbatim) and nearest pole $\tilde u_0$. Suppose
$|\tilde u_0 - u_0|/u_0 > 10^{-6}$. If $\tilde c_k = c_k$ for all
sufficiently large $k$, then $\tilde g - g$ would be a polynomial, so
$\tilde g$ and $g$ would have identical poles — contradicting
$\tilde u_0 \ne u_0$. Hence $\tilde c_k \ne c_k$ for arbitrarily
large $k$: the candidate does not generate the canonical ladder, and
is refuted at the fibre level, before any canonical-anchor sweep at
$q_0$. The $10^{-6}$ tolerance is calibrated from below by the
cross-anchor swing: the true kernel's pole location moves by only
$2.10 \times 10^{-7}$ under the proton–muon re-pin, so the true
kernel always passes (no false refutation), while the tolerance
remains nearly $5\times$ above that swing so that anchor choice can
never trip the gate. From above, it is far sharper than the
few-percent near-match band delegated to the $\S 4(d)$
direction-sanity gate — the two gates are complementary by
construction. $\blacksquare$

## canonical anchor (verified)

From the canonical SDP extraction at $q_0 = 1.10997858\ldots$:

| quantity | value |
|---|---|
| $u_{\text{substrate}}$ at $q_{\text{proton}}$ | $0.008517234550156142$ |
| $u_{\text{substrate}}$ at $q_{\text{muon}}$ | $0.008517236340043958$ |
| relative shift | $2.10 \times 10^{-7}$ (210 ppb) |
| asymptotic $c_k \cdot u^k$ ($k \in \{8,9,10\}$) | $2.118 \times 10^{-13}$ |
| spread | $0.02$ % |
| branch-fit $\beta$ | $0.999$ (simple-pole case is $\beta = 1$) |
| ratio test $c_{k+1}/c_k$ at $k = 10$ | $\to 1 / u_{\text{substrate}} = 117.4$ |
