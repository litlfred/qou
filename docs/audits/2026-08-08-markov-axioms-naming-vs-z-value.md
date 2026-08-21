> # ⛔ SUPERSEDED — the declined half was overtaken one day later
>
> **Read this before the analysis below.** This audit's central recommendation
> — *decline to change `z`; keep convention C in axiom 3, fix only the NAME* —
> is **superseded by the owner ruling of 2026-08-09, which excised convention C
> repo-wide**, and again by the 2026-08-15 ruling making convention D canonical.
> The block this audit is about,
> [`rem:markov-axioms-primitive`](../../content/quantum-observable-universe/braids-and-knots/markov-axioms-primitive.md),
> now carries the excision directly and states the selection is *forced*, not
> stipulated.
>
> **What still stands:** the diagnosis. The contradiction it identifies is real
> and was real — the block named Jones (D) while stipulating Ocneanu C — and the
> two-repair table, the cost accounting, and the Temperley–Lieb provenance
> observation (`1/(q^{1/2}+q^{-1/2}) = δ⁻¹`, the loop reciprocal attached to
> `e_n` rather than `σ_n`) are unaffected by the ruling and are why this document
> is kept rather than dropped.
>
> **What does not:** every sentence recommending that `z` stay at C, and the
> framing of `z_C`'s bar-invariance as a reason to prefer it. Do not cite this
> document as support for convention C.
>
> Salvaged from PR #4767, which was closed as superseded — main's copy of the
> block had already moved past it, so merging the PR would have reverted the
> ruling's own documentation. This audit and its bean were the only two
> artifacts in it that main lacked.

# The Markov-axioms block names Jones and stipulates Ocneanu — the *name* is the defect the corpus lets an agent fix, the *value* is not

Branch `claude/fix-markov-z-stipulation-2026-08-08`, stacked on
`claude/n1dj-trace-registry-guard-2026-08-08`. 2026-08-08.

Predecessors, both required reading:
[`2026-08-08-borromean-trace-convention-forcing.md`](2026-08-08-borromean-trace-convention-forcing.md)
(bean `qou-3qrv`),
[`2026-08-08-trace-convention-registry-and-doc-fix.md`](2026-08-08-trace-convention-registry-and-doc-fix.md)
(bean `qou-n1dj`), and
[`2026-08-08-mass-fibre-dimension-forces-convention-d.md`](2026-08-08-mass-fibre-dimension-forces-convention-d.md)
(bean `qou-n1dj` option 3).

**Nothing is wired, no tier changed, no production numerical value altered, and
no trace parameter was rewritten.**

## 1. The task, and why half of it was declined

The assignment was to correct axiom 3 of
[`rem:markov-axioms-primitive`](../../content/quantum-observable-universe/braids-and-knots/markov-axioms-primitive.md)
from $z = 1/(q^{1/2}+q^{-1/2})$ (convention **C**) to $z = q^3/(q^2+1)$
(convention **D**), on the ground that the same block concludes "*axioms 1–3
force $\mathrm{tr}_M$ to be the non-degenerate **Jones**-Markov trace*" and
Jones is D — so the block names D and stipulates C.

**The contradiction is real.** It has two possible repairs, and they are not
equivalent:

| repair | what changes | cost |
|---|---|---|
| **Fix-value** | axiom 3's $z$ becomes D | decides the reserved `mass` dispute; falsifies ≥ 8 corpus sites; flips `binding` to disputed |
| **Fix-name** | the block says which family member its $z$ is | none — it is a naming/attribution correction |

**Fix-name was done. Fix-value was declined.** Three things on this branch say
Fix-value is not an agent's to make.

### 1a. The prerequisite audit reserves this exact edit to the owner

[`2026-08-08-trace-convention-registry-and-doc-fix.md`](2026-08-08-trace-convention-registry-and-doc-fix.md)
§6, follow-up 1:

