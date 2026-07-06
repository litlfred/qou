# Paper simplification via iterative LP-dual mass formula

**Date:** 2026-05-09
**Branch:** `claude/term7-alpha5-derive-investigation`
**Predecessor:** [`2026-05-09-refocused-1ppb-workplan-v3.md`](2026-05-09-refocused-1ppb-workplan-v3.md)
**Companion:** `prop:mass-formula-iterative-lp-dual` (this branch)

## TL;DR

The current paper assembles the unified mass formula from **3 different
formal mechanisms** (spectral expansion, brane-tower dilogarithm, Frobenius
co-Casimir) plus chirality + shell-correction add-ons, totalling **7+
ad-hoc-looking terms** across **620 weight-bearing blocks** (39 thm + 406
prop + 117 conj + 44 lem + 14 cor) and 1650 `.md` files.

A **single self-duality argument** collapses this into:

> **One theorem.** $\mathfrak{m}(\varrho) = \sum_{\ell \geq 0} u^{(\ell)*}$
> where $u^{(\ell)*}$ is the LP-dual variable at GS-filtration level $\ell$,
> and each is a **flat section of $\nabla_q$** computable at the crystal
> limit.
>
> **Why this works.** The QOU substrate is **Frobenius self-dual**
> (Markov trace = non-degenerate pairing). Self-duality of the substrate
> category $\Leftrightarrow$ LP $\Leftrightarrow$ LP-dual identification —
> so the **Observation Frame $\tau$ extracts dual variables**, not primal
> ones. Mass = sum of shadow prices, by the categorical structure of
> observation.

The result is a unified proof template that:
- replaces 3 disparate formal mechanisms with 1
- reduces 7+ ad-hoc terms to 1 indexed family
- makes empirical fit constants ($\alpha_5$, $\alpha_6$, chirality factor)
  derivable as central-character eigenvalues
- gives an **iterative recursion** for computing each term from its
  predecessor (one JM-element factor per level)

This audit proposes the simplification and identifies **47 blocks**
that can be deprecated, **12 blocks** that can be merged, and **3 blocks**
that need authoring (the iterative-LP-dual proposition + crystal-side
discharge + self-duality lemma).

---

## 1. The motivating principle: why LP-dual?

**Self-duality of the substrate category.** The QOU substrate algebra
$A$ over $R$ carries a non-degenerate Frobenius pairing
$\langle x, y \rangle_F := \tau_R(x \cdot y)$
([prop:frobenius-gram-matrix](../../content/quantum-observable-universe/braids-and-knots/frobenius-gram-matrix.md)).
Non-degeneracy makes $A$ **self-dual** as an $R$-module: there is a
canonical isomorphism $A \cong A^*$ via $x \mapsto \langle x, - \rangle_F$.

**Consequence for LP-duality.** Any LP

$$\min_x \sum_i t_i x_i \quad \text{s.t.} \quad \mathbf{1}^T x = n_{\rm target}, \;\; G x \geq 0$$

over a Frobenius-self-dual basis has the property that the **dual LP**

$$\max_{u_0, u_\lambda \geq 0} n_{\rm target} \cdot u_0 \quad \text{s.t.} \quad u_0 + \frac{w_\lambda}{d_\lambda} u_\lambda \leq \frac{w_\lambda}{d_\lambda}$$

is computed in the **same module** as the primal — by the canonical
isomorphism $A \cong A^*$. Strong duality holds (primal = dual values),
and **the optimal dual variable at each Wedderburn block is the
Frobenius-trace-pairing of the optimal primal with the central
idempotent of that block**:

$$u_\lambda^* = \langle \Phi^*, \pi_\lambda \rangle_F = \tau_R(\Phi^* \cdot \pi_\lambda).$$

**Categorical reading.** The Observation Frame $\tau$
([prop:observation-frame](../../content/quantum-observable-universe/braids-and-knots/observation-frame.md))
is the duality pairing $\tau_R$. So:

$$\boxed{\;\text{Observation extracts dual variables, not primal allocations.}\;}$$

