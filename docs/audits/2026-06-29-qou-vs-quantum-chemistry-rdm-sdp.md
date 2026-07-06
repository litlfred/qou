# Can QOU's compute framework accelerate chemistry? — RDM/SDP analysis

**Date:** 2026-06-29
**Status:** assessment + reproducible numerical demonstration
**Context:** A recurring (thrice-stalled) discussion asked whether QOU's
computational machinery (Hecke/Markov-trace core, Gröbner–Shirshov reducer,
crystal bases, Clarabel SDP, high-precision substrate) can (a) make chemical
computations more efficient, (b) enumerate reaction products / rule out
byproducts, or (c) predict which products form. This note records the verdict
and the evidence so the thread stops re-deriving the same conclusions.

This is a *critical-distance* assessment (per `AGENTS.md` §Critical-distance
license): the framework's claims are read adversarially. None of the negative
findings below bear on QOU's internal physics program; they concern only the
claim of a transferable advantage to quantum chemistry.

---

## 1. Two author corrections, conceded precisely

Earlier dismissals in the thread were too glib. Corrected:

### 1a. "Chemistry has no q" — wrong; conceded with scope

The substrate constant `q₀ ≈ 1.1097` is, in QOU's own logic, the fixer of the
energy scale of *all* interactions: `m_e` and `α` are derived from it, and
chemical energy scales (Hartree `= m_e c² α²`, bond energies `~ α² m_e c²`)
are built from `m_e` and `α`. So chemical energies **do** trace to `q₀`, exactly
as nuclear ones do — "knot-particle interaction at the substrate scale" is
internally consistent. The category error was the dismissal, not the claim.

**But** this concession buys **no computational shortcut.** Two distinct senses
of "q" must be kept apart:

- **q as a per-reaction tunable knob** — does not exist. `q₀` is a single fixed
  constant; there is no honest sense in which one "varies q to rule out a
  product."
