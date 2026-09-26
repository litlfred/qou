---
# qou-hdyp
title: 'GAP: Lean the Markov normalisation and trace identity that gate y_lambda'
status: completed
type: task
priority: normal
created_at: 2026-08-10T19:36:18Z
updated_at: 2026-08-16T11:56:18Z
---


## Why this is a GAP bean and not a Lean file

Per AGENTS.md §"When you can't close it — bean the gap": I could not write,
build and verify this Lean inside the remaining session context, and a file
that does not build — or that carries an uncited `sorry`, or concludes `True`
— violates §Strict Lean Discipline. Beaning is the sanctioned exit.

## What to state

Two theorems, the first strictly weaker and already symbolically confirmed.

**1. Markov normalisation** (verified symbolically, n = 2..6, exactly and
identically in q — see `qou-8x1l`):

    ∑ λ ⊢ n, y_λ(q) * dim V_λ = 1

**2. The trace identity** (the real gate; NOT yet verified):

    ∑ λ ⊢ n, y_λ(q) * χ^λ(β, q) = tr_M(β, q)      for every braid β ∈ B_n

Theorem 1 is the β = identity case of theorem 2, since `χ^λ(1) = dim V_λ`.

## Existing infrastructure to extend (do not start fresh)

    QOU/MathlibExt/MarkovTrace.lean          namespace QOU.MathlibExt.MarkovTrace
    QOU.Mathlib.HeckeAlgebra.MarkovTrace     abstract uniqueness class
    QOU.Braiding.HnMarkovTrace.MarkovTraceTower

Base ring: state over generic `{R : Type*} [CommRing R]` / `[Field R]` per
§7c — this is q-deformation combinatorics with no archimedean content, so ℝ
would be a gratuitous specialisation.

## Why it matters (the argument for formalize-first)

The convention-D `y_λ` were validated three ways — Rust `trace_weights_n` at
1.2e-15, all 3+-row weights vanishing, both table evaluations at ~1e-50 — and
**none of those tests the defining property**. Each compares the weights
against another implementation or a shared convention. Eight hypotheses were
raised and refuted chasing an 8.71e-8 Schur-Weyl residual before anyone
checked whether `Σ y_λ·dim = 1` at all. It does. Had theorem 1 been Lean from
the start, seven of those eight rounds were unnecessary.

Theorem 2 is where the surviving 8.71e-8 lives: with the weights now
vindicated, the residual must be in `χ^λ(β_D)` or in the peel recursion on
that specific braid.

## Note on process

The pre-create existence check returned a non-zero match count and I created
the bean before inspecting it. The two matches turned out to be unrelated
(`qou-78pt` A1 volume term, `qou-840k` float64 excision — my grep hit body
text, not titles), so this is not a duplicate. Wrong order all the same; the
check exists to be read, not counted.

## Build infra RESTORED and verified (2026-08-10)

`lake-cache/qou-v4-24-0` restored: 1.65 GB, **6990 oleans** (well above the
~2919 the skill doc cites). Toolchain `leanprover/lean4:v4.24.0` already
present. Total ~3 min, against a 30-60 min from-source Mathlib build.

**Working `lean`-direct recipe — note the `lean/` component:**

```bash
export PATH="$HOME/.elan/bin:$PATH"
LP=$(ls -d .lake/packages/*/.lake/build/lib/lean | tr '\n' ':')   # 8 dirs
LEAN_PATH="$LP" lean <file>        # exit 0 = checks, sorry-free
```

`lean-environment-setup.md` implies `.lake/build/lib`; on v4.24.0 the oleans
are under `.lake/build/lib/**lean**/Mathlib/...`. Using the documented path
fails with *"unknown module prefix 'Mathlib'"* even though 6990 oleans are
present — a confusing failure that looks like a bad restore rather than a bad
search path. Smoke-tested: a `CommRing` lemma importing
`Mathlib.Algebra.Ring.Defs` compiles, exit 0.

