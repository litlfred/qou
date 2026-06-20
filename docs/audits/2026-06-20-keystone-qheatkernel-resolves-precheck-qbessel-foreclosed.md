# Keystone q-heat-kernel resolves the precheck; q-Bessel binding/finite-n foreclosed (2026-06-20)

**Branch:** `claude/kind-ptolemy-acladr`
**Status:** reconciliation (corpus-grep). Two foreclosures + one resolution, all from existing
corpus content. No new probe was run that re-walks settled work; one verification compute (exit 0).
**Discipline:** corpus-grep + critical-distance + formalize-first.

## TL;DR

Following the owner's q-heat-kernel / q-Bessel(2nd-kind) lead, corpus-grep shows the direction is
**far more developed than the 2026-06-20 lead doc implied**, and resolves the open question that doc
left:

1. **The precheck's "P1 fail" (Σ W_λ = 0.982 ≠ 1) is a normalizer artifact, RESOLVED.** The
   compact q-heat-kernel (`prop:q-heat-kernel-peter-weyl`, already in content) has trace
   `Z(t) = Σ_λ d_λ(q)² e^{-μ_λ(q) t}`; its `t→0` value `Z(0) = Σ_λ d_λ² = 128.979` (at q₀, n=5) is
   the correct normalizer, and `d_λ²/Z(0)` IS a probability measure (`Σ = 1.0000000000`). The
   precheck's `[n]_q! = 131.313` was simply the wrong normalizer; `0.982224 = Z(0)/[5]_q!` exactly,
   and the "mass defect" `1 − 0.982 = ([5]! − Σd²)/[5]! = 0.017776`.
2. **The geometric realization is the COMPACT q-heat-kernel, NOT the non-compact q-Bessel.** The
   2026-06-20 lead pointed at q-Bessel / E_q(2) (2nd kind); corpus-grep
   (`2026-06-14-qbessel-lead4-mu-lambda-qlommel-derivation.md`) shows the finite-n keystone object
   is the **compact SU_q(2) q-Casimir** spectrum `{μ_λ}`, whose heat kernel is exactly
   `prop:q-heat-kernel-peter-weyl`. q-Bessel is the **n→∞ tower** (E_q(2) contraction), a different
   sector.
3. **Both of this session's menu options are foreclosed by existing work** (do not re-walk).

## Option 2 (q-Bessel orthogonality measure ∝ W_λ at partition points) — FORECLOSED

`2026-06-14-qbessel-lead4` settled, by exact symbolic algebra in ℚ(q), that the finite per-n
partition spectrum is **not** a q-Bessel / q-Lommel zero spectrum: `{μ_λ}` is algebraic (rational in
q), finite of size `p(n)`, with `p(n) ≠ n` for `n ≥ 4` (so not the degree-n q-Lommel zero set), and
is the **compact** Casimir, while q-Bessel zeros are the **non-compact** E_q(2) spectrum. Partitions
do not land on the q-Bessel zeros, so "orthogonality measure at partition points" is ill-posed for
finite n. The radial/orthogonality check option 2 proposed is therefore structurally foreclosed; the
right object is the compact heat-kernel trace (this audit).

## Option 1 (q-Bessel 2nd-kind "quadratic action" → binding correction) — LARGELY RETIRED

`2026-06-14-qbessel-joint-ji-binding-probe` ran the joint rotation⊕growth (`J_ν ⊕ I_ν`) q-Bessel
combiner against the data-complete A≥3 binding cases: **NO-GO** — it degrades D / T / ³He
substantially (³He +17.4% → +117.9%, a 6.8× regression); the growth channel contributes ≈0, and the
data prefers the collapsed `|Δθ|` magnitude. PR #2279's q-Bessel "is not load-bearing for binding."
The productive binding directions remain GAP-A-3 / GAP-A-4 (Option E) + the ⁴He JSJ volume.

**The one untested sliver:** the literal *second-kind* (Neumann `Y_ν`, singular) solution — distinct
from the `J`/`I` pair the joint probe tested. But the prior is strongly negative (every q-Bessel
binding lever tried is refuted), and the "quadratic action" the owner names is already realized by
the **content-Casimir `μ_λ`** (quadratic in cell content), which is already wired into the q-heat-
kernel prop. So the 2nd-kind/quadratic structure is present and accounted for — as the heat-kernel
*eigenvalue* `μ_λ`, not a new binding correction term. Bean `qbk2` is updated with this finding and
redirected; it does not warrant a fresh binding probe (would re-walk the NO-GO).

## What is genuinely new and useful (this audit)

The precheck → compact-heat-kernel reconciliation:
[`scripts/keystone_qheatkernel_partition_function.py`](scripts/keystone_qheatkernel_partition_function.py)
(exit 0): `Z(0) = Σd_λ² = 128.979`, `d²/Z(0)` sums to 1.0 exactly, conjugation symmetry holds, and
`Z(0)/[5]! = 0.982224` reproduces the precheck. This identifies the keystone's geometric realization
target as the **compact `prop:q-heat-kernel-peter-weyl` at `t→0`**, supersedes the 2026-06-20
q-Bessel lead's object choice, and turns the "mass defect" into a precise statement:
`[n]_q! − Σ_λ d_λ²` is the gap between the naive `[n]!` normalizer and the heat-kernel partition
function (the two coincide only at `q→1`, where `Σ dim² = n!`).

## The remaining open keystone piece (unchanged, owner-gated DG)

Identifying the *measure* and its compact heat-kernel origin does **not** close the keystone. The open
object stays: does an **S¹-equivariant (Reeb-graded) index** — weighted by `e^{-μ_λ t}` with the
spatial-SO(3) Reeb action of the s5-so3 keystone — reproduce `d_λ²/Z(0)` geometrically, with the
conjugation symmetry arising from a Hodge-★/Poincaré-duality of the manifold? That is infinite-/
equivariant differential geometry, owner-gated, and not advanced here.

## Cross-references

- [`content/.../information-theory/q-heat-kernel-peter-weyl.md`](../../content/quantum-observable-universe/information-theory/q-heat-kernel-peter-weyl.md) — the compact heat-kernel prop (the correct object).
- [`2026-06-14-qbessel-lead4-mu-lambda-qlommel-derivation.md`](2026-06-14-qbessel-lead4-mu-lambda-qlommel-derivation.md) — finite-n ≠ Bessel-zero spectrum (forecloses option 2).
- [`2026-06-14-qbessel-joint-ji-binding-probe.md`](2026-06-14-qbessel-joint-ji-binding-probe.md) — joint J⊕I binding NO-GO (retires option 1's general direction).
- [`2026-06-20-keystone-qbessel-heat-kernel-lead.md`](2026-06-20-keystone-qbessel-heat-kernel-lead.md) — the lead this audit corrects (object was non-compact q-Bessel; should be compact q-heat-kernel).
- [`scripts/keystone_qbessel_plancherel_precheck.py`](scripts/keystone_qbessel_plancherel_precheck.py) — the precheck whose P1 this audit resolves.
