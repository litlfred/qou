# Charm mass via the Frobenius/Wedderburn charm-block projection (negative)

**Date:** 2026-08-02
**Branch:** `claude/charm-mass-projection-2026-08-02` (PR #4594)
**Scope:** the charm-block reading of the complex-mass constituent functional.

> **Forward-reference note.** The block this audit is scoped against —
> `conj:complex-mass-constituent-functional`
> (`QOU.MassTheory.ComplexMassConstituent`) — is **not yet on `main`**: it lives
> on the **open draft** PR #4584. Nothing in this PR imports or depends on it;
> the probe's `consumes` field and this scope line are forward references, and
> the negative below stands on its own compute (the $H_3$ irreps and $y_\lambda$
> are built self-contained). If #4584 lands under a different label, update the
> two references rather than treating them as resolved.

**Trigger:** author request — attack `m_c` as the **Frobenius/Wedderburn
charm-BLOCK projection** of a composite braid's complex volume,
`tr_M = Σ_λ y_λ χ_λ`, **not** the raw volume.

## Prior state (read first)

Two facts frame the block reading. The first is a classical invariant, restated
here with its citation so this audit does not depend on an external document;
the second is recorded as an observation of this session's own sweep.

- **(b) The $T_{3,5}$ carrier supplies no hyperbolic volume — structural
  exclusion, invariant cited.** Torus knots are Seifert-fibred, hence not
  hyperbolic (Thurston's geometrisation of knot complements: a knot complement
  is hyperbolic iff the knot is neither a torus knot nor a satellite). So
  $\mathrm{Vol}(T_{3,5}) = 0$ and its Gromov norm vanishes. This is a genuine
  **scope-(b)** exclusion per AGENTS §"Before declaring refuted": a proved
  invariant forbids the ingredient, and the invariant is named. It excludes
  $T_{3,5}$ *as a volume carrier*; it says nothing about other carriers.
- **(a) Raw composite volume fails — scope-limited.** No parameter-free
  composite-baryon volume examined reproduced $m_c$; the one 4 % near-coincidence
  ($\mathrm{Vol}((\sigma_1\sigma_2^{-1})^5)/\mathrm{Vol}(\mathcal{B}_3)=2.33$ vs
  $\Lambda_c/p=2.44$) is topologically disqualified ($(\sigma_1\sigma_2^{-1})^5$
  is a **knot**, not a 3-quark baryon) and non-repeating (bottom misses 40 %).
  This is **scope-(a)**: it constrains magnitudes over the carriers tried, not
  the raw-volume reading as such.

The surviving OPEN handle: the mass is the **charm-block share** of the Markov
trace, $\mathrm{tr}_M = \sum_\lambda y_\lambda \chi_\lambda$ — the fraction of the
composite's (complex) volume that lands in the generation-2 Wedderburn block of
$H_3$.

## What was derived (no fit)

`computations/charm_frobenius_block_projection_probe.py`, witness
`charm-frobenius-block-projection.witness.json`.

### Infrastructure (self-contained, validated)

The corpus character kernel (`hecke_characters.chi_lambda_braid`) needs
numpy/scipy/`pyhecke_native`, all absent in this sandbox. For $H_3$ the irreps
are tiny (dims 1, 2, 1), so the probe builds them directly:

- **Hoefsmit seminormal irreps** of $H_3$, eigenvalues $q, -q^{-1}$ (AGENTS §7a):
  $[3]$ trivial $\sigma_i\!\mapsto\!q$; $[1^3]$ sign $\sigma_i\!\mapsto\!-q^{-1}$;
  $[2,1]$ standard $\sigma_1=\mathrm{diag}(q,-q^{-1})$,
  $\sigma_2=\begin{psmallmatrix}-1/(q^3+q) & r\\ r & q^3/(q^2+1)\end{psmallmatrix}$,
  $r=\sqrt{q^4+q^2+1}/(q^2+1)$ (solved symbolically from Hecke + braid).
- **Validation:** Hecke residual $=0$, braid residual $\sim10^{-51}$,
  $\mathrm{tr}_M(\mathbb{1})=\sum_\lambda y_\lambda\dim_\lambda = 1.0$.
- **`y_λ`** from the corpus Wenzl bridge (`y_lambda_wenzl_bridge_numeric`, pure
  mpmath), evaluated at the **experimental (proton) pin**
  $q_0 = $ `q_parameter.Q` $\approx 1.1099785827513808$ — the standing default
  for new compute (AGENTS §q₀ anchor convention, owner directive 2026-08-07):
  $y_{[3]}=0.41540$, $y_{[2,1]}=0.28093$, $y_{[1^3]}=0.02274$.
  The bridge is a **live closed form** keyed on the $q$ passed in, not a cached
  muon-built witness, so $y_\lambda$ and $\chi_\lambda$ are both evaluated at
  the same $q_0$ and the ideal/experimental layers are never straddled inside
  one computed quantity.

### Reading (A) — parameter-free, scale-free (primary)

Keep the **same** Borromean baryon geometry $\mathcal{B}_3=(\sigma_1\sigma_2^{-1})^3$
(the proton, 3 components). The three Wedderburn blocks $\lambda\in\{[3],[2,1],[1^3]\}$
are the three generations. Because the complex-volume prefactor and the
$\mathrm{tr}_M$ normalization **cancel in a block ratio**, the generation mass
ratio is a pure function of $q_0$:

$$\frac{m_\text{charm}}{m_\text{light}} \;=\; \frac{y_{[2,1]}\,\chi_{[2,1]}(\mathcal{B}_3)}{y_{[3]}\,\chi_{[3]}(\mathcal{B}_3)}.$$

Block projections on $\mathcal{B}_3$: $y_{[3]}\chi_{[3]}=0.4154$,
$y_{[2,1]}\chi_{[2,1]}=0.5602$, $y_{[1^3]}\chi_{[1^3]}=0.0227$.

| quantity | **predicted** | observed |
|---|---|---|
| $m_\text{charm}/m_\text{light}$ | **1.349** | $\sim372$ (current) → **276× undershoot** |
| $m_\text{top}/m_\text{light}$ | 0.055 | $\sim5\times10^4$ (wrong direction) |

No knob, no SnapPy, no scale. **A 276× undershoot.**

### Reading (B) — SnapPy complex volume + [2,1] projection (task's construction)

Charm braid = Borromean $+ \sigma_1^{2k}$ (even power keeps the permutation
trivial ⟹ **3 components** preserved), one strand carrying winding $3+2k$. SnapPy
computes $\mathrm{Vol}+i\,\mathrm{CS}$; the charm mass candidate is
$\mathrm{Re}\big(\mathrm{Vol}_{\mathbb C}\cdot y_{[2,1]}\chi_{[2,1]}/\mathrm{tr}_M\big)$.

| $k$ | winding | Vol | CS | comps | charm [2,1] proj. Re |
|---|---|---|---|---|---|
| 0 | 3 | 7.328 | ~0 | 3 | 4.11 |
| **1** | **5** | **9.802** | **−0.142** | **3** | **5.08** |
| 2 | 7 | 10.449 | −0.213 | 3 | 5.06 |
| 3 | 9 | 10.685 | +0.248 | 3 | 4.90 |
| 4 | 11 | 10.795 | +0.224 | 3 | 4.75 |

The winding-5, 3-component braid computes cleanly (correct baryon topology). But
the charm projection is $O(5)$ and **flat/non-monotonic in the twist knob** — it
*peaks* at $k=1$ then decreases. Against the proton $[3]$-block anchor (3.05) the
ratio is $\sim1.67$ — undershooting the current $m_c/m_\text{light}\sim372$ by
$\sim220\times$ and even undershooting the *constituent* $\Lambda_c/p=2.44$. **No
twist count reaches the charm scale**, so even spending the (fit) knob fails. The
knob is flagged; Reading (B) is **not canonical**.

## Structural reason (why the block ratio is $O(1)$, not $O(100)$)

Why the block ratio of a **writhe-balanced** baryon braid comes out $O(1)$.
Item 1 is Lean-proved; item 2 follows from it; item 3 is a **size estimate, not
a proof** — so the combination is a scope-(a) sharpening (see §Scope
classification), not a structural exclusion:

1. The two **1-dimensional** block characters are pure writhe monomials —
   $\chi_{[3]}(\beta)=q^{\,w(\beta)}$ and $\chi_{[1^3]}(\beta)=(-q^{-1})^{\,w(\beta)}$,
   where $w$ is the writhe (exponent sum). This is exact multiplicativity of a
   1-dim representation. Formalized sorry-free:
   `QOU.MassTheory.TrivialBlockWrithe.chi_trivial_eq_q_zpow_writhe` /
   `chi_sign_eq_negqinv_zpow_writhe`
   (`content/quantum-observable-universe/lean/QOU/MassTheory/TrivialBlockWrithe.lean`,
   registered in `QOU.lean`; lean-direct EXIT=0, sorry-free).
2. The Borromean baryon has **writhe 0** ($3(+1)+3(-1)$), so both 1-dim block
   characters are pinned to **1**, independent of $q$ — they carry no
   winding/generation information at all.
3. The remaining $[2,1]$ block has $\dim=2$, so its character is $O(2)$ on a
   short balanced braid — an **estimate**, not a proved bound. With the two
   1-dim blocks pinned to $1$, an $O(100)$ ratio would have to come entirely
   from this one $2$-dimensional character; the computed value is $1.35$.

This is the *forward* (formalize-first) prune: **don't search for the
generation hierarchy in the block ratio of a writhe-balanced braid.** It also
sharpens where a viable mechanism could hide: a large hierarchy needs either
(i) a **writhe-imbalanced** carrier (so $q^{w}$ with $|w|\gg1$ supplies the
scale — but that is a different, non-baryon topology), or (ii) the hierarchy is
**not** a block ratio at all (e.g. an absolute muon-anchored Hecke energy per the
canonical mass law, with charm entering through a heavy-flavour dressing functor
that is undefined in the corpus).

## Scope classification (STRICT)

- **Reading (A):** **scope-(a)** — "the $H_3$ Frobenius block ratio, alone, does
  not reproduce the charm/light hierarchy (276× undershoot)." It does **not**
  exclude the complex-mass functional; it excludes the *block-ratio reading* of
  it at balanced writhe.
- **Writhe pruning (item 1–3):** a **proved** structural fact (Lean lemma), but
  it is a *scope-(a) sharpening*, **not** a scope-(b) exclusion of the functional
  — a writhe-imbalanced or non-block mechanism is not ruled out.

## Derived vs assumed

- **Derived (no fit):** the $H_3$ irreps, the validated $\mathrm{tr}_M$, the
  `y_λ` (from $q_0$), and the Reading (A) block ratios. The writhe identities
  (Lean).
- **Assumed:** the *identification* "generation $\leftrightarrow$ Wedderburn
  block of $H_3$" (Reading A) and "winding $\leftrightarrow$ $\sigma_1^{2k}$
  twist" (Reading B). Both are natural but not corpus-derived; the twist count is
  an explicit knob. No knob was spent to force a match in Reading (A).

## Beans (env has no beans CLI — recorded here)

- **GAP (charm-mass block-ratio, closed scope-(a)):** the $H_3$ Frobenius block
  ratio on the writhe-0 baryon is $O(1)$ (1.35), not the $O(100)$ charm/light
  hierarchy. Proved: the two 1-dim blocks are writhe monomials and vanish to 1 at
  writhe 0 (`QOU/MassTheory/TrivialBlockWrithe.lean`). Do **not** re-run the block-ratio
  reading at balanced writhe.
- **GAP (charm-mass, surviving routes):** a viable complex-mass mechanism must
  supply the scale from *outside* the balanced-writhe block ratio —
  candidate (i) a **writhe-imbalanced heavy-flavour carrier** (needs a defined
  charmed-hadron braid with $|w|\gg1$ **and** the right topology/components), or
  (ii) the **absolute muon-anchored Hecke energy** (canonical mass law) with a
  **heavy-flavour dressing functor** — undefined in the corpus
  (`flavor-dressing-functor.md`). Both open; both need a foundational object the
  corpus does not yet have.
- **GAP (unchanged from prior audit):** the gg→cc̄ two-gluon demand profile for
  the operator-selection SDP remains underived.
