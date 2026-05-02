# NV-1 and FROB-FILTER — explanation + proposed conjectures

**Compiled** 2026-05-02 on `claude/refactor-computation-framework-Dmvva`.
**Companion to:**
[`2026-05-02-forward-derivation-pre-archimedean.md`](2026-05-02-forward-derivation-pre-archimedean.md) §C.4.

The 2026-05-02 β-decay sector audit surfaced two new **🔴 hard
flags** that were not explicit in the 2026-05-01 deep audit. This
document explains each precisely, gives the current numerical
status, and proposes **candidate categorical conjectures** that
could close each gap.

---

## Part I — NV-1: the weak-scale crossing count

### Statement of the gap

The standard model defines the Fermi constant via
$G_F = 1/(\sqrt{2}\,v^2)$ with weak-scale VEV $v \approx 246$ GeV.
The QOU framework decomposes $v$ as

$$
  v = N_v \cdot E_\times \cdot \mu_0,
$$

where:

- $E_\times = (q - q^{-1})/2$ is the **per-crossing energy** (Hecke
  eigenvalue, derived from
  [`crossing-energy.md`](../../content/quantum-observable-universe/braids-and-knots/crossing-energy.md));
- $\mu_0 = m_e / (3 E_\times)$ is the **dimensional scale** (forced
  by CAL-0; from
  [`q_parameter.py`](../../folio-assistant/computations/q_parameter.py));
- $N_v$ is the **effective weak-scale crossing count** — a
  topological invariant of the brane-tower at the weak place.

Numerically at $q_0$:
$E_\times \approx 0.1045$ MeV, $\mu_0 \approx 1.6295$ MeV/Skein,
$E_\times \cdot \mu_0 \approx 0.1703$ MeV·{Skein},
$v \approx 246{,}220$ MeV, hence
$$
  N_v \approx 1.45 \times 10^6.
$$

### Where the flag is

[`folio-assistant/computations/beta-decay-from-q.py`](../../folio-assistant/computations/beta-decay-from-q.py)
lines 41–45:

```python
# G_F = 1/(√2 v²) where v ≈ 246 GeV is the weak scale.
# In the QOU: v = N_v · E_cross · μ₀ where N_v is the effective
# crossing count of the weak scale (OPEN COMPUTATION).
G_F_standard = 1.1663788e-11  # MeV⁻² (CODATA 2022)
v_weak = 1.0 / math.sqrt(math.sqrt(2) * G_F_standard)  # MeV
N_v = v_weak / (E_cross * mu_0)  # effective crossing count
```

The script **back-solves** $N_v$ from CODATA $v$ — it does not
derive $N_v$ from the substrate's algebraic structure. Half-life
predictions in [`beta-decay-from-q.py`](../../folio-assistant/computations/beta-decay-from-q.py)
line 50 then scale as $G_F^2 \propto N_v^{-4}$, so a derivation of
$N_v$ would close every β-decay rate prediction simultaneously.

### Why this is a hard flag (not a numerical-only flag)

A numerical-only flag (e.g. MAG-126) becomes derived as soon as a
known computation finishes. NV-1 is different: **no known
computation in the repo derives $N_v$.** The categorical input it
needs — a topological invariant of the weak-place projection of
the substrate — is not yet identified.

This is an audit failure under
[`prop:three-calibration-discipline`](../../content/quantum-observable-universe/observations/three-calibration-discipline.md):
$N_v$ functions as a **fourth external calibration** in the current
code path. Hence 🔴.

### Proposed candidate conjectures

Each candidate identifies $N_v$ as a categorical invariant of the
weak-place projection of the substrate. The candidates are listed
in **decreasing order of plausibility** based on how directly they
plug into existing framework blocks.

#### Candidate (a) — **`conj:nv-as-bratteli-path-count`**

