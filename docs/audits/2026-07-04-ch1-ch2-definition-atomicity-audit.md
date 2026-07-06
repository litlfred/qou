# Chapter 1 & 2 — definition / atomicity / undefined-term audit (2026-07-04)

Owner request: *"lots of archimedean violations in chapter 1 & 2 — archimedean
functor first use without being defined … there are definitions wrapped up in
propositions and DEFINITION in unstructured narrative … this violates several
QA issues, atomicity in particular. All definitions are supposed to be in their
own block for use."*

Scope: **Ch 1 = `quantum-universes/` (54 blocks)**, **Ch 2 =
`quantum-observable-universes/` (298 blocks)**. Tooling:
`content/pipeline/definition-clarity-audit.ts` (agent-owned QA path,
`AGENTS.md §"QA is agent-owned"`) + manual trace of the two owner-named issues.

## Headline findings

### F1 — `archimedean realization functor` used before definition (Ch 2)  — **the owner's headline issue**

> Spelling note: this doc uses "realization" (American) in its own prose to
> match the block label/title `archimedean-realization-functor` /
> $\mathcal{R}_{\mathrm{top}}$ for greppability. Verbatim quotes of Ch 2 content
> keep the corpus's British "realisation".

[`generating-functions-solve-reeb-flow.md`](../../content/quantum-observable-universe/quantum-observable-universes/generating-functions-solve-reeb-flow.md)
uses the object three times (lines 58, 77–79, 100–116), naming it
**$\tau_\infty$** (τ_∞) and *"the realisation functor $\tau$ (τ) from
$\widehat{\mathbb{Z}[q]}$ to $\mathbb{C}[\![q-1]\!]$"*, and links each mention to
`#def:archimedean-realization-functor`.

That definition **does exist** — but as
[`mass-theory/archimedean-realization-functor.md`](../../content/quantum-observable-universe/mass-theory/archimedean-realization-functor.md),
**seven chapters later**, where it is:

- titled **"Archimedean realization functor $\mathcal{R}_{\mathrm{top}}$"**
  (ℛ_top) — a *different symbol* from the $\tau_\infty$ (τ_∞) used in Ch 2;
- built on `def:adelic-substrate`, `def:motivic-mass-measure`,
  `def:spatial-realization-functor` — adelic / motivic machinery **not
  introduced anywhere in Ch 1–2**.

The markdown link *resolves* (labels are global), so `validate` is silent — but
for a Ch 2 reader the archimedean realization functor is **used with no local
definition and under a symbol ($\tau_\infty$, τ_∞) that never appears at the
definition site**. This is genuinely "first use before definition." Note also
the fibre functor is itself written $\tau$ (τ) (`AGENTS.md §7`), so $\tau$ (τ) /
$\tau_\infty$ (τ_∞) / $\mathcal{R}_{\mathrm{top}}$ (ℛ_top) risk being read as one
object.

**Owner ruling (2026-07-04): do not assert identity.** Ch 2 is made
self-consistent by giving $\tau_\infty$ (τ_∞) a one-line local gloss (the
$q\to1$ Taylor germ $\widehat{\mathbb{Z}[q]} \to \mathbb{C}[\![q-1]\!]$),
aligning the bare $\tau$ (τ) to $\tau_\infty$ (τ_∞) — which also removes the
collision with the fibre functor $\tau$ — and softening the two links to a
`cf.` pointer to the global $\mathcal{R}_{\mathrm{top}}$ (ℛ_top), with no
identity claim and no new block.

