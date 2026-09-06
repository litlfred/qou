# `check-sidecars.sh` counted `(R := …)` as evidence of a generic declaration

**2026-09-06 · beans `qou-o43i` · fixed in `scripts/check-sidecars.sh` (fourth
false-positive class)**

## The defect

`check-sidecars.sh` classifies an un-sidecar'd library `.lean` against AGENTS.md
§7c. Its `GEN` regex — the test for "this file declares a **generic** result" —
included the literal `\(R\s*:=`. That is backwards twice over.

**It is a use site, not a binder.** `(R := ℝ)` is Lean's named-argument syntax at
an *application*. It is also the exact spelling §7c **prescribes** for the
archimedean sibling — *"consumes the generic result via a `(R := ℝ)`
instantiation"* — so a file that had been split correctly per §7c was reported as

    ⚠ §7c MIXED generic + archimedean → split into two files per §7c

which is the one edit that cannot help: there is nothing left to split.

**`R` is a parameter NAME, not a type.** Of the 31 occurrences measured, **9 bind
`R` to something that is not a ring at all**:

| file | occurrence | `R` is |
|---|---|---|
| `QOU/Archimedean/IdealTetEqChimney.lean` | `inscribedTriangle_vertex_incidence (R := 1)` | a radius |
| `QOU/Mathlib/BorelCaratheodory.lean` | `norm_le_of_re_le (R := 1) (M := 1)` | a radius |
| `QOU/QBeta/C1ConnectionPoles.lean` | `circleIntegrable_sub_zpow_iff (R := ρ)` | a radius |
| `QOU/MathlibExt/RootsOfUnityProduct.lean` | `Polynomial.natDegree_X_pow_sub_C (R := ℂ)` | `ℂ` |
| `UGB/GrobnerShirshov/HeckeCompletion.lean` | `(R := bsWord₂ a' a ⟨0, hn⟩)` | a **word** |

## The measurement

Over the **3666** non-`.lake` `.lean` files under `content/`, classifying each
twice — with and without `\(R\s*:=` in `GEN` — and diffing the verdicts:

| | count |
|---|--:|
| files where `hasGen` is set **solely** by `(R :=` | 19 |
| **files whose verdict changes** | **15** |
| … of those, `MIXED(action)` → `R-JUSTIFIED` | 15 (all) |
| occurrences sitting on a **declaration** line | **0 of 31** |

**Scope, stated honestly:** `check-sidecars` scans only *changed* files, so these
were never 15 live flags. They are 15 files **primed to mis-fire the moment
anyone edits one** — which is how it was found: by editing one.

The 15: `Archimedean/{DilogPartBAEAssembly, DilogPartBWP1Refutation,
IdealTetEqChimney, ObtuseWedgeDegenerate, OrthoschemeTiling}`, `Knot/BorromeanVolume`,
`Mass/LevelSelectionLogarithmic`, `Mathlib/{BorelCaratheodory, QGevreyOrder}`,
`MathlibExt/{GaussianTailBound, RootsOfUnityProduct}`, `QBeta/C1ConnectionPoles`,
`mass-theory/alpha-k-categorical-closure`,
`q-geometric-langlands/spectral-half-line`, `UGB/GrobnerShirshov/HeckeCompletion`.

## Why the narrowing is safe

Matching the safety argument of the three prior fixes recorded in the script
(`qou-mr3q`, `qou-akb4`, `qou-aemx`):

A genuine §7c violation is a file that **declares** something generic alongside
archimedean content. Declaring is announced by a **binder**, and all four binder
forms — `{R : Type}`, `[CommRing`, `[Field`, `[GroupWithZero` — remain in `GEN`.
So the narrowing cannot hide a violation; it can only stop counting an
application as a declaration. **Zero false clears.**

`hasGen` gates only the two branches that require a generic declaration
(`PRESCRIBED` and `MIXED`); a file with a real binder still reaches them by one
of the four surviving alternatives.

## Reproduction