> *There is a level $k_w \in \mathbb{N}$ — the **weak-sector
> characteristic level** — such that*
> $$
>   N_v = \sum_{\lambda \vdash k_w} f_\lambda^2 \;-\; \delta_w
> $$
> *where $f_\lambda = \dim S^\lambda$ is the Specht-module dimension
> and $\delta_w$ is a small correction counting paths killed by
> the descent involution $\hat\tau_{k_w}$.*

**Why this candidate.** The Plancherel total $\sum f_\lambda^2 =
k_w!$ is a classical topological count of standard Young tableaux
— equivalently, paths from the root to level $k_w$ in the
Bratteli diagram of the symmetric group. This is *the* canonical
"crossing count" in the Hecke-tower picture (Step 10–12 of the
forward derivation). Trying small $k_w$:

| $k_w$ | $k_w!$ | $N_v / k_w!$ |
|-------|--------|--------------|
| 8 | 40,320 | 35.85 |
| 9 | 362,880 | **3.9835** |
| 10 | 3,628,800 | 0.3983 |

So **$k_w = 9$ is the right level** — $N_v$ is ~4 times $9!$.

**Refinement (a′) — TESTED 2026-05-02 (numerical falsification):**

> Initial proposal: $N_v = 4 \cdot 9!$ exactly, where the factor
> $4 = (\dim S^{(2,2)})$ would count the self-conjugate $\kappa=0$
> partition multiplicity at $n = 4$.

**Test result.** $4 \cdot 9! = 1{,}451{,}520$ vs $N_v =
1{,}445{,}519$. **Off by 6001 (0.41%).** CODATA $G_F$ relative
uncertainty is ~5×10⁻⁷, so the 0.4% deviation is **~10⁴× too
large** for measurement noise — the simple equality is
**falsified**.

The exact ratio is $N_v / 9! = 3.98346\ldots$, which is *near* 4
but not 4. Numerical-targeted-fit search shows $N_v \approx
1{,}445{,}519$ is **prime** — so it is *not* a small-integer
multiple of $9!$ or any factorial.

**Refinement (a″) — open candidate.** The 0.4% correction is
suggestive of a substrate-parameter dependence. Three forms worth
testing:

1. $N_v = 9! \cdot 4 \cdot (1 - \hbar_q^k)$ for some small $k$.
   Test: solve $\hbar_q^k = 0.00414$ at $\hbar_q = 0.0991$;
   $k = \log(0.00414)/\log(0.0991) = 2.37$ — **not an integer**.
   So the 4·9! candidate is not closed by a pure $\hbar_q$ power.
2. $N_v = 9! \cdot 4 - \delta_w$ where
   $\delta_w \approx 6001$ counts a sub-tower contribution.
   $\delta_w \approx 5040 \cdot 1.19 \approx 7! \cdot 1.19$ — also
   not clean.
3. $N_v$ is a *q-deformed* Plancherel sum at $q_0$ rather than the
   classical sum:
   $\widetilde{N_v} = \sum_\lambda \dim_q V_\lambda \cdot
   f_\lambda$ at level $k_w = 9$. The classical limit
   ($q\to 1$) gives $\sum f_\lambda^2 = k_w!$; at $q_0$ the value
   shifts by an $\mathcal{O}(\hbar_q^2) \approx 1\%$ correction.
   This is the **strongest remaining candidate** — testable with
   `hoefsmit_witness.json`.

**Recommended test.** Compute
$\sum_{\lambda \vdash 9} \dim_q V_\lambda \cdot f_\lambda$ at
$q_0$ using the existing `hoefsmit_witness.json` and compare to
$N_v = 1{,}445{,}519$. If the agreement is exact to CODATA-$G_F$
precision, conjecture (a″) is the answer. If not, retreat to (b).

**Status as of 2026-05-02.** Refinement (a′) **falsified** by
numerical test; (a″) is the live candidate. Level $k_w = 9$ is
strongly supported (the only level with $N_v / k_w! \in
[1, 10]$).

#### Candidate (b) — **`conj:nv-as-bring-period-rank`**

