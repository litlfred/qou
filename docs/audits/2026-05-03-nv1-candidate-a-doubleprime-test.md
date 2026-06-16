# NV-1 candidate (a″) test — q-deformed Plancherel sum

**Date:** 2026-05-03
**Branch:** `claude/audit-math-framework-FXlp2`
**Source conjecture:**
[`docs/audits/2026-05-02-nv-frob-filter-conjectures.md`](2026-05-02-nv-frob-filter-conjectures.md),
lines 129–159 (Refinement (a″), open candidate).
**Witness:**
[`computations/nv1_candidate_a_doubleprime.witness.json`](../../computations/nv1_candidate_a_doubleprime.witness.json)
**Script:**
[`computations/nv1_candidate_a_doubleprime.py`](../../computations/nv1_candidate_a_doubleprime.py)
**Verdict:** **fail** (q-deformed Plancherel sum falsified).

---

## 1. Conjecture statement

Per the source audit document (lines 141–148):

> *$N_v$ is a $q$-deformed Plancherel sum at $q_0$ rather than the
> classical sum:*
> $$\widetilde{N_v} = \sum_{\lambda \vdash 9} \dim_q V_\lambda \cdot f_\lambda \;\Big|_{q = q_0}.$$
> *The classical limit ($q \to 1$) gives $\sum f_\lambda^2 = k_w!$;
> at $q_0$ the value shifts by an $\mathcal{O}(\hbar_q^2) \approx 1\%$
> correction. This is the strongest remaining candidate.*

**Comparison target:** $N_v = 1{,}445{,}519$ (back-solved from
CODATA $G_F$); pass criterion is agreement to relative precision
$\sim 5 \times 10^{-7}$.

The motivating numerology: $N_v / 9! \approx 3.98346$, *near* but
not 4. Conjecture (a′) of $N_v = 4 \cdot 9! = 1{,}451{,}520$ is
falsified by 0.41% (rel. dev. $4.15 \times 10^{-3}$). Candidate
(a″) asks whether the $q$-deformation of the symmetric-group
Plancherel sum absorbs that 0.41% gap.

## 2. Method

All arithmetic at `mpmath.mp.dps = 50`. Steps:

1. Enumerate all 30 partitions $\lambda \vdash 9$.
2. Compute classical Specht dimension $f_\lambda$ via the standard
   hook-length formula $f_\lambda = n! / \prod_{x \in \lambda} h_x$.
3. Compute the $q$-Hecke-representation dimension via the
   $q$-hook formula
   $\dim_q V_\lambda = [n]_q! / \prod_{x \in \lambda} [h_x]_q$
   at $q_0 = 1.10997859555418057528159407961\ldots$ (50 dps).
4. Sum $\widetilde{N_v} = \sum_\lambda \dim_q V_\lambda \cdot
   f_\lambda$.
5. Cross-check: at $q \to 1$ the formula reduces to
   $\sum f_\lambda^2 = 9! = 362{,}880$ (verified to integer
   equality).
