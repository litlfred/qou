**Conjecture (Rule 14 conditional adoption — owner authorised 2026-05-24).**
Under the Kashaev volume conjecture
([`conj:kashaev-volume-conjecture`](#conj:kashaev-volume-conjecture))
applied to an atomic Hecke element $T_w$ with `Markov closure` knot/link
$K_w$, the multiplicative density prefactor
$\rho_F \in \mathbb{Z}_{>0}$ in the binding-energy formula

$$
  B_{\mathrm{pred}}(K_w)
  \;=\;
  \rho_F \cdot m_e \cdot \mathrm{Vol}_{\mathrm{hyp}}(K_w)
$$

equals the **joint-tower SDP Wedderburn multiplicity** $\nu_{\mathrm{SDP}}(K_w)$
of the canonical Hecke element $T_w$'s saturating SDP solution in the
$H_{n}(q)$ Wedderburn decomposition:

$$
  \rho_F  \;=\;  \nu_{\mathrm{SDP}}(K_w)
$$

per [`atom-knot-mass-derivation`](#def:atom-knot-mass-derivation)
§Algorithm step 3 (the joint-tower SDP solve that produces
$\nu_{\mathrm{SDP}}$ as a non-negative integer multiplicity).

## Evidence (three confirmed atoms)

The numerical coincidence is exact on the three SDP-confirmed
hyperbolic atoms (per
[`atom-knot-mass-derivation`](#def:atom-knot-mass-derivation) line 265):

| Atom | $K_w$ | $\rho_F$ (legacy) | $\nu_{\mathrm{SDP}}$ |
|------|-------|-------------------|----------------------|
| ²H (D)  | knot $6_2$        | 1 | 1 |
| ³H (T)  | knot $8_{11}$     | 2 | 2 |
| ³He     | link $L_{6a4}$    | 2 | 2 |

The ⁴He case uses the magic $A \cdot 8G$ closure rule rather than a
census knot, so its $\nu_{\mathrm{SDP}}$ value is **extrapolated**
($\rho_F = 2$ assumed); R&D follow-up is to extend the joint-tower
SDP solver to confirm $\nu_{\mathrm{SDP}}(⁴\mathrm{He}) = 2$.

## Categorical home (driver x of the 13-driver menu)

This identity falls under driver (x) **MacMahon-style
partition-algebra identities** of the canonical-derivation menu
([`docs/audits/2026-05-23-lambda-scale-canonical-unification.md`](../../docs/audits/2026-05-23-lambda-scale-canonical-unification.md)).
The Wedderburn multiplicity of $T_w$'s SDP solution is a
partition-algebra count: it is the dimension of the saturating
projection in the irreducible-block decomposition
$H_n(q) \cong \bigoplus_{\lambda \vdash n} \mathrm{End}(V_\lambda)$.
The numerical coincidence with the Kashaev density factor pulls
$\rho_F$ onto driver (x) and removes it from the Rule-14 escalation
queue.

## Conditional structure

The conjecture is **conditional on the joint-tower SDP completeness**:
i.e. the joint-tower SDP solver in
[`r5_full_canonical_knot_solver.py`](../../folio-assistant/computations/r5_full_canonical_knot_solver.py)
(when it lands; R&D in progress) gives a unique non-negative integer
$\nu_{\mathrm{SDP}}(K_w)$ for every bound-state knot $K_w$. Until R5-full
SDP ships, the identity is verified on three census atoms and
extrapolated to ⁴He with explicit caveat. The Lean class axiomatises

```lean
class KashaevDensityEqualsSDPMultiplicity
    (M : Type*) [BrCategory M] [Hecke M] [KashaevVolumeConjecture M] where
  /-- The joint-tower SDP multiplicity ν_SDP(K_w) of the canonical
      Hecke element T_w's saturating SDP solution. -/
  nu_sdp : ∀ (K : Knot), ℕ
  /-- ν_SDP equals the Kashaev density prefactor ρ_F. -/
  identity :
    ∀ (K : Knot),
      kashaev_density_prefactor K = nu_sdp K
```

per CLAUDE.md §3b ("class is inhabited"); the only `sorry` is the
class instance, which closes when R5-full canonical knot solver
produces certified $\nu_{\mathrm{SDP}}$ values.

## Why this resolves the Rule-14 escalation

Pre-2026-05-24 the
[`mass_table_ppb.py`](../../folio-assistant/computations/mass_table_ppb.py)
script self-declared the density rule $\rho_F \in \{1, 2\}$ as
*"pending formal justification"* (line 23) — an open Rule-14
violation per the canonical-derivation discipline. With this
conjecture-conditional adoption, $\rho_F$ is:

1. **named canonically** (`nu_sdp` in the new code), connecting to the
   existing `ν_SDP` notation in
   [`atom-knot-mass-derivation`](#def:atom-knot-mass-derivation);
2. **placed on the 13-driver menu** (driver x, MacMahon partition algebra);
3. **conditional on a class** that R5-full SDP will eventually
   inhabit — replacing the open-ended "pending formal justification"
   with an auditable conjecture-conditional dependency.

Owner authorised this adoption per Rule-14 procedure
2026-05-24, in response to
[`docs/audits/2026-05-24-rule14-kashaev-density.md`](../../docs/audits/2026-05-24-rule14-kashaev-density.md)
§Recommendation.

## Notation hazard resolved

Prior to this block, three distinct quantities used the symbol $\rho$
in QOU compute and content (per
[`atom-knot-mass-derivation`](#def:atom-knot-mass-derivation) §Notation):

- $\nu_{\mathrm{SDP}}$ — integer Wedderburn multiplicity (this conjecture)
- $\rho_K$ — CODATA-fit density per knot
- $\rho_F$ — Kashaev prefactor in `mass_table_ppb.py` (unnamed, compute-only)

The renamed compute field (`rho_factor` → `nu_sdp` in
[`mass_table_ppb.py`](../../folio-assistant/computations/mass_table_ppb.py)
ATOM_ASSIGN) consolidates around the canonical $\nu_{\mathrm{SDP}}$ name,
removing the third unnamed $\rho$.

## Consumers

- [`mass_table_ppb.py`](../../folio-assistant/computations/mass_table_ppb.py)
  — ATOM_ASSIGN.`nu_sdp` field (renamed from `rho_factor` in the same
  PR that introduces this block)
- [`predict()`](../../folio-assistant/computations/mass_table_ppb.py)
  — reads `nu_sdp` and emits `B_pred = nu_sdp · m_e · Vol(K)`
- [`atom-knot-mass-derivation`](#def:atom-knot-mass-derivation)
  §Algorithm step 3 — supplies $\nu_{\mathrm{SDP}}$ via joint-tower SDP

## Open R&D

1. **Extend joint-tower SDP to ⁴He** — confirm
   $\nu_{\mathrm{SDP}}(⁴\mathrm{He}) = 2$ explicitly (currently
   extrapolated from D/T/³He pattern).
2. **Extend joint-tower SDP to ⁵Li, ⁶Li, ⁷Li** — the A∈{5,6,7} gap
   per
   [`docs/audits/2026-05-24-a5-a7-isotope-wiring-gap.md`](../../docs/audits/2026-05-24-a5-a7-isotope-wiring-gap.md)
   needs $\nu_{\mathrm{SDP}}$ values; the wider atom→knot census Rule-14
   escalation per
   [`docs/audits/2026-05-24-rule14-atom-knot-census.md`](../../docs/audits/2026-05-24-rule14-atom-knot-census.md)
   recommends waiting for R5-full SDP (owner-decided 2026-05-24).
3. **Extend joint-tower SDP to α-cluster atoms (⁸Be and up)** — the
   α-cluster rule inherits $\rho_F = 2$ from ⁴He; verifying
   $\nu_{\mathrm{SDP}} = 2$ across the α-cluster recursion would close
   the inheritance step.

## Cross-references

- Rule-14 escalation:
  [`docs/audits/2026-05-24-rule14-kashaev-density.md`](../../docs/audits/2026-05-24-rule14-kashaev-density.md)
- Sibling Rule-14 escalation (deferred to R5-full SDP):
  [`docs/audits/2026-05-24-rule14-atom-knot-census.md`](../../docs/audits/2026-05-24-rule14-atom-knot-census.md)
- 13-driver menu (driver x — MacMahon partition algebra):
  [`docs/audits/2026-05-23-lambda-scale-canonical-unification.md`](../../docs/audits/2026-05-23-lambda-scale-canonical-unification.md)
- Coordination ledger:
  [`docs/coordination/2026-05-24-post-1089-followups-ledger.md`](../../docs/coordination/2026-05-24-post-1089-followups-ledger.md)
- Underlying Kashaev volume conjecture:
  [`kashaev-volume-conjecture`](kashaev-volume-conjecture.md)
- $\nu_{\mathrm{SDP}}$ algorithmic definition:
  [`atom-knot-mass-derivation`](atom-knot-mass-derivation.md)
  §Algorithm step 3
