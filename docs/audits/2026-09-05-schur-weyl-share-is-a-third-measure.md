# Route 1 of the Φ_k weight question, measured: the `V^{⊗n}` share is a third measure — and at `dim V = 2` it is null from depth 2 up

> **This note carries a correction — read §🛑 below before quoting anything from §0 or §3.**

**Date:** 2026-09-05
**Bean:** `qou-oots`
**Probe:** [`computations/probes/schur_weyl_share_is_a_third_measure_probe.py`](../../computations/probes/schur_weyl_share_is_a_third_measure_probe.py) — 6/6, exit 0, mpmath 50 dps, exact integer combinatorics, zero builtin-float coercions, no witness
**Answers:** [`2026-09-05-phi-k-weight-family.md`](2026-09-05-phi-k-weight-family.md) §7 route 1
**Adjudicates:** a three-way conflict over what `d_q²` is the share *of*

---

## 🛑 CORRECTION 2026-09-05 — the stratum was misnamed and the verdict overturned

**Two errors below, both mine.** Probe:
[`which_n_the_nucleus_is_a_state_at_probe.py`](../../computations/probes/which_n_the_nucleus_is_a_state_at_probe.py) — 9/9, exit 0.

1. **Depth is off by one throughout §0 and §3.** The Φ_k audit defines *"Depth `k`
   means `k+1` rows"* ([line 104](2026-09-05-phi-k-weight-family.md)), so **the
   depth-3 stratum is EXACTLY 4 rows**, and "≥ 3 rows" — what §3 measures — is
   **depth ≥ 2**. Every number in §3 is correct for what it measures; only the
   name is wrong.

2. **§8's open item does not exist.** This note ends *"route 1 now turns on
   exactly one thing: which `N` the nucleus is a state at."* **It turns on
   nothing.** On the real depth-3 stratum the share is **`0.0` at `N = 3` as
   well as at `N = 2`** — both caps sit below 4 rows. And the Φ_k audit had
   already said so at its lines 107-108: *"at `N = 3` the cap still lands on
   depth ≥ 3, so **`k = 3` is vacuous under `y_λ` at both the mass (`N = 2`)
   and colour (`N = 3`) readings**."* I quoted the paragraph above that
   sentence and did not carry the sentence itself.

**`N` is nonetheless settled, independently: `N = 2`**, by the convention-D
owner ruling of 2026-08-15. The ≥ 3-row blocks are `ker(H_n ↠ TL_n)` and
`TL_n(q) ≅ End_{U_q\mathfrak{sl}_2}(V^{⊗n})`, so the corpus's canonical trace
already factors through the N=2 module's endomorphism algebra — horn 1 of §7 is
the corpus's actual position. Four corpus witnesses and the verifying arithmetic
are in
[`2026-09-05-which-n-the-nucleus-is-a-state-at.md`](2026-09-05-which-n-the-nucleus-is-a-state-at.md).

**F1 and F2 below are unaffected** — neither depends on the depth labelling.

3. **F4 computes the share of the wrong algebra.** It says horn 2's
   `End(V^{⊗n})` has block share `(f^λ)²/n!`. At `N = 2` the operator algebra of
   the pair is **`TL_n`, of dimension `Catalan(n)`** — not `H_n`, of dimension
   `n!`. The correct share is `(f^λ)²/C_n` over `ℓ(λ) ≤ 2`. The root cause is
   §4's bare `≅`: `q`-Schur–Weyl is an isomorphism only for `N ≥ n`, and at
   `N = 2`, `n = 3A` the map is surjective with a kernel of dimension
   `n! − C_n`. Corrected in the note above; three further corpus sites carry the
   same over-claim and are listed there.

4. **Two sourcing errors.** §3 attributes `dim V = 2` to *"the Descartes
   condition"*; the corpus explicitly forbids that attribution
   (`schur-weyl-eightfold.md:53`, `2026-08-04-ocneanu-trace-parameter-audit.md:114`)
   and the live sourcing is the volume axiom. And §3's scope note claims
   `schur-weyl-mass-decomposition.md` keeps λ with rows beyond 3 — read at the
   source it is **line 18**, about `λ₁ > 3` (part *size*, in an approximation no
   live producer runs), not row count.

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
| **F3** | At `N = 2` the `V^{⊗n}` share is **exactly zero** on every partition with ≥ 3 rows (= depth ≥ 2, **not** depth 3 — see the correction above) | constrains the family; does **not** decide Φ₃, which is vacuous at `N = 3` too |
| **F4** | `End(V^{⊗n})` is not a rival state space but the **operator algebra of the same pair**; its share is `(f^λ)²/n!`, a candidate §7 omits | horn 2 is mis-specified |

~~**Route 1 now turns on exactly one thing … which `N` the nucleus is a state
at.**~~ **RETRACTED — see the correction above.** `N = 2` is settled, and it
decides nothing about Φ₃: the depth-3 stratum is vacuous at `N = 3` as well.

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

Mass carried on partitions with ≥ 3 rows — i.e. **depth ≥ 2**, *not* the depth-3
stratum (which is exactly 4 rows; see the correction above) — from check C:

| measure | n = 3 | n = 6 | n = 9 |
|---|---|---|---|
| `V^{⊗n}` share, **N = 2** | **0.0** | **0.0** | **0.0** |
| `V^{⊗n}` share, N = 3 | 0.035464334084 | 0.306778844906 | 0.602339318062 |
| Molien (all λ) | 0.223435033655 | 0.902265160825 | 0.997608919308 |

