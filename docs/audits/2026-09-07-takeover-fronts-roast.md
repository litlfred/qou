# Takeover-fronts roast — six fronts red-teamed (2026-09-07)

**Owner instruction:** "start roasting". **Bean:** `qou-pbwj`. **Method:** the four
lenses + adjudicator of `local/devils-advocate-watcher`, the `da-arity-conflation`
questions, AGENTS.md §"NO FITTING, EXCEPT CAL-1/2/3" (the five mechanisms agents
keep missing), §"Before declaring refuted" (scope (a)/(b)), and §"Defined residual
≠ derived decomposition". Format follows `qou-8t3k` and the ROAST section of
`qou-301d`.

**Register.** The owner is a mathematician. Nothing below that is called a proof
carries an empirical prediction; every empirical statement is labelled as a
comparison against AME/CODATA and is scoped (a) unless an invariant is cited.

**What was read before writing a word** (per the instruction): the six front beans
in full; `qou-qjhc` (all five passes), `qou-17mq` (the observable-C and Option-B
sections), `qou-hok7` from "deg Z_n DERIVED" onward, `qou-vd7j`, `qou-301d`
(all 259 lines); issue #7092; PR #7005 body and its probe on branch
`claude/binding-resolution-is-self-inflicted-2026-09-07`; PR #7093 body;
`computations/probes/binding_volume_difference_probe.py` (`_snappy_braid_vols`,
`main`); `mass_at_3A_proper.atom_braid_word_3A` (docstring, 2026-09-05 state);
`computations/deltalambda/rev_*` headers; `computations/ptolemy/` (listing and the
five duality probes); `QOU/MathlibExt/TowerSpanReduction.lean`,
`InvolutionTowerWitness.lean`, `DisjointBlockTraceLaw.lean`, and the
`MarkovTrace` structure in `OcneanuTrace.lean`; the L2 dashboard witness; the
GGZ §12 "Duality" section in the library; and the corpus-grep per front (results
under each "Is it already answered?").

**Two prior-art hits change the verdicts before any argument is made.**

1. [`docs/audits/2026-08-25-atom-word-closures-are-not-hyperbolic.md`](2026-08-25-atom-word-closures-are-not-hyperbolic.md)
   is a **scope-(b)** result with four named invariants: `atom_braid_word_3A`
   is not a braid word ($2A+1$ averaged letters); every one of its $2^{2A+1}$
   branch braids is monotone (one run per generator, verified for all
   $A \le 24$); hence every branch closure is a connected sum of $(2,k)$ torus
   links (verified 32/32 against SnapPy `deconnect_sum`, SnapPy 3.3.2
   **installed in-sandbox**); hence $\mathrm{Vol} = 0$ for every branch. This
   answers front 1 and refutes front 6's stated angle.
2. [`computations/mirror-nuclei-coulomb-systematics.witness.json`](../../computations/mirror-nuclei-coulomb-systematics.witness.json)
   (re-run 2026-09-07) and
   [`deltalambda-coulomb-mirror-split.witness.json`](../../computations/deltalambda/deltalambda-coulomb-mirror-split.witness.json):
   the ³H/³He split is Coulomb to $0.99 \pm 0.07$ across $A = 3..39$, "so any
   QOU strong kernel must be charge-symmetric". That is the Z-resolved A=3
   observable front 3 wants, already measured, with a consequence front 3 has
   to survive.

---

## Front 1 — `qou-m6gp`: evaluate observable C (SnapPy volume of the derived braid closures)

**Strongest objection.** The bean's premise — "leg C has NEVER executed … the
derived braid closures are UNMEASURED, not refuted" — is true of *that probe*
and false of *the corpus*. The 2026-08-25 audit above computed exactly this
object, with SnapPy installed, and proved (scope-(b), invariants cited) that no
closure of the atom word can be hyperbolic. Worse, the code the bean wants to
run measures the wrong object even once SnapPy is present:
`binding_volume_difference_probe.py:93-111` builds
`braid = [k + 1 for (_c, _d, k) in w]` — it **discards the crossing sign and the
averaging weight of every letter** and closes an all-positive braid. That link
is none of the 32 branches; it is a positivisation the framework never
computes. So "run leg C" as written produces a number about nothing, and the
honest run (per branch) has already been done and returns $0$ for all
branches.

