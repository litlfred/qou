The per-rung coefficients $c_k$ below are the Taylor coefficients of the
finite Habiro sum $\sum_{m=0}^{M} a_m(u)\,(u;u)_m$ with $a_m \in \mathbb{Z}[u]$
and $M = 8$ for the proton and neutron
([Habiro–ladder equivalence](habiro-precision-ladder-equivalence.md)).
The exact evaluation uses that sum directly, with no rung-by-rung truncation;
the ladder records how the per-rung structure arises.

## Per-rung categorical sources

See [Table 1](#tbl:q-beta-categorical-precision-ladder-table1-data).

The categorical primitives are **two**:

- **Kashiwara $b(q) = \sqrt{q^4+q^2+1}/(q^2+1)$** — Hoefsmit off-diagonal coupling on $V_{(2,1)}$.
- **Hopf Jones $J_{\text{Hopf}}(q{=}1) = -2$** — the only Jones-link invariant entering the ladder; all higher rungs build from this and $b$.

**Mixing pattern across rungs:**

- $c_1, c_2$: pure Kashiwara (no Jones).
- $c_3$: pure Jones (no Kashiwara).
- $c_4$: multiplicative Jones $\times$ Kashiwara mixing ($c_3 \cdot b^4$).
- $c_5$: Kashiwara $b^2$ plus a half-Hopf offset, mixed intra/inter block ($-(b^2 + 1/2)$).

Two supersessions, in order. The earlier $c_4 = b^2 + 1/2$ form is superseded: it is 9.5% off the empirical value, while $c_3 \cdot b^4$ matches to 0.9%. The expression $b^2 + 1/2$ was then reassigned to the $c_5$ slot, carrying its categorical reading with it. The earlier $c_5 = c_3^2 \cdot 3 + b = +12.87$ form is in turn superseded: the SDP extraction gives $c_5 = -1.2229$, from which $-(b^2 + 1/2) = -1.2527$ is 2.4% away while $+12.87$ is an order of magnitude away and of the opposite sign.

The KL decategorification governs the appearance of
classical-limit Jones values: the mass observable lives in the KL
classical limit of the Hecke / quantum-group representation theory, so
Jones invariants enter at $q = 1$ rather than at substrate $q_0$.

## Truncation order and error estimate

The ladder is a **convergent series**: $N$ is a *truncation order*
chosen by the target precision, not an all-or-nothing
canonicity decision. The ladder step is

$$
u \;=\; b\,\hbar_q^2 \;\approx\; 0.00852, \qquad
  \frac{1}{u} \approx 117, \qquad \log_{10}\!\frac{1}{u} \approx 2.07,
$$

so **each rung gains $\approx 2.07$ decimal digits**. The truncation
error after $N$ rungs is the standard first-dropped-term bound

$$
\varepsilon_N \;\approx\; \bigl|c_{N+1}\,u^{N+1}\bigr|,
$$

and the required order for relative precision $\varepsilon$ is

$$
N \;\geq\; \frac{\log_{10}(1/\varepsilon)}{\log_{10}(1/u)} - 1
  \;\approx\; \frac{\log_{10}(1/\varepsilon)}{2.07} - 1.
$$

| target | $N$ required |
|---|---|
| $100\times$ experimental ($7.8$ ppb) | $3$ |
| $1$ ppb | $4$ |
| $1$ ppt | $5$ |
| $1$ ppQ ($10^{-15}$) | $7$ |

**Coefficient tier (read with the truncation order).** The $c_k$ carry a
provenance tier: $c_2 = -1$ is **structural** — the exact $u^2$ coefficient
of the explicit-factor product $\prod_{k\ge2}(1 + c_k u^k)$, and therefore
$q_0$-independent by definition. It is not **proved**: the Lean re-reads the $N{=}2$ factor
rather than deriving it. And it is Taylor-exact *for that series* — the
normalised series (cosine factor inside) has $\tilde c_2 = c_2 - 1/8 = -9/8$; $c_k$ for $k \geq 3$ are at present **structural
near-matches** — their empirical value swings with the $q_0$ anchor
(e.g. $c_3$: $-2.010$ at the muon-pin $q_0$, $-2.069$ at the $m_p$-pin
$q_0$), so they are not yet Taylor-exact derivations. A near-match that
beats the experimental target is a genuine result *and* not a
derivation. The permanent
upgrade is to identify the $\mathfrak{Q}_\beta$ **Habiro element** whose Taylor
coefficients *are* the $c_k$ — the same machinery that made the $\alpha_{EM}$
next-order factor $[2]_q(1-h^2\alpha)$ binomial-exact
([`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)).

## canonical precision ladder

Verified at $q_0$ via the canonical formalism at 50 dps:

See [Table 2](#tbl:q-beta-categorical-precision-ladder-table2-data).

The N=4 rung is the first to beat the **7.80 ppb 100$\times$ experimental
target** (CAL-3 σ = 0.78 ppm) — with $c_3$ at tier *near-match* (see the
truncation-order section above). N=3 lands at 13.15 ppb, above that target.
The **signed** column is strictly decreasing at both documented pins: with
the live $c_5 = -(b^2 + 1/2)$ every rung factor $1 + c_k u^k$ has $c_k < 0$
and is therefore below 1. **That is not what the non-monotonicity claim is
about.** The claim
concerns the residual *magnitude* — whether the approximation gets worse —
and on magnitude the signature **survives, and survives only under the live
coefficient**. At the proton pin:

| $N$ | $\lvert\text{residual}\rvert$, live $c_5$ | $\lvert\text{residual}\rvert$, superseded $c_5$ |
|---|---|---|
| 4 | 6.1698 ppb | 6.1698 ppb |
| 5 | **6.2260 ppb** (increases) | 5.5551 ppb (decreases) |

So the $N{=}4 \to N{=}5$ non-monotonicity is produced by the **live**
$c_5 = -(b^2+1/2)$ and is *absent* under the superseded $+12.87$. Reading the
signed column, where $-6.1698 \to -6.2260$ is decreasing, gives the reverse
conclusion. The ladder therefore carries a numerical signature of its own
inexactness on the live coefficient.

**Caveat:** the crossing is only $0.91\,\%$, computed with $c_3$ at the
recorded proton extraction and at the proton pin alone, so it is not robust
to a large $c_3$ move; a full settlement re-extracts $c_3$ at both pins. The
near-match tier of $c_{k\geq3}$ rests independently on the q$_0$-anchor swing
recorded above and does not depend on this crossing.
Agreement at $q_0$ is research-grade and **conditional on** the
Habiro-element upgrade, not an unconditional derivation.

The $N=2$ slight over-ceiling reflects that the Kashiwara-only prediction
gives $b^2$ (= 0.7527) rather than the exact empirical $0.7656$ — the
1.7% gap accumulates to the 0.28 ppm over-shoot. The $N=3$ Hopf
correction absorbs this and brings the residual under the c(K) ceiling.

## Implication for $\Delta S$ (n−p mass split, 1 ppb)

From the canonical formalism:

$$
  \varepsilon_{\Delta S} \;=\; \frac{\mathfrak{Q}_\beta}{\mathfrak{Q}_\beta + m_e} \cdot \varepsilon_Q
  \;\approx\; 0.605 \, \varepsilon_Q.
$$

See [Table 3](#tbl:q-beta-categorical-precision-ladder-table3-data).

At $N=3$ the n−p mass-split residual is **7.96 ppb**, above the 4.74 ppb
100$\times$-experimental Δm_pn target; **$N=4$ is the first rung below
it**, at 4.35 ppb, with $N=5$ taking off a further 0.03 ppb. The chain does not reach
sub-ppb precision on this observable at either documented pin — an earlier
draft of this paragraph claimed it did, on the superseded column.

## Open

Extending the categorical treatment to all $c_k$ reduced
$c_4, c_5$ to closed forms in the two categorical primitives
$b$ (Hoefsmit Kashiwara) and $c_3 = -2$ (Hopf Jones at $q{=}1$), with
sub-percent empirical match. The remaining open questions:

1. **Why $c_4 = c_3 \cdot b^4$?** The multiplicative Jones $\times$
   Kashiwara mixing has no derived categorical proof yet. Suggested
   source: spectral-sequence stratification of the Wedderburn-block
   cohomology of $H_n(q)$.

2. **Why $c_5 = -(b^2 + 1/2)$?** The Kashiwara $b^2$ plus half-Hopf
   offset is suggestive but not derived, and it is 2.4% from the SDP
   extraction $-1.2229$. The earlier $c_3^2 \cdot 3 + b$ reading of this
   slot is superseded.

3. **Inductive closure for $k \geq 6$.** No closed forms proposed.
   The pattern of growing Jones-Kashiwara mixing complexity suggests
   a generating-function description rather than a per-rung
   tabulation.

The full inductive ladder follows from a categorical source for the
operator-valued generating function
$F(z, q) = \sum_k c_k(q) \cdot b(q)^k \cdot z^k$ — for instance the KLR
canonical basis or a Khovanov–Rozansky spectral sequence.

## Provenance of the tables

Tables 2 and 3 above are computed by
[`qbeta_precision_ladder_n5.py`](../../../computations/qbeta/qbeta_precision_ladder_n5.py)
at the muon-pin (CAL-2) $q_0$, in convention C, with $c_4 = c_3 b^4$ and
$c_5 = -(b^2 + 1/2)$. That producer is the first in the corpus to evaluate the
boxed five-rung product itself: the block's previously declared producer,
`probe_q_beta_operator_valued_N3.py`, stops at $N=3$, carries no $c_5$, and is
not the generator of these tables at all — its own witness records
$\varepsilon_{N=1} = 674.83$ ppm against the $+73.80$ ppm of the $N=1$ row,
because its first rung is $\cos(\alpha_{N=1})$ rather than the boxed
$\cos(\alpha - b\hbar_q^2/2)$.

**As previously published, for the record.** The $\varepsilon_Q$ column read
$+1677.5$, $+73.79$, $+1.24$ ppm, then $+6.02$, $-0.57$ ppb and, at $N=5$,
$\sim 0$ ppb in table 2 and $+0.04$ ppb in table 3; the headline residual was
quoted as $-0.0066$ ppm.

*The sign.* The published headline was negative. It cannot be: $\mathfrak{Q}_\beta^A$
sits 1677 ppm above CODATA and every live rung factor is below 1, so the ladder
descends to CODATA from above and a negative residual requires overshooting
zero. Over both documented pins and all four documented $(c_4, c_5)$
assignments the most negative fifth-rung residual is $+6.50$ ppb. This is a
scope-limited negative about the boxed ladder under those assignments, not a
proved invariant.

*The input epoch.* The published $\varepsilon_Q$ column sits 7.133 ppb below the
recomputed one. A change of inputs shifts $\mathfrak{Q}_\beta^A / \mathfrak{Q}_\beta^{\mathrm{CODATA}}$
by one relative amount and moves every rung by it, so the $N=3$ row calibrates
the whole column; applied to the recomputed column that single offset then
reproduces the published $N=2$ row (to its three significant figures) and the
published $N=4$ row (to $-0.572$ against $-0.57$) — the latter only with the
*retired* $c_4 = b^2 + 1/2$, so the published $N=4$ number predated the $c_4$
supersession that its own label column already carried. The cause of the 7.133
ppb offset is not identified: it is not the stored $Q_{\mathrm{AME}}$
(0.78233355931 against the present 0.7823334093099085, a 191.7 ppb gap in the
wrong direction), and not the CODATA-2018 to 2022 $m_e$ move (1.35 ppb).

*The headline's magnitude.* Under that same offset the published-epoch fifth-rung
residual lies in $[-0.63, +0.63]$ ppb across all four assignments, so $-6.6$ ppb
is unreachable at the published epoch as well as at the present one. The
published magnitude has no reproducible provenance in this ladder, and the
recomputed value replaces it rather than being reconciled with it.
