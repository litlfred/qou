# SM-derivation literature analysis → bean workplan

**Date:** 2026-07-31
**Branch:** `claude/standard-model-categorical-gauge-7vj44m` (PR #4419)
**Trigger:** Owner uploaded 11 papers (`library/`, main commit `5d1385d1`) and
directed: "analyze lit and work on beans."
**Scope:** Per-paper analysis of the uploaded Standard-Model literature, mapped
onto the appendix-standard-model gap beans. No paper below closes any bean;
each names a concrete attack route. All routes remain gated by the anti-fit /
anti-laundering discipline.

---

## 1. Bilson-Thompson 2005 (`hep-ph/0503213`) — helon model

**Claims.** First-generation SM fermions and EW bosons are framed 3-braids
("helons" = ribbon pairs). Key mechanisms:

- **Electric charge = ribbon TWIST**: a twist through $\pm 2\pi$ on a ribbon
  carries charge $\pm e/3$; charge quantisation in units of $e/3$ is the
  pairing constraint (twists combine mod $2\pi$).
- **Colour = strand permutation**: the odd-man-out position among the three
  strands gives the three QCD colours; leptons are the permutation-invariant
  triplets.
- **Bosons = identity-permutation triplets** ($\gamma, W^\pm, Z^0$ unbraided);
  $Z^0$/$\gamma$ related by deforming counter-twisted ↔ untwisted helons
  (a Weinberg-mixing heuristic).
- **Generations = braiding pattern** on the neutral "framework": charge
  emission (a trivially-braided $W$) cannot change the braiding, so charged
  leptons decay to same-generation neutrinos — a structural GIM-like rule.
- **$\nu/\bar\nu$ single-handedness** is forced by a double-counting argument.

**Bean impact.**

- **`qou-q377` (hypercharge second invariant) — PRIMARY HIT.** The framework's
  2026-06-02 audit concluded the missing object for $Y$ is a *second crossing
  invariant independent of the writhe*. The helon model reads charge off
  **twist**, not crossings. On a framed link, twist and writhe are exactly the
  two independent components of the self-linking number
  (Călugăreanu–White, $\mathrm{SL} = \mathrm{Tw} + \mathrm{Wr}$). QOU already
  uses $\mathrm{Wr}$ (→ $I_3$, derived; $Q = w/2$ via `def:coulomb-charge`).
  **Candidate:** take $\mathrm{Tw}$ (ribbon-framing twist) as the second
  $\mathrm{U}(1)$ generator and test the Gell-Mann–Nishijima consistency
  $Q = I_3 + Y/2$ against the framework's derived $Q$ and $I_3$ on the
  nucleon doublet and the light hadrons. This is a *candidate direction*, not
  a result: QOU braids are not currently framed/ribbon objects, so the first
  task is to define the framing data categorically (the ribbon structure of
  $\mathbf{Rep}(\mathrm{SU}_q(2))$ supplies a canonical twist $\theta$ — the
  ribbon twist $\theta_j = q^{j(j+1)}$ was already checked in the 2026-06-02
  audit and found to be a spin/Casimir ladder, NOT a charge ladder; the helon
  twist is *per-strand framing data*, a different object. Do not conflate.)
- **`qou-x4qm` (three generations).** Helon route: generation = braid-pattern
  class on the neutral framework. Suggests a QOU probe: classify the
  GS-normal-form classes of 3-braids at fixed permutation and charge data;
  does a natural 3-fold family appear? Open-outcome research; overlap
  permitted.
- **`qou-ni4b` (SU(3)).** Colour-as-permutation is only the $S_3$ shadow of
  colour; it does not produce the SU(3) *group action*. Matches QOU's existing
  position (colour = 3-strand structure). Not a closure route by itself.
- **Caution.** The helon model is a toy: no dynamics, no mass mechanism, no
  Hecke/derivation chain. Import its *mechanisms* as candidate structure, not
  its identifications (helon particle table ≠ QOU knot table; e.g. QOU photon
  = Hopf link $T(2,2)$, helon photon = untwisted unbraided triplet).

## 2. Bigelow 2001 (`math/0005038`) — braid groups are linear

**Claim.** Theorem 1.1: the Lawrence–Krammer representation of $B_n$ is
faithful for all $n$; per Lawrence's construction it is (at generic
parameters) a topologically-defined summand of the Jones representation.
Contrast: the Burau representation — the $(n-1)$-dimensional Hecke summand —
is **unfaithful** for $n \geq 5$ (Moody, Long–Paton, Bigelow).

**Bean impact — `conj:gauge-hecke-realization`.**

- **Supportive:** a faithful linear representation of $B_n$ living in the
  Jones-representation orbit exists. Faithful Hecke-tower realization of braid
  symmetry is not wishful — it is the *generic-parameter* situation.
- **Constraining:** (i) any realization argument must avoid factoring through
  Burau alone; (ii) faithfulness is a **generic-$q$** statement — it can fail
  at special parameter values, so the conjecture's real content at the
  substrate anchor is *faithfulness of the specialisation at* $q_0$;
  (iii) the conjecture is about automorphism monoids of the state groupoid,
  which are braid groups only after the groupoid is identified with a braid
  groupoid — that identification is part of the open work.
