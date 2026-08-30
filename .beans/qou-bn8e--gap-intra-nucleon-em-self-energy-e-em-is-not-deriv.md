---
# qou-bn8e
title: 'GAP: intra-nucleon EM self-energy E_EM is not derived — the pion sets the length scale but not the magnitude'
status: in-progress
type: task
priority: normal
created_at: 2026-08-25T10:36:54Z
updated_at: 2026-08-30T09:34:26Z
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



---

**2026-08-29 — the bean's target NARROWS to one scalar, and the corpus already
had half of what I was about to write.**

**Corpus-grepped FIRST this time, and it paid.** Before attempting the
charge-structure route I ran the object-grep, and
`QOU/MassTheory/NeutronProtonEMSign.lean` on `main` already derives exactly it,
parameter-free and sorry-free:

    Sum_{i<j} q_i q_j  =  0     proton (uud)      chargeStructure_uud
                       = -1/3   neutron (udd)     chargeStructure_udd
    gap                = +1/3                     em_gap_eq
    correction sign    negative                   em_correction_neg

Sixth object-grep hit this session — the first where running the grep **first**
saved the work rather than the failure being found afterwards.

**So the gap is one positive scalar.** Its own docstring says so: *"does not
derive the EM coupling from the 13 categorical drivers"*. Combining with this
branch's two shape constraints, the state is:

| piece | status |
|---|---|
| charge structure, the $0$ vs $-1/3$ | **derived** (corpus, parameter-free) |
| sign of the correction | **derived** (corpus) |
| $E_{\mathrm{EM}}$ even in $\bar\mu_{123}$ | **derived** (this branch) |
| pairwise linking cannot see the carrier | **derived** (this branch) |
| the coupling $k > 0$ | **NOT derived — this is the whole remaining gap** |

**A falsifiable target for $k$**
(`computations/probes/em_selfenergy_coupling_target_probe.py`, mpmath 50 dps,
no witness). Inverting the **external** lattice decomposition
($m_n - m_p$ QED part $= -1.00 \pm 0.16$ MeV, BMW 2015):

    k = 3.0 MeV   [2.52, 3.48]
    r = 0.480 fm  [0.414, 0.571]   if k = alpha_EM * hbar c / r

**This is a TARGET, not a derivation** — inverting a measurement to obtain a
parameter is a fit, and the probe says so in its own docstring. It is recorded
because a target with a number can be *checked*.

**And it prunes a move I was about to make.** Front 4-B established that the
*nuclear* Coulomb length is $\bar\lambda_\pi$; the tempting step was to reuse
it here. Measured, it is **off by 2.9×** ($-0.339$ vs $-1.00$ MeV). The proton
charge radius is off by 1.75×. **Neither** framework length reproduces the
target, so a future derivation of $k$ is falsifiable against a factor stated in
advance.

**Also found: `NeutronProtonEMSign` has ZERO consumers** outside its own file
(only generated `.c` IR). The corpus prune is orphaned, and this branch's
$E_{\mathrm{EM}}$ work never cited it. Both are about the same object.

**Still open, and now sharply:** derive $k$ from the categorical side. Not a
length chosen to match — that is the fit this probe exists to make visible.



---

**2026-08-29, attempt at deriving $k$ — NOT DERIVED. The target moved twice,
both times because of an error of mine.**

Reporting the negative plainly: **I did not derive $k$.** What changed is what a
derivation must produce, and both changes were corrections.

**Error 1 — wrong decomposition, off by 121×.** My previous pass inverted the
**lattice** split of $m_n - m_p$ into QCD ($+2.29$) and QED ($-1.00$ MeV) and
reported $k = 3.0$ MeV. **The framework does not build $\Delta m$ that way.**
Its leading traced-volume term $\Delta m = \alpha|\Delta\Phi|$ predicts the
**net** splitting and over-predicts by $+0.638\%$
(`docs/audits/2026-07-11-np-splitting-residual-not-q0-knob.md`: $1.301589$ vs
$1.293334$). The EM term owes that residual — **$0.008255$ MeV**, not
$-1.00$ MeV. Importing an external decomposition the framework does not use put
my target off by two orders of magnitude.