> **Owner decision on the `mass` channel** (bean `qou-3qrv`): either establish
> the TL premise, **in which case D is forced and the definition chain should be
> corrected to say so**, or accept C and take the −197 ppm. **Do not decide by
> match.**

Rewriting $z$ *is* "correcting the definition chain to say so". It is the second
half of a conditional whose first half the owner holds. The same audit's §2 also
finds the C description **"faithful to the corpus. It is not the error."**

Note also the asymmetry the registry now records: the standing prohibition was
written as *"no agent may switch the production trace"*. Changing the
definitional side instead reaches the same verdict — the channel's C-vs-D
disagreement resolved in D's favour — by walking in the other door. Registering
that as equally forbidden is part of this pass.

### 1b. The strongest pro-D document scopes D to the *fibre*, not to $\mathrm{H}_n(R,q)$

[`2026-08-08-mass-fibre-dimension-forces-convention-d.md`](2026-08-08-mass-fibre-dimension-forces-convention-d.md)
is the document that established D on the corpus's own premise. Its own
scope paragraph:

> It is **not** a claim that C is not a Markov trace on $\mathrm{H}_3(q)$ — it is
> one, a perfectly good member of the Ocneanu family, and **every statement about
> it as such stands.**

`rem:markov-axioms-primitive` and `thm:jones-markov-trace` are exactly such
statements: both are stated on the **full** $\mathrm{H}_n(R,q)$, with no fibre
functor, no $\mathrm{Rep}(\mathrm{SU}_q(2))$, and no Temperley–Lieb quotient. D
is what the *mass channel's two-dimensional fibre* forces; C is a legitimate
inhabitant of the generic braids-and-knots chapter. So "D is right" and "axiom 3
is wrong" are different claims, and only the first is established.

### 1c. The blast radius of Fix-value, measured

At least **8** corpus sites stipulate or derive from
$z = 1/(q^{1/2}+q^{-1/2})$, found by grepping the C $z$-form across `content/`:

| site | file | exposure |
|---|---|---|
| `thm:jones-markov-trace` | `braids-and-knots/jones-markov-trace.md:7` | **stipulates the same value, with the same three axioms — and is cited by `rem:markov-axioms-primitive` itself** |
| its Lean sibling | `braids-and-knots/jones-markov-trace.lean:112` | docstring names the value on the abstract `z` field |
| `prf:trm-hopf-sigma1-sq-closed-form` | `braids-and-knots/trm-hopf-sigma1-sq-closed-form-proof.md:7,10,13` | a **derived closed form** built on $\mathrm{tr}_M(\sigma_1) = z$ |
| `rem:bar-involution-c5-algebraic-identities` | `braids-and-knots/bar-involution-c5-algebraic-identities.md:1` | asserts "$z$ is bar-invariant" — **true for C, false for D** (§3) |
| `prf:trace-locality-meets-gs-nonlocality` | `braids-and-knots/trace-locality-meets-gs-nonlocality-proof.md:11` | carries the value in its hypothesis |
| `prf:hecke-satisfies-blitvic-hypothesis` | `braids-and-knots/hecke-satisfies-blitvic-hypothesis-proof.md:5` | ditto |
| `prop:centered-hecke-variance-positive` (+ proof, + table data) | `observations/centered-hecke-variance-positive*.md` | defines $\tilde\sigma_i := \sigma_i - z$, quotes $z \approx 0.4993$, and the proof runs on $(q^{1/2}+q^{-1/2})^2 > 4$ |
| `prf:algebraic-gns-embedding` | `observations/algebraic-gns-embedding-proof.md:5` | states the recursion with the value, citing `thm:jones-markov-trace` |

And one structural consequence in the registry: `binding`'s
`definitional_source` **is** the line in question, while binding production is C
(`closed_form_tau_M.py::markov_z`). Rewriting that line flips `binding` from
`agreed` to `disputed` — a second dispute manufactured to close the first. Per
the assignment's own instruction the binding channel was left untouched: no
change to `closed_form_tau_M.py`, to `markov_z`, or to binding's registry row.
Whether binding should move to D is a separate open question.

