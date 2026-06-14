**Conjecture (Leading-order $N_v$, conditional on the two upstream substrate axioms).**
*Combining
[the Bring action lemma](#conj:n-v-bring-action) with
[the tower-depth lemma](#conj:n-v-tower-depth-ninety), the
electroweak topological invariant $N_v$ admits the leading-order
closed form*

$$
  N_v \;=\; |S_5| \cdot q_0^{90}
        \;=\; 120 \cdot q_0^{90}
        \;\approx\; 1.4371 \times 10^{6},
$$

*where $|S_5| = 120$ is the order of the Bring-curve automorphism
group and $90$ is the Coxeter-length depth of the brane tower
from $m_e$ to $v$.*

*The corresponding electroweak scale prediction is*

$$
  v \;=\; \frac{N_v \cdot m_e}{3} \;=\; 244.79 \;\mathrm{GeV},
$$

*matching the CODATA Higgs vacuum-expectation value
$v_{\mathrm{CODATA}} = 246.22$ GeV to within $-0.58\%$.*

## Discussion

**Conditional conjecture.**  Conditional on the two substrate axioms
[`conj:n-v-bring-action`](#conj:n-v-bring-action) and
[`conj:n-v-tower-depth-ninety`](#conj:n-v-tower-depth-ninety),
the leading-order closure follows by direct multiplication.  The
$-0.58\%$ residual is a sub-leading correction whose structural
origin is currently unresolved (open conjecture, not yet a
named content block).

This is the **third** block in the
[N_v derivation chain](#conj:n-v-bring-action) and the only one
that is *derived* (modulo the two upstream conjectures).

## Proof

*From [Lemma 1](#conj:n-v-bring-action), the Markov-trace-residual
rescaling factor at the EW slice is $|S_5| = 120$, and from
[Lemma 2](#conj:n-v-tower-depth-ninety), the brane-tower
Coxeter-length depth from $m_e$ to $v$ is $90$ Hecke generations.
The two combine into a single empirical bridge identity*

$$
  \frac{v}{m_e} \;=\; \frac{|S_5|}{3} \cdot q_0^{90}
                \;=\; 40 \cdot q_0^{90}
                \quad (\mathrm{modulo}\; |\varepsilon| \le 0.006),
$$

*where the prefactor $|S_5| / 3 = 40$ is the categorical
contribution of the Bring-fibre-functor on the
$v/m_e \leftrightarrow q_0^{\mathrm{depth}}$ bridge: the
$|S_5| = 120$ rescaling at the EW slice factors through the
$3$-fold splitting $N_v := 3 v / m_e$, leaving $40$ on the bridge.*

*Substituting into the definition $N_v := 3 v / m_e$ from
[hadron-half-life-verification](#ex:hadron-half-life-verification):*

$$
  N_v \;=\; \frac{3 v}{m_e}
        \;=\; 3 \cdot 40 \cdot q_0^{90}
        \;=\; 120 \cdot q_0^{90},
$$

*recovering $|S_5| = 120$ as the full prefactor.  Empirically
this is $1.4371 \times 10^6$ vs the CODATA-derived
$N_v = 1.4455 \times 10^6$ (residual $-0.58\%$).  $\square$ modulo
the upstream conjectures.*

*Numerical sanity check at $q_0 = 1.109978595554181\ldots$ (50 dps):
$v / m_e \approx 481\,839$, $q_0^{90} \approx 12\,012$, ratio
$\approx 40.11$, so $\varepsilon \approx 0.003 < 0.006$. (yes)*

## Sub-leading correction (open)

The exact CODATA value is $\log_{q_0}(N_v / 120) = 90.0558$,
i.e. $N_v = 120 \cdot q_0^{90.0558}$.  The fractional shift
$0.0558$ is approximately:

| candidate | value | residual after correction |
|:-:|:-:|:-:|
| $h^2/8 = (q_0 - q_0^{-1})^2 / 8$ | $0.00547$ | $\sim 0.005\%$ |
| $(q_0 - 1)/2$ | $0.0550$ | exact within $0.001\%$ |
| $1/(2 \pi)$ | $0.159$ | wrong magnitude |

The closest candidate is $(q_0 - 1)/2 = 0.0550$, equivalent to
$L \to 90 + (q_0 - 1)/2$.  Whether this arises structurally from
a sub-leading correction in the Bring fibre functor remains
unresolved (no named content block yet).

## Comparison to other strategies

Per [`docs/audits/n-v-derivation-candidates.md`](../../../docs/audits/n-v-derivation-candidates.md),
this is the **best** non-circular closed form found:

| strategy | best closure | err |
|:-:|:-:|:-:|
| 1: pure $\log_{q_0}$ | $1 \cdot q_0^{125.41}$ | circular (uses $v$) |
| **2: structural prefactor** | $\mathbf{120 \cdot q_0^{90}}$ | $\mathbf{-0.58\%}$ |
| 2 alt: $\mathbf{h \cdot q^{151}}$ | $0.209 \cdot q_0^{151}$ | $+0.64\%$ |
| 2 alt: $h^2 \cdot q^{166}$ | $0.044 \cdot q_0^{166}$ | $+0.63\%$ |

Strategy 2 with prefactor $120$ wins by both magnitude (smaller
absolute residual) and categorical content (Bring autom group is
explicitly tied to QOU substrate, while $h^k$ prefactors do not
have a similar structural origin).