**Can the identity be *proved*? Not as a functor equality — the two are not the
same type.** $\tau_\infty$ (τ_∞) has source the Habiro ring
$\widehat{\mathbb{Z}[q]}$ and target $\mathbb{C}[\![q-1]\!]$;
$\mathcal{R}_{\mathrm{top}}$ (ℛ_top) is the composite
$\widehat{\mathcal{M}} \xrightarrow{\chi_{\mathrm{top}}}
\widehat{\mathcal{M}}\otimes\mathbb{Z} \xrightarrow{\pi_\infty} \mathbb{R}$ with
source the *motivic* ring $\widehat{\mathcal{M}}$ and target $\mathbb{R}$.
"$\tau_\infty = \mathcal{R}_{\mathrm{top}}$" is therefore a type error. The
provable relationship is a **compatibility square on QOU volume classes**: both
realizations, applied to the substrate $q$-volume, return the same real number —
the Bloch–Wigner / Thurston hyperbolic volume
(`prop:thurston-volume-additivity`; the mass-theory doc's own
`prop:vol-through-tau` + `rem:kashaev-as-archimedean-realization`). The
*scaffolding* is provable (both maps exist; both compute $V_{\mathrm{hyp}}$ on
the figure-8 / trefoil cases already witnessed in the corpus); the *general*
naturality $\tau_\infty\circ\mathrm{Li}_2^q = \mathcal{R}_{\mathrm{top}}\circ\mu$
for **all** QOU knots is volume-conjecture-strength and **open** — exactly the
`HabiroFlowSolution` open conjecture the Ch 2 remark already flags. So the owner
ruling is the mathematically correct one: they are related by an open
compatibility, not an equality.

### F2 — the $q$-deformed commutator is defined inside a proposition + a remark, never in a `definition` block (Ch 2) — **the owner's Heisenberg example**

The object $[\hat X,\hat P]_q := J\hbar_q(p)$ is *introduced* (with `:=`) in two
non-`definition` blocks:

- [`prop:heisenberg-commutator`](../../content/quantum-observable-universe/quantum-observable-universes/heisenberg-commutator-prop.md)
  — a `proposition` whose body **states the definition** of the commutator and
  then its two limits;
- [`rem:heisenberg-commutator`](../../content/quantum-observable-universe/quantum-observable-universes/heisenberg-commutator.md)
  — a `remark` that **re-states the same `:=`** before interpreting it.

There is no `def:q-deformed-commutator`. Atomicity violation: the definiendum
lives in prose across a prop and a remark. The proposition should assert a
*property* (the two limits, and the identity with $\varTheta(\xi_q)$); the
`:=` belongs in its own `definition` block that both downstream blocks `uses`.

### F3 — `quantum-flatness` defined inside a proposition (Ch 2) — `clarity-defn-misplaced` **major**

[`prop:emergence-to-quantum-flat`](../../content/quantum-observable-universe/quantum-observable-universes/emergence-to-quantum-flat.md)
carries `defines: ["quantum-flatness"]` and the canonical `:defterm[Quantum
flatness]{#quantum-flatness}` define-site *inside a `proposition`*. A definition
site should not live on a provable block.

## `definition-clarity-audit.ts` candidate lists

Full reports: `/tmp` copies regenerated on demand via

```bash
bun run content/pipeline/definition-clarity-audit.ts \
  content/quantum-observable-universe/<chapter> --branch <branch> --md <out.md>
```

### Chapter 1 (`quantum-universes`) — 2 candidates, both minor

| block | criterion | note |
|---|---|---|
| `def:categorical-connection` | `clarity-defterm-bold` (minor) | term "categorical connection" not bolded at define-site |
| `def:categorical-jet` | `clarity-defterm-bold` (minor) | term "categorical jet" not bolded |

Chapter 1 is otherwise clean: 0 `defn-single`, 0 `defn-tight`, 0 `stmt-*`, 0
`defn-misplaced`.

### Chapter 2 (`quantum-observable-universes`) — 23 candidates

**`clarity-defn-tight` — 2 major, 6 minor** (rambling definitions; motivation /
sub-sections that belong in a following `remark`/`prose`):

| block | sev | evidence |
|---|---|---|
| `def:frobenius-hopf-substrate` | major | 5 sub-sections; 70-word preamble before the definition |
| `def:q-heat-equation` | major | 324 prose words; 5 sub-sections |
| `def:substrate-parameter` | minor | 65-word preamble |
| `def:commutative-qou` | minor | 143-word preamble |
| `def:rigid-dualizing-complex` | minor | 3 sub-sections |
| `def:quantum-observable-universe` | minor | 74-word preamble |
| `def:categorical-reeb` | minor | 95-word preamble |
| `def:q-dilogarithm` | minor | 3 sub-sections |

**`clarity-defterm-bold` — 9 minor** (principal term never emphasised at the
define-site): `def:fermion-boson-decomposition`, `def:commutative-qou`,
`def:quantum-observable-universe`, `def:substrate-parameter-planck`,
`def:categorical-reeb`, `def:categorical-q-ext-deriv`,
`def:frobenius-hopf-substrate`, `def:weight-decomposition`, `def:observation`.