**Fit exposure.** *Selection against the target*, latent: once the closure is
known to be non-hyperbolic, the only way to get a nonzero volume out of this
route is to *choose* a branch, a sign resolution, or a subset of letters — and
the criterion available for choosing is agreement with $B_{\mathrm{AME}}$.
The bean's own "fix the helper so ImportError is a distinct verdict" does not
open that door; anything beyond it does.

**Arity check.** "C is refuted" was read off a witness field that is `null`
(question 4: an absent value read as a truth value). The corrected claim is a
universally-quantified structural statement over *all* branches of *all*
$(Z,N)$ with $A \le 24$ — a family, and the 08-25 audit quantifies it correctly.
Nothing pointwise is being promoted to universal here.

**Is it already answered?** Yes. `docs/audits/2026-08-25-atom-word-closures-are-not-hyperbolic.md`
(scope-(b)); `docs/audits/2026-07-04-he4-link-volume-braid-closure-refuted.md`
(proton, neutron, ³H, ³He, ⁴He closures non-hyperbolic and with the wrong
component counts — ³H closure is 4-component against the 1-component $8_{11}$);
`atom_braid_word_3A`'s own docstring ("Measured: all 32 branch closures for 2H
are non-hyperbolic … Vol = 0 for every one"). `.beans/`: `qou-26f2` is about
tautological assertions, not about C; `qou-17mq` itself cites the 08-25
non-hyperbolicity in its "SECOND BLINDNESS" section while sending the reader to
install SnapPy in another. No `completed`/`scrapped` bean carries "observable C".

**L2 relevance.** None. No dashboard row (`m_mu`, `Q_beta`, `m_n`, `Delta_pn`,
`alpha_em_inv`, `m_K/m_pi`) depends on a hyperbolic volume of an atom-word
closure, and binding $b_2, b_3$ cannot move on a quantity that is provably $0$.

**Result worth having.** A one-line probe fix so that ImportError reports
`unevaluated` rather than `refuted`, plus a cross-reference from the probe's
description to the 08-25 audit — so the next reader does not install SnapPy to
re-derive $0$.

**Verdict (judgement): KILL as a research front; keep a ≤ 10-line chore.** The
question is closed at scope (b) by an audit that installed the tool the bean
says is missing. The residual value is bookkeeping.

---

## Front 2 — `qou-zmat` / issue #7092: is the duality/σ ratio a coboundary?

**Strongest objection.** The issue asks whether vertex scalars
$\lambda_v \in K^\times$ exist with $\sigma(x_t)/x_{\pi(t)} = \prod_i \lambda_{v_i}^{t_i}$
on *one point* — the exact class-1 point of L6a4 — and then reads "yes" as
"duality and the σ-transport are the same map on the variety". That is
question 2 of the arity check: agreement of two maps at a point is pointwise;
"the same map" is the universal closure. Two distinct rational self-maps of a
variety can agree on a Galois orbit. What a "yes" establishes is a fact about
the *point* — it is exchanged with its Galois conjugate by duality up to gauge,
i.e. it is "self-dual up to $\mathrm{Gal}(K/\mathbb{Q})$" — not that
$\rho \mapsto \rho^{-T}$ *induces* $\sigma$. The bean's own title
("identify the duality involution … with the sigma-transport") asks for the
map statement; the coboundary test cannot deliver it. Second, the issue says
"solve the vertex-gauge system over $K$ exactly" — but the system is
multiplicative in $K^\times$, an abelian group, not $K$-linear. The decisive
form is integer: with $M$ the $(\text{coordinates}) \times (\text{vertices})$
exponent matrix, the ratios $r_t$ are a coboundary iff
$\prod_t r_t^{a_t} = 1$ for every $a$ in the left $\mathbb{Z}$-kernel of $M$
(Smith normal form), modulo the $\mu_3$ torsion the fifth pass already
identified as the correct SL(3) gauge. Solving "over $K$" (logs, or a field
linear system) either does not exist or silently enlarges the gauge group.

**Fit exposure.** *Widening the ansatz* — named in the issue as forbidden, and
it is exactly the temptation: the five coordinates eliminated by
`eliminate_fixed_ptolemys=True` may be eliminated differently for $P^{c}$ and
$P^{-c}$, and the moment one adds "per-tetrahedron" or "per-edge" scalars to
absorb that, the coboundary test becomes unfalsifiable again. Also *subset
selection*: 5 of 11 $\{2,1,0,0\}$ coordinates have no partner present; the
test must run on the full system with those as unknowns, not on the 6 that
happen to pair. Both are named in the issue; neither is yet guarded in code.

