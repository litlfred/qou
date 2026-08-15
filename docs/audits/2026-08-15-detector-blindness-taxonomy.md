# A detector is blind to the shape it keys on

**Bean `qou-2ixd`.** Nine detector generations across the convention-C excision,
each of which reported the surface clear, and each of which was blind to a
*shape* rather than to a case. Written down because the pattern recurred often
enough in one arc to be predictive, and because two of the failures were in
tools built specifically to prevent the previous one.

## The claim

Every detector here failed the same way. Not by being wrong about what it
looked at — each was correct on its own terms — but by keying on a **structural
form**, and thereby being unable to see the same fact expressed in a different
form. The blind spot is never a missing case in a list. It is the shape of the
question.

## The nine

| # | detector keyed on | blind to | exposed by |
|---|---|---|---|
| 1 | literal decimal strings (grep) | the fifteen spellings of one formula | 70 → 13 → 178, two published miscounts |
| 2 | `1/(sqrt-ish + …)` | the half-argument form `r/(r²+1)` | `y_lambda_cyclotomic_factor.py:48` |
| 3 | assignment **targets** | a convention computed into a `return` | `pyhecke.gram.z_mp`, + 5 live producers |
| 4 | `z`-named bindings | closed forms **derived** from `z` | `trM_sigma1_sq`, `W2`, `census_hopf` |
| 5 | expression **shape** | `1/(t + 1/t)` where `q = t**2` | `qbeta_5two…probe.py:139` |
| 6 | the **registry record** | the record going stale behind the code | R9 red on main; 25 false "leaks" |
| 7 | **module attributes** (R9) | anything computed inside a function | `gram.z_mp()`, `tr_m_mp()` |
| 8 | **each entry independently** (R9) | entries disagreeing with *each other* | `pyhecke.gram` exporting C and D |
| 9 | **static** analysis | a derived form drifting from its own `z` | `TR_M[5] = z³` (2026-05-19) |

## Four that are worth reading in full

### 3 — returned, not assigned

`scan()` matched an assignment whose *target name* contained `z`. So:

```python
def z_mp(dps=...):
    return +(1 / (_mp.sqrt(q) + _mp.sqrt(qi_)))
```

had no name to match and was invisible. `"178 → 0 actionable"` was never true;
adding return-scanning took it to 11, of which five were live producers in
`computations/`.

### 4 — migrating `z` is not migrating the file

`tr_M(σ₁²) = h·z + 1` holds for *any* Markov parameter. Written out at `z_C` it
becomes `1 + (q-1)/q^{1/2}` — and **the square root is `z_C`'s, not the
identity's**. So a file could migrate `z` to D and keep a closed form that
silently still described C. Four such sites, under names (`W2`, `W11`,
`trM_sigma1_sq`, `census_hopf`) that no `z`-keyed scan looks at.

The same identity existed in five copies. One of them — the sage example's —
drifted from the library and left `hecke_surface.py` **exiting 1 on main**.

### 5 — shape genuinely cannot decide it

```python
t = sp.symbols("t", positive=True)
q = t ** 2
z = 1 / (t + 1 / t)          # convention C
```

No `sqrt`, no `0.5`, not the `t/(t²+1)` form. And it is *character-for-character*
`1/(q + 1/q)` = `1/[2]_q`, the Temperley–Lieb loop reciprocal, which the
selftest requires **not** be flagged. The two differ only in whether the
variable is `q` or `√q` — a fact no expression shape carries. What decides it is
the file's own declaration `q = t ** 2`.

**A detector that reads only expressions cannot see a fact stated in a
declaration.**

### 6 — the tool inherits the record's staleness

`scan_reexports` derived its verdict from the registry's `blocked_migrations`.
`gram.py` migrated to D; the row still said `stays: C`. So the detector
faithfully reported 25 production sites "receiving convention C" that were
receiving D — and R9, which evaluates code rather than reading records, was red
on `main` the whole time.

This one produced a retraction (`qou-76a6`, scrapped). It is the sharpest form
of the pattern: **the failure the tool was built to find, arriving inside the
tool.**

## The counter-move that worked, twice

Numeric evaluation. R9 catches what R4/R5 cannot because a docstring and a
registry field can go stale *together* and still agree; code evaluated at `q₀`
cannot. R11 extends that to derived quantities: `z³` and `h·z²+z` are both
perfectly ordinary expressions in `z`, differing only in that one is right, and
**only evaluation distinguishes them**.

That is not an argument against static detectors — static scanning found sites
3, 4 and 5 — but against trusting them alone.

## The counter-move that failed

Breadth. The closed-form detector's first version matched any half-integer power
of `q` in a migrated file: **50 sites, nearly all legitimate**. `q^{1/2}` is not
a convention marker; it is `[2]_{√q}`, and it appears in Wenzl positivity, in
pair-skein formulas, and in the Jones change of variable.

`trace-convention-audit.ts` had already written this down —

> flagging those "would repeat the loose-grep error that once reported 70
> producers where the truth was 13"

— and it was repeated anyway, in a new detector, six weeks later. Narrowing to
trace/weight bindings took it 50 → 4. Most of that detector's selftest fixtures
now pin the *narrowing* rather than the matching, because over-breadth is its
whole risk.

## What the gates cover now

| rule | asks |
|---|---|
| R4/R5 | does the docstring match the registry? *(string vs string)* |
| **R9** | does the **code** return what the registry says, at `q₀`? |
| **R10** | do a module's symbols agree with **each other**? |
| **R11** | does a **derived** quantity match the `z` it was derived from? |

R10 exists because R9 checks entries independently: `pyhecke.gram` had `z`=D and
`z_mp`/`tr_m_mp`=C, all three accurately recorded, R9 confirming all three, and
nothing reported. A caller imports a module, not a registry entry.

## Practical consequences

1. **A local copy of a library value is a defect**, not a convenience. Five
   copies of one identity; the one that drifted broke an example on `main`.
   Canonical home: `closed_form_tau_M.trM_sigma1_sq` / `wenzl_weights_h2`,
   gated once by R11.
2. **A producer that runs at import cannot be gated by anything that imports
   it.** Three did, and rewrote their witnesses as a side effect of `import`.
3. **A detector needs fixtures that pin its narrowing**, not only its matching.
4. **Verify the premise of a record before deriving from it.** The registry is
   an input, not an axiom.

## Provenance

Every count here is from a committed instrument, not a hand survey:
`scripts/convention-c-producer-audit.py` (selftest 42/42),
`scripts/convention-c-witness-audit.py` (16/16),
`content/pipeline/witness-substitution-audit.ts` (19/19),
`docs/coordination/trace_convention_registry_validate.py` (R9/R10/R11).

R11's negative test injected the historical `TR_M[5] = z³` bug and confirmed the
gate fires; the three published miscounts and one retraction in the table above
are recorded in `qou-2ixd` and `qou-76a6` rather than quietly fixed.
