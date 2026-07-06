# Organic-chemistry redo — audit & work plan (2026-06-08)

**Trigger.** Owner request: "redo organic chem now that more on mass and
binding has been proved; that chapter is VERY old." Primary goals: a
complete picture of **benzene**, including a **γγ pair-production
pathway**, a **shortest-production (GB/birthday) search**, the
**ring-closure binding**, and a comparison to the **n-hexane** route;
plus formalising **heat-as-probability / catalysis**. Standing
directives folded in: **fix all chemistry compute machinery** (expected
broken) and **remove all hardcoded constants** (witness-pin every
numeric literal).

Status: **audit complete; compute-fix + de-hardcode tranche queued.**
The compute/constants inventory (§8) is being filled by a background
sweep and will be appended.

---

## 1. Staleness signal is unreliable here — judge by method, not mtime

This working tree is a **shallow clone** (`git rev-parse --is-shallow-repository` → `true`; 50 commits visible). `benzene-ring.md`
has **2 commits in its entire visible history**; every block reports the
same `2026-06-07` mtime because that is the clone floor, not an authoring
date. **Conclusion: git timestamps cannot measure staleness.** A
file-mtime audit ("all recent, no staleness flags") is an artifact and
must be ignored. Currency is assessed by **which machinery a block
consumes** (Alexander-polynomial/links = old; universal-ILP/Wedderburn =
current).

## 2. There are TWO chemistry chapters, and they disagree

| | `content/quantum-observable-universe/organic-chemistry/` | `content/quantum-observable-universe/molecular-construction/` |
|---|---|---|
| Blocks | 21 | ~40 (H₂, CH₄, CO, CO₂, benzene, electron shells) |
| A covalent bond **is** | a **Hopf LINK** — `B_k = ⊕_k T(2,3)`, k shared trefoils ([`covalent-bond-types.md`](../../content/quantum-observable-universe/organic-chemistry/covalent-bond-types.md)) | a **KNOT** — inverse trefoil `T(2,3)⁻¹`; links **explicitly excluded** ([`ilp-covalent-bond.md`](../../content/quantum-observable-universe/molecular-construction/ilp-covalent-bond.md)) |
| Energy method | Alexander-polynomial weight differences | **universal ILP** + Wedderburn channels (sym/std/alt) |
| Energy scale | `(α² m_e/m_p)·|q+q⁻¹|_nuc` | `E_mol = m_e·α²/(q+q⁻¹)²` (= hartree/[2]_q²) |
| Wired to the proved canonical chain? | **No** | **Yes** — same LP as confinement (B₃) + gluon |
| Benzene model | T(2,6) threading link; barrier 193–386 kJ/mol | H₁₂₀(q) full braid (120 strands); π-system in H₆(q) |

**Headline finding.** The two chapters give **incompatible foundational
definitions of a covalent bond** (link vs knot), **two different energy
scales**, and **two benzene models**. "Redo organic chem" =
**reconcile them, retire the disconnected Alexander/link approach, and
re-anchor on the universal-ILP/Wedderburn chain** that is now proved.

## 3. Wiring status (correcting an earlier mis-call)

An earlier reading (from the nuclear-binding side) claimed
"covalent/electron binding is not wired." **That is wrong** —
`molecular-construction/` wires chemistry to the canonical machinery:

- The covalent-bond operator is selected by the **universal ILP**, *the
  same LP that derives confinement* `B₃` and the gluon `2σ₀` — same Gram
  matrix `G`, same Frobenius positivity constraint, same `tr_M`
  objective; only the state `x` changes
  ([`ilp-covalent-bond.md`](../../content/quantum-observable-universe/molecular-construction/ilp-covalent-bond.md)).
- The molecular energy scale is **derived from q₀ alone**:
  `E_mol = E_hartree/[2]_q² = m_e·α²_EM/(q+q⁻¹)²`.
- Validated, zero fitted parameters: **H₂ D₀ = 4.4834 eV vs 4.478
  observed (+0.1 %)**; **C–C D₀ = 3.21 eV vs 3.60 (−10.9 %)**.

So the chemical eV scale **exists and is anchored**. The corpus-grep
discipline (AGENTS.md) applies: do not declare chemistry energy "out of
reach" — it is partially closed and the gap is accuracy, not existence.

## 4. Bond order = LP-dual active-set (owner-confirmed direction)

`co-lp-dual-binding.md` already realises the owner's "is a triple bond
when the SDP gives a 3?" intuition:

- The **LP dual** of the CO braid selects bond order **k = 3** as
  optimal over k = 1, 2, with per-bond shadow prices `y₁, y₂, y₃`.
- At the triple-bond optimum **all three duals are active ⇒ active-set
  cardinality = 3 = bond order**.
- Observed CO `D₀ ≈ 11.09 eV` (strongest diatomic), consistent with the
  LP picking maximum feasible k.

