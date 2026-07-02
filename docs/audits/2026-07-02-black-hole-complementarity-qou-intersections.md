# Black-hole complementarity × QOU — five-paper intake review + the STU postulates

**Date:** 2026-07-02
**Branch:** `claude/expand-emc-q2-formula-e9r9oc`
**Status of sources:** the five PDFs are queued for fetch on a normal-network
machine (`uploads/black-hole-complementarity-batch/intake.json`); this sandbox's
network policy is github-only (arxiv.org CONNECT 403 via `paper-search-mcp`,
`curl`, and `WebFetch`). The per-paper reviews below are therefore from model
knowledge of these well-known papers and are **not machine-validated against
the fetched PDFs**. Quotations of the STU postulates are close paraphrases,
to be checked against the PDF on intake. arXiv:1810.11563 could not be
identified from this sandbox and is deliberately **not** reviewed or
registered (no fabricated metadata); it is queued for identification.

Corpus grounding: all QOU-side claims below were checked against the corpus
(sweep over `content/`, `docs/`, `computations/`). **No existing block
mentions black-hole complementarity, the stretched horizon, or
`e^S` microstate counting** — the `complementar*` grep hits are SDP strict
complementarity (unrelated). The blocks cited below are the closest
load-bearing structures.

---

## 1. Per-paper review

### 1.1 Susskind–Thorlacius–Uglum, *The Stretched Horizon and Black Hole Complementarity* (hep-th/9306069; `susskind1993`)

Introduces **black hole complementarity** via three postulates (§2 of the
paper, paraphrased):

- **P1.** The formation and evaporation of a black hole, as viewed by a
  distant observer, can be described entirely within standard quantum
  theory; in particular there exists a unitary S-matrix from infalling
  matter to outgoing (Hawking-like) radiation.
- **P2.** Outside the stretched horizon of a massive black hole, physics is
  described to good approximation by semiclassical field equations.
- **P3.** To a distant observer, a black hole appears to be a quantum system
  with discrete energy levels; the dimension of the subspace of states
  describing a black hole of mass $M$ is $\exp S(M)$, the exponential of
  the Bekenstein entropy.

The **stretched horizon** is a timelike membrane roughly one Planck length
above the true horizon which, for the exterior description, is a physical
system that absorbs, thermalizes, and re-emits information. The infalling
observer crosses the true horizon without incident (equivalence principle).
The two descriptions duplicate information, but no single observer can
verify the duplication — complementarity is protected operationally, not
kinematically.

### 1.2 Susskind–Thorlacius, *Gedanken Experiments Involving Black Holes* (hep-th/9308100; `susskindthorlacius1994`)

The consistency check for 1.1 against quantum no-cloning. An exterior agent
must wait of order the information-retention (Page) time $\sim M^3$ to
extract one bit from the radiation before jumping in; the interior copy can
then reach her before the singularity only if the infalling system signals
with super-Planckian energy (growing like $e^{c M^2}$ in Planck units). No
observer ever operationally witnesses a clone, so the postulates are not
falsifiable by any gedanken experiment of this class. This is the original
"decoding-time censor" argument, sharpened twenty years later by
Harlow–Hayden (1.4).

### 1.3 Marolf, *The Black Hole information problem: past, present, and future* (1512.04993; `marolf2017`)

A taxonomy review. The passage the author quoted defines **standard
complementarity**: a *single* Hilbert space with exact unitary evolution;
each observer is embedded with, per time slice, a set of operators that
approximately commute; the semiclassical interpretation of an operator is
observer-dependent, so a degree of freedom "inside" for one observer can be
"outside" for another (the viewpoint of 't Hooft and of
Susskind–Thorlacius–Uglum). This contrasts with *strong* complementarity
(a Hilbert space per observer). Marolf's central tension is the nice-slice
argument: low-energy effective field theory on nice slices implies the
information stays inside unless local QFT breaks down somewhere it
"shouldn't."

### 1.4 Harlow–Hayden, *Quantum Computation vs. Firewalls* (1301.4504; `harlowhayden2013`)

