# The ten `lean.ref`s "with no formalisation" were nine mis-shaped refs and one false positive

**Date:** 2026-08-08
**Bean:** `qou-ref10`
**Branch / PR:** `claude/ref10-unformalised-lean-refs-v2-2026-08-08` / #4757
**Follows:** [`2026-08-08-lean-ref-molecular-namespace-and-weak-triage.md`](2026-08-08-lean-ref-molecular-namespace-and-weak-triage.md)

Bean `qou-ref10` carried the residue of the `lean.ref` drain (#4739) as ten refs
"with no sibling `.lean` and no module at the mapped path", split two ways:

> **Exists elsewhere — repoint (2).** `QOU.BraidsKnots.JSJ_volume_additivity`,
> `QOU.Archimedean.weierstrassProjection`.
>
> **Absent from the whole corpus (7).** The four `QOU.Eightfold.*`, plus
> `QOU.BraidKnot.chirality_frobenius_self_pairing`,
> `QOU.BraidKnot.GBResidueSpectralSum.spectral_decomposition`,
> `QOU.BraidsKnots.RamifiedDiscFusion`.

**The second category is empty.** Every one of the seven has a module in the
Lean tree. Nothing needed formalising, nothing needed demoting, and no `sorry`
was added.

## 1. What the "absent corpus-wide" verdict actually measured

The bean's classification rested on a corpus-wide declaration grep. That grep
enumerates the declaration keywords
`theorem|lemma|def|abbrev|structure|class|inductive|instance` — and so does not
see:

| shape | ref it wrongly condemned |
|---|---|
| `axiom` | `JSJ_volume_additivity` (also the #4739 §1 case, `s5_acts_on_ew_slice`) |
| `opaque` | `weierstrassProjection` |
| **class field** | `GBResidueSpectralSum.spectral_decomposition` |
| module name used as a ref | the four `Eightfold` refs, `RamifiedDiscFusion`, `chirality_frobenius_self_pairing` |

This is the **fourth** instance in this drain of the same failure mode #4739 §1
named: *a resolver reporting a confident wrong answer rather than no answer.*
The first was the `axiom` omission; then the namespace-vs-declaration confusion
in §2; then the `molecular-construction/` namespace defect in §4; now `opaque`
and class fields. A declaration enumerator that is not derived from the Lean
frontend will keep producing this class of error.

## 2. `weierstrassProjection` was worse than broken — it mis-resolved silently

`lean.ref` resolves by **module path**: the resolver walks
`<lakeRoot>/<prefix as path>.lean` from the full ref down to two components.

`QOU.Archimedean.weierstrassProjection` therefore tries
`QOU/Archimedean/weierstrassProjection.lean` (absent), then
`QOU/Archimedean.lean` — **which exists**, and contains no Weierstrass
declaration at all. So the block did not present as broken; it presented as
resolved, against the wrong file.

A ref that mis-resolves is strictly more dangerous than one that fails, because
nothing surfaces it. Worth a checker: *the resolved file must contain the ref's
final component.* That check is a dozen lines and would have caught this one,
the `RamifiedDiscFusion` case, and the `chirality_frobenius_self_pairing` case
in one pass.

## 3. `QOU/Eightfold/` — the chapter is formalised; two files had no namespace

Five modules exist: `Sym2Gate`, `Sym2GateParity`, `RowCapObstruction`,
`GellMannOkuboIdentity`, `WeylInvarianceQDeformation`. Three carried a namespace
matching their module path. **`Sym2Gate.lean` and
`WeylInvarianceQDeformation.lean` declared everything at the root** — violating
AGENTS.md §2 (*all declarations live under the `QOU` root namespace*) and making
every ref into those modules name a declaration that does not exist.

Same defect as the `molecular-construction/` chapter (#4739 §4), in a chapter
that had just been audited: `WeylInvarianceQDeformation.lean` was repaired
three days earlier ([weyl-invariance-file-repair](2026-08-08-weyl-invariance-file-repair.md))
for compiling-red and a tautological headline, and the missing namespace went
unremarked — because the repair was driven by reading the *proofs*, and the
namespace is not a proof property.

Both files now carry `namespace QOU.Eightfold.<Module>`. Blast radius nil: no
Lean file references any of their declarations, and no module imports
`QOU.Eightfold.*`.

## 4. Per-ref disposition

| block | old ref | new ref | note |
|---|---|---|---|
| [`jsj-decomposition-linearity`](../../content/quantum-observable-universe/braids-and-knots/jsj-decomposition-linearity.md) | `QOU.BraidsKnots.JSJ_volume_additivity` | `…LinearJSJVolume.JSJ_volume_additivity` | `axiom` stating exactly the block's headline equation |
| [`glossary-weierstrass-projection`](../../content/quantum-observable-universe/glossary/glossary-weierstrass-projection.md) | `QOU.Archimedean.weierstrassProjection` | `…WeierstrassProjection.weierstrassProjection` | was **mis-resolving**, see §2 |
| [`color-su3-from-g2`](../../content/quantum-observable-universe/eightfold-way/color-su3-from-g2.md) | `QOU.Eightfold.Sym2Gate` | `…Sym2Gate.sym2_dim_3` | only the dimension arithmetic is backed — see §5 |
| [`a2-from-three-strands`](../../content/quantum-observable-universe/eightfold-way/a2-from-three-strands.md) | `QOU.Eightfold.WeylInvarianceQDeformation` | `….cartanMatrix_A2` | the `def` packaging the A₂ datum; no theorem states the block's headline |
| [`q-deformation-weight-lattice`](../../content/quantum-observable-universe/eightfold-way/q-deformation-weight-lattice.md) | `QOU.Eightfold.WeylInvarianceQDeformation` | `….cartan_fixed_while_qSerre_moves` | the file's own docstring calls this "the file's actual claim"; it is this block's claim too |
| [`schur-weyl-eightfold`](../../content/quantum-observable-universe/eightfold-way/schur-weyl-eightfold.md) | `QOU.Eightfold.RowCapObstruction` | `….weyl_dim_alt_eq_zero_iff` | the row-cap obstruction the module is named for |
| [`meson-mass-splitting`](../../content/quantum-observable-universe/eightfold-way/meson-mass-splitting.md) | `QOU.Eightfold.GellMannOkuboIdentity` | `….gmo_cannot_discriminate` | backs the **negative**, as the manifest already said |
| [`chirality-from-frobenius-self-pairing`](../../content/quantum-observable-universe/mass-theory/chirality-from-frobenius-self-pairing.md) | `QOU.BraidKnot.chirality_frobenius_self_pairing` | `….chirality_amphichiral_via_qInt3` | item 2 of 3; items 1 and 3 unformalised |
| [`ramified-disc-fusion`](../../content/quantum-observable-universe/mass-theory/ramified-disc-fusion.md) | `QOU.BraidsKnots.RamifiedDiscFusion` | `….resolvent_agreement` | claim 3 of 3; claims 1 and 2 unformalised |
| [`gs-spectral-decomposition-existence`](../../content/quantum-observable-universe/mass-theory/gs-spectral-decomposition-existence.md) | — | **unchanged** | false positive: a class field, §1 |

Every rewrite was applied only after confirming (a) the module path resolves and
(b) the ref's final component is present in the resolved file. Both checks run
green on all ten.

**No ref was pointed at something stronger than its target proves.** Where the
target is narrower than the block — six of the nine — the `.ts` manifest now
states in plain terms what is and is not machine-checked, following the pattern
already used by `schur-weyl-eightfold.ts` and `meson-mass-splitting.ts`.

## 5. Not repaired here: `Sym2Gate.lean` is vacuous

Its representation-theoretic content does not survive reading:

- `su3_sym2_irreducible` is an **`axiom … : True`**. It asserts nothing — any
  proof of `True` discharges it — so nothing downstream gains content from it.
- `corpus_T1_fails_sym2_gate` and `octonion_3_passes_sym2_gate` conclude
  `1 + 5 = 6 ∧ 1 > 0` and `6 = 6 ∧ 0 = 0`. The representation theory lives
  entirely in the docstrings.

This is bean `qou-8fl1` item 3 and has an owner; the weyl-invariance audit
already deferred it there, and the chapter prose labels the gate result honestly.
It is **not** repaired here. What this pass adds is a docstring recording the
vacuity **at the point of use**, plus a manifest comment on `color-su3-from-g2`
saying the block's headline (PSL(2,7) colour from the octonionic G₂) has no
Lean formalisation anywhere in the corpus — nor does the scope-(b) marked-pair
obstruction its `.md` derives, which is verified in exact arithmetic by
`s4_marked_pair_obstruction.py`, not in Lean.

The parity criterion that actually decides the Sym² gate **is** properly
formalised, sorry-free, next door in `QOU.Eightfold.Sym2GateParity`. It is not
used as `color-su3-from-g2`'s ref because it is a statement about `SU(2)`
irreps, and citing it for an `SU(3)` claim would be a mis-citation of exactly
the kind this drain exists to remove.

## 6. Verification

| check | result |
|---|---|
| `bun run scripts/run-validate.ts content/quantum-observable-universe` | **byte-identical** to `origin/main` (`908481c9d7`) — 29 issues before, 29 after, same lines |
| `lean`-direct, `-DautoImplicit=false`, on every module touched or cited | **exit 0** ×9 |
| `sorry` added | **none** |
| ref resolution (module path + final component present) | 10/10 |

The 29-issue baseline is worth recording: bean `qou-ref10` quotes
`✓ Valid — 10 issue(s)`, which is stale. `main` itself now reports 29 (the
`notation-register-tableN-data` blocks alone contribute ten `Unresolved uses: ""`).
Measured on `origin/main` in the same environment before touching anything, so
the comparison is like-for-like.

Never `lake build` — restored oleans plus `lean`-direct, per the standing
warning in `lean-environment-setup.md`.

### The authors-note preflight ⚠ is not this branch's

`scripts/check-sidecars.sh` flags *"authors-note Lean-coverage stats STALE
(proved-counts drifted)"* on this branch. It is **not** caused by these changes,
and this branch deliberately does **not** carry the refresh.

Running `scripts/refresh-authors-note.ts` on a **clean, detached
`origin/main`** in the same environment produces the identical result —
`684/704 (97.2%)` against the committed `688/704 (97.7%)`, plus two new
`lean-coverage.json` conjecture fields. So the drift is upstream: `main`'s most
recent commit at the time of writing was itself
`chore(authors-note): refresh stale Lean-coverage stats`, and the stat had gone
stale again by the next platform-script version.

Left alone on purpose. Folding it in would (a) make a `lean.ref` PR appear to
move a headline statistic it has nothing to do with, and (b) collide with
whoever is already running that refresh on `main` — doc currency is mechanical
work with one owner, which AGENTS.md says not to overlap.

**Anyone reading the preflight ⚠ on this PR should re-run the check against a
clean `main` before attributing the drift.**

## 7. Follow-ups not taken here

- **A resolved-file-contains-the-declaration check.** §2's mis-resolution is
  invisible to every current checker. Cheap, and would have caught three of the
  ten in one pass.
- **Derive the declaration enumerator from the Lean frontend.** Four regex
  omissions in one drain (`axiom`, `opaque`, class fields, namespace-vs-decl) is
  a pattern, not a run of bad luck.
- **`Sym2Gate.lean` vacuity** — bean `qou-8fl1` item 3, untouched by design.

## Appendix — the ref shape, since it is easy to get wrong

`lean.ref` is `"<package>:<Decl.Path>"`, and the resolver tries, in order:
the block's **sibling** `<rootName>.lean`; then `<lakeRoot>/<prefix>.lean` for
each prefix of the decl path, longest first; then a grep fallback.

So a ref that must resolve through the Lake tree has to be
**`<namespace path>.<declName>`, where the namespace path is also the module
path**. Two consequences that bit this drain:

- **A ref naming only the module resolves but names nothing.** That is the
  whole `Eightfold` group, plus `RamifiedDiscFusion`.
- **A ref using the bare qualified name does not resolve** when the namespace
  is shorter than the module path. `QOU.BraidsKnots.resolvent_agreement` is the
  true Lean name of the `RamifiedDiscFusion` theorem, and it would find
  neither `QOU/BraidsKnots/resolvent_agreement.lean` nor `QOU/BraidsKnots.lean`.

The corpus convention — namespace matching the module path, so both readings
coincide — is the one to author against. `polynomial-bar-involution` is the
clean exemplar: `namespace QOU.BraidKnot.PolynomialBarInvolution` in a sibling
`.lean`, so `QOU.BraidKnot.PolynomialBarInvolution.barPoly_involutive` is
simultaneously the fully-qualified name and a resolvable path. The two files
namespaced in §3 now satisfy it; `RamifiedDiscFusion` and
`chirality_frobenius_self_pairing` still do not (their namespaces are the
parent `QOU.BraidsKnots` / `QOU.BraidKnot`), so their refs resolve by path
without being the bare qualified name. Aligning those is a separate,
larger rename and was not attempted here.
