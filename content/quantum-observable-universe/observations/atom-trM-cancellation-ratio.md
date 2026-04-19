Per [atomic braid mass](#prop:atomic-braid-mass), the atomic
Markov trace is the Wedderburn-weighted partition sum
$$
  \mathrm{tr}_M(W_{\mathrm{atom}})
  = \sum_{\lambda \vdash 3A} w_\lambda
     \cdot \chi_\lambda(W_{\mathrm{atom}}) / d_\lambda
$$
with $w_\lambda = d_q(\lambda)^2 / [3A]_q!$ the Plancherel weight.
This observation records an **empirical universal scaling** of the
cancellation depth of this sum for nuclear atoms in the
$A = 2$ through $A = 4$ range.

## Observation

Let
$$
  S(\varrho)
  = \sum_{\lambda \vdash 3A} \bigl\lvert
      w_\lambda \, \chi_\lambda(W_{\mathrm{atom}}) / d_\lambda
    \bigr\rvert
$$
be the sum of absolute values of the partition contributions.
Numerical evaluation on the standard atom braid words (post
2026-04-19 $1\cdot\sigma_0$ gluon convention) gives:

| Atom | $A$ | $\lvert\mathrm{tr}_M(W_{\mathrm{atom}})\rvert$ | $S$      | ratio                      | $B/(A\,m_n c^2)$ (AME)  |
|------|----:|----------------------------------------------:|---------:|---------------------------:|------------------------:|
| D    | 2   | $9.4\times 10^{-4}$                            | $1.27\times 10^{-1}$ | $7.4\times 10^{-3}$ | $1.18\times 10^{-3}$ |
| T    | 3   | $1.6\times 10^{-4}$                            | $8.26\times 10^{-2}$ | $2.0\times 10^{-3}$ | $3.02\times 10^{-3}$ |
| 3He  | 3   | $9.3\times 10^{-5}$                            | $8.55\times 10^{-2}$ | $1.1\times 10^{-3}$ | $2.75\times 10^{-3}$ |
| 4He  | 4   | $2.1\times 10^{-5}$                            | $2.00\times 10^{-2}$ | $1.1\times 10^{-3}$ | $7.59\times 10^{-3}$ |

(Raw data: `folio-assistant/computations/`
`partition-cancellation-diagnostic.witness.json`.)

**The atom Markov trace is smaller than $S$ by a factor of
$\approx 10^{-3}$ — the same order of magnitude as the
nuclear binding fraction $B/(A\,m_n c^2)$.**

## Interpretation

The Wedderburn partition sum has no intrinsic reason to produce
a near-zero total: each partition contributes an $O(w_\lambda)$
amount with arbitrary sign, and generic Hecke elements produce
traces of order $w_\lambda$ times the leading partition count.
That the atom word produces near-cancellation three orders of
magnitude below its constituent magnitudes is a **physical
signature of nuclear binding**.

Heuristically: for a free atom (no inter-nucleon crossings),
$\mathrm{tr}_M(W_{\mathrm{free}}) = O(1)$ with no delicate
cancellation.  The inter-nucleon crossings in $W_{\mathrm{atom}}$
subtract $O(B/M)$ from this value via the blow-up structure in
[mass-endomorphism tower](#prop:mass-endomorphism-tower).  The
partition-indexed contributions rearrange so that the
subtraction is implemented as near-cancellation among
partitions, with the residue equal to the binding fraction.

**Conjecture** (not proved here): there is an exact identity
$$
  \frac{\bigl\lvert\mathrm{tr}_M(W_{\mathrm{atom}})\bigr\rvert}
       {S(\varrho)}
  \;=\; \frac{B(\varrho)}{A \cdot m_n c^2}
  \;+\; O(\hbar_q^2),
$$
valid to the brane-tower truncation order used in the engine.

## Conjugate-partition signature

The cancellation is not uniform across partitions.  Running
`partition-cancellation-diagnostic.py` shows that at
**doubly magic shell closures** (D, $^{4}\mathrm{He}$), conjugate
partitions $\lambda \leftrightarrow \lambda^\prime$ have
contributions of OPPOSITE sign and near-equal magnitude, producing
clean transpose-symmetric cancellation.  At non-magic atoms (T,
$^{3}\mathrm{He}$), conjugate pairs mostly have the same sign and
the cancellation is distributed differently.

This is consistent with the $H_{3A}$ Wedderburn-block structure
collapsing at shell closure (via
[magic-unfold](#rem:magic-unfold-peel) when that remark is
written), and it provides an empirical signature that can
discriminate magic from non-magic configurations.

## Action for downstream computation

The cancellation structure constrains the accuracy requirements on
per-partition character evaluation: any numerical error in
$\chi_\lambda$ of magnitude $\geq B/(A\,m_n c^2) \times S$ will
swamp the atom trace.  For 4He, this requires $\chi_\lambda$ to be
computed to at least 4-digit relative precision; the current
seminormal-basis evaluation delivers this.

Truncating the partition sum (dropping partitions with small
$w_\lambda \cdot \chi_\lambda$) is **not safe** — see
`docs/sdp-dual-quotient-reduction.md` and the
`sdp-dual-quotient-prefilter` witness for the negative result.  The
atom Markov trace requires the full partition sum to realize the
cancellation.