**Arity check.** (i) The claim is a *family* over coordinates $t$, collapsed to
one yes/no — fine. (ii) Pointwise vs universal — the defect above. (iii)
Shared instance: the whole arc lives on class 1 of L6a4; nothing transfers to
classes 2/3 or to $8_{11}$ without re-running. (iv) No set-level fact is being
read as a truth value.

**Is it already answered?** No. `computations/ptolemy/ptolemy_duality_vs_sigma_comparison.py`
is the inconclusive fifth pass; no probe pulls vertex incidences.
`docs/audits/` hits on "coboundary" are unrelated (germ gauge covariance,
descent cocycles). Library: GGZ arXiv:1207.6711 §12 "Duality" is a *different*
duality (Ptolemy ↔ shape coordinates, Langlands dual groups) and does not
address $\rho \mapsto \rho^{-T}$; §8–9 (decorations as determinants) is what
the fourth pass already used. No `completed`/`scrapped` bean.

**L2 relevance.** None. This is the Eightfold/obstruction-class arc; no
dashboard row reads a Ptolemy coordinate. The Sym² verdict on the 13 classes
is, by the bean's own account, independent of the answer either way.

**Result worth having.** A definite **no** — the ratio is not a coboundary —
which would establish that duality and σ-transport are *different* maps
already at the class-1 point, closing `qou-qjhc` negatively and stopping a
tranche of decoration formalisation that would otherwise be spent proving an
identification that is false.

**Verdict (judgement): CONTINUE, re-scoped to the integer form and to a
point-level statement.** Bounded, exact, decisive. Rewrite the deliverable as
"the class-1 point is/is not exchanged with its Galois conjugate by duality up
to $\mu_3$-gauge", implement the $\mathbb{Z}$-kernel test, treat the five
eliminated coordinates as unknowns, and do not describe a "yes" as a map
identity.

---

## Front 3 — `qou-tbk7`: Z-resolved $b_3$ (takeover of #7005)

**Strongest objection.** PR #7005's "5.81 digits lost to convention, none to
experiment" is a statement about the **data-side** tower
$b_3 = B(3) - 3B(2)$, and the "convention" is which AME datum stands in for
$B(3)$. The resolution of a *target* is not the resolution of a *comparison*:
the comparison's discriminating power is bounded by the prediction's residual,
and the production bond model misses ²H by $+27.34\,\%$
(`2026-08-25-atom-word-closures-are-not-hyperbolic.md` §5), i.e. under one
digit. Six digits on the target buy nothing against a 0.6-digit prediction.
More specifically, on the framework side the "Z-dependence the construction
averages away" is the chain bond model $\prod_i L_i$ with
$L_{pp} = z$, $L_{nn} = z - h$, $L_{pn} = z - h(\tfrac12 - \tfrac{\delta}{4})$
(`chain_bond_arrangement_dependence_probe.py`), which is **purely pairwise**:
its three-body term is identically zero for both mirror partners, so a
"Z-resolved $b_3$ construction" on the framework side resolves $0$ against
$0$, and the whole of $b_3$ remains the open extensive term the AGENTS.md
frontier box says no per-block or pairwise object can supply. And on the data
side, a Z-resolved $b_3(Z,N) = B(3) - B_{pp} - B_{pn} - B_{nn}$ (with the right
multiplicities) needs $B_{pp}$ and $B_{nn}$, which AME does not have — the
diproton and dineutron are unbound. #7005's $3B(2\mathrm{H})$ is not the
construction discarding Z; it is the only pair reference the data supplies.

