---
# qou-u5z0
title: 'AUDIT: a convention-C dependency can survive as a derived IDENTITY — invisible to every detector class'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T17:24:15Z
updated_at: 2026-11-18T08:30:27Z
parent: qou-cdx1
---

Found while sweeping for convention-C spellings during the `qou-cds1` excision.
**The instance is low-stakes; the class is not.**

## The instance

[`computations/qbeta/toroidal_harmonics.py:48-52`](../computations/qbeta/toroidal_harmonics.py):

    # The Markov parameter is z = sqrt(q)/(1+q). Let q = e^(-eta).
    # Then z = 1 / (2 cosh(eta/2)).
    # w = z^2 = 1 / (4 cosh^2(eta/2)) = 1 / (2 (cosh(eta) + 1))
    # Therefore, x = cosh(eta) maps to:
    x_w = 1/(2*w) - 1

The live line is `x_w = 1/(2*w) - 1`. That identity is **exact under convention
C and simply wrong under D** — measured at the proton pin, with `eta = -ln q`:

    C:  z = 0.49932033418369   w = z^2   1/(2w)-1 = 1.005448433353561 == cosh(eta)   TRUE
    D:  z = 0.61268803714647   w = z^2   1/(2w)-1 = 0.331960061687155  vs 1.005448…  FALSE

Off by a factor of 3, not a perturbation. The derivation is
`cosh(η) = 2cosh²(η/2) − 1` composed with `z_C = 1/(2cosh(η/2))`; neither step
survives `z_D = q³/(q²+1)`.

**Scope, stated honestly: LOW.** The module emits **no witness**, and its
apparent importer (`qbeta_toroidal_harmonics_basis_probe.py`) only names it in
its own docstring — it does not import it, and carries no `cosh`, no
`sqrt(q)` and no `z` of its own. So this is exploratory/standalone code, not
feeding production. Fix it when the file is next touched; it does not gate the
excision.

## The class — this is why it is filed

**A convention-C dependency can survive as a *derived identity*: no z
expression, no z literal, no witness edge.** Every detector deployed on this
campaign is blind to it:

