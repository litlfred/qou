# Week-review + prioritized workplan — 2026-08-08

**Scope.** A survey of what landed on `main` since 2026-08-02, the current
1ppq / L2 state, a prioritized next-actions plan, a call on the two
non-landed stragglers (#4617 / #4619), and an honest outside-view
assessment. This is a **review + planning** document — no derivation is
attempted here, nothing is wired, no fit is performed.

**Volume.** ~1180 commits landed on `main` 2026-08-02 → 2026-08-08. The
overwhelming majority are Lean hygiene, wall-side §7c base-ring ports,
audit docs, and bean bookkeeping. The 1ppq needle did **not** move: L2 is
still **2/7**.

---

## (a) What landed this week — themes, and what each CLOSED vs OPENED

### Cluster 1 — Δ_λ value PROVED (the one genuine structural advance)

The single most important landing of the week. The per-partition binding
**value** is now sorry-free, general-n:

> `Δ_λ = (−1)^{n(λ)}·dim V_λ` (signed Springer dimension) —
> `QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional` (#4580),
> with the arc #4553 → #4574 / #4581 / #4586.

- **CLOSED:** the per-partition *value* leg (sign = jet-order valuation
  parity; magnitude = Wedderburn dimension; both substrate-derived). Beans
  `qou-f0ny`, `qou-r0xk`, `qou-dr7h` closeable.
- **OPENED / clarified:** the framing correction that governs everything
  downstream — the six-ansätze failure was **never** about the value. It
  is about the **many-body binding MAGNITUDE** (`r* ≈ 1.585`, the deuteron
  `C_knot` deficit), which the value proof does **not** touch. Two proved
  brackets now pin the missing object: it is **additive, extensive, and
  irreducibly ≥3-body** (intensive-vs-extensive proof + pairwise cap
  `ρ_A ≤ C(A,2)` = `exchangeDet_pow_two_le_four`).
- Full framing: [`docs/audits/2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md`](../audits/2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md).

### Cluster 2 — the deuteron / Δ_λ magnitude convergence (2026-08-02)

The deuteron-magnitude front converged this week onto a single surviving
object. Three sorry-free landings closed the scalar/surface routes:

- **Scalar trefoil channel is Lean-proved NULL** — `TrefoilSurfaceStateSum.lean`
  (on main, `computations/deltalambda/`): H₂(q) (2-strand, one generator)
  is **commutative**, so every commutator vanishes (`commutator_zero`). The
  σ₁³ handle-commutator / surface-curvature channel is null **by
  abelianness**, q₀-independent. scope-(b).
- **b₄ multiplicative cumulant** (Option-E front 4) reaches only **6.3 %**
  of the ⁴He target — scope-(a) undershoot, 0-fit, sorry-free
  (`B4MultiplicativeCumulant.lean`).
- **T₃ writhe-sign vs Δ_λ chirality** (#4623) — derived weak-isospin
  writhe sign tested against the mixed-sign requirement; honest partial.
- **CLOSED:** the σ₁³-trefoil-surface and scalar-invariant routes to the
  deuteron magnitude (proved null / undershoot). The surviving object is
  now precisely named (beans `qou-u8w5`, `qou-prjo`, `qou-i4pz`): an
  **eigenphase-weighted per-block handle-commutator charge on the
  NON-abelian H₆ interface braid** (H₆ is non-commutative ⇒ commutators
  non-zero; naturally mixed-sign, matching the PROBE-4 chirality
  requirement KL-positivity cannot supply) — plus the fibre→archimedean
  τ-transfer.
- **Standing caveat (do not lose):** the deuteron is *separately* closed
  to ~0.036 % via fibre-level tiers, so `C_knot = 5.853` is **likely a
  master-formula normalization artifact**, and the honest resolution may
  be the fibre→τ-transfer rather than any new surface term. Weigh this
  before investing in the H₆-charge construction.

### Cluster 3 — the L1 ℓ¹-ceiling result (hardens the "magnitude absent" claim)

[`2026-08-07-l1-ceiling-confirms-magnitude-absent-and-he4-two-row-suppression.md`](../audits/2026-08-07-l1-ceiling-confirms-magnitude-absent-and-he4-two-row-suppression.md),
0-fit, 50-dps witnesses:

- **CLOSED (scope-a, firmly):** the entire *"find a better Δ_λ"* family.
  The ℓ¹ norm `Σ|y_λ χ^λ Δ_λ|` reaches at most **36–59 %** of the AME
  target for all four of D/T/³He/⁴He — so **no re-signing, no
  re-weighting, no Δ_λ re-derivation** can close the deficit. The missing
  object must be **additive and new**, and must supply 41–64 % of each
  target on its own.
- **OPENED (suggestive, unverified):** ⁴He's two-row sector is suppressed
  **~29,000×** at the doubly-magic, unique Wigner-SU(4) `[1⁴]` nucleus —
  an approximate cancellation (not an exact selection rule; residual
  10⁻⁴ against 50-dps inputs), worth a q-sweep to test for an exact zero
  at q ≠ q₀.

### Cluster 4 — the μ₃ submodularity door (consolidated 2026-08-07)

[`2026-08-07-mu3-door-status-consolidated.md`](../audits/2026-08-07-mu3-door-status-consolidated.md)
consolidates #4404 → #4651 / #4657 / #4662:

- **CLOSED (scope-b):** the per-block multiplicatively-damped operator
  class cannot supply submodularity (pair term `Δ² ≥ 0`; survives the
  GAP-7 slot correction). `sign(y_λ) = (−1)^{P(λ)}` proved a
  content-threshold **depth** parity (not part-count) — machine-verified
  on all 270 partitions n=2..12 (`YLambdaSignThreshold.wenzl_sign`).
- **OPEN, not refuted:** the mixed-sign-weight escape is live but the
  quantitative budget is **~40× short** (negative-weight mass 1.31 % at
  n=9). Two residual holes: `sign(Z)` not derived; class membership of the
  H₉ `|χ|` traces not established.
- **Convention flag (owner call, deliberately unresolved):** the μ₃ arc
  runs on the **non-cyclic perblock** `Σ y_λ|χ_λ|`, while the corpus
  canonical is the **signed cyclic** Jones–Markov trace. Door closed both
  ways (~5–8 % apart), but *which* `cl₃` is canonical is unsettled
  (−1.7688 vs −1.6325 for T). Renamed `c₃ → cl₃` to disambiguate from the
  Q_β precision-ladder coefficient.

### Cluster 5 — Q_β / c₃ front (no movement; one dead-code fix; one lead)

[`2026-08-08-qbeta-l2-assessment-post-week-landings.md`](../audits/2026-08-08-qbeta-l2-assessment-post-week-landings.md):

- **Nothing closed Q_β.** The full **1248 ppb** residual is still the c₃
  truncation; c₃ remains `cal-anchored` (extracted from Q_codata, refused
  by the dashboard). Q_β drives **3 of 5** L2 misses (trio identity).
- **One compute defect fixed:** the c_k tier auto-promotion in
  `per_observable_100x_status.py::load_witness` was **dead code** (flat
  path resolution missed the `qbeta/` subdir). Mechanism fix, numeric
  no-op today.
- **New hard constraint:** the proton/muon anchor swing on Q_β is
  **29.96 ppb = 3.8× the L2 target** — so even a derived c₃ is
  **necessary but not sufficient**; the anchor layer must also be settled.
- **One genuine lead (untested):** this week's `CocenterTraceFactor.lean`
  + `OuterDerivationResidue.lean` + `hh1_hecke_outer_derivations.py`
  land on the *same address* as the surviving fibre-level c₃ carrier —
  the outer/cocenter part survives the Markov trace and exists exactly at
  roots of unity. Falsifiable next step: `dim HH¹(H₅(ζ₅))` at the Bring
  root of unity + bar-parity test (bean `qou-jcmw`, nobody on it).

### Cluster 6 — the c₃ / S_leak RETRACTION (a live cautionary landing)

The `c3-odd-aomega-unification` / `S_leak := c₃ + Vol(4₁)` filter was
**retracted** (PR #4724): the `−Vol(4₁)` "bar-even part of c₃"
identification was **not derived**, and the sign-flip it exploited is
produced by *any* offset in a window of width 0.049. Produced the new
STRICT rule **"Defined residual ≠ derived decomposition"** in AGENTS.md.
Net for the week: this arc **opened nothing and closed nothing** — it
consumed effort and ended in a retraction plus a discipline rule.
[`2026-08-08-hh1-outer-class-bar-parity-prune-does-not-exist.md`](../audits/2026-08-08-hh1-outer-class-bar-parity-prune-does-not-exist.md).

### Cluster 7 — SM / eightfold-way (no L2 leverage; honesty passes)

Substantial eightfold-way authoring + several honesty passes. Net verdict
of the week's own accounting: **the eightfold layer has no L2 leverage**
(ledger row C20), and the A2 "flavor N=3" premise for binding is
**refuted** — the framework gives `N = 2`, and `N = 2` provably cannot
host the octet (`dim V_{(1³)} = C(N,3) = 0`, sorry-free, Schur–Weyl row
cap). [`2026-08-07-eightfold-live-surface-collapse.md`](../audits/2026-08-07-eightfold-live-surface-collapse.md),
[`2026-08-08-sm-eightfold-epistemic-accounting.md`](../audits/2026-08-08-sm-eightfold-epistemic-accounting.md).

### Cluster 8 — hygiene bulk (the majority of the ~1180 commits)

wall-side §7c base-ring regenericisations ("GENUINE" verdicts), the med65
audit second half, lean.ref repointing, wall-side-weak triage, library
Lean red-sweep, one-voice, QA sidecars, provenance hunts, trace-convention
registry. **Zero 1ppq movement** — this is maintenance that keeps the
corpus honest and green, not physics progress. Worth stating plainly.

---

## (b) Current 1ppq / L2 state

**L2 = 2/7** (m_e, m_K/m_π), unchanged. Committed dashboard
`per-observable-100x-status.witness.json` (computedAt 2026-07-18 — **not
re-run this week**):

| obs | role | miss factor |
|-----|------|-------------|
| m_e | CAL-1 anchor | **met** |
| m_K/m_π | meson ratio | **met** |
| m_p | CAL-2 anchor | 437× |
| m_μ | validation | 964× |
| m_n | validation | 416× |
| Q_β | derived | 160× |
| Δ_pn | derived | 159× |

**L1** compute precision (≤1 ppQ cross-method) remains met.

**The live levers, ranked (all q₀-free):**

1. **Δ_λ / deuteron binding MAGNITUDE** (Subgoal-1, scale-free, q₀ cancels)
   — the one open framework-*derivation* precision lever outside the
   measurement-limited ceiling. Value proved; magnitude open. Surviving
   object: the H₆-interface handle-commutator charge (`qou-u8w5` /
   `qou-prjo` / `qou-i4pz`) **or** the fibre→τ-transfer normalization
   resolution.
2. **The additive extensive ≥3-body term** — bracketed by two proofs
   (intensive-vs-extensive + pairwise cap). Localized to the
   **inter-nucleon channel** (`qou-0c19`); candidate mechanisms: the
   torus-operator Bloch-Wigner composition volume (`qou-q6lw`,
   re-scoped live) and Wigner spin-isospin SU(4).
3. **c₃ categorical derivation** (Q_β; drives 3/5 misses) — the
   HH¹/cocenter fibre-level lead (`qou-jcmw`). Necessary-but-not-sufficient
   (anchor swing 3.8× target).
4. **s5-so3 keystone** (`qou-zcjg` / `conj:s5-so3-fiber-action`) — joint
   bottleneck feeding both the color-tube weight and the Δ_λ concentration
   frontier.

**Forbidden (permanent):** any route deriving q₀ from the substrate —
FOREVER GATED, bean `qou-eic1`. Do not plan q₀-derivation work.

---

## (c) Prioritized workplan (ranked next actions)

Each item is tagged with its epistemic character and the relevant bean.

| # | Action | Tier | Bean | Value / risk |
|---|--------|------|------|--------------|
| **1** | **Emit `delta-lambda-witness.json`** with the proved value `(−1)^{n(λ)}·dim V_λ` (general-n), moving `binding_K_direct.py` off `delta_lambda_unavailable`. Witness must state that the magnitude scalar `r*` stays open. | derivation-legal (proved value) | `qou-l39s` | **Highest value / lowest risk.** One concrete unblocked step; the value is proved, not fitted; does NOT produce accurate binding (say so). |
| **2** | **q-sweep the ⁴He two-row signed sum** — test whether the 29,000× suppression is an exact zero at q ≠ q₀ (real selection rule) vs a q₀ coincidence. One finite linear-algebra computation. | probe (derive-then-check) | (new; child of `qou-kemt`) | Cheap, decisive either way; a real selection rule at the doubly-magic SU(4) nucleus would be a genuine structural find. |
| **3** | **Run `dim HH¹(H₅(ζ₅))` at the Bring root of unity + bar-parity test** of the outer class's action on the cocenter. If bar-**even**, the fibre-level c₃ route dies to the same invariant that killed the real routes — cheap, decisive. | probe (formalize-first prune) | `qou-jcmw` | The only genuinely *new* c₃ lead this week; prunes hard either way. |
| **4** | **Construct the H₆-interface handle-commutator charge** symbolically (H₆ non-abelian ⇒ non-zero commutators) and check its eigenphase-weighted trace vs `C_knot = 5.853`, 0-fit — **OR** pursue the fibre→τ-transfer normalization resolution first (cheaper; may dissolve the target). | research (derive-then-check) | `qou-u8w5` / `qou-prjo` | Highest 1ppq leverage IF it lands, but hard and may be chasing a normalization artifact. Do the τ-transfer sanity check first. |
| **5** | **Localize the additive extensive term to the inter-nucleon channel** — test the A=4 color-tube magic-shell saturation and the torus-operator Bloch-Wigner composition volumes `b_i·β(T_{m,n})·b_j` against the ℓ¹-ceiling target (41–64 % per isotope). | research | `qou-0c19` / `qou-q6lw` | The elimination-survivor for the "additive new term"; medium risk, medium horizon. |
| **6** | **Re-scope the "measurement-limited ⇒ not framework-closable" wording** in `docs/precision-goals.md` + the 2026-08-02 lever map from scope-(b) to scope-(a) (numbers stand; a derived c₃ is not excluded). | hygiene / discipline | (fold into `qou-qb8a`) | Small, corrects a live scope-(b) over-claim. |

**Deliberately NOT on the plan:** any 7th fitted Δ_λ ansatz; any
single-scale / per-pair / level / edge / writhe / DT-count deuteron
closure (all walled — see `qou-prjo`); the σ₁³ scalar/surface route
(proved null); the S_leak c₃ filter (retracted); any q₀-derivation
(forever gated).

---

## (d) #4617 / #4619 recommendation

Both PRs are **open drafts**, same author-session lineage, both created
2026-08-02, neither merged. Neither PR's Lean module is on `main`.

### #4617 — μ₃ door VACUOUS at A=2 (`DeuteronFirstOrderCluster.lean`)

- **Finding status: captured on main in prose.** The A=2 vacuity is
  recorded as "A=2 vacuity (parallel route)" in the consolidated μ₃ audit
  (`2026-08-07-mu3-door-status-consolidated.md` §2.3, §6, artifacts
  table). The `Mu3ClusterModularity.lean` it builds against is on main.
- **What is NOT on main:** the sorry-free Mathlib-free Lean *proof* of the
  vacuity (`secondDiff_single_bond_vanishes`, `total_change_decomp`
  Möbius inversion, `deuteron_content_is_first_order`) — 323 additions,
  4 files, `mergeable_state: clean`, lean-direct exit 0.
- **Recommendation: LOW-PRIORITY RE-MERGE (optional).** Per AGENTS.md
  "a Lean-proved piece is a permanent, correct contribution," this cheap
  clean sorry-free module *cements* a claim that currently lives only in
  prose. It is not superseded — it is un-landed. If an idle slot exists,
  rebase + `/prepare-merge`; otherwise it is genuinely marginal (the
  finding is safe). **Not blocking anything.**

### #4619 — σ₁³ Seifert surface-term (`Sigma1CubedSeifertTessellation.lean`)

- **Finding status: SUPERSEDED on main.** Its core negative — the σ₁³
  scalar/character channel is null (`tr[A,B] = 0`) — is already on main via
  `TrefoilSurfaceStateSum.lean` (H₂ abelianness, a *different and stronger*
  proof route: q₀-independent by `commutator_zero`, vs #4619's 40-dps
  numerical null). The surviving direction #4619 pointed at (the σ₁³
  surface term) has since been **closed** — the beans (`qou-u8w5`,
  `qou-prjo`) moved the live object to the **non-abelian H₆ interface
  braid**, i.e. #4619's own object is confirmed dead.
- **The one novel piece not on main:** the tessellation-independence
  certification (TESS-A ≡ TESS-B to 5e-51 ⇒ not a fit). Low standalone
  value now that the direction is closed.
- **Recommendation: DO NOT RE-MERGE.** Effectively superseded. Leave the
  draft open as historical record (never delete branches). If the
  tessellation-invariance harness is ever wanted for a *different* surface,
  cherry-pick the probe then — not now.

---

## (e) Honest assessment + the single highest-leverage move

**Where the framework stands after this week — the blunt version.**

The week was **~95 % hygiene and ~5 % physics**. Roughly 1180 commits
landed; the 1ppq needle did not move (L2 still 2/7, dashboard not even
re-run). The genuine advances were narrow:

1. The Δ_λ **value** is now proved sorry-free general-n — a real,
   permanent contribution, but it **does not** close binding (the value
   was never the gate; the magnitude is).
2. The deuteron-magnitude and μ₃ fronts **converged and closed several
   routes** — the scalar trefoil channel is proved null, the ℓ¹ ceiling
   proves no Δ_λ reweighting can ever close the deficit, and the surviving
   object is now sharply named. This is **productive elimination**: the
   search space is much smaller than it was a week ago, even though no
   number improved.
3. The Q_β / c₃ front produced one dead-code fix and one untested lead;
   the S_leak arc produced a retraction and a discipline rule.

The honest outside-view forecast is unchanged: **the framework's
accuracy story rests on a single open derivation** — the many-body
binding magnitude / additive extensive ≥3-body term — and every route to
it that could be *cheaply* excluded now has been. What remains
(H₆-interface handle-commutator charge; inter-nucleon torus-operator
Bloch-Wigner volume; SU(4) supermultiplet) is genuinely hard and
genuinely open. There is a real risk, flagged repeatedly in the corpus,
that `C_knot = 5.853` is a **normalization artifact** and the deuteron is
already effectively closed via fibre tiers — in which case the "magnitude
gate" is partly a bookkeeping ghost, and the leverage is smaller than the
bean backlog implies.

**The single highest-leverage next move** is **workplan item #4's cheaper
half first: settle whether `C_knot = 5.853` is a real missing magnitude or
a master-formula normalization artifact** by working the
fibre→archimedean τ-transfer (the deuteron is separately ~0.036 %-closed
via fibre tiers). This is decisive and cheap relative to constructing the
H₆ charge, and it determines whether the entire many-body-magnitude
program is chasing physics or chasing a normalization. If it is an
artifact, the L2 binding story simplifies dramatically; if it is real, the
H₆-interface charge (item #4's expensive half) becomes the justified
target. Everything else on the plan is either derivation-legal bookkeeping
(item #1), a cheap prune (items #2, #3), or a longer research horizon
(item #5).

**Concrete immediate action** (derivation-legal, unblocks a consumer, zero
risk): **item #1 — emit the proved-value `delta-lambda-witness.json`** —
should be done regardless, because it is proved, moves `binding_K_direct.py`
off `delta_lambda_unavailable`, and costs nothing.

---

## References

- L2 dashboard: `computations/per-observable-100x-status.witness.json`
- Δ_λ value proof: [`2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md`](../audits/2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md)
- ℓ¹ ceiling: [`2026-08-07-l1-ceiling-confirms-magnitude-absent-and-he4-two-row-suppression.md`](../audits/2026-08-07-l1-ceiling-confirms-magnitude-absent-and-he4-two-row-suppression.md)
- μ₃ door: [`2026-08-07-mu3-door-status-consolidated.md`](../audits/2026-08-07-mu3-door-status-consolidated.md)
- Q_β / c₃: [`2026-08-08-qbeta-l2-assessment-post-week-landings.md`](../audits/2026-08-08-qbeta-l2-assessment-post-week-landings.md)
- Lever map: [`2026-08-02-1ppq-lever-map-post-q0-gate.md`](2026-08-02-1ppq-lever-map-post-q0-gate.md)
- L2 volume-binding cluster: [`2026-08-07-l2-volume-binding-cluster.md`](2026-08-07-l2-volume-binding-cluster.md)
- Deuteron handle beans: `qou-u8w5`, `qou-prjo`, `qou-i4pz`
- q₀ forever-gate: `qou-eic1` / [`2026-08-02-subgoal2-q0-derivation-forever-gated.md`](../audits/2026-08-02-subgoal2-q0-derivation-forever-gated.md)