**The part that is real — and it RAN while this roast was being written.**
The one Z-resolved A=3 quantity that *is* a clean observable is the mirror
displacement $B(^3\mathrm{H}) - B(^3\mathrm{He}) = 0.7638$ MeV (5.88 digits),
and the framework's bond model predicts it with no free input. Measured here
at the proton pin (`mp.dps = 30`, $z = 0.61269$, $h = 0.20906$):
$\ln(L_{pp}/L_{nn}) = 0.41736$, so the un-normalised exact-trace split is
$E_0 \cdot 0.41736 = 1.747$ MeV, $2.29\times$ AME. A sibling session claimed
`qou-tbk7` at 18:30 UTC and ran the full test
(`computations/probes/z_resolved_b3_mirror_split_probe.py`, 17/17, proton pin,
convention D); its un-normalised exact form gives **1.74707** MeV — the same
number, independently — and its writhe-normalised production chain gives
**0.76532** MeV against AME **0.76375** ($+0.205\,\%$, $1556\,\sigma_{\exp}$).
The sibling then did the thing this roast would have demanded: it checked
the next mirror pairs. The chain split is the **same constant at every
mirror pair** ($\alpha \ln(q_0^3(1 + q_0 - q_0^2))$, Z-independent), while AME
grows — $^7$Li/$^7$Be $1.644$ MeV (ratio $0.465$), $^{13}$C/$^{13}$N $3.003$ MeV
(ratio $0.255$). So the $A = 3$ landing is a coincidence of one point, already
on record in `coulomb_mirror_killswitch_probe`, and the writhe factor
$\alpha \ln(1 - h) = -0.9818$ MeV that produces it is load-bearing. And on
$b_3$ itself: **negative on every form** (chain $-2.36 / -3.12$, exact
$-1.87 / -3.62$, $B^0_{\mathrm{can}}$ $-1.37 / -1.30$ MeV) against a positive
target ($+1.808 / +1.044$) — the pairwise wall in Z-resolved form, exactly as
argued above. This is consistent with the corpus's own
`mirror-nuclei-coulomb-systematics` witness, which finds the split is
**Coulomb** ($0.99 \pm 0.07$ of uniform-sphere $\Delta E_C$ across $A = 3..39$)
and concludes the strong kernel must be charge-symmetric: the word's
pp/nn asymmetry ($L_{pp} - L_{nn} = h$ exactly, a *strong-sector* difference)
is a prediction the data contradict in kind at $A \ge 7$.

**Roast of the sibling's result, since it now exists.** The $+0.205\,\%$ at
$A = 3$ is the textbook shape of *selection against the target* one level
up: of three forms (chain-normalised, exact un-normalised, $B^0_{\mathrm{can}}$)
exactly one lands, and it lands only at the one mirror pair where the
constant happens to equal the Coulomb value. The sibling labelled it a
coincidence, which is correct; the hazard is a later reader quoting "the
mirror split from $q_0$ alone to 0.2 %" without the $A = 7, 13$ line beneath
it. Its verdict text should carry the three-pair table, not the one-pair
number, wherever it is repeated.

**Fit exposure.** Two live mechanisms, both now realised in miniature. *Per-case
dispatch / form selection*: three forms, one hit. *Importing an empirical
term*: the missing $B_{pp}, B_{nn}$ are routinely filled from effective-range
parameters or a Coulomb model with $r_0 = 1.2$ fm — somebody else's fit
(`mirror-nuclei-coulomb-systematics` uses exactly such an $r_0$ and says so).

**Arity check.** "The construction discards the resolution it has" conflates
the data-side tower (A-only by necessity) with the framework word (Z-resolved
by construction); question 3 — two different instances, one sentence. And
"~6.1 digits, in the company of $Q_\beta$" compares a *target's* resolution
with a dashboard column that reports *prediction residuals* — different
quantities in one table (the PR flags it as inference; the bean title does
not). The sibling's "lands from $q_0$ alone" is a one-instance statement
about $A = 3$ being read against a family over $A$; its own table refutes the
universal reading.

**Is it already answered?** **Yes, as of 18:30 UTC today**, by the takeover
session on `qou-tbk7` (witness `z-resolved-b3-mirror-split-probe.witness.json`,
not yet on `main`). Before that: `a3-mirror-residual-reconciliation.witness.json`,
`deltalambda-coulomb-mirror-split.witness.json`,
`mirror-nuclei-coulomb-systematics` (re-run 2026-09-07),
`coulomb_mirror_killswitch_probe` (the $A = 3$ hit beside $0.65 / 1.59$ MeV
misses), `2026-07-11-mirror-split-coulomb-diagnosis` (the C-frame $3\times$),
`chain_bond_arrangement_dependence_probe.py`, and the AGENTS.md frontier box.
No `completed`/`scrapped` bean carries "Z-resolved".

**L2 relevance.** None on the dashboard. On binding: $b_3$ cannot move — the
derived construction has no three-body term and now measures negative on
every form against a positive target. The A=3 split is not an L2 match
($1556\,\sigma$) and is not a match at all at $A = 7, 13$.

**Result worth having.** Now had: the separation the sibling states — the
A-only $b_3$ mixes the mirror bond difference (framework: predicted, wrong
beyond $A = 3$; data: Coulomb) with the connected 3-body term (framework
$\le 0$; data $> 0$), and the second is the open object. The follow-on worth
one paragraph: the pp/nn interface letters $(1, 0)$ vs $(1, -h)$ encode a
*strong* charge-symmetry breaking that the $A \ge 7$ data exclude, which is a
constraint on the shape of the production word, not on a magnitude.

