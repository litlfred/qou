# Per-basis-element structural invariants — α_EM is one of six (scoping, 2026-06-09)

> **Author question (2026-06-09).** "Habiro object is the fundamental-rep
> fermion-loop unknot — there is derivation cheat sheet. Would be
> interesting to walk this all the way through. See where the unknot
> plays a role at each step. Do those for the other 6 knot-operator
> basis elements (and/or Gram inverse) as a table. Are there other
> FSC-like things that emerge? … Structural invariants across
> Cat → Alg → Geom → Arch → Phys. Noether structural
> constants/relations? Anything in the literature? May help simplify
> proofs and compute/caching."

This doc scopes the answer. **It does NOT close anything new.** It
shows the existing infrastructure already determines a per-basis-element
family of six structural invariants — α_EM is the row-1 (unknot)
instance — and lays out cheap decisive experiments to identify the
other five.

## 1. The 6-element basis is already canonical

The Gröbner–Shirshov NF basis of `H_3(q)` on three strands is

`{ 1, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀ }`

with the particle dictionary established in
[`appendix-knot-operations-archimedean/particle-nf-table.md`](../../content/quantum-observable-universe/appendix-knot-operations-archimedean/particle-nf-table.md):

| # | Hecke element | NF symbol | Knot type | Particle |
|---|---|---|---|---|
| 1 | `1` | γ | unknot | photon |
| 2 | `σ₀` | σ₀ | single +crossing | u-quark / σ₀-channel |
| 3 | `σ₁` | σ₁ | single +crossing | partner |
| 4 | `σ₀σ₁` | L₊ | Hopf+ link | gluon₊ |
| 5 | `σ₁σ₀` | L₋ | Hopf− link | gluon₋ |
| 6 | `σ₀σ₁σ₀` | e⁻ | trefoil T(2,3) | electron |

The full multiplication table is in
[`appendix-knot-operations/knot-operator-basis-table.md`](../../content/quantum-observable-universe/appendix-knot-operations/knot-operator-basis-table.md)
(36 pairs × every torus operator T(m,n), exact in `h = q − q⁻¹`).

## 2. The cross-pipeline table — each row × each chain stage

