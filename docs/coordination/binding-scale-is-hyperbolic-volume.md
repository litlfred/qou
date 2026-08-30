# The binding scale is the hyperbolic volume — coordination ledger

**Date:** 2026-07-13 · **Owner question:** "what is driving the scale?" (of
per-isotope binding). This ledger records the answer and, per the "make sure
Lean proved" directive, the **exact** proof status of each part — separating what
is Lean-proved, what is conditional on an open conjecture, and what is empirical.

## The answer

The per-isotope binding scale is `m_e · Vol(K)` — the **hyperbolic volume** of the
nuclear sub-link — carried by the bond-count law

`B(K) = m_e · Σ_n M_n(A) · Vol_n(K)`,  `M_n(A) = (n−1)` (linear-chain bonds).

This is the one construction that does **not** undershoot: ³H = m_e·2·Vol(8₁₁) =
8.47 MeV (−0.16%), ³He = m_e·2·Vol(L6a4) = 7.49 MeV (−3%), zero fit. Every
parameter-free object that undershot this session (the `sgn·dim` Δ_λ base 70–89%,
the Reeb phase θ_λ ~270×, the deuteron resummation ~37×) undershot precisely
because it **lacked the volume** — the missing magnitude is not a q₀ power (checked
and excluded) but the **volume**, a distinct hyperbolic invariant.

**Physical driver (volume conjecture).** `Vol(K)` is the exponential growth rate
of the colored Jones polynomial, `Vol(K) = lim_N (2π/N)·log|J_N(K; e^{2πi/N})|`
— the braid's categorical entropy / na-Stokes "computational time." So *binding
energy = m_e × (hyperbolic complexity of the nuclear braid)*: more linking → more
volume → more binding.

## Lean / proof status (STRICT — the "make sure Lean proved" table)