**Verdict (judgement): CLOSE-OUT, not continue.** The re-scope this roast
would have proposed has been executed and returned the expected negative
with the coincidence correctly labelled. Do not build "the Z-resolved $b_3$
construction" further: it resolves $0$ (framework 3-body) against the open
extensive term, and the pairwise piece is already known to fail past $A = 3$.
The bean stays open only for the charge-symmetry paragraph and the
three-pair table; the ${}^6$Li/${}^7$Li tower extension the sibling declined
is correctly declined (same pairwise wall, and $A = 5$ is unbound).

---

## Front 4 — `qou-0ie7`: $\mathrm{REV}_n$ sharpness with the $\Sigma\beta$ constraint

**Strongest objection.** The bean asserts the dropped constraint
$\sum_i \beta_i = n + \ell(\ell-1)/2$ is "the only remaining relaxation of
size". No accounting supports that. The over-statement budget at the argmax
is $\approx 3\times$ (#7081, ratio of the maximised bound to the enumerated
truth, $3.09\times$ at $n = 40$). PR #7093 prices the Jensen inter-class
coupling at $1.21\times$ and shows it *shrinks* with $\ell$. That leaves a
factor $\approx 2.5$ unattributed, and the $\Sigma\beta$ constraint is a
restriction on the feasible set, not a term in the bound — it cannot reduce
the per-configuration over-statement of the **one-body** term
$\sum_i F(\beta_i) \le \ell C$, where $F(k) = \sum_{m \le k} \varepsilon_m$
saturates at $C = 6.1714$ only as $k \to \infty$ and the maximiser's
$\beta$'s are $O(\sqrt n)$ with $W/\ell \approx 1.7$. If most of the 2.5 sits
in the one-body slack, a $\Sigma\beta$ formulation will shave the gap and
leave the exponent where it is — a fourth "no closure" in the style of #7093.
A referee asks for the decomposition before the formulation.

**Fit exposure.** None in the forbidden sense — the deliverable is a proved
bound, and a bound is either valid or not. The live hazard is *reading
$n \le 44$ numerics as sharpness*: `rev_sharpness_discriminator_control_probe`
already shows the $n^{3/4}$ column of a provably $\Theta(\sqrt n)$ control is
flat at $1.20$–$1.23$ over exactly the reachable range. Any "the new bound is
$O(\sqrt n)$ on the data" or "tracks $n^{3/4}$" statement below
$n \sim 150$ is the tolerance-sized-to-its-window error. The bean's own
"measure against the exact $\mathrm{REV}_n$ ($n \le 44$)" is fine as a
sanity check on a bound and useless as evidence on the exponent.

**Arity check.** $\Omega(\sqrt n) \le \mathrm{REV}_n \le O(n^{3/4})$ are
$\forall n$ statements with constants; "the $3/4$ is sharp" is an
$\exists c\, \forall N\, \exists n > N$ statement — a different arity, and it
is not decidable from any finite table. Also: $\mathrm{REV}_n$ carries
$\ln q_0$ as inverse temperature, so "the object" is a one-parameter family
in $q$; the exponent question is being asked at one archimedean point. Fine
if said; the bean does not say it.

**Is it already answered?** No. `rev_beta_coordinate_identity_probe.py`
states constraint (III) and never uses it; `rev_beta_bound_polynomial_max_probe`
maximises over $(\ell, W)$ with $n$ entering only through $\hat H$; #7093's
three refutations are on the pair term, not on (III). `qou-hok7` records the
resummation route to $B_D$ as negative on `main` since 2026-08-21. No
`completed`/`scrapped` bean.

**L2 relevance.** None, and the bean should say so: `qou-hok7` itself records
that "what remains genuinely open is $\mathrm{REV}$'s asymptotics, which is a
statement about the *object*, not about a route to $B_D$". Neither the
exponent nor the constant feeds a dashboard row or a binding $b_k$.

**Result worth having.** The budget: at the maximiser's own $(\ell, W)$ and
$n \in \{16, 24, 32, 40\}$, split the $3\times$ into (one-body slack)
$\times$ (Jensen coupling) $\times$ (what (III) would remove) — three
numbers that either justify a $\Sigma\beta$ formulation or kill it before it
is written.