**Do NOT `lake build` to verify.** It re-resolves the dep graph, rebuilds
Mathlib from source, and drops the restored oleans (~40 min lost, per the
skill doc's own history note). `lean`-direct is the verification path.

Next agent: environment is ready; write theorem 1 and check it with the
recipe above. Re-seed the cache branch if a build materially extends it.

## prepare-merge: the witness conflicts are mechanical (2026-08-11)

The rebase (37 commits onto 1529) halts on the first commit with 11 `UU`.
Most are transient — replaying commit-by-commit conflicts files that the net
diff does not. Only **three** witnesses were genuinely changed by *both*
sides:

| witness | main | this branch | resolution |
|---|---|---|---|
| `alpha/alpha-k-jones-markov-h12` | convention C | convention C | either |
| `habiro/habiro-h9-spectral-decomposition` | convention C | convention C | either |
| `probes/markov-stab-trace-axis-probe` | **clean (D)** | convention C | **take main** |

Measured with `scan_doc` from `convention-c-witness-audit.py` against
`git show origin/main:<f>` and `git show HEAD:<f>`.

**Uniform rule: take main's side on all three.** No file here needs this
branch's version, and the third actively needs main's — upstream migrated it
to D while this branch still carries the stale C. Taking "mine" there would
*regress* a witness main already fixed.

Note the first two are still convention C on **both** sides: they are not
resolved by the merge, only un-conflicted. They belong to the `qou-eea0`
regeneration backlog, not to this PR.

During a rebase, main is `--ours` and the replayed commit is `--theirs`, so
the resolution is `git checkout --ours <file>` — easy to invert under time
pressure, hence writing it down.

## Reuse pass result (step 2a)

- **Three-row vanishing: already on main, stronger.**
  `TemperleyLiebTower.conventionD_kills_antisymmetriser` (n=3, from the Markov
  moment equations) + `YoungDiagramThreeRowCorner.threeRow_vanishing_all_levels`
  (all n). Mine reach it only via the Wenzl-bridge factor at r=2 — a different
  route, weaker reach. Kept as the bridge-side mechanism with upstream named
  canonical in the docstring; not deleted, because the routes are genuinely
  distinct.
- **Normalisation `∑ y_λ·dim = 1`: NOT on main.** Nearest is
  `fr_weight_normalised` (DepthStratifiedFrobeniusReciprocity), a rearrangement
  for a single Frobenius-pulled-back weight — not a sum over partitions. So
  `markov_normalisation_two`/`_three` and both bridge lemmas stand as new.

## CLOSED — the identity holds identically in q, 2/2 atoms

`computations/markov/markov_identity_symbolic_probe.py` + witness
(`markov-identity-symbolic.witness.json`, `q0Anchor: independent`).

| atom | H_n | crossings | convention | residual |
|---|---|---|---|---|
| proton | 3 | 11 | `averaged-crossings` | **identically 0** |
| deuteron | 6 | 23 | `colour-weighted-averaged-crossing` | **identically 0** |

`Σ_λ y_λ(q)·χ^λ(β) = tr_M(β)` as an identity of **rational functions** — the
residual's numerator normalises to exactly 0, and evaluates to exactly 0 at
every sample point including q = 2, nowhere near either anchor. Zero `Float`
atoms on both sides and in every `χ`, which is the machine-checkable form of
"nothing here is pinned".

This is strictly stronger than the two facts it complements. `Σ y_λ·dim V_λ = 1`
evaluates at the **identity braid** (one point of the braid group); the ~1e-50
bridge-vs-peel agreements are **two points of the q-line**. The deuteron case
matters most: it is the smallest word carrying the colour-weighted p–n
interface.

### What had to be fixed first

The test could not run at all. `hecke_character_symbolic._q_character_compute`
— the symbolic path, `q` always a Symbol — called `d_for_ctype` without the
`delta=` override that function's docstring reserves for q-symbolic callers,
so an `averaged_weighted` crossing arrived as
`-0.499656072298243*q + 0.499656072298243/q`. **Every symbolic `χ^λ` for an
A ≥ 2 word held δ frozen at one anchor while presenting as a function of q.**
PR #5209.

### A retraction worth keeping

The first deuteron run reported "residual not identically zero" after 25
minutes. That was **my bug**: `sp.sympify` reading `y_λ` from the witness mints
a bare `Symbol("q")` (`commutative` only) while both other sides use
`hecke_symbolic.q` (`positive`, `real`, …) — different variables, so the
difference could never cancel. Caught by running the 0.7 s n=3 control before
saying anything. The tell: numerically 1.7e-73 relative at q₀ and exactly 0.0
at q=2, while `simplify` insisted nonzero. **Numerically zero everywhere and
symbolically nonzero is a symbol or normalisation problem, never a discovery.**

Guards added: bind on read; refuse a verdict when the residual has >1 free
symbol; and replace `simplify(r) == 0` — not a decision procedure, and it
failed here even after the symbols agreed — with the degree bound (a nonzero
rational `p/s` with `deg(p) = d` has at most `d` roots).

### Not claimed

General β, general n. Two atoms is two words. What is shown is that the
identity is not an accident of the anchor. The cost of going further is now
measured: the weighted δ makes the bridge 1525.9 s at H₆ against 0.5 s for the
colour-blind proton, because δ(q) = (q−1)²(1−q⁻⁴)/3 turns a scalar into a
degree-8 rational function. H₉ and above may not be feasible symbolically.