| claim | status |
|---|---|
| **bond-count multiplicity `M_n(A) = (n−1)`** and the cluster-measure identity `6·Σ_k (A−k)k = (A−1)A(A+1)` | ✅ **Lean-proved, sorry-free** — [`QOU/Mass/LinearChainBondCount.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/LinearChainBondCount.lean) (`chainBonds`, `linear_chain_cluster_measure`, proved by induction; 0 sorries; source-confirmed — not `lean_verify`'d in this sandbox) |
| **deuteron `Vol = 0`** (2-body Hopf sub-link) | geometric fact — the Hopf link is **non-hyperbolic**, so the RHS of the volume conjecture vanishes ([`degree-one-braid-trivial-volume-proof.md`](../../content/quantum-observable-universe/mass-theory/degree-one-braid-trivial-volume-proof.md), KMM convention) |
| **`Vol(K)` IS the binding scale** (the load-bearing claim) | ⚠️ **CONDITIONAL — but now PER-LINK, and mostly on PROVEN instances (narrowed 2026-07-13, citation verified).** The framework needs only the volume-conjecture instances for its specific links, not full KMM: **L6a4 = Borromean rings** — **PROVEN** (a Whitehead chain; R. van der Veen, *Proof of the volume conjecture for Whitehead chains*, [arXiv:math/0611181](https://arxiv.org/abs/math/0611181), Acta Math. Vietnam. 2008 — family explicitly includes the Borromean rings; web-verified 2026-07-13), and since 2026-07-26 **machine-proved sorry-free in-repo** (`QOU.Knot.FigureEightVolume.tendsto_log_borromeanKashaev_vol`, bricks B1–B5 in [`BorromeanVolume.lean`](../../content/quantum-observable-universe/lean/QOU/Knot/BorromeanVolume.lean), PR #4381 — carrier defined by the Habiro root-of-unity positive sum, GL2011 App. A; the diagrammatic identification is the cited input, mirroring the 4₁ precedent). **4₁ (muon anchor)** — proven (Ekholm/Andersen–Hansen), and since 2026-07-26 **machine-proved sorry-free in-repo** (`QOU.Knot.FigureEightVolume.tendsto_log_kashaev_vol`, the E5d Riemann-sum squeeze in [`FigureEightVolumeSqueeze.lean`](../../content/quantum-observable-universe/lean/QOU/Knot/FigureEightVolumeSqueeze.lean), milestone qou-cpfn). **8₁₁ (³H)** — **open** (the one remaining open instance). So the ³He and 𝓑₃-anchored scale identifications are conditional on *proven theorems*; only ³H rides an open instance. Per "conditional-proved ≠ premise-established," the general claim stays conditional. |
| **the 3% accuracy** of `m_e·2·Vol` vs AME | empirical (measured; the −3% ³He residual is the Coulomb/EM piece, 31% derived) |

> **8₁₁ (³H) has two open legs, not one** (2026-07-17,
> [audit](../audits/2026-07-17-8-11-vc-open-and-id-unverified.md)): besides the
> open VC instance, the **8₁₁ = ³H assignment itself** is a
> `manual-historical-volume-match` (chosen for the −0.16 % fit, not returned by
> the SDP knot-ID). No citation closes 8₁₁'s VC (it lies in no proven family and
> is beyond the individually-verified frontier). The honest closure is the
> **canonical SDP knot-ID at H₉** for the true A=3 link — which may land a
> van-der-Veen-closable link (as L6a4 did) or *derive* 8₁₁, replacing the
> historical guess. Not a refutation of either leg; both are scope-(a) open.

> **The 5- and 6-crossing instances are proven — and were already proven when
> this ledger was written** (2026-08-30, bean `qou-ckbv`). VC for $5_2$ is
> Ohtsuki, *On the asymptotic expansion of the Kashaev invariant of the $5_2$
> knot* (library `104171-qt-83`, preprint `ki52`); for $6_1$, $6_2$, $6_3$ it is
> Ohtsuki–Yokota, *…knots with 6 crossings* (library `ki6c`, §§3–5, each headed
> "Proof of Theorem 1.1 for the $6_x$ knot"; the abstract states "we show the
> volume conjecture for these knots"). **$6_2$ is the canonical $^2$H closure**
> in `computations/substrate/knot_volumes.py`, so a load-bearing instance moves
> from open to proven.
>
> Both papers were in `library/` the whole time, and `ki6c` was already cited by
> `QOU/QBeta/GZThirdKnotRankGrading.lean` — for its saddle-point data, without
> anyone noticing it also discharges the conjecture. Meanwhile
> `b1-hyperbolic-rows-theorem-table2-data` recorded $6_2$ and $6_3$ as **open**
> and $5_2$ as "numerical, not full proof", the opposite of what the papers say.
> So this was not a literature gap but a reading gap: the corpus-grep discipline
> that catches a *missing* citation does not catch one that is present, filed,
> and unread.
>
> **Not upgraded:** the seven-crossing sequel (*Internat. J. Math.* **28**(13),
> 2017) is real — web-verified — but is not in `library/`, so $7_*$ stays open
> pending a filed copy. **Its authorship is no longer unsettled** (2026-08-30):
> `library/ki52` ref **[26]** reads "Ohtsuki, T., *On the asymptotic expansion
> of the Kashaev invariant of the knots with 7 crossings*, in preparation" —
> **sole author**, from a primary source already filed. (Same reference list
> settles the neighbouring attribution: ref [28] is "Ohtsuki, T., **Takata,
> T.**", so the two-bridge torsion paper is a two-author work.) The blocker is
> now only the filed copy, not the byline. **8₁₁ is unaffected** and remains the
> load-bearing open instance: an 8-crossing knot, outside every family above.

> **⚠️ Do not close 8₁₁ off a two-bridge or a "42,000 knots" headline**
> (2026-08-30, bean `qou-b5h9`). Two results now in `library/` reach 8₁₁ and
> neither gives it the volume conjecture:
>
> * **8₁₁ = b(27,10) is two-bridge** (isometry-verified in-sandbox against the
>   SnapPy `8_11` exterior), so Ohtsuki–Takata, *Geom. Topol.* **19** (2015)
>   853–952 (`library/download-1/`) covers it, as does Garoufalidis–Yoon
>   (`library/arxiv-2411.03801v2/`). But both prove `ω²(D) = ±τ(K)/(2√−1)` — a
>   statement about the **1-loop / torsion** coefficient, defined from the
>   diagram with no reference to asymptotics. The bridge to the actual Kashaev
>   prefactor is Ohtsuki–Takata Prop. 4.9, gated on their **Assumption 4.8**
>   (Poisson summation + saddle point), which the literature verifies only up to
>   7 crossings. Ohtsuki–Takata never claims the volume conjecture for anything;
>   "volume conjecture" occurs twice in its 100 pages, both in the historical
>   survey. Same for 10₄₃ = b(73,27).
> * *FAMED by computer: proving the Andersen–Kashaev volume conjecture for
>   42,000 knots* (arXiv:2512.17437) proves its conjecture for all knots with
>   ≤ 12 crossings, nominally including 8₁₁. It is the **Andersen–Kashaev** VC
>   for the **Teichmüller TQFT**, not the coloured Jones at $e^{2\pi i/N}$.
>   `references.bib` already carries this scope warning for a neighbouring
>   Chen–Yang result; it is repeated *here*, at the 8₁₁ row, because that is
>   where a reader will otherwise act on the headline.
>
> What the two-bridge results *do* give: the **modulus** half of the corpus's
> $c_\sigma$ law, unconditionally for every hyperbolic two-bridge knot, since
> $\tau_{DG}$ and $\tau_{OT}$ are reciprocals and $|\omega|^2 = |\tau_{OT}|/2$.
> For 8₁₁ that predicts $|\omega_{\text{Hessian}}| = 0.238296403552$. Whether
> that number is the Kashaev asymptotic prefactor there is the open part.

**Bottom line for Lean:** the *combinatorics* of the scale (the bond count) is
proved; the *identity* that makes `Vol` the scale is the open volume conjecture.
So "binding = m_e·Vol" is a **rigorous conditional result** modulo one named,
class-axiomatised conjecture — not an unconditional theorem. Claiming it as
"derived/proved" without that qualifier would be laundering.

## What this narrows the open gate to

The magnitude is **not** a universal missing scale — it is `m_e·Vol` wherever the
sub-link is hyperbolic (derived modulo the volume conjecture). The genuine open
items are narrow and specific:

1. **⁴He 4-body `Vol₄`** — **falsifiable test EXECUTED (2026-07-13,
   `vol4_4he_snappy_falsification_probe.py`): NEGATIVE.** SnapPy (validated
   against the corpus L6a4/8₁₁ to 1e-11) shows no in-advance-named structural
   candidate matches the residual-implied `Vol₄ = 8.048`: the linear 4-chains
   (L8a21/L8a20) sit at 10.149 (+26%), the brunnian Borromean-analogue is
   non-hyperbolic, L8n7 carries exactly Vol(Borromean). The prediction
   `8.048 < Vol(8₁₁)=8.286` was already against the volume-complexity trend. So
   the naive "n=4 term = one chain-link volume" reading **fails at ⁴He**
   (scope-(a); the Lean-proved multiplicity and the A=3 results are untouched).
   **Closed out same day** (`he4_vol4_prediction_test_probe.py` +
   [audit](../audits/2026-07-13-he4-vol4-prediction-test.md)): the implied
   `Vol₄` is now computed *exactly* from AME/m_e/corpus volumes (8.0484,
   confirming the pre-registered 8.048 to 4e-4), and a guarded census scan of
   all 7463 4-component HT links (≤14 crossings) finds **zero** volumes within
   ±0.05 of 8.048 (nearest ±0.31) — the prediction falls in a *gap* of the
   census spectrum, so no ≤14-crossing 4-component link carries it even
   post-hoc. Honest routes: the SDP canonical knot-ID at H₁₂ for the true ⁴He
   link, or a non-single-volume n=4 term.
2. **deuteron** — NOT an open wall. It is derived via `m_e·Vol(𝓑₃)·Δtr` at
   **+0.19%** (the single-nucleon Borromean knot 𝓑₃, scalar-trace collapse). The
   "Hopf `Vol=0`" is only the *bond-count multi-body-chain* route being
   inapplicable at A=2 (a 2-body chain has no hyperbolic sub-link) — a
   route-boundary, not a gap. My earlier "deuteron wall / entanglement
   resummation" framing (#3736) over-stated it: the resummation undershoot is a
   negative for *that route*, not evidence the deuteron is open.

### Why "two derivations"? They are ONE — two contractions of the q-Reeb phase

The cheat-sheet "derived twice" (`m_e·Vol(𝓑₃)·Δtr` at +0.19% and
`μ₀·ℏ_q·J_q²(j=n/2)` at −9%) is **not** two independent derivations — a single
physical binding number should have one, and it does. Both are collapses of the
**single per-block q-Reeb phase `θ_λ`** (the Reeb coordinate): the cheat sheet
states it outright — *"the per-rep highest-weight `j=n/2` collapses the per-block
Reeb phase just as the scalar trace does."*

| collapse of `θ_λ` | resulting form | accuracy |
|---|---|---|
| scalar trace (`Δtr`) — full contraction | `m_e·Vol(𝓑₃)·Δtr` (volume route) | +0.19% |
| highest weight `j=n/2` — leading-spin truncation | `μ₀·ℏ_q·J_q²` (rotational route) | −9% |

So the object is `θ_λ`; `Vol` is its all-orders (semiclassical, colored-Jones-
growth) contraction and the rotor `J_q²` is its leading-spin truncation. The ~9%
gap between them is the **inter-scheme truncation error** (leading spin vs full
trace), i.e. a **consistency check of the one derivation**, not two. This unifies
the session's threads: the Reeb phase `θ_λ` is the object; the hyperbolic volume
is what makes its contraction extensive and MeV-scaled; the "two derivations" are
its two collapse schemes. (The third, per-λ route with a fitted `C_knot = 5.852`
— exactly the μ_ext I measured — was **retracted as a fit**; it is not a
collapse of `θ_λ` but an anchor inversion.)
3. **mirror Coulomb residual** — 31% derived (`tanh(ln q₀)·B_pp`); the pairwise
   EM route is provably empty (Borromean pairwise linking 0). **Calibrated
   2026-07-13:** the fixed `B_pp/3` Borromean-channel candidate is a
   single-point coincidence — the 8-pair mirror systematics
   (`split/ΔE_C = 0.838 ± 0.059`) shows the split follows the continuum Coulomb
   `Z(Z−1)/A^{1/3}` scaling, which a fixed 1/3 fails at ⁷Li/⁷Be (2.2×). The
   honest open object: derive `~0.84·α·Z(Z−1)/R(A)` from the categorical EM
   (α_EM + a derived radius law). **Attempted 2026-07-13 (R2-c): PARTIAL** —
   `split = (3/5)·α·ΔZ(Z−1)·m_π/A^{1/3}` (pion-Compton radius `R = λ̄_π·A^{1/3}`,
   CAL-3 length, zero fitted constants) gives `split/pred = 0.985 ± 0.069`
   across all 8 pairs, superseding both fixed-1/3 and pairwise tanh on scaling;
   the underived steps are the Yukawa packing selection (`R_unit = λ̄_π` at
   coefficient 1) and the volume→radius extensivity identification —
   [`2026-07-13-mirror-split-continuum-em-derivation-attempt.md`](../audits/2026-07-13-mirror-split-continuum-em-derivation-attempt.md).

## Session cross-refs

Mass-binding closure tranche (#3764, 2026-07-13): mirror-split 1/3 = **datum
only**, gate decomposed S1/S2/S3
([`2026-07-13-mirror-split-one-third-mechanism-probe.md`](../audits/2026-07-13-mirror-split-one-third-mechanism-probe.md));
S₃-equivariant EM functional — **S2 closed** (equal pair-weight derived from
link symmetry), new μ̄ sign-rep obstruction (coupling through |μ̄| only), S3
re-scoped to **one scalar κ**, calibration-constrained by the 8-pair mirror
systematics above (a κ closure reproducing only A=3 is single-point)
([`2026-07-13-mirror-split-s3-em-functional-attempt.md`](../audits/2026-07-13-mirror-split-s3-em-functional-attempt.md));
deuteron coupling derive-or-refute **negative** + corrective on #3736: the
level-1/2 median resummation plateaus at ~21% of B_D at *every* coupling —
"reaches B_D as x→1/√2" was an extrapolation artifact
([`2026-07-13-deuteron-coupling-candidates-derive-or-refute.md`](../audits/2026-07-13-deuteron-coupling-candidates-derive-or-refute.md)).
Deuteron trans-series negative (#3736); Δ_λ gate + CKRecursion review (#3723);
Borromean redirect + Reeb test + "magnitude not a q₀ power" (#3738);
θ_λ magnitude gate ([`2026-07-03-theta-lambda-via-reeb-nastokes-jet-filtration.md`](../audits/2026-07-03-theta-lambda-via-reeb-nastokes-jet-filtration.md)).
