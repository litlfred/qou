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
