# Organic-chemistry redo — workplan (2026-06-08)

PR [#1994](https://github.com/litlfred/qou/pull/1994) ·
branch `claude/affectionate-hopper-seYEv` ·
audit [`docs/audits/2026-06-08-organic-chem-redo-audit.md`](../audits/2026-06-08-organic-chem-redo-audit.md).

## Goal

Redo organic chemistry on the now-proved universal-ILP/Wedderburn chain,
with **benzene** as centerpiece: a **γγ-from-light assembly spine**,
a **general (non-post-justified) molecular projector**, a fixed and
witness-pinned compute layer, and an n-hexane comparison.

## Decisions locked (owner, 2026-06-08)

1. **γγ is always the start.** Chain existing propositions:
   Breit–Wheeler `γγ→e⁺e⁻` → `q q̄` → Borromean nucleons → atoms →
   molecules. Thermal rearrangement is a secondary "reactor" overlay.
2. **Bond order = LP-dual active-set k** (= # saturated channels).
3. **Reconcile the two chemistry chapters**; retire the disconnected
   Alexander/link path where it conflicts with the ILP/Wedderburn chain.
4. **No hardcoded constants** — witness-pin every numeric literal.
5. **General-before-special**: define the molecular projector from
   symmetry-group factorization (parabolic Hecke subalgebra), with
   benzene a derived special case — never the motivating example.

## Dependencies owned by siblings (consume, do NOT duplicate)

A≥3 binding closure (carbon = A=12 is on the benzene critical path) is
**actively owned** by a sibling cluster — verified 2026-06-08:

| PR | Scope |
|----|-------|
| [#1839](https://github.com/litlfred/qou/pull/1839) | Residue-A (SW-residue) kernel — the A≥3 body-order series |
| [#1933](https://github.com/litlfred/qou/pull/1933) | GAP-A-4 T17 Schur–Weyl R-matrix — first categorical χ derivation |
| [#1942](https://github.com/litlfred/qou/pull/1942) | `prop:borromean-h4-categorical-derivation` (H₄ chain) |
| [#1975](https://github.com/litlfred/qou/pull/1975) | GAP-A-4 icosahedral / non-Schur-Weyl refutation |
| [#1808](https://github.com/litlfred/qou/pull/1808) | H₃→H₄ jump (Markov stabilization) |
| [#1762](https://github.com/litlfred/qou/pull/1762) | 1ppQ roadmap / binding attack-plan hub |

**Conclusion for owner's "if A>3 not active, work on it too":** it *is*
active. This PR **consumes** the A≥3 result for the carbon atom rather
than re-deriving it. Per owner directive, assume it lands; coordinate.

## Workstreams (ordered)

### WS-A — Compute hygiene (FIRST; independent, high value)
Inventory verdict: no chemistry script routes through the canonical
`lp_dual_solver.py`; several hardcode constants and roll their own
`hecke_mul`.

- [x] A1. `h2-molecular-binding.py`: dropped vestigial `m_e_MeV`/`G`/
  `alpha_bind` (dead nuclear scale; eV conversion uses derived `E_MOL`).
  Behavior-preserving; D₀(H₂)=4.6231 eV (NF-enum). Commit 14358b95.
- [x] A2. `molecular-frobenius-lp.py` routed through
  `solve_operator_selection_lp(TR_M, G, n_target)`; witness now emits
  `y0_star`/`y_star`/`active_set`/`duality_gap`, strong duality gap
  1.27e-15. Commit 34dc2f13.
- [x] A2-CO. New falsifiable probe `co_bond_order_active_set.py`
  (commit e185e7c9). **FINDING:** the interleaved single-chain model
  gives active-set = **1** (only σ binds; π pairs anti-bind via
  ee-repulsion). This **falsifies** `co-lp-dual-binding.md`'s one-chain
  decreasing-positive-marginal mechanism. Correct topology = 3
  ORTHOGONAL orbital channels (σ⊥πₓ⊥π_y) → bond order = # orthogonal
  channels (→ WS-F2). Did NOT bake in 3 (no fabricated valence cap).
- [~] A3. **DEFERRED — infra-dependent.** Clean form = route scripts
  through `pyhecke.molecular`, but that module's import chain
  (`qou_substrate` via `pyhecke.gram` + a bare `hecke_core` from the
  `substrate/` subdir) isn't cleanly resolvable without package-install
  wiring. Per owner "assume compute infra will land" — defer until the
  package paths land (sibling #1062), then swap + equivalence-check.
- [ ] A4. Create backing computes for `ch4`/`co2`/`ilp-covalent`
  (currently theory-only .md) + witnesses. (CO now has A2-CO.)
- [ ] A5. Run `lp_dual_witness_validator.py`; chemistry witnesses green.

### WS-B — De-hardcode `.md` constants → witness-pin
~25 bare literals flagged (193–386, 200–400, 150 kJ/mol; 11.09, 8.28,
3.21, 3.60, 0.2083… eV). Each becomes a `:val[…]{witness=…}` (or `.ts`
`cites`/witnessRef) pointing at a WS-A witness.

- [ ] B1. molecular-construction LP-dual files.
- [ ] B2. organic-chemistry Alexander/barrier tables.

### WS-C — General molecular projector + Lean (the anti-post-justification deliverable)
Define the projector from symmetry **before** benzene.

- [ ] C1. `def:molecular-strand-partition` — λ=(n₁,…,n_k)⊢N for a
  k-sub-unit composite.
- [ ] C2. `def:parabolic-hecke-subalgebra` — H_λ(q)=⊗H_{nᵢ}(q) ↪ H_N(q).
- [ ] C3. `def:molecular-assembly-projector` + `prop:assembly-projector-exists`
  — canonical projector onto each Wedderburn block per λ (provable Hecke
  theory; **Lean-provable, not conjectural**). Delocalization = symmetric block.
- [ ] C4. `ex:benzene-symmetric-projector` — λ=(2,2,2)⊢6 (3 acetylenes),
  C₆/D₆ closure; benzene as the derived case.
- [ ] C5. Non-post-justification check: same defn reproduces CH₄/CO₂
  projectors with no foreknowledge.
- **Numerology guard:** the projector lives in **H₆(q)** (6 carbons);
  the "120 strands" is an atom count, *not* |S₅|=120 — do not match it
  to a group order.

### WS-D — γγ-from-light assembly spine
- [ ] D1. `def:` light→atom chain reusing `breit-wheeler-pair-production`,
  `quark-antiquark-production`, `meson-to-proton-via-borromean`.
- [ ] D2. atom→acetylene (C₂H₂): triple bond = LP-dual k=3 covalent op.
- [ ] D3. acetylene→benzene: 2×C₂H₂→C₄H₄ intermediate → +C₂H₂ → C₆H₆,
  ring closure via WS-C projector. (Note: owner's "C4H8/C6H12" are the
  *saturated* cousins; benzene path is C₄H₄→C₆H₆, no added H. Offer
  cyclohexane C₆H₁₂ as the saturated-ring comparison.)
- [ ] D4. Shortest-production (GB/birthday) framing — claim
  "unique up to molecular symmetry, canonicalized by min-action SDP"
  (retrosynthesis is non-unique).
- [ ] D5. Net-emission ledger `(NF-net_final − NF-net_initial)·𝔈₀`;
  photon channel categorical, phonon channel archimedean (partial ledger).

### WS-E — SDP active-set = bond order; extend to magic/shells
- [ ] E1. Witness probe: read LP/SDP active-set cardinality for CO/CO₂
  bonds; confirm = bond order (3/2). Discharge the integrality caveat
  (`conj:q-integer-mass-formula`) or flag it.
- [ ] E2. Same probe on the confinement SDP at closed shells — does the
  active-set yield nuclear magic (2,8,20,28,50,82,126) and electron-shell
  (2,8,18,32) numbers?

### WS-F — Reconcile the two chapters
- [ ] F1. Decide bond primitive (link vs knot) — molecular-construction's
  knot/ILP wins (it's wired + validated); migrate organic-chemistry's
  Alexander/link bonds or scope them as a complementary view with an
  explicit consistency proposition.
- [ ] F2. **Correct `co-lp-dual-binding.md`** (surfaced by A2-CO probe):
  its triple-bond mechanism ("one chain, decreasing-but-positive
  marginals") is falsified — a single chain binds only σ. Rewrite to the
  ORTHOGONAL-channel model (σ⊥πₓ⊥π_y independent ~H₂-like channels; bond
  order = # orthogonal channels, valence-limited). Note it is "conditional
  on `conj:q-integer-mass-formula`" — frame the correction accordingly.

### WS-G — Heat-as-probability / catalysis (research leg, one simple case)
- [ ] G1. Markov-trace-as-partition-function framing; T via Boltzmann
  weight on birthday grading; catalyst = lowers peak-birthday of desired
  pathway. Validate selectivity (benzene vs hexane) against real yields.
  *Lowest priority; most ambitious.*

## Validation gates (every commit touching content/compute)
`bun run validate quantum-observable-universe`; LP-dual witness validator;
witnessed-values (no bare literals); conjectural-propagation audit on new
provable blocks.

## Review triage (PR #1994, 2026-06-08)
- Gemini (H₁₂₀→H₆): accept-with-modification — H₁₂₀ is the correct full
  120-strand braid; clarified cell to show H₁₂₀ full + H₆ π-system.
- Copilot (line 22 `rev-parse`): accept — prefixed `git`, fixed reporting.
- Copilot overview: no action.
