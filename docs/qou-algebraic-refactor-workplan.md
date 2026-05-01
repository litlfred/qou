# QOU algebraic refactor — workplan

Branch: `claude/qou-algebraic-refactor-1qVFc`

This refactor migrates the magic-number / shell-closure story from
matrix-evaluation evidence (Hoefsmit seminormal forms at $k = 3\dots10$,
blocked at $k \geq 12$) to a pure homological / algebraic-geometry
framework: full-twist neutrality, BB-stratified jet condensation, and
LR-fusion rigidity.

## Chapter mapping (directive → repo)

| Directive name | Repo directory | Manifest position |
|---|---|---|
| Ch 3 — Yekutieli Brane Tower | `lifting-and-descent` | Ch 4 |
| Ch 4 — Braiding and knot theory | `braids-and-knots` | Ch 5 |
| Ch 8 — Algebraic Substrate | `algebraic-substrate` | Ch 7 |
| Ch 10 — Nuclear binding and magic numbers | `observations` | Ch 12 |

## Block kinds (CLAUDE.md §3b conjectural propagation)

The directive labels each item "Proposition", but the framework-level
claims (full-twist global neutrality, spectral-sequence collapse on the
magic ladder, LR rigidity for double-magic states) assert novel
structure. They are authored as `conjecture` blocks (Lean axiom-classes)
with prose titles "Proposition X. ..." preserved. Provable Hecke /
partition fragments stay as `proposition`s where genuinely derivable.

## Phase 1 — this PR

### New conjecture blocks (each is a `.ts` + `.md` + `.lean` triple)

| Label | Chapter | Section | Title |
|---|---|---|---|
| `conj:categorical-neutrality-saturated-shells` | `braids-and-knots` | Categorical Mass Foundations | Categorical neutrality of saturated shells (full-twist trivial action) |
| `conj:homological-shell-condensation` | `lifting-and-descent` | Mass in the Brane Tower | Homological shell condensation (BB-stratified $E_\infty^{p,>0} = 0$ at magic $n$) |
| `conj:diagrammatic-double-magic-lr-fusion` | `observations` | Beta-decay observations (after `magic-numbers-from-q`) | Diagrammatic double-magic and LR-fusion rigidity |

### Illustration blocks (`.ts` + `.md`, no Lean)

In `observations`, kind `example`, sibling section to `magic-numbers-from-q`:

| Label | Case | Visual content |
|---|---|---|
| `ex:single-magic-O18-diagram` | $^{18}\mathrm{O}$ ($Z=8$, $N=10$) | Self-conjugate Z-block + frayed N-block; non-zero $\kappa$ leakage |
| `ex:double-magic-Ca40-diagram` | $^{40}\mathrm{Ca}$ ($Z=N=20$) | Twin self-conjugate blocks; LR fusion with cancelling $\sum c(x) = 0$ |
| `ex:non-magic-Li6-diagram` | $^{6}\mathrm{Li}$ ($Z=N=3$) | Frobenius arms exceed legs; non-zero full-twist flux vectors |

### Interpretive remarks

- `rem:phi-n-global-section` (`braids-and-knots`) — interprets
  `conj:mass-endomorphism`: in this refactor $\Phi_n$ is the **global
  section** of the categorical mass endomorphism over the rigid braided
  monoidal category. Locality assumptions are dropped; non-trivial
  ribbon action propagates unbounded topological flux, so finite
  observable mass forces global topological neutrality.
- `rem:k12-barrier-bypass` (`observations`) — interprets
  `prop:magic-numbers-from-q`: the homological condensation
  conjecture analytically bypasses the $k \geq 12$ matrix-evaluation
  barrier. Hoefsmit numerical verification at $k = 3\dots10$ is
  reframed as **empirical computational verification** of the
  homological prediction; the higher magic numbers $\{50, 82, 126\}$
  are not waiting on hardware.

