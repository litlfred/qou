The Mittag-Leffler formula
([GB residue spectral sum](#prop:gb-residue-spectral-sum)) sums
residues of the mass trace at the root-of-unity poles
$\zeta_\ell$.  The previous exposition illustrated the dominant
contribution at $\zeta_1 = 1$, closest to $q_0 \approx 1.11$.
This proposition enumerates **all** poles and shows why the sum
cannot be truncated at the nearest one without losing structural
information: the higher-order residues can interfere constructively
or resonate.

**Proposition (full pole enumeration).**
*Working over $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$ and
specialising to a target ring $k$ with $q$ taking values in $k^\times$,
the Markov trace $q \mapsto \mathrm{tr}_M(T_w, q)$ extends to a
meromorphic function of $q$ with simple poles at every primitive
root of unity $\zeta_n^{(j)} = e^{2\pi i j/n}$ for $\gcd(j, n) = 1$
and $n \geq 2$, arising from zeros of the $q$-integer factors
$[k]_q = (q^k - q^{-k})/(q - q^{-1})$ in the denominators of the
Wedderburn weights $w_\lambda(q)$.*

*The Mittag-Leffler expansion at $q_0$ is*

$$
  \mathrm{tr}_M(T_w, q_0)
  \;=\;
  \mathrm{tr}_M^{\mathrm{entire}}(T_w, q_0)
  \;+\;
  \sum_{n \geq 2} \sum_{\substack{j=1 \\ \gcd(j,n)=1}}^{n-1}
    \frac{r_n^{(j)}(T_w)}{q_0 - \zeta_n^{(j)}},
$$

*with residues $r_n^{(j)}(T_w) \in k$ and kernel
$1/(q_0 - \zeta_n^{(j)})$.  The sum is absolutely convergent on
the regular locus (Habiro's theorem,
[Habiro ring](#def:habiro-ring)).*

**Distances to $q_0 = 1.11$: not monotone in $n$.**
*Write $\zeta_n^{(j)} = \cos(2\pi j/n) + i\sin(2\pi j/n)$.  Then*

$$
  \bigl|q_0 - \zeta_n^{(j)}\bigr|^2
  \;=\;
  q_0^2 - 2 q_0 \cos(2\pi j/n) + 1.
$$

*Distances for the lowest $n$ with $q_0 = 1.11$:*

| $n$ | $\zeta_n^{(j)}$ | $|q_0 - \zeta_n^{(j)}|$ | $1/\lvert q_0 - \zeta_n^{(j)}\rvert$ |
|---|---|---|---|
| 1 | $+1$  | $0.11$ | $9.1$ |
| 2 | $-1$  | $2.11$ | $0.47$ |
| 3 | $e^{\pm 2\pi i/3}$ | $1.67$ | $0.60$ |
| 4 | $\pm i$ | $1.49$ | $0.67$ |
| 5 | $e^{\pm 2\pi i/5}$ | $1.33$ | $0.75$ |
| 6 | $e^{\pm\pi i/3}$ | $1.06$ | $0.94$ |
| 7 | $e^{\pm 2\pi i/7}$ | $0.92$ | $1.09$ |
| 8 | $e^{\pm\pi i/4}$ | $0.84$ | $1.19$ |
| 10 | $e^{\pm\pi i/5}$ | $0.72$ | $1.39$ |
| 12 | $e^{\pm\pi i/6}$ | $0.62$ | $1.61$ |

*The distance is **not monotone** in $n$: $\zeta_1$ is uniquely
closest, but $\zeta_6, \zeta_7, \zeta_8, \ldots$ are all closer to
$q_0$ than $\zeta_2$ or $\zeta_3$.  Truncating at the closest pole
(only $\zeta_1$) discards the bulk of the sum.*

**Conjugate pairs and reality.**
*For each non-real $\zeta_n^{(j)}$ the conjugate $\zeta_n^{(n-j)}
= \overline{\zeta_n^{(j)}}$ is also a primitive $n$-th root of
unity, and $r_n^{(j)} = \overline{r_n^{(n-j)}}$.  The pair's
Mittag-Leffler contribution sums to the real quantity*

$$
  \frac{r_n^{(j)}}{q_0 - \zeta_n^{(j)}}
  + \frac{\overline{r_n^{(j)}}}{q_0 - \overline{\zeta_n^{(j)}}}
  \;=\;
  \frac{2 \operatorname{Re}\bigl[r_n^{(j)} (q_0 - \overline{\zeta_n^{(j)}})\bigr]}
       {q_0^2 - 2q_0\cos(2\pi j/n) + 1},
$$

*so each cyclotomic level $n \geq 3$ contributes a real sum over
$\varphi(n)/2$ conjugate pairs.  The total mass is real despite
being built from complex residues.*

**Interference and resonance.**
*Because the residues $r_n^{(j)}(T_w)$ depend on how the braid
word $T_w$ intersects the $n$-th filtration stratum, different
braids have different residue patterns.  Three observable
regimes:*

1. *$\zeta_1$-dominant (simple braids, confinement level
   $\ell(K) = 1$).  Only $r_1(T_w)$ is large; higher $r_n$ are
   suppressed.  Regime of trefoil and other level-$1$ nuclei.*
2. *Resonant cancellation (intermediate braids).  Residues
   $r_n^{(j)}$ at several $n$ have alternating signs and similar
   magnitudes; their sum is smaller than any individual term.
   This regime produces **stable** configurations whose masses
   sit below the $\zeta_1$-only approximation.*
3. *Resonant enhancement (deep braids, $\ell(K) \geq 3$).
   Residues at several $n$ reinforce each other.  This regime
   produces **unstable** configurations whose masses sit above
   the $\zeta_1$-only approximation — a structural account of
   the drip-line kinks noted in
   ([what empirical BW misses](#rem:bw-empirical-misses)).*

*Truncating at $\zeta_1$ alone replaces every configuration with
a non-resonant baseline, losing precisely the regimes (2) and
(3) that encode nuclear stability structure.*

**Habiro-ring reformulation (convergent form).**
*Instead of summing the Mittag-Leffler expansion pole by pole,
the full residue structure is packaged in the Habiro cyclotomic
expansion*

$$
  \mathrm{tr}_M(T_w, q_0)
  \;=\;
  \sum_{m \geq 0} a_m(T_w) \cdot (q_0; q_0)_m,
  \qquad
  (q_0; q_0)_m = \prod_{k=1}^{m}(1 - q_0^k),
$$

*where $a_m(T_w) \in \mathbb{Z}[q, q^{-1}]$ are the cyclotomic
coefficients.  The $m$-th term $(q_0; q_0)_m$ vanishes at every
$\zeta_n$ with $n \leq m$, so truncating at order $m$ **neglects
exactly** the residues from roots of unity of order $\leq m$.
Habiro's convergence theorem
([Habiro ring](#def:habiro-ring)) shows the series converges for
all $q_0$ in the image of the Habiro ring's completion.
Consequence: **every order-$m$ truncation loses only the
$\zeta_1, \ldots, \zeta_m$ residues, not the higher ones**, so
the Habiro form is the natural symbolic-computation target for
the spectral sum.*

**Relation to Chern–Simons level-$k$ truncation.**
*Each root of unity $\zeta_k^{(1)} = e^{2\pi i/k}$ corresponds to
a level-$(k-2)$ Chern–Simons theory on $S^3$ (Reshetikhin–Turaev).
The residue $r_k^{(1)}(T_w)$ at $\zeta_k^{(1)}$ is the RT
invariant of the closed braid at level $k-2$.  The full
spectral sum is therefore a sum over all Chern–Simons levels,
with the Cauchy kernel giving each level a geometric weight.*

**Consistency with the dominant-pole approximation.**
*The $\zeta_1$-only approximation captures $\sim 9.1/\sum_n 1/|q_0
- \zeta_n^{(j)}|$ of the total kernel weight: dominant but not
overwhelming.  For light atoms in the regime-(1) baseline the
approximation is good; for atoms in regime (2) or (3) it fails
at the percent level — consistent with the observed $5\%$–$20\%$
discrepancies on $^4$He through $^{40}$Ca in the current
three-channel witness.*