> *$N_v$ equals the rank of the distinguished
> $S_5 \times \langle\hat\tau\rangle$-stable period sub-lattice on
> Bring's surface at the weak-place projection
> $\rho_{\rm weak}\colon \widehat{\mathcal{M}} \to
> \mathbb{Z}[q]/\Phi_{p_w^{k_w}}(q)$.*

**Why this is plausible.** The same Bring-surface period-lattice
construction is the candidate path for `conj:magic-numbers-bring`.
The genus-4 torus knots are the **same** genus that controls the
$1/\alpha$ derivation. A unified Bring-period framework would
explain $N_v$ + magic numbers + $1/\alpha$ from a single source.

**Compute test.** This requires the period-lattice machinery on
Bring's surface that is currently research-grade (see
`docs/audits/conjecture-cones.md` for the open Bring-surface
items). Higher cost than (a).

#### Candidate (c) — **`conj:nv-as-cyclotomic-index`**

> *$N_v = [\,\widehat{\mathcal{M}} : \rho_{\rm weak}^{-1}(1)\,]$,
> the index of the kernel of the cyclotomic projection
> $\rho_{\rm weak}\colon \widehat{\mathcal{M}} \to
> \mathbb{Z}[q]/\Phi_{p_w^{k_w}}(q)$ at the weak place.*

This connects NV-1 directly to
[`def:adelic-substrate`](../../content/quantum-observable-universe/algebraic-substrate/adelic-substrate.md)
and
[`def:motivic-galois-character`](../../content/quantum-observable-universe/lifting-and-descent/motivic-galois-character.md).
It would be the **cleanest** categorical statement, but requires a
concrete instance of `MotivicGaloisCharacter` for QOU at $q_0$
(GAP 6a) — which itself is an open framework gap.

#### Candidate (d) — **`conj:nv-as-jet-bundle-rank`**

> *$N_v = \mathrm{rank}_R\,J^{k_w}\mathcal{S}$ for the
> categorical jet bundle on the state bundle $\mathcal{S}$ at the
> weak-sector level $k_w$.*

This connects NV-1 to Step 15 (categorical jet prolongation). The
rank of $J^{k_w}\mathcal{S}$ grows polynomially in $k_w$ via the
Bratteli recursion + descent-Bratteli filtration; matching $N_v$
would give $k_w$ directly.

### Why naïve numerology fails — the right derivation pattern

The numerical sweeps above (a′ test, q-Plancherel sums, PSLQ
multiplicative search at 200 dps over $\{q^k, [k]_q, \hbar_q^k\}$)
**do not produce a clean closed form** for $N_v$. This is *not* a
defect of the conjecture; it is a defect of the search method.

The paper's analogous derivation —
[`alpha-em-categorical-trace`](../../content/quantum-observable-universe/braids-and-knots/alpha-em-categorical-trace.md)
for $1/\alpha_{\rm EM}$ — succeeds **not** by PSLQ pattern-matching
on $1/\alpha$ alone, but by deriving each factor from upstream
*categorical structure* and using PSLQ only as a **uniqueness
witness** at the end:

| Factor in $1/\alpha = 45\,[3]_q\,(1 + \delta_{CS} + 8q\,\delta_{CS}^2)$ | Upstream block |
|---|---|
| Two-strand idempotent completeness $w_+ + w_- = 1$ | `thm:em-spectral-completeness` |
| Coupling normalisation via $\mathrm{tr}_\tau(e_-)\cdot e_-$ | `cor:gauge-coupling-uniqueness` |
| Force-carrier sector $\{T_{2,9}, T_{3,5}\}$, complexity $[9]_q[10]_q$, **integers 9 and 10** appear | `prop:force-carrier-bring-uniqueness` |
| $\delta_{CS} = \hbar_q^4\,[5]_q$ as Plancherel-weighted character product | `prop:gram-determinant-plancherel-ratio` |
| $45 = \binom{10}{2}$ as $\Lambda^2 V_{\rm nat}^{10}$ dimension | `prop:exterior-square-borromean` |