### Lean (axiom-class pattern, CLAUDE.md §3b)

Each `conj:` block carries a Lean file under
`content/quantum-observable-universe/lean/QOU/` declaring the
conjecture as a typeclass with named structural fields. Downstream
results (e.g. magic-number ladder) become conditional theorems
parameterised on the relevant typeclass instance.

Per CLAUDE.md "Namespace = chapter module", each new module is
nested under the existing chapter namespace it logically extends:

| Lean ref | Module path | Chapter namespace |
|---|---|---|
| `qou:QOU.BraidKnot.ShellNeutrality.SaturatedShellConjecture` | `QOU/BraidKnot/ShellNeutrality.lean` | `BraidKnot` (Ch 5, braids-and-knots) |
| `qou:QOU.LiftingDescent.HomologicalCondensation.ShellCondensationConjecture` | `QOU/LiftingDescent/HomologicalCondensation.lean` | `LiftingDescent` (Ch 4, lifting-and-descent) |
| `qou:QOU.Interactions.LRFusion.DoubleMagicConjecture` | `QOU/Interactions/LRFusion.lean` | `Interactions` (sibling of `ConfinementSDP`, `NuclearOperatorRegimes`) |

The LR-fusion content block lives in `observations/`, but the Lean
module sits under `Interactions` because the existing repo has no
`QOU.Observations` namespace and LR-fusion is a particle-interaction
construction in the spirit of the other `Interactions/*` modules.

### Manifest wiring

- `braids-and-knots.ts` — append `categorical-neutrality-saturated-shells`
  and `phi-n-global-section` after `mass-endomorphism-conjecture` in
  *Categorical Mass Foundations*.
- `lifting-and-descent.ts` — append `homological-shell-condensation`
  to *Mass in the Brane Tower*.
- `observations.ts` — append `diagrammatic-double-magic-lr-fusion`,
  `single-magic-O18-diagram`, `double-magic-Ca40-diagram`,
  `non-magic-Li6-diagram`, `k12-barrier-bypass` after
  `magic-numbers-from-q` in *Beta-decay observations*.

### Validation gate

Each commit runs `cd content && bun run validate`. The refactor merges
only when:

1. Zod + constraint validation pass for the new triples.
2. `lean.ref` URIs resolve to the new `QOU.*` modules.
3. `interprets` cross-refs for the two `remark` blocks resolve.
4. `uses[]` are minimal (CLAUDE.md §"Dependency graph integration").

## Phase 2 — deferred

- Document-wide sweep replacing every reference to "local trivialisation"
  / "screening" with explicit global-section language.
- Concrete Lean proofs for the provable Hecke fragments
  (full-twist content formula, $\sum c(x) = 0 \Rightarrow \lambda = \lambda'$).
- Numerical witnesses for the LR-fusion rigidity prediction on the
  $\{50, 82, 126\}$ ladder.
- Integration of `prop:magic-numbers-from-q` deltas
  ($+33.2, +20.4, +4.4$) as empirical-verification table inside
  `conj:homological-shell-condensation`.

## Citations to register

CSL-JSON keys follow the canonical `authorYEAR` (or
`author1-author2YEAR`) lowercase ASCII format used elsewhere in
`content/schema/references.ts`. The following may be added if not
already present:

- `bialynicki-birula1973` — BB stratification
- `geck-pfeiffer2000` — Iwahori–Hecke characters
- `ariki1996` — Specht modules at roots of unity
- `ram1991` — Hecke trace / RSK

Existing keys reused (already in `content/schema/references.ts`):
`hoefsmit1974`, `jucys1974`, `murphy1992`, `mathas1999`,
`kassel1995`, `turaev2010`, `yekutieli2010`, `yekutieli2008`,
`yekutieli2015`.

Citations are placed directly with the claim they support in the
`.md` files; structural results internal to the framework are
referenced via cross-block hyperlinks (`[text](#label)`), not via
external citations.
