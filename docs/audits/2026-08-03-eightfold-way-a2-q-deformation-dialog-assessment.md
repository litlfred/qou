# Eightfold-way / A₂ / q-deformation dialog assessment

**Date:** 2026-08-03
**Branch:** `claude/eightfold-way-a2-lattice-ijoegv`
**Trigger:** external dialog (Gemini) pitching a chain of claims — that
Drinfeld–Jimbo $q$-deformation makes the angles between the $A_2$ simple
roots $q$-dependent; that at real $q$ the angle becomes imaginary and the
flavour weight lattice becomes hyperbolic; that this identifies
$\mathrm{SU}(3) \to \mathrm{SU}(2,1)$; that the gluon flux tube is evidence
of hyperbolic geometry; and that QOU realises $\mathbf 3 \otimes
\bar{\mathbf 3} = \mathbf 8 \oplus \mathbf 1$ topologically.
**Audience:** anyone evaluating a "$q$ curves the flavour lattice" re-pitch,
or planning Standard-Model / eightfold-way formalisation work.

**Bottom-line up front.** The dialog's central mathematical claim is
**false**, and falsifiable in one line: the $[2]_q$ appearing in the quantum
Serre relation is the **Gaussian binomial coefficient**
$\binom{2}{1}_q$, **not** the Cartan-matrix entry. The dialog
fused two unrelated occurrences of the numeral $2$. Everything downstream —
imaginary angles, Cauchy–Schwarz violation, hyperbolic root lattice,
$\mathrm{SU}(2,1)$ — is a cascade from that single conflation. The
citations, unusually, are all real; three of six are cited for claims
stronger than they support. Every "in QOU, $X$" statement in the dialog is
invented, and each is *weaker* than what the corpus already states about
itself.

## 1. The fatal error, stated precisely

Classical Serre relations for a Kac–Moody datum read
$(\mathrm{ad} e_i)^{1-a_{ij}}(e_j) = 0$. For $A_2$, $a_{12} = -1$, so
$1 - a_{12} = 2$ and the relation expands as

$$
  e_i^2 e_j - 2\, e_i e_j e_i + e_j e_i^2 = 0 ,
$$

where the coefficient $2 = \binom{2}{1}$ is a **binomial coefficient**. The
Drinfeld–Jimbo quantisation replaces binomial by Gaussian binomial:

$$
  \sum_{k=0}^{1-a_{ij}} (-1)^k
  \binom{1-a_{ij}}{k}_{q_i}
  e_i^{\,1-a_{ij}-k} e_j e_i^{\,k} = 0
  \quad\Longrightarrow\quad
  e_i^2 e_j - [2]_q\, e_i e_j e_i + e_j e_i^2 = 0 .
$$

So $[2]_q = \binom{2}{1}_q = q + q^{-1}$ deforms
$\binom{2}{1} = 2$.

The dialog instead read that $2$ as the $2$ in the *Cartan-matrix
normalisation*

$$
  a_{ij} = \frac{2(\alpha_i,\alpha_j)}{(\alpha_i,\alpha_i)} ,
  \qquad
  \cos\theta = \frac{(\alpha_1,\alpha_2)}{|\alpha_1|\,|\alpha_2|} = -\tfrac12
  \;\Rightarrow\; \theta = 120^\circ ,
$$

and concluded $2\cos\theta_q = -(q+q^{-1})$. These are two different $2$'s —
a binomial coefficient and a normalisation constant — that coincide
numerically at $A_2$. There is no equation relating them.

**What is actually true.** In Drinfeld–Jimbo quantisation the **root datum
is fixed input, not output**. The Cartan matrix, root lattice, weight
lattice, and Weyl group of $U_q(\mathfrak{sl}_3)$ are *identical* to those
of $\mathfrak{sl}_3$; only $q_i = q^{d_i}$ with $d_i = (\alpha_i,\alpha_i)/2$
enters, and $d_i = 1$ in the simply-laced case. For generic $q$,
$\mathrm{Rep}\,U_q(\mathfrak g) \simeq \mathrm{Rep}\,\mathfrak g$ as tensor
categories (Drinfeld–Kohno / Kazhdan–Lusztig); weight multiplicities are
literally equal. Crystal bases exist *precisely because* the weight
combinatorics is $q$-independent — the $q \to 0$ limit retains the same
lattice.

**Scope.** This is a **scope-(b) structural exclusion** per
[`AGENTS.md` §Before declaring "refuted"](../../AGENTS.md): the invariant
cited is that the root datum is an input to the quantisation functor, so no
choice of $q$ can move it. The hexagon does not bend.

