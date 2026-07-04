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

### F1 — `archimedean realisation functor` used before definition (Ch 2)  — **the owner's headline issue**

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
for a Ch 2 reader the archimedean realisation functor is **used with no local
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

3. **Framework decision — F1** (archimedean realisation functor): requires the
   author's ruling on whether $\tau_\infty$ (local $q\to1$) $=
   \mathcal{R}_{\mathrm{top}}$ (global adelic) before the fix shape is fixed.

All content edits validated with
`bun run scripts/run-validate.ts content/quantum-observable-universe` (after
`scripts/setup-folio-assistant.sh`); definition `.lean` siblings verified
`lean`-direct where the toolchain is restorable.
