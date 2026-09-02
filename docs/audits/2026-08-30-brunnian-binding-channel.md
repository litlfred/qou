# Why the binding multiplier is a coordination COUNT, not a linking number — the Brunnian channel

**Date:** 2026-08-30
**Arc:** bk-crossing mass-binding · **Bean:** `qou-brng` (the linking-vs-self-energy amplitude assignment — the open positive target)
**Lean:** `content/quantum-observable-universe/lean/QOU/Mass/BrunnianBindingChannel.lean` (sorry-free; lean-direct exit 0; axioms propext/Classical.choice/Quot.sound)
**Tier:** formalize-first — resolves the amplitude assignment's type question AND both sub-questions (up to two precisely-bounded residuals + the numerology-suspect saturation value; see below). No fit; no wiring.

## The question

`qou-brng` asks: in the arc's two multiplier laws at fixed hyperbolic volume,

    mass    m(K) = m_e · Vol(K) · lw / ℏ_q²      lw = (Σ_{λ⊢c+1} dim_q λ)/(c+1)   (q-dim SELF-trace)
    binding B(K) = m_e · Vol(K) · M              M  = coordination count z = A−1   (integer)

why is the binding multiplier the **integer coordination count M** while the mass multiplier is the
**q-dimension self-linking weight lw**? The bean names this "a categorical statement about linking
(mutual) vs self-energy (self-linking) amplitudes" and labels it the surviving route (the
volume-defect rival was refuted 2026-08-21).

## The corpus correction that reframed the attack

A six-path corpus check surfaced a fact that kills the naive reading and points at the right one.
The naive reading is "binding multiplier = the integer Gauss linking number of the assembly." That
is **wrong for the actual nuclei**:

- The ³He / ⁴He building-block carrier is the **Borromean link L6a4**, which is **Brunnian**: every
  *pairwise* Gauss linking number lk(Kᵢ,Kⱼ) is identically **zero** (remove any component and the
  rest fall apart). A multiplier read off pairwise linking numbers would be **0** for exactly these
  nuclei.
- The corpus already uses `M` as a **coordination / bond count** (graph degree z = A−1;
  `content/quantum-observable-universe/mass-theory/bk-coordination-multiplicity.md`, fit-free to
  <3% for the non-magic A=3 pair), NOT a linking number.
- The sibling em-linking thread proved the same obstruction from the field-theory side:
  `docs/audits/2026-08-01-em-linking-reads-round1.md` — O1 (Milnor μ̄₁₂₃ is totally antisymmetric,
  Khesin form-degree parity), and Round 3's decisive distinction between the **topological** pairing
  ⟨V₁,BS(V₂)⟩ (linking number, sign-changing, **zero** for Brunnian/unlinked tubes) and the
  **metric** pairing ⟨A₁,J₂⟩ (Coulomb-like, nonzero). Every pairwise *topological* term vanishes in
  the Brunnian baryon regime.

So the real question sharpens to: **why is the binding carrier an unsigned coordination count that
survives Brunnian vanishing, rather than a signed linking number that does not?**

## The resolution (proved half)

The already-proved crossing-energy channel decomposition (`QOU.Braiding.CrossingEnergy.decomposition`,
`content/quantum-observable-universe/knots-particles-confinement/crossing-energy.lean`) splits the
mutual crossing energy of a component pair with n₊ positive and n₋ negative inter-component
crossings into two channels:

    signed   (strong / cosh)   channel  =  ½(n₊ − n₋)(q + q⁻¹)      multiplicity n₊ − n₋ = 2·lk
    unsigned (Coulomb / sinh)  channel  =  ½(n₊ + n₋)(q − q⁻¹)      multiplicity n₊ + n₋

The signed multiplicity is the **writhe** n₊ − n₋ = 2·(Gauss linking number); the unsigned
multiplicity is the sign-blind crossing **count** n₊ + n₋.

`QOU.Mass.BrunnianBindingChannel` formalizes the Brunnian specialization that
`crossing-energy.lean` does not carry:

- **`brunnian_signedChannel_zero`** — a Brunnian pair has pairwise lk = 0, i.e. n₊ = n₋, so the
  signed (linking-number) channel is identically zero.
- **`brunnian_energy_is_count_channel`** — the entire mutual/binding energy is then carried by the
  unsigned count channel.
- **`brunnian_binding_survives`** — that channel is strictly positive for a crossing pair (m > 0) at
  a substrate modulus q > 1: **binding is nonzero even though the pairwise linking number is zero.**