```python
#!/usr/bin/env python3
"""Measure the `(R :=` blind spot: classify every content .lean twice."""
import re, subprocess
from pathlib import Path
ROOT = Path("/home/user/qou")

GEN_LIVE = re.compile(r'(\{R\s*:\s*Type|\[CommRing|\[Field\b|\[GroupWithZero|\(R\s*:=)')
GEN_FIX  = re.compile(r'(\{R\s*:\s*Type|\[CommRing|\[Field\b|\[GroupWithZero)')
RTYPE    = re.compile(r'(:\s*ℝ|\(ℝ\)|→\s*ℝ|ℝ\s*\))')
STRONG   = re.compile(r'(Real\.(sqrt|rpow|log|exp|cos|sin|pi|tan|arctan)|CODATA|MeV)')
ORDERED  = re.compile(r'(\blinarith\b|\bpositivity\b|\bnlinarith\b|LinearOrdered)')
WEAK     = re.compile(r'(0\s*<|<\s*1|≤|≥)')
DECCMP   = re.compile(r'([0-9]+\.[0-9]+[ \t]*[<>≤≥]|[<>≤≥][ \t]*\(?[ \t]*[0-9]+\.[0-9]+)')
DECL     = re.compile(r"^[ \t]*(?:noncomputable[ \t]+)?"
                      r"(?:theorem|lemma|def|abbrev|instance)[ \t]+([A-Za-z_][A-Za-z0-9_'.]*)", re.M)

def strip_comments(src):
    s = re.sub(r'/-([^-]|-+[^-/])*-+/', '', src)          # one-line /- ... -/
    out, deleting = [], False                              # sed range delete
    for line in s.split("\n"):
        if not deleting and "/-" in line:
            deleting = "-/" not in line[line.index("/-") + 2:]
            continue
        if deleting:
            deleting = "-/" not in line
            continue
        out.append(line)
    return re.sub(r'--.*', '', "\n".join(out))             # -- line comments

def verdict(body, gen_re):
    hasGen = bool(gen_re.search(body)); hasR = bool(RTYPE.search(body))
    hasS = bool(STRONG.search(body));   hasO = bool(ORDERED.search(body))
    hasW = bool(WEAK.search(body));     hasD = bool(DECCMP.search(body))
    hasJ = hasS or (hasO and hasR) or (hasW and hasR) or (hasD and hasR)
    decls = set(DECL.findall(body))
    paired = any(d.endswith("_real") and d[:-5] in decls for d in decls)
    if hasGen and (hasR or hasJ) and paired: return "PRESCRIBED"
    if hasGen and (hasR or hasJ):            return "MIXED(action)"
    if hasR and not hasJ:                    return "BASE-RING-MINIMAL(action)"
    if hasR or hasJ:                         return "R-JUSTIFIED"
    return "GENERIC-OK"

files = [ROOT / p for p in subprocess.run(["git", "ls-files", "content"], cwd=ROOT,
         capture_output=True, text=True, check=True).stdout.split()
         if p.endswith(".lean") and "/.lake/" not in p]
for f in files:
    body = strip_comments(f.read_text(encoding="utf-8", errors="replace"))
    if not GEN_LIVE.search(body):
        continue
    a, b = verdict(body, GEN_LIVE), verdict(body, GEN_FIX)
    if a != b:
        print(f"{f.relative_to(ROOT)}\n    {a} -> {b}")
```

## Consequence for this PR

`QOU/QBeta/SeparableInterfaceHypothesesHaveContentReal.lean` had been written
`@separability_hypotheses_have_content ℝ _` **specifically to dodge this
detector**, with a docstring saying so. The workaround is removed and the
§7c-prescribed `(R := ℝ)` restored; `check-sidecars` now reports the pair as
`no ℝ, generic OK` / `archimedean construct present, ℝ justified`, and both files
are `lean`-direct exit 0.

## What is NOT fixed

The same script's **content-block arm** prints
*"→ qa-sweep … (refresh stale criteria)"* for **every** changed block, with no
staleness test at all (`scripts/check-sidecars.sh`, content-block branch). The
line reappearing after a clean sweep is the script working as written, not a
failed refresh. Left alone deliberately: unlike the `GEN` defect it produces no
wrong *verdict*, only a suggestion that is always printed, and changing it would
need its own measurement of what "stale" should mean for a sidecar.