| detector | keys on | sees this? |
|---|---|---|
| expression scan (mine) | `1/(sqrt q + …)`, `sqrt(q)/(q+1)`, return forms | **no** — no z expression in the code |
| value-literal scan (mine, `486178eb26`) | the decimal `0.49932…` | **no** — no literal |
| witness-layer intersection (sibling) | witnesses carrying the C fingerprint | **no** — emits no witness |
| consumer read-edge (sibling, #5669) | who *reads* a C-frame witness | **no** — no read edge |

The C-ness lives entirely in a **comment plus an arithmetic identity**. Only
re-deriving the mathematics finds it.

## How it was found, and the cheap generalisation

By enumerating **mathematically equivalent spellings of z_C** and grepping for
each, rather than grepping for the spellings already known. Seven forms all
evaluate to `0.499320334183694452` at the proton pin:

    1/(sqrt q + 1/sqrt q)      sqrt(q)/(q+1)        q**0.5/(1+q)
    (q**0.5 + q**-0.5)**-1     1/(2*cosh(ln q/2))   0.5/cosh(0.5*log q)
    Re 1/(2*cos(-i*ln q/2))

The **hyperbolic** family is the one that pays: `z_C = 1/(2 cosh(η/2))` with
`η = ln q`. Nothing in the campaign greps `cosh`.

Two notes for whoever automates this:

- **Narrow to the reciprocal shape.** Bare `cosh(` is **873** hits corpus-wide
  (toroidal harmonics, Ohtsuki ladders); `1/(2 cosh(…))` is 17, of which 15 are
  the harmonic normaliser `1/(2 cosh η)` — **no half-argument**, a different
  quantity. `z_C` needs `η/2`. The half is the discriminator.
- **Selftest with a negative case.** My first cut of the regex failed its own
  positive selftest (`mp.mpf(1) / (…)` is not a bare `1`), and would have
  reported a clean surface. Include the negative `two_cosh_u = 2 * mp.cosh(u)`
  so a widened pattern cannot silently swallow the normaliser.


## Second sweep round — three more equivalence classes, all CLEAN

Continued the method. Verified numerically that these also equal
`z_C = 0.499320334183694452` at the proton pin, then greped each with
selftests:

| spelling | corpus hits | verdict |
|---|---|---|
| `1/sqrt([2]_q + 2)` (also `1/sqrt(q + 1/q + 2)`, `1/sqrt((q+1)^2/q)`) | **0** | clean |
| `0.5*sech(ln q / 2)` | **0** | clean |
| `1/[2]_{sqrt q}` — reciprocal of `sqrt(q) + 1/sqrt(q)` | 2 files define it, **0 invert it** | clean |

The third needs the detail, because it is the near miss:

    qbeta_cosh_q_sinh_q_candidate_scan.py:72   two_q_half = mp.sqrt(q) + 1/mp.sqrt(q)
    qbeta_sym_part_hecke_natural_form.py:97    two_q_half = sp.sqrt(q) + 1/sp.sqrt(q)   # [2]_{q^(1/2)}

`1/two_q_half` **is** z_C exactly. Neither file takes that reciprocal — the
first only records it as witness data, the second **multiplies**
(`form_2 = -two_q_half * h_tilde**2 / 2`). So `[2]_{q^(1/2)}` is a quantity in
its own right here, a Hecke natural form, and both are legitimate.

**They are one reciprocal away, though.** A future edit that divides by
`two_q_half` becomes a convention-C site under a name containing no `z`, no
`sqrt(q)/(q+1)`, and no `0.49932`. Worth a watch pattern rather than a fix:
flag `/\s*two_q_half` or `two_q_half\s*\*\*\s*-1`.

**Net across both rounds:** ten equivalence classes enumerated, one live site
found (the hyperbolic identity above), one near-miss class recorded, the rest
clean. Recording the negatives so the next agent does not re-sweep them — the
value of the method is knowing which forms are *excluded*, not only which hit.


## 2026-10-10 re-audit verdict: **LIVE** (bean `qou-am5t`)

A convention-C dependency surviving as a DERIVED IDENTITY, invisible to every
detector. Live, and the bean's own framing is right: the instance is low-
stakes, the class is not. No value-based detector can see an identity that no
longer mentions `z`.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.

---

## 2026-10-10 — the class has a SECOND, bigger member, and it is now drained: 4 producers wrote convention C into their own witnesses as a STRING

Re-audit of the C→D migration tracker (session epic `qou-am5t`). This bean
filed the *derived-identity* shape. Chasing its own recommended discriminator —
the hyperbolic family, `z_C = 1/(2 cosh(η/2))` — turned up a different and more
consequential shape in the same family: **a convention surviving as a string
literal bound for a witness field.**

### What was found

Nine committed non-`_deprecated` witnesses carry the C formula as text:

```sh
grep -rln "sqrt(q)+1/sqrt(q)\|sqrt(q) + 1/sqrt(q)" --include=*.witness.json computations/ | grep -v _deprecated
```

They split three ways, and the split is the finding:

**(A) Correct records — 3 files, no action.**

| witness | why it is correct |
|---|---|
| `cal4-disguise-hunt` | the string is the **detector's own finding text** about C-blindness. Same adjudication as `intra_ordering_value_fingerprint_audit.py` in the comparison ledger: a detector must carry the value it detects with. |
| `h4-markov-weights-closed-form` | `markov_z_convention = "C (…) — deliberately, and ONLY here: this arm reproduces a C-era artifact and must be evaluated at the z that artifact used"`. **Exemplary** — this is exactly what a declared comparison arm should look like. |
| `qbeta/gram-mp-path-convention-d-migration` | `description` narrating the straddle that was **fixed**. Historical. |

**(B) Four producers whose live `z` is convention D and whose witness label was convention C — ALL FOUR FIXED HERE.**

| producer | live `z` (D) | C label site(s) | witness field |
|---|---|---|---|
| `qbeta/qbeta_symbolic_chain_alpha_b.py` | `:114` | `:233` | `/data/symbolic_closed_forms/z` |
| `qbeta/qbeta_alpha_eff_hoefsmit_symbolic_probe.py` | `:71` | `:16` docstring, `:107` banner, `:166` | `/data/alpha_eff_symbolic` |
| `deltalambda/nuclear_quotient_jones_torus_link_probe.py` | `:59` | `:16` docstring, `:146` | `/context/markov_parameter` |
| `rigid_monoidal_gap_invariance_check.py` | `:72` (as `Z`) | `:29` docstring, `:228-230` | `/data/hecke_convention` |

All four re-run after the fix: **exit 0, and the semantic diff of each witness
is EXACTLY ONE LINE — the label. Every number byte-identical.** That is the
cleanest available confirmation of the diagnosis: these producers have been
computing convention D all along and only *describing* themselves as C.

**(C) Two residual items, not fixed, recorded.**

- `demazure-markov-trace.witness.json` — producer `:167` is D, but the witness
  is genuinely `scriptHash`-stale (`f5171246af95` → `9a3af82f7874`) and
  `computedAt 2026-07-05`, i.e. **pre-ruling**. Its `sqrt(q)+1/sqrt(q)` is not
  a label: it is **substituted into every published `w0`** across every
  partition, so the whole symbolic payload is a C-frame object. This one the
  existing staleness gate *can* see; a re-run is a real recompute with real
  output changes and is **not** in scope for a label fix.
- `constit_factor_and_volhyp_test.py:98` — **not a defect.** Live `z` is D at
  `:86`; `"sqrt(q)+1/sqrt(q)"` is a **search-basis label** in a factor search,
  commented `# = 1/z`. The *comment* is now wrong (under D,
  `1/z_D = (q²+1)/q³ ≠ √q + 1/√q`) while the basis element is a perfectly
  legitimate expression to search over. Cosmetic; flagged, not changed.

### Why this bean is the right home: EVERY detector is blind, and for a NEW reason

The table in this bean's own §class section holds, and a fifth row is worse than
the four already there:

| detector | keys on | sees a C string in a witness field? |
|---|---|---|
| expression / shape scan | `z` **assignment and return expressions** | **no** — a string literal is not an expression |
| **value audit** (`scripts/convention-c-value-audit.py`) | compiles the RHS and **evaluates** it | **no** — the RHS is a Python `str`; it evaluates to **itself**, never to `0.4993…` |
| witness-layer intersection | witnesses carrying the C **fingerprint value** | **no** — there is no number, only text |
| witness staleness (`witness_dependency_drift.py`) | `scriptHash` drift | **no** — three of the four **MATCHED**, so it reported them *fresh*, and it was right: the witness faithfully recorded a producer that misdescribed itself |
| algebraic-signature counter-move (`(q²+1)` divides the peel denominator) | the **answer's** factorisation | **no** — no answer to factor |

The value audit is the one that matters, because it is the campaign's
evasion-proof detector: it cannot be beaten by re-spelling `z`, since it
evaluates rather than matches. **It is beaten by not being an expression at
all.**

**And this is the exact MIRROR IMAGE of the recorded root of taxonomy rows
22 / 25 / 26** — *"the interesting text is assumed to be a `str` in the AST, at
the call."* There, the interesting text was a `str` and the detector read it
positionally as an expression. Here the interesting text **is** a `str` and
every detector assumes it is an expression. Same assumption, opposite polarity,
and it hid the opposite half of the surface.

### Two smaller traps caught while measuring, each of which cost a wrong claim

Both are recorded because I made them, not because I avoided them:

1. **`computation.script` is the witness STEM, not a path.** A stem→producer
   resolver that transforms `nuclear-quotient-jones-torus-link` →
   `nuclear_quotient_jones_torus_link.py` reports **PRODUCER NOT IN TREE** for
   three of these six, because the producers carry suffixes the stem drops
   (`_probe`, `_check`, `_test`). All three are right there. A "producer
   missing" verdict from a stem transform is a statement about the transform.
2. **The identifier's CASE.** `rigid_monoidal_gap_invariance_check.py` binds
   `Z = Q**3 / (Q**2 + 1)` at `:72` — capital. A grep for a lowercase `z`
   assignment reports the file as having **no `z` binding at all**, and I wrote
   exactly that into its docstring before re-checking and correcting it in the
   same session. Same class as the Lean-side `markovZC` / `markovZc` collision.

### The original instance is STILL LIVE and is unchanged

`computations/qbeta/toroidal_harmonics.py:48-52` still carries
`x_w = 1/(2*w) - 1`, exact under C and off by a factor of 3 under D, with the
C derivation in the comment above it. Scope unchanged and still **LOW** (emits
no witness; its apparent importer only names it in a docstring). Left alone
per this bean's own instruction: *"Fix it when the file is next touched; it
does not gate the excision."*

### One figure in this bean has moved — re-measure, do not quote

This bean records *"bare `cosh(` is **873** hits corpus-wide"*. Measured
2026-10-10, excluding `.claude/worktrees/` and `_deprecated`: **473**. Whether
that is drain or a different exclusion set is **not** established here — the
bean does not say what its own scan excluded, and a live agent worktree inflates
any repo-root walk. The *discriminator* is unaffected and still works: the
reciprocal half-argument shape `1/(2*cosh(…))` returns **10 hits**, of which 7
are `scripts/convention-c-triage.py`'s own selftest and documentation, 1 is the
`pm_qm_pythagorean_identity` normaliser `1/(2 cosh η)` (**no half-argument** — a
different quantity, exactly as this bean warns), and 2 are the C sites named
above.

### Status

Staying `todo`. Part (B) is drained and part (A) needs nothing, but the bean's
**original** instance is still live by its own triage, and part (C) carries one
genuine stale-payload witness (`demazure-markov-trace`) whose re-run is a real
recompute. The class statement — *a convention can survive with no expression,
no literal, and no witness edge* — is what this bean is for, and it now has two
confirmed shapes rather than one.

Reproduce:

```sh
grep -rln "sqrt(q)+1/sqrt(q)\|sqrt(q) + 1/sqrt(q)" --include=*.witness.json computations/ | grep -v _deprecated
grep -rnE "1\s*/\s*\(\s*2\s*\*?\s*(mp\.)?cosh" --include=*.py . | grep -v worktrees | grep -v _deprecated
```

## Round 86 Progress (PR #8398)
- Branch: `feat/round86-irrcubic-resolvent3-dimsum5-tau1-satdiff-43c1`
- Commit 1 (code + probe): `b5de63778dc1a1dd5f06089955f845fb94bba20f`
- Commit 2 (witness): `cda43c1b21fb03c917cb1d6c4ebc184aeff1e706` (`scriptSha256 = d48339de07d62c85bc2a014c14ff39ca61b8c6091d44dbc01d9abdb15245ae18`)