The zeros are exact, not small: `d_q^{SU(N)}` carries the factor `[N + c]_q` and
the cell of content `c = −N` contributes `[0]_q = 0`.

The corpus asserts the state space is `V^{⊗3A}` with **`dim V = 2`**:

- [`per-nucleon-channel-decomposition.md`](../../content/quantum-observable-universe/nuclear-interactions/per-nucleon-channel-decomposition.md) line 13 — *"The typed Garside element acts on `V^{⊗3A}`"*, a live `definition` block, at the nuclear `3A` level.
- [`state_space_natural_three_sym2_gate.py`](../../computations/state_space_natural_three_sym2_gate.py) lines 8–17 — *"every object in the framework's state space … is built from tensor powers of the ONE fibre `V`, with `dim V = 2` by the Descartes condition."* **The value is right; that sourcing is not** — `schur-weyl-eightfold.md:53` says Descartes *"is compatible with but does not uniquely force `N = 2`"*, and `2026-08-04-ocneanu-trace-parameter-audit.md:114` says ***"Do not claim `N = 2` is forced by the Descartes condition"***. The live derivation is `VolumeConstraintForcesFibreTwo.lean` (sorry-free).

**So under the corpus's own reading, the module-share measure vanishes
identically from depth 2 up** — which *includes* the depth-3 stratum, so Φ₃ ≡ 0
by the Φ_k audit's own R1 (`phi_eq_zero_of_weights_vanish`). That is the *same*
row-cap invariant R1 uses to retire `y_λ`, applied to the object route 1
proposes to derive the measure *from*. The conclusion Φ₃ ≡ 0 is correct; what
was wrong was inferring from it that `N` decides the matter.

~~Route 1 at `N = 2` therefore does not select between the survivors — it excludes
the module-share reading for Φ₃. It survives only at `N ≥ 3`.~~ **RETRACTED.**
The real depth-3 stratum is null at `N = 3` too. What route 1 *does* establish
is a **constraint**: any measure consistent with the corpus's canonical trace
must vanish on `ker(H_n ↠ TL_n)`, i.e. on every λ with ≥ 3 rows. Molien and
unrestricted classical Plancherel both put mass there, so route 1 constrains
the family without selecting one.

**Scope.** This is a scope-(b) structural exclusion *of the `N=2` module-share
reading*, resting on a proved vanishing (`[0]_q = 0`) — not a claim that the
corpus's `N` is 2 for the colour channel.
~~`schur-weyl-mass-decomposition.md` line 19 records the corpus keeping λ with
rows beyond 3.~~ **RETRACTED — that was second-hand and wrong.** It is line 18,
and it says an *approximation* discards partitions with *"rows longer than 3"* —
`λ₁ > 3`, part **size** (its own examples `(3A−1,1)` and `(3A−2,2)` are two-row
partitions), not row count. And `N = 3` is not what production runs: the
canonical colour path `bring_color_weighted` uses `z_D`, the SU(2)/TL parameter.

---

## 4. F4 — horn 2 names the operator algebra, and its share is the omitted candidate

`End(V^{⊗n})` is not an alternative state space. Under q-Schur–Weyl it is the
**operator algebra of the same dual pair**, and the corpus says so in Lean —
[`MassLeftMulEndomorphism.lean`](../../content/quantum-observable-universe/lean/QOU/MassEndomorphism/MassLeftMulEndomorphism.lean)
lines 7–21, and [`QSchurWeyl.lean`](../../content/quantum-observable-universe/lean/QOU/QuantumObservableUniverses/QSchurWeyl.lean)
line 11.

> **🛑 CORRECTED — the algebra below is wrong at `N = 2`.** `q`-Schur–Weyl is an
> isomorphism only for `N ≥ n`; at `N = 2`, `n = 3A` the map `H_n(q) ↠
> End_{U_q\mathfrak{sl}_2}(V^{⊗n}) = TL_n(q)` has kernel of dimension
> `n! − Catalan(n)`. So the operator algebra of the pair is `TL_n`, and its
> block share is `(f^λ)²/C_n` over `ℓ(λ) ≤ 2`, **not** the `(f^λ)²/n!` below.
> See [`2026-09-05-which-n-the-nucleus-is-a-state-at.md`](2026-09-05-which-n-the-nucleus-is-a-state-at.md) §4c.

Its block share *as written here* is the dimension share in `H_n(q) ≅ ⊕_λ M_{f^λ}`
— correct for `H_n`, and `H_n` is the wrong algebra:

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

[`library/arxiv-1001.2180v2/sections/sec-026-61-decomposition-of-tensor-representations.md`](../../library/arxiv-1001.2180v2/sections/sec-026-61-decomposition-of-tensor-representations.md)
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
- ~~**That the corpus's `N` is 2 for the colour channel.**~~ **Settled: `N = 2`** —
  see the correction above. It does not decide Φ₃ either way.
- **The atom's strand count.** [`atomic-braid.md`](../../content/quantum-observable-universe/knots-particles-confinement/atomic-braid.md)
  line 2 says `H_{A+Z}(q)` (nucleons + electrons);
  [`schur-weyl-mass-decomposition.md`](../../content/quantum-observable-universe/mass-theory/schur-weyl-mass-decomposition.md)
  line 1 and [`hecke_3a_weights.py`](../../computations/hecke/hecke_3a_weights.py)
  lines 5–6 say `H_{3A}(q)`. No block reconciles them; Φ_k is on the `3A`
  reading.
- **Nothing here asks for the `qou-uk8o` sweep to be reverted**, and nothing here
  depends on it.