**Verdict (judgement): CONTINUE, conditional on the budget first.** Pure
mathematics with a definite answer and no fit surface; but the bean's
premise that (III) is the last relaxation of size is unmeasured, and PR #7093
already showed that this arc guesses and refutes at one attempt per session.
Measure the split; formulate only if (III) owns the majority of the gap.

---

## Front 5 — `qou-fq1i`: SandwichReduces on a symmetric-group tower

**Strongest objection.** The model already exists in one line and the
labour is Mathlib plumbing that reaches nothing. On
$A = \mathrm{MonoidAlgebra}\,R\,(\mathrm{Equiv.Perm}(\mathrm{Fin}\,n))$ with
the standard inclusions, $g_m = (m\; m{+}1)$, $g_m^{-1} = g_m$, the
$q = 1$ Ocneanu trace $\mathrm{tr}(w) = z^{\,n - c(w)}$ ($c$ = number of
cycles) satisfies every field of `OcneanuTrace.MarkovTrace` (T1: class
function; T2: $\mathrm{tr}(1) = 1$; T3/T3′: multiplying $a \in S_n$ by the
transposition $(n\; n{+}1)$ merges the cycle of $n$ with the fixed point
$n+1$, so $\mathrm{tr}(a g_n) = z\,\mathrm{tr}(a)$ with $z = z^{-1}$
substituted for $g_n^{-1} = g_n$), and it is non-multiplicative
($\mathrm{tr}(g_1)^2 = z^2 \ne 1 = \mathrm{tr}(g_1^2)$). `SandwichReduces`
for it is the double-coset decomposition
$S_{m+1} = S_m \sqcup S_m\, s_m\, S_m$, a two-line group fact. So the witness
is *guaranteed* to exist before the session starts, and what it exercises —
"the filtration content **and** the trace content of `TowerSpan`, on a
tower Mathlib lacks" — is exactly what `qou-301d` already predicted it would
and no more: it does not touch the Hecke tower, where the quadratic relation
is the content, and it does not touch the atom word, which
`DisjointBlockTraceLaw.lean:470-480` records as outside every route's reach
(maximal level occurring four times). The bond-product reading stays
**measured, not derived** after the session exactly as before it.

**Fit exposure.** None, because nothing numerical is produced. The hazard is
rhetorical: a sorry-free witness on $S_n$ being cited downstream as
"TowerSpan holds for a Hecke-type tower" — question 3 of the arity check
(shared type, different instance).

**Arity check.** `TowerSpan` is $\forall n\, M$; `SandwichReduces B m` is per
$(B, m)$; both are families. Instantiating them on one algebra proves an
existence statement about *models* of the axioms, not anything about the
production instance. The 2026-09-07 entries in `qou-301d` are careful about
this; the bean title is not.

**Is it already answered?** No — the S_n model is not in the tree
(`grep 'Equiv.Perm (Fin'` finds five unrelated files; `SandwichReduces` occurs
only in the two 09-07 modules and `qou-301d`). `qou-301d` itself carries the
roast that governs: "payoff is hygiene, not physics", and its ROAST of
2026-08-30 held exactly. `completed` bean `qou-t8qh` (q-Jucys–Murphy) is
adjacent infrastructure, not this.

**L2 relevance.** None. No observable reads `TowerSpan`.

**Result worth having.** A **counterexample**: a `MarkovTrace` on a growing
tower for which `DisjointBlockMultiplicative` *fails*. `DisjointBlockTraceLaw`
records "NOT ACHIEVED: no counterexample … every small model I tried had the
axioms force the law to hold". The $S_n$ tower with the class-function trace
*satisfies* the law (it is multiplicative on disjoint supports), so it cannot
be that counterexample either — which is worth writing down, because it
narrows where one could live (it needs $h \ne 0$ or a non-class-function
trace).

**Verdict (judgement): KILL as a front; allow as a capped chore.** If done at
all, cap at one session, state in the module docstring that it proves the
$q = 1$ shadow only, and do not let the Lean be cited as evidence about
$H_n(q)$. The only route with content is the Hecke tower itself
(`H_{m+1} = H_m + H_m g_m H_m` at $q \ne 1$), and that needs the Hecke algebra
as a tower in Lean, which `qou-08a2` prices at an epic.

---

## Front 6 — `qou-dgpz`: Option B, a DERIVED atom→knot rule at $A \ge 4$