The AMPS firewall experiment requires the infalling observer to first
distill, from the early radiation $R$, the purification of a near-horizon
mode $B$. Harlow–Hayden argue this distillation is a quantum computation of
circuit complexity generically **exponential in the black-hole entropy**,
so it cannot be completed before the hole evaporates: the entanglement
conflict ($B$ with the interior vs $B$ with $R$) is never operationally
exhibited. Computational complexity acts as the censor protecting
complementarity — the modern quantitative descendant of 1.2.

### 1.5 arXiv:1810.11563 — queued for identification

Not reviewed: title/authors could not be verified from this sandbox and
guessing citation metadata is worse than waiting one fetch cycle. Action
item in `uploads/black-hole-complementarity-batch/intake.json`.

---

## 2. Does QOU fit Marolf's "standard complementarity"? — Yes

The author's question: does QOU instantiate the single-Hilbert-space
picture? Point for point:

| Standard-complementarity ingredient (Marolf §"two proposals") | QOU realisation |
|---|---|
| One Hilbert space | Markov-trace GNS space: $H_\infty(q)$ carries a unique tracial state $\mathrm{tr}_M$ in the Wenzl-positive window, and GNS gives a single separable $\mathcal{H}$ with faithful $*$-representation — [`algebraic-gns-embedding`](../../content/quantum-observable-universe/observations/algebraic-gns-embedding.md) |
| Exact unitary evolution | braid/R-matrix evolution in the one algebra; dagger-unitarity (the `su2-emergence-dagger-unitarity` chain in `models-of-qous/`) |
| Per-observer, per-time-slice operator sets that approximately commute | an observer is a configuration in $\mathrm{Bun}^{\circ}$ ([`observable-subcategory`](../../content/quantum-observable-universe/information-theory/observable-subcategory.md)); its accessible operators are the subalgebra reachable by *finite braid computation* from its chart; spacelike-separated frames approximately commute by the Lieb–Robinson cone $|Z| = c_q$ ([`information-causality`](../../content/quantum-observable-universe/information-theory/information-causality.md)) |
| Observer-dependent semiclassical interpretation; inside-for-one is outside-for-another | per-observer computational time ([`computational-spacetime-observer`](../../content/quantum-observable-universe/information-theory/computational-spacetime-observer.md)): what is degree-$0$ semantic data in one frame is beyond finite derivability from another; the inside/outside split is **provability-relative** |

So QOU is a *standard*-complementarity model, not a strong one — with one
structural novelty: where STU make the inside/outside split geometric
(stretched horizon), QOU makes it **arithmetic** (Gödel/finite-derivability,
[`incompleteness-implies-horizon`](../../content/quantum-observable-universe/information-theory/incompleteness-implies-horizon.md)).
The 't Hooft lineage the author pointed at is already in the corpus as the
beable dictionary
([`observable-beable-correspondence`](../../content/quantum-observable-universe/information-theory/observable-beable-correspondence.md)):
beable algebra $\leftrightarrow$ degree-$0$ algebra $\Gamma(\mathcal{S}, A_0)$,
superselection sectors $\leftrightarrow$ aeons $\pi_0(\mathrm{Bun}^{\circ})$.

There is also a precise **stretched-horizon analogue**: the degree-$1$
quotient sheaf on the horizon. $\Gamma(\mathcal{H}, A_1/A_0)$ is a surface
layer with real exterior dynamics — it carries the thermal winding modes
(temperature $\sim \eta_q$), absorbs degree-$0$ identity, and re-emits only
degree-$\geq 1$ data
([`hawking-radiation`](../../content/quantum-observable-universe/information-theory/hawking-radiation.md),
[`jet-horizon`](../../content/quantum-observable-universe/information-theory/jet-horizon.md)).
That is functionally STU's membrane: a physical thermalizing skin *for the
exterior observer*, absent for the global (semantic) description.

---

## 3. The three postulates, mapped

### 3.1 P2 (semiclassical exterior) — a QOU **consequence** ✓

