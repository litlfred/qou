# Q_β Φ probes — the corpus "Φ_q" is the compact q-dilog, not Faddeev Φ_b (modular double missing)

**Date:** 2026-07-06
**Status:** ACCURACY FINDING (corpus-grep + literature). Explains why prior
Φ probes on the Q_β decay face were unreliable, and fixes the object the
f-map must use. Feeds
[`docs/scope/2026-07-06-qbeta-fmap-torus-knot-cs-phase-geometry.md`](../scope/2026-07-06-qbeta-fmap-torus-knot-cs-phase-geometry.md).

---

## 1. The finding

The corpus utility [`computations/_phi_q_util.py`](../../computations/_phi_q_util.py)
defines, under the name "Faddeev quantum dilogarithm Φ_q",

```
Φ_q(z) = ∏_{k≥1} (1 − q^{−k}·z)^{−1}
```

— a **single compact product** (the q-Pochhammer / compact quantum
dilogarithm, `1/(z; q^{−1})_∞`). This is **not** the Faddeev *non-compact*
quantum dilogarithm `Φ_b` that appears in the Andersen–Kashaev complex
volume / the root-of-unity saddle of the colored Jones. The true `Φ_b`
(literature, §3) is a **ratio of two products** — a **modular double**
`b ↔ b^{−1}`:

```
Φ_b(x) = ∏_{k≥0}  (1 + e^{2πi b²(k+½)}   e^{ 2π b x})
                  ─────────────────────────────────────
                  (1 + e^{−2πi b^{−2}(k+½)} e^{2π b^{−1} x})
       = exp ∫_{ℝ+iε}  e^{−2ixz} / (4 sinh(zb) sinh(zb^{−1}))  dz/z.
```

**The corpus form carries only the numerator-type product; the entire
`b^{−1}` (modular-dual) factor is absent.** For generic `b` that dual
factor does not vanish, so the corpus "Φ_q" ≠ `Φ_b`.

## 2. Why this is the Q_β decay-face inaccuracy

Per the two-saddle scope, Q_β = Im 𝔙 (bar-odd, sinh, decay) lives on the
**root-of-unity / Faddeev** saddle.

> **Correction (2026-07-07, self-review).** An earlier draft of this section
> claimed "the modular double `b ↔ b^{−1}` **is** the bar involution
> `q ↔ q^{−1}`," and that the compact single product "has no genuine bar-odd
> content." **Both are wrong** and are retracted. With `q = e^{2πi b²}`:
> `b ↔ b^{−1}` (modular / S-duality) maps `q → q̃` (the modular *dual*), **not**
> `q → q^{−1}`; the bar `q → q^{−1}` corresponds to `b → i b`. They are
> **distinct** involutions. And the compact form **is** bar-asymmetric under
> `q ↔ q^{−1}` (`∏(1−q^{−k}z)^{−1}` at `q` ≠ at `q^{−1}`), so it does carry
> bar-odd content. The claims below are the corrected, conservative ones.

Two facts that **do** hold:

- **The compact form lacks the modular double.** `Φ_b` is a *ratio* over
  both `b` and `b^{−1}` (`Φ_b = Φ_{b^{−1}}`, the S-duality that pairs `q`
  with `q̃`); the compact `∏(1−q^{−k}z)^{−1}` has the `b`-product only. The
  missing `b^{−1}` factor is the **modular / quantum-Teichmüller (root-of-
  unity) structure** — the analytic content of the Faddeev saddle that the
  compact form cannot reproduce, regardless of its (nonzero) bar-odd part.
- **The kernel is literally `sinh(zb)·sinh(zb^{−1})`** — the q-hyperbolic
  sinh structure, symmetric under the *modular* `b ↔ b^{−1}`. The compact
  product throws away the `b^{−1}` factor and so the modular structure.

The **bar-even/bar-odd (cosh/sinh) split** — the object the Lean
`bar_parity_decomposition` proves and `prop:phi-b-bar-parity-decomposition`
records — is the **bar `q ↔ q^{−1}`** parity, a *separate* structure from the
modular double. Both are features of `Φ_b`; the compact form shares the bar
parity but not the modular double.

