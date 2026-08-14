# G3 keystone ↔ Newton-polyhedra / q-difference-slope / Bessel–Askey — frontier consolidation (2026-08-11)

Consolidation of two threads that turn out to meet at the same irregular
q-difference connection. Written after a stale session (the 2026-07-13/14
alien-calculus ↔ surreal review and G3 tetrahedron-index scaffold, both
merged) returned to find the swarm far ahead. This maps the **current,
machine-checked frontier** so effort is directed at what is genuinely open
and unclaimed — not re-tread.

Verification basis for this pass: `grep`-confirmed sorry-status on the named
Lean files (0 real `sorry` tactics; the only "sorry" tokens are the words
"sorry-free" in docstrings) + a live run of the certified GGM probe. Full
`lake build` of the moved QOU package was not re-run this session (stale
cached oleans vs a ~5,200-commit-advanced main); claims below are scoped to
what was actually checked.

## 1. G3 keystone — the monodromy datum `z(q₀) → A_ω`

The keystone splits into existence / uniqueness / constructive (phib audit
§4). Current state:

| Leg | Status (2026-08-11) | Where |
|---|---|---|
| **Uniqueness** | **sorry-free, conditional-class** | `FaddeevPhiPhysical` (`QBeta/FaddeevPhiFullUniqueness.lean`) proves `faddeevPhi_uniqueUpToScalar` via `PhiBProdLociDensity.phiBProd_uniqueUpToScalar_of_normalForm`; the Liouville "doubly-periodic ⇒ constant" step is a proved lemma in `MathlibExt/DoublyPeriodicLiouville.lean` (no longer a carried hypothesis); `MonodromyDatumRigidity.lean`, `CyclicDilogPentagon.lean` (A-core) sorry-free. |
| **Constructive datum** | **GGM integer-3 certified** | `computations/probes/qbeta_g3_ggm_stokes_41.py` (runs green on main): Stokes matrix `S⁰=[[1,0],[−3,1]]`, `det W_m = 2` exact, q-difference eq (49) exact, descendant tower `S⁺₁₁ = 1−8q−9q²+…`, singularity at `ι = ±Vol(4₁)/π = ±0.64613`, substrate value `Σ_e I(0,e)(q_sub) = 0.4276442013` [13 d]. |
| **Existence** | heat-kernel / theta route (§4a) | open analytic target (G2/G0). |

**Takeover note (2026-08-11).** The A_ω leg's owning agent (bean `qou-vr3q`)
stalled — last A_ω commit 10 days prior (`caf115a24`), substantive work 3 weeks
prior. Owner authorised takeover. On takeover I verified the leg is worked to
its genuine research frontier; every tractable sub-step is already landed. The
current, accurate state:

- **`A_ω = 3` is LANDED as a certified DT/3d-index count, conditional on a
  published conjecture** (`mass-theory/aomega-fourone-dt-count.md`, Theorem
  conditional on `conj:stokes-dt-bps-bridge`; the value 3 comes only from the
  sorry-free decidable integer-matrix computation `QOU.QBeta.StokesQZeroDTCount`,
  eq-(60) `S⁺(0)=[[1,3],[0,1]]`; the bridge class asserts no value). This is the
  Volume-Conjecture-style Rule-14 adoption the owner directed 2026-08-02, and it
  passed the mandatory non-degeneracy gate on the **closed** GPPV/GGM state-integral
  BPS sector (the **open**-HOMFLY Gukov–Stošić sector gives `det(4₁)=5 ∉ {3,4}`
  and was correctly **rejected** — no degenerate class landed there).
- **The trace-field `disc(ℚ(√−3))=−3` shortcut is REFUTED** (superseding my
  earlier framing): reading GGM 2012.00062 directly, the 4₁ off-diagonal DT
  spectrum is the **pair `{3,4}`** (eq 98); the co-occurring `4` has no
  discriminant meaning, so a single-scalar discriminant identity cannot be "the
  DT invariant" (`2026-07-18-aomega-stokes3-is-dt-invariant-not-tracefield-disc.md`).
- **The scalar-symmetry-constant question is RESOLVED against a universal scalar**
  by the 5₂ cross-knot test (`FiveTwoDTSpectrumSplit.lean`, sorry-free;
  `2026-08-02-fivetwo-crossknot-34-resolution.md`): 5₂ is chiral, its 3×3 Stokes
  block splits `{3,4}` across chirality (`S⁺(0)` carries 4, `S⁻(0)` carries 3), so
  the literal 4₁ symmetry constant `(S₁₂+S₂₁)/S₁₁=3` is **not** a universal scalar.
  The real fork is *which spectrum member the observable inherits via chirality*,
  not scalar-vs-spectrum.