The horizon ideal $\mathfrak{h} \subset A_0$ constrains only restrictions to
$\mathcal{H} = V(\mathfrak{h})$. Outside, $A_0 \neq 0$ (the configuration is
in $\mathrm{Bun}^{\circ}$) and the full jet tower is unconstrained: degree-$1$
transport (winding) and degree-$2$ curvature (linking) give the semiclassical
field content, and $q \to 1^{+}$ recovers the classical/entropic-gravity
limit ([`entropic-gravity`](../../content/quantum-observable-universe/observations/entropic-gravity.md)).
The author's instinct is right: P2 needs no new axiom in QOU.

### 3.2 P1 (unitary exterior S-matrix) — **splits**; only half is currently a consequence ⚠

- **P1a — exact unitary global evolution in one Hilbert space: consequence.** ✓
  (GNS + R-matrix unitarity, §2 table rows 1–2.)
- **P1b — the exterior record is complete** (the S-matrix restricted to
  infalling-matter $\to$ outgoing-radiation data is unitary, i.e. the
  radiation carries the information): **not currently a QOU claim — the
  corpus as written denies it.**
  [`information-paradox-incompleteness`](../../content/quantum-observable-universe/information-theory/information-paradox-incompleteness.md)
  explicitly selects "preserved but inaccessible" (Gödel: true but
  unprovable from outside), and
  [`hawking-radiation`](../../content/quantum-observable-universe/information-theory/hawking-radiation.md)
  states the radiation "carries no information about the internal state."
  Read strictly that is Hawking's 1976 position, and for the *exterior*
  observer it makes evolution non-unitary (thermal) — in Marolf's taxonomy
  that is a remnant/hidden-sector answer wearing complementarity
  kinematics.

**Minimal repair (proposed): the witness-completeness conjecture.**

> **Conjecture (witness completeness / exterior unitarity).** For a jet
> horizon $\mathcal{H}$ of finite lifetime, the map from the trapped
> degree-$0$ section data to the *total accumulated* degree-$\geq 1$ witness
> stream across $\mathcal{H}$ (all of $\Gamma(\mathcal{H}_t, A_k/A_0)$,
> $k \geq 1$, integrated over the evaporation) is injective on the physical
> state space.

