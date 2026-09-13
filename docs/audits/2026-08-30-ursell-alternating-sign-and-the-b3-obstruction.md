# The 3-body sign obstruction is a missing $(-1)^{n-1}$

> **🛑 §3–§4 WITHDRAWN 2026-09-12 — the sign is not missing, it is Mayer's.**
> The partition function this document's §6 asked for exists (the hard-core
> lattice gas on the nucleon sites with the interface-letter traces as pair
> weights), and its Mayer expansion of `−ln(Ξ/Ξ_free)` carries `−φᵀ_n` at
> **every** order — so the corpus's uniform minus *is* the classical sign, and
> "restoring the alternation" is the same expansion at **negative activity**.
> `b₃ < 0` holds for every bond triple in `(0,1)`, with no `2/3` threshold. §1
> (the identity), §2 (the alternation) and §5a (`μ = e^{−B/α}`) stand. The
> `2.2511` / `2.7439` MeV of §4 are negative-activity coefficients, not
> postdictions. See
> [`2026-09-12-ursell-partition-function-for-b3.md`](2026-09-12-ursell-partition-function-for-b3.md)
> and `QOU.MassTheory.UrsellPartitionFunctionB3` (sorry-free). Left as a dated
> record.

**Date.** 2026-08-30
**Scope.** **(a)** — an identification, not a derivation. It does not refute
`MayerThreeBodySign` and does not close the magnitude.
**Producer.** [`computations/probes/ursell_alternation_sign_identity_probe.py`](../../computations/probes/ursell_alternation_sign_identity_probe.py)
→ `ursell-alternation-sign-identity.witness.json`, 6/6 assertions.
**Source.** `library/s10955-022-02992-6/` — Jansen & Kolesnikov, *Cluster
Expansions: Necessary and Sufficient Convergence Conditions*, J. Stat. Phys.
**189**:33 (2022), ingested by PR #6152.
**Bean.** `qou-rwhv`.

---

## 0. Correction — the first version of this document had the sign backwards

**What it asserted (2026-08-30, first commit):** that the paper's Eq. (3.1),
$\varphi^{T}_{n} = (-1)^{n}|\varphi^{T}_{n}|$, gives $\varphi^{T}_{3} \le 0$,
"the same conclusion `MayerThreeBodySign.lt_of_b3_pos` reaches"; that the two
results agree; and that the escape therefore requires an attractive component.

**What is true:** the classical law is $(-1)^{n-1}\varphi^{T}_{n} \ge 0$, so
**$\varphi^{T}_{3} \ge 0$** — the *opposite* sign, and the sign nature has. The
two results do **not** agree; they differ by exactly the factor at issue.

**How the exponent was settled.** Not by re-reading the scan. The OCR of Eq.
(3.1) in `library/s10955-022-02992-6/sections/` does read `(−1)n`, but that is
inconsistent with the paper's **own Corollary 3.3**, which gives sign $(-1)^k$
for $\psi_{n,n+k}$ together with $\psi_{1,1+k} = \varphi^{T}_{1+k}$ — i.e. sign
$(-1)^{m-1}$ for $\varphi^{T}_m$. The probe settles it by computing
$\varphi^{T}_n$ directly from the paper's definitions (p. 5: Mayer
$f = e^{-v}-1$, weight $w(G) = \prod_{\{i,j\}\in E(G)} f_{ij}$, $\varphi^{T}_n =
\sum_{G\in C_n} w(G)$) in exact rational arithmetic. At $n = 2$,
$\varphi^{T}_2 = f \le 0$, so the $(-1)^n$ reading fails immediately; measured,
it fails on **0 of 200** trials across $n = 2,3,4,5$ while $(-1)^{n-1}$ holds on
**200 of 200**. Treat the OCR'd exponent as a scanning artifact.

**What the error contaminated, and its state.** The PR #6152 body (rewritten),
bean `qou-rwhv` (rewritten), and §1–§5 of this document (rewritten below). It
reached no Lean file, no witness, and no content block. The lesson is the
ordinary one: **the excerpt I read was OCR of a superscript, and a superscript
is exactly what OCR loses.** A sign quoted from a scan is not measured until it
is recomputed from the definitions.

---

## 1. The identity

Under the Boltzmann identification $f^{\text{corpus}} = e^{-v}$, so that the
Mayer variable is $g = f^{\text{corpus}} - 1$, the corpus's connected 3-body
cumulant is **exactly minus** the third Ursell function:

$$
  b_3^{\text{corpus}}(f_{12},f_{13},f_{23}) \;=\; -\,\varphi^{T}_{3}(f_{12}-1,\;f_{13}-1,\;f_{23}-1)