- **`brunnian_channels_strict_mono`** — the two mutual invariants genuinely diverge: the signed
  channel stays flat at 0 as the crossing count grows, the unsigned channel strictly increases.

**Conclusion:** the binding carrier for a Brunnian nuclear link is forced to be the **unsigned
coordination count** (the sinh / Coulomb channel), because the signed linking-number channel is
empty. This is *why* the arc's `M` is a coordination count / graph degree and not a Gauss linking
number — the distinction is not cosmetic, it is forced by the Brunnian topology of the actual
carriers.

## Cross-thread convergence

This is the **discrete analogue** of the em-linking thread's independently-reached resolution. Round
4 of `2026-08-01-em-linking-reads-round1.md` concluded that the route around the Brunnian/O1
obstruction is *"an UNSIGNED quantity"* (Khesin Rmk 3.5, 3.6 — the asymptotic crossing number: the
Gauss integral with the *absolute value* of the numerator, symmetric, nonzero when lk = 0). The
crossing count n₊ + n₋ is exactly that unsigned object at the combinatorial level. Two unconnected
threads — a discrete crossing-energy split for nuclear binding, and a continuum flux-tube energy
bound for EM repulsion — land on the same unsigned invariant. (Caveat, kept honest: the em-linking
thread's own quantitative parameterisations of κ(A) were later retracted, Rounds 5–6; the surviving
*structural* point — unsigned, not signed — is what converges here, not any particular κ(A) fit.)

The deuteron (Hopf link, 2-body) is the consistency check at the boundary: there lk = 1 ≠ 0 and the
coordination count z = 1 also, so signed and unsigned channels agree. The two invariants coincide
for a Hopf-bonded pair and diverge only at A ≥ 3 (Brunnian), where the unsigned count is the correct
non-vanishing carrier.

## The two sub-questions — now proved (with a precisely-bounded residual)

The 2026-08-30 follow-up (`brunnian_*` lemmas + `content/…/mass-theory/brunnian-binding-channel.md`)
proves both sub-questions the type-resolution left open, up to one honestly-stated residual each.

**Sub-question 1 — the crossing count → coordination count map.** PROVED for the canonical carriers.
`minimal_brunnian_bond`: a minimal Brunnian bond (n₊ = n₋ = 1, the pairwise pattern inside L6a4)
has count-channel multiplicity ½(n₊+n₋) = 1 — one coordination unit per bonded pair.
`cluster_coordination_count`: a fully-bonded cluster then carries C(A,2) = A(A−1)/2 units, i.e.
per-nucleon z = A−1. *Residual:* the exact map beyond the minimal-bond model (pairs with n₊+n₋ > 2)
is not derived; which pairs bond is the coordination-graph question, saturation-limited for heavy A
(`QOU.Mass.CoordinationSaturation`).

**Sub-question 2 — bare integer vs q-dim self-trace.** PROVED as a bar-parity fact. Under the bar
involution q ↦ q⁻¹ the count (binding) channel is bar-ODD (`countChannel_barOdd`) while the mass
self-trace lw = (Σ_{λ⊢c+1} dim_q λ)/(c+1) is bar-EVEN — every quantum dimension is bar-even
(`quantumDim2_barEven`: [2]_q = q + q⁻¹). The two bar sectors are orthogonal
(`barEven_barOdd_eq_zero`: a function that is both vanishes), so a binding multiplier can never be a
mass multiplier (`binding_not_mass_sector`). The assignment is forced by parity, matching the
corpus cosh/sinh split (Q_β the bar-odd partner of the bar-even meson scale). *Residual:* the
*Hamiltonian-level* claim that rest mass **is** the closed self-trace and binding **is** the open
mutual pairing — the parity distinction is proved, its dynamical origin is not.

**Sub-question 3 (unchanged) — the exact saturation value ≈ ℏ_q².** The bean's 2026-08-21 verdict
stands: with the volume-defect route refuted this is **numerology-suspect**; not touched here, and
must not be forced.

## Verdict

The linking-vs-self-energy assignment is resolved and machine-checked: the binding carrier is the
unsigned coordination count (Brunnian channel), the mass carrier is the bar-even q-dim self-trace,
the two are bar-orthogonal, and the minimal-bond count → z=A−1 map is proved — reconciled with the
Brunnian obstruction and cross-validated by the em-linking sibling thread's independently-reached
unsigned-invariant route. Two precisely-bounded residuals remain (the >minimal-bond coefficient and
the Hamiltonian origin of the mass=self/binding=mutual identification), plus the untouched
numerology-suspect ℏ_q² saturation value. Those are the surviving `qou-brng` kernel.