- **q as the global energy-scale constant** — real, but the map
  `q₀ → specific bond/reaction energy` runs through the per-molecule electronic
  Hamiltonian, which is QMA-complete (§2). The hardness lives in *which*
  Hamiltonian (the molecule's combinatorial/quantum structure), not in `q₀`'s
  *value*. Knowing the substrate constant does not collapse the Hamiltonian.

### 1b. "Crystal bases enumerate byproducts — already in QOU"

There is a genuine, non-numerological bridge — but it is classical combinatorial
representation theory, and QOU's *specific* crystals do not generically apply:

- Byproduct enumeration = enumerate the integer-kernel fiber `{x ≥ 0 : Nx = b}`
  of the formula matrix `N`, connected by a **Markov basis** (Diaconis–Sturmfels);
  computing one = generators of a toric ideal = EXPSPACE in general.
- A **crystal graph `B(λ)`** is a Markov basis with the hard part done: Kashiwara
  operators `f̃_i` are a canonical move-set, the graph is connected by
  construction, and vertex weights = lattice points of string/GT polytopes.
  Connectivity is precisely the expensive part of Markov-basis computation.
- **Scope:** this fires only when the fiber carries the right structure — the
  transportation-polytope / contingency-table class (Kostka numbers, GT
  patterns), where `N` is totally unimodular / network-structured. For those,
  enumeration is *already* easy and SNF/HNF is overkill. A general chemical
  formula matrix is an arbitrary integer matrix, not in that class.
- QOU's crystals (§7b: `sl_n` folded to type B, KLR, Demazure) are tuned to the
  *physics* Cartan datum; they are not a drop-in lattice-enumeration toolkit.
  Using them requires the chemical lattice to carry those root systems — the
  unjustified step.

**Forward research question — resolved in §4:** is there a class of reactions
whose stoichiometric fiber is the weight space of a QOU-relevant crystal? Answer:
**no for generic chemistry** (missing-shape obstruction), **yes exactly for the
metathesis / double-displacement class** (independent cation+anion conservation →
type-A contingency-table crystal), but that class is already easy and the
q-deformation adds nothing. Full analysis + verified demo in §4.

---

## 2. QMA-completeness and why SDP does not dodge it

**QMA** is the quantum analogue of NP: a "yes" instance admits a quantum witness
that a poly-time quantum verifier accepts. The canonical complete problem is
**Local Hamiltonian** — decide whether the ground-state energy is `≤ a` or `≥ b`
with `b − a ≥ 1/poly` — proved QMA-complete by Kitaev (5-local; later 2-local,
then on a line). The **electronic-structure** Hamiltonian is QMA-complete
(Schuch–Verstraete 2009, which is also their proof that no universal efficient
DFT functional exists). Operationally: even a fault-tolerant quantum computer is
not believed to solve it in the worst case (`QMA ≠ BQP` is expected).

**"Why collapse the Hamiltonian? You have SDP."** Conceded — the naive
`diagonalize 2^N` framing is wrong. The ground-state energy of a 2-body
Hamiltonian is a *linear* functional of the two-particle reduced density matrix
`²D`:

> `E₀ = min_{²D N-representable} Tr(K ²D)`  — a linear objective over a convex set.

You never touch the `2^N` wavefunction. This is the **variational-2-RDM method**:

- **Coleman (1963)** — the variational principle above, and identification of
  *the* obstruction: **N-representability** (which `²D` arise from a genuine
  antisymmetric N-electron state). Deciding membership in this convex set is
  itself **QMA-complete** (Liu–Christandl–Verstraete 2007). The hardness moved
  from "diagonalize `2^N`" into "describe the feasible cone."
- **Garrod–Percus (1964)** — the tractable necessary conditions **D, Q, G**
  (2-positivity: particle, two-hole, particle–hole matrices each `⪰ 0`), giving
  an SDP whose minimum is a rigorous **lower bound**. **Erdahl (1978)** added
  T1, T2 (partial 3-positivity).
- **Mazziotti (2000s)** — the large-scale numerical method (boundary-point /
  augmented-Lagrangian SDP) that made it a working quantum-chemistry tool.

So SDP gives **bounds**, and the gap closes only by climbing the positivity
hierarchy at exponential cost — worst exactly in the strongly-correlated regime
where "which product forms" is decided. The grid/OPF analogy is apt: SDP
relaxation of optimal power flow is *often* tight; chemistry is the same
phenomenon, but the non-tight instances are the chemically decisive ones, and
the worst case is provably QMA-hard.

---

## 3. Reproducible demonstration

Scripts: [`2026-06-29-rdm-sdp-demo/rdm_demo.py`](2026-06-29-rdm-sdp-demo/rdm_demo.py)
and [`2026-06-29-rdm-sdp-demo/symmetry_blocks.py`](2026-06-29-rdm-sdp-demo/symmetry_blocks.py)
(standalone; need `numpy`, `cvxpy`, `scipy`). Test system: **4-site Hubbard ring
at half filling** (`N=4` electrons, `r=8` spin-orbitals) — the minimal case with
a real DQG gap. (2-electron systems such as H₂ are solved *exactly* by DQG, so
they would show no gap — a necessary caveat against using H₂ as the demo.)

### 3a. The DQG relaxation gap (D/Q/G maps verified vs exact operators to 1e-16)

| U/t | E_exact | E_DQG (lower bound) | gap | gap/\|E\| |
|----:|--------:|--------------------:|----:|--------:|
| 0   | −4.00000 | −4.00000 | 0.00000 | 0.00% |
| 1   | −3.34085 | −3.35494 | 0.01409 | 0.42% |
| 2   | −2.82843 | −2.86257 | 0.03414 | 1.21% |
| 4   | −2.10275 | −2.16497 | 0.06222 | 2.96% |
| 8   | −1.32023 | −1.40072 | 0.08049 | 6.10% |

DQG is **exact at U=0** and the gap **grows monotonically with correlation** —
tight where chemistry is easy, loose exactly where it is hard.

### 3b. Symmetry block-reduction of the 2-RDM SDP (`∧²ℂ⁸`, 28-dim)

Cost proxy = `Σ (block size)³` (interior-point scaling):

| Reduction | Block sizes | Max block | `Σ size³` |
|---|---|---:|---:|
| None | one 28×28 | 28 | 21 952 |
| **Abelian** (translation C₄ × Sz) — *standard, cheap* | `[4,4,4,4, 2,2,2,2, 1,1,1,1]` | 4 | 292 |
| **Non-abelian** (point group D₄ × spin SU(2)) | `[3, 2,2,2, 1,1,1]` | 3 | 54 |

Verified: spin sectors split as `∧²(ℂ⁴⊗ℂ²) = (Sym²ℂ⁴ ⊗ S=0) ⊕ (∧²ℂ⁴ ⊗ S=1)
= 10 ⊕ 18`; D₄ decomposition `Sym²ℂ⁴ = 3A₁⊕2B₁⊕B₂⊕2E`, `∧²ℂ⁴ = A₂⊕B₁⊕2E`.

**Finding:** abelian symmetry already does the heavy lifting (28 → max-block-4).
The further non-abelian win (292 → 54, 5.4×) is **entirely the SU(2) spin
Casimir**, not the point group — and **spin-adaptation (using S², not just Sz)
is already standard** in RDM quantum chemistry (Gidofalvi–Mazziotti,
van Aggelen S²-projected 2-RDM). So QOU's Wedderburn machinery would *reproduce*
the known spin-adaptation, not surpass it.

---

## 4. Forward question: which reaction class IS a QOU-relevant crystal?

§1b left an open, non-numerological question: is there a class of reactions
whose stoichiometric fiber is the weight space of a crystal, so that Kashiwara
operators give a free connected Markov basis? Resolved precisely.

**The obstruction (generic chemistry: NO).** A crystal `B(λ)` is "fixed *shape*
λ, varying *content*"; its weight space `B(λ)_μ` is "fixed shape AND fixed
content." Chemical conservation `Nx = b` fixes the **content/weight** μ (the
element budget) but supplies **no shape** (no root system). So a generic chemical
fiber, mapped to "words of content μ," is the *full* weight space
`⊕_λ K_{λμ} B(λ)_μ` — many highest-weight sources, no single connected crystal.
The Kashiwara structure that would help requires a shape, and distinguishable
molecules carry no non-abelian symmetry to supply one.

