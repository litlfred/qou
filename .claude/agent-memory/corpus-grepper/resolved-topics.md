# corpus-grepper — resolved topics

Split out of `MEMORY.md` on 2026-09-03: it is a lookup table consulted per
topic, and the injected file's first 200 lines are the scarce resource.
Read this before declaring any listed topic open; add a row when a sweep
settles one.

Append here whenever a sweep lands. Format: *question → where → verdict →
date*. This is the entry type that saves the most work.

- Groupoid with inequivalent fibre objects carrying a 3-dim `W` whose
  fundamental is not self-dual → bean `qou-dwsh` body (completed
  2026-08-03) → answered; reachable by path 6 only.

- **Why is the integer coordination count `M` the binding multiplier while
  mass carries the q-dim linking weight `lw`?** (bean `qou-brng`, "the
  linking-vs-self-energy route") → **PARTIALLY COVERED, and the target has
  moved.** 2026-08-30.
  - *Still open, and the corpus says so in as many words:*
    `docs/audits/2026-08-30-coordination-saturation-formalized.md`
    §"What stays open" — *"the amplitude assignment … is **not** proved."*
  - *But a `B = Σ_bonds f(bond)` law is scope-(b) EXCLUDED as a TOTAL* by
    `QOU.Mass.PairwiseCumulantVanishing.b3_eq_zero_ofBondFunctional`
    (sorry-free, `f` arbitrary, `μ` bond-dependent) against AME
    `b₃ = +1.426222 MeV`. So "why is `M` the multiplier" cannot be answered
    by any per-bond assembly alone.
  - *The nearest existing derivation* is the Gram-quadratic split
    `B ~ ⟨Σᵢgᵢ⟩²_G = Σᵢ⟨gᵢ⟩²_G + 2Σ_{i<j}⟨gᵢ,gⱼ⟩_G` —
    `docs/audits/2026-07-11-eigenfunction-weight-kernel-link-and-wn-derive-or-refute.md`
    Parts 10–13, beans `qou-v0yw` / `qou-vibo`. **Its numbers are stale**
    (convention-C + float64, see the TRAP below); its algebra survives.
  - *Citable rather than re-derivable:* Moffatt–Ricca `procrsoclondona92`
    (`ocr/` only — see the `ocr/` TRAP).

## Moved from `MEMORY.md` 2026-09-03 (it had grown past line 200)

- **Does the corpus hold "the Markov/Ocneanu trace family over all SU(N)
  specialisations `z_N = q^N/[N]_q` spans exactly `n` of the `p(n)` trace
  functionals, so no combination isolates a >1-dim block character"?**
  → **CLOSED, but on a BRANCH, not `main`.** 2026-09-02.
  - Carrier: `computations/probes/markov_trace_family_rank_probe.py`, commit
    `9f97474c46` (PR #6415), branch `claude/tower-row-cap-sm-binding-2026-09-01`
    — **not on `origin/main`** — plus the `2026-09-02` section of bean
    `qou-brng`. Verbatim same numbers (rank = n at n=2..7, only the two
    1-dim blocks recoverable, `(4,2)` visible-but-not-isolable).
  - **On `main` the result is genuinely absent** — all six paths empty for the
    span-dimension SHAPE.
  - **THREE different things are called "rank" here — resolve before citing:**
    (i) `markov_z_fibre_rank_bar_covariance_probe.py` "fibre rank" = the SU(N)
    index `N`; (ii) `pyhecke_n_generic.gram_inverse_n` "rank" = Gram rank at a
    FIXED z = #{≤2-row λ} (2 at n=3, 3 at n=4); (iii) the span dimension = n.
    A topic-grep for "rank" + "Markov" returns (i) and (ii) and misses (iii).
  - The H₃ coefficients `6.22044128, −33.41778449, 28.19734321` are in **no
    commit reachable from main** (`git log --all -S` empty); only the branch
    probe docstring + the branch bean carry them. The probe's phrase *"the
    corpus carries a three-trace combination at H₃"* is **unsourced**.
  - Adjacent-but-different result that IS on `main`: the >2-row blocks are the
    **TL kernel / Schur–Weyl row cap** (not "hidden information") —
    `QOU/QBeta/TraceBlindSector.lean` header, `qbeta_blind_sector_is_the_tl_kernel_probe.py`,
    bean `qou-i9gk` (completed). That is about `ω_λ = 0`, NOT about span rank.
  - Row cap / hook-content, citable on `main`: `schurPrincipal_eq_zero_iff`
    (`s_λ=0 ⟺ ℓ(λ)>r`, all n/λ/r, sorry-free), `wenzlLevel_conventionD`,
    `ocneanu_param_eq_of_fibre_qdim` (`z·[N]_q=q^N`),
    `computations/schurweyl/ocneanu_weight_general_n.py`,
    `docs/audits/2026-08-16-wenzl-level-family.md`. **Caveat:**
    `IsOcneanuWeightSystem` is class-carried with **no instance**.
  - Over-generalising an n=3 coincidence is a **named recurring defect** here:
    `qbeta_rank_one_identity_is_n3_only_probe.py` + PR #5337 (*"do not
    generalise the n=3 coincidence"*).
  - **Not classical from held sources.** Library has the p(n) side
    (`arxiv-2409.09372v4`: Irr is a basis of trace functions) and a BMW
    trace-space dimension (`arxiv-1403.4021v2`, ≤3), but **no rank = n**.
    **Wenzl 1988 (Invent. Math. 92) is cited in `references.ts` and NOT
    ingested** — the obvious place the classical statement would live.

## 2026-09-03 — six-strand two-nucleon exchange-sensitive invariant (bean `qou-brng`)

- **Does the corpus hold an EXCHANGE-SENSITIVE, real-valued, non-Markov-trace
  invariant of the six-strand two-nucleon link (`Δ₃,₃ = (σ₃σ₂σ₁)(σ₄σ₃σ₂)(σ₅σ₄σ₃)`
  in `B₆`) that could carry the T=0/T=1 ratio 33.7055?** → **GENUINELY OPEN on
  all six paths; the exchange operator itself is heavily worked.** 2026-09-03.
  - *Six-strand exchange spectrum (Markov-trace side, all closed scope-(a)):*
    `computations/probes/lifting_the_isospin_grading_to_six_strands_probe.py`
    (`de5c18f588`, bean `qou-r1yj` completed: cap 1 → 3/2, Pauli lock lost),
    `computations/probes/block_transposition_lift_probe.py` (`qou-brng`
    2026-09-02 §: all 11 blocks, `|λ| = q^k`, `k∈ℤ`, ceiling 9, k=0 only in
    ℓ(λ)≥3 blocks), `computations/block_swap_spectrum.py` (June: 22 distinct
    eigs at m=3,n=6, q→1 Sym²/Λ² labelling). Sign convention of `L` differs
    between r1yj and brng — do not "correct" one into the other.
  - *Closest existing exchange-sensitive REAL quantity:* `computations/
    block_swap_binding.py` → `block-swap-binding.witness.json`
    `binding_signal_log_Sfree_over_Satom` (⁴He, S₂×S₂ block swaps of 3-strand
    blocks; sign-only −0.43, averaged +0.277). It IS `tr_M(W·β_σ)`-derived, so
    fails the non-trace criterion.
  - *Topological/Vassiliev side:* `QOU/KnotTheory/Vassiliev/*` is component-
    count-agnostic scaffolding (`ChordDiagram n`, `IsFiniteType m`); the only
    link-valued datum is `BrunnianVassilievBridge.muBar_realized : ∃ val : K → ℤ`
    on the A-component Brunnian link, class-carried, **no instance**. No 6-component
    Milnor `μ̄(i₁…i_k)`, no pairwise/triple linking BETWEEN two baryon triples,
    anywhere in Lean/content/computations. `μ̄₁₂₃` (`StandardModel/
    SecondCrossingInvariant.lean:99-120`, `B : S → ℚ`, single-object) is
    channel-blind (`docs/audits/2026-09-03-two-mubars-selector-vs-magnitude.md`).
  - *T=0/T=1 discriminators held:* all are ALGEBRAIC (Hecke projectors `P±`,
    `y_(2)/y_(1,1)`, `InterfaceScalar.lean`, `isospin-singlet-binds-more.md`) or
    conditional colour-selection (`ColorFlavorIsospinSelection.lean`, class
    `InterfaceExchangeAntisymmetry` is `trivially_inhabited`). Deuteron owner
    ruling audit (`2026-08-29-deuteron-knot-owner-decision.md`) says nothing
    about the channel. The Milnor indeterminacy audit
    (`2026-08-29-gap2-he4-milnor-indeterminacy-exclusion.md`) is a scope-(b)
    prune for all-`lk=1` clusters — check whether the 6-strand two-nucleon link
    has `lk≠0` pairs before proposing higher `μ̄`.
  - **🛑 THAT GATE WAS RUN THE SAME DAY, AND IT CLOSES THE LINKING-DATA
    SUBCLASS — scope (b).** `computations/probes/two_nucleon_linking_matrix_
    channel_blind_probe.py`. Two corpus facts compose: (F1) the inter-nucleon
    `lk` **IS** `I₃` — `inter_nucleon_linked_channel.py` derives the arc as the
    Hopf link `T(2,2k)` (pp `+1`, nn `−1`, pn `0`, "NO numeric is tuned") and
    `u1_hypercharge_assignment.py:336` names the same datum *"I_3 =
    writhe/2-of-inter-nucleon-arc"*; (F2) Milnor indeterminacy, above.
    Composed: the `³S₁` (T=0) and `¹S₀` (T=1) np channels have the **same
    flavour content**, so `I₃ = 0` in both, so their linking matrices are
    **identical on all 15 pairs** (verified under both the single-arc and
    all-9-pairs readings). Every function of the linking data therefore gives
    asymmetry exactly **1**, against 33.7055. By-product: the tower is DEAD at
    `I₃ = ±1` (pp, nn: `ℤ/1`) and ALIVE only at `I₃ = 0` (np: `ℤ/0`) — where
    **both** channels sit, which is why surviving does not help.
    **So do NOT propose any higher `μ̄` / linking-integral route for the
    T=0/T=1 split** — including Evans–Berger nth-order linking below, which is
    inside this closed subclass. Still open: an invariant reading the braid word
    BEYOND its linking data, or a non-Milnor super-pairwise object.
  - **🛑 CORRECTION 2026-09-04 — the line above used to end "…or anything
    carrying SPIN (the same wall bean `qou-7zob` reaches from the flavour
    side)". SPIN IS NOT A ROUTE, and `qou-7zob` says so rather than agreeing
    with it — I cited a bean for the opposite of what it states.** In the
    S-wave Pauli LOCKS spin to isospin (`S=1 ⟺ T=0`, `S=0 ⟺ T=1`), so a
    Pauli-consistent interface carries a projector in each SU(2) with the roles
    exchanged and the same two scalars multiply to the same number:
    `QOU.QBeta.InterfaceScalar.separable_interface_degenerate`
    (`InterfaceScalar.lean:628`, sorry-free). Its docstring carries the sharper
    half — *"the conclusion holds for **every** `fSpace`, so no choice of space
    index rescues a separable interface"* — and the one surviving shape
    (non-separable `(S,L)` tensor coupling, bean `qou-vbyi`) is closed by
    `TensorCouplingCannotUnbindSinglet` (#6488). **The real residue is that
    theorem's own hypothesis**: `fSpin s1 = fIso t1`, `fSpin s0 = fIso t0` —
    the two SU(2)s carrying the SAME scalars is ASSUMED, not derived.
  - *Library:* higher (4th, nth-order) linking integrals + braid winding numbers
    are in `library/1992evansberger/ocr/page-007..011.txt` (**ocr/ only**;
    `sections/` is 437 B). Habegger–Masbaum 2000, Bar-Natan 1995, Birman–Lin
    1993, Meilhan–Yasuhara 2012, Milnor 1954/1957 are in `references.ts` and
    **NOT ingested** (INDEX.md 0 hits). No held source treats a 6-component link.

## 2026-09-04 — where the knot-complement ambient `S³` comes from (bean `qou-fxou`)

- **Is the Alexander–Markov ambient `S³` the same object as the gauge group
  `SU(2) ≅ S³`?** → **THREE objects share the glyph; the recorded corpus
  contradiction is a conflation, not a disagreement.** Audit:
  `docs/audits/2026-09-04-where-the-ambient-s3-comes-from.md`.
  - `S³_AM` — Alexander/Markov ambient: a **bare classical input**.
    `thm:jones-markov-trace` is pure `H_n(ℂ,q)` and names no 3-manifold; `S³` is
    a *hypothesis of the imported theorems*. Not the gauge group.
  - `S³_Reeb` — `def:reeb-bundle`, the link of the exceptional divisor, a circle
    bundle over `𝒮_p ≅ ℂP¹`. **Is** `SU(2)` structurally (Hopf = coset
    `SU(2)→SU(2)/U(1)`). The 2026-06-28 audit §(i) is right *about this one*.
  - `M_S` — `rem:brings-qou-4tuple` item 1, the unit circle bundle in `T*S` over
    Bring's **genus-4** surface. Carries `Θ` (Liouville restricted) hence the
    volume form — and is **provably NOT `S³`**: `b₁ = 8` vs `0`,
    `QOU/Eightfold/CircleBundleBettiObstruction.lean` (11 decls, lean-direct
    exit 0), scope-**(b)**, invariant = first Betti number via Gysin.
- **Does the corpus have a natural degree-3 volume form?** → **YES, prose-tier.**
  `Θ ∧ dΘ` named "the contact volume form" in
  `braids-and-knots/bar-involution-geometric-kac-sunada.md:1`,
  `stochastic-mechanics/bar-involution-table2-data.md:11`,
  `mass-theory/reeb-bundle.md:7`; `Θ ∧ (dΘ)ⁿ` is the measure of the q-YM-Levi
  action (`information-theory/gravitational-constant-properties.md:22`).
  **Zero Lean, zero `definition` block** — do not cite it as formalised.
- **The `sp₁ = Im ℍ` / tetraplectic route** → **already closed in the corpus**:
  `rem:tetraplectic-su2-gauge-reading` says in as many words that the triad is
  *the adjoint, not a 3-dim fundamental*; `quaternion-so3-motivation.md:13-18`
  says `Im ℍ` carries the `SO(3)` **rotation** rep. Real Frobenius–Schur type ⇒
  `Sym2GateFSTrichotomy.real_triple_fails_gate`. Fourth independent sighting of
  one invariant.

### TRAP added the same day — a bare-string grep declared a corpus-wide absence

The 2026-09-04 predecessor audit asserted *"`Sp(1)` appears in `library/` only,
never in `content/`"*. It is in **5** `content/` files. The grep used the bare
string `Sp(1)`; every occurrence is written `\mathrm{Sp}(1)`. One unknown
spelling ⇒ a confident corpus-wide absence claim. **When a topic-grep returns
zero, grep the LaTeX spelling too before writing "absent".**

## 2026-09-04 — the `ker Θ` rank contradiction, dim 7, and `J` on the contact distribution (bean `qou-xlw1`)

Audit: `docs/audits/2026-09-04-contact-distribution-complex-rank-and-dimension-seven.md`.

- **Is `H = ker Θ` rank 2 (`dim M_S = 3`) or rank 4 (`dim M = 5`)?** → **BOTH are
  DERIVED, from opposite halves; the outlier is the assumption one manifold
  carries both.** Scope-**(b)**, invariant = hypersurface-type parametrisation
  `dim = 2n+1`, `rank_ℝ H = 2n` (`ContactDistributionRank.realRank_succ`).
  - **TRAP — the site count answers this the WRONG way.** rank-4 is 2 sites
    (`archimedean-realisations.md:3`, `brings-qou-axiom-map.md:10`) against 9 at
    dim 3, so it reads as two typos. It is not: rank-4 is the **hypothesis of the
    whole archimedean chain** — no `Λ^±` splitting at rank 2, so no `F_A^+`, so
    the archimedean substrate parameter `q(p) = 1 + |⟨L_Θ,F_A^+⟩|` is ill-formed
    (17 `content/*.md` consume `F_A^+`). The Lean already gates on it:
    `models-of-qous/instanton.lean:85-100` and `self-dual-curvature.lean:38,47`
    take `cr.n = 2` / `dim_ℝ H = 4` as an **explicit hypothesis**;
    `CRManifoldData` (`CRRealisation.lean:27-56`) pins `n` nowhere.
  - `brings-qou-4tuple.md` carries both halves 19 lines apart (line 12 dim 3;
    line 31 the `F_A^+` formula). Also in that block: it says covering **degree
    3** while `brings-is-qou-verification.md:15` + `Elaboration.lean:151` say
    **4**, and Riemann–Hurwitz (`g=4`, `R=14`) gives 4.
  - `brings-qou-axiom-map.md:10` misquotes its own citation: `S_p ≅ ℂ²` where
    item 3 (`brings-qou-4tuple.md:18`, `c-quantum-universe.md:7`) says `ℙ¹(ℂ)`.
- **Any 7-dimensional object?** → **NO manifold anywhere.** `7-manifold` /
  `seven-manifold` / `4n+3` / `quaternionic contact` = 0 on all six paths. Three
  independent *pointers*: `form_stabilizer_genericity_su3_routes.py:21` (generic
  3-forms live in dim 7; only corpus `S^7` outside Mathlib), bean `qou-8p1g`
  ("go to `m ≥ 2`, real dim ≥ 8" — but its `Sp(3)/Sp(1)³` candidate is CLOSED,
  `quaternionic_flag_su3_exclusion.py`), and `qou-uq5x` (`S⁶ = G₂/SU(3)`).
  **Present and easy to miss: an SU(3)-Sasaki–Einstein `S⁵`**, built June 2026,
  living **only in `docs/audits/2026-06-16-s5so3-*`** — a `content/`-only grep
  misses it.
- **Does anything give `ker Θ` a complex structure?** → **YES, 7 prose sites, and
  the corpus explicitly identifies that `J` with the categorical `i`**
  (`q-deformed-commutator.md:1`, `linearisation-convention.md:1`,
  `heisenberg-commutator.md:1`, `substrate-radial-coordinate.md:7`,
  `i-as-braiding-orientation.md:4`, `commutative-crossing-energy.md:25`,
  `instanton.lean:87`). **No Lean carries it** — every `J` is a bare scalar
  (`J : K` / `J : R` / `J : ℝ`); `J² = −Id` is docstring-only. The identification
  `J_CR ↔ i·id_V` typechecks **only at rank 4**, so §3 is §1 from the other side.
  The one Lean `J² = −id` is `OctonionComplexStructure.Le_sq_eq_neg_id` on
  `Im 𝕆` — unconnected to `ker Θ`.
- **Path 5 (library, all four tiers incl. `ocr/`) is EMPTY for the entire CR /
  contact / Sasakian layer:** `Sasakian` 0, `CR manifold` 0, `pseudoconvex` 1,
  `7-manifold` 0, `quaternionic contact` 0 — while 34 `content/` files say "CR
  manifold". Nothing held to cite; closing it needs an upload (Boyer–Galicki;
  Dragomir–Tomassini; Bryant). **Bare `sasaki` matches 5 section files — all
  surnames in bibliographies.** Grep `Sasakian`, not `Sasaki`.
- **Path 6 EMPTY** for `Levi distribution` / `ker Θ` / `contact distribution` /
  `Levi form` / `CR complex structure`. No bean has ever worked this.
- **Live constraint on the step AFTER the rank question:**
  `docs/coordination/s5-so3-keystone.md:31,47,51` — no compact / finite-dim
  Sasakian arena can host `W_λ` (`q₀` real > 1, not a root of unity). Scope
  **(a)** against a 7-dim contact route: different construction, must be re-run.

## 2026-09-04 — the hyperbolic volume as a QOU structure (bean `qou-xlw1`)

Audit: `docs/audits/2026-09-04-how-the-hyperbolic-volume-could-arise-from-qou.md`.

- **Is the hyperbolic volume "imported, not a QOU structure"?** → **NO, and that
  claim was MINE and is RETRACTED.** ~180 QOU `.lean` files on this layer;
  `Archimedean/HyperbolicMetric.lean` builds `dH` on `H³` from path lengths
  (sorry-free isometry engine); `MathlibExt/IdealTriangulation.lean` (sorry-free)
  has `IdealTetrahedron`, `volume_eq_lob_sum`, `param_im_pos`, `param_prod = −1`,
  `SatisfiesEdgeEquations`. **`figure-eight-kashaev-volume.witness.json` is
  `verdict: CONFIRMED`** — Richardson 2.03017614 vs `2·Cl₂(π/3)`, err 2.93e-4.
  SnapPy 3.3.2 really runs (`snappy-cusp-seeding.witness.json`, 45 ms).
- **Route tiers:** L1 poles **T0**; L2 pole↔cusp / L3 cusp-completeness / L5
  volume conjecture **T3** (class, no instance); L4 Archimedean limit **T1+T2**.
  Top-level route statement `brings-surface/thurston-relaxation.md:7-11` is a
  **`prose` block** — programme, not result. Stated for the `Φ_q`-piece **`K_S`
  only**, never general knots.
- **🛑 WEAKEST LINK, and it is a TYPE:** `algebraic-geometric-dilog-equivalence.lean:44`
  has `opaque BlochWignerD : ℝ → ℝ` and `class …(q x : ℝ)`, so the shape parameter
  is **real** — but the corpus PROVES `D` vanishes on ℝ
  (`MassTheory/BlochVolumeLegFlatVanishing.lean:111 eq_zero_of_conjAntisymm_ofReal`,
  sorry-free). Honest instantiation forces `volume = 0`. Not a live contradiction
  (`opaque`; the theorem is `ℂ → ℝ` and unwired). Fix is a **re-typing** to
  `Im z > 0`, reusing `IdealTetrahedron.param`. Scope **(a)**.
- **🛑 Claim-shape:** `pole_cusp_bijection_proved` (`:124`) contains **no cusp and
  no bijection** — it exhibits `n` roots of `(x;q)_n`. The file's prose is honest;
  the NAME is what gets cited.
- **Bring's surface DOES have its hyperbolic structure used** —
  `Archimedean/EmCouplingBringZeroMode.lean`, sorry-free: (2,4,5) triangle,
  240 triangles, area `12π`, `χ=−6`, `g=4`, `b₁=8`, `b₁/Area = 2/(3π)`. **But it
  is ARITHMETIC in geometric clothing** (`gaussBonnetArea` is a `def`; the proofs
  are `ring`). Three facts assumed in docstrings / absent: (B1) area = angle
  defect, (B2) the 240, (B3) `B ≅ ℍ²/Γ` — **B3 absent from the whole corpus.**
  Mathlib's `UpperHalfPlane` is **never imported** by QOU.
- **The source for B1–B3 IS HELD and is cited for a DIFFERENT section:**
  `library/pjm-v154-n1-p09-s/sections/sec-001-2-the-universal-cover-of-brings-curve-if-b-b-is.md`
  (Riera–Rodríguez 1992 §2, pp. 2–8) gives `Γ*` = (2,4,5) triangle group,
  `φ: Γ*→S₅`, `Γ = ker φ` torsion-free, **`B = Δ/Γ` genus 4** — and `[Γ*:Γ]=120`
  × 2 triangles = the corpus's unsourced `240`. `references.ts:9012` cites this
  paper for its **period matrix** only. Held **twice**
  (`the-period-matrix-of-bring-s-curve-1hik02mwva`, `duplicate_of`) and **absent
  from `library-duplicate-ledger.json`**. Second Fuchsian route also held:
  `arxiv-2402.08782v1` (Bring via Hecke group `H₃`).
- **GENUINELY OPEN on all six paths: the `ℍ²`(Bring) ↔ `H³`(knot complement)
  link.** `.beans/` = **0** for `Gauss-Bonnet`, `triangle group`, `(2,4,5)`,
  `systole`, `uniformis`. No agent has ever worked it. Scope **(a)** — path 0 was
  down.
- **Smallest honest Lean:** NOT Gauss–Bonnet arithmetic (already T0, re-deriving
  is the trap). Best target is the **re-typing** above; next is `qou-idvt`'s live
  T1–T4 Lobachevsky/concavity ladder (in-progress — do not re-scope).

## 2026-09-04 — the CITATION gap on the hyperbolic-volume / eightfold arc (epic `qou-8lxd`)

Audit: `docs/audits/2026-09-04-citation-gap-inventory.md`. 15 beans, all parented
to `qou-8lxd`. Answers most "is X sourced?" questions on this arc without a sweep.

**Held and clean (H) — do not re-check:** Kashaev 1997 (`arxiv-q-alg-9601025v2`,
73 citers) and 1995; Ohtsuki 2016 (`104171-qt-83`); Andersen-Hansen 2006
(`arxiv-math-0506456v1`); **Neumann-Zagier 1985** — held 3x (one work), registered
with `alternates`, cited in 63 files, duplication recorded in front-matter AND
`references.ts` AND by INDEX.md giving the copies no row; **Fulton-Harris 1991** —
registered w/ ISBN+DOI, `verified-clean`, NOT held (fine: textbooks are registered
without PDFs), and the FS trichotomy enters Lean as a **parameter**
(`fs : ℕ → FSType`, `Sym2GateFSTrichotomy.lean:103`), not an assertion;
**Woronowicz 3D left-covariant calculus** — `woronowicz1987-twisted-su2` IS cited
(`brings-is-qou-proof.md:11,15`, `connection-su2.ts`). *That last one I nearly
filed as uncited off the sibling block; check the PROOF block before the
VERIFICATION block.*

**Not held (U), named works:** Murakami-Murakami 2001 Acta 186 (**63 citers**,
the single highest-leverage upload); every Woronowicz differential-calculus paper
(`library/` has **0** files containing the phrase "differential calculus");
Bryant 1987 / Hitchin 2000 (generic-3-form `G₂` — `baez2002` is cited there and
does **not** contain it); Butruille 2005 / Gray / Fernandez-Gray; and the whole
**CR/contact/Sasakian layer — 0 held AND 0 registered across 828 `references.ts`
entries**, against 34 `content/` files and 10 blocks with no `cites` field at all.
Cheapest adequate CR source is **Blair** (Darboux, `dim = 2n+1`), not Boyer-Galicki.

**No reference key exists at all for:** Riemann-Hurwitz, Gauss-Bonnet. Both are
used as arithmetic (`CoveringDegreeRamification.lean:88-91` says outright it is
"a definition encoding Riemann-Hurwitz ... not a proof"). Held sources exist for
both — cheapest fix cites the already-registered `s40879-023-00706-0`
(Braden-Disney-Hogg, *Bring's curve: old and new*).

**Riera-Rodriguez §2** (the (2,4,5) triangle group, `B = Δ/Γ`, `[Γ*:Γ]=120` ⇒ the
corpus's unsourced **240**) is still uncited at `EmCouplingBringZeroMode.lean`.
Existing beans `qou-3q4q`/`qou-fkmt` cover *other* sections of the same paper —
and both name the `duplicate_of` copy rather than `pjm-v154-n1-p09-s`.

**CORRECTION I OWE:** my 2026-09-04 audit called the duplicate ledger
"under-counting" for omitting the Riera pair. Wrong framing — the ledger holds
**4 hand-adjudicated DETECTOR MISSES**; machine-detected duplicates live in
section front-matter (**23 dirs**) and in `references.ts` `alternates`. The Riera
pair is in both. Nothing under-counts.

**Second correction:** `grep -c '\bsorry\b'` reports 1-4 in five arc Lean files and
**every match is the string "sorry-free" in prose** or a commented-out instance.
The arc is sorry-free. Had it not been, the zero-`-- Ref:` finding would be an
AGENTS.md §1 violation instead of a gap that *falls through* §1 — which is the
whole point of bean `qou-3o59`.

**Unmeasured, worth a bean if wanted:** a systematic `library/<docId>` ↔
`references.ts library.docId` reconciliation. 828 entries / 394 with docId / 576
dirs / 23 duplicates — the residual is **not** 182 and was never measured.
`library/0803219` was found incidentally.

## Tower-series divergence near a singularity (resolved 2026-09-06)
STABLE. "Is the tower series divergent / where is the singularity" has carriers; do not re-declare open.
Hecke n-tower binding period `a_D^(n)=S(n)/n`: Gevrey-1/2 at q=1 (Lean `QOU/Mass/BindingGevreyHalf.lean`),
level-1/2 Borel singularity ξ=1/√2 real positive, non-polar (`docs/audits/2026-07-12-alien-calculus-review-binding-gevrey-half.md` §3,
`computations/lever1_borel_half_singularity_probe.py`); at q₀ q-Gevrey ~q₀^{n²}, q-Borel radius ≈0.955
(`deltalambda/deuteron-wall-qborel-resummation.witness.json`); deuteron-wall resummation REOPENED `qou-hok7`.
Ohtsuki κ-tower: Gevrey-1, singularity Vol(4₁)/π≈0.646, Stokes 3. c_k D-ladder: CONVERGENT (three reversals; do not re-run).
A→∞ nuclear tower series: unwritten (survey 2026-09-05 §7g). Brane-tower "divergence" = plateau in σ⁻¹ chain length (`qou-20yf`), bean `km42` wording stale.
TRAP: the 2026-09-05 survey §7g (pre-correction) cited the Gevrey result to AlgebraicSubstrate/{KernelGrowthBound,DominationTowers,PolyhedralDomination}; it lives in QOU/Mass/BindingGevreyHalf.lean.

## 2026-09-06 — hyperbolic surface law `S/V → 2` in `H³`, Yekutieli kites, surface term (bean `qou-j8hp`)

- **Has anyone computed/tested `S/V → 2`, `A_surf/A → const`, or a `(ln A)/A` surface correction?**
  → **GENUINELY OPEN (grep-open; path 0 down).** The `ln A` *separation law* IS in the corpus, but only
  as the Coulomb-pairing radius, never as a surface law: `2026-08-25-em-linking-o2-neutrality-applied-to-kappa-contest.md:326-343`
  + `em_linking_alpha_scaling_provenance_probe.py:170` + witness `law_scores` (`ln A` 9.253 % vs `A^{1/3}` 3.505 %),
  restated `sm-26-parameter-chip-away.md:193-201`, `sm-eightfold-derivation-cheat-sheet.md:486`,
  `observations/bw-mass-decomposition-dictionary.md:10`. Sinh-ball VOLUME `π(sinh 2R − 2R)` is stated (prose + probe string);
  the AREA `4π sinh² R` and the ratio appear nowhere. Zero Lean on hyperbolic ball volume/area
  (`Real.sinh` only in `FaddeevPhiBRealIntegral.lean`; `HyperbolicMetric.lean` has `dx dy dz/z³` only).
- **Kites**: three homonyms. (i) Yekutieli's 2-cell (`library/arxiv-1007.1250v4` Def 4.1.1: string `σ` + linear square `τ`;
  `4^k` square kites per binary tessellation `tes_k I²`) — worked to a verdict in bean `qou-20bk` (completed 2026-09-06) +
  `LiftingDescent/CrossedModuleSurfaceHolonomy.lean` (sorry-free): no 2-dim Yekutieli object carries a non-abelian 3-body term;
  the only 3-body object is `∫γ` over a balloon (Thm 8.6.6). (ii) "kite-tail" `(1+r²)^k` cyclotomic factor of `tr_M`
  (`docs/audits/2026-05-09-kite-tail-reconciliation.md`, `computations/_deprecated/kite_tail_*`) — a braid triangle `σᵢσⱼσᵢ`, NOT Yekutieli.
  (iii) nothing Penrose/Ptolemy. **Nobody counts kites as a function of A.** "surface of kites" has no corpus meaning.
- **Stokes surface term**: `2026-08-30-nonabelian-stokes-and-the-surface-term.md` — bad set `|bad(τ,k)| ≤ a₀ + a₁·2^k`
  (perimeter count, singular points of `σ`); shape only, no magnitude. Lean shadow: `AffineCountIsNotASurfaceTerm.lean`
  (affine count ≠ `A^{2/3}`), `Sigma1CubedSeifertTessellation.lean` (abelian shadow trivial). No Lean on the singular-locus count.
- **Library**: Yekutieli surfaces HELD (`arxiv-1007.1250v4`, one 261 KB section file, key `yekutieli2015`); ALL cited Yekutieli
  keys held since 2026-09-05 (`qou-3pck`). Hyperbolic ball volume HELD in **`arxiv-1010.5321v3` *Formulas on hyperbolic volume*
  §3.1 Bolyai** `πk³ sinh(2x/k) − 2πk²x` (registered, line ~11661). Ratcliffe / Benedetti–Petronio / Weizsäcker / Bethe1936
  REGISTERED-ONLY; Martelli, Harborth, Bezdek ABSENT (639 dirs); `library/18` (ball-packing rigidity) cites Kuperberg–Schramm
  only. Thurston held copy = Ch 1–2, has hyperbolic trig but no ball volume. Isoperimetric/Cheeger hits are all probability
  (Stein kernels, concentration) — no hyperbolic isoperimetry held.
- **Q5**: no bean/audit tries or rules out a hyperbolic surface law. The coordination-graph Lean is explicitly Euclidean:
  `EquilateralBound.lean:2-3,34` (ℝ³), `MaxContactSimplex.lean:184` (kissing 12), `qou-usft` RESULT 6 ("ENTIRE nuclear
  EM-sector geometry is two lines of classical Euclidean"). Not a refutation of an `H³` cluster — an unexamined import, same class as `A^{1/3}`.