Corroborating corpus evidence that the Φ layer was already known-shaky:

- [`li2q_phiq_bar_symmetry_witness.py`](../../computations/li2q_phiq_bar_symmetry_witness.py)
  records that **`prop:li2q-phiq-bar-symmetrization` is FALSIFIED** — the
  claimed `Li₂^q ↔ Φ_q` bar-symmetrization identity does not hold
  numerically. It *also* uses yet another convention
  (`∏_{k≥0}(1−q^{2k+1}z)^{−1}`, odd powers), so the corpus carried **three
  inconsistent "Φ" conventions** (compact `q^{−k}`; odd-power `q^{2k+1}`;
  true `Φ_b` modular double) — a classic source of the "compute may have
  been inaccurate" symptom.
- A cluster of Φ_q probes sits in `computations/_deprecated/`
  (`_phi_q_util.py`, `d_phi_q_series.py`, `per_block_phi_q.py`,
  `brane_tower_per_channel_phi_q.py`, …); the deprecated `d_phi_q_series.py`
  self-notes it returns "the wrong value" pending "a principled fix."

## 3. Literature (the correct object)

- Faddeev–Kashaev, *Quantum dilogarithm as a 6j-symbol* and Faddeev's
  modular double: `Φ_b` integral + product, modular invariance
  `Φ_b = Φ_{b^{−1}}`, inversion `Φ_b(x)Φ_b(−x) = Φ_b(0)² e^{πix²}`, poles at
  `c_b + ibℕ + ib^{−1}ℕ` (simple, on the modular lattice).
- Andersen–Kashaev, *A TQFT from quantum Teichmüller theory* — `Φ_b` as the
  state-integral building block of the complex-volume (Vol + i·CS) invariant.
- Dimofte–Gukov, *Quantum Field Theory and the Volume Conjecture*
  (arXiv:1003.4808) — `Φ_b` and the root-of-unity saddle of the colored
  Jones.