6. Variants tested (only when principal sum disagrees):
   (a) $\sum_\lambda (\dim_q V_\lambda)^2$;
   (b) self-conjugate-only restriction $\sum_{\lambda = \lambda'}
   \dim_q V_\lambda \cdot f_\lambda$;
   (c) descent-involution residual $\delta_w = N_v -
   \widetilde{N_v}$ (no canonical formula in the source doc, so
   only the size of the gap is reported).

The script does not reuse any existing `dim_q` module — the
$q$-hook formula is implemented inline, per the task constraint.

## 3. Results

### Sanity check — classical limit

$$\sum_{\lambda \vdash 9} f_\lambda^2 = 362{,}880 = 9!$$

Verified to exact integer equality (witness:
`classical_limit_check.ok = true`).

### Principal candidate (a″)

| Quantity | Value |
|----------|-------|
| $\widetilde{N_v}(q_0) = \sum_\lambda \dim_q V_\lambda \cdot f_\lambda$ | $\mathbf{488{,}814.852553}\ldots$ |
| $N_v$ target | $1{,}445{,}519$ |
| $\widetilde{N_v}(q_0) / N_v$ | $0.338159\ldots$ |
| Relative deviation $(\widetilde{N_v}-N_v)/N_v$ | $-6.62 \times 10^{-1}$ |
| Required precision (CODATA $G_F$) | $5 \times 10^{-7}$ |

Discrepancy is $\approx 1.3 \times 10^6$ times the required
precision. The $q$-deformation does **not** absorb the 0.4% gap;
in fact it makes the comparison vastly worse, because at $q_0$
each $\dim_q V_\lambda$ is **larger** than $f_\lambda$ by
$\mathcal{O}(\hbar_q^2)$ but the principal sum
$\sum \dim_q V_\lambda \cdot f_\lambda$ at $q = 1$ already equals
exactly $9! = 362{,}880$ — so its $q$-deformed value is on the
order of $9! \cdot (1 + \mathcal{O}(\hbar_q^2)) \approx 5 \times
10^5$, nowhere near $N_v \approx 1.4 \times 10^6$. The candidate
is roughly **1/4 of $N_v$**, not within an $\hbar_q^2$
neighbourhood.

### Variants (also fail)

| Variant | Value | Rel. deviation from $N_v$ |
|---------|-------|---------------------------|
| (a) $\sum_\lambda (\dim_q V_\lambda)^2$ | $658{,}784.267\ldots$ | $-5.44 \times 10^{-1}$ |
| (b) Self-conjugate only ($\lambda = \lambda'$, 8 partitions) | $8{,}808.057\ldots$ | $-9.94 \times 10^{-1}$ |
| (c) $\delta_w = N_v - \widetilde{N_v}$ residual | $956{,}704.147\ldots$ | $\delta_w / 7! \approx 189.82$ — no clean structure |

None of (a), (b), (c) close the gap. Variant (a) is also off by
order unity. Variant (c) does not produce a recognisable
small-integer residual (the audit's hint
$\delta_w \approx 7! \cdot 1.19$ would require a starting
candidate near $4 \cdot 9!$, not $\widetilde{N_v}$, so the
descent-involution heuristic was attached to candidate (a′), not
(a″).)

## 4. Verdict

**Candidate (a″) — q-deformed Plancherel sum hypothesis —
is falsified.**

- Numerical disagreement is at the $66\%$ level, $\sim 10^6 \times$
  the CODATA-$G_F$ tolerance.
- The $q$-deformation cannot be the closure mechanism for the
  $N_v / 9! \approx 3.98346$ "near 4" numerology, because the
  classical $\sum f_\lambda^2$ already equals $9!$ exactly and the
  $q$-deformed sum is not even on the right order of magnitude
  to reach $\sim 4 \cdot 9!$.

The structural reason: $\widetilde{N_v}(q_0) \approx 1.347 \cdot
9!$. So the $\hbar_q^2$ correction shifts the Plancherel sum by
$\sim 35\%$ — far larger than the 0.4% gap audit (a″) was hoping
to absorb, and in the wrong direction (too small by a factor of
roughly 3, not 1.004 vs. 1.000). The conjecture's error estimate
of "$\mathcal{O}(\hbar_q^2) \approx 1\%$" assumed $\hbar_q^2$
multiplied a sum that was already near $4 \cdot 9!$; the actual
classical sum $\sum f_\lambda^2 = 9!$ is a different reference
point, and a 35% shift of $9!$ does not pass through $4 \cdot 9!$.

## 5. Residual structure & follow-on

### What we know after this test

1. $N_v = 1{,}445{,}519$ remains **prime** and is not equal to
   $\sum_\lambda \dim_q V_\lambda \cdot f_\lambda$ at level 9 for
   any of the three principal Plancherel-flavoured Ansätze.
2. Per the source audit doc, $4 \cdot 9!$ is falsified at $4.15
   \times 10^{-3}$ relative deviation, and $\widetilde{N_v}$
   above is falsified at $-6.62 \times 10^{-1}$ — neither the
   classical "4·9!" nor its $q$-deformation works.
3. The classical-limit check
   $\sum f_\lambda^2 = 9!$ is **exact** to integer equality at
   our 50-dps precision, so the implementation of the q-hook
   formula and the partition enumeration are correct (a wrong
   formula would have failed the classical-limit check).

### Recommended follow-on

Per the source audit doc (lines 161–179), the documented
fallback is **candidate (b) — `conj:nv-as-bring-period-rank`**:

> *$N_v$ equals the rank of the distinguished
> $S_5 \times \langle \hat \tau \rangle$-stable period
> sub-lattice on Bring's surface at the weak-place projection
> $\rho_{\rm weak}\colon \widehat{\mathcal{M}} \to
> \mathbb{Z}[q]/\Phi_{p_w^{k_w}}(q)$.*

Candidate (b) is research-grade (requires the Bring-surface
period-lattice machinery currently open under
`conj:magic-numbers-bring`). With (a) and (a′) and (a″) all
falsified, it is the next live conjecture for the $N_v$
identification. Possible additional cheap probes before paying
the Bring-period cost:

- Test whether $N_v$ matches a **Hecke trace** at level 9 with
  a non-trivial element (rather than the identity / Plancherel
  weight) — i.e. $\mathrm{tr}_M(\beta)$ for a distinguished
  braid $\beta \in B_9$ (e.g. the full twist).
- Test whether $N_v$ is a **dimension of a specific block**
  (e.g. the dimension of the $H_9(q_0)$ regular representation
  decomposed by central character, summed only over the weak
  sector blocks).
- Test the level-9 **Schur–Weyl mass-counting variant**
  $\sum_\lambda \dim_q V_\lambda \cdot s_\lambda(\mathbf{1})$
  where $s_\lambda$ is the Schur polynomial evaluated at a
  designated point — variants in `schur_weyl_q_hecke_v2.py` may
  already cover this.

These "cheap" probes can be run with the same machinery (mpmath
+ partitions of 9) and would either narrow the search or
reinforce the case for jumping straight to (b).

## 6. Files

- Script:
  [`computations/nv1_candidate_a_doubleprime.py`](../../computations/nv1_candidate_a_doubleprime.py)
- Witness:
  [`computations/nv1_candidate_a_doubleprime.witness.json`](../../computations/nv1_candidate_a_doubleprime.witness.json)
- Source conjecture:
  [`docs/audits/2026-05-02-nv-frob-filter-conjectures.md`](2026-05-02-nv-frob-filter-conjectures.md)
