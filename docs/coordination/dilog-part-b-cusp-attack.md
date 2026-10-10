# Coordination ledger — dilog Part-B cusp cancellation attack

**Goal.** Close (or reduce to a minimal named residual) the genuine Part-B wall of
`conj:dilogarithm-archimedean-limit`: the **uniform iπ-tower + linear-pole
cancellation across the cusp** yielding

$$
  \mathrm{reg}_n(x;q) \;\longrightarrow\; \mathrm{Li}_2(x) - \frac{\pi^2}{3}
  \qquad (q\to1^+,\ n\to\infty),
$$

where `reg_n` is the bare `(1−q)·log Φ_n(x;q)` with the exact per-factor
asymptotic `log(x qᵏ) + iπ` subtracted from every negative factor (`k > k*`,
`k* = log_q(1/x)`). Part A (`q→1⁻`) is CLOSED sorry-free (`archimedeanLimit_Ioo`,
merged #4157). Numerics + constant-identification: audit
`docs/audits/2026-07-17-dilog-archimedean-limit-partB-pole-cancellation.md`.

## The decomposition (what the wall actually is)

Using `clog_one_sub_pole_phase_split` (PR #4173, sorry-free): for a negative
factor `1 − x qᵏ` (`x qᵏ > 1`),

$$
  \mathrm{Log}(1 - x q^k) = \log(x q^k) + \log\!\big(1-(x q^k)^{-1}\big) + i\pi .
$$

Subtracting `log(x qᵏ) + iπ` (no free parameter) leaves `log(1-(x qᵏ)^{-1})`.
So (with `log Φ_n = −Σ_{k<n} log(1 − x qᵏ)`):

$$
  \mathrm{reg}_n = (1-q)\Big[\; -\!\!\sum_{k \le k_*}\!\log(1-x q^k)
     \;-\!\!\sum_{k_* < k < n}\!\log\!\big(1-(x q^k)^{-1}\big)\;\Big].
$$

The **iπ-tower cancellation is per-factor exact** (each negative factor's `+iπ`
is removed by the subtraction) — so `Im(reg_n) ≡ 0`. The **linear pole**
`log(x qᵏ)` is likewise removed per-factor by definition. The remaining content
is the convergence of the two **real** pieces:

| Piece | Sum | Limit | Vector | Status |
|---|---|---|---|---|
| **W-P1** positive factors `k ≤ k*` | `−(1−q)Σ_{k≤k*} log(1−x qᵏ)` | `Li₂(x) − π²/6` | V3 | open |
| **W-P2** regularized negative factors `k > k*` | `−(1−q)Σ_{k>k*} log(1−(x qᵏ)⁻¹)` | `−π²/6` | V1+V2 | **PROVED sorry-free (#4191)** |

Sum `= Li₂(x) − π²/3`. ✓

> **W-P2 CLOSED (2026-07-25, #4191).** The regularized negative-factor half is
> fully proved sorry-free in `DilogPartBEulerTail.lean`: the eta asymptotic
> `euler_tail_asymptotic` — `(1−p)·Σ'_m −log(1−p^{m+1}) → π²/6` as `p→1⁻`
> (`p = 1/q`) — assembled from V1 (`euler_tail_coeff_limit` + `_le` + `_nonneg`),
> V2b (`euler_tail_jseries_tendsto`, Tannery), and V2a
> (`euler_tail_lambert_rearrange`, nonneg Fubini). This is the classical
> Hardy–Ramanujan / Dedekind-eta limit `(1−p)log∏(1−pᵐ) → −π²/6`, previously
> absent from Mathlib and the corpus.

### W-P2 is the Euler-function / Dedekind-eta asymptotic

Substituting `m = k − k*` and `x q^{k*} = 1`: `(x qᵏ)⁻¹ = q^{−m}`. With
`p = 1/q ∈ (0,1)` (so `q→1⁺ ⟺ p→1⁻`), the piece is
`−(1−q)Σ_{m≥1} log(1 − pᵐ)`, and

$$
  \boxed{\;\lim_{p\to1^-}(1-p)\cdot\log\!\prod_{m\ge1}(1-p^m) \;=\; -\frac{\pi^2}{6}\;}
$$

— the **Euler-function / Dedekind-eta / Hardy–Ramanujan asymptotic**. This is a
genuine Mathlib gap (not present in Mathlib or the QOU corpus as of 2026-07-25).
It splits into:

- **V1 (cheap, LANDED sorry-free — #4191):** the two Tannery/DCT inputs for the
  Lambert `j`-series, `DilogPartBEulerTail.lean`:
  - `euler_tail_coeff_limit` — termwise `(1−p)pʲ/(1−pʲ) → 1/j`;
  - `euler_tail_coeff_le` + `euler_tail_coeff_nonneg` — uniform `0 ≤ · ≤ 1/j`
    (⇒ `·×(1/j)` dominated by summable `1/j²`).
- **V2 (medium):**
  - **V2b (heart, LANDED sorry-free — #4191):** `euler_tail_jseries_tendsto` —
    `Σⱼ (1/j)(1−p)pʲ/(1−pʲ) → Σⱼ 1/j² = π²/6` via Tannery
    (`tendsto_tsum_of_dominated_convergence`, arbitrary filter) + `hasSum_zeta_two`.
  - **V2a (remaining — the Lambert rearrangement):** for `p∈(0,1)`,
    `Σ'_m −log(1−p^{m+1}) = Σ'_j (1/(j+1))·p^{j+1}/(1−p^{j+1})`, a **nonneg Fubini**
    (`tsum_comm` / `summable_prod_of_nonneg`) on `a m j = p^{(m+1)(j+1)}/(j+1)`:
    - row: `Σ'_j a m j = −log(1−p^{m+1})` — reuse the corpus primitive
      `neg_log_one_sub_hasSum` (`DilogarithmArchimedeanLimit.lean:264`).
    - col: `Σ'_m a m j = (1/(j+1))·p^{j+1}/(1−p^{j+1})` — geometric shift
      `Σ'_m r^{m+1} = r/(1−r)`.
    - summability of the uncurried family from rows-summable + row-sums-summable
      (`Σ_m −log(1−p^{m+1})` summable, the one nontrivial bound).
    Combined with V2b this gives the eta asymptotic
    `(1−p)·Σ'_m −log(1−p^{m+1}) → π²/6`, i.e. `(1−p)·log ∏(1−pᵐ) → −π²/6`.

### W-P1 is the Part-A Riemann sum on the far side of the branch point

- **V3 (hard):** `−(1−q)Σ_{k≤k*} log(1−x qᵏ) → Li₂(x) − π²/6` for the `q>1`
  geometric partition in `u = qᵏ` running from `u=1` (k=0) **up to the branch
  point** `u = 1/x` (k=k*, where `x u = 1`). Reuse the Part-A integrand
  machinery in `DilogPartAConvergence.lean` (`integral_zero_one_eq_LiTwo`,
  `riemann_error_bound`, `tail_bound`, the convexity/monotonicity bricks) adapted
  to the `u>1` side with the integrable `log` singularity at the branch point.

### V4 (assembly)

Combine V1–V3 + `clog_one_sub_pole_phase_split` (#4173) into
`reg_n → Li₂(x) − π²/3`, with the uniform `q→1⁺ × n→∞` exchange.

## Discipline

Formalize-first; anti-fit (no constant is fitted — `π²/6 = ζ(2) = Li₂(1)` is the
theorem-forced dilog-inversion / Faddeev-`Φ_b` modular anomaly, audit §"Derivation").
Each vector lands sorry-free or honestly reduces to a minimal named residual. The
block stays `kind:conjecture` until V4 assembles the whole limit.

Beans: milestone `qou-icx5`; V1 `qou-sbfy`, V2 `qou-tt1l`, V3 `qou-jplv`,
V4 `qou-9m98`. Building block already landed: `qou-ips1` / #4173.

---

## 2026-07-25 — W-P1 status: fully assembled, reduced to one scalar limit

**W-P2 is CLOSED** (the Dedekind-eta asymptotic, #4191). **W-P1's entire
machinery is now landed sorry-free** in
`folio/quantum-observable-universe/lean/QOU/Archimedean/DilogPartBBranchPointSum.lean`:

| Brick | Lemma | PR |
|---|---|---|
| interior target integral | `integral_Icc_eq_LiTwo_sub` | #4210 |
| improper target limit | `tendsto_integral_x_to_c_nhdsWithin_one` (→ `π²/6 − Li₂(x)`) | #4210 |
| going-up convexity/monotonicity | `convexOn_neg_log_one_sub_mul_Icc`, `h_monotoneOn_Ioc` | #4215 |
| going-up per-cell squeeze | `h_integral_le_right_Icc`, `h_integral_ge_left_Icc` | #4219 |
| **going-up telescoping bound** | `riemann_error_bound_up` (majorant `qⁿ(q−1)(h(qⁿ)−h(1))`) | #4241 |
| log-sum = Riemann sum | `partialSum_up_eq` | #4247 |
| change of variables | `integral_one_to_c_eq_LiTwo_sub` | #4257 |
| error decomposition | `error_up_eq` | #4262 |
| **assembly** | `wp1_riemann_bound` | #4262 |

`wp1_riemann_bound` gives, for `1 < q`, `x·qⁿ < 1`:
`0 ≤ (Li₂(xqⁿ) − Li₂(x)) − (1−q)Σ_{k<n} log(1−xqᵏ) ≤ (q−1)(−log(1−xqⁿ)) − (q−1)qⁿ(−log(1−x))`.

As `q→1⁺` with `xqⁿ→1⁻`: `Li₂(xqⁿ)→π²/6` (brick 2 Abel), the
`(q−1)qⁿ(−log(1−x))` term `→0` (bounded × `q−1`). **So W-P1 → `Li₂(x) − π²/6`
iff the single scalar limit `(q−1)·log(1−xqⁿ) → 0`.**

### The residual: `(q−1)·log(1−xqⁿ) → 0` is non-uniform (NOT closeable as a brick)

This is the irreducible open input, and it does **not** admit a clean
unconditional proof:

- With `n = k*(q) = ⌊log_q(1/x)⌋` (the last positive factor), the endpoint sits
  against the branch point: `x·q^{k*} ∈ [1/q, 1)`, so `δ := 1−xq^{k*} ∈ (0,(q−1)/q]`.
  That is only an **upper** bound on `δ` (a *lower* bound on `−log δ`), never the
  **lower** bound on `δ` needed to force `(q−1)(−log δ)→0`.
- `δ` is governed by the **fractional part of `log_q(1/x)`**, which oscillates as
  `q→1⁺`. The limit is genuinely **conditional** — it holds under the Faddeev
  scaling (or a Diophantine no-resonance condition on `x`), not for every `q→1⁺`.
  This is the same analytic-number-theoretic subtlety the conjecture itself flags
  ("exact cancellation among algebraic poles before evaluating the principal
  branch").
- **Trivial sub-case (bulk):** if `x·qⁿ ≤ ρ < 1` (endpoint bounded away from the
  branch point) then `δ ≥ 1−ρ` and `(q−1)(−log δ)→0` immediately — proving the
  *bulk*, short of the branch point.

**A future proof needs the sequence-indexed Faddeev-scaling machinery** (joint
limits of the integer `nⱼ` and real `qⱼ`, with floor functions + equidistribution
of `frac(log_{qⱼ}(1/x))`), or a Diophantine hypothesis on `x`. That is genuine
research-level analytic number theory, not a Lean brick — do **not** fabricate a
one-liner (anti-laundering). The clean analytic seed to start from: `t·log t → 0`
as `t→0⁺`, applied once a lower bound `δ ≥ c(q−1)` is available from the scaling.

Bean `qou-jplv` carries this. V4 (`reg_n → Li₂(x) − π²/3`) then glues W-P1 + W-P2
(#4191) + the `clog_one_sub_pole_phase_split` per-factor split (#4173), and is
gated on this same scalar limit.

### Independent parallel confirmation + two sharpenings (2026-07-25, session `claude/keystone-vectors-2026-07-25`)

A fresh-context independent attack (branch `claude/keystone-vectors-2026-07-25`,
probe [`dilog_partb_wp1_residual_uniformity_probe.py`](../../computations/probes/dilog_partb_wp1_residual_uniformity_probe.py),
mpmath 50 dps) reproduces this exact wall — **two independent routes converge, which
strengthens the negative** — and sharpens it in two ways not previously recorded here:

1. **Explicit constructive counter-sequence (scope-(b) for the *unconditional pointwise*
   claim).** The residual is not merely "non-uniform / unproven": it *provably fails*
   along a named `q_m→1⁺` sequence. Pin `log(1/x)/log(q_m) = m + θ_m` with `θ_m = e^{−m}`;
   then `k*_m = m`, and `R(x; q_m, k*_m) = (q_m−1)·log(1−x q_m^{k*_m}) → −log(1/x) ≠ 0`
   (mechanism: `δ ≈ θ_m(q−1)`, `log δ ≈ −m`, `R ≈ (L/m)(−m) = −L`, `L = log(1/x)`;
   verified 50 dps). Taking `θ_m = e^{−cm}` steers the limit to a family of nonzero
   values. So the **unconditional** pointwise limit is a *proved* false statement (a
   witness sequence exists) — a scope-(b) obstruction, not a scope-(a) proof gap. The
   *conditional* (Faddeev-scaled / Diophantine no-resonance) limit stays scope-(a) open,
   exactly as recorded above.

2. **The conjecture's stated `n(1−q)→∞` hypothesis is orthogonal to the obstruction.**
   At the branch-point split index `n = k*(q)`, `k*·(q−1) → log(1/x) = const` (probe:
   1.204 across q = 1.1 … 1.0001), so `n(1−q) → ∞` is **never satisfied at k***; that
   hypothesis constrains the *global* cutoff `N` (the full W-P1+W-P2 window), not the
   interior split index whose obstruction is `frac(log_q 1/x)`. Consequence: the
   conjecture *as literally written* contains no hypothesis that pins the residual —
   closure requires **either** an added Diophantine/restricted-approach hypothesis on
   `q→1⁺`, **or** the **iterated-limit** reading (bulk `x qⁿ ≤ ρ < 1` first, giving
   `(q−1)Σ log(1−xqᵏ) → Li₂(x)−Li₂(ρ)` cleanly, then `ρ→1⁻` via the sorry-free Abel
   brick `tendsto_LiTwo_nhdsWithin_lt_one`), which needs **no** Diophantine input. The
   θ-averaged residual `→ 0` (Cesàro; bad set measure-zero), consistent with the
   equidistribution route flagged for V4.

No fabrication; the wall stands. This note only sharpens the *scope* (unconditional =
proved-false; conditional/iterated = the honest open target) and flags the
statement-level gap for whoever states V4's hypotheses. Probe not wired to production.

### Iterated-limit route CONFIRMED as the closeable W-P1 path (2026-07-26, branch `claude/dilog-partb-iterated-limit-2026-07-26`, PR #4343)

The iterated-limit reading flagged above is now **numerically confirmed sound**
(probe [`dilog_partb_iterated_limit_probe.py`](../../computations/probes/dilog_partb_iterated_limit_probe.py),
mpmath 30 dps, exit 0). Both stages converge monotonically **and** the sorry-free
`wp1_riemann_bound` (#4262) inequality is respected in every row:

- **INNER** (bulk, `q→1⁺`, `ρ` fixed in `(x,1)`, `n(q)=max{n: x qⁿ≤ρ}`):
  `−(1−q)·Σ_{k<n(q)} log(1−x qᵏ) → Li₂(x) − Li₂(ρ)`. The bulk cutoff `ρ<1` keeps
  the endpoint bounded away from `u=1/x`, so `−log(1−x qⁿ) ≤ −log(1−ρ)` is bounded
  and the `wp1_riemann_bound` majorant `→0`. **This is exactly where the Diophantine
  subtlety is avoided** — no no-resonance hypothesis is needed because `ρ` is fixed.
- **OUTER** (`ρ→1⁻`): `Li₂(x) − Li₂(ρ) → Li₂(x) − π²/6` via `tendsto_LiTwo_nhdsWithin_lt_one`
  (sorry-free). Converges sub-linearly (the `−log(1−ρ)` derivative singularity of `Li₂`
  at 1) — expected; the honest convergence witness is monotone decrease.

Combined iterated limit `= Li₂(x) − π²/6` = the W-P1 target; with W-P2 (#4191),
`reg_n → Li₂(x) − π²/3` under the iterated ordering.

**Epistemic status (STRICT).** The iterated limit is a **weaker** statement than the
joint limit. It does **not** contradict — and does not close — the joint claim, whose
unconditional form is proved-**false** (the resonant counter-sequence above). It is the
honest, Diophantine-free target for a Lean V4 assembly. The whoever-states-V4 owner
must decide whether the iterated ordering suffices for the physical keystone (a
statement-level modelling choice), OR whether the joint limit under an added Faddeev /
Diophantine hypothesis is required. **Lean brick for the INNER bulk-closure is in
progress on PR #4343** (reuses `wp1_riemann_bound` + `tendsto_LiTwo_nhdsWithin_lt_one`;
lands sorry-free or reduces to a minimal named residual — no fabrication).

### The limit ordering is NOT free — na-Stokes path-ordering selects the iterated limit (2026-07-26, owner insight; branch `claude/dilog-nastokes-curvature-2026-07-26`, beans qou-a0e9)

The "iterated vs joint" ambiguity (MQ1) that the iterated-limit closure (#4343) left as an
open *modelling* choice is **resolved on physical grounds by the framework's own derivation
chain** (`𝐂 → Yekutieli non-abelian Stokes → 𝐇_n(q)`). Owner insight (2026-07-26):

> "Limits need to follow na-Stokes, which I guess is path-ordered exponential."

**Mechanism.** The observable is a **holonomy** — a path-ordered exponential `𝒫exp(∫A)`,
realized via Yekutieli's non-abelian *multiplicative* surface integral (the framework's
`Yekutieli non-abelian Stokes` step; existing infra `def:yekutieli-triple`,
`prop:yekutieli-lifting`, the `brings-surface/` geometric-realization chapter). A
multiplicative integral is **defined** as an *ordered refinement* limit: refine the
lattice, take the **ordered** product of local exponentials, take the limit in that order.
It is intrinsically **iterated**, never a joint/symmetric limit — the ordering is
constitutive, not a gauge choice.

- The non-commutativity that *forces* the ordering lives at the **fibre / categorical**
  level (braid/Hecke `σ_i` don't commute; same fibre-vs-observable split as the
  `Im(q)` banner). The scalar partial product `Φ_n = ∏_{k<n}(1−xqᵏ)⁻¹` is the
  **archimedean shadow** (`τ`) of that path-ordered fibre holonomy.
- Refining the mesh (`q→1⁺`) over a sub-path first, then growing the path to the cusp
  (`ρ→1⁻`), **is exactly the INNER→OUTER order** of the #4343 closure
  (`wp1_bulk_tendsto` then `wp1_outer_tendsto`). The **joint** limit would scramble the
  path-ordering of a `𝒫exp` — not a legal operation on a holonomy. **MQ1's symmetry
  assumption was the error; a path-ordered exponential says the two limits are not
  interchangeable, and picks the iterated one.**

**Curvature route to MQ2/MQ3 (`−π²/3` = anomaly, not artifact).** In non-abelian Stokes,
the gap between the naive abelian `exp(∫F)` and the true **surface-ordered** integral is a
**curvature/area (commutator) term**. If `Φ_n` is the Yekutieli multiplicative integral,
the `−π²/3` shift is a candidate for *exactly* that non-abelian correction — a genuine
geometric quantity (consistent with the audit's `Φ_b` modular/framing anomaly), not a
regulator artifact. **Concrete lead:** `lem:yekutieli-leading-coefficient` (Ch 6,
`QOU.Archimedean.yekutieli_leading_coefficient`) already characterizes the Yekutieli
obstruction as the **leading Chebyshev coefficient** — so the curvature term may already
have a corpus handle; the MQ2/MQ3 target is to show that coefficient evaluates to `−π²/3`.

**What remains (honest — not asserted).** The na-Stokes argument *selects* the iterated
ordering at the level of principle. To *prove* it:
1. **(bean qou-zbcj)** identify `Φ_n(x;q)` explicitly as the Yekutieli multiplicative
   integral of the specific `𝐂`-connection, and check its refinement order is the
   `(ρ then q)` one used in #4343.
2. **(bean qou-tw5z)** compute the surface-ordering curvature/commutator term and verify
   it equals `−π²/3` (starting from `lem:yekutieli-leading-coefficient`).
3. **(bean qou-yczy)** numerical cross-check of the curvature decomposition.

Until (1)–(2) land, the iterated closure (#4343) stands as the honest *mathematical*
result and the na-Stokes selection stands as the *stated, principled* — but not yet
Lean-proved — resolution of MQ1. Anti-laundering: this is recorded as the direction and
scaffolded as a **conjecture**, not wired to production as proved.

### Joint-route conditional closure LANDED — second, independent Part-B total (2026-07-31, branch `claude/dilog-partB-joint-assembly-2026-07-31`, PR #4423)

The **joint** `(q,n)` W-P1 limit — the physically/mathematically genuine limit, *not* the
weaker iterated one — is now closed **conditionally on an explicit Diophantine no-resonance
bound** and assembled into the Part-B total, sorry-free:

| Brick | Lemma | File | PR |
|---|---|---|---|
| analytic seed `t·log t → 0` | `tendsto_mul_log_nhdsWithin_zero` | `DilogPartBBoundarySeed` | #4270 |
| conditional boundary limit | `boundary_term_vanishes` | `DilogPartBBoundarySeed` | #4270 |
| **joint W-P1** (`→ Li₂ x − π²/6` under no-resonance) | `tendsto_wp1_sum_of_no_resonance` | `DilogPartBWP1Capstone` | #4270 |
| W-P2 tail on the joint filter (`p=1/q`) | `tendsto_wp2_tail_of_q` | `DilogPartBJointAssembly` | #4423 |
| **joint Part-B total** (`→ Li₂ x − π²/3`) | `tendsto_partB_total_joint_of_no_resonance` | `DilogPartBJointAssembly` | #4423 |

`tendsto_partB_total_joint_of_no_resonance` gives: along any filter `l` with `q→1`,
`x·qⁿ→1⁻`, and `c(q−1) ≤ 1−x·qⁿ` (`c>0`), the combination
`(q−1)Σ_{k<n} log(1−xqᵏ) − (1−q⁻¹)Σ'_m(−log(1−q⁻ᵐ⁻¹)) → Li₂(x) − π²/3`. It assembles the
joint W-P1 capstone (#4270) with the W-P2 Euler tail (`euler_tail_asymptotic` composed along
`1/q → 1⁻`), subtracted exactly as `naStokes_physical_partB_value` combines its two ordered
pieces.

**Two independent conditional closures of the epic now coexist** — the *iterated* one
(`naStokes_physical_partB_value`, gated on the na-Stokes ordering conjecture) and the *joint*
one (`tendsto_partB_total_joint_of_no_resonance`, gated on the explicit Diophantine
no-resonance bound). Neither discharges its premise; the *unconditional* joint pointwise limit
remains proved-**false** along the resonant counter-sequence (2026-07-25 note above). The joint
route carries its hypothesis *explicitly* in the signature (no conjectural class), which is why
it needs no ordering conjecture. Honest scope per §"Conditional-proved ≠ premise-established".

### Faddeev-scaling POSITIVE — unconditional cusp-reaching W-P1 limit LANDED (2026-07-31, branch `claude/dilog-partB-faddeev-scaling-2026-07-31`)

The honest **positive** counterpart to the proved-false unconditional branch-index limit: an
explicit restricted (Faddeev) scaling that *reaches the branch point* yet satisfies the
no-resonance bound **by construction**, so the joint W-P1 limit holds **unconditionally along
it** — sorry-free, `wp1_faddeev_tendsto` (`DilogPartBFaddeevScaling.lean`).

**The scaling.** Take the *moving* interior target `ρ(q) := 2 − q → 1⁻` and the bulk floor
index `n(q) := nOfQ x q (2−q) = ⌊log((2−q)/x)/log q⌋` (largest `n` with `x·qⁿ ≤ 2−q`). Then:

- **no-resonance is automatic:** `x·qⁿ ≤ 2−q ⇒ 1 − x·qⁿ ≥ q − 1`, i.e. the bound with `c = 1`;
- **the cusp is reached:** `x·qⁿ ∈ ((2−q)/q, 2−q]` and `2−q → 1⁻`, so `x·qⁿ → 1⁻` (squeeze).

Feeding both to `tendsto_wp1_sum_of_no_resonance` (#4270) gives, with **no Diophantine
hypothesis**,

`(q−1)·Σ_{k<n(q)} log(1−x·qᵏ) ⟶ Li₂(x) − π²/6`   as `q → 1⁺`.

**Why this is stronger than the iterated route and consistent with the false unconditional
one.** Unlike `wp1_bulk_tendsto` (fixed `ρ`, needing a *second* `ρ→1⁻` iterated limit), this is
a **single joint** `q→1⁺` limit that already reaches the cusp. It does **not** contradict the
proved-false unconditional branch-index limit: that failure is *pointwise over all `q→1⁺` at the
resonant index* `⌊log_q(1/x)⌋`; here `n(q)` is a *specific* restricted approach chosen to avoid
resonance (back off by exactly one cell width). Existence of one convergent cusp-reaching
scaling is the concrete positive content the equidistribution / Faddeev programme targets.

**What remains (bean `qou-jplv`).** The *measure-theoretic* "**a.e.** approach converges"
statement — equidistribution of `frac(log_q 1/x)` / three-distance theorem — is the deeper
open residual; `wp1_faddeev_tendsto` exhibits a single good approach, not full-measure. Combined
with the W-P2 tail (`DilogPartBEulerTail` + the assembly of PR #4423), this scaling gives the
Part-B total `→ Li₂(x) − π²/3` unconditionally along the Faddeev approach.

### The a.e. residual — precise route + Mathlib tooling gap (2026-07-31 scoping)

The remaining open positive is: **for a.e. `x ∈ (0,1)`, the branch-index boundary term
`R(x,q) = (q−1)·log(1 − x·q^{k*(q)})` → 0 as `q→1⁺`** (`k*(q) = ⌊log_q(1/x)⌋`), hence the
*unconditional-index* W-P1 converges for a.e. `x`. Mathlib inventory (checked 2026-07-31):

- **AVAILABLE:** `MeasureTheory/OuterMeasure/BorelCantelli.lean` (Borel–Cantelli),
  `MeasureTheory/Function/ConvergenceInMeasure.lean`.
- **ABSENT:** real-number **equidistribution / Weyl criterion** for `frac(α n)` (the only
  `Weyl` in Mathlib is `LinearAlgebra/RootSystem/WeylGroup` — unrelated). So the classical
  *equidistribution* route is **not** wireable from Mathlib as-is; it would require building
  Weyl/three-distance from scratch (a genuine Mathlib contribution).

**Route that avoids equidistribution — Borel–Cantelli on resonance windows (tractable, multi-brick).**
`R(x,q) ↛ 0` requires `δ = 1−x q^{k*}` to be **exponentially** small (`log δ ~ −c/(q−1)`) —
from the counter-sequence analysis, `δ ≥ (q−1)^{1+ε}` fails only on a *resonance window*
`W_m(ε)` where `frac(log_q(1/x))` is within `~(q−1)^ε` of `0`. Along a discretizing sequence
`q_m→1⁺`, `measure(W_m) ≲ (q_m−1)^ε` is **summable** for a suitable schedule, so
`Borel–Cantelli` gives `x ∉ W_m` eventually a.e. — hence `δ_m ≥ (q_m−1)^{1+ε}`, the seed
`t·log t→0` (`DilogPartBBoundarySeed`) closes `R→0`, and `boundary_term_vanishes` +
`tendsto_wp1_sum_of_no_resonance` give a.e. convergence. **Bricks (bean `qou-jplv`):**
(1) define `W_m(ε)` measurably and bound `measure(W_m) ≲ (q_m−1)^ε`; (2) choose the schedule so
`Σ_m measure(W_m) < ∞`; (3) `Borel–Cantelli` ⇒ a.e. `x` in finitely many `W_m`; (4) glue to
`δ_m ≥ (q_m−1)^{1+ε}` and discharge via the seed. This is a research-grade multi-brick build,
not a single file; scoped here so the next attacker starts from the BC route, not the (absent)
Weyl one.

### Scope-(b) refutation LANDED — the unconditional branch-index limit is machine-checked FALSE (2026-07-31, branch `claude/dilog-partB-wp1-refutation-crux-2026-07-31`)

The 2026-07-25 numerical counter-sequence (`R(x;q_m,k*_m) → −log(1/x) ≠ 0`) is now a
**sorry-free Lean theorem** — upgrading the "proved-false" claim from a 50-dps probe to a
machine-checked obstruction (`DilogPartBWP1Refutation.lean`, `lean`-direct exit 0). This
proves the Diophantine no-resonance hypothesis of `tendsto_wp1_sum_of_no_resonance` (#4270) is
**necessary**, not merely convenient.

The witness: `q_m := exp(L/(m+e^{−m}))` (`L = log(1/x)`), `n_m := m`. Then `1 < q_m`,
`q_m → 1⁺`, `x·q_m^m = exp(−β_m) → 1⁻` (`β_m := L·e^{−m}/(m+e^{−m}) → 0`), and

`not_tendsto_boundary_zero`: `¬ Tendsto (fun m => (q_m−1)·log(1−x·q_m^m)) atTop (𝓝 0)`,

because `tendsto_boundary_refute`: `(q_m−1)·log(1−x·q_m^m) → log x ≠ 0`. The proof factors the
term as `[m·(q_m−1)]·[log(1−x q_m^m)/m]`: (A) `m·(q_m−1) → L` via the algebraic identity
`m·t_m = L − β_m` + the `add_one_le_exp` squeeze `t ≤ eᵗ−1 ≤ t·eᵗ`; (B) `log δ_m/m → −1` via the
endpoint identity `x q_m^m = e^{−β_m}`, the log squeeze `log β_m − β_m ≤ log δ_m ≤ log β_m`
(from `β e^{−β} ≤ 1−e^{−β} ≤ β`), and `log β_m/m = log L/m − 1 − log(m+e^{−m})/m → −1` (using
`Real.isLittleO_log_id_atTop`). Product `→ L·(−1) = −L = log x`, uniqueness of limits ⇒ `↛ 0`.

**This bounds what the a.e. route can hope for:** the pointwise-over-all-`q→1⁺` limit is
*provably* false, so only the *measure-theoretic* (a.e.-`x`, Borel–Cantelli) or *restricted-
scaling* (Faddeev, #4427) positives are attainable — exactly the two directions now recorded.

### BC a.e. build — deterministic bricks LANDED (2026-08-01, branch `claude/dilog-partB-bc-brick-spec-2026-07-31`)

The two `x`-pointwise (measure-free) bricks of the Borel–Cantelli programme are proved
sorry-free in `DilogPartBBorelCantelli.lean`, reducing the a.e. claim to a **pure Lebesgue
measure estimate**:

- `branch_endpoint_eq`: `x·q^{⌊s⌋} = exp((⌊s⌋−s)·log q)` with `s := log(1/x)/log q` — the
  branch-index endpoint identity, so the gap is governed by the resonance `frac s = s − ⌊s⌋`.
- `branch_gap_lower_of_fract`: **no-resonance ⇒ gap** — if `frac s ≥ θ` (`θ>0`) and `q∈(1,2]`,
  then `1 − x·q^{⌊s⌋} ≥ (θ/4)(q−1)`. This is *exactly* the `c·(q−1) ≤ 1−x·qⁿ` hypothesis that
  `boundary_term_vanishes` (#4270) consumes (`c = θ/4`), so `frac s` bounded below ⇒ the
  boundary term `→ 0`.

**What remains — the one measure brick (bean `qou-zuuz`).** Only the estimate
`measure{x ∈ (0,1) : frac(log(1/x)/log q_m) < ε_m} ≲ ε_m` (the resonance-window Lebesgue
bound), then Mathlib's `measure_limsup_eq_zero` (first Borel–Cantelli, present) gives a.e.
`frac` bounded below, and the two deterministic bricks above close a.e. convergence. That
window estimate is the genuine metric-number-theory residual (Mathlib lacks Weyl
equidistribution; the window bound is a direct change-of-variables `x = e^{−u}` + periodicity
argument, not Weyl). The deterministic reduction is now machine-checked — the a.e. positive is
one measurability+measure lemma away.

#### Correction (2026-07-26, same tranche): the curvature = −π²/3 route is REFUTED — −π²/3 is abelian dilog data, not a non-abelian anomaly

The "concrete lead" above (`lem:yekutieli-leading-coefficient` → the curvature term is
`−π²/3`) **does not hold up**. Investigated in
[`docs/audits/2026-07-26-nastokes-curvature-yekutieli-coefficient.md`](../audits/2026-07-26-nastokes-curvature-yekutieli-coefficient.md).
Findings:

- **`lem:yekutieli-leading-coefficient` = a discrete `H²` obstruction integer (`= 1`),**
  not a series/limit/transcendental (the leading coefficient of the monic genus-filtration
  Chebyshev basis; `monicCheb_monic` ⇒ `leadingChebyshev_eq_one`, sorry-free). No multiple
  of `1` is `−π²/3`. **`no-match`.**
- **`−π²/3 = −2·Li₂(1)` is an *abelian* dilog cusp value** — fully accounted for by two
  boundary `π²/6` terms already proved sorry-free (W-P1 Abel limit
  `tendsto_LiTwo_nhdsWithin_lt_one`; W-P2 `euler_tail_asymptotic`). It is **not** a
  commutator/curvature term: the corpus's own `holonomy_perm`
  (`YekutieliIntegration.lean`, sorry-free) proves the path-ordering defect **vanishes in a
  `CommMonoid`**, and `Φ_n = ∏(1−xqᵏ)⁻¹` is a product of commuting scalars (the τ-shadow).
  A genuine commutator would live at the non-commutative **fibre** level
  (`germ-commutator-q-curvature`), not in the scalar observable. Calling scalar `−π²/3` a
  non-abelian curvature is a category error. **`no-match`** (at best `numerical-coincidence`).

**What survives.** Only the **ordering selection** (MQ1: na-Stokes ⇒ iterated, not joint)
is defensible — `structural-partial`, corpus-supported (`holonomy` = ordered `List.prod`;
joint limit legal only in the abelian degeneration), but not yet Lean-proved that the
specific `Φ_n` is the Yekutieli MI of the specific `𝐂`-connection (bean qou-zbcj, still
open). That sound half — and *only* that half — is encoded in the new conditional class
`QOU.Archimedean.NaStokesPartBOrdering` (`DilogNaStokesOrdering.lean`, sorry-free,
lean-verify exit 0): its theorem derives the Part-B total `Li₂(x) − π²/3` from the two
proved bricks by uniqueness of limits, explicitly **not** claiming `−π²/3` is a curvature
term. Bean qou-tw5z (curvature route) → outcome `no-match`; qou-yczy (probe) → not needed
(the compute was symbolic/corpus).