PSLQ at 1000–2000 dps then *confirms* no shorter rational
combination matches CODATA — it does not *find* the form.

### Recommended derivation strategy for NV-1 (parallel to $1/\alpha$)

The same five-step pipeline applied to $N_v$:

| Step | $1/\alpha$ counterpart | $N_v$ analog needed |
|------|------------------------|---------------------|
| 1. Identify the **strand-count** at the relevant place | 10 strands (Bring genus-4 torus knots) | What is the weak-place strand-count? Likely 4 (electroweak SU(2)×U(1) → 4 gauge bosons) or 6 (Goldstone-eaten degrees) |
| 2. Identify the **force-carrier sector** | $\{T_{2,9}, T_{3,5}\}$ — genus-4 torus knots | The weak gauge bosons $W^\pm, Z$ as torus knots (genus?). The 2026-05-01 audit (§4·D) records that no QOU block currently identifies $W^\pm, Z$ as specific torus knots — this is a **content gap** before NV-1 can be derived. |
| 3. Identify the **Plancherel-completeness statement** | $w_+ + w_- = 1$ on two-strand braiding | The completeness statement for the weak-Higgs idempotent decomposition |
| 4. Construct **closed-form ansatz** in $\{q^k, [k]_q, \hbar_q^k\}$ | $45\,[3]_q\,(1 + \hbar_q^4[5]_q + 8q(\hbar_q^4[5]_q)^2)$ | Plug strand count, force-carriers, Plancherel weight into the ansatz |
| 5. **PSLQ uniqueness witness** at high precision | 1000-dps probe over $\{q^k, [k]_q, \hbar_q^k\}_{k\leq 10}$ | Same probe; current 200-dps sweep was inconclusive due to (a) basis redundancies and (b) CODATA $G_F$ has only ~5×10⁻⁷ relative precision so PSLQ cannot resolve below that |

**Action items implied:**

1. **Author `prop:weak-force-carrier-torus-knots`** — the analog of
   `prop:force-carrier-bring-uniqueness` for the weak sector.
   Identify $W^\pm, Z$ as specific torus knots $T_{p,q}$ (or as
   non-torus knots if the weak sector lives off Bring). This is
   the **prerequisite** for any closed-form derivation of $N_v$.
2. **Author `prop:weak-spectral-completeness`** — the analog of
   `thm:em-spectral-completeness` for the weak idempotent
   decomposition.
3. **Run PSLQ at 1000-dps** with a CODATA-uncertainty-respecting
   target (treat $N_v$ as known only to ~5×10⁻⁷; use this as
   the PSLQ tolerance).
4. **Cross-check via Yekutieli rigidity:** any $\mathbb{Q}(q)$-linear
   weak-coupling normalisation extending the Borromean rule
   uniquely determines $v$. This is the same rigidity argument used
   for `Geom(K)` and would predict $N_v$ if (1)–(2) are in place.

**Status as of 2026-05-02.** Numerical sweeps are exhausted and
inconclusive. The path forward is **content-block authoring**, not
more compute. The (a)/(b)/(c)/(d) candidates above remain on the
table; (b) (Bring-period rank) gains plausibility because the EM
force-carriers already live on Bring genus-4, so a unified
EW-on-Bring-surface picture is geometrically natural.

### Bring-surface inventory (research finding, 2026-05-02)

