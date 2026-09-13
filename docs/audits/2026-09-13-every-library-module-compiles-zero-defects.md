# The sizing answer: ZERO of 2836 library modules are broken

*2026-09-13, `--all` sweep on `main` `e22bd4561` (= `main` + a docs-only branch).*

## The measurement

```
scripts/lean-library-sweep.py --package QOU --all --jobs 2

  library modules        2836
    never built (new)     134   [measured]
    source-changed        n/a  (--all: freshness rule not consulted)
    TO COMPILE (--all)   2836   [= every module]
  parallelism: --jobs 2 x 2 thread(s) = 4 of 4 cores

=== library sweep: 2821 ok, 0 RED, 1 TIMEOUT + 0 UNVERIFIED (NOT failing),
    14 skipped (dependency red), 11426s ===
```

**Zero RED. Zero UNVERIFIED.** 3 h 10 m, every module compiled from source.

## What was being asked, and why it was stuck

Bean `qou-g5sp` established that **most of this library is outside `lake build
QOU`'s import closure** — the sweep's own `--all` help text puts it at *1863 of
2773* (that figure is the tool's; this run did not re-derive it). The obvious
follow-up was: *of those, how many are actually broken?*

I proposed two methods for it and **retracted both as unsound** — each inferred a
property of the *corpus* from a property of this container's *build state*. I then
recorded that answering it needed a different build environment. **That was also
wrong**, and it is the third retraction in this arc: `--all` with `--only`
chunking exists precisely to fit a constrained container, and here it did the
whole library in one pass on 4 cores.

## The answer

**Zero.** Nothing in the library is broken. Combining this run with the
root-targeted run from the same session (`2026-09-13-library-root-compiles-1451-modules-zero-red.md`):

| | count |
|---|---|
| library modules | **2836** |
| `ok` in this `--all` run | 2821 |
| additionally `ok` in the root run (of the 15 left unjudged here) | 9 |
| **judged `ok` across the two runs** | **2830** |
| still unjudged | **6** |
| **RED, either run** | **0** |

## Why a RED here would have meant something, and why 0 therefore does

Established by reading `lean-library-sweep.py` before the result landed, so the
reading rule was fixed in advance rather than fitted to the answer:

- **Nothing is trusted.** Under `--all` the freshness rule is never consulted;
  every module is rebuilt from source in topological order into the shadow. A
  dependent cannot be compiled against a stale dependency olean because no stale
  olean is in play. That is **5 of the 10 REDs** from my corpus-typecheck —
  structurally impossible here.
- **A signal death is not a RED.** `rc < 0` (SIGSEGV) is classified `UNVERIFIED`
  and printed *"NOT a corpus defect on this evidence"* (script lines 600-615).
  That is **the other 5**.
- **TIMEOUT is its own label**, not RED.

So a RED in this run would have been a **source error against QOU source**. There
were none. The residual conditionality is against **Mathlib**, whose oleans are
restored rather than rebuilt — a Mathlib-side mismatch remains possible; a QOU-side
one does not.

## 🛑 The reframing — and the premise `qou-g5sp` was built on is FALSE

I first wrote this section as *"`lake build QOU` does not reach them"*. **It does.**
The paper lakefile declares the library with an explicit glob:

    [[lean_lib]]
    name = "QOU"
    srcDir = "."
    # WIDEN THE BUILD TO THE WHOLE TREE (bean qou-rc7b).
    globs = ["QOU", "QOU.+"]

A Lake library with no `globs` defaults to `roots.map Glob.one` — root plus its
transitive imports, the state `qou-g5sp` describes. **That ended 2026-08-08**, a
month before the bean was opened, when `qou-rc7b` (`done`) added the glob. It is on
`origin/main`. So `lake build QOU` compiles **all 2836**. Corroborated by the
background build's own log: `[6459/6460] QOU.Eightfold.ObstructionClassForcesComplexType`,
a job count only a whole-tree build reaches.

**Import closure ≠ build coverage**, and the bean treated the first as implying the
second. Measured today by walking `import` lines transitively from `QOU.lean`:

    library modules                 2836
    reachable from QOU.lean         1451   (51.2%)
    OUTSIDE the import closure      1385   (48.8%)

The **67 %** figure `qou-g5sp` asserts twice is **not reproducible** and is
withdrawn; `qou-rc7b` independently measured 47 % in August on a smaller tree,
consistent with today's 48.8 % and not with 67 %.

### So what IS the gap?

Not build coverage — **nothing runs that build automatically.** CI auto-triggers
are off repo-wide (`build.yml` is `workflow_dispatch`-only, owner directive
2026-06-30). A breaking change lands and nothing notices until an agent builds or
sweeps by hand. That is how `BruhatRankCriterion` went red (`qou-1u90`, #7185) —
**not** because the module was unreachable.

**This removes the owner decision I was about to raise.** I had named "reach them
from the root, or make the sweep the gate" as an owner call, three times. The first
half has been done for a month; the second is a CI-trigger question the owner has
ruled on twice, most recently 2026-08-09 *with this failure cost on the table*, and
AGENTS.md says not to re-propose it without a new reason. I have none. Withdrawn.

**None of this weakens the result above** — 2821 ok / 0 RED stands, and is *more*
interesting for it: these modules were being built all along.

## The 15 unjudged, and the honest remainder

One module timed out — `QOU.Machinery.HeckeH4BlockMap211`, at the default 1800 s —
and 14 were skipped behind it. It is **not a new problem**: the same module
compiled **ok** in the root run two hours earlier, at the same budget, while
sharing the machine with `HeckeH4BlockMap31`. It sits near the wall and lands on
either side of it depending on what else is running.

Nine of the 15 are covered by that root run (`QOU` itself, `HeckeH4BlockMap211`,
`HeckeH4Semisimple`, `HeckeH4Wedderburn`, `…WedderburnCoord`, `…WedderburnInv`,
`…WedderburnMulA`, `…MulB`, `…MulC` — all `ok`). **Six are genuinely unjudged:**

    QOU.Hecke.FullRankFromWedderburn
    QOU.Hecke.InstanceOnH3A
    QOU.Hecke.InstanceOnH4A
    QOU.Hecke.MarkovTraceOnH3A
    QOU.Hecke.MarkovTraceOnH4A
    QOU.Machinery.HeckeH4RepDecomp

**Four of those six are exactly the `QOU.Hecke.* H3A/H4A` family my bean named as
the SIGSEGV class** — the attribution #7272 retracts. So after compiling 2830
modules, the only set left unjudged in the entire library is the one I got wrong,
which is either poetic or a hint that something about that cone is genuinely
expensive. A re-run restricted to `QOU.Hecke` at `--timeout 5400` is in flight to
settle it; until it reports, **these six are unverified, not passing** — and this
document does not claim otherwise.

## Scope

- One library, `QOU`. **UGB and Fred2005 are not swept** by this script.
- `main` as of `e22bd4561`; the denominator is **2836**, not the 2833 quoted
  earlier in the session — a rebase onto current `main` added three modules
  mid-session, and the earlier figure is stale by exactly that.
- Conditional on the restored Mathlib snapshot, as above.
- "Compiles" is not "is correct": this measures elaboration, not whether any
  declaration says something true or non-vacuous. The vacuity, axiom and
  `#print axioms` gates are separate and are not run here.