**Caveat:** this is *conditional on* `conj:q-integer-mass-formula` — the
**integrality** of the LP optimum is conjectural, not proved. The
"active-set cardinality = integer bond order" claim needs the ILP
integrality result discharged.

## 5. What already exists for each owner goal — and the critique

| Owner goal | Where it lives | Verdict / critique |
|---|---|---|
| Triple-bond operator ("do we have it?") | `organic-chemistry/covalent-bond-types.md` (k-link), `molecular-construction/co-triple-bond-energy.md`, `co-lp-dual-binding.md` (LP picks k=3) | **Exists in both** — but as *link* (organic) vs *knot* (mol-constr). Reconcile. |
| Ring-closure binding ("hexene closure releases a lot") | `organic-chemistry/prop:ring-closure-barrier`, `rem:chain-ring-energy`, `prop:chain-ring-comparison` | Predicts the **activation barrier** (193–386 kJ/mol) via Alexander weight diff 5−3=2. **Weak test:** a factor-of-2-wide prediction band "matching" a factor-of-2-wide experimental band. Also conflates barrier with *resonance/release* energy. Uses the **disconnected** Alexander method. |
| SDP active-set = bond order | `co-lp-dual-binding.md` | **Confirmed**; integrality conjectural (§4). |
| Aromatic delocalization "donut" operator (the S₆ question) | combinatorics in `rem:organic-chain-taxonomy` (Hückel 4n+2); emergence in `molecular-construction/benzene-threading-emergence.md` | **Operator gap.** The explicit object is the **q-symmetrizer / Jones–Wenzl projector on H₆(q)**, cyclic-(C₆)-invariant, projecting the 6 π-electrons onto the symmetric Wedderburn block. Combinatorics present; explicit projector missing. |
| γγ pair-production pathway / shortest GB production | none in either chemistry chapter | **Genuinely new.** Template exists: `predicted-spectra/meson-to-proton-via-borromean.md` (3 parallel γγ → Borromean confine). |
| Heat-as-probability / catalysis / yield | none; hooks in `stochastic-mechanics/`, KL-decategorification (AGENTS.md §7b) | **New, most ambitious.** Home = Markov-trace-as-partition-function (Jones↔Potts/six-vertex); T via q or Boltzmann weight on birthday grading; catalyst = lowers peak-birthday of desired pathway. |

## 6. New content to add (beyond reconciliation)

1. **Aromatic delocalization operator** — explicit C₆-invariant
   Jones–Wenzl/q-symmetrizer on H₆(q); the categorical realization of
   the "donut" and of Hückel 4n+2.
2. **γγ → benzene assembly** — parallel-γγ creation story on the
   Borromean template, *plus* the physically-correct **thermal
   rearrangement** framing (3 acetylene braids → benzene), with the
   net-emission ledger `(NF-net_final − NF-net_initial)·𝔈₀`.
   Distinguish creation (matter from photons) from rearrangement
   (matter conserved). **Caution:** "shortest pathway" is *retrosynthesis*
   — non-unique; claim only "unique up to molecular symmetry,
   canonicalised by min-action SDP."
3. **n-hexane comparison** — ring-closure-keep-π (benzene) vs
   stay-open-saturate (hexane); the aromatic bonus = the T(2,6)/Jones–
   Wenzl object hexane lacks.
4. **Magic/shell active-set probe** — read active-set cardinality off
   the confinement SDP at closed shells; test it yields nuclear magic
   (2,8,20,28,50,82,126) and electron-shell (2,8,18,32) numbers.
5. **Heat/catalysis** (research leg) — one simple case
   (acetylene→benzene vs →hexane selectivity) via the partition-function
   reading; validate against real yields.

## 7. Decisions locked (owner)

- Bond order = **LP-dual optimal k / active-set cardinality**.
- **Reconcile** the two chapters; retire the disconnected Alexander/link
  approach where it conflicts with the ILP/Wedderburn chain.
- Staleness by **method**, not mtime.
- **No hardcoded constants** — every numeric literal witness-pinned.

## 8. Compute-fix + de-hardcode inventory (to be appended)

Pending the background sweep. Will list: every chemistry compute script
(incl. `_deprecated/benzene_resonance.py`, the `molecular-construction`
binding computes), whether each emits a witness and imports canonical
machinery (`pyhecke`, `pyhecke_native`, `lp_dual_solver`, `vol_density*`)
or rolls its own; the witness files and whether content references them;
and the **bare numeric literals** in both chapters' `.md` that must be
witness-pinned. LP/SDP computes must route through
`lp_dual_solver.py` and emit primal+dual fields per AGENTS.md.

---

*Audit author: agent session on `claude/affectionate-hopper-seYEv`.
Cross-refs: `meson-to-proton-via-borromean.md`, `magic-A-binding-formula.md`,
`docs/coordination/2026-06-05-step9-binding-closure.md`.*
