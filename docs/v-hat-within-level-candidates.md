# V̂ within-a-level improvement candidates

This note enumerates candidate structural improvements to the
per-jet-level aggregated volume $\hat V$ used in the brane-tower
pipeline.  The session identified this axis as the only remaining
structural lever for reaching the 1-ppm mass target
(`docs/mass-1ppm-workplan.md`): Kähler orders diverge on
T/3He, the jet-scaling loop is saturated at level 3, and pair-form
swaps (content-weighted, per-nucleon SDP gluon) either over-correct
or fail to transfer.

All current pipelines compute a scalar $\hat V_i$ per H_n(q)
generator $\sigma_i$, weighted by the Plancherel measure
$w_\lambda = d_q(\lambda)^2 / [n]_q!$ and summed against the braid
word's character.  The session's negative results can be traced to
this scalar-per-generator collapse: two sources of correlation
structure (Kähler q-derivatives and SYT-content weights) cannot
coexist under the current single-level formula because the scalar
path double-counts.

## Candidate 1 — Per-SYT content-weighted $\hat V$, single-gen

**Status.** Implemented as the JM cell tower in
`computations/syt_cell_tower.py`
(`Track 1`).  Tested only under proton-calibrated $E_0$, no Kähler;
gives D / T / 3He = 0.10 / 0.28 / 0.22 %.  Untested under
production (β-decay $E_0$ + Kähler + $\hbar_q^2$).

**Risk.** Same over-correction pattern as content-weighted pair
under production — the JM content $q^{2 c_T(k)}$ weights and
Kähler q-derivatives likely capture overlapping structure.

**Action.** Wire `syt_cell_tower` into `unified_lift.binding_unified`
using the JM cells for the single-gen term, at `kahler_order=0`.
Compare against scalar-under-production baseline on D / T / 3He.
~30 min, small modification.

## Candidate 2 — Gram-projected $\hat V$

**Idea.** The 6×6 Gram $G$ has a negative eigenvalue at $q_0$ (see
`docs/ilp-sdp-audit.md`).  Project $\hat V$ onto the positive
subspace $G^+ = \sum_{\lambda_i > 0} \lambda_i v_i v_i^T$ before
feeding to $\Phi_q$.  This enforces quadratic Frobenius positivity
on the per-level $\hat V$ itself, which the current scalar sum
cannot guarantee.

**Risk.** Projection discards information — especially at
$q_0 = 1.11$ where one eigenvalue is negative with significant
magnitude ($-0.74$).  Might make D worse while helping T/3He, or
vice versa.

**Action.** Single line change in `canonical_plus_multibrane.py`:
`V_hat_i → G_plus @ G_plus_pseudoinv @ V_hat_i`.  Re-run the
unified-lift tower and compare.  ~1 hour.

## Candidate 3 — Mixed scalar/content pair with scale factor

**Idea.** The failed `binding_full_content_pair` probe showed
content-weighted $V̂_{ij}$ over-corrects by 5–500× under
production calibration.  If the over-correction is homogeneous —
i.e., content pair = (scale factor) × scalar pair — a single
scale-factor fit recovers the scalar path.  If not, the ratio
varies by pair and reveals where SYT correlations actually
matter.

**Action.** Read `content-weighted-pair-probe.witness.json` and
`binding-full-content-pair.witness.json`, compute
$r_{ij} := V̂_{ij}^{\mathrm{content}} / (V̂_i \cdot V̂_j)$ for
every pair, plot the distribution, check dispersion.  ~20 min,
research-only.

## Candidate 4 — Ocneanu / Jones–Wenzl weight, with ω_λ sum=1

**Idea.** Use the canonical Jones–Markov weight
$\omega_\lambda(q, z) = z^{n-1} \prod_x (1 - z q^{2c(x)}) /
(1 - q^{2 h(x)})$ in place of the Plancherel weight
$w_\lambda$.  This *would* satisfy the Markov axioms exactly
at $q \neq 1$ (unlike Plancherel), and matches the canonical
`tr_M_element` used in `binding_canonical.py`.

**Why user flagged "not JW"**: earlier session data showed the
Plancherel sum has Σ $w_\lambda \approx 0.99$ at $q_0$ for D —
close to 1 by accident of the small-n partition count.  The
Jones–Wenzl sum at the same $q_0$ gives ≈ 0.09 — very far from
1.  So naive JW is worse than Plancherel here.  A re-normalised
JW might differ; user preference is to keep Plancherel.

**Status.** Research-locked as "keep Plancherel" per session.
Revisit only if Candidates 1–3 all fail.

## Candidate 5 — Covariant V̂ (keep partition index)

**Idea.** Don't collapse to a scalar $\hat V_i$.  Carry the full
partition-indexed vector $\hat V_i^\lambda$ through to $\Phi_q$
and sum outer.  Each $\hat V_i^\lambda$ is a character value
weighted only by $1/d_\lambda$, not by $w_\lambda$.  Then
$\Phi_q$ acts on the partition-indexed tensor, and the Plancherel
average is deferred to the outermost sum.  This defers averaging
past the non-linearity of $\Phi_q$, which is where the Kähler
vs content-weighted double-counting occurs.

**Risk.** $\Phi_q$ on a partition-indexed vector is not
well-defined — $\Phi_q$ takes scalar arguments.  Would need to
either (a) define $\Phi_q$ per irrep (via the representation's
spectral coordinate) or (b) evaluate $\Phi_q$ pointwise on the
diagonal entries of each partition's matrix, which is a much
larger computation.

**Action.** Research: write out the Ω¹-jet-up action on
$\hat V^\lambda$ (per-irrep) explicitly and check if the
Plancherel average commutes with the $\Phi_q$ sum, or if the
two mis-commute in a way that produces a correction term.

## Candidate 6 — Full-atom SDP gluon (P2.1b)

**Status.** Parked for separate fork per user.  Expected ~1 MeV
gain on D from removing the uniform 2·σ_0 gluon assumption.  This
is the only candidate with a clear ~1 MeV prediction of gain; all
others are speculative.

## Recommended order

1. **Candidate 3** (20 min, research) — reveals whether the
   content/scalar ratio is uniform or structured.  Informs which
   of 1–5 is most likely to close the residual.
2. **Candidate 1** (30 min, implement) — wire JM cells into
   production, test.  If it over-corrects like content-pair did,
   matches the pattern and confirms Candidate 2 / 5 are needed.
3. **Candidate 2** (1 hour) — Gram-projection is a cheap single-
   line fix; if it closes the residual on any atom, that's
   decisive evidence for the PSD-cone origin of the error.
4. **Candidate 5** (research, open-ended) — last resort if 1–3
   fail.  Reformulates the pipeline to defer the Plancherel sum.
5. **Candidate 6** (separate fork) — highest expected gain (~1
   MeV on D) but largest engineering cost.

## Closed levers (for reference)

| Lever | Result |
|-------|--------|
| Kähler arbitrary-order | Diverges on T/3He |
| Jet-scaling extra levels | Saturated at level 3 |
| Content-weighted pair (production) | Over-corrects 5–500× |
| Per-nucleon H_3 SDP gluon | No atom-level transfer |
| Jones–Wenzl weight at q_0 | Sum ≠ 1 — naively worse than Plancherel |