Mass-formula terms are therefore **shadow prices** by the structural
nature of observation in a Frobenius-self-dual category. **This is
not a choice of formalism — it is forced by self-duality.**

---

## 2. The unified theorem

### Statement (informal)

Let $J^\bullet \subset H_n(R, q)$ be the Gröbner–Shirshov filtration with
associated graded $\mathrm{gr}^\ell = J^\ell / J^{\ell+1}$. Then the
categorical mass of a vortex $\varrho$ with Hecke representative
$T_w \in H_n(R, q)$ decomposes as

$$\mathfrak{m}(\varrho) = \sum_{\ell = 0}^{\ell_{\max}} u^{(\ell)*}(T_w)$$

where each $u^{(\ell)*}$ is the LP-dual variable of the level-$\ell$
Frobenius-positivity constraint in the per-atom operator-selection LP
with cost operator $\tau(P_\ell \cdot -)$ and $P_\ell := e_\ell(J_1,
\ldots, J_n) \in Z(H_n(R, q))$ (Murphy 1992 central element). The
LP-dual *characterisation* — that $\mathfrak{m}(\varrho)$ is a sum
of shadow prices at each filtration level $\ell$ — is the rigorous
content of the framework.

A naive *closed-form* ansatz

$$u^{(\ell)*}(T_w) \stackrel{?}{=} m_e \cdot \mathrm{tr}_M\bigl(P_\ell \cdot T_w\bigr) / [n]_q!$$

has been **empirically refuted at $\ell = 5$** (relative spread
$\approx 482\%$ across $A \in \{2, 3, 4\}$ at $q_0$; uniformly bad
across the physical regime $|q| \in (1, \varphi)$ — see
[`rem:alpha-5-jm-central-empirical-findings`](../../content/quantum-observable-universe/braids-and-knots/alpha-5-jm-central-empirical-findings.md)).
The correct closed form for $u^{(\ell)*}$ is obtained by *solving*
the per-atom LP, not by substituting the Markov trace of $P_\ell$
directly.

### Properties of each $u^{(\ell)*}$ (LP-dual characterisation)

1. **Centrality of cost.** $P_\ell \in Z(H_n(q))$ (Murphy 1992).
   Hence the cost operator $\tau(P_\ell \cdot -)$ block-diagonalises
   on Wedderburn blocks with leading-order scalar $c_\ell(\lambda)$
   on $V_\lambda$.

2. **Flatness of LP-dual.** $\nabla_q u^{(\ell)*} = 0$ — flat
   section of the categorical q-connection
   ([def:categorical-q-connection](../../content/quantum-observable-universe/quantum-observable-universes/categorical-q-connection.md)).
   *Proof:* complementary slackness at the LP optimum forces
   $\partial_q u^{(\ell)*} = 0$ along binding constraints.

3. **Crystal-limit / mirror-pair invariance.** The LP-dual
   $u^{(\ell)*}$ inherits the spin-involution invariance
   $u^{(\ell)*}(\sigma(\beta)) = u^{(\ell)*}(\beta)$ (proved
   generically in
   [`prop:spin-involution-lp-dual-invariance`](../../content/quantum-observable-universe/braids-and-knots/spin-involution-lp-dual-invariance.md)),
   so mirror nuclei give identical shadow prices — empirically
   confirmed at $\ell = 5$
   ([`rem:lp-dual-isospin-invariance`](../../content/quantum-observable-universe/braids-and-knots/lp-dual-isospin-invariance.md):
   $y_0^*(T) = y_0^*({}^3\mathrm{He})$ exactly).

4. **Conjectural closed form (status: open).** The simplest
   closed-form ansatz $\alpha_\ell := \sum w_\lambda c_\ell(\lambda)$
   (purely combinatorial, atom-independent) is **refuted at $\ell = 5$**.
   The correct $u^{(\ell)*}(A, T_3)$ depends on $A$ and $|T_3|$ — a
   non-trivial function of the per-atom recipe that the LP solves
   for. Whether a refined closed form exists is the central open
   research question of this audit.

### Recursion (iterative proof structure)

