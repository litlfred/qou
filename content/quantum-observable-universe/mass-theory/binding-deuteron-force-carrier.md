**Conjecture (deuteron force-carrier identification).**
*The substrate-fixed force-carrier torus knot for the deuteron
binding ($A = 2$) is* $T(2, 3)$ *(the trefoil), with*
$\alpha_{\mathrm{shift}}(T(2, 3)) = 3 \cdot (2 - 1) = 3$.
*Consequently the deuteron pins the substrate-universal per-rep
Reeb coupling* $\rho_0 = B(D) / (m_e \cdot 3) \approx 1.451$
(*dimensionless, in units rad⁻¹ after carrying the* $14.7$ MeV/rad
*phase scale*).

## Phase-3 status — candidate identification

The audit table in
[`prop:binding-alpha-shift-extension`](#prop:binding-alpha-shift-extension)
records the Phase-3 candidates for the $A \ge 3$ light nuclei
($T, {}^{3}\mathrm{He}, {}^{4}\mathrm{He}$) but leaves the
deuteron's force-carrier knot as
"*$T(?, ?)$ — pinned by $\rho_0$ calibration*".  This block
proposes — and constructs the concrete
`BindingForceCarrierKnot` instance for — the candidate
$T_D := T(2, 3)$.

### Rationale

1. **Smallest non-trivial torus knot.**  $T(2, 3)$ is the trefoil,
   the minimum-pole-order column-rich irrep on a torus knot.  This
   matches the deuteron's role as the lightest $A \ge 2$ nucleus —
   the natural "ground state" of the per-rep Reeb-phase hierarchy.

2. **$\mathcal{B}_3$ braid-closure consistency.**  The binding-
   endomorphism analogy ([2026-05-28 audit](../../../docs/audits/2026-05-28-binding-endomorphism-analogy.md))
   closes the deuteron via $B = m_e \cdot \mathrm{Vol}(\mathcal{B}_3) \cdot \Delta\mathrm{tr}$
   to $+0.19\,\%$.  The 3-strand braid $\mathcal{B}_3$ has
   $T(2, 3)$ as its canonical boundary torus knot — the trefoil is
   the $(2, 3)$-cable of the core circle in $\mathcal{B}_3$'s Seifert
   fibre structure.  The per-rep Reeb-phase refinement
   ($B = m_e \cdot \rho_0 \cdot \alpha_{\mathrm{shift}}$) inherits this
   identification structurally.

3. **$\rho_0 \approx 14.7$ MeV/rad calibration.**  Per the
   `binding_rotation_phase_lead.py` probe, the deuteron's full
   Markov-weighted q-Reeb phase aggregation gives
   $\rho_{\mathrm{full}}(D) = 14.6673$ MeV/rad.  With
   $\alpha_{\mathrm{shift}} = 3$ and $m_e \approx 0.511$ MeV, the
   substrate coupling reads
   $\rho_0 = B(D) / (m_e \cdot 3) \approx 1.451$, consistent with
   the substrate-universal range targeted by the audit.

## Lean structure (§3b-cond)

The candidate identification is wired through three `def`
declarations and one `instance` declaration in
[`binding-deuteron-force-carrier.lean`](binding-deuteron-force-carrier.lean):

- `def deuteronP : ℕ → ℕ` — `(p_A) = (2)` at $A = 2$, sentinel $0$
  elsewhere.
- `def deuteronK : ℕ → ℕ` — `(k_A) = (3)` at $A = 2$, sentinel $0$
  elsewhere.
- `def deuteronAlphaShift : ℕ → ℕ` — `(α_shift_A) = (3)` at $A = 2$,
  sentinel $0$ elsewhere.
- `instance deuteronForceCarrierKnot : BindingForceCarrierKnot
  deuteronAlphaShift deuteronP deuteronK` — discharges the
  `matches_alpha_shift` field by case-split on $A = 2$, both
  branches closing by `simp` on the definitions.  **No** `sorry`.

The sentinel-$0$ convention for $A \ne 2$ keeps the instance closed
under `funext` without committing to the tritium / ${}^{3}\mathrm{He}$ /
${}^{4}\mathrm{He}$ identifications (those are handled in their own
blocks once authored).

## Remaining open math

This block is a **candidate** identification — *not* a derived
uniqueness theorem.  Proving that $T(2, 3)$ is the substrate's
unique choice (rather than one of several structurally-coherent
candidates such as $T(2, 4)$ or $T(3, 2)$) requires the per-nucleus
minimisation argument on $H_6(q)$'s Wedderburn block at the binding's
smallest non-trivial irrep — the same Hecke-trace minimisation
principle queued at
[`prop:meson-color-tube-uniqueness`](#prop:meson-color-tube-uniqueness)
for the meson force-carrier pair.

Closure path: lift the meson minimisation result to $H_{3A}(q)$ at
$A = 2$ (i.e. $H_6(q)$), and verify that the trefoil $T(2, 3)$
realises the minimum.  This is the same proof technique queued for
the $A \ge 3$ identifications — they all share the structural
machinery.

## Status

This conjecture is **conditional on the substrate-uniqueness leg**
of Phase 3 — the candidate identification $T(2, 3)$ is consistent
with all measured / proved structural data, and the Lean
`BindingForceCarrierKnot` instance is sorry-free for the candidate,
but the *substrate-uniqueness* of the choice awaits the
$H_6(q)$ Hecke-trace minimisation.

Progress on the Phase-3 backlog for
[`prop:binding-alpha-shift-extension`](#prop:binding-alpha-shift-extension):
deuteron candidate identified ($T(2, 3)$), tritium / ³He candidates
already noted in the audit table ($T(2, 5)$), ⁴He candidate already
noted ($T(3, 4)$).  All four $A \in \{2, 3, 4\}$ candidates now
have concrete `(p_A, k_A)` selectors awaiting substrate-uniqueness
proof.