**Error 2 — Euclidean import.** I wrote $k = \alpha_{\mathrm{EM}}\hbar c / r$
and solved for a length ($r \approx 0.480$ fm), presupposing a $1/r$ Coulomb
law. The framework's own EM corrections do not have that shape:
`prop:meson-em-sinh-closed-form` writes its correction as
$(\alpha_{\mathrm{em}}/\pi)\times$ a dimensionless function of $\hbar_q$.
Solving for a length is **the same "unexamined Euclidean import" that
`qou-17mq` flagged for the $\kappa(A)$ separation law** on the neighbouring
front — I committed next door the defect main had just documented.

**Corrected target, in the framework's native shape:**

    dE = -m_p * (alpha_em/pi) * f(hbar_q) * gap        gap = 1/3, derived

    k_required = 0.024765 MeV
    f_required = 0.011363

**One observation, and it is only that.** $f_{\mathrm{req}}$ is
$O(\hbar_q^2)$ — $\hbar_q^2 = 0.0098172$, ratio $1.157$ — and
$1/\hbar_q^2$ is structural in the mass formula. **Right order is not right
value.** Choosing a function to close that 16 % is the fit this whole line is
avoiding, and I have not done it. The meson block's own
$f = 1 + \log(1+\hbar_q)$ is off by $96\times$ and is not reusable — it
corrects a mass-**squared ratio**, a different object.

**Why I stopped rather than continued.** Every remaining move I could see was
choosing an $\hbar_q$-function to hit $0.011363$. That is numerology, and the
corpus is explicit about it. A derivation has to come from the categorical side
— what the EM sector *is* for a three-strand Borromean carrier — not from
matching a number.

**State of the bean, unchanged in kind but sharper:** charge structure, sign,
evenness in $\bar\mu_{123}$, pairwise-blindness all derived; $f$ (hence $k$)
not. The target it must hit is now the framework's own residual rather than an
imported one.



---

**2026-08-29, third attempt — $k$ still NOT derived, but the EM sector yields
its first parameter-free consequence, and this bean's framing was wrong.**

I stopped the last attempt at *"every remaining move is picking an
$\hbar_q$-function to hit 0.011363"*. Attacking the **structure** instead of
the number produced three findings.

**1. "One scalar remains" — my own framing — is wrong. Two remain.** The
symmetric quadratics in three charges span a **2**-dimensional space: the *self*
term $\sum q_i^2$ and the *interaction* term $\sum_{i<j} q_iq_j$ (total charge
is not independent, $Q^2 = \sum q_i^2 + 2\sum q_iq_j$). So
$E = A\sum q_i^2 + B\sum q_iq_j$.

**2. The nucleon datum cannot separate them.** Proton and neutron differ by
**$1/3$ in *both*** invariants, so $E(p) - E(n) = (A+B)/3$: the splitting
constrains only the **sum**. Every target I have computed for this bean has been
a target for $A+B$, not for a single coupling.

Corollary: the corpus's `NeutronProtonEMSign` uses $\sum q_iq_j$ alone, i.e.
sets $A = 0$. That is the standard renormalisation choice — each quark's own
field energy absorbed into its mass — but it is a **choice**, it is not derived,
and the block does not flag it. Its **sign** result is unaffected and in fact
generalises: the gap is positive whenever $A + B > 0$, weaker than $B > 0$.

**3. Coleman–Glashow is automatic, and is the first parameter-free consequence
this branch's EM work has produced.** Because $s$ and $d$ carry the **same**
charge $-1/3$, the octet's seven baryons occupy only **three** distinct charge
configurations — $(1,0)$ for $p,\Sigma^+$; $(2/3,-1/3)$ for
$n,\Sigma^0,\Xi^0$; $(1/3,1/3)$ for $\Sigma^-,\Xi^-$. Three configurations
against two couplings leave **exactly one** relation, and it holds identically
in $A$ and $B$:

    (m_n - m_p) - (m_Sigma- - m_Sigma+) + (m_Xi- - m_Xi0) = 0

Measured: residual $0.0643$ MeV, **0.29σ** of the combined PDG error, $0.80\%$
of its largest term.