**`clarity-stmt-tight` — 5 minor** (statement carries a long preamble / runs
long): `prop:braiding-induced-ordering`, `prop:q-laplacian-spectral-tower`,
`prop:braiding-eigenvalue-extraction`, `prop:qou-canonical-action`,
`prop:fibre-functor-atlas`.

**`clarity-defn-misplaced` — 1 major**: `prop:emergence-to-quantum-flat` (F3).

Clean axes (0 candidates): `clarity-defn-single`, `clarity-stmt-pure`,
`clarity-grad-style`, `clarity-rhetorical-header`, `clarity-proof-pure`,
`clarity-anchor-colon`.

## Fix plan (tranches)

1. **Mechanical / self-contained (no architecture decision):**
   - defterm-bold: bold the principal term at each define-site (11 blocks, Ch 1+2).
   - defn-tight majors + selected minors: move motivational preamble /
     interpretive sub-sections out of the `definition` into a following
     `remark`/`prose` (`interprets:` the definition), leaving the definition
     tight at the top.
   - stmt-tight minors: move preamble to a preceding `prose`; interpretation to
     a following `remark`.

2. **Structural / atomicity (new `definition` blocks + `.lean` siblings +
   manifest wiring + `uses[]` rewiring) — F2, F3.**

3. **Framework decision — F1** (archimedean realization functor): resolved by
   the owner ruling "do not assert identity" (2026-07-04). See Resolution below.

All content edits validated with
`bun run scripts/run-validate.ts content/quantum-observable-universe` (after
`scripts/setup-folio-assistant.sh`); definition `.lean` siblings verified
`lean`-direct where the toolchain is restorable.

## Resolution status (PR #3288)

**Done:**

- **F1** — Ch 2 `generating-functions-solve-reeb-flow.md` gives $\tau_\infty$
  (τ_∞) a local gloss ($q\to1$ Taylor germ $\widehat{\mathbb{Z}[q]}\to
  \mathbb{C}[\![q-1]\!]$), aligns the bare $\tau$ (τ) to $\tau_\infty$ (removing
  the fibre-functor collision), and softens the two links to `cf.`
  pointers to the global $\mathcal{R}_{\mathrm{top}}$ (ℛ_top) — no identity
  claim, no new block (owner ruling). Provability analysis recorded above:
  $\tau_\infty = \mathcal{R}_{\mathrm{top}}$ is a **type error** (different
  source/target); the real relation is an open volume-conjecture-strength
  compatibility.
- **F2** — new atomic `def:q-deformed-commutator`
  (`.ts`/`.md`/`.lean`, `qDeformedCommutator` verified `lean` exit 0);
  `prop:heisenberg-commutator` slimmed to the two limit properties;
  `rem:heisenberg-commutator` no longer re-defines. Wired into
  `sec:heisenberg-commutator`.
- **F3** — new atomic `def:quantum-flatness`
  (`.ts`/`.md`/`.lean`, `IsQuantumFlat` verified `lean` exit 0);
  `prop:emergence-to-quantum-flat` define-site demoted to `:refterm`. Also
  fixes the previously-dangling `#def:quantum-flatness` link in
  `mass-endomorphism/mass-identity-C-proof.md`. `clarity-defn-misplaced`
  major: **cleared** (1 → 0).
- **`clarity-defn-tight` major** `def:q-heat-equation` — definition kept tight;
  four elaboration sub-sections moved to a follow-on
  `rem:q-heat-equation-elaboration`.
- **`clarity-defterm-bold`** — `def:quantum-observable-universe` (was
  `*italic*`) and `def:weight-decomposition` now bold the principal term.
- **Item 2 (defterm/naming batch).** `observation.md` now leads with
  **observation** as the primary term (keeping **intent** as the synonym);
  `def:commutative-qou` title aligned to "Strictly commutative QOU
  (commutative specialisation)" so the bolded term **strictly commutative**
  matches (clears both its `defterm-bold` and `defn-tight` FP flags);
  `substrate-parameter-planck.md` bolds **quantum Planck constant** (was
  `*italic*`); Ch 1 `def:categorical-connection` bolds **curvature** (was
  `*italic*`).