**Strongest objection.** The bean's "DISTINCT ANGLE" — *take the per-(Z,N)
canonical word and ask what its closure is as a link via SnapPy `identify()`*
— is refuted at scope (b) by
`2026-08-25-atom-word-closures-are-not-hyperbolic.md`: the word is not a
braid; each of its $2^{2A+1}$ branches closes to a connected sum of $(2,k)$
torus links; $\mathrm{Vol} = 0$ for every branch at every $A \le 24$. And
`2026-07-04-he4-link-volume-braid-closure-refuted.md` already ran the
component-count version: the ³H closure is 4-component, $8_{11}$ is a knot.
`identify()` on a connected sum of torus links returns no census knot and no
volume, so the route delivers *nothing* the EM-linking exponent $p$ could be
measured on — the exact blocker `qou-17mq` says Option B exists to remove.
Underneath: `2026-08-25-knot-id-is-an-admitted-fit.md` shows the existing
$A \le 3$ assignments were chosen by proximity of $\mathrm{Vol}$ to
$B_{\mathrm{AME}}/(\rho m_e)$ (the producer says so verbatim), that the SDP
"selector" is a feasibility check with no objective, and that the "closure
identifies as $6_2$" check round-trips SnapPy's own stored braid word. There
is no derived map at $A \le 3$ to extend.

**Fit exposure.** Maximal — this is the front the 2026-09-05 census-route
retirement is *about*. Every way past the scope-(b) obstruction is a
selection: pick a branch (32 at ²H, 512 at ⁴He), pick a sign resolution of
the averaged letters, pick which letters to drop, pick a census manifold
near a target. The AGENTS.md "giveaway" applies literally: $A \in \{5,6,7\}$
had no prediction because no census object matched. Owner ruling A
(2026-08-29) — deuteron knot is the canonical braid closure, Vol $=0$,
binding not a volume term — already concedes the point at $A = 2$.

**Arity check.** "The one route that unblocks $p$" reads an *absence* (no
derived map) as a *pointer to a route* — question 4 in a new spelling: a
set-level fact ("the corpus has exactly one $A$ with hyperbolic geometry")
does not make any particular construction a route. And "derive the knot from
the word already in production" assumes the word has *a* closure; it has
$2^{2A+1}$, none hyperbolic (question 1: a family, not an object).

**Is it already answered?** Yes, negatively, three times: the two audits
above, PR #1421 ("no derived atom→knot rule"), `qou-vd7j` (Frobenius selector
admits 0/3558, then diagnosed as an over-determination artefact — which
removes the obstruction reading without supplying a selector),
`2026-07-13-atom-knot-rule-a5plus-constraints.md` (constraint table, $\mathrm{Vol}_4$
in a census gap), `2026-05-24-a5-a7-knot-census-candidates.md`. `completed`
bean `qou-5vhf`: "the substrate complexity bound cannot select a link".

**L2 relevance.** None directly; the stated payoff is the exponent $p$ in the
EM-linking kernel, which feeds $\kappa(A)$, which is not a dashboard row and
whose series `qou-17mq` has shown cannot see $p$ anyway.

**Result worth having.** The negative is already written. What is not
written, and would be worth one paragraph in `conj:canonical-knot-id-sdp`'s
block: that any atom→knot map must be a map *other than* Markov closure of
the production word, because closure is structurally volume-trivial — which
turns "no derived rule" from an absence into a constraint on the rule's
shape.

**Verdict (judgement): KILL as posed.** The distinct angle is dead on
arrival by a scope-(b) audit; every other angle is census selection, which
the owner retired on 2026-09-05. Do not start on "start B" unless the angle
is one that does not pass through closure of `atom_braid_word_3A` or through
a census — and none has been named.

---

## Adjudication across the six

Expected value is judged against the owner's stated goal — L2, with the
binding gap read as *shape* (#7005's lost digits; $\mathrm{REV}_n$ as a free
energy over partition shapes). Blunt summary: **no front moves a dashboard
row.** The one front that touched a well-resolved binding observable with a
parameter-free prediction (front 3) was executed by a sibling while this roast
was being written, and returned the negative predicted above, with the $A = 3$
coincidence correctly labelled.