$$

Measured in exact rational arithmetic (`fractions.Fraction`, no tolerance, no
float) on **400/400** random non-uniform triples in $(0,1)^3$. It holds trivially
at $n = 2$ as well: $W(2) = 1 - f = -(f-1) = -\varphi^{T}_2$.

**It is a low-order identity and does not extend.** At $n = 4$ the corpus's `b4`
matches **neither** $+\varphi^{T}_4$ nor $-\varphi^{T}_4$ — 200/200 mismatches
against each. So the correspondence covers $n \le 3$, which happens to be the
whole of the 3-body question, and nothing beyond it. Do not quote it as a
general theorem.

## 2. The alternation

In the purely repulsive class — $v \ge 0$, i.e. $g \in (-1,0)$, i.e.
$f^{\text{corpus}} \in (0,1)$, which is where **every** framework bond factor
lives — the Ursell functions **alternate**:

$$(-1)^{n-1}\,\varphi^{T}_{n} \;\ge\; 0 \qquad\Longrightarrow\qquad \varphi^{T}_2 \le 0,\quad \varphi^{T}_3 \ge 0,\quad \varphi^{T}_4 \le 0.$$

## 3. The consequence — the obstruction is a missing sign

The corpus carries a **uniform** minus at both orders: $b_n = -\varphi^{T}_n$
for $n = 2$ and $n = 3$.

* At $n = 2$ that is **correct**. Binding is positive, $\varphi^{T}_2$ is
  negative, so $b_2 = -\varphi^{T}_2 > 0$. ✓
* At $n = 3$ the Ursell function has **already flipped sign on its own**. The
  uniform minus therefore inverts the physical answer, and produces exactly the
  negative $b_3$ that `MayerThreeBodySign` proves is forced.

Restoring the alternation — $b_n = (-1)^{n-1}\varphi^{T}_n$, which reproduces
$b_2 = -\varphi^{T}_2 > 0$ **and** gives $b_3 = +\varphi^{T}_3 > 0$ — yields the
sign AME has, for **every** $f \in (0,1)$: no threshold, no $f_{pn} > 2/3$, no
attractive component.

**So `MayerThreeBodySign`'s $b_3 < 0$ is not a physical obstruction. It is a
missing $(-1)^{n-1}$.**

## 4. Magnitude, at the framework's own bond factors

Measured at the canonical proton pin, convention D, uniform bonds, scale pinned
at the deuteron ($\text{MeV}/W$-unit $= B_{\text{AME}}(D)/b_2$):

| typing | $f_{pn}$ | corpus $b_3$ ($W$) | $\varphi^{T}_3$ ($W$) | $b_3$ restored (MeV) | ÷ AME avg 1.4262 | ÷ AME triton 1.8081 |
|---|---|---|---|---|---|---|
| χ ($f_{pn} = z_D$) | 0.6126880371 | −0.3919307866 | +0.3919307866 | **2.2511** | 1.578 | **1.245** |
| probe-2 | 0.5082297894 | −0.6065851255 | +0.6065851255 | **2.7439** | 1.924 | 1.518 |

Right sign, and within **1.25×–1.92×** of the AME target with **zero free
parameters**. For calibration, the chirality-weighted-trace candidate family
recorded in bean `qou-9v7t` sits **6–14× short** on the same quantity.

**This is a postdiction of a magnitude, not a derivation of one**, and the
over-shoot is real: 25 % against the triton anchor at the χ typing, 58 % against
the isospin average. Which of those two is the right target is itself open — see
`QOU.Mass.PairwiseCumulantVanishing`'s docstring and bean `qou-9v7t`, where the
Coulomb asymmetry of the A = 3 doublet is flagged as unresolved.

## 5. What is **not** established

* **`MayerThreeBodySign` is not refuted.** Every statement in it remains true of
  the object it is about — `b3_le_of_nonneg`, `lt_of_b3_pos` and
  `b3_neg_of_le` are correct. What is established is that **that object differs
  from the classical one by a sign the classical theory does not carry.** The
  same goes for `QOU.Mass.PairwiseCumulantVanishing`, whose pairwise-additive
  vanishing is unaffected.
* ~~**The Boltzmann identification is an interpretation.**~~ **Retracted the
  same day — it is derived, and by the corpus.** See §5a.
* **Nothing here supplies the extensive term.** The four sorry-free prunes
  bounding the $\ge 3$-body scaling (`CoordinationSaturation`,
  `ChainBondOrderDependence`, `BodyOrderRecurrenceDepth`, `MayerThreeBodySign`)
  are untouched as *scaling* results; only the last one's *sign* reading changes.