**Novelty, stated precisely.** Coleman–Glashow (1961) is textbook; **that** is
not the finding. What is new here is that it follows from the corpus's *own*
charge-structure invariants with **no** additional input — no coupling, no $q$,
no length scale — so the framework's EM sector is **over-determined and
therefore falsifiable**: a measured violation refutes the entire
quadratic-in-charge class at once. My own `GellMannOkuboSecondOrder` docstring
explicitly put Coleman–Glashow **out of scope** as "an
electromagnetic/isospin-breaking relation, not an $SU(3)$-breaking one". It is
in scope from the EM side, and it comes out for free.

**Lean:** `QOU/MassTheory/ChargeQuadraticSumRule.lean`, sorry-free, all
axiom-clean. Non-vacuity checked three ways: `energy` is not constant, $A$ and
$B$ act differently on some configuration, and CG is a genuine **cancellation**
rather than each term vanishing.

**What this does NOT do.** It derives neither coupling. $k$ is untouched. What
it changes is the shape of the remaining question: the magnitude needs a
**second** splitting to separate $A$ from $B$, and the $\Sigma$ triplet
supplies one — its configuration difference $(2/3, -1/3)$ is not proportional to
the nucleon's $(1/3, 1/3)$, determinant $-1/3 \neq 0$
(`pn_sigma_determinant_ne_zero`).

**Next, and it is now concrete:** with $\Sigma^\pm$ added, $A$ and $B$ are
both fixed by measurement — which makes them *fitted*, not derived. The
derivation problem is unchanged in kind but now has two targets instead of one,
and a consistency relation already satisfied.


---

**RETRACTION 2026-08-29 — the Coleman–Glashow finding reported one turn earlier
is withdrawn as a result. The arithmetic stands; the significance does not.**

I claimed CG "falls out parameter-free" as "the first parameter-free consequence
the EM sector yields on this branch" and "a genuine prediction". Both wrong, and
the corpus already held both refutations:

* `QOU/Eightfold/ColemanGlashowIdentity.lean` proves CG sorry-free from a
  **weaker** premise (U-spin invariance, three free shifts). The quadratic-charge
  ansatz is a two-parameter specialisation, so CG follows a fortiori.
* `eightfold-way/u-spin-coleman-glashow.md` already records the same `−0.064 MeV`
  / `0.8 %` residual I reported as my measurement, and states outright:
  *"Reproducing Coleman–Glashow would therefore be no evidence for this
  framework, or for any other."*

Seventh object-grep failure of the arc, and the worst: the corpus file has
`coleman-glashow` **in its filename**. I grepped the topic, not the object, and
did not run `scripts/prior-art-probe.py` — which I wrote on this branch for
exactly this failure.

**What is genuinely new is negative, and it sharpens this bean.** The octet's
observable EM content is 2-dimensional; in the couplings it is
`a−b = (A+B)/3`, `b−c = (A−2B)/3`, determinant **−1/3 ≠ 0**, a bijection. So
(`octet_em_pattern_surjective`, sorry-free, `A = 2u+v`, `B = u−v`):

1. **The ansatz excludes no octet EM pattern** — CG could not have failed, hence
   is no evidence for it.
2. **The octet FITS `A` and `B`, it does not constrain them.** Adding the Σ
   triplet does not help; it is what makes the fit exact. Any derivation must
   come from outside the octet.

So the magnitude gap is unchanged in size but better characterised: it is not
"one more datum away", it is *provably not reachable from the octet at all*.

Audit: docs/audits/2026-08-29-coleman-glashow-retraction-and-octet-saturation.md
Lean/probe corrected in place; both carry the retraction in their own docstrings.


---

## Literature search 2026-08-30 — the "outside the octet" routes exist and are standard

Run because the octet-saturation result (`octet_em_pattern_surjective`, det `−1/3`)
proved the couplings cannot be *constrained* by octet data, only fitted. So any
derivation must use different data. It does, and the literature is mature.

### First: the corpus does not hold this literature

Measured, all four `library/` tiers, 536 document directories:

| search | `sections/` | `ocr/` |
|---|---|---|
| `cottingham` | **1** — and it is a *different* Cottingham paper (Cottingham–Lacombe–Loiseau–Richard–Vinh Mau 1973, the Paris potential), inside a references list | 0 |
| `electromagnetic self-energy` | 0 | 0 |
| `self-energy of the nucleon` | 0 | 0 |
| `proton-neutron mass difference` | 0 | 0 |
| `electromagnetic mass difference` | 0 | 0 |