### 1a. What $q$ *does* deform (the correct replacement)

Three things, none of them the lattice geometry:

1. **The coproduct.** $\Delta(E_i) = E_i \otimes 1 + K_i \otimes E_i$ is
   **non-cocommutative**: $\Delta \neq \tau \circ \Delta$. Tensor-factor
   ordering matters, so Clebsch–Gordan coefficients become $q$-dependent and
   orderings of a multi-constituent state are inequivalent. *This* — not a
   deformed $I_3$ — is the mechanism for constituent asymmetry.
2. **Quantum dimensions, braiding, ribbon twist.** $[n]_q$, the $R$-matrix,
   the Markov trace, the twist $\theta$. This is where QOU actually lives.
3. **Root-of-unity truncation.** At $q$ a root of unity the *category*
   truncates (tilting modules modulo negligible morphisms → fusion category
   with label set a Weyl alcove at level $k$). That is a **restriction of
   the same lattice to a finite sub-alcove**, not a change of angle or
   curvature. See §5 T4 — this is the one place the dialog's instinct points
   at something real.

**Consequence for the originating question** ("should $u,d$ have $I_3$
$q$-deformed from $\pm\tfrac12$?"): **no.** The $I_3$ eigenvalues are
exactly $\pm\tfrac12$ in $U_q(\mathfrak{su}_2)$; weights are undeformed. The
asymmetry lives in item 1.

## 2. The $\mathrm{SU}(3) \to \mathrm{SU}(2,1)$ claim

The dialog asserts the metric on the root space acquires signature
$(+,+,-)$, "circles become hyperbolas", and the hexagon shatters. This is
wrong for a reason independent of §1: $\mathfrak{su}(2,1)$ and
$\mathfrak{su}(3)$ share the **same complexification** $\mathfrak{sl}(3,
\mathbb C)$, hence the *same* root system, *same* Cartan matrix, *same* $A_2$
hexagon. The Killing form is negative-definite on $\mathfrak k$ and
positive-definite on $\mathfrak p$; on *any* Cartan subalgebra it is
therefore **definite**, not Lorentzian. The $(2,1)$ signature is that of the
Hermitian form on $\mathbb C^3$, not of the root space.

What genuinely changes, and the dialog got right: the $6$ roots split $2$
compact / $4$ non-compact ($\dim\mathfrak k = \dim\mathfrak u(2) = 4$,
$\dim\mathfrak p = 4$); the real rank drops to $1$; the restricted Weyl
group is $\mathbb Z_2$; and there are **no non-trivial finite-dimensional
unitary representations**. That last point is the strongest correct
observation in the whole dialog — but it is a statement about unitarity, not
about lattice geometry.

## 3. The physics claims

| Claim | Verdict |
|---|---|
| Gell-Mann matrix $Y = \tfrac{1}{\sqrt3}\mathrm{diag}(1,1,-2)$ | **Wrong, and self-inconsistent.** $Y = \lambda_8/\sqrt3 = \tfrac13\mathrm{diag}(1,1,-2)$. As written it gives $Y(u) = 1/\sqrt3$, contradicting the dialog's own table two paragraphs later ($Y(u) = +1/3$). |
| Turaev–Viro at a root of unity ⇒ hyperbolic geometry | **Sign error.** TV at a root of unity is Euclidean 3d gravity with $\Lambda > 0$ — *spherical*, not hyperbolic. Cited as support for the hyperbolic conclusion it contradicts. (Also: triangles have angle sum $180^\circ$; tetrahedra do not.) |
| Flux tube / confinement is evidence of hyperbolic geometry | **Inverted.** Pure $AdS_5$ — maximally symmetric, hyperbolic — gives the Maldacena–Rey–Yee **Coulomb** potential $V \sim -c/r$: conformal and explicitly *non*-confining. Confinement requires **breaking** that symmetry (hard wall / soft wall / IR cutoff). The dialog names the IR wall and then credits the result to hyperbolicity. Flux-tube confinement is evidence of *broken* conformal symmetry, i.e. the opposite of the stated inference. |
| $\mathbf 3$ is the standard representation, neither symmetric nor antisymmetric; $\mathbf 3 \otimes \mathbf 3 = \mathbf 6_S \oplus \bar{\mathbf 3}_A$; $Q = I_3 + Y/2$ | **Correct.** |

## 3a. "Hyperbolic ⇒ stability": three different things called negative

A follow-on question asked whether Asselmeyer-Maluga's "both knot
complements have to carry a hyperbolic structure, i.e. a space of constant
negative curvature" means stability, and whether it is "the metric $(+,+,-)$
that ensures time flow and stability". Three distinct objects are being
merged; separating them is what makes the useful part survive.

1. **Hyperbolic 3-manifold.** Constant negative **sectional curvature**,
   with a **Riemannian, positive-definite** metric — signature $(+,+,+)$.
   *Negative curvature is not negative signature.* There is no time
   direction and no light cone in $\mathbb H^3$.
2. **Lorentzian signature $(+,+,-)$.** An **indefinite** metric: light
   cones, causal structure, time flow. A different concept, and not what
   Thurston geometrisation supplies.
3. **The Killing form on a root space** (the $\mathrm{SU}(2,1)$ discussion
   of §2). A third object again — and, per §2, definite on any Cartan
   subalgebra regardless of real form.

So the answer to "is it the $(+,+,-)$ metric that gives stability" is
**no** — nothing in the hyperbolic-knot-complement picture is Lorentzian.

**But the stability instinct is right, for a stronger reason: Mostow
rigidity.** For a complete finite-volume hyperbolic 3-manifold the
hyperbolic structure is **unique up to isometry**; there is no moduli, no
deformation, no drift. Consequently every geometric quantity — in particular
the **volume** — is a *topological* invariant. That is a far sharper
stability statement than any signature argument, and it is already
**load-bearing in QOU**: it is the licence for treating $\mathrm{Vol}(K)$ in
$m(K) = m_e\,\mathrm{Vol}(K)\,\rho(K)/\hbar_q^2$ as an invariant of the knot
rather than of a chosen metric. Mostow is already cited in the corpus (e.g.
[`atom-knot-mass-derivation-proof.md`](../../content/quantum-observable-universe/mass-theory/atom-knot-mass-derivation-proof.md)).

**Where the time-asymmetry instinct does have a real home** — but as an
analogy needing construction, not a derivation: geodesic flow on a
negatively curved manifold is **Anosov**. Anosov flows are *structurally
stable* (the flow as a whole is robust under perturbation) while individual
trajectories diverge *exponentially* (positive Lyapunov exponent), and the
tangent bundle splits into stable and unstable sub-bundles $E^s \oplus E^u$
— contraction in forward time, expansion in backward time. That splitting is
genuinely time-asymmetric, and "stable only with respect to $+$ time flow"
is a fair description of $E^s$. This is the correct referent, and it comes
from **dynamics on** a negatively curved space, not from a metric signature.

**Do not wire this.** No object in the corpus currently instantiates it, and
two further conflations should be resisted explicitly:

- **SDP stability is unrelated.** Stability of an SDP solution is strict
  feasibility / Slater's condition / uniqueness of the optimal face, read
  off the **dual** variables (`y_star`, `active_set`) that this repo already
  requires every LP/SDP witness to emit. It has no connection to sectional
  curvature. Merging the two would be a category error of exactly the kind
  the LP/SDP dual discipline exists to expose.
- **Vortex-tube stability is a topological-invariance claim** (helicity /
  linking number conservation), again not a curvature-signature claim — cf.
  `1508.01458`, where the network is stable because knottedness is
  topologically protected in exactly three spatial dimensions.

## 4. Citations

All six arXiv identifiers were checked and are **real, correctly titled**
(no fabrication — the usual failure mode did not occur here):

| ID | Status |
|---|---|
| [`hep-ph/9612303`](https://arxiv.org/abs/hep-ph/9612303) Klein-Kreisler & Ruiz-Altaba, *The q-deformed quark model* (PRD **61**, 036001) | real; **over-claimed**, see below |
| [`1910.09966`](https://arxiv.org/abs/1910.09966) *Braids, 3-manifolds, elementary particles* (Symmetry **11**, 1298) | real |
| [`1803.04009`](https://arxiv.org/abs/1803.04009) Gang & Yonekura, *Symmetry enhancement and closing of knots in 3d/3d correspondence* (JHEP **07**(2018)145) | real; **homonym error**, see below |
| [`1508.01458`](https://arxiv.org/abs/1508.01458) Berera, Buniy, Kephart, Päs, Rosa, *Knotty inflation* (EPJC **77**, 682) | real |
| [`1911.04486`](https://arxiv.org/abs/1911.04486) Vancea, *Knots and the Maxwell Equations* | real |
| [`1012.5432`](https://arxiv.org/abs/1012.5432) Thompson, *Towards Topological Quantum Computation?* | real |

Two are cited for more than they support:

All six PDFs are in [`library/`](../../library/) (owner upload
[`cba63fa`](https://github.com/litlfred/qou/commit/cba63fa178c9ded661581c11b5a96efadec3bdd7)
plus the pre-existing `9612303v1.pdf`) and the two load-bearing claims below
were checked **against the PDFs**, not the abstracts.

**The $\mathrm{SU}(3)$ in `1803.04009` is a homonym — confirmed from the
source.** Gang–Yonekura's $\mathrm{SU}(3)$ is a **flavour symmetry of a 3d
$\mathcal N=2$ SCFT** obtained by compactifying the **6d $A_1$** $(2,0)$
theory on a knot complement. The simplest instance (their eq. 1.3) is

> $T^{DGG}[M = S^3, K = \text{figure-eight knot}] = $ a $\mathrm U(1)_0$
> vector multiplet coupled to two chiral multiplets of charge $+1$,

whose manifest $\mathfrak u(1)_{\text{top}} \times
\mathfrak{su}(2)_{\text{manifest}}$ enhances to $\mathrm{SU}(3)$, with
$\mathfrak u(1)_{\text{top}}$ the **topological monopole charge** and the
off-diagonal $\mathrm{SU}(3)$ generators supplied by **monopole operators**.
The authors themselves write that these enhancements "are **accidental and
unexpected** from 6d viewpoint." This is not the $u/d/s$ eightfold-way
$\mathrm{SU}(3)$ under any reading: the parent theory is $A_1$, the group
acts on chiral multiplets and monopoles, and the enhancement is accidental.
The dialog asserted it "directly links hyperbolic knot geometry to the exact
$\mathrm{SU}(3)$ structure of the Eightfold Way." Same three letters,
unrelated object — the group-name analogue of the overloaded-symbol failure
mode in [`AGENTS.md` §Conditional-proved](../../AGENTS.md). (Note also that
the paper's $\mathfrak{su}(2)$ criterion runs the *other* way from the
dialog's use: enhancement is expected for **Lens spaces** and *not* expected
when $M$ is hyperbolic.)

**`hep-ph/9612303`: the dialog inverted the paper's conclusion.** This is
the most serious citation failure in the thread. The dialog wrote that the
deformation "provided a way to naturally induce the mass splitting between
the proton and neutron **without having to manually insert explicit
electromagnetic corrections**." The paper says the opposite, in its own
words (§1):

> "contrary to naive expectations, the $q$-deformed $\mathrm{SU}(2)$ of
> isospin **cannot accommodate the large mass difference of pions without
> invoking explicit electromagnetic corrections**"

and in the abstract: "everything **fits** with experimental data. We find,
nevertheless, that it is **impossible** to parametrize successfully the
large mass difference between the charged and neutral pions with the single
$q$ of $U_q(s\ell(2))$." So $q$ is a **fitted** parameter, and the paper's
headline result is a **negative**. Trading a *computed* EM correction for a
*fitted* $q$ is a reparametrisation, not a derivation. Under the repo's
anti-fit discipline this is a **cautionary precedent, not support** — and it
is a direct precedent for the "no seventh fit-based ansatz" rule: a
one-parameter $q$-fit that works on the nucleons and fails on the pions is
exactly the failure signature that rule exists to catch.

## 5. Every "in QOU" statement in the dialog is invented

The dialog has no corpus access. It fabricated: production of matter by
$\gamma\gamma$ from trivial knots via $\bowtie_K$; $\bar{\mathbf 3}$ as a
mirror knot; a requirement that $q \bowtie_K \bar q$ "decompose into exactly
9 allowable knot configurations"; and hyperbolic knot complements supplying
an AdS bulk "so QOU does not need a 5th dimension". None of these are corpus
constructions. Three are actively contradicted:

1. **The hyperbolic-bulk claim collapses at low crossing number.** The
   unknot and every torus knot have hyperbolic volume $0$. The electron knot
   is the trefoil $T_{2,3}$ — Seifert-fibered, **non-hyperbolic** — as
   already recorded in
   [`2026-06-16-hyperbolic-hurdle-dialog-assessment.md`](2026-06-16-hyperbolic-hurdle-dialog-assessment.md),
   where this is flagged as the *recurrent* dilog re-pitch failure mode. If
   the photon is the unknot, the proposed "hyperbolic bulk" is empty exactly
   where the dialog starts.
2. **It contradicts a proved theorem.** The dialog places $\mathrm{SU}(3)$
   inside single-fibre structure. Per
   [`sm-gauge-truncation.md`](../../content/quantum-observable-universe/appendix-standard-model/sm-gauge-truncation.md),
   $\mathrm{Aut}^\otimes(\tau)$ of a *single* QOU fibre is **exactly**
   $\mathrm{SU}(2)$ (or its split real form) — proved. Any $\mathrm{SU}(3)$
   must be groupoid-level: multi-strand, framing, or inter-fibre.
3. **The corpus is harsher on itself than the dialog is.**
   [`sm-open-problems.md`](../../content/quantum-observable-universe/appendix-standard-model/sm-open-problems.md)
   records $Y$ as *"open: writhe map falsified"*, $\mathrm{SU}(3)$ as
   *"open: no construction; octonion fragments only"*, freeze-out as
   *"open: heuristic, no derivation"*, and three generations as *"open …
   nowhere addressed"*.

## 6. Formalisation targets — what would make this derivative of QOU

Organising principle: a result is *derivative of QOU* only if forced by the
substrate data $(q_0, \mathbf H_n(q), \tau)$ **with no new adjustable
input**. Each target below names the missing object and the battery it must
pass. Ordered by leverage-per-cost.

### T1 — Weyl-invariance of the $q$-deformation (cheap; closes this thread)

Prove in Lean, over a generic `[CommRing R]` (wall-side clean, no `ℝ`):

- `qSerreCoeff 2 1 q = qInt 2 q` — the quantum Serre coefficient **is** the
  Gaussian binomial $\binom{2}{1}_q$;
- the $A_2$ Cartan matrix, root lattice and Weyl group carried by
  $U_q$ are **independent of $q$**.

Value: a scope-(b) exclusion that prunes an entire re-pitch family ("$q$
curves the flavour lattice", "$q$ makes angles imaginary", "$q \Rightarrow
\mathrm{SU}(2,1)$") before anyone runs a search. This is precisely the
formalize-first prune of [`compute-author.md` §3.3](../../.claude/skills/local/compute-author.md).
Finite combinatorics; no archimedean content.

### T2 — the second crossing invariant (hypercharge) — **sharpest target**

The corpus's own #1 open item, and the only thing between QOU and a derived
$\mathrm U(1)_Y$. The Lean already proves the *factorisation criterion* ($Y$
factors through $w$ iff constant on writhe fibres). The open side is
**existence**.

Concrete handle the corpus has not yet exploited: on a framed link,
$\mathrm{Sl} = w + \mathrm{tw}$ — writhe and twist are exactly the two
independent components of the self-linking number. QOU's Hecke category is
**already ribbon**: the twist $\theta_\lambda$ acts by a scalar
$q^{c_\lambda}$ set by the content/framing anomaly. So the target is:

> prove the ribbon twist eigenvalue supplies a gauge-orbit-invariant,
> writhe-independent datum on knot states,

which would be derivative *by construction* — $\theta$ is part of the
braided-ribbon data $\tau$ already carries, not an import. It must then pass
the two batteries already stipulated in
[`sm-hypercharge-invariant.md`](../../content/quantum-observable-universe/appendix-standard-model/sm-hypercharge-invariant.md):
Gell-Mann–Nishijima against the derived $Q = w/2$ on the nucleon doublet,
and the first-generation $Y$ spectrum with its $\mathbb Z_6$ relations. A
**negative** — proof that no such invariant exists from strand data alone —
is equally valuable and would be a genuine scope-(b) exclusion.

> **Literature upgrade found in the uploads (2026-08-03).** `1910.09966` §5
> is *this exact route*, and is a materially stronger precedent than the
> Bilson-Thompson helon model the corpus currently cites "without
> endorsement". Its section titles are §5.1 *Electric Charge as Dehn Twist
> of the Boundary*, §5.2 ***Electric Charge as a Frame of the Knot
> Complement***, §5.3 *The Charge Spectrum*, §5.4 *Vanishing of the Magnetic
> Charge and Quasimodularity*. It reports obtaining the charge spectrum
> $\pm\tfrac13, \pm\tfrac23, \pm 1$ in units of $e$, with the factor
> $\tfrac13$ attributed to **4-dimensional topology (Hirzebruch signature
> theorem)** — i.e. *derived* rather than assigned, which is precisely the
> discriminator the corpus demands. Read §5 before writing T2; if the
> construction survives the two batteries it is the shortest path to a
> derived $\mathrm U(1)$, and if it fails, *why* it fails is the sharpest
> available constraint on the missing invariant.

### T2a — a conflict to resolve first: is the electron knot hyperbolic?

`1910.09966` assigns **fermions to hyperbolic knot complements and bosons to
torus bundles**. QOU takes the electron knot to be the trefoil $T_{2,3}$,
which is a **torus** knot — Seifert-fibered, non-hyperbolic, volume $0$ (the
recurrent failure mode recorded in
[`2026-06-16-hyperbolic-hurdle-dialog-assessment.md`](2026-06-16-hyperbolic-hurdle-dialog-assessment.md)).
Under Asselmeyer-Maluga's classification the QOU electron would land on the
**boson** side. Either the assignment differs for a stated reason, or one of
the two schemes is wrong. This is cheap to settle and worth settling before
importing anything from that paper — including the §5 charge construction,
which is stated for hyperbolic complements.

### T3 — $\mathrm{SU}(3)$ colour: run the dimension battery *first*

> **⚠ Superseded in part (2026-08-03, same day).** The battery was run. The
> claim below — *no $\mathbf 8\oplus\mathbf 1$ in the Wedderburn
> decomposition of $\mathbf H_3(q)$* — is literally true but **points at the
> wrong object**: the Hecke blocks are the *multiplicity spaces*, and at
> $N=3$ they are exactly the multiplicities $(1,2,1)$ of the baryon
> decuplet / octet / singlet. Read
> [`2026-08-03-flavour-su3-schur-weyl-obstruction.md`](2026-08-03-flavour-su3-schur-weyl-obstruction.md)
> instead: the real obstruction is that QOU's fibre has $\dim V = 2$, so the
> $(1^3)$ block *drops entirely*, and the corpus's two candidate 3-objects
> are respectively Elliott's $\mathrm{SU}(3)$ (a homonym) and an icosahedral
> triple excluded by the $\mathrm{Sym}^2$ test.

Constrained by the proved $\mathrm{SU}(2)$-emergence theorem to live at
groupoid level. Before constructing anything, state and check where the
adjoint $\mathbf 8$ is supposed to sit. Note the immediate obstruction:
$\dim \mathbf H_3(q) = 3! = 6$, with Wedderburn blocks
$\lambda \in \{(3),(2,1),(1^3)\}$ of dimensions $1,2,1$ — so
$1^2 + 2^2 + 1^2 = 6$. There is **no $\mathbf 8 \oplus \mathbf 1$ in the
block decomposition of $\mathbf H_3(q)$.** Any proposal must name the
categorical object carrying the $\mathbf 8$ and check its dimension before a
line of compute is written.

### T4 — the truncation ("freeze-out") mechanism

The corpus calls this *"a heuristic with no derivation"*. The canonical
mathematical truncation with the right shape is the **root-of-unity
quotient** (§1a item 3): tilting modules modulo negligible morphisms, label
set a Weyl alcove at level $k$. That is a rigorous freeze-out, not a
metaphor — this is the one place the dialog's instinct points somewhere
real.

**Named obstruction, stated up front:** $q_0 \approx 1.10998$ is **real, not
a root of unity**, and at real $q > 1$ there is *no* truncation
($\mathrm{Rep}\,U_q \simeq \mathrm{Rep}\,\mathfrak g$, semisimple, same
characters).

**This is better-scaffolded than "heuristic" suggests.** The corpus already
states the required saddle-sorting as a conditional proposition:
[`phi-q-aj-machinery-identification`](../../content/quantum-observable-universe/stochastic-mechanics/phi-q-aj-machinery-identification.md)
identifies $\Phi_q$ (Faddeev) as the **root-of-unity saddle**
($q = e^{2\pi i/N}$) and $\mathrm{Li}_2^q$ (Rogers) as the **real saddle**
($q \in (0,1)$) of the *same* AJ object $\hat A_K(\hat L, \hat M; q)$,
algebraic over $\mathbb Z[q^{\pm1}]$ on both sides — "the two contexts
differ only by the choice of archimedean saddle." That is precisely the
fibre/observable split of [`AGENTS.md` §Im(q) at fibre vs observable
level](../../AGENTS.md), already written down. Honest target: either
**(i)** show the truncation consequence follows at the root-of-unity saddle
and survives transport to the real saddle — which would *derive* the
freeze-out — or **(ii)** show it cannot, converting "heuristic" into a
stated impossibility and forcing a different mechanism. **Wire nothing until
(i) or (ii)**, and note that the enabling proposition is itself conditional
on two conjectures, so (i) would be conditional-proved, not proved
(§Conditional-proved ≠ premise-established).

### T5 — mass/binding: a no-free-parameter certificate

The ledger entry is *"Mass hierarchies from morphism amplitudes | open: must
reduce to the canonical volume–density / Hecke-energy mass chain"*. The
formalisable content is a **conservation-of-inputs theorem**: that the map
(3 calibration inputs) → (predicted observable) admits no additional free
parameter, i.e. `predict obs` is a closed term containing no numeric literal
not traceable either to a CODATA-tagged calibration or to a proved
categorical constant. This is mechanically checkable, and it is *the* thing
that distinguishes "derivative" from "fitted". Half-built already: the
`canonical_mass` facade plus the hidden-CODATA-literal rollup (bean `46ke`,
53 scripts) are the two existing pieces.

### T7 — the $q$-hyperbolic structure deforming under $\bowtie_K$

Proposed in session: *"what we need is a $q$-hyperbolic structure that
deforms following the Reeb flow according to the knot-particle operation
under $\bowtie_K$"*, with the observation that this *should be implicit in
non-abelian Stokes + the Frobenius pairing, but is worth calling out*. That
reading is correct, and the call-out is worth making because **two of the
three pieces already exist in the corpus and the third is a named published
object that is not yet cited anywhere.**

**What is already there.**

- *The deformation space itself.* Mostow rigidity says the **complete**
  hyperbolic structure cannot deform (§3a) — so the deformation necessarily
  lives in the space of **incomplete** structures, Thurston's Dehn-surgery
  space, coordinatised by **cusp/boundary-torus data** with the
  Neumann–Zagier symplectic form on $H^1(\partial M)$. The corpus already
  carries this:
  [`cusp-shape-bar-parity`](../../content/quantum-observable-universe/braids-and-knots/cusp-shape-bar-parity.md)
  works with the $4_1$ cusp shape $\omega = e^{i\pi/3}$ and the
  Neumann–Zagier complex volume $\mathfrak V = \mathrm{Vol} + i\,\mathrm{CS}$.
- *Its $q$-deformation.* The quantisation of that boundary-torus symplectic
  structure gives $q$-commuting meridian/longitude operators and hence the
  **quantum $A$-polynomial** — which the corpus already states as
  [`phi-q-aj-machinery-identification`](../../content/quantum-observable-universe/stochastic-mechanics/phi-q-aj-machinery-identification.md),
  $\hat A_K(\hat L, \hat M; q)\cdot J_N(K;q) = 0$. So "the $q$-deformed
  hyperbolic deformation structure" is **not a new object to invent**: it is
  $\hat A_K$.

**Why it is "implicit in NA-Stokes + Frobenius" — and where that is not
enough.** Non-abelian Stokes supplies holonomy-along-a-flow (the
multiplicative integral of a connection), and the Frobenius pairing
$\mathrm{tr}_M = \sum_\lambda y_\lambda \chi_\lambda$ supplies the knot
invariant. Together those give the $q$-side. But they yield a **number per
knot**, whereas the deformation space is the **annihilator** of the family
$\{J_N\}$ — a different object, reached only through the $q$-holonomic
(AJ) step. Calling this out explicitly is the substance of the proposal: the
trace is not the variety, and the bridge between them is exactly the block
the corpus already has. The hyperbolic structure enters the trace only
*asymptotically* (volume-conjecture regime), which is why the saddle-sorting
of T4 is load-bearing rather than cosmetic.

**The genuinely missing piece: the Reeb side.** The corpus has figure-eight
Reeb machinery
([`figure-eight-reeb-rotation`](../../content/quantum-observable-universe/braids-and-knots/figure-eight-reeb-rotation.lean))
but nothing ties Reeb dynamics to $\hat A_K$. The published object that does
exactly this is **knot contact homology** — the Legendrian/Reeb-orbit theory
of the unit conormal torus $\Lambda_K \subset ST^*\mathbb R^3$ (Ekholm–
Etnyre–Ng–Sullivan) — whose **augmentation polynomial** recovers the
$A$-polynomial (Ng) and whose $Q$-deformation is the Aganagic–Vafa
augmentation polynomial. *That* is literally "a $q$-deformed hyperbolic
deformation structure indexed by Reeb flow". Target: identify the corpus's
$\hat A_K$ with the augmentation polynomial of $\Lambda_K$, which would make
the Reeb flow the deformation parameter rather than a separate structure.
Not yet cited anywhere in the corpus — checked.

**Named obstruction on the $\bowtie_K$ half.** Functoriality is the hard
part and it has a concrete failure mode to design around: **connected sums
are never hyperbolic.** $S^3 \setminus (K_1 \# K_2)$ contains an essential
annulus, hence is not atoroidal, hence admits no complete hyperbolic
structure. So if $\bowtie_K$ contains connected sum, a "$q$-hyperbolic
structure deforming under $\bowtie_K$" fails at its base case. Two honest
routes: restrict $\bowtie_K$ to operations that preserve hyperbolicity
(Dehn filling, satellite/cabling with hyperbolic pieces — for which
$A$-polynomial behaviour is studied), or move the claim down to the
**geometric-decomposition** level, where volume *is* additive over the JSJ
hyperbolic pieces even when the total is not hyperbolic. The second is
weaker but survives connected sum, and is the one compatible with the
corpus's existing volume-additivity usage. State which before building.

**Do not wire.** T7 is a research target with one conditional proposition,
one un-cited literature bridge, and one unresolved obstruction. It is
recorded here so the next agent does not re-derive the framing from scratch.

### T6 — three generations

*Open: nowhere addressed.* Downstream of T2/T3 — a generation count is not
attackable before the gauge factors exist. Do not start here.

## 7. Recommendation

T1 now (cheap, and it retires this re-pitch class permanently). T2 next — it
is the corpus's own top open item and the ribbon-twist handle is a genuine
un-exploited lead. T3 only after its dimension battery is written down. T4
gated on the root-of-unity question being settled either way. T5 is
incremental and tractable. T6 not yet.

Nothing in the dialog changes any production compute.

## 8. Papers to obtain next

All six dialog citations are already in [`library/`](../../library/)
(`9612303v1`, `1012.5432v4`, `1508.01458v1`, `1803.04009v2`, `1910.09966v1`,
`1911.04486v4`). The following are **not** in the dialog — they surfaced
from `1910.09966`'s own bibliography and are closer to QOU's actual
machinery than four of the six papers the dialog cited.

| Want | Why it matters here |
|---|---|
| **Gavrilik**, *Quantum algebras in phenomenological description of particle properties*, Nucl. Phys. B (Proc. Suppl.) **102/103** (2001) 298 — [`hep-ph/0103325`](https://arxiv.org/abs/hep-ph/0103325) | **Highest priority.** The only $q$-deformed-flavour line that is genuinely on-topic: $q$ of $\mathrm{SU}_q(n)$ is tied to the **flavour mixing (Cabibbo) angle**, and **torus knots as 2-braids are associated with vector mesons of different flavours**. Directly touches the corpus's [`sm-params-ckm.md`](../../content/quantum-observable-universe/appendix-standard-model/sm-params-ckm.md), and is the eightfold-way-adjacent $q$-deformation the dialog was groping for. Check carefully whether $q \leftrightarrow \theta_C$ is *derived* or *fitted*. |
| **Finkelstein**, *Knots and Preons*, Int. J. Mod. Phys. A **24** (2009) 2307 — [`0806.3105`](https://arxiv.org/abs/0806.3105) | Particle model built from **knots represented by quantum groups** — the closest published analogue to QOU's own construction. Worth reading for what it does with $\mathrm{SU}_q(2)$ representation labels vs. knot invariants. |
| **Bilson-Thompson**, *A Topological Model of Composite Preons* — [`hep-ph/0503213`](https://arxiv.org/abs/hep-ph/0503213) | Already cited in [`sm-hypercharge-invariant.md`](../../content/quantum-observable-universe/appendix-standard-model/sm-hypercharge-invariant.md) as the ribbon-twist precedent, but apparently not read into `library/`. Needed to evaluate T2 against its stated precedent. |
| **Bilson-Thompson, Markopoulou, Smolin**, *Quantum Gravity and the Standard Model*, Class. Quant. Grav. **24** (2007) 3975 — [`hep-th/0603022`](https://arxiv.org/abs/hep-th/0603022) | The braided-ribbon → SM-charge construction in its developed form; the natural adversarial comparison for T2. |

Lower priority, only if T4 (root-of-unity truncation) is pursued: a standard
reference on **tilting modules and the negligible-morphism quotient** at a
root of unity (Andersen; Sawin, *Quantum groups at roots of unity and
modularity*, [`math/0308281`](https://arxiv.org/abs/math/0308281)) — needed
to state the Weyl-alcove truncation precisely enough to prove (i) or (ii).