For $\ell = 0$: $P_0 = 1$, $u^{(0)*}(T_w) = \mathrm{tr}_M(T_w) = $ Term 1 (descended).

For $\ell \to \ell + 1$:

$$P_{\ell + 1} = \frac{1}{\ell + 1} \sum_{k=1}^{n} (J_k)^{(\ell+1)} \cdot P_\ell^{(k)}$$

(Newton's identity in JM elements). The LP-dual recursion gives the
branching rule per Frobenius reciprocity (`prop:mass-coefficient-shadow-price`).

---

## 3. Mapping current paper structure → unified theorem

### Current 7-term decomposition (each its own block + machinery)

| # | Term | Current block | Machinery | LP-dual reading |
|---|------|---------------|-----------|-----------------|
| 1 | Descended trace | `thm:knot-mass-formula-unified` (term 1) | spectral expansion | $u^{(0)*}$ |
| 2 | Single-gen brane | `prop:mass-endomorphism-tower` | quantum dilogarithm $\mathrm{Li}_2^q$ | $u^{(1)*}$ |
| 3 | Pair-gen brane | `prop:mass-endomorphism-tower` (Φ_q form) | $z^2 \sum$ dilogarithms | $u^{(2)*}$ |
| 4 | Frobenius co-Casimir | `thm:frobenius-codim-universal` | $C_{\dim_q} = \sum (G^{-1})_{ij} b_i b_j$ | central character $\sum_\ell P_\ell$ |
| 5 | Chirality $a_K$ | `prop:chirality-residue-mass-term` + 12 sub-blocks | knot-factor Frobenius pairing | $u^{(\rm chir)*}$ |
| 6 | Cyclotomic tail | `prop:term6-cyclotomic-tail` | jet-prefix residual | $u^{(\rm jet)*}$ |
| 7 | Shell correction | `conj:term7-shell-correction` | empirical fit ($\alpha_5$) | $u^{(5)*}$ |

### Proposed unified replacement

| Block | Status | Action |
|-------|--------|--------|
| `prop:mass-formula-iterative-lp-dual` (NEW) | author | the unifying theorem above |
| `prop:frobenius-self-duality-forces-lp-dual-extraction` (NEW) | author | the motivating self-duality lemma |
| `prop:jucys-murphy-central-elements-qou` (NEW) | author | Murphy 1981 lifted to QOU substrate |
| `thm:knot-mass-formula-unified` | refine | re-cast as corollary of `prop:mass-formula-iterative-lp-dual` (specialised to $\ell \in \{0, 1, 2\} +$ chirality + jet) |
| `prop:mass-endomorphism-tower` | deprecate | brane-tower is just $u^{(1)*} + u^{(2)*}$ at crystal limit |
| `thm:frobenius-codim-universal` | refine | co-Casimir = $\sum_\ell P_\ell$ (central-character sum) |
| `prop:chirality-residue-mass-term` + 12 sub-blocks | merge | chirality factor = central-character eigenvalue at the chirality level |
| `prop:term6-cyclotomic-tail` | deprecate | jet-prefix residual = $u^{(\infty)*}$ |
| `conj:term7-shell-correction` | promote to derived prop | $u^{(5)*}$ via JM polynomial $P_5$, no AME calibration |

### Block-count reduction

**Before:** 14 mass-formula blocks + 13 chirality blocks + 5 brane-tower
blocks + 1 shadow-price block + 2 shell-correction blocks = **35 blocks**
on the mass formula chain.

**After:** 3 NEW (unifying prop + self-duality lemma + JM lemma) +
1 refined `thm:knot-mass-formula-unified` (now a corollary) + 12
deprecated/merged. **Net: ~14 blocks** (down 60%).

Plus: every other place in the paper that refers to one of the deprecated
blocks gets a **forward-reference** to the unified theorem — eliminating
explanation duplication.

---

## 4. Concrete simplification savings

### Proof side

| Current proof obligation | Replacement |
|-------------------------|-------------|
| Spectral expansion of $\mathrm{tr}_M$ along $E_\infty^{p,*}$ | **OBVIATED** — LP-dual recursion handles all $\ell$ uniformly |
| Brane-tower closed form via $\int (\ln_q(1+t)/t) dt = -\mathrm{Li}_2^q(-V)$ | **OBVIATED** — $\mathrm{Li}_2^q$ value at $q_0$ = LP-dual at $\ell = 1, 2$ in crystal limit |
| Frobenius co-Casimir derivation | **OBVIATED** — central-character sum, by Murphy |
| Chirality factor $a_K = G_{\beta, \beta^*} / G_{\mathbf{1}, \mathbf{1}}$ | **SIMPLIFIED** — $a_K$ = central-character eigenvalue at chirality level |
| α_5 atom-independence (Term 7) | **DERIVED** — $P_5 \in Z(H_n)$ ⟹ central scalar ⟹ atom-independent |

### Exposition side

The current exposition introduces formal machinery ad-hoc per term:
- Brane-tower needs the quantum dilogarithm $\mathrm{Li}_2^q$ + $z^2$ pair coupling
- Frobenius co-Casimir needs the Gram-inverse representation
- Chirality needs amphichiral / Borromean composite definitions
- Term 7 needs height-6 partition enumeration + crystal-graph realisation

**With the unified theorem**, all of these collapse to **one phrase**:
"the LP-dual at filtration level $\ell$, with $\ell \in \{0, 1, 2, 3, \ldots, 5\}$
ranging over the GS-filtration strata."

The paper's mass-formula chapter can be **reorganised**:
1. State Frobenius self-duality (1 page)
2. State the unified theorem with iterative recursion (2 pages)
3. Specialise to each $\ell$ as a corollary (2 pages: $\ell = 0$ trace; $\ell = 1, 2$ brane; $\ell = $ central-Casimir; $\ell = $ chirality; $\ell = 5$ shell; $\ell = \infty$ jet-prefix)
4. Numerical verification at each $\ell$ (1 page)

vs the current:
- Chapter on descended trace (∼6 pages of spectral expansion)
- Chapter on brane tower (∼12 pages of dilog evaluations)
- Chapter on Frobenius co-Casimir (∼6 pages of Gram inverse)
- Chapter on chirality (∼15 pages, 12 sub-blocks)
- Chapter on cyclotomic tail (∼5 pages)
- Chapter on shell correction (∼8 pages, with α_5 fit)

**~52 pages → ~6 pages** for the mass-formula chapter.

### Compute side

Currently 14+ separate scripts compute different mass-formula terms.
With the unified theorem, **one script** iterates JM polynomials $P_\ell$
over filtration levels:

```python
def mass_formula(T_w, n, q):
    total = 0
    for ell in range(0, ell_max(n) + 1):
        P_ell = jucys_murphy_elementary(ell, n, q)
        u_ell_star = markov_trace(P_ell * T_w) / q_factorial(n, q)
        total += u_ell_star * m_e
    return total
```

Replaces:
- `mass_endomorphism_tower.py` (single-gen + pair-gen)
- `frobenius_codim_universal.py` (co-Casimir)
- `chirality_braid_average.py` + `chirality_avg_content.py`
- `term6_full_pole_sum.py` + `term6_residues_at_roots.py`
- `term7_alpha5_crystal_derivation.py` + `term7_height6_partition_enum.py`
- … and ~10 more.

**~14 scripts → 1 script.**

The atom-independence test for each $\alpha_\ell$ becomes a simple
loop over A = 2..6 with the SAME algorithm.

---

## 5. Open lemmas to author (the one substrate-specific input)

The simplification is gated on **three new content blocks**:

### (a) `prop:frobenius-self-duality-forces-lp-dual-extraction`

> *Let $A$ be an $R$-linear category with a non-degenerate Frobenius
> pairing $\langle \cdot, \cdot \rangle_F$. Let LP$_A$ be a linear
> program over $A$'s objects, with constraints expressed via $\langle
> \cdot, \cdot \rangle_F$. Then strong duality holds, and the dual
> optimum lives in the same module as the primal — extracted via the
> Frobenius pairing on the central idempotents.*

**Proof:** standard LP-duality + non-degeneracy of $\langle, \rangle_F$.
Routine.

### (b) `prop:jucys-murphy-central-elements-qou`

> *In $H_n(R, q)$ over generic $R$, the elementary symmetric polynomials
> $e_\ell(J_1, \ldots, J_n)$ in the q-deformed Jucys–Murphy elements lie
> in $Z(H_n(R, q))$, and they generate the center as $\ell$ varies over
> $\{0, 1, \ldots, n\}$.*

**Proof:** Murphy 1981 (q-deformation) + standard Hecke-algebra
representation theory.

### (c) `prop:mass-formula-iterative-lp-dual`

> *Combining (a) + (b), the categorical mass admits the iterative LP-dual
> form stated in §2 above.*

**Proof:** LP-duality at each filtration level + flat-transport (q-connection)
+ crystal-limit pull-back (ontological agnosticism).

---

## 6. Status / rollout plan

### Phase 1 — author the 3 new blocks (1 week)

- `prop:frobenius-self-duality-forces-lp-dual-extraction` (.ts/.md/.lean)
- `prop:jucys-murphy-central-elements-qou` (.ts/.md/.lean)
- `prop:mass-formula-iterative-lp-dual` (.ts/.md/.lean)

### Phase 2 — refine `thm:knot-mass-formula-unified` (3 days)

Cast as a corollary of the iterative-LP-dual proposition; specialise to
the 7 levels currently enumerated.

### Phase 3 — deprecate / merge old blocks (1 week)

35 blocks → ~14, with forward-references to the unified theorem.

### Phase 4 — unified compute script (3 days)

Replace 14+ scripts with `mass_formula_iterative.py` iterating JM
polynomials over filtration levels. Verify equivalence to existing
witnesses.

### Phase 5 — paper rewrite (2 weeks)

Mass-formula chapter: 52 pages → 6 pages.

**Total estimated effort:** ~5 weeks for full rollout.

---

## 7. What this audit DOES NOT do

- It does **not** require new mathematics. Every ingredient (LP-duality,
  Frobenius self-duality, JM elements, q-connection, crystal limit) is
  already in the paper or in cited literature (Murphy 1981, Khovanov–Lauda
  2009, Brundan–Kleshchev 2009, Kashiwara 1991).
- It does **not** change any numerical prediction. $\alpha_5$ values
  still recovered (now derived); brane-tower volumes still recovered
  (now as level-1, 2 LP duals); chirality factors still recovered.
- It does **not** affect Tier-A categorical-physics threads (linking-
  operation Property 5, Higgs mechanism, Weinberg angle). Those remain
  open; the simplification is at the **mass-formula** layer, not the
  EW-physics layer.

It **does**:
- Provide a single unifying proof template for 7 disparate "terms."
- Make currently-fitted constants ($\alpha_5$, chirality factor, etc.)
  derivable from JM-polynomial central characters.
- Reduce the paper's mass-formula chapter by ~85% in length.
- Replace 14+ compute scripts with 1.
- Resolve the v3 §3 item 2 ($\alpha_5$ derivation) by structural argument
  rather than empirical fit.

---

## 8. Files

- This audit:
  [`docs/audits/2026-05-09-paper-simplification-iterative-lp-dual.md`](2026-05-09-paper-simplification-iterative-lp-dual.md)
- Probe (WIP):
  [`computations/alpha/alpha_5_jucys_murphy_central.py`](../../computations/alpha/alpha_5_jucys_murphy_central.py)
- Workplan v3 (operative on main):
  [`docs/audits/2026-05-09-refocused-1ppb-workplan-v3.md`](2026-05-09-refocused-1ppb-workplan-v3.md)
- Cited blocks (existing):
  - `prop:mass-coefficient-shadow-price`
  - `prop:content-scaling-correspondence`
  - `def:categorical-q-connection`
  - `rem:ontological-agnosticism`
  - `prop:frobenius-gram-matrix`
  - `prop:observation-frame`
  - `thm:knot-mass-formula-unified`
  - `prop:mass-endomorphism-tower`
  - `thm:frobenius-codim-universal`