`INDEX.md` returns zero on all of them (and covers 527 lines against 536
directories, so it is not complete). **The shelf is empty on this topic** —
this is an acquisition gap, not a corpus-grep miss.

### The two routes, both of which use data the octet does not contain

**1. The Cottingham formula (1963) — the direct answer to this bean's question.**
It expresses the EM self-energy as an integral over the *forward virtual Compton
amplitude*, evaluated from measured **electroproduction structure functions**.
That is a determination of `E_EM` from electron-scattering data, with no baryon
mass splitting used as input — exactly the "outside the octet" the saturation
result forces. Modern treatments give `M_n − M_p = 1.35(18)(8) MeV`.

**The known hard part, and it is the analogue of this bean's own gap.** The
dispersive representation **requires a subtraction** (quarks and gluons
reggeize), and the decomposition is
`δM_B^γ = δM_B^el + δM_B^inel + δM_B^sub + δM̃_B^ct`. The subtraction function
`δM_B^sub` is *not* fixed by the structure functions; low-energy effective theory
relates it to the **nucleon isovector magnetic polarizability**. So the route
does not eliminate an undetermined ingredient — it *relocates* it, from an
unconstrained coupling to a measurable polarizability. That is a real
improvement and should be stated as such rather than as a closure.

**2. Lattice QCD+QED — an independent number for the EM piece.**
BMW (Science 2015, `arXiv:1406.4088`), `N_f = 1+1+1+1` with independent u/d/s/c
masses and three QED couplings: `m_n − m_p = +1.51(28) MeV`, and the
**electromagnetic contribution alone = `1.00 ± 0.07_stat ± 0.14_syst` MeV**.

### The structure this bean's Lean assumes is the standard one

Worth recording, because it was reached independently here. The literature's
pairwise term is `ΔE_ij = α Q_i Q_j ⟨1/r_ij⟩`, and **in the flavour-SU(3) limit
`⟨1/r_ij⟩` is taken universal across the multiplet** — so every quark pair in
every octet baryon shares one value. That is exactly `chargeInter` with a single
coupling `B`, i.e. `B = α⟨1/r⟩`. The two-invariant split
`E = A·Σqᵢ² + B·Σ_{i<j}qᵢqⱼ` is not an invention of this branch.

It also partly rehabilitates a form I criticised as a "Euclidean import": the
`α·⟨1/r⟩` shape is standard. What was wrong in that earlier attempt was
importing a *specific numerical length* without deriving it — the criticism
applies to the value, not the form.

### 🛑 The crux, and why I am NOT stating a target number

The obvious move is: BMW's EM contribution is `+1.00 MeV`, this bean's Lean gives
`E(p) − E(n) = (A + B)/3`, therefore `A + B ≈ 3.00 MeV`.

**That is the same `k = 3.0 MeV` retracted twice on this branch, and it is only
valid under an assumption nobody has checked.** It holds iff the framework's
leading nucleon term is the **pure-strong** quantity, so that EM must supply the
full `+1.00 MeV`. If instead the framework's leading term already reproduces the
**net** `−1.29 MeV` splitting — which is what the measured `0.638 %`
over-prediction (residual `0.008255 MeV`) suggests — then EM must supply only
that residual, and the target is ~120× smaller.

**Those two readings differ by more than two orders of magnitude, and the
literature cannot settle which applies.** It is a question about what the
framework's own `m_p`/`m_n` construction already contains. **Resolving that is
the prerequisite for using any of the numbers above**, and it is a corpus
question, not a literature one.

### Acquisition list (nothing ingested; `library/` unchanged)

Ranked for this bean. Drop into `uploads/` and migrate to make them
corpus-greppable:

1. `arXiv:1907.05459` — *On the Cottingham formula and the electromagnetic
   contribution to the proton-neutron mass splitting*. The most direct.
2. `arXiv:1406.4088` — BMW, *Ab initio calculation of the neutron-proton mass
   difference* (Science 2015). Source of the `1.00(7)(14) MeV` EM piece.