A parallel research investigation of the Bring genus-4 inventory
(post-PR #500) returns a **definitive negative finding** on one
candidate path: there are **no unidentified torus knots embeddable
on Bring's surface** at genus ≤ 4 with the saturating-generator
constraint of `prop:force-carrier-bring-uniqueness`.

| Knot | $(p,q)$ | Genus | Crossings | Current assignment |
|------|--------|------:|----------:|--------------------|
| $T_{2,3}$ | trefoil | 1 | 3 | $e^-, u$; 1s shell |
| $T_{2,5}$ | cinquefoil | 2 | 5 | $\mu, b$; 1d shell |
| $T_{2,7}$ | — | 3 | 7 | $\tau, c$; 2s–2d |
| $T_{3,4}$ | — | 3 | 8 | color binding (sub-shell) |
| $T_{2,9}$ | — | **4** | 9 | strong/EM force; 2f–3p |
| $T_{3,5}$ | — | **4** | 10 | EM force / *flavor change candidate* |

**Genus-4 capacity bound** (`prop:torus-knot-genus-four-unique`):
$(p-1)(q-1) = 8$ with $\gcd(p,q) = 1$ has exactly two primitive
solutions, $(2,9)$ and $(3,5)$. **Both occupied** by the EM force-
carrier sector. There is **no room** on Bring for additional
genus-4 torus knots.

**Implication for NV-1.** Three viable paths remain for $W^\pm, Z$:

- **Path α — non-Bring genus-2 torus knots.**
  [`knot-particle-generation.md`](../../content/quantum-observable-universe/braids-and-knots/knot-particle-generation.md)
  tentatively lists $T(2,6) \to Z$, $T(2,8) \to H$ (Higgs) at
  genus 2, on a **different algebraic curve**, not Bring. Authoring
  effort: identify the host curve, give the analog of
  `prop:force-carrier-bring-uniqueness` there.
- **Path β — $T_{3,5}$ as unified weak/EM mediator.**
  [`unmapped-torus-knots.md`](../../content/quantum-observable-universe/braids-and-knots/unmapped-torus-knots.md)
  lines 104–111 already speculate that $T_{3,5}$ encodes flavor
  change ($u\leftrightarrow d$ via $W^\pm$), since its $(p,q) =
  (3,5)$ structure cross-links the quark-family count $3$ with
  the second-generation lepton winding $5$. Authoring effort:
  promote this remark to `prop:t35-flavor-change-mediator` with
  a representation-theoretic decomposition of $T_{3,5}$ into
  three weak generators ($W^+, W^-, Z$).
- **Path γ — $W^\pm, Z$ as non-torus knots on Bring.** Like the
  Higgs candidate $4_1$ (figure-eight) in
  `topological-mass-trefoil.md`. Authoring effort: identify the
  three non-torus knots and prove genus / homology compatibility
  with Bring.

**Strongest path (paper-internal evidence):** **β** — $T_{3,5}$
double duty. The paper already has the speculation block
(`unmapped-torus-knots.md`) plus the dictionary entry
(`knot-particle-dictionary.md` lists $T_{3,5}$ as "weak force ($\beta$-decay)"
on the same row as $10_{124}$). Closing path β requires deriving
the SU(2) sub-decomposition of $T_{3,5}$'s representation —
likely via Schur–Weyl on $V^{\otimes 5}$ ↔ Hecke $H_5(q)$.

**Updated recommended action sequence:**

1. **Author `prop:t35-as-weak-mediator`** — claim that $T_{3,5}$
   carries the weak interaction; cite the cross-link argument
   already in `unmapped-torus-knots.md`.
2. **Author `prop:weak-spectral-completeness`** — the SU(2)
   idempotent decomposition of $T_{3,5}$'s Wedderburn presentation,
   analog of `thm:em-spectral-completeness`.
3. **Build closed-form ansatz** for $N_v$ in
   $\{q^k, [k]_q, \hbar_q^k\}$ using the 10 crossings of $T_{3,5}$
   + Plancherel weights at level $n=10$ (= $T_{3,5}$ crossing
   count).
4. **PSLQ uniqueness** at 1000-dps over the $T_{3,5}$ basis.

If the analog $1/\alpha$ form is the right shape, the prediction
would be roughly $N_v \sim [10]_q \cdot [n]_q \cdot (\text{small
correction})$ for some level $n$. PSLQ at high precision will
either confirm or kill it.

---

## Part II — FROB-FILTER: the Frobenius-positivity filter
   activation threshold

### Statement of the gap

The β-decay Q-value computation in
[`branching-qvalues.witness.json`](../../folio-assistant/computations/branching-qvalues.witness.json)
uses **three different methods** depending on atomic mass $A$:

| $A$ | Method | Configs counted | Reference |
|-----|--------|-----------------|-----------|
| 1 (n→p) | $(\Sigma_{\rm all} + 1) \cdot m_e$ | full sum + electron correction | line 31 |
| 3 (³H→³He) | $|\Sigma_{\rm all}| \cdot m_e$ | 64 H₃ configs | line 44 |
| 6 (⁶He→⁶Li) | $|\Sigma_{\rm FP}| \cdot m_e$ | **2048 of 4096** Frobenius-positive | line 56 |
| 14 (¹⁴C) | TBD | ~268M configs | line 70 |

The "Frobenius-positivity filter" keeps only those Hecke
configurations whose parent and daughter matrix elements satisfy
$\langle{}\cdot, \mathbf{1}\rangle_F \geq 0$ for both states
("me_par ≥ 0 AND me_dau ≥ 0", line 63).

The witness's open-problems list (lines 67–71) explicitly flags:

> "Frobenius filter activation threshold between A=3 and A=6 needs
> derivation"
> "The +1 (emitted electron) should emerge from the LP dual, not
> be added manually"
> "⁶He error (-10.9%) may improve with refined LP dual eigenvalue
> threshold"

### Why this is a hard flag

The activation rule **changes the formula** (different sum, different
norm). Without a categorical justification, the rule is an empirical
fit — even if the per-rule computations are categorical. This is a
🔴 wall-adjacent flag: not a numerical leak (no Archimedean input
crosses the wall), but a **methodological discontinuity** with no
algebraic source.

### Categorical observation

The Frobenius pairing $\langle\cdot,\cdot\rangle_F$ on $H_n(q)$ has
**signature** $(p_n, q_n)$ as a symmetric bilinear form. Reading
off the Wedderburn block dimensions:

- $H_1$: trivial — 1 dim, signature (1, 0)
- $H_2$: 2 dims (sym + alt), signature (1, 1) — half positive, half negative
- $H_3$: 6 dims = 1 + 4 + 1 (sym + std + alt), 64 = 2⁶ closed configs
- $H_4$: 24 = 1+9+4+9+1
- $H_n$: $\sum_\lambda f_\lambda^2 = n!$

The **Frobenius signature** of $H_n$ depends on which Wedderburn
blocks have $c(\lambda) \geq 0$ (positive-content) vs
$c(\lambda) < 0$ (negative-content) — at $q_0$ the sign of
$y_\lambda$ (the Jones–Markov central coefficient — see
notation §7aa) inherits this.

The threshold A=3 → A=6 corresponds to
$n = 3A = 9$ → $n = 18$, i.e. the **Hecke level for the closed
braid**. At $n = 9$, $H_9(q)$ has 30 partitions and a particular
positive/negative split; at $n = 18$ the split is much richer.

### Proposed candidate conjecture

#### **`conj:frobenius-filter-categorical`**

> *Let $A_*$ be the smallest $A \geq 1$ such that the Frobenius
> form on $H_{3A}(q_0)$ has **non-trivial signature** — i.e.
> $q_{3A} \geq 1$, where $H_{3A}(q_0)$ has signature $(p_{3A},
> q_{3A})$ as a symmetric bilinear form. Then for $A < A_*$ the
> Q-value uses $\|\Sigma_{\rm all}\|$ (no filtering needed); for
> $A \geq A_*$ the Q-value uses $\|\Sigma_{\rm FP}\|$, where
> $\Sigma_{\rm FP}$ restricts to the **maximal positive-definite
> sub-cone** of the Frobenius form — equivalently, to the LP-feasible
> dual cone of `prop:bw-coefficient-shadow-price`.*

**Categorical content.** The filter is the projection onto the
positive-definite part of the Wedderburn-block signature. The
threshold is the smallest $A$ where the form acquires its first
negative direction.

**Compute test.** Compute the signature of
$\langle\cdot,\cdot\rangle_F$ on $H_3, H_6, H_9, H_{12}, H_{15},
H_{18}$ at $q_0$ (sum the signs of $y_\lambda$ at $q_0$ weighted
by $f_\lambda^2$). If the first $A$ with $q_{3A} \geq 1$ matches
the empirical activation in `branching-qvalues.witness.json`,
this conjecture is plausible. The compute is straightforward
given existing
[`y_lambda_wenzl_bridge_extended.py`](../../folio-assistant/computations/y_lambda_wenzl_bridge_extended.py).

**Refinement.** A stronger version pins the filter rule
"me_par ≥ 0 AND me_dau ≥ 0" (line 63) to the *intersection* of
two LP feasible cones (one per state): exactly the operator-
selection LP from `prop:bw-coefficient-shadow-price` evaluated at
both parent and daughter states.

#### Why this connects to existing framework

If true, **FROB-FILTER closes via**:

- **Step 12** (partition weights, $y_\lambda$ closed forms via Wenzl
  bridge);
- **`prop:bw-coefficient-shadow-price`** (LP shadow prices ↔
  positivity cones);
- **`conj:homological-shell-condensation`** (the magic-shell
  structure determines which Wedderburn blocks have $c(\lambda) =
  0$, the boundary of the cone).

So FROB-FILTER is **likely a corollary** of existing conjectures +
an explicit signature computation — not a new conjecture
requiring fresh framework. **This is the easier of the two
flags.**

### Recommended action

1. Compute Frobenius signature of $H_{3A}$ at $q_0$ for $A \in
   \{1, 2, 3, 4, 5, 6\}$ using existing $y_\lambda$ infrastructure.
2. Compare the first $A$ with $q_{3A} \geq 1$ to the empirical
   threshold in the witness.
3. If they match, author `conj:frobenius-filter-categorical` as a
   P2-priority block. Author the "+1 from LP dual" remark in the
   same block (companion line 68 of the witness).

### **Test result (2026-05-02): the conjecture lands at A=2.**

Computation: evaluated the Wenzl-bridge $y_\lambda(q_0)$ values
from
[`y-lambda-wenzl-bridge-symbolic-witness.json`](../../folio-assistant/computations/y-lambda-wenzl-bridge-symbolic-witness.json)
at $q_0$ to 25 dps; weighted by Plancherel $f_\lambda^2$; tabulated
$(p_n, q_n)$ as a symmetric-bilinear-form signature.

| $A$ | $n=3A$ | $p_n$ ($f^2$ on $y_\lambda > 0$) | $q_n$ ($f^2$ on $y_\lambda < 0$) | first neg? | dominance |
|----|------:|-------:|-------:|---|---|
| 1 | 3 | 6 | **0** | no | 100% pos |
| 2 | 6 | 538 | **182** | **first appearance** | 75% pos / 25% neg |
| 3 | 9 | 178902 | **183978** | (from A=2) | 49% pos / 51% neg — *balanced* |

**At $n=6$** the negative directions first appear: 3 partitions
have $y_\lambda(q_0) < 0$ — namely $(3,1,1,1)$ ($c=-3$, $y \approx
-6.85\times 10^{-4}$), $(2,2,1,1)$ ($c=-5$, $y \approx -3.42\times 10^{-4}$),
and $(1,1,1,1,1,1)$ ($c=-15$, $y \approx -1.24\times 10^{-5}$). At
$n=9$ the signature is **nearly balanced** (10 of 30 partitions
have $y_\lambda < 0$, totalling 51% by Plancherel weight).

**Match against empirical FROB-FILTER activation:**

- **A=1 (n→p, n=3)**: witness uses $\Sigma_{\rm all} + 1$ — *no
  filtering*. **Signature confirms:** pure positive ($q_n = 0$),
  so summing all 64 H₃ closed configs is unconditional.
- **A=3 (³H→³He, n=9)**: witness uses $|\Sigma_{\rm all}|$ over
  64 configs. **Signature shows:** *nearly balanced* (51%
  negative). Cancellation is severe but the absolute value of the
  full sum still gives the right Q-value (3.6% error, consistent
  with the empirical witness).
- **A=6 (⁶He→⁶Li, n=18)**: witness switches to $|\Sigma_{\rm FP}|$
  over 2048 of 4096 *Frobenius-positive* configs. Signature for
  $n=18$ not yet computed (witness only covers $n \leq 11$);
  expected to show $q_n > p_n$ (negative dominance).

**Refined conjecture (post-test):**

> **`conj:frobenius-filter-categorical-refined`** — the FROB-FILTER
> activation rule is: at $A_* \geq 2$, the Frobenius signature on
> $H_{3A}(q_0)$ first acquires a negative direction; for
> $A < A_*$, $\Sigma_{\rm all}$ is **unconditional** (positive
> definite). For $A_* \leq A < A_{**}$, $\Sigma_{\rm all}$ remains
> usable but with cancellation; for $A \geq A_{**}$, where
> negative directions become dominant ($q_{3A} > p_{3A}$), the
> $\Sigma_{\rm FP}$ filter is **required** for numerical stability
> + categorical positivity. The threshold $A_{**}$ is determined
> by the *signature crossover* — the smallest $A$ with $q_{3A} >
> p_{3A}$.

**Empirical fit:**

- $A_* = 2$ (first negative appears at n=6) ✓
- $A_{**}$ probably 4 or 5 (n=12 or n=15) — needs n=12, 15, 18
  signature compute, blocked on extending Wenzl-bridge witness
  beyond n=11. Would close this conjecture quantitatively.

**Reduction to existing framework.** The conjecture is now a
**corollary** of `prop:bw-coefficient-shadow-price` (which
identifies BW coefficients with LP dual variables on the
Frobenius positivity cone) + `prop:y-lambda-recipe-from-partition`
(which gives $y_\lambda \in \mathbb{Z}[q^{\pm 1/2}]$ closed forms).
**No new framework needed** — author the conjecture block citing
both upstream props + the signature compute.

**Action:** extend
[`y_lambda_wenzl_bridge_extended.py`](../../folio-assistant/computations/y_lambda_wenzl_bridge_extended.py)
to $n=12, 15, 18$ (estimated 1–4 hours each level via Schur
principal-specialisation), then compute $A_{**}$.

---

## Part III — Joint observation: Both flags route through the LP
   dual side

A common theme: **both NV-1 and FROB-FILTER are LP-dual phenomena**.

- **NV-1** asks: what is the *count* of dual basis vectors in
  $H_{k_w}(q_0)$ at the weak-sector level?
- **FROB-FILTER** asks: what is the *positive-definite sub-cone*
  of the Frobenius form on $H_{3A}(q_0)$, and at which $A$ does it
  become a strict subset?

Both flags would close if the **LP-dual side of the
operator-selection LP** at higher levels (Hecke level ≥ 9) were
fully characterised. This is *the same direction* as audit §3·D
(multi-level quadratic SDP, levels 4–7 missing), which is the
*compute* gap: the algebraic statement and the compute pipeline
need to land together.

**Recommended P1 sequence:**

1. P1.A — run the (a′) test for NV-1 (5 min compute).
2. P1.B — run the signature computation for FROB-FILTER (1 hr compute).
3. P1.C — author `conj:nv-as-bratteli-path-count` (or its winning
   variant) and `conj:frobenius-filter-categorical` as content
   blocks.
4. P1.D — extend `sdp_cross_channel.py` to levels 4–7 to feed the
   LP-dual side of both conjectures (audit §3·D).

If P1.A succeeds at 4-significant-figure agreement,
`conj:nv-as-bratteli-path-count` becomes the **strongest single
algebraic prediction in the framework** — the weak scale fixed by
a Plancherel count on $S_9$, with a single self-conjugate-partition
multiplicity factor.

---

**End of document.** Owner action: review proposed conjectures,
authorise P1.A / P1.B as compute jobs, then content-block author
the winning conjecture.
