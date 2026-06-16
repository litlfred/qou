## Definition

Let $H_n(q)$ be the Iwahori–Hecke algebra on $n$ strands with the
canonical Wedderburn decomposition
$$
  H_n(q) \;\cong\; \bigoplus_{\lambda \vdash n} \mathrm{End}(V_\lambda)
$$
indexed by partitions $\lambda \vdash n$. The
:defterm[two-row stratum]{#two-row-stratum}
is the subset of partitions with at most two parts:
$$
  \Lambda^2(n) \;:=\; \{\, \lambda \vdash n : \ell(\lambda) \le 2 \,\}
  \;=\; \{\, (n-k, k) : 0 \le k \le \lfloor n/2 \rfloor \,\}.
$$

The corresponding
:defterm[two-row projection]{#two-row-projection}
$$
  \pi_{\mathrm{2-row}} \;\colon\; H_n(q) \;\to\;
    \bigoplus_{\lambda \in \Lambda^2(n)} \mathrm{End}(V_\lambda)
$$
is the orthogonal projection onto the two-row Wedderburn subalgebra
(idempotent: $\pi_{\mathrm{2-row}}^2 = \pi_{\mathrm{2-row}}$). The
canonical Markov trace splits accordingly:
$$
  \mathrm{tr}_M(\beta)
  \;=\; \underbrace{\sum_{\lambda \in \Lambda^2(n)} y_\lambda(q) \cdot \chi^\lambda_q(\beta)}_{\mathrm{tr}_M(\pi_{\mathrm{2-row}}\,\beta)}
  \;+\; \underbrace{\sum_{\ell(\lambda) > 2} y_\lambda(q) \cdot \chi^\lambda_q(\beta)}_{\mathrm{tr}_M((1-\pi_{\mathrm{2-row}})\,\beta)}
$$

with $y_\lambda$ the Wenzl weight
from [`prop:wedderburn-weight-canonical`](#prop:wedderburn-weight-canonical).

## Structural significance

The two-row stratum carries the $\mathrm{SU}(2)$ Schur–Weyl image. Under
the natural restriction
$$
  H_n(q) \;\twoheadrightarrow\; \mathrm{End}_{\mathrm{SU}(2)}\!\bigl(V^{\otimes n}\bigr),
\quad V = \mathbb{C}^2,
$$
partitions with $\ell(\lambda) > 2$ lie in the kernel — they correspond
to higher-rank symmetry components absent from the $\mathrm{SU}(2)$
spin-pairing observable. The two-row sector is where the
$q$-deformed spin observables — including the
magic-shell coupling of
`conj:magic-shell-stabilization`
— live.

## Indexing the stratum

$|\Lambda^2(n)| = \lfloor n/2 \rfloor + 1$. For $n = 12$ (the
$^4\mathrm{He}$ strand count) this gives **7** partitions:

$$
\Lambda^2(12) = \{(12), (11,1), (10,2), (9,3), (8,4), (7,5), (6,6)\}.
$$

Some of these are particularly distinguished:

- $\lambda = (n)$: trivial rep; one-dimensional, $V_{(n)} = \mathbb{C}$.
- $\lambda = (n-1, 1)$: standard rep; dimension $n - 1$.
- Self-conjugate $\lambda$ within $\Lambda^2(n)$: only $(n/2, n/2)$
  when $n$ is even — the **balanced two-row** partition. For
  $n = 12$, this is $(6, 6)$.

The non-self-conjugate two-row partitions $(n-k, k)$ with $k < n/2$
form mirror pairs under the bar involution $q \mapsto q^{-1}$ (each
$(n-k, k)$ paired with itself under the involution, since the
conjugate partition $(n-k, k)' = (2, 2, \dots, 2, 1, \dots)$
generally exits $\Lambda^2$).

## Empirical use

The companion probe
[`probe_he4_canonical_tr_m_fingerprint.py`](computations/probe_he4_canonical_tr_m_fingerprint.py)
computes the per-partition decomposition
$c_\lambda := y_\lambda(q_0) \cdot \chi^\lambda_q(\beta_{^4\mathrm{He}})$
across all 77 partitions of 12 and finds the two-row stratum
$\Lambda^2(12)$ carries $86.6\,\%$ of $\mathrm{tr}_M(\beta_{^4\mathrm{He}})$ — the
content of [`prop:he4-two-row-dominance`](#prop:he4-two-row-dominance).

The earlier
[`delta_lambda_2row_stratum_analysis.py`](computations/delta_lambda_2row_stratum_analysis.py)
established the same pattern across $\{D, T, {}^3\mathrm{He}, {}^4\mathrm{He}\}$:
the dominant block per atom always lies in $\Lambda^2(3A)$.