With this, QOU lands exactly on the Harlow–Hayden position: the information
**is** in the record (P1b holds), and what the computational horizon blocks
is *decoding*, not existence. Note the corpus's own third-row option in the
paradox table ("partial witnesses accumulate toward a proof that never
terminates") is precisely this conjecture's mechanism; the block currently
*rejects* that row. Verdict on the author's "first two are QOU
consequences": **P2 yes; P1 only as P1a**, or in full after adopting
witness completeness. This is a scope-limited reading of the current
corpus text, not a structural exclusion — one conjecture block flips it.

### 3.3 P3 (discrete levels; $\dim = e^{S}$) — precise QOU analogue ✓ (conjecture-ready)

**Discrete levels: consequence.** Energy is crossing energy quantized in
Planck steps $t_P(q) = q/(q-1)$
([`discrete-planck-step`](../../content/quantum-observable-universe/information-theory/discrete-planck-step.md)),
and mass is $\mathfrak{m}(K) = \mathrm{tr}_M(\beta_K) \cdot E_0$ over
discrete braid closures — the spectrum seen by a distant observer is
discrete, with $E_{\mathfrak{H}} = \mathfrak{m}_{\mathfrak{H}} c_q^2$,
$c_q = 1/(q-1)$
([`mass-energy-equivalence`](../../content/quantum-observable-universe/information-theory/mass-energy-equivalence.md)).

**Dimension counting.** Two corpus ingredients must be composed, and the
composition is the precise analogue:

1. The horizon **mode space**: $S_{\mathrm{BH}} = \dim \Gamma(\mathcal{H}, A_1/A_0)$
   — entropy as the *linear* dimension (rank) of the degree-$1$ jet space on
   the horizon surface; the area $A$ *is* that rank
   ([`information-paradox-incompleteness`](../../content/quantum-observable-universe/information-theory/information-paradox-incompleteness.md),
   [`hawking-radiation`](../../content/quantum-observable-universe/information-theory/hawking-radiation.md)).
2. The horizon **state count**: the $q$-dimension partition block
   ([`lqg-entropy-qdim-partition-pole`](../../content/quantum-observable-universe/gravity-spacetime/lqg-entropy-qdim-partition-pole.md)):
   per-puncture $Z_1(s) = \sum_j [2j+1]_q\, e^{-s\, \tau(C_q(V_j))}$, horizon
   generating function $(1 - Z_1(s))^{-1}$ with pole at $Z_1(s_\star) = 1$,
   entropy density $s_\star$, Immirzi-style calibration
   $\gamma = s_\star/2\pi$ reproducing $S = A/4\ell_P^2$.

Item 1 counts **modes** (punctures), item 2 counts **states per mode
configuration**. A mode space of rank $n \propto A$ whose punctures carry
$[2j+1]_q$-dimensional labels spans a state space of $q$-dimension
$e^{s_\star A}$ at the pole. That composition is STU P3:

> **Conjecture (QOU black-hole state counting — STU P3 analogue).** Let
> $\mathcal{H} = V(\mathfrak{h})$ be a jet horizon in an archimedean QOU at
> substrate $q_0$, with mode rank
> $A = \dim \Gamma(\mathcal{H}, A_1/A_0)$. Let
> $\mathcal{H}^{\mathrm{ext}}_{\mathrm{BH}}$ be the GNS closure, under
> $\mathrm{tr}_M$, of the exterior horizon-mode algebra: the span of
> trace-closed puncture labelings $(V_{j_1}, \ldots, V_{j_n})$ of
> $\Gamma(\mathcal{H}, A_1/A_0)$ subject to the Markov trace-closure (Gauss)
> constraint $\sum_p m_p = 0$. Then its quantum dimension satisfies
>
> $$
> \dim_q \mathcal{H}^{\mathrm{ext}}_{\mathrm{BH}}
> \;=\; e^{s_\star A}
> \;=\; \exp S(M),
> \qquad
> \sum_j [2j+1]_{q_0}\, e^{-s_\star\, \tau(C_{q_0}(V_j))} = 1,
> $$
>
> where $M = \mathrm{tr}_M(\beta_{\mathcal{H}}) \cdot E_0$ is the mass a
> distant observer assigns and $S(M)$ its Bekenstein entropy under
> $\gamma = s_\star / 2\pi$.

Two QOU-specific refinements that STU cannot state:

- **P3 counts the exterior sector only — definitionally.** The interior
  degree-$0$ section space is invisible to the count:
  $\dim \Gamma(\mathcal{H}, A_0) = 0$ from outside, while the sections
  exist semantically (Gödel: existence without provability). QOU therefore
  splits P3 into **P3-ext** (the conjecture above — witnessable states,
  $= e^{S}$) and **P3-int** (the uncounted Gödelian core). This dissolves
  the perennial ambiguity in P3 ("is $e^S$ the number of microstates or of
  exterior-distinguishable states?"): in QOU it is the latter, by
  construction.
- **"Dimension" is quantum dimension.** What the Markov trace counts on a
  braided object is $\dim_q$, not vector-space dimension. At real
  $q_0 \approx 1.11$ these differ; the conjecture is stated in $\dim_q$
  and the identification with STU's Hilbert-space dimension is part of
  what a proof must supply (see flags, §5).

### 3.4 ST94 gedanken + Harlow–Hayden — the QOU decoding censor

The no-cloning defense maps cleanly. In QOU, verifying duplication means
completing a braid computation that extracts a degree-$0$ identity from the
exterior record; the computational-horizon bandwidth bound
$t \geq \frac{c \log 3}{\mathfrak{B}(q)}\, 3^{\,c - c_0}$
([`computational-horizon`](../../content/quantum-observable-universe/information-theory/computational-horizon.md)),
with $\mathfrak{B}(q_0) \approx 82$ $q$-bits/Planck-step
([`information-bandwidth`](../../content/quantum-observable-universe/information-theory/information-bandwidth.md)),
is exponential in the crossing complexity — the same shape as
Susskind–Thorlacius's $e^{cM^2}$ signal bound and Harlow–Hayden's
$e^{S}$ distillation complexity. Bridge, stated once: **HH say decoding is
exponentially hard; QOU as written says stronger — not finitely derivable
at all** (incompleteness, not complexity). The stronger claim is exactly
what makes P1b fail (§3.2); adopting witness completeness retreats QOU to
the HH position, where the gedanken defense still goes through on the
bandwidth bound alone.

$E = \mathfrak{m} c_q^2$ tie-in (this branch's original theme): the censor
and the energetics share the constant — $\mathfrak{B}(q) = q\,\eta_q/(q-1)^2 = c_q^2\, q\, \eta_q$,
so the same $c_q^2 \approx 83$ that amplifies mass into crossing energy
sets the exterior decoding bandwidth. Mass–energy conversion and
information leakage rate are the one constant seen twice.

---

## 4. Summary table

| STU postulate | QOU status | Carrier |
|---|---|---|
| P1a global unitarity | consequence ✓ | GNS + R-matrix ([`algebraic-gns-embedding`](../../content/quantum-observable-universe/observations/algebraic-gns-embedding.md)) |
| P1b exterior record complete | **open — corpus currently denies it**; repair = witness-completeness conjecture (§3.2) | [`information-paradox-incompleteness`](../../content/quantum-observable-universe/information-theory/information-paradox-incompleteness.md) |
| P2 semiclassical exterior | consequence ✓ | [`jet-horizon`](../../content/quantum-observable-universe/information-theory/jet-horizon.md) + $q \to 1$ limit |
| P3 discrete levels | consequence ✓ | Planck-step quantization + $\mathrm{tr}_M$ mass |
| P3 $\dim = e^{S}$ | precise analogue, conjecture-ready (§3.3) | [`lqg-entropy-qdim-partition-pole`](../../content/quantum-observable-universe/gravity-spacetime/lqg-entropy-qdim-partition-pole.md) × degree-$1$ mode rank |
| stretched horizon | present as $\Gamma(\mathcal{H}, A_1/A_0)$ | [`hawking-radiation`](../../content/quantum-observable-universe/information-theory/hawking-radiation.md) |
| no-cloning censor (ST94/HH13) | present, *stronger form* | [`computational-horizon`](../../content/quantum-observable-universe/information-theory/computational-horizon.md) bandwidth bound |

---

## 5. Critical-distance flags (standing red-team license)

1. **The Hawking-1976 sentence will draw referee fire.**
   [`hawking-radiation`](../../content/quantum-observable-universe/information-theory/hawking-radiation.md)'s
   "the radiation carries no information about the internal state" is
   contradicted by the post-2019 consensus (Page curve from replica
   wormholes). QOU can keep its Gödel-hiding position, but the block should
   say *whose* description the sentence lives in (exterior finite-derivability),
   or adopt witness completeness. As written it reads as a physics claim
   the field considers settled the other way.
2. **The $\gamma = s_\star/2\pi$ calibration is Immirzi-shaped.** The match
   to $S = A/4$ in the LQG block spends one calibration constant, exactly as
   LQG spends the Immirzi parameter. Fine — but do not present P3-ext as
   parameter-free until $s_\star$ is derived from the substrate.
3. **$\dim_q$ vs $\dim$.** The conjecture in §3.3 deliberately does not
   assert that quantum dimension equals Hilbert-space dimension at real
   $q_0 > 1$; conflating them silently would be a category error of the
   c_k-flip-flop type (fibre vs archimedean level).
4. **Provenance.** Reviews in §1 are from model knowledge; postulate
   wordings are paraphrases pending the PDF fetch. Do not quote §1 as if
   verified against the papers.

## 6. Follow-ups (not in this tranche)

1. Fetch the 5 PDFs on a normal-network machine (`gen-bib-papers-list.py`
   picks up the four registered refs); identify 1810.11563 and register it.
2. Promote the §3.3 conjecture to a `conjecture` content block
   (`conj:bh-state-counting`) in `information-theory/` or
   `gravity-spacetime/`, with a §3b class axiomatisation.
3. Promote §3.2 witness completeness to `conj:witness-completeness` and
   decide the corpus position: keep Gödel-hiding (and re-scope the
   hawking-radiation sentence) or adopt exterior unitarity.
4. Add `interprets`-linked remark connecting
   [`observable-beable-correspondence`](../../content/quantum-observable-universe/information-theory/observable-beable-correspondence.md)
   to standard complementarity (the 't Hooft lineage the author flagged).