The first row is the decisive one on its own. `thm:jones-markov-trace` is in the
same chapter, states the identical axioms with the identical $z$, and is the
block that `rem:markov-axioms-primitive` **cites** two lines above the sentence
under repair. Changing one and not the other does not remove an inconsistency;
it manufactures a sharper one between a block and its own citation.

## 2. What was changed

### `braids-and-knots/markov-axioms-primitive.md`

- The concluding sentence no longer calls the result "the non-degenerate
  Jones-Markov trace". It now says axioms 1–3 determine $\mathrm{tr}_M$ uniquely
  and non-degenerately **once $z$ is fixed**, that the stipulated value selects
  the **full-Hecke Ocneanu / Wenzl $z$-trace = convention C**, that C has
  $y_{(1^3)}(q) \neq 0$ so its closure is **not** the Jones polynomial, and that
  the Jones case is convention D, $z = q^3/(q^2+1)$, on the two-dimensional
  $\mathrm{SU}_q(2)$ fibre. The name *Jones–Markov trace* is stated not to fix
  $z$ by itself.
- "Link invariance of the **Jones polynomial** is restored by the writhe
  prefactor" → "of the **closure invariant**" (the writhe prefactor is generic
  to the family; the Jones attribution was the same misnomer).
- **The provenance of the stipulated value, recorded as an observation and
  explicitly not as an established finding** — preserving the epistemic label the
  predecessor audit put on it ("*I have not established that this is what
  happened, only that the shapes coincide*"). With loop parameter
  $\delta = q^{1/2}+q^{-1/2}$, the stipulated $z$ equals
  $q^{1/2}/(q+1) = \delta^{-1}$, and on the Temperley–Lieb side the stabilisation
  parameter belongs to the **projection** $e_n$, not to the Hecke generator
  $\sigma_n$ of axiom 3. The block states both normalisations, which resolves an
  apparent conflict in the sources: for idempotent $e_n^2 = e_n$ the value is
  $\delta^{-2}$ (Jones 1985 relation (V), $t/(1+t)^2 = \delta^{-2}$, as read in
  the predecessor audit), and rescaling to $e_n^2 = \delta e_n$ multiplies it by
  $\delta$ to give $\delta^{-1}$. Both are correct in their own normalisation, so
  "$\mathrm{tr}(e_i) = 1/\delta$" and "$= 1/\delta^2$" are not competing claims.
  Either way the parameter is $e_n$'s and axiom 3 attaches it to $\sigma_n$:
  right concept, wrong generator.
- A new paragraph recording what is **convention-independent** (§3), so a future
  reader does not re-derive it.

### `braids-and-knots/jones-markov-trace.md` — a false sentence, not a misnomer

The block asserted:

> For any braid $\beta$, $\mathrm{tr}_M(\rho_n(\beta))$ computes the **Jones
> polynomial** of the closure $\hat\beta$ up to framing.

At the $z$ the same block stipulates two lines earlier ($z_C$) this is **false**,
not merely loosely named. The Jones polynomial is the member with
$y_{(1^3)} = 0$; C has $y_{(1^3)}(q_0) \approx 0.0227449 \neq 0$, and the two
functionals differ on an explicit braid — 195.82 ppm on $\beta_{\mathrm{Bor}}$,
with $D \neq C$ Lean-proved
(`QOU.BraidsAndKnots.BorromeanTraceConventionSplit.conventionD_ne_conventionC`).
Two functionals that disagree on a braid closure cannot both be that closure's
Jones polynomial. Corrected to name the family member selected by $z$ and to pin
the Jones case to $y_{(1^3)} = 0 \Leftrightarrow z = q^3/(q^2+1)$.

This block was not in the assignment's scope. It was fixed anyway, per AGENTS.md
§"small-moderate fixes for related bugs ride on the active PR": leaving a false
mathematical sentence standing in the block that the repaired block *cites*
would have made the repair cosmetic.

### The registry

- `doc_claims` gains a row for `jones-markov-trace.md:7`, so **both** definitional
  pins are under R6 and cannot drift apart — any future change of $z$ in one is
  now machine-visible as a mismatch in the other.
- `meta.negative_stabilisation` records the $z_{-}$ facts of §3.
- `mass.open_item` records that the dispute is closable from **neither** end by
  an agent, with the site inventory of §1c as the cost of the definitional route.
- **`mass` was deliberately left `disputed`** and its `definitional_convention`
  left at C. That is the finding, not an oversight.

## 3. Downstream consequences in the block, checked

The assignment asked whether the block's other numbers survive a change of
convention. They do — and the reason is worth recording, because it means this
part of the block needs no repair under **either** convention. Verified
symbolically (sympy, exact cancellation), $h = q - q^{-1}$,
$q_0 = 1.1099785827513808$ (experimental / proton pin):

| | $z$ | $z(q_0)$ | $z_{-} = z - h$ | $z_{-}(q_0)$ | $\bar z = z\|_{q\to q^{-1}}$ |
|---|---|---|---|---|---|
| **C** | $q^{1/2}/(q+1)$ | $0.49932033418369445250$ | $\dfrac{q^{3/2}-q^3-q^2+q+1}{q(q+1)}$ | $0.29026003538805515083$ | $= z_C$ (**bar-invariant**) |
| **D** | $q^3/(q^2+1)$ | $0.61268803714646524365$ | $1/(q^3+q)$ | $0.40362773835082594197$ | $1/(q^3+q)$ (**not** invariant) |

- **$z_{-} := z - (q-q^{-1})$ is convention-independent as a formula.** It comes
  from substituting $\sigma_n^{-1} = \sigma_n - h$ into axiom 3; nothing about
  the value of $z$ enters. Only the number it evaluates to moves.
- **The $z\,z_{-} = 1$ analysis carries over verbatim.** Its roots are $z = q$
  and $z = -q^{-1}$ — the two one-dimensional characters of $\mathrm{H}_n(R,q)$,
  both degenerate. The equation $z(z-h) = 1$ mentions only $h$, so the root pair
  is identical under every member of the family. The block's claim was checked
  and needed no change.
- **The $z^k$ strand-appending factor carries over verbatim.** It counts $k$
  applications of axiom 3, whatever $z$ is.
- **A new exact identity, on D's side:** $z_{-}^{D} = 1/(q^3+q) = \bar z_D$
  *exactly*. Under convention D the positive and negative stabilisation
  parameters are exchanged by the bar involution. (Check:
  $q^3/(q^2+1) - (q-q^{-1}) = \bigl(q^4 - (q^4-1)\bigr)/\bigl(q(q^2+1)\bigr)
  = 1/(q^3+q)$.) No analogue holds for C, where $\bar z_C = z_C \neq z_{-}^{C}$.
- **Therefore `rem:bar-involution-c5-algebraic-identities` is C-specific.** Its
  "the Markov parameter $z$ is bar-invariant" is true for C and **false** for D,
  so it belongs in the Fix-value blast radius. Its companion factorisation
  $h = (q^{1/2}-q^{-1/2})(q^{1/2}+q^{-1/2})$ is an identity in $q$ alone and is
  unaffected; only the *naming* of $q^{1/2}+q^{-1/2}$ as $1/z$ is convention-bound.

So: no number in the block moved, because none of the block's derived claims
depended on which member of the family axiom 3 selects. The defect was never
arithmetic — it was that the block did not say which member it had selected.

## 4. Verification

CI is `workflow_dispatch`-only, so the agent's own checks are the gate
(AGENTS.md §"QA is agent-owned; CI is a backup").

| check | result |
|---|---|
| `trace_convention_registry_validate.py --lint-docs --selftest` | **PASS**, 0 errors, 21 warnings (all pre-existing R5); RC1/RC2/RC3 all CAUGHT; R3 live-confirms C at $3.39\times10^{-19}$ and D at $3.31\times10^{-19}$ |
| same, `--strict` | **FAIL** — and it failed identically *before* this pass. The 21 R5 warnings are the tracked backlog (Borromean tracers outside `production_files` with no `convention X` docstring). Not drained here: the registry says explicitly *"do not infer the convention from the value it returns"*, so guessing 21 of them is the documented way to make a mislabel canonical |
| `bun run scripts/run-validate.ts content/quantum-observable-universe` | exit 1, **29 issues — byte-identical before and after** this pass (`diff` of the two runs is empty); neither edited block appears in the output. The 29 are pre-existing (unresolved `uses`, the ten `notation-register-tableN-data` blocks with empty `uses`, one dangling remark, missing Lean decls) |
| render-QA, grep battery | run on both edited `.md`: balanced math delimiters (single and display), balanced braces, balanced begin/end and bigl/bigr, no KaTeX-rejected operator macro, no list-marker hijack inside display math, no bare align-family. Clean |
| render-QA, pipeline | `scripts/setup-folio-assistant.sh` succeeded (clone + 302 packages), so the platform **was** available and was used |
| `m_p` unchanged | `canonical_mass.proton_mass_mev() = 938.2720894273243`, `neutron_mass_mev() = 939.5654227645324` — no compute, witness, or $z$ touched |
| Lean | none added, none changed |

## 5. Two premises of the assignment that did not hold

Recorded so the next agent is not surprised by them.

1. **The registry was not on `main`.** The assignment said all prerequisite work
   was merged and to branch from `origin/main`. At `origin/main` = `3f1a4e3f23`,
   `docs/coordination/trace-convention-registry.{json,md}` and
   `trace_convention_registry_validate.py` **do not exist** — they live on the
   unmerged sibling `claude/n1dj-trace-registry-guard-2026-08-08` (`58bf84f3ac`),
   together with the "notwithstanding the name" paragraph the assignment quoted.
   This branch is therefore **stacked on that sibling**, not on `main`; merge the
   sibling first.
2. **Neither gate the assignment named can pass, at baseline.** `--strict` and
   `run-validate` both fail on `main` for reasons unrelated to trace
   conventions (§4). The honest gates used instead: registry errors $0 \to 0$,
   registry warnings $21 \to 21$, all three selftests still caught, and
   `run-validate` output byte-identical.

## 6. Follow-ups

0. **Bean [`qou-h9p8`](../../.beans/qou-h9p8--gap-remmarkov-axioms-primitive-thmjones-markov-tra.md)**
   carries the definitional-side half of the decision, with the site list, the
   verified $z_{-}$ / bar table, and a third option worth weighing against both
   (leave $z$ free in the generic block and name two specialisations, so the
   mass-vs-binding split becomes expressible rather than merely documented). It
   is registered in the `mass` channel's `open_item` as
   `bean_definitional_side`.
1. **The owner decision on `mass` (bean `qou-3qrv`) is unchanged and now has its
   full cost on both sides**: −197 ppm across ~30 `F_Bor` consumers if
   production moves to C, or the §1c inventory of ≥ 8 corpus sites (one of them
   a bar-invariance claim that fails under D) if the definition moves to D. Do
   not decide by match.
2. **If the owner rules D**, the definitional edit is a *chapter-wide* pass, not
   a one-line one: §1c is the work list, `thm:jones-markov-trace` and its Lean
   sibling first, and `binding`'s registry row needs re-sourcing in the same
   commit so it does not silently flip to disputed.
3. **Consider whether the braids-and-knots chapter should carry both members
   explicitly** — a single generic block with $z$ free, and two named
   specialisations — rather than one block stipulating one member. That would
   make the mass-vs-binding split expressible without either channel's
   definition being wrong.
4. **Drain the 21 R5 warnings** (inherited follow-up), confirming each function's
   trace rather than inferring it from its value.
