---
# qou-bn8e
title: 'GAP: intra-nucleon EM self-energy E_EM is not derived — the pion sets the length scale but not the magnitude'
status: in-progress
type: task
priority: normal
created_at: 2026-08-25T10:36:54Z
updated_at: 2026-08-29T16:26:15Z
---

**Where this stands (2026-08-25, PR #5744, branch `claude/standard-panel-qou-derivation-ixuolx`).**

The owner asked to derive the intra-nucleon EM contribution using the corpus's
meson/pion material. **What came out is a length scale, not an energy.** Stating
the negative plainly rather than dressing the partial result as a closure.

**What IS established.**

The empirical rescale factor `1.178176504688906` sitting in
`computations/mirror_nuclei_coulomb_systematics.py` traces to $r_0 = 1.2$ fm,
and $r_0$ is the reduced pion Compton wavelength
$\bar\lambda_\pi = \hbar c / m_\pi$. So **the pion sets the nuclear Coulomb
length scale**, and the factor is not a free fit. Substituting
$\bar\lambda_\pi$ for the empirical $r_0$ moves the chain mean
$0.838 \to 0.987$ with **no empirical length left in the expression** — the
strongest form of the result, since it removes an input rather than tuning one.

**What is NOT established — the gap.**

$E_{\mathrm{EM}}$ itself. A length scale fixes the $1/r$ in a Coulomb energy;
it does not fix the charge distribution, the exchange term, or the overall
normalisation. Nothing here derives the magnitude of the intra-nucleon
self-energy, and no probe in this branch claims to.

**Do not conflate this with the inter-nucleon front.** They are different
objects, and a retraction on this branch was caused by exactly that conflation
(`docs/audits/2026-08-25-4b-corrections-duplication-and-two-fronts.md`). The
binding-energy derivation `(A1)` shows the *self*-terms cancel in the binding
energy, so 4-B's EM-linking invariant does **not** gate this, and this does not
gate 4-B.

**Next honest step.** Either (i) derive the charge distribution from the
Borromean/color-tube geometry already in the corpus and integrate, or (ii) find
the categorical object whose archimedean evaluation *is* the self-energy. Route
(ii) is the framework-native one. Do not fit a normalisation to the mirror-pair
residuals — that reproduces the anti-fit failure mode the corpus is full of.



---

**Progress 2026-08-25 — the localisation argument is now proved, and measured.
The magnitude gap survives, unchanged.**

Applying the discipline that worked on `qou-s4h6`: ask what the structure permits
before hunting a formula. The corpus already argues that an EM-sector quantity is
*where* a splitting must live —
[`rem:isospin-mass-split-em-localisation`](content/quantum-observable-universe/mass-theory/isospin-mass-split-em-localisation.md)
concludes the mirror-isobar split *"must therefore be entirely sourced by the
Coulomb term"* because *"the trace tower, co-Casimir, chirality, and
shell-correction functionals all respect these structural involutions."* It is a
`remark` with no Lean.

New file `QOU/MassTheory/InvolutionSelectionRule.lean`, sorry-free, axiom-clean
(two of three depend on `propext` alone), §7c-generic:

- `split_invariantSector_eq_zero` — an $\iota$-invariant sector contributes
  **zero** to the $\iota$-split. The valid core.
- `split_sum_eq_split_remainder` — a sum over a **`List`** of invariant sectors
  plus a remainder splits exactly like the remainder. The enumeration is a
  `List` *in the type* deliberately, so the arity cannot be lost between the
  proposition and the prose.
- `omitted_sector_breaks_localisation` — **the enumeration is load-bearing.**
  Omit one non-invariant sector and the conclusion is false: the argument reports
  "the split is entirely $G$'s, hence zero" while the true split is 2.

**Measured, and this is the part worth keeping.** Of the four sectors the remark
names, **one** has a proved sign-flip invariance in this corpus
(`prop:crystal-isospin-degeneracy`, itself conditional on
`CrystalEigenlineSignBlind`). No theorem asserts it for the trace tower, the
co-Casimir, or chirality. The nearest chirality result,
`QOU.Resurgence.chiral_sign_cancels`, **does not help and should not be cited
here**: it concerns a *different* involution (diagram conjugation, not the
generator sign-flip) and states **anti**-invariance,
$\mathrm{sign}(\bar\mu) = -\mathrm{sign}(\mu)$. An anti-invariant sector is the
one that *survives* a split, not one that drops out.

So the remark's *"all respect these structural involutions"* is one proved case
generalised to four, across at least two distinct involutions — the
`da-arity-conflation` shape. Scope-**(a)**: the localisation is very plausibly
true and is **not** refuted; as supported, it does not follow. The fix is to
prove the two missing invariances, not to weaken the remark.

**The bean's own gap is untouched.** A selection rule says *where* a quantity may
live, never how big it is. $E_{\mathrm{EM}}$ is still not derived, here or
anywhere in this corpus.



---

**2026-08-25, second pass — the Coulomb localisation is wrong twice, and this
TIGHTENS the bean rather than closing it.**

Chasing the localisation claim in `rem:isospin-mass-split-em-localisation`
turned up two independent defects. The second is the larger and was **not mine**.

**1. The trace-tower premise is false at the substrate.** New file
`QOU/MassTheory/TraceSignFlipRegime.lean` (sorry-free, axiom-clean). The Hecke
relation forces $\sigma^{-1} = \sigma - (q - q^{-1})$, so a generator flip moves
any linear functional by exactly $(q - q^{-1})\,\mathrm{tr}(1)$, vanishing iff
$q^2 = 1$ — by `double_braiding_eq_one_iff`, exactly the symmetric-braiding
locus. **The trace tower is sign-flip blind precisely where the braiding is
symmetric, and QOU sits off it.** At $q_0$ the flip moves the trace by
$0.209\,\mathrm{tr}(1)$ (mpmath: 0.20906 against the repo's own $q_0$).

No contradiction with `prop:crystal-isospin-degeneracy`, a $q \to 0$ statement
that stays true there. The defect is a **regime conflation** — a crystal-limit
invariance licensing a claim about the functional at $q_0$.

**2. The Coulomb term has the wrong sign — found in the block's own `.qa.json`.**
A `trap-superlative` finding by whichever agent swept the block already carried
this, and I would have missed it. Verified independently in exact mpmath rather
than taken on trust:

    m(3H) - m(3He) = (m_n - m_p) - (B(3H) - B(3He))
                   =    +1.2933   -    +0.7638      = +0.5296 MeV

The Coulomb-driven binding difference enters with the **opposite sign** at 1.44x
the split's magnitude; the free-nucleon difference at 2.44x. **Acting alone the
Coulomb term gives the wrong sign.** That agent's finding and proposed fix were
both correct. The answer was in the sidecar — a place the corpus-grep checklist
does not name and I had not thought to look.

**Why this tightens rather than closes this bean.** The surviving constraint is
that the split lives outside the involution-invariant sector. That complement
holds **both** the nuclear Coulomb term **and** $m_n - m_p$, and the second
dominates. The intra-nucleon EM self-energy is carried in the **free-nucleon
masses**, not in the binding difference (which is what
`mirror_split_s3_em_functional_probe.py` §(A1) says, and what made C2 a genuine
correction). So the mirror split is **not a route around $E_{\mathrm{EM}}$ — it
requires it.** The bean's target is now load-bearing for a second observable
rather than isolated.

Block re-scoped per AGENTS.md §"Before declaring refuted": the observation
stands, only the localisation onto Coulomb goes.

**Still open, unchanged:** $E_{\mathrm{EM}}$ itself. No magnitude here.



---

**2026-08-25, third pass — co-Casimir settled, and the enumeration is short a
term.**

**The co-Casimir sector is invariant, by arity.** By
`thm:frobenius-codim-universal`, $\tau(C_{\dim_q}) = \sum_\lambda 1/\dim_q(\lambda)$
— a sum over the Wedderburn blocks of $H_n(R,q)$, a function of $(n,q)$ alone
that takes **no braid word as an argument at all**. A generator sign flip cannot
move it. Both mirror isobars are $A = 3$, hence the same $n$, so it cancels
between them exactly.

Proved through a new general lemma rather than as a one-off:
`split_comp_eq_zero` (a sector factoring through an involution-invariant of the
state contributes zero) plus `factoringSector` to package it for the `List`.
That is the useful form — a sector is usually invariant **by arity**, because it
never sees what the involution moves, rather than by computation. Both depend on
`propext` alone.

**The enumeration omits a term of the mass formula.**
`thm:knot-mass-formula-unified` carries **three** terms — descended trace, brane
tower, Frobenius co-Casimir. The remark names four sectors (trace tower,
co-Casimir, chirality, shell correction), overlapping those only partly: the
**brane tower** is a term of the formula and is **absent from the list**, with no
invariance result. That is exactly the case
`omitted_sector_breaks_localisation` proves fatal — now found in the corpus
rather than constructed as a counterexample.

**Not over-claiming:** I have not shown the brane tower is non-invariant. Its
status is "no result", like chirality. What changed is that it is now known to
be *missing from a list that has to be exhaustive*.

**Sector audit, complete as far as it goes:**

| sector | sign-flip status |
|---|---|
| Frobenius co-Casimir | **invariant** (arity) |
| descended trace | **not invariant** at the substrate |
| brane tower | in the formula, absent from the list, **no result** |
| shell correction | invariant at $q \to 0$ **only** |
| chirality | **no result** |

**Still open, unchanged:** $E_{\mathrm{EM}}$ itself. Three passes on this bean
have sharpened *where* it must live and *why* it is needed; none has produced a
magnitude.



---

**RETRACTION, same session — the brane tower DOES have an invariance result.**

The pass above said the brane tower is *"a term of the formula, absent from the
list, with no invariance result"*. The second half is **wrong**. `main` carries
`QOU/Mass/BraneTowerIsospinBlind.lean`:

- `braneTowerR_eq_binom_sum` — the trace-invariant tower collapses to
  $\sum_k \binom{n-1}{k} z^k f_k$; its own docstring says *"There is **no**
  braid-word input"*. That is the **same arity argument** I had just made for
  the co-Casimir, one file over, and I did not run the same grep.
- `braneTowerW_isospin_blind` — the general form, invariant once the per-subset
  weight is Markov-invariant.

**Fourth duplication-class error today** (Milnor port, `qb`, `sub_inv_ne_zero`,
now this), and the cause was identical every time: declaring a corpus item absent
without grepping the object. I ran the object-grep on `co.casimir` in the very
same pass and did not run it on `brane tower`.

**What survives:** the brane tower is a term of the unified formula and is absent
from the remark's four-sector list. But the omission is **benign** — the omitted
term is invariant — so the enumeration gap does **not** break the localisation.
Materially different from what I published.

**Corrected sector audit:**

| sector | sign-flip status |
|---|---|
| Frobenius co-Casimir | **invariant** (arity) |
| brane tower | **invariant** (arity; general form conditional on Markov-invariance) |
| descended trace | **not invariant** at the substrate |
| shell correction | invariant at $q \to 0$ **only** |
| chirality | **no result** |

**Two independent routes now agree.** The cited synthesis
(`docs/audits/2026-06-26-t2t3-trace-invariance-status-synthesis.md`) concludes
the split is carried by T₁ and T₅ (chirality), *"not by the brane tower"*. My
`TraceSignFlipRegime` result proves T₁ is not sign-flip invariant at the
substrate — the same two-sector answer, reached from the Hecke relation rather
than from the tower's combinatorics.

The localisation onto Coulomb still fails, for the two reasons already recorded
(descended trace non-invariant at $q_0$; Coulomb term has the wrong sign), not
for a third about enumeration.



---

**2026-08-25, fourth pass — chirality settled from `main`; sector audit COMPLETE.**

Grepping `chirality` the way I should have grepped `brane tower` answered it
immediately, twice over, from work already on `main`. **Fifth object-grep
failure this session**, and this time on the sector I had *just named* as next.

**Chirality breaks both involutions the remark names:**

- **Hopf antipode** — `chirality_is_unique_S_odd`
  (`frobenius-s-classification.lean`): the chirality term is the **unique
  S-odd** term of the three. It is the one term that *anti*-commutes with the
  antipode.
- **Hecke-skein sign flip** — `prop:chirality-dual-space-derivation` defines the
  factor as $\prod_c (1 + \mathrm{sign}(c)\,h)$ over a `List CrossingSign`. It
  reads the crossing signs directly; a flip maps $(1+h) \leftrightarrow (1-h)$.

**But chirality does not source THIS split.** ${}^3\mathrm{H}$ and
${}^3\mathrm{He}$ carry the same crossing multiset (one positive, one negative),
so both get $1 - h^2$. **Not over-claiming that as "chirality cancels"** — the
factor multiplies a descended trace that *differs* between the isobars, so
whether the product cancels is a separate question I have not analysed.

**Credit: the corpus had my τ_sym result first.** The same block carries
$\tau_{\mathrm{sym}}(\sigma) - \tau_{\mathrm{sym}}(\sigma^{-1}) = h$,
$h = q - q^{-1}$ — my `trace_inv_sub_trace` specialised to the 1-dim symmetric
rep. `TraceSignFlipRegime`'s docstring now says so up front. What it genuinely
adds is **when the deviation vanishes**: any linear functional on any algebra
rather than $\tau_{\mathrm{sym}}$ over $\mathbb{R}$; the **iff**; and the tie to
`double_braiding_eq_one_iff` making *"trace is sign-flip blind"* and *"braiding
is symmetric"* the same condition.

**COMPLETE SECTOR AUDIT — two of four named sectors fail, not one:**

| sector | status |
|---|---|
| Frobenius co-Casimir | invariant (arity) |
| brane tower | invariant (arity; general form conditional) |
| **descended trace** | **NOT invariant at the substrate** |
| **chirality** | **breaks BOTH involutions** |
| shell correction | invariant at $q \to 0$ only |

**Meta-finding, and the one I would keep.** Five object-grep failures in one
session, every one the same shape: declaring a corpus item absent after grepping
the *topic* and not the *object*. The corpus-grep checklist names five paths;
what it does not say loudly enough is that the unit of search is the **named
declaration**, not the subject matter. Four of the five would have been caught by
a single `grep -rn '^\(theorem\|lemma\|def\) .*<Object>' content/`.

**Still open, unchanged across four passes:** $E_{\mathrm{EM}}$'s magnitude. Every
pass has sharpened *where* it lives and *why* it is needed; none has produced a
number.



---

**2026-08-29 — arc work-plan review after 1524 commits landed on `main`.**

**Nothing on `main` touched this arc's eight Lean files.** Verified per file
against the merge base: zero commits. No conflicts, no supersession.

**But one landing reframes the arc's priority order, and it is not this bean.**
`qou-tnho` settled 2026-08-29: *"the hypercharge programme IS blocked upstream
on N=3"*. Read from `eightfold-open-problems.md`'s own conditionality ledger —
`N = 3` gates **every** flavour statement, the obstruction is proved and the
**construction is missing**.

That lands squarely on **front 4 (GMO)**, which is entirely
$(I, Y)$-ansatz work: `gmo_second_order`, `gmo_blind_to_Yd`, the two
absorption lemmas, both surjectivity theorems. $Y$ is a flavour quantum number
on the $A_2$ weight lattice. So **the whole GMO front is a refinement of a
blocked branch** — the theorems stay true and sorry-free, and none of them is
reachable as physics until $N = 3$ exists.

It does not weaken front 4's verdict; it deepens it. I closed `qou-s4h6`
concluding *"the only route left is deriving $e, f, g$ categorically"*.
`qou-tnho` says the **stage those coefficients live on** is itself gated. Two
independent arguments, same direction.

**Consequence for the arc's order, which inverts what I had.** I ended the last
pass saying front 4-A was answered and front 4 was the live one. Backwards:

| front | status after the review |
|---|---|
| **4-A — N=3 / non-symmetric reconstruction** | **the gate.** Proved the band argument is circular (symmetric-category machinery, non-symmetric braiding). The missing $N=3$ *construction* is what unblocks the flavour sector |
| 4 — GMO | **blocked behind 4-A.** Pruned as far as it goes; second-order GMO is vacuous, and the stage is gated |
| 4-B — EM linking | partially blocked: $\mathfrak{m}_n - \mathfrak{m}_p$ is not flavour-gated, so **this bean stays live** |
| this bean — $E_{\mathrm{EM}}$ | **live, and the only front not gated on $N=3$** |

So this bean is now the arc's *least* blocked item, not its weakest. That is a
change of judgement on my part, and the reason is external: the flavour side
acquired a proved upstream gate while $E_{\mathrm{EM}}$ did not.

**Also opened from this review:** `qou-54tg` — a Lean/narrative divergence in
`q-game-of-life`, whose `_reversible` theorem assumes an involutivity its own
proof denies at generator level. In this arc's lane because
`double_braiding_eq_one_iff` is the σ-level fact the two sides disagree about.
