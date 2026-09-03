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
    BEYOND its linking data, a non-Milnor super-pairwise object, or anything
    carrying SPIN (the same wall bean `qou-7zob` reaches from the flavour side).
  - *Library:* higher (4th, nth-order) linking integrals + braid winding numbers
    are in `library/1992evansberger/ocr/page-007..011.txt` (**ocr/ only**;
    `sections/` is 437 B). Habegger–Masbaum 2000, Bar-Natan 1995, Birman–Lin
    1993, Meilhan–Yasuhara 2012, Milnor 1954/1957 are in `references.ts` and
    **NOT ingested** (INDEX.md 0 hits). No held source treats a 6-component link.