- **Item 3 (F1 scaffolding formalized).** New `conjecture` block
  `conj:archimedean-realisation-volume-compatibility`
  (`.ts`/`.md`, wired after `generating-functions-solve-reeb-flow`) states the
  precise open statement: $\tau_\infty$ (τ_∞) and $\mathcal{R}_{\mathrm{top}}$
  (ℛ_top) are *not* equal as functors (different source/target types), but the
  real-valued volume observables agree on QOU volume classes
  ($\tau_\infty\circ\mathrm{Li}_2^q = \mathcal{R}_{\mathrm{top}}\circ\mu = V_{\mathrm{hyp}}$);
  the scaffolding is established on the figure-8 / trefoil cases, the general
  naturality is the volume-conjecture-strength `HabiroFlowSolution` open
  conjecture.
- **Item 1 (long-statement trims).** `prop:q-laplacian-spectral-tower` — the
  truncation argument marked as an explicit `**Proof.**` and the "four
  consumers" table + concrete truncation values + fibre-vs-observable
  interpretation moved to a follow-on `rem:q-laplacian-consumers`; **cleared**.
  `prop:qou-canonical-action` — the trace-factorisation / two-forms / uniqueness
  derivation marked as an explicit `**Proof.**` and the observability-cohomology
  interpretation moved to a follow-on `rem:canonical-action-obstruction`;
  **cleared**.
- **Item 2 (`def:q-dilogarithm` de-bundle).** The bold sub-sections were dropped
  so the definition reads as one object (level-$k$ primitive setup →
  $q$-dilogarithm as the pentagon-normalised level-2 primitive), consistent with
  the `QDilogarithm` Lean structure (whose `pentagon` field makes the pentagon
  *definitional*, not a separable proposition — so no extraction of the pentagon
  itself). Only the monoidal-associator interpretation + tikzcd moved to a
  follow-on `rem:q-dilogarithm-pentagon-associator`; **cleared**.

Ch 2 clarity candidates **23 → 11** (the 11 remaining are all the adjudicated
false positives / aggressive-threshold minors below).

**Adjudicated as false positives / author-naming (not defects):**

- `def:frobenius-hopf-substrate` `defn-tight` — the five "sub-sections" are the
  definition's *axioms* (Algebra / Coalgebra / Frobenius / Non-degeneracy /
  Self-duality), a legitimately structured definition, not rambling.
- `def:categorical-reeb`, `def:categorical-q-ext-deriv` (Ch 2),
  `def:categorical-jet` (Ch 1) `defterm-bold` — the principal term **is** bolded
  at the define-site; the scanner misses bold spans that contain inline math
  (`**$q$-deformed exterior derivative**`) or wrap across a line
  (`**jet\nobject**`).
- `fermion-boson-decomposition.md` `defterm-bold` — bolds its real definienda
  (**boson**, **fermion**).
- `def:rigid-dualizing-complex` `defn-tight` — the three "sub-sections" are the
  definition's *conditions* (Finite injective dimension / Rigidifying
  isomorphism / Van den Bergh duality), a legitimately structured definition,
  not rambling — same class as `frobenius-hopf-substrate`.
- `def:q-dilogarithm` `defn-tight` — **resolved** (Item 2 above) by a
  Lean-consistent light de-bundle rather than the skill's speculative
  `def:level-k-primitive` + `prop:q-dilogarithm-pentagon` split: the
  `QDilogarithm` Lean structure carries `pentagon` as a *defining field*, so the
  pentagon is definitional and must **not** be extracted to a separate
  proposition (that would desync `.md` from `.lean`). Only the associator
  interpretation moved out.

**Remaining (lower-value polish, deferred):** the `clarity-defn-tight` /
`clarity-stmt-tight` **minors** where the flagged "preamble" is the
definition/statement's own ambient-data setup (`Let $(\mathbf{C},A,\tau)$ be
… with maximal torus $T$ … and weight decomposition …`) — standard
graduate-math style that the aggressive 60/80-word threshold over-flags:
`def:substrate-parameter`, `def:categorical-reeb`, `prop:braiding-induced-ordering`,
`prop:braiding-eigenvalue-extraction`, `prop:fibre-functor-atlas`. Each is an
agent-adjudicated candidate, not a confirmed defect. (The two genuinely-long
statements `prop:q-laplacian-spectral-tower` and `prop:qou-canonical-action` were
**resolved** in Item 1 above.)
