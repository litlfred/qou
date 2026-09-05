# Route 1 of the Φ_k weight question, measured: the `V^{⊗n}` share is a third measure — and at `dim V = 2` it is null on depth 3

**Date:** 2026-09-05
**Bean:** `qou-oots`
**Probe:** [`computations/probes/schur_weyl_share_is_a_third_measure_probe.py`](../../computations/probes/schur_weyl_share_is_a_third_measure_probe.py) — 6/6, exit 0, mpmath 50 dps, exact integer combinatorics, zero builtin-float coercions, no witness
**Answers:** [`2026-09-05-phi-k-weight-family.md`](2026-09-05-phi-k-weight-family.md) §7 route 1
**Adjudicates:** a three-way conflict over what `d_q²` is the share *of*

---

## 0. Verdict up front

The Φ_k weight audit closes with three routes and calls the first decisive and
**structural rather than numerical**:

> A derivation of the block measure from the Schur–Weyl decomposition of the
> nuclear braid representation. […] If that object is `V^{⊗n}` with `V` the
> `U_q(sl_N)` fundamental, the share is `f^λ d_q(λ)/[n]_q!`-shaped (Molien) and
> the question is closed. If it is the endomorphism algebra `End(V^{⊗n})`, the
> share is `d_q²/D²`-shaped and the question is closed the other way.
> **Naming which object the nucleus is a state in is the whole content.**

Measured rather than described, the route does not close the question either
way. Four findings:

| # | finding | consequence for route 1 |
|---|---|---|
| **F1** | Molien **is** Féray–Méliot's q-Plancherel — confirmed independently, numerically and by change of variables | §2 of that audit is strengthened |
| **F2** | Molien is **not** the `V^{⊗n}` share. Both are "Molien-shaped"; they are different measures, each normalised on its own index set | horn 1's parenthetical is wrong |
| **F3** | At `N = 2` the `V^{⊗n}` share is **exactly zero** on every partition with ≥ 3 rows | route 1 at `N=2` **excludes** the module reading for Φ₃, by that audit's own R1 |
| **F4** | `End(V^{⊗n})` is not a rival state space but the **operator algebra of the same pair**; its share is `(f^λ)²/n!`, a candidate §7 omits | horn 2 is mis-specified |

**Route 1 now turns on exactly one thing, and it is not which of two families:
it is which `N` the nucleus is a state at.**

---

## 1. F1 — the Molien ↔ q-Plancherel identification, confirmed independently

Numerically (check A): `Σ_λ f^λ q^{−κ_λ} d_q^{hook}(λ) / [n]_q! = 1` exactly at
`n = 2 … 7`, over **all** partitions, with
`d_q^{hook}(λ) = [n]_q! / Π_{cells}[h]_q`.

Analytically, the corpus's own `Q = q²` bridge closes it in one line. Féray–Méliot
use the non-symmetric `[k]_Q = (Q^k − 1)/(Q − 1)`, and at `Q = q²`

$$
[k]_Q \;=\; \frac{q^{2k}-1}{q^2-1} \;=\; q^{\,k-1}\,[k]_q .
$$

With `Σ_{cells} h = n(λ) + n(λ′) + n`, `b(λ) = n(λ)` and `κ_λ = n(λ′) − n(λ)`:

$$
M_{n,Q}(\lambda) \;=\; \frac{Q^{b(\lambda)} f^\lambda}{\prod_{\square}[h]_Q}
\;=\; \frac{q^{2n(\lambda)} f^\lambda}{q^{\,n(\lambda)+n(\lambda')}\prod_{\square}[h]_q}
\;=\; \frac{f^\lambda\, q^{-\kappa_\lambda}}{\prod_{\square}[h]_q},
$$

which is the Molien family. So the identification now rests on two independent
legs rather than one.

---

## 2. F2 — "Molien-shaped" is not "is Molien"

Both candidates are `f^λ` times one dimension over one normaliser. They are
different measures:

| | weight | index set | normaliser |
|---|---|---|---|
| **`V^{⊗n}` share** | `f^λ · d_q^{SU(N)}(λ)`, with `d_q^{SU(N)}(λ) = Π_{cells}[N+c]_q/[h]_q` | λ with **≤ N rows** | `[N]_q^n` |
| **Molien** | `f^λ · q^{−κ_λ} · d_q^{hook}(λ)` | **all** λ | `[n]_q!` |

Each sums to **exactly 1** on its own index set (checks A and B), so neither is
a mis-normalisation of the other — the usual way two candidate measures turn out
to be one. Maximum per-λ deviation at `N = 3`, `n = 6`:

| pair | max deviation |
|---|---|
| share ↔ Molien | 0.2715583611 |
| share ↔ classical Plancherel | 0.2206291110 |
| Molien ↔ classical Plancherel | 0.0622915500 |

Three distinct measures.

---

## 3. F3 — the row cap, turned on the object route 1 derives from

Mass carried on partitions with ≥ 3 rows — the depth-3 stratum Φ₃ acts on
(check C):

| measure | n = 3 | n = 6 | n = 9 |
|---|---|---|---|
| `V^{⊗n}` share, **N = 2** | **0.0** | **0.0** | **0.0** |
| `V^{⊗n}` share, N = 3 | 0.035464334084 | 0.306778844906 | 0.602339318062 |
| Molien (all λ) | 0.223435033655 | 0.902265160825 | 0.997608919308 |

The zeros are exact, not small: `d_q^{SU(N)}` carries the factor `[N + c]_q` and
the cell of content `c = −N` contributes `[0]_q = 0`.

The corpus asserts the state space is `V^{⊗3A}` with **`dim V = 2`**:

- [`per-nucleon-channel-decomposition.md`](../../content/quantum-observable-universe/nuclear-interactions/per-nucleon-channel-decomposition.md) line 13 — *"The typed Garside element acts on `V^{⊗3A}`"*, a live `definition` block, at the nuclear `3A` level.
- [`state_space_natural_three_sym2_gate.py`](../../computations/state_space_natural_three_sym2_gate.py) lines 8–17 — *"every object in the framework's state space … is built from tensor powers of the ONE fibre `V`, with `dim V = 2` by the Descartes condition."*

**So under the corpus's own reading, the module-share measure vanishes
identically on the depth-3 stratum, and Φ₃ ≡ 0 by the Φ_k audit's own R1**
(`phi_eq_zero_of_weights_vanish`). That is the *same* row-cap invariant R1 uses
to retire `y_λ`, applied to the object route 1 proposes to derive the measure
*from*.

Route 1 at `N = 2` therefore does not select between the survivors — it excludes
the module-share reading for Φ₃. It survives only at `N ≥ 3`, where the share is
nonzero and is a third measure that is neither survivor.

**Scope.** This is a scope-(b) structural exclusion *of the `N=2` module-share
reading*, resting on a proved vanishing (`[0]_q = 0`) — not a claim that the
corpus's `N` is 2 for the colour channel.
[`schur-weyl-mass-decomposition.md`](../../content/quantum-observable-universe/mass-theory/schur-weyl-mass-decomposition.md)
line 19 records the corpus keeping λ with rows beyond 3, and the depth-3 channel
is read elsewhere at `N = 3`.

---

## 4. F4 — horn 2 names the operator algebra, and its share is the omitted candidate

`End(V^{⊗n})` is not an alternative state space. Under q-Schur–Weyl
`H_n(q) ≅ End_{U_q\mathfrak{sl}_N}(V^{⊗n})` (Jimbo) it is the **operator algebra
of the same dual pair**, and the corpus says so in Lean —
[`MassLeftMulEndomorphism.lean`](../../content/quantum-observable-universe/lean/QOU/MassEndomorphism/MassLeftMulEndomorphism.lean)
lines 7–21, and [`QSchurWeyl.lean`](../../content/quantum-observable-universe/lean/QOU/QuantumObservableUniverses/QSchurWeyl.lean)
line 11.

Its block share is the dimension share in `H_n(q) ≅ ⊕_λ M_{f^λ}`:

$$
\frac{(f^\lambda)^2}{n!}, \qquad \sum_\lambda (f^\lambda)^2 = n! \ \text{(Burnside)},
$$

the **classical Plancherel measure** — normalised at every `n` (check D), and
**q-independent**, which is its own objection for a substrate observable but is
not the row-cap one. §7 does not list it.

`d_q²/D²` is the share of **neither** object: it is the Reshetikhin–Turaev /
Verlinde weight of the `S²×S¹` Hilbert space
([`2026-06-20-keystone-wlambda-beasley-witten-localization.md`](2026-06-20-keystone-wlambda-beasley-witten-localization.md) lines 22–24).

---

## 5. The literature already says all of this, in a paper §2 cites

[`library/arxiv-1001.2180v2/sections/sec-023-61-decomposition-of-tensor-representations.md`](../../library/arxiv-1001.2180v2/sections/sec-023-61-decomposition-of-tensor-representations.md)
— Féray–Méliot §6.1, the same paper the Φ_k audit uses for its §2
identification, in a section it did not open:

> We associate to this decomposition the following measure on partitions
> `Φ[λ] = m_λ · dim(S^λ)/N^n`. […] **the same construction with the regular
> representation gives rise to the Plancherel measure.** […] notice that the
> **Schur-Weyl measure charges only the Young diagrams whose lengths are smaller
> than `N`**.

That is F2, F3 and F4 in the literature's own vocabulary. **The term
"Schur-Weyl measure" appears nowhere outside `library/`** — 0 hits across
`content/`, `docs/`, `computations/` and `.beans/`. The corpus does not have a
name for the quantity route 1 asks for.

Also held, ingested and greppable but **registered in neither `references.ts`
nor any citation** (0 hits outside `library/`): `library/arxiv-1009.4034v1`,
Méliot, *Kerov's CLT for Schur-Weyl measures*. Its `sections/` begin at §2, so
the measure's definition is not in the extracted text — use `arxiv-1001.2180v2`
§6.1 for the formula.

---

## 6. Adjudication: `d_q²` is assigned three incompatible origins in the corpus

This is cheap to fix and is the highest-value prose defect found here.

| source | what it says `d_q²` is the share of |
|---|---|
| [`2026-06-16-keystone-plancherel-target-clarification.md`](2026-06-16-keystone-plancherel-target-clarification.md) line 47 | *"the measure produced by the Schur–Weyl `V^{⊗n}` decomposition under the symmetric (dimension-squared) pairing"* |
| [`2026-06-20-keystone-wlambda-beasley-witten-localization.md`](2026-06-20-keystone-wlambda-beasley-witten-localization.md) lines 22–24 | *"the colour-λ sector of the `S²×S¹` Hilbert space … This is `d_q² = q-dim End(V_λ)`"* — note `End(V_λ)`, the **simple object's** endomorphism algebra |
| [`2026-09-05-phi-k-weight-family.md`](2026-09-05-phi-k-weight-family.md) §7 | `End(V^{⊗n})`, the **tensor power's** endomorphism algebra |

At most one can be right, and this note establishes that **none of the three is
the `V^{⊗n}` share**, which is measured above and is a distinct measure. The two
dated audits are left as the records of their own analyses (the `qou-3nva`
precedent); this note is the live adjudication.

Note also that `2026-06-16` lines 41–44 explicitly forbids importing the
Beasley–Witten argument across sectors — *"different sectors … **Do not bridge
them.**"*

---

## 7. Route 1 has no Lean carrier today

[`QOU/SchurWeyl/HeckeWedderburnDataGeneral.lean`](../../content/quantum-observable-universe/lean/QOU/SchurWeyl/HeckeWedderburnDataGeneral.lean)
lines 17–27, in the corpus's own words:

> **The weights are a parameter of this construction, not a result of it.**
> Given *any* family `w : λ ↦ ℝ`, the functional `Σ_λ w_λ χ_λ` is well defined
> and `markov_eq` holds by `rfl` […] It does **not** deliver a Markov trace.

So the existing Wedderburn infrastructure cannot select a weight family — it
takes one as input. Route 1 must be argued from the module, not from that
infrastructure.

Related open: bean `qou-us0a` records that nothing in the tree touches
`U_q(gl_N)` or a double centraliser, and that Mathlib v4.24.0 carries no
Jacobson density / bicommutant.

---

## 8. What is NOT established

- **Which family Φ_k should use.** Route 1 is narrowed and partly excluded, not
  completed.
- **That the corpus's `N` is 2 for the colour channel.** §3's scope note.
- **The atom's strand count.** [`atomic-braid.md`](../../content/quantum-observable-universe/knots-particles-confinement/atomic-braid.md)
  line 2 says `H_{A+Z}(q)` (nucleons + electrons);
  [`schur-weyl-mass-decomposition.md`](../../content/quantum-observable-universe/mass-theory/schur-weyl-mass-decomposition.md)
  line 1 and [`hecke_3a_weights.py`](../../computations/hecke/hecke_3a_weights.py)
  lines 5–6 say `H_{3A}(q)`. No block reconciles them; Φ_k is on the `3A`
  reading.
- **Nothing here asks for the `qou-uk8o` sweep to be reverted**, and nothing here
  depends on it.