Sources:
[math/0604094](https://arxiv.org/pdf/math/0604094),
[arXiv:1003.4808](https://arxiv.org/pdf/1003.4808),
[arXiv:1910.11747 (general modular quantum dilogarithm)](https://ar5iv.labs.arxiv.org/html/1910.11747).

## 4. Consequence for the f-map (and the fix)

- **`F_odd(q)` — the bar-odd / root-of-unity factor of `F(q)` (parity split,
  [`qbeta_fmap_parity_stability_probe.py`](../../computations/qbeta/qbeta_fmap_parity_stability_probe.py))
  — must be built from the modular-double `Φ_b`, i.e. its
  `b↔b^{−1}`-antisymmetric part.** The compact q-Pochhammer cannot carry it.
- **`F_even(q)` (mass/bar-even) may keep the compact form** — that is the
  real-q/Rogers-adjacent object, and the corpus's use of `phi_q` in the
  *mass* tower (`m_p/m_e`) is on the correct face.
- **Reeb link:** the Reeb tangent `tan θ = z` (`z = δ^{−1}`, the Markov
  exchange amplitude; g_reeb tranche, #3448) is the contact-form holonomy
  whose quantum wavefunction is `Φ_b`; the phase reframe
  `Q_β/Q_A = cos Φ(u)` with `Φ₁ = √2` is that Reeb/CS holonomy, and `Φ`
  should be read off the modular-double `Φ_b`, not the compact product.

**Pre-registered next probe (non-fishing):** compute the compact
`∏(1−q^{−k}z)^{−1}` vs the true modular-double `Φ_b` at the substrate `b`
(with `q = e^{2πi b²}` the fibre/root-of-unity assignment) and quantify the
discrepancy on the bar-odd part; verify the `Φ_b` pole lattice gives the
observed simple dominant pole at `u_substrate` (PR #1727). This replaces the
compact-`Φ_q` inputs of the deprecated probes. **No c_k value / no picked
root-of-unity — flip-flop guard respected.**

## 4a. Terminology ruling + corpus sweep (2026-07-06)

**Ruling.** Two distinct objects, name each correctly:

| object | correct name | wrong name (do not use) |
|---|---|---|
| `∏_{k≥1}(1−q^{-k}z)^{-1}` (single q-Pochhammer, `phi_q`) | **compact quantum dilogarithm** / q-exponential | ~~Faddeev Φ_q~~ |
| modular-double ratio, `sinh(zb)sinh(zb^{-1})` kernel | **Faddeev (non-compact) quantum dilogarithm `Φ_b`** | — |

"Faddeev" belongs to the modular-double `Φ_b` only. The Lean lemma file
[`QOU/QBeta/FaddeevModularDouble.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/FaddeevModularDouble.lean)
(sorry-free, `lean`-direct exit 0) axiomatises `Φ_b` and proves the
bar-parity (sinh/cosh) decomposition.

**Sweep.** A conservative codemod corrected **238 mislabel lines across 92
source files** (`.py`/`.md`/`.lean`/`.ts`), rewriting "Faddeev Φ_q",
"Faddeev recursion/iterated/functional equation/resummation", "Bring +
Faddeev h⁴", etc. → "compact q-dilog / compact-q-dilog …". Protected
(unchanged): bibliographic keys (`faddeev-kashaev`, `andersen-kashaev`),
`Kashaev` volume, genuine `Φ_b` references, and the two hand-corrected
utilities. **File renames** (`git mv`, references updated): the three
`*faddeev*` scripts → `xi_ell_phi_q_probe.py`,
`m_p_bring_plus_phi_q_h4_probe.py`, `mass_table_bring_phi_q_h4_sweep.py`
(+ their `.script-qa.json` sidecars and `.witness.json` outputs + the
in-script `WitnessBuilder` names + `faddeev_h4` identifiers). No module
imports referenced them, so no import breakage. Pre-existing stray
`git_files.txt` (a filename dump) left untouched.

## 4b. Resolution (2026-07-07) — validated evaluator + the historical inaccuracy pinned

- **`Φ_b` now exists in the compute, literature-verified**:
  [`computations/qbeta/phi_b_evaluator.py`](../../computations/qbeta/phi_b_evaluator.py)
  implements the Faddeev integral and passes a gating battery (shift equations
  in `b` and `1/b` at real *and* complex `b`; modular duality; inversion with
  the constant `e^{iπ(b²+b⁻²)/12}`; the FK modular-double product identity to
  **1.8e-37**). Conventions verified line-by-line against the owner-uploaded
  source [`library/arxiv-math-0604094v1/0604094v1.pdf`](../../library/arxiv-math-0604094v1/0604094v1.pdf) (Hikami,
  arXiv:math/0604094, eqs (2.1)–(2.5)) via the map `γ = πb²`, `φ = 2πbz`.
- **The suspected "Φ compute inaccuracy" has a pinned mechanism**: the
  battery's first run caught a **complex-power principal-branch bug**
  (`qq**(k+½)` sign-flips when `arg(qq) ≈ ±π`), which had produced a 2.2e-2
  error masquerading as a formula/convention discrepancy. Any historical Φ
  probe raising complex bases to half-integer powers is suspect for the same
  bug class; the fix is explicit exponentials (no branch ambiguity).
- The evaluator's **native regime is real `b` ⇔ |q| = 1** — the fibre/decay
  face where `F_odd` lives. The real-substrate continuation
  (`arg b = −π/4`) remains open.

## 5. Coordination

- Complements the [two-saddle scope](../scope/2026-07-06-qbeta-fmap-torus-knot-cs-phase-geometry.md)
  (why F(q) is root-of-unity) and the
  [parity-stability probe](../../computations/qbeta/qbeta_fmap_parity_stability_probe.py)
  (F = F_even × F_odd). This doc supplies the *correct analytic object* for
  `F_odd`.
- #3429 (power-class pincer, ζ₄ parity) and #3437 (`conj:binding-qbeta-complex-volume`)
  should use `Φ_b` (modular double), not the compact `phi_q`, for any
  decay-face evaluation.