The canonical derivation chain
([`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md))
runs Cat → Alg → Geom → Arch → Phys. Each of the 6 basis elements
appears at every stage:

| Stage | Universal object | Per-row instance | Observable handle |
|---|---|---|---|
| **Cat** (step 1–2) | `H_n(q) ↷ V^⊗n` via R-matrix; Yekutieli–Stokes for σ² = hσ + 1 | `b_i` as morphism in `H_3(q)` | block decomposition `⊕_λ M_{d_λ}` |
| **Alg** (step 3–6) | Markov trace `τ`; Frobenius pairing `⟨a,b⟩_F = τ(ab)`; Gram matrix `G_{ij}=τ(b_i b_j⁻¹)` | `τ(b_i)`: `1, z, z, z², z², hz²+z` | Wedderburn block content |
| **Geom** (step 4) | Bring χ=−6 surface ↔ 6 torus-knot basis (Bring–Klein correspondence) | unknot / Hopf / trefoil knot type for `b_i` | Vol(K), CS invariant, Jones poly J(b_i)(q) |
| **Arch** (step 9) | `τ: 𝐂 → Arch` evaluates at `q = q₀` (real) | numerical row of `G(q₀)`, `G⁻¹(q₀)` | Hoefsmit `b`, Reeb `z`, Hopf `[2]_q` at `q₀` |
| **Phys** (step 10–11) | Confinement SDP + Q-value extraction | particle identity + coupling | **per-row dimensionless coupling** |

The diagonal of `G(q₀)` and `G⁻¹(q₀)` is **the natural family of
6 dimensionless invariants** — one per basis row.

## 3. The FSC-like family — α_EM is row 1

From [`mass-theory/gram-matrix-spectral-connection.md`](../../content/quantum-observable-universe/mass-theory/gram-matrix-spectral-connection.md),
in the central-idempotent basis the Gram inverse is

```
G⁻¹_{λ,μ} = δ_{λμ} · [n]_q! / (dim_q(λ) · dim(λ))
```

Summing the diagonal gives the **Frobenius co-Casimir** `Σ_λ 1/dim_q(λ)`,
which is the trace identity proved in
[`thm:frobenius-codim-universal`](../../content/quantum-observable-universe/mass-theory/frobenius-codim-universal.md).
Each term in the sum is a single basis-row's structural shadow price.

**Per-row shadow prices** (the LP-duals `y_i*` from
[`prop:operator-selection-lp`](../../content/quantum-observable-universe/mass-theory/knot-operator-lp-selection.md)
= `prop:knot-operator-lp-selection`) are dimensionless q-rational
functions; at `q = q₀` they collapse to real numbers. **These ARE the
"FSC-like structural invariants" the question asks about.**

**Row 1 — unknot / γ — is α_EM.** PR #1521 identified the Habiro
element `[2]_q · (1 − h²α)` as the **closed fermion-loop unknot in
fundamental SU_q(2) rep** with `1/(8π) = 1/(π · dim H¹(M_Bring))`.
This is the row-1 instance of the per-basis structural invariant.

**Rows 2–6 — open identification.** The framework predicts five
analogous per-row structural couplings. Candidate observable handles:

| Row | Hecke | Knot | Particle | Candidate α-analog (OPEN — to be tested) |
|---|---|---|---|---|
| 1 | `1` | unknot | γ | **α_EM** ✓ identified (#1511 + #1521) |
| 2 | `σ₀` | single-crossing | σ₀-channel / u | strong-channel coupling at single crossing? `α_s` candidate, OPEN |
| 3 | `σ₁` | single-crossing | partner | mirror of row 2; chirality-paired? OPEN |
| 4 | `σ₀σ₁` | Hopf₊ | gluon₊ | 2-strand coupling, possibly `α_w` or weak iso-coupling; ratio Z/H scale lives here per electroweak triplet, OPEN |
| 5 | `σ₁σ₀` | Hopf₋ | gluon₋ | mirror of row 4; LP-active edge per `knot-operator-lp-selection.md` for p/n confinement, OPEN |
| 6 | `σ₀σ₁σ₀` | trefoil T(2,3) | e⁻ | "universal pair-production operator"; possibly `m_e/m_p` Yukawa-like dimensionless ratio, OPEN |

**The framework's prediction:** if α_EM is row 1, then the SM's
running couplings + dimensionless mass ratios should organise as
**six (not three) per-row structural invariants** from the same
H_3(q)-Gram-inverse diagonal, with the SM's three gauge couplings
appearing as specific row-combinations rather than as fundamental.

**Status assessment.** This is a *structural prediction*, not a
derivation. Treating it as a coupling-constant identification before
each row's α-analog has been independently identified would repeat the
c_k flip-flop pattern (q₀-dependent near-match wired as derivation).
The discipline lock applies: identify Taylor-exactly per row, OR mark
as cal-anchored, OR don't wire.

## 4. Cheap decisive experiments (one per row, ~1 day each)

For each row `i = 2..6`, the same template that identified α_EM as
row 1 (`alpha_em_habiro_categorical_1loop_identification.py`,
PR #1521) can be applied:

| Exp | Row | Test | Pass ⟹ | Fail ⟹ |
|---|---|---|---|---|
| 1 | 2 (σ₀) | does `τ(σ₀² · α) = z·(hz+1)·α` reproduce a known dimensionless SM coupling at q₀? | row-2 α-analog identified | row 2 has no SM-coupling analog at this level |
| 2 | 3 (σ₁) | mirror of exp 1 with σ₁ | confirm chirality pairing | independent of row 2 |
| 3 | 4 (L₊) | does `J_2(Hopf₊)(q₀)` give a dimensionless coupling matching `α_s` or `α_w`? | weak/strong row identified | other identification needed |
| 4 | 5 (L₋) | mirror of exp 3 | chirality pair | independent |
| 5 | 6 (e⁻) | does `J_2(trefoil)(q₀) / J_2(unknot)(q₀)` give `m_e/m_p` or `α_em/α_w`? | electron-row coupling | other identification |

Each experiment is bounded (~1 day) and decisive (q₀-stability test
across the muon-pin and m_p-pin q₀ rules a candidate in or out the
same way item-1/item-2 ruled mechanisms in/out for the Q_β bridge).

## 5. Optimization / caching implications

If the per-row α-family is real, the framework gains a **basis-aligned
cache architecture**:

1. **6-element cache (not per-knot, not per-particle).** Currently
   `vol_density_per_block` is cached per knot K; mass scripts iterate
   per atom. A 6-element basis-row cache replaces both: every
   per-knot or per-atom compute decomposes into a sum of six
   basis-row contributions, each cached once at `q₀`.

2. **S_3 symmetry exploitation.** Rows 2 ↔ 3 (σ₀ ↔ σ₁) and
   4 ↔ 5 (L₊ ↔ L₋) are S_3-symmetric pairs (single transposition
   ↔ mirror; positive ↔ negative Hopf). Caching one of each pair
   halves the effective basis size.

3. **Gram-inverse precompute once.** `G⁻¹(q₀)` is a 6×6 matrix of
   q-rationals; computed once it serves every downstream LP/SDP
   operator-selection problem (proton, neutron, deuteron, every
   EW carrier). Currently witness emission for each compute
   re-derives.

4. **Proof simplification.** Theorems of the form "an observable
   factors through `H_3(q)` Frobenius pairing" can be stated row-by-row
   instead of per-operator. The §3b-cond conditional classes can be
   re-parametrised: one class per basis row (6 total) replaces the
   per-observable proliferation (~30 currently).

## 6. Noether-style framing

Each basis-row invariant `y_i*` is a **conserved quantity associated
with a symmetry** in a precise sense:

- The basis-row index is preserved by the Hecke relation σ² = hσ + 1
  (the relation closes the basis under multiplication, with the
  multiplication table being the basis-row symmetry data).
- The Frobenius pairing `⟨·,·⟩_F` is the conserved bilinear form;
  Noether's theorem in the categorical setting (Müger 2003,
  Etingof–Nikshych–Ostrik 2005 on fusion categories) associates a
  conserved per-row "dimension" with each simple object.
- The 6 rows correspond to the 6 simple objects of the irreducible-
  module category of `H_3(q)` (NOT the same as the 3 Wedderburn
  blocks of H_3 over ℚ(q); the basis size 6 = |S_3|, the partition
  count is 3 — the basis-vs-block distinction is itself a structural
  observation).

So the 6 invariants are *Noether-like* in the categorical-conservation
sense.

### Refinement from the 2026-06-09 probe run

`per_basis_row_invariants_probe.py` extracted all 6 basis rows' τ + Gram-diagonal at canonical q₀. Two sharper structural facts than the scoping above:

1. **The 6 basis rows collapse to 3 Wedderburn blocks** with quantum dimensions `(3) → 1`, `(2,1) → [2]_q`, `(1,1,1) → 1`. The `G⁻¹_diag` values per block are `[3]_q! / 1`, `[3]_q! / (2·[2]_q)`, `[3]_q! / 1` — so at q₀ there are only **2 distinct numerical G⁻¹_diag values** (6.120579 and 1.521853), not 6. Rows γ and e⁻ are in the two 1-dim blocks and share `[3]_q!`; rows σ₀, σ₁, L₊, L₋ all sit in the (2,1) block and share the second value.

   This means the "6 dimensionless coupling constants" framing in §3 is too coarse-grained: at the Wedderburn level, the per-block invariants are only **2** distinct (matching the 3-block structure with the 2 trivial blocks degenerate). The 6-fold count comes from counting Markov traces `τ(b_i)` per basis row, where the values are 1, z, z, z², z², hz²+z — five distinct numerical values, six basis indices.

   Implication for §5 caching: the basis-aligned cache is even smaller than claimed — exploit the **block-level** symmetry, not just the S_3 pair symmetry; 2 G⁻¹ values + 5 τ values + the σ↔σ⁻¹ mirror.

2. **No bare row = observable-ratio match exists at any row.** The probe swept m_e/m_p, m_p/m_e, α_EM, 1/α_EM, 1/(4π), 1/(8π), α_EM/(4π), √(m_e/m_p), ∛(m_e/m_p) against τ and G⁻¹_diag for each row; best match was 95.5% off (`G⁻¹_diag (3) = 6.12` vs `1/α_EM = 137.04`). This is the **expected** result per #1521's pattern — α_EM at row 1 is not a bare value match but the *composite* `α · [2]_q/(8π) · (1−h²α)` where `1/(8π) = 1/(π·dim H¹(M_Bring))` enters from the Bring shadow-world measure.

   So the §4 experimental program **must** follow the composite template (Habiro element × Planck-tick scale × shadow-world geometric factor), NOT bare row-value matching. Confirmed: a one-script row-by-row identification is OUT OF SCOPE for the cheap pre-commit tests.

### Literature status (2026-06-09 scan)

**The mathematical objects are all named; the physical-coupling
interpretation appears to be original.** Per-simple-object dimensionless
invariants are well-established under several names:

- **Quantum dimensions `dim_q(λ)`** of simple objects in a modular tensor
  category (Verlinde 1988; Etingof–Nikshych–Ostrik 2005) — Perron–
  Frobenius eigenvalues of fusion matrices.
- **Jones-index data `τ(b_i b_j⁻¹)`** of subfactors (Wenzl, *Hecke
  algebras of type An and subfactors*, Invent. Math. 1988) — exactly
  our Gram matrix at roots of unity, but called "indices" not
  "couplings".
- **Per-knot Habiro lifts** (Garoufalidis–Scholze–Wheeler–Zagier,
  *The Habiro ring of a number field*, arXiv:2412.04241, 2024) — the
  closest published analogue to PR #1521's identification:
  one number-theoretic invariant per knot, evaluable at every root of
  unity.
- **Volume conjecture invariants** (Kashaev 1997, Murakami–Murakami
  2001) — per-knot hyperbolic volume from N-colored Jones at
  `q = e^{2πi/N}`, interpreted as *geometry* not coupling.
- **Chern–Simons Wilson-loop expectations** (Witten 1989, Kaul–Ramadevi
  hep-th/9804122) — per-knot `J_K(q)` are *observables*, and the only
  coupling constant in CS is the integer level `k`.

**No published identification** of these invariants with the Standard
Model's α_EM or other gauge couplings exists. Atiyah's 2018 "fine
structure constant" topological proposal is the only published attempt
to derive α from a topological invariant; it was rejected by the
community (Carroll, Baez critiques). The Gram-inverse "shadow price"
reading also does not appear in subfactor / TQFT literature — the Gram
inverse exists (controls Jones–Wenzl idempotents) but is never framed
as a dual-LP price.

**Bottom line:** QOU's framing — *per-basis-element Habiro element ↔
per-particle dimensionless coupling, with α_EM as the row-1 unknot
instance* — is **not in the published literature**. The mathematical
substrate is standard; the physical-coupling identification is the
contribution. This raises (does not settle) two implications:

1. If the row 2–6 α-analogs identify cleanly (experiments §4), it is a
   genuinely novel structural prediction with priority.
2. If they don't (the cheap experiments rule them out), the per-row
   framing remains a clean *organisation* of the existing categorical
   structure even without coupling-constant interpretations — and the
   §5 caching/proof-simplification wins still apply.

The closest *mathematical* template is Garoufalidis–Scholze–Wheeler–
Zagier (2024): "one Habiro element per knot" is the same construction
PR #1521 surfaced for the unknot. Re-reading their paper with the per-
basis-row lens may surface naming + machinery (the Habiro ring of a
number field, evaluation at roots of unity, the per-knot integrality
statements) we can re-use rather than re-derive.

## 7. Recommendation

**Defer wiring** until at least one of experiments #1–#5 closes
(positive identification + q₀-stability check across pin re-pins).
If none close, the per-row family is a beautiful structural pattern
without observable handles — record it, don't claim it.

If 2+ close, the basis-aligned cache architecture (§5) becomes the
canonical compute-pipeline restructure; the per-row §3b-cond classes
replace much of the existing per-observable class proliferation.

**Cheapest first move:** experiment #5 (row 6, electron / trefoil).
The trefoil already has a closed Jones polynomial `J(T(2,3))(q) =
−q⁻⁴ + q⁻³ + q⁻¹`; comparing its value at `q₀` against
`m_e/m_p × small dimensionless rational` is a one-script test. If
that lands cleanly, it would be the second confirmed row after α_EM.

## 8. Sibling-PR cross-link

The α_EM thread (#1521 closed; #1503 closure to CAL-2 floor; RT
Phases 1–4 dormant) is the row-1 worked example. If experiment 5
closes, an analogous "row-6 categorical identification" PR following
the #1521 template would be the natural next mover.

## References (corpus)

- [`canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md) — the 5-stage pipeline
- [`appendix-knot-operations/knot-operator-basis-table-intro.md`](../../content/quantum-observable-universe/appendix-knot-operations/knot-operator-basis-table-intro.md) + tables 1–4 — the basis multiplication structure
- [`appendix-knot-operations-archimedean/particle-nf-table.md`](../../content/quantum-observable-universe/appendix-knot-operations-archimedean/particle-nf-table.md) — particle ↔ basis dictionary
- [`mass-theory/gram-matrix-spectral-connection.md`](../../content/quantum-observable-universe/mass-theory/gram-matrix-spectral-connection.md) — Gram and Gram-inverse role; co-Casimir
- [`mass-theory/knot-operator-lp-selection.md`](../../content/quantum-observable-universe/mass-theory/knot-operator-lp-selection.md) — LP/SDP shadow prices on the 6-element basis
- [`mass-theory/frobenius-gram-matrix.md`](../../content/quantum-observable-universe/mass-theory/frobenius-gram-matrix.md) — Frobenius non-degeneracy via `det G ≠ 0`
- PR #1521 (α_EM Habiro = fundamental-rep fermion-loop unknot) — row-1 worked example

## What this doc is NOT

- Not an attempt to identify the row 2–6 α-analogs. Those are the
  cheap experiments §4.
- Not a Lean formalisation. The §3b-cond per-row class pattern is
  scoped in §5 but not authored.
- Not a wiring instruction. Discipline lock applies: no row 2–6
  invariant gets named as a derivation until its q₀-stability test
  passes.
- Not a literature claim. The "Noether-style" framing is plausible
  given Müger/Etingof but the literature scan for published names
  for this specific construction is in flight.
