# D11 is mis-scoped in both censuses: the block points at a vacuous stub while a substantive carrier exists

**Date:** 2026-09-05
**Branch:** `claude/d11-wigner-su4-carrier-content-2026-09-05`
**Beans:** `qou-tsnp` (12 `holds : Prop` carriers), `qou-hprp` (23, live)
**Status:** scoping correction on one census entry, plus one unambiguous fix.
**No new mathematics. No content written into any carrier.**

---

## VERDICT

**`WignerSu4FromSpinIsospin` (D11) is listed by `qou-tsnp` as a carrier that asserts
nothing. It is that — but repairing it the way D9 and D10 were repaired would be
wrong, because a *substantive* D11 carrier already exists under a different name and
namespace, with two real parameter-quantified fields and three honestly-labelled
`opaque marker` ones. The defect is not an unencoded conjecture; it is a block whose
`lean.ref` points at the wrong declaration. Writing content into the stub would
duplicate the real carrier rather than fix anything.**

---

## How this arose

D9 (`IsospinFromCanonicalBowtie`, #6671) and D10 (`SpinFromSo3Fiber`, #6683) were
repaired in `qou-tsnp`'s prescribed shape: replace `holds : Prop` with fields encoding
the block's content, caller-parameterised so the class is refutable, no instance. D11
was next on the list — it is what D9 and D10 feed. Reading it first, per that bean's
*"Not mechanical … do not batch-rewrite"*, is what found this.

## What is actually there — three names for one conjecture

| | declaration | location | content |
|---|---|---|---|
| **stub** | `QOU.BraidsAndKnots.WignerSu4FromSpinIsospin` (lower-case `u`) | `nuclear-interactions/wigner-su4-from-spin-isospin.lean` | `holds : Prop` — nothing |
| **library** | `QOU.WignerSU4FromSpinIsospin` (upper-case `U`) | `lean/QOU/ParticleInteractions/WignerSU4FromSpinIsospin.lean` | 2 real fields + 3 labelled markers |
| **docstring's claim** | `QOU.BraidsAndKnots.WignerSU4FromSpinIsospin` | `lean/QOU/BraidsAndKnots/WignerSU4FromSpinIsospin.lean` | **this file does not exist** |

The `.ts` refs the **stub**: `ref: "qou:QOU.BraidsAndKnots.WignerSu4FromSpinIsospin"`.
The stub's own header text disagrees with its own class by capitalisation *and* names a
third path that is absent from the tree.

## The library carrier is not vacuous

```lean
class WignerSU4FromSpinIsospin where
  su4_action : True                        -- `opaque marker`, labelled as such
  a_four_yields_singlet : True             -- `opaque marker`, labelled as such
  dynamic_capacity_from_plancherel_weight (A Z N : ℕ) (S W_lam E_gate E_0 : ℝ) :
    E_gate = E_0 * Real.log (1 / W_lam)    -- real, parameter-quantified
  dynamic_occupancy_c_lambda (B_AME E_gate c_lam : ℝ) :
    c_lam = B_AME / E_gate                 -- real, parameter-quantified
  alpha_cluster_from_su4_quadruplets : True -- `opaque marker`, labelled as such
```

Two fields are exactly the shape `qou-tsnp` asks for. The three `: True` fields each
carry an `opaque marker` docstring naming *why* they are unstatable — the SU(4)
representation infrastructure — which is the sanctioned opt-out, not a dodge.

**This is `qou-tsnp`'s own shadow case.** That bean already corrected its count 18 → 16
→ 12 by deleting four entries that *"do have substantive library formalisations,
declared under the ref's leaf name in a differently-named file, which a class-name match
misses."* D11 is a fifth instance the correction did not catch, because here the names
differ by **capitalisation and namespace** rather than by file name.

## Measured blast radius

- Consumers of the **library** class, excluding its own file and the `QOU.lean` import:
  **zero**.
- Consumers of the **stub** class: **zero** — the only other mention in the tree is a
  docstring in `content/pipeline/lean-vacuity-axiom-audit.ts`, which cites it as an
  exemplar of the `holds : Prop` shape.

So nothing depends on either, and the mis-ref has cost nothing yet beyond the census
mis-scoping.

## What this PR does, and what it deliberately leaves

**Fixed** — the stub's header, which was internally inconsistent: it named a
capitalisation its own class does not use and a file path that does not exist. That is
an unambiguous error and is corrected to describe what is actually there, including a
pointer to the substantive carrier.

**NOT done — the ref repoint, and this is a judgement for the author.** The obvious
repair is to point the `.ts` at the library class and delete the stub, per AGENTS.md
§0a (*"let the ref resolve to the library decl"*). Two things stop me doing it
unilaterally:

1. §0a's preferred form wants **candidate-2** resolution, i.e. the declaration's
   namespace matching its path. The library class is `namespace QOU` at
   `QOU/ParticleInteractions/`, so a repoint to `qou:QOU.WignerSU4FromSpinIsospin`
   would resolve only by the grep fallback.
2. Aligning the namespace to `QOU.ParticleInteractions` would make candidate 2 work —
   but that directory has **no single convention** (`QOU.Atomicity`,
   `QOU.ParticleInteractions`, `QOU.BraidKnot`, and bare `QOU` in `HadronDisplay.lean`
   all appear), so I would be imposing a convention rather than following one, on a
   file this branch does not otherwise touch.

Both are cheap and safe given the zero-consumer measurement; which is *right* is a call
about pipeline convention, not about the mathematics. Recorded rather than guessed.

**NOT done — writing content into the stub.** That was the plan on arrival and it is
the wrong repair: it would create a second D11 carrier competing with the real one.
Recorded because "apply the same fix as last time" is exactly the reflex this case
defeats.

## Consequence for the two censuses

`qou-tsnp`'s count of 12 and `qou-hprp`'s of 23 both include this entry as a carrier
needing content. For D11 that is **not** the repair. Neither count is wrong about the
*syntax* — the stub does declare `holds : Prop` — but the queue's implied action does
not apply here. Corrected in both beans.

## References

- `content/quantum-observable-universe/nuclear-interactions/wigner-su4-from-spin-isospin.lean`
  — the stub; its `.ts` and its `.md`.
- `content/quantum-observable-universe/lean/QOU/ParticleInteractions/WignerSU4FromSpinIsospin.lean`
  — the substantive carrier, imported at `QOU.lean:421`.
- [`2026-08-23-free-prop-field-census.md`](2026-08-23-free-prop-field-census.md) — the
  corpus census (PR #5562) and `scripts/free-prop-field-audit.py`.
- #6671 (D9) and #6683 (D10) — the two carriers where the content repair *was* correct.