**The positive sub-case (metathesis / double-displacement: YES, exactly).** When
a reaction conserves cations and anions **independently** — double displacement,
ion exchange, salt metathesis — the fiber acquires the missing structure. A state
is a contingency table `T[i,j]` = moles of salt `(cation_i)(anion_j)`; the two
conservation laws are row sums (cation budget) and column sums (anion budget).
This is the transportation polytope = **type-A crystal of contingency tables**
(RSK / Danilov–Koshevoy), and:

- the **Markov basis is the 2×2 swap** `T[i,j]±1, T[k,l]±1, T[i,l]∓1, T[k,j]∓1`;
- each swap **is an elementary balanced metathesis** — e.g.
  `AgNO₃ + NaCl → AgCl + NaNO₃` (verified mass-balanced: every swap conserves
  both ion budgets);
- adjacent-row swaps are Bender–Knuth involutions realizing the type-A Kashiwara
  operators; the fiber is connected by them (Markov-basis property).

Verified ([`2026-06-29-rdm-sdp-demo/metathesis_crystal.py`](2026-06-29-rdm-sdp-demo/metathesis_crystal.py)):
the `r=c=[1,1,1]` fiber = 6 permutation matrices = `|Weyl(A₂)| = 3!`; the
`r=[2,1,1], c=[1,2,1]` fiber (7 tables) is connected by swaps and every swap is
mass-balanced.

**Caveat — present but not accelerating.** This class is exactly where the
formula matrix is totally unimodular, so enumeration is *already* easy (the 2×2
swaps are the whole basis; no Gröbner needed). The crystal **explains** the
tractability; it does not speed up an otherwise-hard problem. And QOU's
**q-deformation adds nothing**: the q-grading weights tables by a statistic
(`q^{inv}` / charge) with no chemical meaning. So the honest landing is: the
crystal/representation-theory connection to chemistry is **real but classical
(q=1) and confined to the already-easy metathesis class** — the same verdict as
§3, reached from the enumeration side rather than the energy side.

## 5. Verdict

**QOU's compute optimizations do not transfer to chemistry, for principled
(not incidental) reasons:**

- **Representation-theoretic block reduction** — at `q=1` (electrons are honest
  fermions; there is no `q` in the electronic Hamiltonian) the Hecke algebra
  collapses to `ℂ[S_N]`, the symmetric-group machinery chemistry already uses
  (unitary-group approach, spin-adaptation). The distinguishing `q ≠ 1` structure
  is unphysical for molecules. §3b confirms the only real lever (SU(2) spin) is
  already pulled.
- **High precision (50–65 dps)** — wasted; the relaxation gap (10⁻³–10⁻²)
  dwarfs floating-point error.
- **Gröbner–Shirshov** — wrong Gröbner (braid-word normal forms, not the
  moment/SOS or NPA polynomial hierarchies that appear in SDP).
- **Crystals** — the genuine enumeration bridge is classical and applies only to
  the TU/contingency-table class (§1b); QOU's physics-tuned crystals are not a
  drop-in.

**The one transferable item flows chemistry → QOU, not the reverse:** the
**boundary-point SDP solver** (Mazziotti; Malick–Povh–Rendl–Wiegele). Per
iteration it does only (i) a reusable linear solve in constraint space and (ii)
one eigendecomposition **per PSD block** for the cone projection — memory
`O(n²)` per block, no Hessian assembly. It scales far past interior-point
(Clarabel, which choked on the 4096-variable demo here and needed SCS) and
**composes with the Wedderburn block-reduction QOU already computes**. If QOU's
confinement/operator-selection SDP (`prop:operator-selection-lp`) ever hits scale
limits on larger Hecke blocks, this is the drop-in upgrade.

---

## References (literature)

- Kitaev, Shen, Vyalyi, *Classical and Quantum Computation* (2002) — Local
  Hamiltonian QMA-completeness.
- Schuch, Verstraete, *Nature Physics* **5**, 732 (2009) — electronic-structure
  QMA-completeness; DFT functional limitation.
- Liu, Christandl, Verstraete, *PRL* **98**, 110503 (2007) — N-representability
  is QMA-complete.
- Coleman, *Rev. Mod. Phys.* **35**, 668 (1963) — variational 2-RDM principle.
- Garrod, Percus, *J. Math. Phys.* **5**, 1756 (1964) — D, Q, G conditions.
- Mazziotti, *Phys. Rev. Lett.* **93**, 213001 (2004) — large-scale /
  boundary-point variational 2-RDM.
- Diaconis, Sturmfels, *Ann. Statist.* **26**, 363 (1998) — Markov bases / toric
  ideals for lattice fibers.