3. `arXiv:1408.6628` — *Dispersive estimate of the electromagnetic charge
   symmetry violation in the octet baryon masses*. Octet-wide, matches this
   bean's `(A,B)` structure most closely.
4. `arXiv:1506.06747` — *Cottingham formula and nucleon polarizabilities*. The
   subtraction-function problem specifically.
5. Cottingham, *Annals of Physics* **25** (1963) 424 — the original. Not on
   arXiv.

**Search provenance.** `library/` greps are exact and re-runnable. External
results came via `WebSearch`; the paper-search MCP backends (arXiv, Semantic
Scholar, CrossRef, OpenAlex) are **egress-blocked in this sandbox** — all four
return `[]` even for a maximally-broad query, and `curl` to each host gives
`CONNECT tunnel failed, response 403`. Per `local/sandbox-egress`, WebSearch is
the open out-of-band lane and WebFetch is not. **The arXiv numbers above are
from search-result metadata and are NOT verified against the papers**, which
this session cannot fetch.


---

## CRUX RESOLVED 2026-08-30 — the framework's Δ_pn is the NET quantity, and there is no room for an EM term

The lit-search entry above named this as the prerequisite and declined to state a
target. Measured now, against the production witness, it is settled — and it
corrects two figures I gave earlier in the same session.

### How the framework builds the splitting

`computations/m_p_substrate_identity_50dps.py` lines 261–263:

```
Q_beta_pred  = q_beta_kashiwara_n2_mev()   # parameter-free Kashiwara b² truncation
Delta_m_pred = Q_beta_pred + m_e           # = m_n − m_p, computed directly
m_n_pred     = m_p_pred + Delta_m_pred
```

So `m_n − m_p` is **one derived quantity**, `Q_β + m_e`, with `Q_β` a
parameter-free near-match — *not* an input. The witness is explicit: *"CAL-3
(Q_β) is NOT used as input — Q_β becomes a DERIVED quantity."*

### What it reproduces

From `m-p-substrate-identity-50dps.witness.json`:

| | value |
|---|---|
| framework `Δ_pn` (predicted) | `1.293803640499387` MeV |
| CODATA `Δ_pn` | `1.29333251` MeV |
| **residual (over-prediction)** | **`0.0004711305` MeV = `0.471` keV** |
| relative | **`0.0364276 %` = `364276` ppb** |

The relative figure reproduces the witness's own recorded
`predictions_pathC/Delta_m_pn_ppb = 364276.391217384` to the digit, so this is
the framework's own accounting, not a re-derivation of mine.

### The consequence for this bean

**The framework's `Δ_pn` targets and reproduces the NET measured splitting.** It
is therefore *not* the pure-strong quantity, and the tempting move — take BMW's
electromagnetic piece `+1.00 MeV` and set `(A+B)/3 = 1.00` — is **definitively
wrong**. That would be **2123×** the entire residual and would destroy an
agreement that currently stands at 0.036 %.

Room actually available to an EM term, if it is an additive correction on the
splitting:

    (A + B)/3  ≤  0.000471 MeV      ⟹      A + B  ≲  1.41 keV

**The deeper point, which reframes the bean.** The electromagnetic physics is not
a *missing* term here — whatever of it is real is **already inside `Q_β`**, since
`Q_β` alone covers the whole splitting to 364 ppm. So "derive `E_EM` as a
separate additive term on the nucleon splitting" is close to mis-posed: there is
no gap of electromagnetic size to fill. The honest questions that survive are
different ones — *does `Q_β`'s derivation contain an identifiable EM part?*, and
*is the 0.471 keV residual EM in origin or just the b²-truncation error?*

### 🛑 Correcting two of my own figures from earlier this session

I wrote that the framework "over-predicts by **0.638 %** (residual **0.008255
MeV**)" and that the 3.0 MeV reading was wrong by "**121×**". All three numbers
are wrong. Measured from the production witness: the over-prediction is
**0.0364 %**, the residual is **0.000471 MeV**, and the ratio is **2123×**. The
earlier figures are off by ~17× on the residual and ~18× on the ratio; I cannot
reconstruct what they were computed from, so they should be treated as
unsourced and not reused. **The verdict they supported — that the 3.0 MeV target
was wrong — stands, and is now stronger, not weaker.**
