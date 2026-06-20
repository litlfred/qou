# Keystone q-deformed shift — first structural crack via the canonical H₃→H₅ lift

**Date:** 2026-06-20
**Branch:** `claude/keystone-q-shift-structural-crack-2026-06-20`
**Scope:** First structural crack at the open q-deformed closure of
`conj:s5-so3-fiber-action` (the keystone), now that `pyhecke_native` builds in
the web sandbox (PR #2511). Resolves a standing "open input" objection and
reports the RAW operator-valued branching shift.
**Compute:**
[`docs/audits/scripts/keystone_h3_h5_lift_block_shift.py`](scripts/keystone_h3_h5_lift_block_shift.py)
(self-checking; `ALL CHECKS PASS`). **No tuning to 210 ppb, m_μ/m_e, h⁴, or any
target — every number is computed first, compared second.**

---

## VERDICT (one line)

The canonical **H₃↪H₅ lift exists, is computable, and is fit-free** (it is the
standard Hecke inclusion induced by the Bring **S₃↪S₅** spacetime/color
embedding), and the block-projector trace **sidesteps the 2026-06-02
nonexistence theorem** — but the muon-(3,2) vs electron-(3,1,1) operator-valued
branching shift it produces is **O(1) (ratio ≈ 3.067), seven orders of magnitude
above the 210 ppb target**. The branching is a **leading-order generation
selector, not an O(10⁻⁷) residual knob**; this is positive evidence that 210 ppb
is an **anchor-shift artifact** (no natural O(10⁻⁷) structural quantity lives at
the keystone blocks).

---

## 1. The objection that is now removed

The functor-resolution doc
([`2026-06-13-s5-so3-fiber-action-functor-resolution.md`](2026-06-13-s5-so3-fiber-action-functor-resolution.md))
§4 step 2 asks for the H₃(q) Markov-trace shift between the muon `E_{(3,2)}`
(ℓ=2) and electron `E_{(3,1,1)}` (ℓ=1) projectors. PR #2511 flagged a blocker:
*"which H₅ braid is the muon?"* — evaluating a 3-strand knot through an H₅
projector seemed to need a 5-strand lift, and choosing one to hit 210 ppb would
be a fit.

**The lift is not free to choose — it is already supplied by the geometry.** The
Bring quintic carries the S₅ action; the three Borromean **color** strands sit
inside the five Bring coordinates as the standard **S₃↪S₅** subgroup (fixing 2
points). That embedding induces the **standard Hecke inclusion**

$$ H_3 = \langle \sigma_1, \sigma_2\rangle \;\hookrightarrow\; H_5 = \langle \sigma_1, \sigma_2, \sigma_3, \sigma_4\rangle, $$

so the Borromean braid $\beta = (\sigma_1^{-1}\sigma_2)^3$ lifts **canonically**
to $B_5$ with strands 4, 5 idle. No fit: the lifted braid is forced by the
inclusion. (Owner observation, 2026-06-20.)

## 2. Why this sidesteps the 2026-06-02 nonexistence theorem

[`2026-06-02-h5-h3-functor-keystone.md`](2026-06-02-h5-h3-functor-keystone.md)
proved there is **no canonical map sending the ℓ=2 fiber amplitude to the h⁴
coefficient**, because `(2,1)` occurs with **multiplicity 2** in the relevant
restrictions — so `Hom(fiber, (2,1))` has no distinguished **basis vector**, and
choosing one is a fit.

The lift here never chooses a basis vector. It evaluates the **whole block
projector** trace

$$ \mathrm{tr}\big(E_\lambda \cdot \rho_5(\beta)\big) \;=\; y_\lambda^{(5)} \,\chi^\lambda(\beta), $$

which is **basis-independent** — it sums over both `(2,1)` copies automatically.
The multiplicity-2 obstruction is real for "read off a scalar from a line" but
**irrelevant** for "trace the block." So the operator-valued branching is a
well-defined number per block. This is the precise sense in which the keystone
functor is usable even though the nonexistence theorem holds.

## 3. The RAW numbers (at q₀ ≈ 1.10997859556)

**Self-check (the lift is honest).** The normalized Markov trace is compatible
with the inclusion H₃⊂H₅ (`tr₅(x) = tr₃(x)` for x with no σ₃,σ₄):

$$ \sum_{\lambda \vdash 5} y_\lambda^{(5)}\,\chi^\lambda(\beta) \;=\; \mathrm{tr}_M^{(3)}(\beta) \;=\; 0.998366621838\ldots $$

holds to f64 floor (residual 2.3×10⁻¹⁶; the `y_λ` weights are f64-internal). The
lift re-derives the Borromean invariant, not a re-normalization.

**H₅ block-resolved contributions of the lifted Borromean:**

| λ ⊢ 5 | dim S^λ | y_λ⁽⁵⁾ | χ^λ(β) | y·χ |
|---|---|---|---|---|
| (5) | 1 | 0.118148 | 1.00000 | 0.118148 |
| (4,1) | 4 | 0.109379 | 3.99419 | 0.436878 |
| **(3,2) muon ℓ=2** | 5 | **0.061724** | **4.98837** | **0.307901** |
| **(3,1,1) elec ℓ=1** | 6 | **0.016767** | **5.98837** | **0.100405** |
| (2,2,1) | 5 | 0.007750 | 4.98837 | 0.038658 |
| (2,1,1,1) | 4 | −0.000929 | 3.99419 | −0.003710 |
| (1⁵) | 1 | 0.0000862 | 1.00000 | 0.0000862 |

**Operator-valued branching shift, muon vs electron:**

$$ \frac{y_{(3,2)}\,\chi^{(3,2)}(\beta)}{y_{(3,1,1)}\,\chi^{(3,1,1)}(\beta)} = \frac{0.307901}{0.100405} = \mathbf{3.0666} $$

So `|ratio − 1| = 2.067`, which is **6.99 orders of magnitude larger** than the
210 ppb (2.1×10⁻⁷) reference.

## 4. Reading — what it gives, and what it does not

- **Gives:** a fit-free, canonical, computable operator-valued branching object.
  The two generation blocks differ at **O(1)**. (Note `χ^{(3,2)} ≈ 4.988 ≈ 5 −
  O(h²)` and `χ^{(3,1,1)} ≈ 5.988 ≈ 6 − O(h²)` — the q-deformation of the bare
  dimensions; the distinction is dominated by the **Markov weights** `y_λ`, which
  differ by ~3.7×.)
- **Does NOT give:** a 210 ppb knob. The shift is O(1), seven orders too coarse
  to *be* the muon residual as a small correction. The 210 ppb residual cannot
  be produced by perturbing this branching without fitting.
- **Consistent with** the 2026-06-13 framing and the owner's standing position
  (CLAUDE.md precision-goals): **210 ppb is an anchor-shift artifact** of the
  2026-05-28 proton re-pin (m_μ/m_e became a 9.5σ *prediction*), not a structural
  q-deformation that lives at the keystone. This compute supplies positive
  evidence: there is **no natural O(10⁻⁷) quantity** at the (3,2)/(3,1,1) blocks
  — everything there is O(1).

**Discipline note (per the formalize-first / no-fit rules).** The productive next
step is **not** a `1.000000210` hunt at this level. If the operator-valued
branching has any role, it is in the **leading** generation structure (the
O(100) ratio m_μ/m_e ≈ 206.8 itself), where an O(1) block distinction is the
right order of magnitude to *seed* — not in the residual tail. The block ratio
3.067 is reported RAW; it is **not** claimed to derive m_μ/m_e, and no further
combination is fished for.

---

## What this audit does and does not claim

- **Does** establish the canonical, fit-free H₃↪H₅ lift (Bring S₃↪S₅ → standard
  Hecke inclusion) and compute the block-resolved Borromean trace at q₀.
- **Does** prove (self-check, 15-digit) that the lift preserves the Markov trace.
- **Does** explain why the block-projector trace sidesteps the 2026-06-02
  multiplicity-2 nonexistence theorem (no basis vector is chosen).
- **Does** report the RAW muon/electron branching ratio (≈ 3.067, O(1)).
- **Does NOT** fit, tune, or propose any normalization to reach 210 ppb,
  m_μ/m_e, or h⁴; these are falsification references only.
- **Does NOT** wire to production, advance L2 numerically, or discharge any Lean
  `sorry`. No LP/SDP solve (no dual emission required).

## Cross-references

- Functor resolution (§4 the open obligation):
  [`2026-06-13-s5-so3-fiber-action-functor-resolution.md`](2026-06-13-s5-so3-fiber-action-functor-resolution.md).
- The nonexistence theorem this lift sidesteps:
  [`2026-06-02-h5-h3-functor-keystone.md`](2026-06-02-h5-h3-functor-keystone.md).
- Tool unblock (the wheel this compute depends on):
  [`2026-06-20-pyhecke-native-build-unblocked.md`](2026-06-20-pyhecke-native-build-unblocked.md) (PR #2511).
- Per-block h⁴ localization (h⁴ exclusively in the (2,1) block):
  [`scripts/borromean_per_block_h4_localization.py`](scripts/borromean_per_block_h4_localization.py) (PR #2504).
- Conjecture / Lean class:
  [`S5SO3FiberAction.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean)
  (`conj:s5-so3-fiber-action`).
- Bean: `s5bb` (q-closure was OPEN; this is the first RAW crack).