| rank | front | bean | verdict | L2 row that could move | fit surface | already answered? |
|---|---|---|---|---|---|---|
| 1 | $\mathrm{REV}_n$ with $\Sigma\beta$ | `qou-0ie7` | continue **after** the $3\times$ budget split | none | window-sized reading of $n \le 44$ | no |
| 2 | #7092 coboundary | `qou-zmat` | continue, integer ($\mathbb{Z}$-kernel) form, point-level claim | none | ansatz widening on the 5 eliminated coordinates | no |
| 3 | Z-resolved $b_3$ / mirror split | `qou-tbk7` | close-out (charge-symmetry paragraph + three-pair table only) | none; $b_3$ negative on every form, split coincidental at $A = 3$ | form selection (3 forms, 1 hit at 1 pair), imported $r_0$ | **yes — sibling, 18:30 UTC today**, plus the Coulomb witnesses |
| 4 | SandwichReduces on $S_n$ | `qou-fq1i` | kill / capped chore | none | none | no (model is a one-liner) |
| 5 | observable C | `qou-m6gp` | kill / 10-line chore | none | branch selection if pushed past Vol $=0$ | **yes, scope (b)** |
| 6 | Option B | `qou-dgpz` | kill as posed | none | maximal — census selection | **yes, three times** |

**Fund first (judgement): front 4, and only its first step — the budget.**
With front 3 closed by the sibling's run, nothing left on the list serves the
L2 goal, so the ranking is by *definiteness per session*. The
$\mathrm{REV}_n$ question is pure mathematics with a yes/no answer and no fit
surface, and one cheap measurement — splitting the $3.09\times$ over-statement
at the $n = 40$ argmax into one-body slack, Jensen coupling, and the part
constraint (III) would remove — decides whether the $\Sigma\beta$
formulation is worth writing or is a fourth guess. Front 2 is second: bounded,
exact, decisive, but it decides a point-level fact in an arc with no
observable. Fronts 1, 5 and 6 should not be started; front 3 should be
written up, not extended.

**One caution on reading front 3's landing.** The sibling's
$+0.205\,\%$ at $A = 3$ will be quoted. It is one form of three, at one
mirror pair of three, with the writhe factor $\alpha \ln(1-h) = -0.98$ MeV
doing the work, and the same constant misses by $0.65$ and $1.59$ MeV at
$A = 7, 13$. Under §"NO FITTING" that is *selection against the target* in
miniature, and under the ranking rule it is worth less than the honest
$2.29\times$ miss of the un-normalised form — because only the miss can be
iterated. Wherever the number is repeated, the three-pair table goes with it.

**What this roast did not do.** No code was changed, no witness regenerated,
no bean closed. The single new number ($\ln(L_{pp}/L_{nn}) = 0.41736$ at the
proton pin) was computed in-session from the production functions
`closed_form_tau_M.markov_z`, `hecke_h` and `_li_2_q_util.flavor_split_leading`
at `mp.dps = 30`, agrees with the sibling's independent $1.74707$ MeV once
multiplied by $E_0$, and is not committed anywhere as a witness.

## Addendum (2026-09-11, merge-coordinator, on the owner's instruction at merge time) — the Front 1 verdict is superseded by measurement

Row 5 of the adjudication table and Front 1 above say observable C is "already
answered, scope (b)" because `2026-08-25-atom-word-closures-are-not-hyperbolic.md`
found $\mathrm{Vol} = 0$ for every atom-closure branch. **That premise is stale,
and #7130 (merged `ec645c5a538`) overrules it by running leg C on the live
word**: the 2026-08-25 result is the *grouped* word, whose core is monotone;
the live alternating core (2026-09-05) is not, and sign-faithfully every
per-nucleon 3-strand branch closure is a **hyperbolic** 2-component link —
proton branches L9n10 ($9.9665$), L11a252 ($16.1911$), L7a6 ($4.7495$),
L9a21 ($11.9429$); neutron branches L11a252, L9a21 (twice), L11n202 ($8.1957$).
What #7130 establishes instead is stronger on the quantity leg C actually
prices: each inter-nucleon interface is a single letter, so every atom-branch
closure is the connected sum of its $A$ nucleon pieces (`deconnect_sum`,
800/800 branches), and by additivity of simplicial volume over the JSJ pieces
$\Delta\mathrm{Vol} = \mathrm{Vol}(\text{atom}) - \mathrm{Vol}(\text{free}) \equiv 0$
on every branch, hence $B_C = 0$ — **scope (b) on the difference only**, not
on hyperbolicity, and the absolute-volume reading is a separate open question
(bean `qou-l99f`, carried by #7121). So the verdict for Front 1 (the difference reading is dead;
do not start it as a research front) survives; its stated *reason*
("non-hyperbolic, $\mathrm{Vol} = 0$", "run leg C produces a number about
nothing") does not, and the "already answered" cell of row 5 should be read as
"answered by #7130, on the difference". Measurement outranks the roast; the
text above is left as the dated record of the roast as delivered.