- Literature-context paragraph added to the block
  (`gauge-hecke-realization.md`, cites `bigelow2001`).

## 3. Baez–Huerta 2010 (`0904.1556`) — the algebra of GUTs

**Claims.** SM fermion content = specific representation of
$\mathrm{SU}(3){\times}\mathrm{SU}(2){\times}\mathrm{U}(1)$ satisfying the
hypercharge relations that make the $\mathbb{Z}_6$ quotient act trivially;
SU(5) embeds it in $\Lambda \mathbb{C}^5$ (hypercharge from the grading),
Spin(10) and Pati–Salam extend.

**Bean impact — `qou-q377` target spec.** Whatever second invariant QOU
proposes for $Y$ must reproduce the exact rational spectrum
$Y \in \{\pm 2, \pm 1, \pm 4/3, \pm 2/3, \pm 1/3, 0\}$ on the first
generation with the $\mathbb{Z}_6$ consistency (equivalently: the SU(5)
grading relations). This is the falsification battery for any twist-based
candidate from §1 — run it *before* wiring anything.

## 4. Tong 2017 (`1705.01853`) — line operators in the SM

**Claims.** The SM gauge group is $\tilde G/\Gamma$, $\Gamma \subseteq
\mathbb{Z}_6$, undetermined by current experiment; line-operator spectra and
theta-angle periodicities distinguish $\Gamma$.

**Bean impact.**

- **`conj:sm-gauge-truncation`:** the block's containment-not-isomorphism
  phrasing and $\mathbb{Z}_6$ caveat are exactly aligned with the literature;
  citation added (`tong2017`). A completed truncation derivation would have to
  *predict* $\Gamma$ — a sharper falsifiable output than the SM itself
  currently fixes.
- **`qou-y087` ($\theta_{\mathrm{QCD}}$):** theta periodicity depends on
  $\Gamma$; any framing-phase speculation must first fix $\Gamma$.

## 5. Dubois-Violette 2016 (`1604.01247`) + Furey 2016 (`1611.09182`) — algebra routes to SU(3)

**Claims.** DV: SU(3) colour from unimodularity + the exceptional Jordan
algebra $J_3(\mathbb{O})$; triality ↔ 3 generations; $\mathbb{O} \cong
\mathbb{C} \oplus \mathbb{C}^3$ ↔ quark-lepton symmetry. Furey: inside
$\mathbb{C} \otimes \mathbb{O}$, the stabilizer of a complex structure is
$\mathrm{SU}(3) \times \mathrm{U}(1)$ with correct electric charges generated
by a number operator.

**Bean impact — `qou-ni4b` (and `qou-x4qm`).** The corpus already carries
octonion fragments (`QOU/MathlibExt/OctonionSU3Stabilizer.lean`,
`OctonionSU3RankSix.lean`, `BringsSurface/ColourComplexStructure.lean`,
genus-4 octonion-recovery audit 2026-07-12). The literature route is:
octonion structure on the genus-4 substrate → complex structure → SU(3) as
stabilizer (Furey/DV), with triality as the generation candidate. Concrete
next Lean step for the bean: state (conjecture class, content-bearing) that
the colour-complex-structure stabilizer acts on the 3-strand state space —
connecting the existing `ColourComplexStructure` fragment to
`conj:sm-gauge-truncation`'s SU(3) factor. Do NOT claim the action exists;
the class states it, the fragments constrain it.

## 6. Hikami 2004 (`math/0403224`) — torus-knot colored Jones

Closed-form/difference-equation machinery for $J_N(T(p,q))$. Feeds the Higgs
RT route (level selection + invariant-to-mass formula, open frontiers of the
2026-05-24 SM-map audit §6). No bean yet; becomes relevant when the RT-route
ratio test (cheap, ~50 lines) is run.

## 7. Not analysed this pass

`0603022` (Bilson-Thompson–Markopoulou–Smolin; embeds §1 into LQG — same
mechanisms, different host), `1003.4485`, `0511710` (higher gauge theory —
formalisation background for the 2-group ledger row), `1808.08110` (DV part
II). Read on demand when the corresponding bean is picked up.

---

## Bean workplan (priority order)

1. **`qou-q377` — hypercharge.** (a) Define per-strand framing/twist data on
   QOU braid states categorically (ribbon structure ≠ per-strand framing —
   see §1 caution); (b) compute $\mathrm{Tw}$ on the nucleon doublet + light
   hadrons; (c) run the Gell-Mann–Nishijima + Baez–Huerta $Y$-spectrum
   battery (§3) as the falsification gate. Formalize-first: state the
   invariant's required properties as a Lean class before any numeric sweep.
2. **`qou-ni4b` — SU(3).** Connect `ColourComplexStructure` to a
   content-bearing stabilizer-action conjecture class (§5). No instance.
3. **`qou-x4qm` — generations.** Two independent candidate routes now on
   file (braid-pattern classes §1; triality §5) — record both in the bean,
   attack later.
4. **`qou-y087` — theta.** Blocked on $\Gamma$ (§4) and SU(3) (§5); park.
5. Remaining parameter beans (`qou-pvu4`, `qou-ha6c`, `qou-pj82`,
   `qou-5iaz`, `qou-z3x8`, `qou-qydm`, `qou-y0mq`): no new literature
   leverage this upload; unchanged.
