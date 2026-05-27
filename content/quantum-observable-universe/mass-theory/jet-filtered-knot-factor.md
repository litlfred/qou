**Conjecture.**
*Let $\beta(Z, N)$ be the nuclear braid of an $(Z, N)$ atom
([atomic braid](#def:atomic-braid)), and let $a(Z, N)$ be the
Bethe--Weizsäcker knot factor that multiplies the bulk binding
$B_{\mathrm{bulk}}$.  Then $a(Z, N)$ is determined by the
**jet-filtered character convergence** of the nuclear quotient
braid $\bar\beta$, obtained by collapsing each nucleon to its
Wedderburn trace.*

**Part 1 (Established).** *At each jet level $k \geq 3$, define
the per-level knot invariant*

$$
  a_k(\beta)
  = \frac{\sum_\lambda w_\lambda \,
    \chi_\lambda^{(k)}(\beta)}
  {\sum_\lambda w_\lambda \,
    \dim \mathrm{Res}^{H_k}_{H_3}(V_\lambda)}
$$

*where $w_\lambda = d_q(\lambda)^2/[k]_q!$ are the Wedderburn
weights and $\chi_\lambda^{(k)}(\beta)$ is the character of
$\beta$ in $V_\lambda$ restricted to $H_3(R, q)$ via the branching
rule.*

*Then $a_k$ **converges by $k = 4$**: for all $k \geq 4$, the
ratio $a_k$ is topology-independent (depends on $q$ but not on
$(Z, N)$ beyond the $H_3$ characters of $\beta$).*

*The denominator simplifies:
$\sum_\lambda w_\lambda \dim \mathrm{Res} = 1 + W_{\mathrm{std}}$
where $W_{\mathrm{std}} = (q^2 + 1)^2/(q^4 + 4q^2 + 1)$.*

**Part 2 (Established).** *The three $H_3(R, q)$ characters of the
inter-nucleon braid satisfy exact algebraic identities:*

1. *Extremal cancellation
  ([confined knot binding](#prop:confined-knot-binding)):
  for each proton-neutron crossing,
  $W_{\mathrm{sym}} \chi_{\mathrm{sym}} +
   W_{\mathrm{alt}} \chi_{\mathrm{alt}} = 0$.*

2. *Crossing balance: $\hat{V}_{\mathrm{pp}} +
  \hat{V}_{\mathrm{nn}} = 2\hat{V}_{\mathrm{pn}}$ exactly,
  where $\hat{V}_{xy}$ is the Wedderburn volume of a single
  $xy$-crossing.  The deviation is
  $\delta V = \hat{V}_{\mathrm{pp}} - \hat{V}_{\mathrm{pn}}
  = h/2$ (half the Hecke parameter).*

3. *For $Z = N$ even-even nuclei ($\mathrm{sp} = \mathrm{ap}
  = V_{\mathrm{std}}^{\mathrm{inter}}$):
  $a_k = V_{\mathrm{std}}^{\mathrm{inter}} / (1 + W_{\mathrm{std}})$.*

4. *For $Z = N$ odd-odd nuclei ($\mathrm{sp} = -\mathrm{ap}$,
  extremal cancellation):
  $a_k = W_{\mathrm{std}} \cdot V_{\mathrm{std}}^{\mathrm{inter}}
  / (1 + W_{\mathrm{std}})$.*

**Part 3 (Intermediate knot detection).** *During nucleon-by-nucleon
construction of $\beta(Z, N)$, the intermediate NF at each step
$A' \leq A$ matches a reference knot pattern (trefoil, Hopf link,
figure-eight, unknot) with measurable cosine similarity.  For $Z = N$
nuclei, the pattern **alternates**: trefoil at odd $Z$, Hopf link at
even $Z$.  Double-magic nuclei (${}^{16}\mathrm{O}$) converge to the
**unknot** ($\cos \approx 0.66$).*

**Part 4 (Conjecture).** *The BW knot factor $a(Z, N)$ is the
Jones polynomial of the **nuclear quotient braid** $\bar\beta$,
evaluated at $q$:*

$$
  a(Z, N) = J_{\bar\beta}(q)
$$

*where $\bar\beta$ is the braid obtained from $\beta(Z, N)$
by collapsing each nucleon (B$_{3}$ confinement + quark crossings +
gluon dressing) to a single effective crossing, retaining only
the inter-nucleon topology.*

*For known knot types:*

| $A$ | Quotient braid | $J(q)$ | Verified |
|-----|---------------|--------|----------|
| $2$ | single pn crossing | $1$ (satellite) | $\checkmark$ |
| $3$ | figure-eight $4_1$ | $1 - h^2$ | $\checkmark$ |
| $4$ | Borromean $B_3^2$ | $(1 - h^2)^2$ | $\checkmark$ |
| $\geq 5$ | quotient nuclear braid | $J_{\bar\beta}(q)$ | **open** |

*The quotient braid $\bar\beta$ for $A \geq 5$ involves
$\binom{A}{2}$ inter-nucleon crossings of types pp, nn, pn.
Its Jones polynomial is a Laurent polynomial in $q$, computable
from the transfer matrix $V_{\mathrm{std}}$ of the inter-nucleon
crossing chain.  The conjecture asserts that this polynomial,
properly normalised, gives the BW knot factor.*

*Evidence: for ${}^6\mathrm{Li}$, the needed knot factor
$a \approx 1.134$ satisfies
$(1 - h^2)^2 \cdot (1 + h^2)^5 \approx 1.133$ — suggestive of
$2$ amphicheiral channels (from the ${}^4\mathrm{He}$ core) and
$5$ chiral channels (from the additional pn structure).  The
exponent $5$ and its algebraic origin are open.*

*The **NF transition lifting** approach (tracking how the NF
changes at each nucleon addition and using the transition element
to weight confinement channels) provides a potential path to a
closed-form recursive formula.*

**Witness**: `jet-knot-invariants.witness.json`,
`intermediate-knot-detection.witness.json`.