## 5a. $f = e^{-v}$ is derived — it is §10a read backwards

An earlier version of §5 called the Boltzmann identification "an interpretation".
That was wrong, and the derivation was already in the corpus.
[`2026-08-08-binding-functional-attack-vectors-and-li2q-guard.md` §10a](2026-08-08-binding-functional-attack-vectors-and-li2q-guard.md)
establishes, from two facts:

1. **the trace is multiplicative over bonds** —
   $\mathrm{tr}_{\text{atom}} = \mathrm{tr}_{\text{free}}\cdot\prod_{\text{bonds}}\mu_k$,
   verified there to $1.2\times10^{-31}$;
2. **energy is extensive**,

that the map from trace to energy satisfies the Cauchy equation and is therefore
$B = -\alpha\ln\mu$ — *"the log form is forced"*. **Inverting:
$\mu = e^{-B/\alpha}$.** The corpus's bond factor *is* the Boltzmann factor of
the corpus's own derived bond energy, with $v := B/\alpha$.

It is also literally the same object: §10b's
$\mu_{pn} = z - h(\tfrac12 - \delta/4)$ is character-for-character the $f_{pn}$
of `MayerThreeBodySign`'s probe-2 typing.

Measured in the probe, both conventions: $\mu \in (0,1)$, $v = B/\alpha > 0$,
and $e^{-v} = \mu$ to $10^{-40}$.

| | $\mu_{pn}$ | $B(^2\mathrm{H}) = -\alpha\ln\mu$ | ÷ AME 2.224566 |
|---|---|---|---|
| **D** (canonical) | 0.5082297894 | **2.8332 MeV** | **1.274** |
| C (what §10a itself used) | 0.3948620864 | 3.8897 MeV | 1.749 |

The C row reproduces §10a's own recorded "+74.9 %", which is the cross-check
that this is the same computation. **The D row is new**: §10a predates the
2026-08-15 convention-D ruling, so its ²H over-binding is **+27.4 %, not
+74.9 %** — the migration more than halves it. Tracked as its own item; the
*derivation* is convention-independent (it needs only multiplicativity), the
*numbers* are not.

> **Naming caveat, so nobody reads physics out of a convention.** In the Mayer
> convention $v > 0$ is called "repulsive", and here $v = B/\alpha$ is the
> **binding** energy, which is positive. The alternation theorem holds on
> $f \in (0,1)$, which is where the corpus sits. Calling the corresponding
> $v = -\ln\mu > 0$ "repulsive" is bookkeeping and asserts **nothing** about the
> nuclear force.

**What remains open is narrower than §5 claimed: the normalisation.** §10a gives
$B = -\alpha\ln(\text{trace})$ and the standard cluster expansion gives
$\ln\Xi = \sum_n (z^n/n!)\int\varphi^{T}_n$, so the connected $n$-body part of
$B$ should be $\alpha$ times the $n$-th Ursell term *up to a combinatorial
factor this work does not derive*. The **sign is settled**; the magnitude in §4
is reported under a deuteron-pinned scale, and the $\alpha$-scaled alternative
differs by ~10 %. Pinning that factor is the remaining work.

## 6. What would settle the normalisation

Exhibit the polymer / cluster model whose activity expansion has the corpus's
$b_3$ as its third Ursell coefficient — name the polymer set, the weight, and
the compatibility relation. With that, $f = e^{-v}$ is either derived or
provably unavailable. `rebenko2022virial` is the relevant setting note: it works
the **canonical** (fixed particle number) ensemble, which is what matches a
nucleus, where the grand-canonical activity expansion does not.

## 7. The other four sources in the drop

| ref | role |
|---|---|
| `procacci2016mayer` | Penrose's tree-graph identity with a minimum-spanning-tree partition scheme; improved convergence **radii** for Mayer and Virial series under a stable, tempered potential. A radius result — no cumulant sign. |
| `rebenko2022virial` | graph expansions of correlation functions in the **canonical** ensemble via Kirkwood–Salsburg. See §6. |
| `dousse2016ising` | weighted dependency graphs for the Ising model, **cumulants** as the working object, CLTs for pattern counts. A bounding technique. |
| `mann2021partition` | the **quantum** member of the drop — approximation algorithms for quantum partition functions on abstract-polymer / cluster-expansion machinery. |

`library/ising/` is a later revision of `dousse2016ising`, recorded in
[`library-duplicate-ledger.json`](library-duplicate-ledger.json); two grep hits
across the two directories are **one** source.
