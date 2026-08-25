# The all-`n` Temperley–Lieb weight-vanishing lemma

**Verdict: PROVED in Lean, sorry-free, for all `n` and all `λ`** — with one
external input, a published theorem of Wenzl, cited and named below rather
than assumed in Lean.

The statement [#5207](https://github.com/litlfred/qou/pull/5207) named as what
would turn its four measured points into a theorem:

> `y_λ = 0 ⟺ λ has ≥ 3 rows`, at `z_D = q³/(q²+1)`, via the Ocneanu-trace
> weight formula.

Lean: [`QOU/QBeta/WenzlWeightVanishing.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/WenzlWeightVanishing.lean)
· probe [`wenzl_level_two_vanishing.py`](../../computations/probes/wenzl_level_two_vanishing.py)
· output [`wenzl-level-two-vanishing.json`](../../computations/probes/wenzl-level-two-vanishing.json).

## What changes

#5207 established `radical = ⟨E⁽³⁾⟩` **as ideals** at `n = 3, 4, 5, 6`, with
coranks `1, 10, 78, 588 = n! − Catalan(n)`, resting on
[#5185](https://github.com/litlfred/qou/pull/5185)'s `det G ≡ 0` identically
over `ℚ(q)` and its `n = 3` weights. It closed by saying, correctly:

> *Still hypothesised: the identification **for all n**. Four points is four
> points.*

That sentence can now be retired. The `≥ 3`-row blocks are exactly the ones
the trace annihilates, at every `n`. The measured coranks are no longer four
coincidences that happen to match `n! − Catalan(n)`; they are the first four
values of a proved statement.

Neither #5185's nor #5207's measurements are re-derived here. They are cited.

## The identification: `z_D` is Wenzl level `r = 2`

The route runs through a change of Hecke normalisation, and it is worth
writing out because the two conventions differ by more than a rescaling of
`z`.

Wenzl and Orellana use `g² = (Q−1)g + Q`, eigenvalues `Q, −1`. This repo uses
`σ² = (q − q⁻¹)σ + 1`, eigenvalues `q, −q⁻¹` (AGENTS.md §7a). Matching
eigenvalues forces `σ = g/q` and **`Q = q²`**; the Markov parameters then
differ by that same factor, `z_W = q·z`.

Wenzl's parameter relation `z_W = Q^r(1−Q)/(1−Q^r)` inverts to
`Q^r = z_W/(1 − Q + z_W)`. Substituting convention D:

```
q·z_D = q⁴/(q²+1)
1 − Q + q·z_D = (1−q²)(q²+1)/(q²+1) + q⁴/(q²+1) = (1 − q⁴ + q⁴)/(q²+1) = 1/(q²+1)
Q^r = [q⁴/(q²+1)] · (q²+1) = q⁴ = Q²      ⟹   r = 2
```

**Convention D is the SU(2) level exactly** — not approximately, and not at a
particular `q`. This is `wenzlLevel_conventionD`, proved in Lean as the
algebraic identity it is.

It was already in the corpus, at
[`schur_principal_mpmath.py` `_wenzl_constants`](../../computations/schur_principal_mpmath.py)
(*"`Q^r = q⁴ = Q²`, i.e. **r = 2**, the SU(2) level"*). The probe re-derives
it from scratch so the Lean rests on a check rather than on a docstring.

## The mechanism: one cell

Wenzl's weight is the principal specialisation in hook-content form — the
formula `markov_weights_symbolic.schur_principal_symbolic` and
`schur_principal_mpmath._schur_principal_with` already compute:

$$s_\lambda = Q^{n(\lambda)} \prod_{x \in \lambda} \frac{1 - Q^{\,r + c(x)}}{1 - Q^{\,h(x)}}$$

with `c(x) = j − i` the content and `h(x)` the hook length. The whole lemma is
the numerator:

- A factor `1 − Q^{r + c(x)}` vanishes iff `Q^{r+c(x)} = 1`, and for `Q` not a
  root of unity that means **`c(x) = −r`**.
- Contents down the first column are `0, −1, −2, …`, so a cell of content `−r`
  is `(r, 0)` — the first cell of row `r+1`.
- Young diagrams are down-left closed, so *any* cell of content `−r` drags
  `(r, 0)` in with it. There is no way to have such a cell without having more
  than `r` rows, and no way to have more than `r` rows without one.

Hence `s_λ = 0 ⟺ ℓ(λ) > r`, for every `r` and every `λ`. At `r = 2`: `y_λ = 0`
iff `λ` has at least three rows. The Temperley–Lieb row cap is a statement
about the single cell `(2, 0)`, of content `−2`.

The denominators cannot interfere: every cell of a diagram has hook length
`≥ 1`, so `1 − Q^{h(x)} ≠ 0` under the same genericity (`one_le_hook`).

## Lean

Namespace `QOU.QBeta.WenzlWeight`. Generic `[Field R]` — no ordering, no `ℝ`,
no archimedean construct (AGENTS.md §7c) — except in the one instantiation
lemma, which sits below the substrate→archimedean wall and is used by nothing
above it.

| Declaration | Statement |
|---|---|
| `one_le_hook` | every cell of a diagram has hook length `≥ 1` |
| `wenzlLevel_conventionD` | `z_D` inverts to `Q^r = Q²`: convention D **is** level 2 |
| `colLen_gt_of_content_eq_neg` | a cell of content `−r` forces `> r` rows |
| **`schurPrincipal_eq_zero_iff`** | **`s_λ^{(r)} = 0 ⟺ ℓ(λ) > r`** — all `r`, all `λ` |
| **`conventionD_weight_eq_zero_iff`** | **`y_λ = 0 ⟺ λ has ≥ 3 rows`** |
| `conventionD_weight_eq_zero_iff_rowLens` | same, via `rowLens.length` |
| `conventionD_weight_ne_zero_of_two_rows` | the surviving side, stated positively |
| `not_root_of_unity_of_pos_ne_one` | the hypothesis holds at every `Q > 0`, `Q ≠ 1` |
| `colLen_ofRowLens_one_one_one`, `colLen_ofRowLens_two_one` | row counts of `(1³)`, `(2,1)` |
| `discriminates_at_n_three` | `(1³)` dies, `(2,1)` survives |

`schurPrincipal_eq_zero_iff` is quantified over **every** `YoungDiagram` and
**every** level `r`. There is no `n`-cap and no row-count restriction; `n` does
not appear in the statement at all, which is what "all `n`" means here.

### The genericity hypothesis is real, and it is satisfiable

The theorem assumes `∀ k ≠ 0, Q^k ≠ 1`. That is not decoration — at a root of
unity the statement is **false**: a hook length can kill a denominator, and
numerator factors can vanish away from content `−r`. It is exactly the
condition under which `H_n(Q)` is semisimple and the weights are defined.

An `iff` behind an unsatisfiable hypothesis proves nothing, so satisfiability
is proved rather than waved at: `not_root_of_unity_of_pos_ne_one` derives the
hypothesis from `0 < Q`, `Q ≠ 1`, which holds at the substrate
(`Q = q₀² ≈ 1.232`).

And `discriminates_at_n_three` checks the criterion is not answering "zero" to
everything: over `ℚ` at `Q = 2` it derives that `(1³)` has weight zero and
`(2,1)` does not — the two blocks #5185 measured.

### Verification

> **Snapshot note.** The declaration table above and the axiom block below
> record the file **as of #5217** (11 declarations). #5230 added the
> `IsOcneanuWeightSystem` class and eight further declarations without changing
> any of these; the current full list is in
> [`2026-08-16-ocneanu-weight-axiomatisation.md`](2026-08-16-ocneanu-weight-axiomatisation.md).

`lean`-direct against the real import cone, **exit 0**, no warnings, 2.0 s.
Not via `lake build`: this tree is a cache restore with no `.trace` files, and
`lake build` would evict it (bean `qou-r13s`). Mathlib olean count **6990**
before and **6990** after.

```
'QOU.QBeta.WenzlWeight.one_le_hook'                        [propext, Classical.choice, Quot.sound]
'QOU.QBeta.WenzlWeight.wenzlLevel_conventionD'             [propext, Classical.choice, Quot.sound]
'QOU.QBeta.WenzlWeight.colLen_gt_of_content_eq_neg'        [propext, Classical.choice, Quot.sound]
'QOU.QBeta.WenzlWeight.schurPrincipal_eq_zero_iff'         [propext, Classical.choice, Quot.sound]
'QOU.QBeta.WenzlWeight.conventionD_weight_eq_zero_iff'     [propext, Classical.choice, Quot.sound]
'QOU.QBeta.WenzlWeight.conventionD_weight_eq_zero_iff_rowLens'  [propext, Classical.choice, Quot.sound]
'QOU.QBeta.WenzlWeight.conventionD_weight_ne_zero_of_two_rows'  [propext, Classical.choice, Quot.sound]
'QOU.QBeta.WenzlWeight.not_root_of_unity_of_pos_ne_one'    [propext, Classical.choice, Quot.sound]
'QOU.QBeta.WenzlWeight.colLen_ofRowLens_one_one_one'       [propext, Classical.choice, Quot.sound]
'QOU.QBeta.WenzlWeight.colLen_ofRowLens_two_one'           [propext, Classical.choice, Quot.sound]
'QOU.QBeta.WenzlWeight.discriminates_at_n_three'           [propext, Classical.choice, Quot.sound]
```

No `sorryAx` anywhere. No `sorry`, no `native_decide`, no `axiom`, no
`: True`, no conditional class carrying the conclusion. This is a standalone
library file with no `.qa.json` sidecar, so nothing but this check covers it
(AGENTS.md §"QA is agent-owned").

## What is NOT proved here — read this before citing

**One external input, and it is a published theorem, not a gap in the
argument.**

> **Wenzl (1988), *Hecke algebras of type `A_n` and subfactors*, Invent. Math.
> **92** 349–383** — that the Ocneanu/Markov trace weights on `H_n(Q)` at
> Markov parameter `z_W = Q^r(1−Q)/(1−Q^r)` **are** the principal
> specialisations `s_λ(1, Q, …, Q^{r−1})`.

That is the "Ocneanu-trace weight formula" of #5207's own phrasing — the
*route* it named, supplied as the given. Quoted from Orellana p. 17, read
locally (`library/arxiv-math-9806163v1/9806163v1.pdf`).

> **Superseded 2026-08-16 by [#5230](https://github.com/litlfred/qou/pull/5230).**
> This paragraph read: *"It is cited with `-- Ref:`, not axiomatised: no Lean
> `axiom`, no conditional `class`, nothing in the signature carrying it."*
> That was true when written and is **now false**. On owner direction the input
> has been **axiomatised** as the class `IsOcneanuWeightSystem`, threaded as an
> explicit `[Instance]` hypothesis (AGENTS.md §3b-cond).
>
> **Nothing became more proved.** The statements in the table above are still
> exactly as proved as they were. What changed is that the three statements
> about the **actual Ocneanu weight** — as opposed to the `schurPrincipal`
> formula — now carry the dependency in their types and wear `_of_wenzl` in
> their names, and must be cited as *"proved conditional on Wenzl 1988"*.
> The unconditional core, `schurPrincipal_eq_zero_iff` included, is untouched.
> Class design, the conditional/unconditional boundary, and a scoping of the
> route to unconditional:
> [`2026-08-16-ocneanu-weight-axiomatisation.md`](2026-08-16-ocneanu-weight-axiomatisation.md).

Two things soften the dependence without removing it:

1. **The Lean is about the corpus's actual production weight.** `schurPrincipal`
   is a verbatim transcription of what
   `wedderburn_jones_markov.y_lambda_at` computes (via `y_lambda_su_n` /
   `schur_principal_mpmath`). Wenzl is needed for "and that function is the
   trace's Wedderburn weights" — a pre-existing corpus commitment, not
   something this lemma introduces.
2. **At `n = 3` the bridge is independently verified.** #5185 solved the three
   defining trace equations symbolically over `ℚ(q)` — `tr(1) = 1`,
   `tr(σ₁) = z`, `tr(σ₁σ₂) = z²` — and got exactly these weights, without
   going through Wenzl. The probe reproduces that.

**Also not proved here** (unchanged from #5207, and not claimed): that
`TL_n := H_n/⟨E⁽³⁾⟩` — that is Jones's definition — and that the blocks of
`TL_n` are the `≤ 2`-row `λ`, which is classical TL structure theory.
Formalising `H_n(q)` and `TL_n` as Lean objects remains the larger build
#5185 described, and this file does not attempt it.

**Scope note.** Nothing here is a refutation, and no scope-(b) structural
exclusion is claimed. The one negative — the criterion is false at a root of
unity — is a statement about the hypothesis, not about the framework.

## Cross-check

Exactly over `ℚ(q)`, no float64 anywhere (sympy `cancel`/`simplify`, exact
integer combinatorics):

| Check | Result |
|---|---|
| Lean `rowLen`/`colLen` definitions vs corpus arm/leg | **416 cells**, all partitions of `n ≤ 8`, identical |
| `Q^r` at `z_D` | `q⁴ = Q²`, `r = 2` exactly |
| `n = 3` weights vs #5185 | `(q⁴+1)/(q²+1)²`, `q²/(q²+1)²`, `0` — exact match |
| two-row weights vs Lean `TemperleyLiebTower.yw = [n−2k+1]_q/[2]_q^n` | **18** cases, `n = 2 … 7`, exact |
| `y_λ = 0 ⟺ ℓ(λ) ≥ 3` | `n = 1 … 8`, every partition |
| `Σ (dim V_λ)²` over `ℓ(λ) ≥ 3` | `1, 10, 78, 588, 4611, 38890` = `n! − Catalan(n)`, `n = 3 … 8` |

The first row is the one that matters most for trusting the Lean: it is the
transcription check. The Lean states hook, content and `n(λ)` through
`YoungDiagram.rowLen`/`colLen`, while the corpus states them through
arm/leg — a silent divergence there would make a correct proof about the
wrong object, and it is the only failure mode a proof-checker cannot catch.

The last row extends #5207's `1, 10, 78, 588` by two terms. Those two are
predictions of the proved statement, not new measurements.

## Consequence

The n = 6 result stands where #5207 left it, but the ladder above it is no
longer open-ended. `Catalan(n)/n!` collapses, and the fraction of `H_n` the
Markov–Gram form annihilates now has a proof rather than an extrapolation
behind it — `81.7 %` at `n = 6`, and `→ 1` as `n` grows. Any compute treating
`G` as a form on `H_n` rather than on `TL_n` is working in the kernel, and
that is now a theorem about every `n` rather than an observation at four of
them.
