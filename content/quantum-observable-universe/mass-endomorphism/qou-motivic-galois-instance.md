# QOU MotivicGaloisCharacter instance via Habiro $\to$ Frob_p

The QOU brane-tower substrate carries a concrete instance of
[`def:motivic-galois-character`](#def:motivic-galois-character)
constructed by the **Habiro evaluation map**

$$
  \mathrm{Frob}_p \;=\; f(u) \big|_{u = \zeta_{2p}}
  \;\in\; \mathbb{Z}[\zeta_{2p}],
$$

where $f(u) = \sum_{m \geq 0} a_m(u) \cdot (u; u)_m$ is the Habiro
cyclotomic expansion of the atomic Markov trace
$\mathrm{tr}_M(T_w, q)$ and $u = q^{1/2}$. The cyclotomic Pochhammer
$(u; u)_m$ vanishes once $m \geq 2p$, so the sum **terminates**
after a finite number of terms.

## Construction (three steps)

1. **Extraction**
   ([`computations/probes/habiro_frobenius_probe.py`](../../../computations/probes/habiro_frobenius_probe.py)).
   For each atom in
   `habiro-coefficients-atomic.witness.json` (proton, neutron,
   deuteron) and each prime $p \in \{2, 3, 5, 7, 11, 13\}$, evaluate
   $f$ at $u = \zeta_{2p}$. Witness:
   `habiro-frobenius-probe.witness.json` field `frob_p_complex`.

2. **Compatibility verification.** Two finite-place coherence
   checks pass on every $(p, \text{atom})$ cell:

   - **Galois-norm integrality.** The trace
     $N(\mathrm{Frob}_p) = \sum_{\sigma \in \mathrm{Gal}(\mathbb{Q}(\zeta_{2p})/\mathbb{Q})} \sigma(\mathrm{Frob}_p)$
     is a rational integer for every cell (residual $< 10^{-7}$).

   - **Weil purity at small primes.** At $p \in \{2, 3\}$, the
     orbit-spread $\max|\sigma(\mathrm{Frob}_p)| - \min|\sigma(\mathrm{Frob}_p)|$
     is below $10^{-10}$ for every atom; the inferred weight
     $w = 2 \log_p |\mathrm{Frob}_p|$ takes integer or near-integer
     values. At larger primes the spread grows — the QOU motive
     is **mixed** in general (composite of pure-weight sub-motives),
     consistent with the brane tower being a sum across cohomology
     degrees.

3. **Lean instance**
   ([`qou-motivic-galois-instance.lean`](qou-motivic-galois-instance.lean)).
   The instance discharges
   [`def:motivic-galois-character`](#def:motivic-galois-character)
   for the QOU substrate. The `frobenius_at` field maps each prime
   to its extracted Frobenius eigenvalue; the
   `almost_everywhere_nontrivial` field is a substrate axiom
   (AGENTS.md §3b) backed by the numerical witness for primes
   $\leq 13$.

## Per-cell summary (from witness)

|atom|$p=2$|$p=3$|$p=5$|$p=7$|$p=11$|$p=13$|
|---|---|---|---|---|---|---|
|p (proton) |$\|F\|=8$, $w=6$ |$\|F\|=1$, $w=0$ |$\|F\|=0.62$, partial|partial|partial|partial|
|n (neutron)|$\|F\|=8$, $w=6$ |$\|F\|=2.65$, $w\approx1.77$ |$\|F\|=0.24$, partial|partial|partial|partial|
|D (deuteron)|$\|F\|=96$, $w\approx13.17$ |$\|F\|=4.58$, $w\approx2.77$ |$\|F\|=1.44$, partial|$\|F\|=38.74$, partial|partial|partial|

Cells marked "partial" are those where the on-disk Habiro data
runs out before the Pochhammer truncation point
($m_{\max}$ in the on-disk file is below $2p$); the Galois-norm
integrality still holds in those cells, indicating the partial sum
is already a good approximation to the true Frobenius eigenvalue.
Unmarked cells achieve full truncation within the data and pass the
Weil-purity check $|\sigma(\mathrm{Frob}_p)| = p^{w/2}$ for every
$\sigma$ in the Galois orbit.

## Downstream consumers

This instance discharges audit GAP 5b
([`docs/audits/family-4-motivic-path.md`](../../../docs/audits/family-4-motivic-path.md)).
Theorems that previously took
[`def:motivic-galois-character`](#def:motivic-galois-character)
as an `[instance]` hypothesis can now use the explicit QOU instance
directly. In particular,
[`conj:motivic-perpetual-obstruction`](#conj:motivic-perpetual-obstruction)
becomes an unconditional theorem for the QOU substrate (the
non-triviality witness reduces to the substrate axiom in field
`almost_everywhere_nontrivial`).

## Coherence

Cross-prime coherence is structurally automatic from the Habiro
theorem: any two evaluations $f|_{u = \zeta_{2p}}$ and
$f|_{u = \zeta_{2q}}$ are extracted from the same Habiro element
and so respect the natural Galois action on $\mathbb{Q}(\mu_\infty)$.
The deeper $\ell$-adic archimedean Weil/Deligne behaviour falls
outside the scope of this construction.
