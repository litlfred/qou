## Evidence

Steps 1 and 2 are proved statements about generating functions. Steps 3 and 4 explain what the finite window of coefficients does and does not show.

Write $c_k$ for the pinned ladder coefficients at the substrate
anchor (canonical SDP extraction),
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

Both consequences are statements about the limit $k \to \infty$.
They identify a unique simple dominant pole at $u = \rho$ only when
the whole sequence is known.

**Step 3 — what the window shows.** The pinned convention-C
coefficients $c_2, \ldots, c_{10}$ show the simple-pole signature at
$\rho = u_0$ (table below). The ratio $c_{k+1}/c_k$ approaches
$1/u_0 \approx 117.4$ by $k = 10$. The normalised magnitudes
$c_k\,u_0^k$ for $k \in \{8, 9, 10\}$ agree at
$\approx 2.118 \times 10^{-13}$ with $0.02\,\%$ spread. A log-slope fit
of $\ln(c_k u_0^k)$ against $\ln k$ gives $\beta \approx 0.999$, close
to the simple-pole value $\beta = 1$.

These are finite-window measurements, and they do not determine the
pole. For any rational $h$, the series $g(u) + u^{11} h(u)$ has the
same coefficients $c_2, \ldots, c_{10}$ and its poles include those of
$h$, which can be placed anywhere. So the window is consistent with a
unique simple dominant pole at $u_0$, and it is equally consistent
with other pole locations and orders. That is why the statement is a
conjecture. The window's signature is also anchor-stable: re-pinning
from the proton to the muon anchor moves $u_0$ by
$2.10 \times 10^{-7}$ relative (210 ppb).

**Step 4 — the test, assuming the conjecture.** Let $F$ be a candidate
generating coefficients $\tilde c_k$ by the same recursion mechanism,
with rational $\tilde g(u) = \sum_k \tilde c_k u^k$ (Step 1 applies)
and nearest pole $\tilde u_0 \ne u_0$. If $\tilde c_k = c_k$ for all
sufficiently large $k$, then $\tilde g - g$ is a polynomial, so
$\tilde g$ and $g$ have the same poles. Hence, if $g$ has its dominant
pole at $u_0$ as conjectured, the candidate does not reproduce the
ladder for all large $k$. This implication is proved; its premise is
the conjecture.

The operational threshold
$|\tilde u_0 - u_0|/u_0 > 10^{-6}$ is a chosen value. It sits about
$5\times$ above the measured proton–muon shift of $u_0$, so anchor
choice alone does not trip the test, and it is much sharper than the
one-decade window used by the $\S 4(d)$
[direction-sanity gate](q-beta-direction-sanity-gate.md). A candidate
that fails it is inconsistent with this conjecture, which is a
scope-limited negative, not a structural refutation.

## Measured window (convention-C frame)

From the SDP extraction (convention C) at $q_0 = 1.10997858\ldots$:

| quantity | value |
|---|---|
| $u_{\text{substrate}}$ at $q_{\text{proton}}$ | $0.008517234550156142$ |
| $u_{\text{substrate}}$ at $q_{\text{muon}}$ | $0.008517236340043958$ |
| relative shift | $2.10 \times 10^{-7}$ (210 ppb) |
| asymptotic $c_k \cdot u^k$ ($k \in \{8,9,10\}$) | $2.118 \times 10^{-13}$ |
| spread | $0.02$ % |
| branch-fit $\beta$ | $0.999$ (simple-pole case is $\beta = 1$) |
| ratio test $c_{k+1}/c_k$ at $k = 10$ | $\to 1 / u_{\text{substrate}} = 117.4$ |
