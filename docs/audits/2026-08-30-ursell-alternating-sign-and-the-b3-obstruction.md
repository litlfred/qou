# The Ursell alternating-sign property, and what it says about the b₃ obstruction

**Date.** 2026-08-30
**Scope.** **(a)** — a literature identification and a question it raises. No
derivation, no refutation, no magnitude. Nothing here is wired to production.
**Sources.** The six-PDF cluster-expansion drop of commit `a12f83c4cd`, ingested
into `library/` by PR #6152.

---

## 1. The finding

`library/s10955-022-02992-6/` — Jansen & Kolesnikov, *Cluster Expansions:
Necessary and Sufficient Convergence Conditions*, J. Stat. Phys. **189**:33
(2022) — carries, in §3.1 *"Forest Partition Schemes: Alternating Sign
Property"*, the classical **alternating-sign property of the Ursell functions**:

$$
  \varphi^{T}_{n}(x_1,\dots,x_n) \;=\; (-1)^{n}\,\bigl|\varphi^{T}_{n}(x_1,\dots,x_n)\bigr|
$$

valid for a **non-negative pair potential** — i.e. purely repulsive
interactions. The paper cites it as its own ref `[8, Eq. (2.8)]` and proves the
multi-rooted generalisation
$(-1)^{k}\psi_{n,n+k}(x_1,\dots,x_{n+k}) \ge 0$ twice over: once from a
forest-graph equality (Corollary 3.3), and once, in Remark 3.1, by reduction to
the classical $n=1$ statement through Lemma 3.4.

**At $n = 3$ this reads $\varphi^{T}_{3} \le 0$.**

## 2. The corpus reaches the same conclusion by a different route

`QOU.MassTheory.MayerThreeBodySign` (sorry-free, generic `CommRing`) proves, for
the multiplicative assembly $W(K) = 1 - \prod_{i<j} f_{ij}$ and the Ursell
inversion $b_2 = W(2)$, $b_3 = W(3) - 3b_2$:

* `b3_eq` — $b_3 = 3f_{pn} - 2 - P_3$;
* `b3_le_of_nonneg` — from $P_3 \ge 0$, $b_3 \le 3f_{pn} - 2$;
* `lt_of_b3_pos` — therefore $b_3 > 0 \implies f_{pn} > 2/3$.

The framework's own $f_{pn} = z_D = 0.6126880\ldots < 2/3$, so $b_3 < 0$ is
forced, **for every edge set** (the edge set enters only through $P_3 \ge 0$).

Two results, two arguments, one conclusion: the connected three-body cumulant is
non-positive, and the edge set is not what is doing it.

## 3. What is NOT established — the shape check

The two statements are **not** the same theorem, and this document does not
claim they are. Per AGENTS.md §"Grep the claim SHAPE, not only the topic",
the differences are exactly where a false identification would live:

| | classical $\varphi^{T}_{3}$ | corpus `b3` |
|---|---|---|
| **the object** | the third Ursell function of a grand-canonical **activity expansion** of a genuine pair potential | an inclusion–exclusion cumulant of a **binding functional**, $b_3 = \bar B(3) - 3b_2$ |
| **the hypothesis** | $U \ge 0$ pointwise, on the **potential** | $P_3 \ge 0$, on a **product of bond factors** |
| **the setting** | infinite-volume statistical mechanics with a convergent expansion | a finite 4-point combinatorial identity over a generic `CommRing` |
| **what proves it** | forest-graph equality / Lemma 3.4 | a one-line bound on $3f_{pn} - 2 - P_3$ |

Nothing above licenses reading `MayerThreeBodySign` as an *instance* of the
classical theorem. What it licenses is the question:

> **Is the corpus's $b_3$ an Ursell function in the theorem's sense?**

and both answers are informative:

* **If yes** — the obstruction is far broader than the $1 - \prod f$ assembly.
  No change of assembly escapes it, `QOU.Mass.PairwiseCumulantVanishing` and
  `MayerThreeBodySign` become two shadows of one classical fact, and the only
  remaining escape is the **hypothesis**.
* **If no** — then `MayerThreeBodySign`'s vocabulary ("Mayer", "Ursell") is
  doing more work than its content, and the naming should be scoped to say so.

## 4. Why the hypothesis is the interesting half either way

The classical theorem's escape route is documented and named: **the potential
must fail to be non-negative**, i.e. carry an attractive component. And that is
not a gap in the literature — it is the subject of the very paper that records
the sign property. Jansen–Kolesnikov's own abstract:

> "We prove a new convergence condition for the activity expansion of
> correlation functions in equilibrium statistical mechanics with **possibly
> negative pair potentials**. For non-negative pair potentials, the criterion is
> an if and only if condition."

So the sign obstruction and the convergence theory for the class that escapes it
are in the same 47 pages, and the corpus now holds them.

**Where the framework sits.** The per-bond factors are $f_{pp} = z$,
$f_{nn} = z - h$, $f_{pn} = z - h(1/2 - \delta/4)$ (bean `qou-9v7t`). At the
canonical proton pin $z_D = 0.6126880\ldots$, and the two typed factors subtract
from it, so **all three lie strictly in $(0,1)$**.

> **⚠ The next step is an interpretation, and it is flagged as one rather than
> asserted.** Under a Boltzmann reading $f = e^{-\beta U}$, $f < 1
> \Leftrightarrow U > 0$, so every bond in the framework would be repulsive and
> an attractive channel would show up as a bond factor **greater than 1** —
> of which there is none. But the corpus's $f$ are Markov/bond factors built
> from $z$, **not** exponentiated potentials, and no step in the corpus
> identifies them with a Boltzmann factor. Establishing or refuting that
> identification is the concrete next measurement, and until it is done this
> paragraph is a suggestion about where to look, not a result.

## 5. What would settle §3

Exhibit the polymer / cluster model whose activity expansion has the corpus's
$b_3$ as its third Ursell coefficient — i.e. name the polymer set, the weight,
and the compatibility relation. With that in hand the classical theorem either
applies (and the obstruction is structural, §3 first branch) or provably does
not (second branch). Absent it, the agreement in §2 is a coincidence of
conclusions and should be reported as one.

## 6. The other four sources in the drop, and what each is for

| ref | role |
|---|---|
| `procacci2016mayer` | Penrose's tree-graph identity with a minimum-spanning-tree partition scheme; improved convergence **radii** for Mayer and Virial series under a stable, tempered potential. A radius result — it says nothing about any cumulant's sign. |
| `rebenko2022virial` | graph expansions of correlation functions in the **canonical** ensemble via Kirkwood–Salsburg. The canonical (fixed particle number) setting is the one that matches a nucleus; the grand-canonical activity expansion does not. Relevant to §5. |
| `dousse2016ising` | weighted dependency graphs for the Ising model, with **cumulants** as the working object and CLTs for pattern counts. The bounding technique, not a sign result. |
| `mann2021partition` | the **quantum** member of the drop — approximation algorithms for quantum partition functions on abstract-polymer / cluster-expansion machinery. Cite for the polymer-model formulation. |

`library/ising/` is a later revision of `dousse2016ising` and is recorded in
`docs/audits/library-duplicate-ledger.json`; two grep hits across the two
directories are **one** source.

## 7. What this does not do

It does not supply the extensive term, it does not close the ⁴He magnitude, and
it does not refute anything. The magnitude gap recorded in bean `qou-9v7t`
(6–14× on `b3_sym`, depending on variant) is untouched. This is a relocation of
the *sign* question from the assembly to the positivity hypothesis, plus the
observation that the corpus now holds the convergence theory for the class on
the other side of that hypothesis.