**The genuinely open piece — and why it is not closeable by a session.** What
remains is an *internal* combinatorial/categorical formula for the q→0 3d-index
DT count of a knot in terms of QOU Hecke/Bring data (Wedderburn multiplicities of
`H_n(q)`, Markov-trace, Bring embedding) reproducing `S⁺(0)₁₂=3` for 4₁ *and* the
companion `4` / surviving the 5₂ cross-knot test. Per
`2026-08-02-aomega-internal-derivation-symmetry-constant-target.md` §B this is an
**open problem in the categorification of DT / 3d-index invariants — open in the
DT/state-integral literature itself, not merely a QOU wiring gap.** Recomputing
the q→0 index "internally" via the QOU colored Jones / state integral *is*
re-importing GGM, not a categorical shortcut. Until such a formula exists, `A_ω=3`
is *certified as GGM's DT count* (imported, proven-for-4₁, conditionally adopted)
but **not internally derived** — and claiming a closure would violate the
anti-laundering rule. This is the honest terminus, not a to-do.

Superseded reductions worth recording so they are not re-opened: the abstract
`FaddeevPhi`-ratio route (beans `qou-cons`/`qou-rp5f`) hit a genuine wall — the
bare class carries no regularity field, so its solution set is closed under
multiplication by any doubly-periodic function (`faddeevPhi_mul_latticeIndicator`,
sorry-free). The uniqueness leg was instead closed through the **regularity-carrying**
`FaddeevPhiPhysical` (`hNF : MeromorphicNFOn Φ univ` + strip-growth), which is the
correct fix; the abstract-ratio beans are effectively superseded.

## 2. Newton-polyhedra / q-difference-slope / Bessel–Askey

The sibling thread the review asked about. It is real, largely landed, and
connects to G3 through the same irregular q-difference connection (the Newton
polygon of that connection is where "slope" lives).

| Item | Status | Where |
|---|---|---|
| **slope = q-Gevrey level (general k)** | **proved sorry-free** | `Mathlib/QGevreyOrder.lean` `slopeKCoeff_order`: for `L_k = z^kσ−1`, `2·log_q c_{jk}/(kj)² → 1/k` = order `1/k` = level `k` = Newton slope. Bean `qou-slvl` DONE 2026-08-08. |
| **q-difference kernel = prolongation symbol** | `validated` | `conj:qdifference-kernel-prolongation-symbol` (`QOU.Mass.QDifferenceKernelIsProlongationSymbol`). |
| **C1 ↔ GGM bar-parity faces** | `validated` | `conj:c1-ggm-bar-parity-faces` (`DoorVParityNoIdentity`). |
| **SL₂ period conserved quantity** | `validated` | `prop:sl2-period-conserved-quantity`. |
| **Jackson q-Bessel contiguity / recurrence** | Lean sibling exists, **`validation: not_checked`** | `prf:jackson-q-bessel-contiguity` (`qbessel_first_kind_coeff_closed_form`). |
| **q-Bessel 2nd-order q-difference equation** | Lean sibling exists, **`validation: not_checked`** | `prf:q-bessel-second-order-qdifference` (`qbessel_second_order_recurrence`). |
| **q-Bessel c_k recurrence (C-finite)** | Lean sibling exists, **`validation: not_checked`** | `prf:q-bessel-c-k-recurrence-cfinite` (`qbessel_coeff_closed_form`). |
| **RSZ general slope ↔ growth theorem** | **open (hard)** | Ramis–Sibuya–Zhang ch. 5; `qou-slvl` explicitly scopes the `L_k` family as *witnesses, not a proof of the general statement*. `RSZIsoformalInterface.lean`, `QGevreyTaming.lean`, `PolyhedralDomination.lean`, `DominationTowers.lean`, `KernelGrowthBound.lean` are the supporting infra. |

## 3. Genuinely open, unclaimed micro-targets (for direction)

1. **Three `not_checked` q-Bessel/Askey blocks** (§2 rows 5–7). Their Lean
   siblings exist but carry `validation: not_checked`; machine-validating the
   q-Bessel recurrences (or surfacing a gap) is bounded, on-topic, and appears
   unclaimed. This is the most concrete near-term item on the Bessel–Askey side.
2. **G3 step-3 residual — a *derivation*.** The Stokes-integer → odd-face-anchor
   map, via the trace-field `ℚ(ζ₁₂)` unification. Held by `qou-vr3q`; anti-fit
   gated (must derive, not match).
3. **RSZ general slope↔growth theorem** — the one hard-open piece of the
   Newton-slope thread; epic-scale Mathlib-gap infra (cf. `qou-08a2`).

## 4. Discipline notes

- No production wiring, no `c_k`/`A_ω` value claimed here; this is a status
  map. The GGM probe is audit-only and unchanged.
- The G3 uniqueness leg being sorry-free **conditional on `FaddeevPhiPhysical`**
  is the §3b-cond pattern, not a closed keystone: the class axioms
  (`MeromorphicNFOn`, strip-growth) are Lean-regularity carried inputs that the
  concrete `phiBProd` satisfies, not the physical bridge. "Sorry-free ≠ derived"
  still applies to the step-3 residual.
