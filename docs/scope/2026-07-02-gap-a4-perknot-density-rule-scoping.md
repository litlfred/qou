# GAP-A-4 scoping note — deriving the per-knot density rule ρ(K) (bean fv0y)

**Date:** 2026-07-02 · **Discipline:** formalize-first (AGENTS.md §Formalize-first
probe discipline; `.claude/skills/local/compute-author.md §3.3`). Read-only
scoping; no repo edits, no new ansatz proposed. All numerical near-matches below
are labeled **LEAD** or **near-match**, never derivation.

---

## 1. State of the gap

**GAP-A-4** = derive the general per-knot density rule ρ(K)
(`conj:rho-prefactor-structural`,
`content/quantum-observable-universe/mass-theory/conj-rho-prefactor-structural.md`
— note: the 2026-05-18 gating-context doc still cites the stale
`braids-and-knots/` path; the block now lives in `mass-theory/`).

### The key numbers (recomputed this session at q₀ = 1.10997859555733471)

| quantity | value | source |
|---|--:|---|
| tr_M(p) (per-knot Hecke trace, 𝓑₃ proton) | 1.0653 | excision ledger + `_li_2_q_util.vol_density_per_block` |
| tr_M(n) | 0.9232 | ibid. (p≠n distinct — the real structure) |
| naive per-knot absolute m_p = m_e·Vol(𝓑₃)·tr_M/ℏ_q² | 406.3 MeV (**−56.7%**); m_n = 352.1 (−62.5%, **inverted ordering** m_n < m_p) | `docs/coordination/2026-06-24-lambda-a-fit-excised-per-knot-density.md` |
| λ_A (excised global fit) = (3q²+4+3q⁻²)/4 | 2.5328 → m_p 966 (+2.96%) | ibid. |
| round-trip ρ_rt(p) = m_p^CODATA/(m_e·Vol(𝓑₃)/ℏ_q²) | **2.45995** | recomputed (Vol(𝓑₃)=8G=7.32772, 1/ℏ_q²=101.862) |
| round-trip ρ_rt(n) | **2.46334** | recomputed |
| ρ_rt(p)/tr_M(p) | **2.3092** | recomputed |
| ρ_rt(n)/tr_M(n) | **2.6683** | recomputed |
| \|tr_M(β_Bor)\| implied by F_Bor | ≈ 0.99856 (F_Bor = 4.46914 vs [3]_q!/q³ = 4.47557) | `computations/canonical_mass.py`, `m_p_substrate_identity_50dps.F_Bor` |

**Two structural facts fall out immediately:**

1. **The round-trip density is nearly p/n-DEGENERATE** — ρ_rt(p)/ρ_rt(n) =
   0.99862 (0.14% apart) — while tr_M is **15.4% asymmetric**
   (tr_M(p)/tr_M(n) = 1.15392). So the missing multiplier ρ_rt/tr_M is *itself
   per-knot* (2.309 for p vs 2.668 for n): **no single q₀ scalar closes both**.
   This is why absolute mass was rerouted through the muon-anchored
   `canonical_mass.py` facade (owner ruling 2026-06-24,
   `docs/canonical-mass-formula-guardrail.md`) and why ρ(K)'s remaining leverage
   is **BINDING** (trace ratios, scale cancels, p≠n split is signal).
2. **There are (at least) two "per-knot trace" conventions in the corpus**:
   the chi-cache proton trace 1.0653 vs the F_Bor-implied \|tr_M(β_Bor)\| ≈ 0.9986
   (same 𝓑₃ braid family, different normalization/embedding). Any ρ(K) rule is
   under-specified until the convention is pinned — the Rule-14 hidden-DOF
   warning from the q-dim route probe (option-e ledger, 2026-06-28 cont. row)
   applies verbatim.

### What is already refuted (do NOT re-derive)

Fit-based / structural closures, all verified in the ledgers cited:

| Refutation | Ref |
|---|---|
| 6 original Δ_λ ansätze (co-Casimir #602, Demazure, LP-Plancherel/LP-Frobenius #603, crystal, augmented Markov) | `docs/audits/2026-05-18-delta-lambda-gating-context.md` |
| Bratteli induction H₃→H₄ (3/3) | PR #1841 (`gap-a-path-b-lambda.md`) |
| Markov-trace stabilization (z<1 obstruction) | PR #1850, consolidation #1853 |
| Option-E Kashiwara Δ_λ (5/5) | PR #1860 |
| GAP-A-3 brane-tower P_λ channels (5/5) | PRs #1868 + #1870 |
| Cross-isotope extrapolation of the ³He √([3]_q/[2]_q) near-match (numerology confirmed) | PRs #1882, #1883 |
| T3 Path-B bar-symmetric q-Pochhammer λ(K) (4 candidates, worst −98%) — **already per-knot base, refutation STANDS** | PR #1897; `2026-06-05-gap-a4-final-retrospective.md §2` |
| Pauli–Young / Wigner-SU(4) Δ_λ (19th no-fit closure) | PR #2466; `2026-06-18-pauli-young-delta-lambda-the3-refutation.md` |
| dim and dim_q as bounded-across-A magnitude weights (diverge, 54–451× at ⁶⁷Li) | `2026-06-18-dimq-bounded-across-a-prune.md` |
| Single-dominant-block (sparse) magnitude | `2026-06-18-sparse-interface-magnitude-the3-prune.md` |
| PROBE-4 KL multiplicity sum → chirality sign (KL positivity; Lean-proved premise) | PRs #2381, #2416; `2026-06-16-option-e-probe4-kl-positivity-prune.md` |
| KL left-cell Betti B_λ as canonical \|Δ_λ\| (not cell-invariant; contributive ×2.0 only, scope (a)) | option-e ledger 2026-06-25 + 2026-06-24 rows |
| A=4 full 77-partition f^λ sum (−80.4%; #2839's "B_(10,2)=584 closes A=4" refuted) | option-e ledger 2026-06-28 rows |
| Sign-only Δ_λ reassignment (ℓ¹ ceiling 0.36–0.59 < 1, scope (b), Lean `DeltaLambdaL1Ceiling.lean`) | PR #2925; `2026-06-28-delta-lambda-l1-ceiling-sign-only-prune.md` |
| Dense Wedderburn-projector SDP (degenerate face, selects no unique operator) | `2026-06-17-wedderburn-sdp-structural-bound.md` |
| v9 (1+q)/2 mirror-pair factor as a derivation (+0.12% same-pin, sign-flipped on re-pin) | PR #1707; option-e ledger PROBE 1 |
| B₃-level ρ = round[dim_q(λ*)] from braid strand count alone (p vs ³He indistinguishable at H₃) | `conj-rho-prefactor-structural.md` §Critical structural finding; `rho-prefactor-structural-verifier.witness.json` |

### λ_A-family-bound refutations — these do NOT constrain per-knot forms

Per `docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md` (Step 2
verdicts): **6 of 7 re-examined refutations built their ansätze on λ_A itself**
and rule out only λ_A-family forms; the canonical per-knot tr_M(K) base was
**never tried** in them:

- `gap_a4_L1_light_series_probe.py` — L1a/b/c (PR #1874's refutation is λ_A-bound)
- `gap_a4_He3_residual_probe.py` — λ_A/2, √(λ_A/[2]_q) ansätze
- `gap_a4_S_K_additive_probe.py` — additive S(K) with lw = λ_A base (so PR #1886's
  T1 "closed NEGATIVE **under uniform-λ**" does not close the per-knot-base S(K) family)
- `gap_a4_T2_per_knot_vol_probe.py` — anchored on the λ_A convention (so PR #1891's
  Vol-convention refutation is family-bound)
- `gap_a4_T4_schur_weyl_icosahedral_probe.py` — tried to *derive* λ_A (deriving a fit; misdirected)
- `binding_color_vs_charge_tn3he.py` — base_lw = λ_A

**Honest exception:** the co-Casimir Δ_λ = 1/dim_q refutation (#602) is
density-independent (verdict lives in the per-partition sum) — **robust**, not
an artifact. The per-knot re-runs are scoped in bean **3xbo** (status **todo**
as of 2026-07-02, `.beans/3xbo--…`), child of the completed x5az audit.

---

## 2. Hypothesis classes still open

**(A) Per-knot-base re-run of the λ_A-bound closure families** (bean 3xbo).
Re-run L1-style per-atom density rules, the additive S(K) family, the ³He
residual, and color-vs-charge with `vol_density_per_block` (p≠n-distinct
tr_M(K)) as the base instead of λ_A.
*Must produce:* binding B(K) across D/T/³He/⁴He (and the T/³He split
+1.4947 m_e) without per-atom retuning; for the artifact hypothesis, any
verdict flip vs the λ_A-based run.
*Status:* open, never run; scoped, cheap.

**(B) The canonical GAP-A-1 corollary route** (the conjecture's own closure
path): ρ = dim_q(λ*(T_w)) with λ* the dominant Wedderburn summand of the
canonical Hecke element at the **atomic** strand count n₀ = 3A, entering
through the binding operator K(𝓗) = binding link · ⊗ᵢ T_w(nucleonᵢ).
*Must produce:* the observed ρ table (p/n → 1, ³H/³He → 2) with the
orthogonal-copies interpretation reconciled (obligation 3 of the block), then
extension to A ≤ 60 without re-tuning.
*Status:* open; blocked on canonical knot-ID (GAP-A-1) multi-term SDP cost
(T2–T6 wiring — the prototype's single-term cost gives ρ⋆=3 for ²H instead of
the historical 1). The B₃-level shortcut is falsified (see §1); H_{3A}
evaluation is the required refinement.

**(C) The s5-so3 geometric W_λ route** — owner-**authorized** (narrow 2026-06-19
reversal; G1-framing correction in the keystone ledger 2026-06-26 row: not
owner-gated, blocked only on research-level DG). The full-Hecke geometric-index
program (`docs/scope/2026-06-24-keystone-fullhecke-geometric-index-program.md`,
G1 live in PR #2524, Beasley–Witten localization on S³/2I).
*Must produce:* the λ-family W_λ = d_q(λ)²/D² whose index passes the
already-Lean-formalized gates: defect cubic 144·C(n) = −n(n−1)(2n−13) with the
n=7 sign flip (#2811, cross-checked #2744), the full C/D/E ladder (#2825), the
deuteron f_pn ∈ (0.395, 0.661) bracket (`KeystoneFpnBracket.lean`), and
conjugation symmetry W_λ = W_{λ'} (#2794). SU(2)/WRT sub-route is (b)-foreclosed
(#2717, Lean #2727) — the index must live full-Hecke side.
*Status:* the single open categorical object; this is where the Δ_λ/λ(K)
**magnitude** must ultimately come from (keystone ledger: "the single open
object for m_τ, GAP-A-3 binding Δ_λ, and GAP-A-4 mass λ(K)").

**(D) Option-E PROBE 2 — the A=4 multi-nucleon interface operator**
(`docs/coordination/option-e.md` §Open probes; the mirror-pair symmetry
collapses at A=4). Consumes the operator-valued branching combiner cluster
(#2369/#2371/#2372); the complete ⁴He χ (77 partitions) is on main
(`…-matrix-m` witness, option-e ledger 2026-06-28).
*Must produce:* the ×5.1 magnitude gap at ⁴He (f^λ sum gives 5.55 MeV vs
28.30 AME) from an interface/branching object, not a weight refit.
*Status:* open; the honest frontier named by the PROBE-4 prune.

**(E) z2bn magnitude-side fibre kernel** — S(m) = Σ_λ dim_q(λ) has an exact
q-Gaussian/Habiro generating function (PR #2899, Lean
`QOU.Mass.BindingQGaussianHabiro`); listed by the ℓ¹-ceiling PR #2925 as the
active magnitude lever that escapes the sign-only cap, and by the A-scaling
probe as exactly the "structured kernel that bends the A-scaling".
*Must produce:* the 41–64% missing ℓ¹ mass with A-structure (no flat
convention lands D/T/³He/⁴He simultaneously — spread 2.2–4.7×).
*Status:* structure pinned, closure downstream; scope (a).

**(F) The residual-structure map as a constraint surface** (not a closure):
log_{q₀} Δ_λ(A,T₃) = a(A) + b(A)·T₃ + c(A)·T₃² (IMME shape;
`2026-06-29-delta-lambda-residual-synthesis.md`) — bar-odd writhe (4Z) carries
the p≠n channel; a(A) power-law is A ≤ 4 only. Near-match tier, unwired; any
candidate ρ(K) rule must reproduce this decomposition's parity split.

---

## 3. Formalize-first invariants (prune BEFORE any wide search)

**I-1. p/n near-degeneracy vs trace asymmetry (kills the "single missing
q₀-constant" class — a (b)-grade exclusion with a measured invariant).**
ρ_rt(p)/ρ_rt(n) = 0.99862 but tr_M(p)/tr_M(n) = 1.15392, so any
ρ(K) = tr_M(K)·f with knot-independent f gives m_n/m_p = tr_M(n)/tr_M(p) =
0.8665 ≠ 1.00138 — off by 15.5%, orders beyond any tolerance. Any absolute-mass
correction factor must satisfy f(p)/f(n) ≈ 1.1555⁻¹·… ≈ 0.8654, i.e. nearly
*invert* the trace asymmetry.
*Lean-lemma shape:* generic ordered field;
`theorem no_uniform_scalar_density (tr_p tr_n ρ_p ρ_n f : R) (h₁ : tr_p/tr_n ≥ 1.15) (h₂ : ρ_p/ρ_n ≤ 1.001) : ρ_p = f*tr_p → ρ_n = f*tr_n → False`
(arithmetic-trivial; the value is the *gate* — it structurally forecloses the
scalar-family before anyone scans it). Corollary: the per-knot density's honest
domain is binding, matching the excision ledger.

**I-2. Bar-parity (q ↔ q⁻¹) channel separation.** The p≠n split is carried by
the bar-ODD writhe channel (σ−σ⁻¹ = 4Z; `imme_mirror_diff` Lean, residual
synthesis), while the absolute scale is bar-even. Precedent: #2584's projector
shift was refuted partly for being **bar-mixed**. Any candidate per-knot
correction should be decomposed into bar-even/bar-odd parts first; a bar-even
candidate cannot supply the p≠n binding split.
*Lean-lemma shape:* `barOdd (fun q => trM_p q − trM_n q)` /
`barEven (fun q => trM_p q + trM_n q)` on the symbolic H₃ traces (fibre-level,
generic R per §7c — no q₀).

**I-3. Positivity + growth bound across A.** Markov weights y_λ > 0, W_λ > 0
(Lean `qPlancherelWeight` infra, #2794); and the bounded-across-A prune shows
dim and dim_q both diverge (54–451× overshoot at A ≥ 6) while sgn/raw
undershoot 10⁵×. So any per-knot magnitude weight must have **intermediate
(≈ linear-in-A) growth**.
*Lean-lemma shape:* a class hypothesis
`class BoundedDensityRule (ρ : ℕ → R) : Prop where growth : ∀ A, ρ A ≤ C * A`
used as a §3b-cond gate on candidate rules — refutes the whole
combinatorial-dimension family without a scan (already effectively proved
piecewise; consolidating it is cheap).

**I-4. The ℓ¹ ceiling (already Lean-proved — reuse, don't re-derive).**
`DeltaLambdaL1Ceiling.lean`: any sign/chirality reassignment on the existing
y_λχ^λdim data is capped at 0.36–0.59 of target ⇒ a candidate ρ(K) rule that
only re-signs existing data is dead on arrival; it must add ℓ¹ mass.

**I-5. Ratio-lead screen (run this session; leads ≠ derivations).**
At q₀: [2]_q = 2.01090, [3]_q = 3.04371, [3]_q! = 6.12058, [3]_q!/q³ = 4.47557,
F_Bor = 4.46914, λ_A = 2.53278.

- **ρ_rt/tr_M(p) = 2.3092: NO natural q-object within 1%.** Closest:
  [3]_q!/(2q³) (−3.09%), [2]_q·q = q²+1 (−3.34%), q+1 (−8.6%), [2]_q (−12.9%).
  And since r_p ≠ r_n (2.309 vs 2.668) no single object *could* close both (I-1).
- **√([3]_q!) = 2.47398 vs ρ_rt = 2.45995/2.46334: +0.57%/+0.43% — a ≤1%
  LEAD to verify, NOT a closure.** Entropy caveat (deliberate junk control run
  alongside): e^{0.9} matches ρ_rt(p) to **0.014%** — at 3-digit precision with
  ~20 candidates screened, sub-1% single matches carry essentially zero
  evidential weight (the PSLQ entropy-bound discipline, PR #1805 precedent).
  Cheap decisive test before spending anything: does √([3]_q!) track ρ_rt under
  the muon↔proton q₀ re-pin (the option-e "failure-mode signature") and at
  50 dps? Also note 5/2 (λ_A's constant term) is +1.6% — the already-known
  2-sig-fig near-match the excision ledger records.
- **tr_M(p)/tr_M(n) = 1.15392 vs q^{3/2} = 1.16942 (+1.34%)** — near-match,
  > 1%, not a lead.
- **F_Bor/([3]_q!/q³) = 0.99856 ⇒ \|tr_M(β_Bor)\| ≈ 0.9986 ≠ 1.0653 = tr_M(p).**
  Not a numerology item — a **convention discrepancy to pin** (which trace is
  "the" per-knot density?). This is I-6:

**I-6. Trace-convention uniqueness.** Before any ρ(K) search, pin the
canonical per-knot trace object (chi-cache tr_M(K) at the knot's own strand
count vs the F_Bor braid trace vs the H_{3A} embedded trace of
`conj-rho-prefactor-structural` §refinement). The q-dim route probe already
showed convention freedom is a hidden DOF spanning 0.41→5.62 on the ⁴He
ceiling — an unpinned convention makes any "match" unfalsifiable.
*Lean-lemma shape:* a definitional consolidation + equality/inequality lemma
between the two H₃ traces (compute-checked witness first).

---

## 4. Recommended attack order

Constraints respected: **no new fit-based ansatz** (Δ_λ gate, 19-closure chain);
**Subgoal-2 absolute-mass q₀ derivation stays out of scope** except the narrow
s5-so3 W_λ reversal; absolute masses stay routed through `canonical_mass.py`.

1. **Bean 3xbo re-runs** (per-knot base for the 6 λ_A-bound closures +
   co-Casimir cross-check). *Cost:* hours; scripts exist, swap the density
   base. *Gate:* any verdict flip ⇒ the flipped family (most plausibly the
   per-knot-base additive S(K) or the L1-style per-atom rule) becomes the
   priority numerical thread; no flips ⇒ the artifact hypothesis closes
   honestly and per-knot leverage is confirmed as binding-only. Either way the
   ledger gets a durable (a)/(b)-scoped verdict per script.
2. **Trace-convention pin (I-6) + p/n degeneracy invariant (I-1) formalized.**
   *Cost:* ~1 session (witness + two small Lean lemmas over generic R).
   *Gate:* fixes the object every later step talks about; I-1 forecloses the
   scalar-correction family with a cited invariant so no one scans it. Fold in
   the cheap √([3]_q!) lead disposal (cross-anchor + 50 dps check, minutes;
   expected outcome per the e^{0.9} control: drop).
3. **Bar-parity decomposition (I-2) of the p−n trace difference and the
   binding residual.** *Cost:* 1 session (symbolic H₃ compute + parity Lean
   lemma). *Gate:* classifies every surviving candidate class as bar-even/odd;
   bar-even candidates exit the p≠n channel without a scan.
4. **s5-so3 geometric W_λ program (class C)** — the authorized magnitude
   frontier. Do **not** duplicate: G1 is live in PR #2524 and the gate suite
   (#2811/#2825/#2794, f_pn bracket) is already formalized; contribution here
   is coordination + consuming any W_λ output into the deuteron
   `deuteron_fpn_from_Wmap` harness (#2528). *Cost:* multi-session DG research
   (upstream); *gate:* a W_λ passing the defect-cubic + f_pn gates feeds
   directly into classes D/E magnitudes.
5. **PROBE 2 / A=4 interface operator (class D) + z2bn kernel (class E)** —
   pursue only after 1–3, constrained by I-3 (linear-in-A growth) and I-4
   (must add ℓ¹ mass) and the A-scaling non-uniformity finding. *Cost:*
   multi-session; χ data for ⁴He is on main, Betti-side sums are
   Rust-infeasible at S₁₂ (don't re-attempt full Betti).
6. **Explicitly not to be done:** a 7th/20th fitted weight; any
   Vol(𝓑₃)·ρ/ℏ_q² absolute-mass re-pin (guardrail); a fresh λ_A derivation
   attempt (T4-style — deriving a fit); re-walking the §1 refutation table.

---

## 5. Cross-references (all verified this session)

- `docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md` — 6-of-7
  λ_A-family-bound verdicts; co-Casimir robust; the −57%/ρ≈2.46 nuance table.
- `docs/coordination/2026-06-24-lambda-a-fit-excised-per-knot-density.md` —
  excision ruling + same-day correction (per-knot is also wrong for absolute mass).
- `docs/canonical-mass-formula-guardrail.md`, `computations/canonical_mass.py`,
  `computations/m_p_substrate_identity_50dps.py` — muon-anchored facade; F_Bor.
- `computations/_li_2_q_util.py::vol_density_per_block` (line 424) — per-knot
  density def (binding-valid, absolute-mass-deprecated).
- `docs/coordination/gap-a-path-b-lambda.md` — PRs #1816, #1841, #1850, #1853,
  #1860, #1868, #1870, #1872, #1874, #1876, #1882, #1883, #1886, #1891, #1897;
  T1/T2/T3 closed rows; 18→19 closure chain; 2026-06-23 rescope note.
- `docs/audits/2026-05-18-delta-lambda-gating-context.md` — Δ_λ gate, Paths
  A–D, six ansätze, 2026-05-29 retraction.
- `content/quantum-observable-universe/mass-theory/conj-rho-prefactor-structural.md`
  — GAP-A-4 statement, B₃-level falsification, n₀=3A refinement, GAP-A-1 corollary path.
- `docs/coordination/s5-so3-keystone.md` — narrow owner reversal (2026-06-19,
  recorded 2026-06-22; G1-framing correction 2026-06-26); gates #2794/#2811/#2825/#2744;
  SU(2) foreclosure #2717/#2727; live G1 #2524.
- `docs/coordination/option-e.md` — PROBE 1 refuted (#1707), PROBE 4 pruned
  (#2381/#2416 + 2026-06-25 Betti cell-dependence), PROBE 2 open, A=4
  non-closure (2026-06-28 rows), ℓ¹ ceiling #2925, z2bn #2899.
- `docs/audits/2026-06-29-delta-lambda-residual-synthesis.md` — IMME residual map.
- Beans: `x5az` (completed audit), `3xbo` (re-runs, **todo**), `yq5q` (session).
- Session numerics: q-bracket/ratio screen at q₀ = 1.10997859555733471
  (mpmath, 50 dps); all values quoted in §1/§3 reproduced from first principles
  except tr_M(p/n) = 1.0653/0.9232 (quoted at ledger precision).
